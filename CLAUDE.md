# CLAUDE.md — Evidence Engine

Ownership-transparency platform: maps private equity ownership of local businesses and private credit exposure in retirement funds, as one graph. Full context lives in `docs/` — read `docs/README.md` for the map. The build plan is being replaced (2026-10-26): grill sessions settle every open item, then a wayfinder spec drives the build. Until that spec exists, "Step N" still resolves to `docs/build_roadmap.md`.

## Stack (always true)
- Python 3.12, FastAPI, SQLAlchemy 2.0 + Alembic, Pydantic v2, Celery + Redis (+ Beat, Flower), PostgreSQL 16, MinIO/S3 via boto3, httpx + tenacity, Playwright, pdfplumber/camelot, pandas/polars, pytest.
- Anthropic API for extraction (Sonnet-class bulk via batch API; Opus-class for conflicts). Prompt lives in `app/core/`; Claude drafts it, the developer approves it, golden-fixture tests check it.
- Package/deps: `uv`. Services: `docker compose up` (postgres, redis, minio).

## Role contract (non-negotiable; rewritten 2026-10-26)
Claude writes all of the code, from the spec. The developer decides; Claude builds.

The developer DECIDES — through grill sessions or wayfinder tickets — every:
1. Architectural, schema, and vocabulary question (tables, columns, statuses, predicates, enums, source types).
2. Product-behavior question (what publishes, how it's labeled, what counts as evidence).
3. Approval of the extraction prompt.

Claude BUILDS: application code, connectors, pipeline tasks, endpoints, migrations, the extraction prompt draft, and all test suites — from decisions already recorded in `docs/` or the spec.

Claude never makes a decision on its own. When a build hits a question the docs/spec don't answer, stop and put it to the developer (options + a recommendation); never pick silently and never "improve" a recorded decision.

## Architecture invariants (never violate, never "improve")
- The LLM never finds facts. Connectors retrieve documents; extraction only emits claims quoting those documents verbatim; `verify_citations` mechanically string-matches every quote against the stored text and auto-rejects failures.
- All connector output enters through one door: `POST /internal/claims` (or its service equivalent), validated against `app/core/contracts.py`. That file is the constitution.
- Claims are append-only; edges are derived. Corrections retract edges (with an `events` row); nothing is silently rewritten or deleted.
- Two independent sources (different source_type or domain) → edge `verified`. One non-official source → `reported`, labeled as such. Conflict → never published as fact; shown as "sources disagree". Official-filing source types (`nppes, form5500, form_adv, sec_filing, irs_exempt_org, sos, license_board, cafr`) self-verify; one source type per publisher, never per fetch method (docs/adr/0003). **No manual review anywhere** — every classification and publication decision is automated (docs/adr/0002).
- Ownership categories are computed by code from each owner's `OwnerKind` and the business's ownership chains; the LLM never classifies them (docs/adr/0001). Vocabulary: `GLOSSARY.md`.
- `no_evidence_found` is a first-class, publishable outcome — never pad, never guess.
- Idempotency: claim uniqueness = hash(subject, predicate, object, doc_sha, quote), enforced by DB unique index.
- Predicate vocabulary (closed set): `acquired_by, owned_by, operates_location_of, lends_to, allocates_to, holds_position, renamed_from`. Adding a predicate is a schema decision → developer only.
- Google Places is lazy/on-demand only. Never bulk. Bulk identity comes from the NPPES census and rosters.

## Directory layout
```
app/core/               # contracts (the constitution), models, verify, score, resolve, extraction prompt
app/source_connectors/  # one module per source (bdc_soi.py: see the bdc-parser skill)
app/workers/            # pipelines defined here as Celery chains
app/api/                # per-group APIRouter files
app/config.py           # pydantic-settings, .env-backed
app/db.py               # engine, sessionmaker, get_db dependency
app/logging_setup.py    # setup_logging, called first in main.py
app/main.py             # app factory + include_router
tests/                  # suites + fixtures/
docs/                   # living project docs; requirements pivot, docs follow
```
Structure decisions (settled 2026-08-31, don't relitigate): thin route functions in per-group `APIRouter` files — no controllers layer; single `config.py`, not a config package; orchestration is declarative Celery `chain()`s in one workers module, not orchestrator classes. The connectors folder is `app/source_connectors/` (renamed from `connectors/`); never create `app/connectors/`.

## Working rules
- **Git commits are the developer's alone.** Never run `git commit` (or push, amend, rebase, tag) unless the developer explicitly asks for that specific commit in that moment. Staging with `git add` when asked is fine; the commit itself is theirs.
- Every connector needs 2–3 REAL fixture files in `tests/fixtures/<connector>/` and a conformance test before it's "done". No fixtures, no done.
- When a source changes shape in production: update the fixture to the new reality FIRST, then the fix.
- Scrape etiquette: per-domain Redis token bucket, identified user agent, robots.txt, prefer official APIs/bulk files.
- Never introduce PitchBook/Preqin/CB Insights data or any paywalled secondary source. Public primary sources only.
- Log per-call cost for paid APIs (Places, Anthropic) from day one.
- Quality bar for anything you produce: the developer must be able to re-explain it from memory the next morning. Prefer boring, explicit code over clever code. (The hand-writing learning goal was dropped 2026-10-26; this bar stays.)

## Documentation rules
- Before generating code or answering questions that depend on FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic, or Celery API specifics, look up the current official docs via the Context7 MCP server (`context7` tools) rather than relying on training data.
- Never emit deprecated patterns (Pydantic v1 syntax, legacy FastAPI idioms). When unsure whether a pattern is current, check Context7 first.
- If the Context7 server is unavailable, say so explicitly and flag any answer drawn from training data as unverified against current docs.

## Commands
- `uv run uvicorn app.main:app --reload` · `uv run celery -A app.workers worker -Q intake,resolve,retrieve,extract,verify,publish` · `uv run celery -A app.workers beat` · `uv run alembic upgrade head` · `uv run pytest` · `docker compose up -d`

## Agent skills

### Issue tracker

Local markdown: issues, specs and wayfinder maps live as files under `.scratch/<effort>/`. See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context: `GLOSSARY.md` at the repo root + `docs/adr/`. See `docs/agents/domain.md`.
