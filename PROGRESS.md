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

## Rulings since the original planning chat

- **2026-09-14 — 7 predicates.** `acquired_by, owned_by, operates_location_of, lends_to, allocates_to, holds_position, renamed_from`. `majority_stake`/`minority_stake` dropped; stake size/type goes in the claim's `value` (e.g. `{"stake_pct": 65, "stake_type": "majority"}`).
- **2026-10-16 — FastAPI/Python only.** Nothing is built in Laravel; Laravel mentions in docs are learning comparisons only.
- **2026-10-16 — Launch scope.** Launch = the 29-step roadmap engine + pre-launch-seeding workstreams. On-demand user research and launch-state vet license boards are required before launch (removed from the roadmap's deferred list).
- **2026-10-16 — Pricing.** `monetizationideas.md` is canonical: Premium ~$8/mo or ~$79/yr; standalone deep-dive $29–49; headline exposure number free. `decisions.md` §5 updated to point there.
- **2026-10-16 — First connector.** Press-release RSS (roadmap Step 10); sponsor portfolio pages follow at Step 14. Roadmap wins over the plan doc on build order.
- **Parked (not in docs yet):** a Research/Pro tier (~$20–30/mo: BDC loan-book diffs, rollup dossiers, insurer map). Don't launch it until the graph has real depth.

## Up next

- Step 2 — DB schema + Alembic loop
- Step 3 — FastAPI skeleton + `POST /internal/claims`
- Step 4 — `store_document`
- Step 5 — Celery wiring
