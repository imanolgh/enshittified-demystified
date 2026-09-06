# Architecture Study Notes — Laravel → FastAPI Mapping & Open Structure Proposals

Study material for the Evidence Engine project (FastAPI, SQLAlchemy 2.0, Alembic, Pydantic v2, Celery). Captures two Q&A exchanges between the developer (Laravel background) and Claude Code, verbatim in substance, so the trade-offs can be studied before a final structure decision. The proposals in Part 2 are **undecided** — nothing has been changed on disk.

---

## Background: structure already settled (for context)

These were decided earlier and are recorded in CLAUDE.md; the discussion below builds on them.

- **No controllers layer.** Thin route functions in per-group `APIRouter` files under `app/api/`, registered in `main.py`. FastAPI handles what Laravel controllers did: validation via the Pydantic parameter model (auto-422), response shaping via `response_model=`, DI via `Depends()`. Route bodies are 3–8 lines: call service, return.
- **Layers:** `app/api/` (thin routes) → `app/core/` (domain services: contracts, models, verify, score, resolve — developer-only) · `app/source_connectors/` (one module per external source; fetch → `RawDocument`, no DB writes, no queuing) · `app/workers/` (Celery tasks + declarative `chain()` pipelines in one module; tasks stay dumb).
- **Ingestion is pipeline-driven, not HTTP-driven.** Celery Beat schedules → chains → tasks → connectors. An API route may enqueue a run and return 202, but the request is not the unit of work; the document is.
- **Singles, not folders:** `app/config.py` (pydantic-settings, .env-backed), `app/db.py` (engine, sessionmaker, `get_db()`), `app/logging_setup.py`, `app/main.py`.

---

# Part 1 — Developer question: models, validation, and migrations across the two stacks

**Developer asked:** "With Laravel models, those did not define request and response structures and validation rules, right? How do Laravel models differ from Pydantic and SQLAlchemy models? How do FastAPI database schemas compare to Laravel migrations? And how do Alembic migrations compare to Laravel models/migrations?"

## The big-picture mapping

Correct premise: Laravel models never defined request/response structures or validation. The new stack has **two model families** doing what Laravel spread across three or four concepts:

| Laravel | This stack | Job |
|---|---|---|
| FormRequest / `$request->validate()` | **Pydantic model** (request side) | Validate incoming data |
| API Resource | **Pydantic model** (via `response_model=`) | Shape outgoing data |
| Eloquent model | **SQLAlchemy model** | Represent a DB table, query it |
| Migration files | **Alembic revision files** | Change the schema over time |
| — (no equivalent) | **Alembic autogenerate** | Diff models vs. DB to draft migrations |

- **Pydantic models** live at the *boundaries* — HTTP in, HTTP out, LLM output in. Validation and serialization. `app/core/contracts.py` (roadmap Step 1) is all Pydantic.
- **SQLAlchemy models** live at the *database* — one class per table. `app/core/models.py` (Step 2) is all SQLAlchemy.
- The two families are never mixed.

## Eloquent vs. SQLAlchemy models

Same job, opposite philosophies:

**Eloquent is implicit.** The model class is nearly empty; columns aren't declared in it. Eloquent discovers them from the live database at runtime (`$practice->name` works because the DB says so). Validation is not the model's job; types are whatever the DB returns plus `$casts`.

**SQLAlchemy 2.0 is explicit.** Every column is declared in the class with its Python type:

```python
class Entity(Base):
    __tablename__ = "entities"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    entity_type: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    aliases: Mapped[list["EntityAlias"]] = relationship(back_populates="entity")
```

The class *is* the schema definition, readable without opening the database. Column typos fail at import time; editors autocomplete columns. The cost is verbosity.

Two further behavioral differences:

1. **Active Record vs. Unit of Work.** Eloquent: `$model->save()` — each object persists itself immediately. SQLAlchemy: objects are `session.add()`-ed and nothing hits the DB until `flush()`/`commit()` — the session batches a unit of work into one transaction. This is why `get_db()` yielding one session per request matters: one request = one transactional unit.
2. **Neither validates.** A SQLAlchemy model will hold garbage until a DB constraint rejects it, same as Eloquent. Validation is always Pydantic's job, at the boundary, before data reaches a SQLAlchemy model.

## Migrations: Laravel vs. Alembic

Clarification first: there is no separate "FastAPI database schema" — FastAPI knows nothing about databases. The schema lives in exactly two places: SQLAlchemy models (the *intended* schema) and the Alembic migration chain (how the real DB *gets there*).

**What's the same:** versioned files, each with upgrade and rollback (`up()`/`down()` ≈ `upgrade()`/`downgrade()`), applied in order, tracked in a DB table (`migrations` ≈ `alembic_version`). `php artisan migrate` ≈ `uv run alembic upgrade head`.

**The key workflow inversion:**

- **Laravel:** the migration is the hand-written source of truth (`$table->string('name')`); the model never mentions the column. Schema truth lives in the migration pile.
- **Alembic:** the *model* is the source of truth. Edit the SQLAlchemy model first, run `alembic revision --autogenerate`, and Alembic diffs models against the live DB and drafts the migration for you. The migration is derived output, not authored input.

Loop: Laravel = *migration → DB → model discovers it*. This stack = *model → autogenerate → review → upgrade*.

Consequences:

1. The current schema is readable in one place (`models.py`) instead of mentally replaying a stack of migration files.
2. **Autogenerate is a draft, not gospel.** It misses things (renames appear as drop+add; server defaults and some index changes get skipped). Hence the roadmap's bolded rule: **read the generated migration** before `upgrade head`. Non-negotiable.

Structural note: Laravel migrations are ordered by timestamp; Alembic revisions form a linked chain (each file names its `down_revision` parent). Same day-to-day effect, but merging branches produces an explicit "merge revision" in Alembic rather than silent timestamp ordering.

## One request, end to end (the "validate at the boundary" pattern)

```
request JSON
  → Pydantic model validates (or auto-422)                [FormRequest]
  → route calls service with clean typed data
  → service builds/queries SQLAlchemy models in session   [Eloquent]
  → commit
  → return filtered through response_model Pydantic       [API Resource]
  → response JSON
```

Pydantic guards every edge (HTTP in, LLM out, API out); SQLAlchemy owns persistence in the middle; Alembic keeps the real database matching what `models.py` claims.

---

# Part 2 — Developer proposal: `database/` folder and `pydantic_models/` under `api/` (UNDECIDED)

**Developer proposed (opinion requested, no changes made):**

1. A `database/` folder containing the current `db.py` content as a setup file, plus two subfolders — one for Alembic migrations, one for SQLAlchemy models.
2. A `pydantic_models/` folder at the root of the `api/` folder — reasoning: these Pydantic models affect API routes that hit `core/` or `source_connectors/` directly, so they should sit at the API root level.
3. Within `pydantic_models/`, two subfolders: `requests/` and `responses/`.

## Claude's assessment of the `database/` folder

The instinct traces to Laravel's root `database/` folder (`migrations/`, `seeders/`, `factories/`). But note what Laravel *doesn't* put there: models. Eloquent models live in `app/Models`. Laravel itself decided migrations and models are different kinds of things — migrations are tooling artifacts about *change over time*; models are live application code imported daily. The proposal groups them because both say "database," but they have different audiences, change rates, and owners.

Concrete issues, descending weight:

1. **Moving SQLAlchemy models out of `core/` breaks the ownership map.** `app/core/models.py` is where the roadmap (Step 2) and CLAUDE.md place them — inside the developer-only constitution zone, next to `contracts.py`, `verify.py`, `score.py`, because the models *are* the domain. A `database/models/` folder relocates a settled artifact to make a category label line up. Categorizing by *kind of thing* rather than *domain role* is the same instinct that produced the controllers question, resolved the same direction each time.
2. **Alembic lives at repo root by tooling convention.** Migrations are not application code — nothing in `app/` imports them; only the `alembic` CLI reads them via `alembic.ini`'s `script_location`. Moving is possible but reconfigures against the default every Alembic doc assumes, for zero functional gain. Directly analogous to Laravel's root-level `database/migrations`, which nobody moves into `app/`.
3. **What remains for the folder is `db.py` — ~25 lines.** A package holding one small setup file is structure without content.

**Where the instinct does have a future:** when `core/models.py` outgrows one file (~8 tables will get there), the natural split is `app/core/models/` as a subpackage — grouping happens *inside* core, ownership intact. That is the endorsable version of the idea, when file size demands it.

## Claude's assessment of `pydantic_models/` under `api/`

Stronger pushback — this one has a real architectural cost: **it points the dependency arrow the wrong way.**

The premise is that Pydantic models exist to serve API routes. But `contracts.py` actually contains: `RawDocument` (emitted by connectors, consumed by workers), `ExtractedClaim` (validates *LLM output* inside a Celery task), `ResolvedEntity` (resolution result). Most never touch HTTP. They are contracts of the *pipeline*, which runs on Beat schedules with no request in sight. If they live under `app/api/`, then `source_connectors/`, `workers/`, and `core/` all import from the web layer — the domain depends on the delivery mechanism. Standard layering everywhere (FastAPI, Laravel, anywhere) runs the other way: `api` imports from `core`, never the reverse. Same lesson as the earlier `EDGARIngestionController` discussion in a different coat: the request is not the center of this app; the document is.

**The defensible version:** schemas that are *genuinely HTTP-only* — query-param models, pagination envelopes, a 202-enqueued response — can live in `app/api/` next to their routers (a `schemas.py` per route group, or a small `api/schemas/` package). Real, common pattern. The dividing rule: **if only routers import it, it can live in `api/`; if the pipeline touches it, it belongs in `core/contracts.py`.** The roadmap deliberately puts even `ClaimCardOut`/`EdgeOut` in contracts.py — the claim card's shape is product, part of the constitution, not incidental API plumbing.

## Claude's assessment of the `requests/`/`responses/` split

Mild pushback, practical grounds. It mirrors Laravel's `Http/Requests` vs. `Resources`, but that split existed because those were *different base classes with different mechanics*. In Pydantic both directions are the same kind of object, and many schemas serve both (a `ClaimIn`/`ClaimOut` differing by two fields, or one model used verbatim both ways). A direction-based split scatters one resource across two folders and forces a "which folder?" decision for every dual-use model.

**Convention that ages better: group by resource, suffix by direction** — `schemas/claims.py` holding `ClaimIn`, `ClaimCardOut`; `schemas/entities.py` holding `EntityOut`, `GraphOut`. When editing an endpoint, its input and output shapes sit side by side, where they're actually wanted.

## Claude's summary position (developer decides)

- `database/` folder: **don't** — keep `db.py` top-level, Alembic at root, models in `core/`; when models outgrow one file, split within core as `core/models/`.
- Domain contracts under `api/`: **no** — dependency direction; they stay in `core/contracts.py`.
- HTTP-only schemas near routers: **yes, legitimate** — per-group `schemas` modules inside `api/` when Step 3+ creates the need.
- Requests/responses split: **prefer grouping by resource** with In/Out suffixes.

Weighting note: two of these points (models in core, contracts as constitution) also carry weight from the project's settled docs (roadmap Step 1–2, CLAUDE.md ownership map). Final call is the developer's.
