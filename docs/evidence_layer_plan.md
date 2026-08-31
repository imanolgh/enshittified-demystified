# Evidence Layer — Technical Build Plan
### Filing-grounded evidence engine for PE ownership claims and PC exposure claims — FastAPI/Python stack
### (Laravel equivalents noted throughout as a reference for a Laravel-fluent reader)

---

## 1. Architecture Principle (read this before anything else)

The system's trust guarantee comes from one rule enforced in code, not policy:

> **The LLM never finds facts. It only extracts facts from documents the pipeline retrieved, and every extracted claim must contain a verbatim quote that code mechanically verifies against the stored source document. Claims that fail quote verification are rejected automatically.**

Pipeline in one line:

```
Entity Resolution → Source Retrieval (deterministic) → LLM Extraction (cited) → Mechanical Citation Verification → Confidence Scoring → Graph Storage → Human Review Queue (exceptions only)
```

The AI is a reading-comprehension engine over documents you fetched. Hallucination becomes a catchable failure mode instead of a trust catastrophe.

---

## 2. Core Stack

| Concern | Choice | Laravel equivalent (for reference) | Why |
|---|---|---|---|
| Framework | **FastAPI** (Python 3.12) | Laravel | Async-first API framework; auto-generated OpenAPI docs |
| ORM + migrations | **SQLAlchemy 2.0** + **Alembic** | Eloquent + `php artisan migrate` | More explicit than Eloquent; Alembic autogenerates migration diffs |
| Data validation | **Pydantic v2** | Form Requests / DTO validation (no true equivalent) | The quiet superpower: the Claim schema *is* a Pydantic model, so LLM JSON output validates automatically and malformed extractions never reach the DB |
| Database | PostgreSQL 16 | same | Recursive CTEs for ownership-chain traversal; JSONB for raw payloads |
| Queue | **Celery** + Redis (or `arq` for a lighter async option) | Laravel Queues + Redis; `Bus::chain()` / `Bus::batch()` ≈ Celery `chain()` / `group()` / `chord()` | Every pipeline stage is a Celery task |
| Queue monitoring | **Flower** | Horizon | Dashboard for tasks, retries, throughput (less polished than Horizon) |
| Scheduling | **Celery Beat** | Laravel Scheduler (`app/Console/Kernel`) | Recurring crawls and filing polls |
| HTTP client | **httpx** (async) + **tenacity** (retry/backoff) | Laravel HTTP client (Guzzle) + retry middleware | Per-domain rate limiting via a Redis token bucket ≈ `RateLimiter` |
| Scraping | **Playwright** (JS-heavy pages) + BeautifulSoup / `selectolax` | Browsershot/Dusk + `symfony/dom-crawler` | Meaningfully stronger ecosystem than PHP's |
| PDF / table extraction | **pdfplumber** + **camelot**, in-process | (no good PHP option — would have been AWS Textract) | Schedule of Investments and CAFR tables parse natively; no sidecar, no per-page bill |
| Bulk data | **pandas** / **polars** | `COPY` + raw SQL via `DB::` | Form 5500 CSVs → clean → Postgres |
| LLM | **Anthropic Python SDK** (Sonnet-class bulk, Opus-class escalation) | Anthropic PHP SDK / plain HTTP | Structured outputs pair with Pydantic |
| Search / fuzzy match | **Meilisearch** Python client + **rapidfuzz** | Laravel Scout + Meilisearch | Entity/alias matching (Stage 1) and consumer search (Stage 7) |
| Admin / review UI | **Starlette-Admin** or **SQLAdmin** (+ custom review views), or a small Vue panel; Streamlit acceptable for a scrappy internal v1 | **Filament** | The honest gap of the Python path — Filament had this nearly free; budget real days here |
| Auth / API | FastAPI dependencies + `fastapi-users` (or hand-rolled JWT) | Sanctum + API Resources | Serves claim cards and graph endpoints to Vue |
| Frontend | Vue 3 | same | FastAPI's OpenAPI schema can generate the TS client |
| Document storage | S3 via **boto3** | Flysystem S3 driver | Immutable raw-document archive — your legal defense when a claim is contested |
| Testing | **pytest** + httpx test client | Pest / PHPUnit | Citation-verification loop tests first |
| Deploy | Docker: `uvicorn` (API) + Celery workers + Beat + Redis + Postgres | Forge / Vapor | More moving parts than a Forge deploy; standard once containerized |

## 3. Data Sources & APIs to Integrate

### 3.1 Shared / Entity Resolution
| Source | Access | Used for |
|---|---|---|
| **Google Places API** | Paid API | Canonical local-business identity (name, address, place_id). **Lazy/on-demand only** — canonicalizes user searches and enriches entities; never used for bulk seeding (the per-lookup cost would dwarf all LLM spend) |
| **NPPES NPI Registry** | Free federal API **+ free monthly bulk file** | Healthcare cheat code, twice over: the bulk file is a downloadable census of every U.S. provider/clinic organization (the seeding backbone — load it like Form 5500), and the API serves on-demand freshness checks. Each record maps a clinic to its organization NPI, authorized official, and other-name aliases — your #1 tool for linking a local clinic to its parent DSO |
| **State Secretary of State registries** | Scraping (a few states have APIs) | Legal entity records, registered agents, officers, mergers. Wildly inconsistent per state — build state-by-state, starting with your launch states |
| **OpenCorporates** | API (free tier limited; paid reasonable) | Normalized company registry data across jurisdictions — shortcut before building 50 state scrapers |

### 3.2 PE Evidence Connectors
| Source | Access | Yields |
|---|---|---|
| **PE firm portfolio pages** | Scraping (public marketing pages) | Highest-yield PE source — sponsors brag about acquisitions. Maintain a registry of ~500 sponsor domains and crawl on schedule |
| **SEC EDGAR full-text search** | Free API (`efts.sec.gov`) | Sponsor filings, Form D private-placement notices, 8-Ks mentioning acquisitions |
| **Press release wires** | RSS/scraping (PRNewswire, BusinessWire, GlobeNewswire) + Google News RSS per entity | Acquisition announcements with dates — the acquisition-date feature comes from here |
| **DSO / rollup location pages** | Scraping | The clinic-level roster that links "Bright Smiles of Croton" to "Smile Brands Inc." |
| **WARN notices** | State DOL pages, mostly scraping/CSV | Post-acquisition layoff evidence for the worker-side surface |
| **CourtListener RECAP API** | Free/nonprofit API | Litigation touching sponsors/portcos without paying PACER by the page |
| **Local news** | Google News RSS, GDELT (free) | Small-market acquisition coverage national wires miss |

### 3.3 PC Evidence Connectors
| Source | Access | Yields |
|---|---|---|
| **SEC EDGAR — BDC filings (10-K/10-Q, N-2)** | Free API | Schedule of Investments tables: which fund lends to which company, at what rate, non-accrual status. The core PC dataset |
| **Form ADV (SEC IAPD)** | Free bulk data downloads | Private fund advisers, AUM, fund lists |
| **DOL Form 5500 + Schedule H** | Free bulk datasets (annual CSVs) | Every private-sector retirement plan's investment lineup — the backbone of the 401(k) exposure checker |
| **Public pension CAFRs/ACFRs** | PDF downloads from each system's site | Alternatives allocation %, sometimes fund-level commitments. Top ~100 systems first |
| **NAIC statutory insurance filings** | Partially free, partially paid via aggregators | Insurer PC exposure — later phase, hardest access |

### 3.4 Explicitly Out of Bounds
- **PitchBook / Preqin / CB Insights** — licensing prohibits building on their data, they're secondary sources (breaks the provenance premise), and consumers can't verify their citations. At most, one internal seat later as a lead-checking aid, never as a displayed source.

---

## 4. Database Schema (migrations to write first)

```
entities
  id, canonical_name, entity_type (business|brand|sponsor|fund|dso|pension|insurer|lender),
  jurisdiction, place_id (nullable), npi (nullable), status, created_at

entity_aliases
  id, entity_id, alias, alias_type (dba|legal_name|former_name|domain), source_document_id

documents                      -- immutable once written
  id, source_type (edgar|sos|portfolio_page|press_release|cafr|form5500|news|court|submission),
  url, retrieved_at, sha256, storage_path, mime_type, raw_text (nullable), meta JSONB

claims                         -- atomic, cited assertions
  id, subject_entity_id, predicate (acquired_by|owned_by|majority_stake|minority_stake|
      lends_to|holds_position|allocates_to|operates_location_of|renamed_from),
  object_entity_id, event_date (nullable), value JSONB (amounts, %, rates),
  document_id, verbatim_quote TEXT, quote_verified BOOL, quote_offset,
  extraction_model, extracted_at, status (auto_verified|needs_review|rejected|retracted)

edges                          -- the published graph (derived from claims)
  id, from_entity_id, to_entity_id, relation, effective_date,
  confidence (verified|reported|estimated), ownership_type
      (pe_fund|pe_backed|conglomerate|family|employee_owned|trust|public|independent|unknown),
  supporting_claim_ids JSONB, published_at, retracted_at (nullable)

review_items
  id, claim_id, reason (single_source|conflict|low_confidence|community_flag),
  assigned_to, resolution, resolved_at

ingest_batches / ingest_items  -- batch submission tracking
  batch: id, name, submitted_by, counts, status
  item: id, batch_id, input_name, input_address, resolved_entity_id, stage, result
```

Key design points:
- **Claims are append-only; edges are derived.** Corrections retract an edge and add a new one — you never silently rewrite history, which is both your credibility story and your legal posture.
- **`verbatim_quote` + `quote_verified`** is the anti-hallucination mechanism, stored per claim.
- **`confidence` + `ownership_type`** on edges powers the claim cards, including the honest "unknown" and the Fiskars-isn't-PE taxonomy.

---

## 5. Pipeline Flow — Step by Step (Celery tasks)

Everything below is a Celery task. Sequencing uses Celery `chain()` (≈ Laravel `Bus::chain()`), fan-out uses `group()` (≈ `Bus::batch()`), and "run X after all of these finish" uses `chord()` (≈ `Bus::batch()->then(...)`). Task names below use Python snake_case; the Laravel job-class name each replaces is shown in parentheses on first mention.

### Stage 0 — Intake
`create_ingest_batch` (was `CreateIngestBatch`) → accepts a single name or a CSV of thousands (`name, address, city, state, category`); pandas validates the CSV. Each row becomes an `ingest_item` and dispatches Stage 1 via a Celery `group()`. Queue: `intake` (monitored in Flower).

### Stage 1 — Entity Resolution (`resolve_entity`, was `ResolveEntityJob`)
1. Normalize input (strip punctuation, expand abbreviations).
2. Google Places lookup → address + place_id.
3. Healthcare? Match against the pre-loaded NPPES bulk census first (free, local); NPPES API only on census miss → organization NPI, authorized official, parent org name.
4. State SoS / OpenCorporates lookup → legal entity, registered agent, officers.
5. Fuzzy-match against existing `entities` + `entity_aliases` (Meilisearch + rapidfuzz scoring) to avoid duplicates.
6. Output: `entity_id` (created or matched) with aliases recorded. Ambiguous matches (score below threshold) → `review_items` instead of guessing.

**This stage is where most real-world failure happens. Budget accordingly.**

### Stage 2 — Source Retrieval (`retrieve_{connector}` tasks, fan-out; was `Retrieve{Connector}Job`)
For the resolved entity + its aliases, dispatch one task per relevant connector inside a Celery `chord()` whose callback triggers Stage 3 (category-aware: a dental clinic triggers NPPES/DSO/portfolio/news connectors; a fund triggers EDGAR/ADV connectors).

Each connector task:
1. Queries/scrapes its source (httpx for APIs/static pages, Playwright for JS-heavy pages; per-domain rate limiting via a Redis token bucket; respect robots.txt; tenacity exponential backoff on 429/5xx).
2. Stores the raw document to S3 (boto3), computes sha256, writes a `documents` row via SQLAlchemy.
3. Extracts plain text (HTML → text via selectolax/BeautifulSoup; PDFs → pdfplumber; tables → camelot, structured JSON stored in `meta`). All in-process — no sidecar.
4. Skips documents whose sha256 already exists (dedup).

Celery Beat (≈ Laravel Scheduler): recurring crawls of sponsor portfolio pages, DSO rosters, and news RSS to catch *new* acquisitions — this feeds the Acquisition Alarm feature.

### Stage 3 — LLM Extraction (`extract_claims`, was `ExtractClaimsJob`)
Runs per entity once its retrieval chord completes (the `chord()` callback ≈ `Bus::batch()->then(...)`).

1. Assemble the document set (text + parsed tables) for the entity, chunked to context limits.
2. Call Claude (Anthropic Python SDK) with a strict system prompt; the response is parsed straight into Pydantic `Claim` models — anything that fails validation is dropped and logged before it can reach the DB:
   - Emit claims only in the fixed predicate vocabulary.
   - **Every claim must include a verbatim quote copied exactly from the provided document.**
   - Classify ownership_type per the taxonomy (pe_fund vs conglomerate vs family etc.).
   - If the documents contain no ownership/exposure evidence, return an explicit `no_evidence_found` result — a first-class outcome, not an error.
3. Model tiering: Sonnet-class for bulk; escalate to Opus-class when documents conflict or classification is ambiguous.
4. Write raw response to the claim rows (`extraction_model`, `extracted_at`).

### Stage 4 — Mechanical Citation Verification (`verify_citations`, was `VerifyCitationsJob`)
Pure Python, no AI:
1. For each claim, string-search `verbatim_quote` (whitespace-normalized) in the stored document text.
2. Found → `quote_verified = true`, record offset. Not found → **auto-reject** the claim and log for prompt tuning.
3. Sanity checks: cited document actually mentions the subject alias; event_date is plausible; numeric values in `value` appear in the quote for PC claims.

### Stage 5 — Confidence Scoring & Edge Publication (`score_and_publish`, was `ScoreAndPublishJob`)
1. Group verified claims by (subject, predicate, object).
2. **Two independent documents agree → publish edge as `verified`.** ("Independent" = different `source_type` or different domains — a press release syndicated to five sites counts once.)
3. One source → publish as `reported` **and** open a `review_item` (single_source).
4. Conflicting claims → no publication; `review_item` (conflict), escalated extraction pass with both documents side-by-side to assist the human.
5. `no_evidence_found` → entity flagged `independent (no PE evidence found)` / `unknown` — the honest state the consumer UI displays.

### Stage 6 — Human Review (Starlette-Admin/SQLAdmin panel or small Vue app; ≈ Filament)
Reviewers see: the claim, the quote highlighted in the source document, the conflicting evidence if any. Actions: approve (publish edge), edit-and-approve, reject, request more retrieval. Every action audited. Community submissions (from the Verified Ledger feature) enter this same queue as `source_type = submission` documents and count as one source — they can corroborate but never solo-publish a `verified` edge.

### Stage 7 — Serving
- `GET /api/entities/{id}/card` → claim card: verdict, ownership_type, sponsor, acquisition date, N sources with links + quotes, confidence.
- `GET /api/entities/{id}/graph` → recursive CTE (via SQLAlchemy `text()`) walking edges for the ownership-chain / money-flow visualization (cap depth, label each hop with confidence). FastAPI routers ≈ Laravel API controllers.
- Retraction/correction endpoint feeds a public changelog — corrections displayed, not hidden.

---

## 6. PE vs. PC: Same Pipeline, Different Muscles

| | PE evidence | PC evidence |
|---|---|---|
| Dominant problem | **Extraction from scattered prose** (press releases, portfolio pages, registries) | **Table parsing from structured filings** (Schedule of Investments, CAFR allocation tables, Form 5500) |
| Key stage | Stage 2 breadth (many connectors) + Stage 3 classification | camelot/pdfplumber table extraction *before* Stage 3; LLM interprets parsed tables |
| Claim shape | Ownership edges (`acquired_by`, `operates_location_of`) | Financial edges with values (`lends_to` @ rate, `allocates_to` @ %, `holds_position` @ amount) |
| Extra layer | Ownership-type taxonomy (the misattribution fix) | Jargon decoder content keyed to claim types (gates, PIK, non-accrual) — written once, attached to every relevant card |
| Easiest wins | Sponsor/DSO rosters (national PE layer) × NPPES bulk census (national denominator) — their join is the launch map | Form 5500 bulk CSVs (no scraping!) + top-100 pension CAFRs |

Form 5500 deserves emphasis: it's a **bulk annual CSV download**, not a scrape — with pandas/polars you can load the entire universe of private-sector plan lineups into Postgres in a weekend, with no LLM involved (the government CSV *is* the structure). It's the fastest path to a working MyRetirementX-Ray demo.

---

## 7. Operational & Legal Guardrails

- **Immutable document archive** — every published claim links to a stored copy with retrieval date and checksum. This is the answer to both "prove it" and takedown pressure.
- **Two-source rule in code**, not policy (Stage 5).
- **Public corrections log** — retraction workflow, never silent edits. In a market allergic to overclaiming, visible corrections are a feature.
- **Scrape etiquette** — per-domain rate limits, identified user agent, robots.txt respect, prefer official APIs/bulk data wherever they exist. Most of your best sources (EDGAR, NPPES, Form 5500, CourtListener) are official and free — lead with those.
- **Cost controls** — LLM spend is per-document-set per entity; cache extractions by document sha256 so re-runs are free; batch API pricing for the big seeding runs. Rough planning figure: a few cents to a few tens of cents per entity depending on document volume — real money at 100k entities, trivial at pilot scale.
- **Defamation posture** — publish only quote-verified, sourced claims; label confidence honestly; show the evidence inline. "PE-owned (verified — 3 sources)" with clickable receipts is a fundamentally different legal and trust position than a bare pin on a map.

---

## 8. Build Order (prototype → wedge → scale)

**Phase 1 — Prove the trust loop (1–2 weeks of effort)**
Alembic migrations for the schema above; one connector (sponsor portfolio pages for ~20 known DSO/vet rollup sponsors); `extract_claims` + `verify_citations` tasks; a *minimal* review view (Starlette-Admin or Streamlit is fine at this stage). Add roughly a week to the estimate for stack ramp-up. Success = a claim card for a real clinic with verified quotes. **The citation-verification loop is the premise — prototype it first.**

**Phase 2 — Healthcare wedge**
Load the NPPES bulk census (national); add the NPPES API, state SoS for launch states, press-release RSS, and lazy Google Places resolution. Match DSO/sponsor rosters against the census for the national baseline, then run a deep batch of every dental + vet practice in one metro. Measure: % auto-verified, % unknown, % needing review — these numbers tell you real coverage and review staffing needs.

**Phase 3 — Batch scale + alerts**
CSV batch intake at thousands-of-entities scale; Celery Beat re-crawls; diff detection on portfolio pages/rosters → new-acquisition events → Acquisition Alarm notifications.

**Phase 4 — PC layer**
Form 5500 bulk load (pandas); camelot BDC Schedule of Investments parsing; top-100 pension CAFR ingestion; PC claim types + jargon decoder content. This is where the Python choice pays back most visibly. This lights up MyRetirementX-Ray on the same graph.

**Phase 5 — Graph depth**
Cross-link the layers (sponsor → PC lender → pension LP where public evidence exists, `estimated` edges labeled as such); expose the money-flow graph views; open community submissions into the review queue.

---

## 9. What This Deliberately Does Not Do

- No PitchBook/Preqin data (licensing + provenance premise).
- No LLM answers beyond the corpus — "no evidence found" is always preferred over inference.
- No silent corrections, no unsourced edges, no solo-published community tips.
- No claims of completeness — the honest `unknown` state is load-bearing for trust.

---

## 10. Appendix — Laravel → FastAPI/Python Translation Cheat Sheet

For a Laravel-fluent reader, the concepts map almost one-to-one; only the names and a few idioms change.

| You're used to (Laravel) | You'll write instead (Python) | Note |
|---|---|---|
| `php artisan make:migration` / `migrate` | `alembic revision --autogenerate` / `alembic upgrade head` | Alembic diffs your SQLAlchemy models to generate migrations |
| Eloquent model | SQLAlchemy declarative model | Relationships declared explicitly (`relationship()`); no magic accessors |
| Form Request validation | Pydantic model | Also used for LLM output and API request/response bodies — one schema, three uses |
| API Resource | Pydantic response model | FastAPI serializes it and documents it in OpenAPI automatically |
| Controller / route | FastAPI router + path-operation function | Dependency injection via `Depends()` replaces service-container binding |
| Middleware | FastAPI middleware / dependencies | |
| `Bus::chain()` | Celery `chain()` | |
| `Bus::batch()` / `->then()` | Celery `group()` / `chord()` | |
| `dispatch(new Job)` | `task.delay()` / `task.apply_async(queue=...)` | |
| Queue worker (`queue:work`) | `celery -A app worker -Q intake,resolve,...` | |
| Horizon | Flower | |
| Scheduler (`Kernel::schedule`) | Celery Beat schedule | |
| `Http::retry()->get()` | `httpx` + `tenacity` decorator | |
| `RateLimiter` | Redis token bucket (hand-rolled or `limits` library) | |
| `Storage::disk('s3')` | `boto3` client | |
| Scout + Meilisearch | Meilisearch Python client (+ rapidfuzz for local scoring) | |
| Filament resource | Starlette-Admin / SQLAdmin view, or a Vue page on FastAPI endpoints | The one place Laravel had a clear edge |
| Sanctum | `fastapi-users` or JWT dependency | |
| Pest test | pytest function + httpx `TestClient` | |
| `.env` + `config()` | `pydantic-settings` `BaseSettings` | Typed, validated env config |
| Forge deploy | Docker Compose (api + worker + beat + redis + postgres) | |
