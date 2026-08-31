# Evidence Layer — Full Laravel Architecture
### Building the entire system (PE + PC pipelines, graph, review, serving) in PHP/Laravel

---

## 1. When This Is the Right Choice

You ship fastest in the stack you know. Laravel covers every pipeline stage adequately, and the two places PHP is genuinely weak (PDF table extraction, heavy dataframe work) can be outsourced to a managed service (AWS Textract) instead of running your own Python. Choose this if solo/small-team velocity and one deployable codebase matter more than best-in-class data tooling.

## 2. Stack

| Concern | Choice | Notes |
|---|---|---|
| Language/Framework | PHP 8.3 · Laravel 11 | |
| Database | PostgreSQL 16 | JSONB for payloads; recursive CTEs for graph walks |
| ORM | Eloquent | Entities, Claims, Edges, Documents models |
| Queue | Laravel Queues + Redis | One queue per stage: `intake`, `resolve`, `retrieve`, `extract`, `verify`, `publish` |
| Queue monitoring | **Horizon** | Dashboards, retries, per-queue workers |
| Scheduling | Laravel Scheduler | Recurring crawls (portfolio pages, RSS, EDGAR polling) |
| HTTP client | Laravel HTTP (Guzzle) | Retry/backoff middleware; per-domain rate limiter via `RateLimiter` + Redis |
| Scraping | HTTP client + `symfony/dom-crawler`; **Laravel Dusk or a headless-Chrome sidecar (Browsershot)** for JS-heavy portfolio pages | PHP's scraping story is workable, not luxurious |
| PDF/tables | **AWS Textract** (managed) — the pragmatic call in an all-PHP build; `smalot/pdfparser` only for simple text PDFs | This replaces the Python sidecar |
| LLM | Anthropic PHP SDK (or plain HTTP) — Sonnet-class bulk, Opus-class escalation | JSON-schema-constrained outputs |
| Validation of LLM output | `justinrainbow/json-schema` or hand-rolled DTO validation | PHP's answer to Pydantic; less elegant, fully functional |
| Search / fuzzy matching | Laravel Scout + **Meilisearch** | Stage 1 alias matching + consumer search |
| Admin / review UI | **Filament v3** | The killer advantage of this path: Stage 6 review queue, claim editor, corrections log in days, not weeks |
| Auth/API | Sanctum + Laravel API resources | Serves claim cards, graph endpoints to Vue |
| Frontend | Vue 3 + your Bootstrap familiarity (or Tailwind) | Same in either architecture |
| Storage | S3 via Flysystem | Immutable document archive |
| Testing | Pest | Feature tests around the citation-verification loop first |
| Deploy | Forge/Vapor, or Docker on a VPS | Single app + workers + Redis + Postgres |

## 3. Pipeline → Laravel Primitives

| Stage | Implementation |
|---|---|
| 0 Intake | `IngestBatch`/`IngestItem` models; CSV upload via Filament; `Bus::batch()` dispatch |
| 1 Resolve | `ResolveEntityJob`: Places API → NPPES → SoS/OpenCorporates → Scout fuzzy match → create/match Entity; ambiguity → `review_items` |
| 2 Retrieve | One job class per connector (`RetrieveEdgarJob`, `RetrievePortfolioPageJob`, `RetrieveForm5500Job`…). Form 5500 = artisan command bulk-loading DOL CSVs straight into Postgres (`COPY`) |
| 2.5 Parse | `ParseDocumentJob` → Textract for PDFs/tables → normalized text + table JSON onto the `documents` row |
| 3 Extract | `ExtractClaimsJob`: assemble doc set → Claude call → schema-validate → write `claims` |
| 4 Verify | `VerifyCitationsJob`: whitespace-normalized `str_contains` of quote against stored text; fail → auto-reject |
| 5 Score/Publish | `ScoreAndPublishJob`: group claims, two-source rule, write `edges`, open `review_items` for single-source/conflict |
| 6 Review | Filament resources: ReviewItem list, claim detail w/ highlighted quote, approve/edit/reject actions, audit log |
| 7 Serve | API controllers; ownership-chain endpoint = recursive CTE via `DB::select` |

## 4. Honest Weaknesses of the All-PHP Path

1. **Document parsing depends on Textract** — per-page cost (~$1.50/1k pages text, more for tables) and AWS lock-in, in exchange for zero parsing infrastructure. At CAFR/BDC volumes this is tens of dollars a month at pilot scale; fine.
2. **Complex table semantics** (multi-page Schedule of Investments with footnotes) may need a second LLM pass over Textract output where Python's camelot would have given cleaner structure directly.
3. **Bulk data ergonomics** — loading/transforming Form 5500's giant CSVs is `COPY` + SQL rather than pandas. Entirely doable; less pleasant.
4. **Scraping JS-heavy sites** needs Browsershot/headless Chrome; Python's Playwright ecosystem is smoother.

None of these are blockers. They're paper cuts, paid for with the massive velocity of Filament + Horizon + your existing fluency.

## 5. Build Order (unchanged from the master plan)

1. Migrations + one connector + Extract/Verify jobs + Filament review = the trust loop, ~1–2 weeks.
2. Healthcare wedge (NPPES, SoS launch states, press RSS, Places).
3. Batch scale + scheduled re-crawls + acquisition-diff alerts.
4. PC layer: Form 5500 bulk command, Textract-parsed BDC filings + CAFRs.
5. Cross-layer edges + graph views + community submissions.
