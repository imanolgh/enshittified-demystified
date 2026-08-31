# Research Flows — Scenario Walkthroughs
### Concrete end-to-end traces of claim gathering, verification, and publication for the PE and PC paths, in the FastAPI/Celery stack
### Covers: initial bulk seeding, on-demand lookups, and ongoing scheduled refresh

All entity names in Scenario examples that reference real companies (e.g., Heartland Dental / KKR) reflect widely reported public information and are used for realism; fictional local businesses are marked.

---

# PART A — PRIVATE EQUITY FLOWS

## Scenario A0: National Seeding — Census × Rosters (runs before A1)

**Trigger:** One-time launch seeding, then monthly refresh.

1. `load_nppes_census`: download the free NPPES bulk file → pandas filter to Tier-1 taxonomies → national entities for every dental/medical organization (names, addresses, authorized officials, other-name aliases). Same ETL pattern as Form 5500; no API calls, no Places, no LLM.
2. Sponsor/DSO roster crawl (the Scenario A3 crawler, run in full): each roster location → `operates_location_of` claim citing the roster page.
3. **The census match:** roster locations resolved against census entities. Matches publish the PE-connected layer; every unmatched census entity publishes as "no PE evidence found (checked {date})".
4. Result: the national healthcare map lights up — PE-connected layer + honest-independent denominator — for a few dollars of extraction and zero per-lookup API cost. Deep per-entity research (A1) then adds metro-depth chains on top.

## Scenario A1: Metro Depth — 2,000 Dental & Vet Practices in One Metro

**Trigger:** You select a launch metro's census slice (or upload `westchester_dental_vet.csv`) via the admin endpoint, for full connector fan-out on each entity.

### Step 1 — Intake
`POST /admin/ingest-batches` → pandas validates the CSV → 2,000 `ingest_items` rows (status `queued`) → Celery `group()` dispatches 2,000 `resolve_entity` tasks onto the `resolve` queue. Workers process ~4–8 concurrently (rate limits, not CPU, are the bottleneck).

### Step 2 — Entity Resolution (`resolve_entity`)
For row: *"Bright Smiles Dental, 123 Grand St, Croton-on-Hudson, NY"* (fictional):

1. **Google Places** Text Search → canonical name, formatted address, `place_id`, category confirmation. (1 call, ~$0.017)
2. **NPPES API** (free): `https://npiregistry.cms.hhs.gov/api/?organization_name=Bright+Smiles+Dental&state=NY` → returns organization NPI **1234567890**, authorized official "J. Chen DDS", and — the gold — "Other Organization Name" field listing **"Smile Partners Management LLC"** (a management-company alias).
3. **NY SoS scrape** for both names → Bright Smiles Dental PLLC (active) + Smile Partners Management LLC, foreign LLC, registered agent = CT Corporation.
4. **Meilisearch/rapidfuzz** match against existing entities → "Smile Partners Management" matches an existing DSO entity at 0.94 → link instead of create.
5. Write: entity `ent_8821` (business) with aliases, `operates_under` hint → `ent_privileged DSO ent_0455`. Item status → `resolved`.

**Failure branches:** Places returns 3 plausible matches → item status `ambiguous`, lands in review queue with candidates; no NPPES hit for a vet named "Pet Palace" → continue with Places + SoS only (NPPES is dental/medical, vets resolve via state veterinary license boards where scraped).

### Step 3 — Retrieval Fan-out (`retrieve_*` tasks, Celery `chord`)
Category `dental` + DSO link triggers this connector set for `ent_8821` + `ent_0455`:

| Task | Call | Typical yield |
|---|---|---|
| `retrieve_dso_roster` | Playwright fetch of smilepartners.com/locations | Location page listing Croton office → confirms operates_under |
| `retrieve_portfolio_pages` | Fetch known sponsor domains whose portfolio mentions "Smile Partners" (from sponsor registry crawl index) | e.g., sponsor page: "Smile Partners — Partnered 2022" |
| `retrieve_press` | Google News RSS `q="Smile Partners Management"` + wire archives | PR: "Sponsor X announces growth investment in Smile Partners" |
| `retrieve_edgar_fts` | `https://efts.sec.gov/LATEST/search-index?q=%22Smile+Partners%22` | Form D from 2022 raise, if any |
| `retrieve_sos_history` | Amendment/merger filings | Name changes, mergers |

Each document → S3 (`docs/{sha256}.html`), `documents` row (url, retrieved_at, sha256, source_type). Dedup by sha256. The chord's callback fires `extract_claims` when all retrievals settle.

### Step 4 — Extraction (`extract_claims`)
Assemble the 6–12 documents (text-extracted) → one Claude call (Sonnet-class) with the claim JSON schema. Pydantic-validated output, e.g.:

```json
[
 {"subject":"ent_8821","predicate":"operates_location_of","object":"ent_0455",
  "quote":"Croton-on-Hudson — Bright Smiles Dental","doc":"d_4410"},
 {"subject":"ent_0455","predicate":"acquired_by","object":"ent_sponsorX",
  "event_date":"2022-06-14",
  "quote":"Sponsor X today announced a growth investment in Smile Partners Management","doc":"d_4412"},
 {"no_evidence_for":["lends_to"]}
]
```

Malformed items fail Pydantic → logged, dropped, batch flagged if failure rate >5%.

### Step 5 — Mechanical Verification (`verify_citations`)
Pure Python: normalize whitespace, substring-match each `quote` in its doc's stored text. Match → `quote_verified=true` + offset. No match → claim auto-rejected + logged for prompt tuning. Sanity checks: subject alias appears in doc; event_date within doc's plausible range.

### Step 6 — Scoring & Publication (`score_and_publish`)
- `acquired_by(SmilePartners → SponsorX)`: supported by press release (wire) **and** sponsor portfolio page (different domains/source_types) → **edge published, confidence `verified`**, ownership_type `pe_backed`.
- `operates_location_of(BrightSmiles → SmilePartners)`: DSO roster **and** NPPES other-name field → **verified**.
- Result the consumer app can now serve: *Bright Smiles → Smile Partners (DSO) → Sponsor X (PE)* — full chain, 4 receipts.
- A different item in the batch with only one source → edge `reported` + `review_item(single_source)`.

### Step 7 — Batch Outcome Report
Batch dashboard after ~a day of wall-clock (rate-limit bound):
`resolved 94% · verified chain 31% · reported 9% · no_evidence_found 52% · needs_review 8%`.
The 52% "no evidence" entities publish as **"No PE evidence found (checked {date})"** — the honest state, and in Tier-1 verticals a meaningful "likely independent" signal.

---

## Scenario A2: On-Demand — User Searches a Business Not in the Graph

**Trigger:** `GET /api/search?q=harbor+veterinary+ossining` → no entity match above threshold.

1. API responds instantly with `status: researching` (+ any fuzzy near-matches) — never block the request on the pipeline.
2. Dispatch the same chain as A1 for a single entity on a **priority queue** (`resolve → retrieve → extract → verify → publish`); on-demand single-entity research completes in minutes (bounded by polite crawling), not seconds.
3. Frontend polls `GET /api/entities/pending/{ticket}` or subscribes via SSE; when published, the claim card renders.
4. If the outcome is `no_evidence_found`, that publishes too — with its checked-date — so the next searcher gets an instant answer.
5. Every on-demand search thus **grows the graph permanently**; user demand becomes your crawl prioritization signal.

---

## Scenario A3: Ongoing — Scheduled Sponsor-Page Diff Detects a New Acquisition

**Trigger:** Celery Beat, nightly: `crawl_sponsor_registry` iterates ~500 known sponsor/DSO/rollup domains.

1. `retrieve_portfolio_pages` refetches each portfolio/locations page → sha256 compare vs. last stored version. Unchanged (majority) → stop, $0 LLM spend.
2. Changed: diff the extracted text. New string detected: *"Hudson Valley Veterinary Group — joined 2026."*
3. Dispatch `resolve_entity("Hudson Valley Veterinary Group")` → resolves or creates entity → targeted retrieval (press RSS for the name, EDGAR FTS) → extract → verify → publish `acquired_by` edge (initially `reported` if only the portfolio page attests; press pickup days later upgrades it to `verified` automatically when the second claim lands).
4. **Event emission:** publication of a new `acquired_by` edge fires `acquisition_event` → notification fan-out to users following that entity/category/region (the Acquisition Alarm product) and to the public changelog.
5. Same nightly loop covers DSO rosters (location adds/removals) and Google News RSS per tracked sponsor.

**Beat schedule (PE):**

| Task | Cadence |
|---|---|
| Sponsor portfolio + DSO roster crawl | nightly |
| Press RSS/GDELT poll per tracked entity | every 6h |
| EDGAR full-text poll (tracked sponsor names) | daily |
| SoS re-check for tracked entities | monthly |
| Re-verify stale `reported` edges (hunt for 2nd source) | weekly |
| Refresh `no_evidence_found` entities | quarterly, and instantly on any mention in press feeds |

---

# PART B — PRIVATE CREDIT FLOWS

## Scenario B1: Initial Seeding — The Three Bulk Loads

### B1a — Form 5500 universe (the weekend win)
1. `load_form5500(year=2025)`: download DOL EFAST bulk CSVs (plan header + Schedule H) — no scraping, no LLM.
2. polars/pandas: filter defined-contribution plans → normalize sponsor employer names → upsert `entities(type=plan)` + `allocates_to` **structured claims** with `source_type=form5500_bulk`.
3. Bulk-load claims skip LLM extraction entirely (the government CSV *is* the structure) but still carry document provenance (file, row, year) and publish as `verified` (single authoritative source rule: official filings self-verify).
4. Outcome: essentially every private-sector plan in the U.S. is queryable by employer name.

### B1b — BDC loan books (the parsing workhorse)
1. `discover_bdcs`: EDGAR company search, SIC/filer type → list of ~150 BDC CIK numbers → entities.
2. Per BDC: `retrieve_edgar_filing(cik, "10-K")` via `https://data.sec.gov/submissions/CIK{cik}.json` → latest 10-K/10-Q → S3.
3. `parse_soi`: pdfplumber/camelot extract the **Schedule of Investments** tables (often 30–80 pages) → normalized rows: borrower name, instrument, rate (spot PIK terms), principal, fair value, non-accrual flag.
4. `extract_claims` (LLM pass over *parsed table JSON*, not raw PDF): emits `lends_to` claims — one per borrower — each quoting its table row text; plus fund-level facts (total PIK %, non-accrual %).
5. Verification quirk: quotes match against the *parsed table text* stored on the document row; a numeric cross-check asserts the quoted principal equals the structured value.
6. Borrower names → `resolve_entity` (no Places — these aren't storefronts; EDGAR/SoS/fuzzy only). This is where PC meets PE: **"Borrower: Smile Partners Management LLC" resolves to `ent_0455`** — and the cross-layer edge `lends_to(BDC_Fund → SmilePartners)` joins the graphs.

### B1c — Top-100 public pension CAFRs
1. Curated registry: pension system → CAFR download URL pattern.
2. `retrieve_cafr` → PDF → `parse_cafr` targets the asset-allocation statement → LLM extracts `allocates_to` claims with page-anchored quotes ("...alternative investments of 27.8%... (p. 47)").
3. Where the CAFR lists individual fund commitments (many do), extract those too → `holds_position(Pension → Fund)` edges — LP relationships entering the graph.
4. Single authoritative source → `verified`, page-cited.

## Scenario B2: On-Demand — Paid 401(k) Analysis Request

**Trigger:** User submits employer name (or types tickers off their statement) → `POST /api/analyses`.

1. Employer name → fuzzy match against the Form 5500 sponsor index (already loaded, B1a) → plan entity → lineup. Ambiguous (multiple plans) → ask the user to pick (plan names shown). No 5500 (gov worker) → route to pension flow instead.
2. For each lineup holding:
   - **Mutual fund** → resolve ticker → check cached **N-PORT** holdings (`retrieve_nport` on cache miss: EDGAR, structured XML — parse without LLM) → scan holdings for entities carrying `type=fund(PC)` or interval-fund/BDC flags in the graph → indirect exposure claims.
   - **Known PC/interval fund in the lineup directly** → direct exposure, graph lookup only.
   - **CIT (collective investment trust)** → limited disclosure: report states "opaque vehicle; public filings do not disclose holdings" + link the fact sheet if retrievable. Honest-unknown, surfaced as such.
3. Assemble the report **from published edges and claims only** — the analysis step does no new asserting, only composing: exposure table, each line citing its filing (5500 row / N-PORT / 10-K), jargon-decoder blocks (gates, PIK) attached by claim type, and the compliance framing (informational, no recommendations).
4. Deliver + attach a **monitor**: entity-watch rows on the plan and each lineup fund → future filing refreshes that change exposure fire an alert (the subscription product).

Marginal cost per analysis ≈ a few resolution calls + cache misses; the expensive work was B1's seeding.

## Scenario B3: Ongoing — Filing-Season Refresh

**Beat schedule (PC):**

| Task | Cadence | Behavior |
|---|---|---|
| EDGAR submissions poll per tracked CIK (BDCs, interval funds) | daily | New 10-Q/10-K detected → B1b chain for that filing → **diff vs. prior quarter**: new borrowers (new `lends_to` edges), departed loans (edge end-dated), non-accrual/PIK deltas (claim updates + alert events) |
| N-PORT refresh for funds appearing in user-monitored lineups | monthly cycle | Re-parse, diff holdings, alert on new PC exposure |
| Form 5500 annual bulk reload | yearly (staggered release) | Reload, diff lineups per plan → "your plan added Fund X" alerts |
| CAFR season sweep | annually per system's fiscal calendar | Re-parse, allocation trend claims (this year vs. last) |
| Stale-edge re-verification | weekly | Same as PE |

Diffing is the theme: ongoing PC work is **compare-new-filing-to-old-edges**, emit deltas as events, and events drive both data freshness and every alert product.

---

# PART C — CROSS-CUTTING MECHANICS

**Priority queues:** `on_demand` (user-facing, minutes) > `refresh` (scheduled) > `seed` (bulk). Same tasks, different queues and worker allocations.

**Idempotency everywhere:** claims keyed by hash(subject, predicate, object, doc_sha, quote) — retries and re-parses can never duplicate; re-running a filing is safe by construction.

**Event log:** every edge publication/retraction/confidence-change appends to an `events` table — the single feed powering Acquisition Alarm, plan-change alerts, the public changelog, and cache invalidation for claim cards.

**Review queue inflow:** ambiguous resolutions (A1), single-source edges (A1/A3), extraction conflicts, community submissions, numeric cross-check failures (B1b). Everything else flows lights-out.

**The flywheel, restated as data flow:** user searches (A2) prioritize crawling → crawling publishes edges → edges make searches instant → filings refresh (A3/B3) emit events → events drive alerts → alert subscribers fund the crawling.
