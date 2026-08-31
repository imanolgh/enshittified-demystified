# Evidence Layer — Full FastAPI (Python) Architecture
### Building the entire system (PE + PC pipelines, graph, review, serving) in Python

---

## 1. When This Is the Right Choice

Python is the native language of this workload: scraping, PDF/table parsing, dataframe wrangling, and LLM tooling are all best-in-class here, with no Textract dependency and no sidecar. Choose this if you're willing to trade your PHP fluency for the ecosystem fit — and accept that the admin/review UI, which Filament gives Laravel nearly for free, must be assembled from smaller pieces.

## 2. Stack

| Concern | Choice | Notes |
|---|---|---|
| Language/Framework | Python 3.12 · **FastAPI** | Async-first; automatic OpenAPI docs for your API |
| Database | PostgreSQL 16 | Same schema, same recursive CTEs |
| ORM | **SQLAlchemy 2.0** + Alembic (migrations) | The Eloquent equivalent; more explicit, more verbose |
| Data validation | **Pydantic v2** | The quiet superpower of this path: your Claim schema *is* a Pydantic model, and the LLM's JSON output validates against it automatically — malformed extractions rejected before they touch the DB |
| Queue | **Celery + Redis** (or `arq` for a lighter async-native option) | Jobs, chains, groups ≈ Laravel Bus chains/batches |
| Queue monitoring | **Flower** | Celery's dashboard ≈ Horizon (less polished) |
| Scheduling | **Celery Beat** | Recurring crawls ≈ Laravel Scheduler |
| HTTP client | **httpx** (async) + `tenacity` (retry/backoff) | Per-domain rate limiting via Redis token bucket |
| Scraping | **Playwright** (JS-heavy pages) + BeautifulSoup/`selectolax` (HTML) | Meaningfully better than PHP's options |
| PDF/tables | **pdfplumber + camelot** in-process | No sidecar, no Textract bill — the Schedule of Investments and CAFR tables parse natively |
| Bulk data | **pandas / polars** | Form 5500 CSVs → cleaned → Postgres in a notebook-grade workflow |
| LLM | **Anthropic Python SDK** — Sonnet-class bulk, Opus-class escalation | First-party SDK; pairs with Pydantic for structured outputs |
| Search / fuzzy matching | **Meilisearch** via its Python client (+ `rapidfuzz` for cheap local scoring) | Same engine as the Laravel path |
| Admin / review UI | **The honest gap.** Options: (a) **Starlette-Admin** or **SQLAdmin** for CRUD + custom review views, (b) build the review queue as a small Vue app on FastAPI endpoints, (c) Streamlit for a scrappy internal v1 | Budget real days here; nothing matches Filament's completeness |
| Auth/API | FastAPI dependencies + `fastapi-users` (or roll JWT) | Serves claim cards / graph to Vue |
| Frontend | Vue 3 | Identical in either architecture — FastAPI's auto-generated OpenAPI schema can even generate your TS client |
| Storage | S3 via `boto3` | Immutable document archive |
| Testing | pytest + httpx test client | Citation-verification loop tests first |
| Deploy | Docker: `uvicorn` (API) + Celery workers + Beat + Redis + Postgres; fly.io/Render/VPS | More moving parts than a Forge deploy, standard once containerized |

## 3. Pipeline → Python Primitives

| Stage | Implementation |
|---|---|
| 0 Intake | CSV upload endpoint → pandas validation → `ingest_items`; Celery `group()` dispatch |
| 1 Resolve | `resolve_entity` task: Places → NPPES → SoS/OpenCorporates → Meilisearch/rapidfuzz match → Entity upsert; ambiguity → review |
| 2 Retrieve | One Celery task per connector; Playwright pool for JS pages; Form 5500 = pandas ETL script, not a scrape |
| 2.5 Parse | In-process: pdfplumber text, camelot tables → normalized text + table JSON on `documents` |
| 3 Extract | `extract_claims` task: doc set → Anthropic SDK call → **Pydantic-validated** claim objects → insert |
| 4 Verify | Pure-Python quote matching (normalized substring) → `quote_verified` or auto-reject |
| 5 Score/Publish | Grouping + two-source rule + edge upsert + review_items — plain SQLAlchemy logic |
| 6 Review | Starlette-Admin/SQLAdmin resource with custom claim-detail view (quote highlighted in doc text), or small Vue panel |
| 7 Serve | FastAPI routers; ownership chain = recursive CTE via SQLAlchemy `text()`; OpenAPI docs free |

## 4. Honest Weaknesses of the All-Python Path

1. **You're learning while building.** Every Eloquent/Blade/Artisan reflex needs a SQLAlchemy/Jinja-or-Vue/Typer translation. Expect the first month to run at half your Laravel speed.
2. **The review UI is artisanal.** Filament's resource-with-actions-and-audit-log in an afternoon becomes days of Starlette-Admin customization or a hand-built Vue panel. Since human review is a core trust mechanism, this is the path's most material cost.
3. **More deployment surface.** API process + Celery workers + Beat + Flower vs. Laravel's tighter conventional story. Docker Compose tames it, but it's on you.
4. **Framework glue is thinner.** Laravel hands you auth scaffolding, rate limiting, notifications, and conventions; in FastAPI you select and wire libraries for each.

## 5. Where This Path Clearly Wins

- **PC layer is dramatically nicer**: pandas for Form 5500, camelot for Schedule of Investments, no Textract cost or lock-in.
- **Pydantic-validated LLM extraction** is the cleanest possible implementation of "reject malformed claims automatically."
- **Playwright scraping** for hostile/JS-heavy sponsor pages.
- **Data-science adjacency**: when you later want dedup embeddings, entity-matching models, or exposure analytics, you're already home.

## 6. Build Order (unchanged in substance)

1. Alembic schema + one connector + extract/verify tasks + a *minimal* review view = the trust loop. Add a week over the Laravel estimate for stack ramp-up.
2. Healthcare wedge (NPPES, launch-state SoS, press RSS, Places).
3. Batch scale + Beat re-crawls + acquisition-diff alerts.
4. PC layer (this is where the path pays you back: pandas + camelot, no managed-service dependency).
5. Cross-layer edges + graph views + community submissions.
