# Build Progress

Tracks roadmap position (`docs/build_roadmap.md` step numbering). Claude keeps this current; git history is the source of truth for what's committed.

**Currently on: Step 1 — Contracts (`app/core/contracts.py`)**

## Done

- **Day 0 — Prerequisites** (2026-09-03)
  - Toolchain: uv, Docker Desktop + WSL2, Python 3.12 venv
  - `pyproject.toml` + `uv.lock` (core deps; anthropic/playwright/pdfplumber/polars/flower deferred until their steps)
  - `docker-compose.yml`: postgres 16, redis, minio — all verified healthy
  - Repo skeleton, docs committed, CLAUDE.md contract
  - Structure decisions (see CLAUDE.md): `source_connectors/` rename, thin routers/no controllers, single `config.py`, chain-based orchestration; stubs for `config.py`, `db.py`, `logging_setup.py`, `main.py`

## In progress

- **Step 1 — Contracts (Day 1)**: developer hand-writes `app/core/contracts.py` (RawDocument, ExtractedClaim + predicate enum, ResolvedEntity, ClaimCardOut, EdgeOut)
  - [ ] contracts.py written (developer)
  - [ ] validation test suite (Claude, after)

## Up next

- Step 2 — DB schema + Alembic loop
- Step 3 — FastAPI skeleton + `POST /internal/claims`
- Step 4 — `store_document`
- Step 5 — Celery wiring
