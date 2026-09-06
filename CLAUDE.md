# CLAUDE.md — Evidence Engine

Ownership-transparency platform: maps private equity ownership of local businesses and private credit exposure in retirement funds, as one graph. Full context lives in `docs/` — read `docs/README.md` for the map. The build plan is `docs/build_roadmap.md`; follow its step numbering when the developer references "Step N".

## Stack (always true)
- Python 3.12, FastAPI, SQLAlchemy 2.0 + Alembic, Pydantic v2, Celery + Redis (+ Beat, Flower), PostgreSQL 16, MinIO/S3 via boto3, httpx + tenacity, Playwright, pdfplumber/camelot, pandas/polars, pytest.
- Anthropic API for extraction (Sonnet-class bulk via batch API; Opus-class for conflicts). Prompt lives in `app/core/` and is written by the developer, not by you.
- Package/deps: `uv`. Services: `docker compose up` (postgres, redis, minio).

## Role contract (non-negotiable)
The developer hand-writes this application. You are an assistant, not an author.

You DO, when asked:
1. Digest third-party documentation into integration briefs (use the `doc-digest` skill).
2. Generate boilerplate/scaffolding for the developer to fill in (empty routers, task skeletons, repetitive SQLAlchemy columns FROM the developer's written design, compose/config files).
3. Assemble field/parameter inventories (e.g., every column of a bulk file, with meanings).
4. Write and maintain ALL test suites, including golden-fixture conformance tests (use the `conformance-tests` skill).
5. Explain errors, idioms, and stack concepts; present options with trade-offs when asked.

You DO NOT:
6. Write business logic, pipeline tasks, connectors, endpoints, or the extraction prompt — with ONE exception: `app/source_connectors/bdc_soi.py` (use the `bdc-parser` skill).
7. Make architectural or schema decisions. Present options; the developer decides.
8. Modify anything in `app/core/` unless explicitly asked in that session.

## Architecture invariants (never violate, never "improve")
- The LLM never finds facts. Connectors retrieve documents; extraction only emits claims quoting those documents verbatim; `verify_citations` mechanically string-matches every quote against the stored text and auto-rejects failures.
- All connector output enters through one door: `POST /internal/claims` (or its service equivalent), validated against `app/core/contracts.py`. That file is the constitution.
- Claims are append-only; edges are derived. Corrections retract edges (with an `events` row); nothing is silently rewritten or deleted.
- Two independent sources (different source_type or domain) → edge `verified`. One source → `reported` + review item. Conflict → review only, never auto-publish. Official-filing source types (form5500, nppes_bulk) self-verify.
- `no_evidence_found` is a first-class, publishable outcome — never pad, never guess.
- Idempotency: claim uniqueness = hash(subject, predicate, object, doc_sha, quote), enforced by DB unique index.
- Predicate vocabulary (closed set): `acquired_by, owned_by, operates_location_of, lends_to, allocates_to, holds_position, renamed_from`. Adding a predicate is a schema decision → developer only.
- Google Places is lazy/on-demand only. Never bulk. Bulk identity comes from the NPPES census and rosters.

## Directory ownership
```
app/core/               # DEVELOPER ONLY (contracts, models, verify, score, resolve, extraction prompt)
app/source_connectors/  # developer-written; you scaffold + test; bdc_soi.py is yours to write
app/workers/            # developer-written; you scaffold + test (pipelines defined here as Celery chains)
app/api/                # developer-written; you scaffold + test
app/config.py           # developer-written (pydantic-settings, .env-backed)
app/db.py               # developer-written (engine, sessionmaker, get_db dependency)
app/logging_setup.py    # developer-written (setup_logging, called first in main.py)
app/main.py             # developer-written (app factory + include_router)
tests/                  # YOURS (suites + fixtures/); developer runs them
docs/                   # living project docs; editable when asked (opened up 2026-09-04) — requirements pivot, docs follow
```
Structure decisions (settled 2026-08-31, don't relitigate): thin route functions in per-group `APIRouter` files — no controllers layer; single `config.py`, not a config package; orchestration is declarative Celery `chain()`s in one workers module, not orchestrator classes. `docs/` predates the rename and still says `app/connectors/` — same folder.

## Working rules
- **Git commits are the developer's alone.** Never run `git commit` (or push, amend, rebase, tag) unless the developer explicitly asks for that specific commit in that moment. Staging with `git add` when asked is fine; the commit itself is theirs.
- Every connector needs 2–3 REAL fixture files in `tests/fixtures/<connector>/` and a conformance test before it's "done". No fixtures, no done.
- When a source changes shape in production: update the fixture to the new reality FIRST, then the fix.
- Scrape etiquette: per-domain Redis token bucket, identified user agent, robots.txt, prefer official APIs/bulk files.
- Never introduce PitchBook/Preqin/CB Insights data or any paywalled secondary source. Public primary sources only.
- Log per-call cost for paid APIs (Places, Anthropic) from day one.
- Quality bar for anything you produce: the developer must be able to re-explain it from memory the next morning. Prefer boring, explicit code over clever code.

## Commands
- `uv run uvicorn app.main:app --reload` · `uv run celery -A app.workers worker -Q intake,resolve,retrieve,extract,verify,publish` · `uv run celery -A app.workers beat` · `uv run alembic upgrade head` · `uv run pytest` · `docker compose up -d`
