# Evidence Layer — Technical Build Plan
### Filing-grounded evidence engine for PE ownership claims and PC exposure claims — FastAPI/Python stack
### (Laravel equivalents noted throughout as a reference for a Laravel-fluent reader)

---

## 1. Architecture Principle (read this before anything else)

The system's trust guarantee comes from one rule enforced in code, not policy:

> **The LLM never finds facts. It only extracts facts from documents the pipeline retrieved, and every extracted claim must contain a verbatim quote that code mechanically verifies against the stored source document. Claims that fail quote verification are rejected automatically.**

Pipeline in one line:

```
Entity Resolution → Source Retrieval (deterministic) → LLM Extraction (cited) → Mechanical Citation Verification → Confidence Scoring → Graph Storage → ~~Human Review Queue~~ *(removed: no manual review, ADR 0002 (`docs/adr/0002-no-manual-review.md`))*
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
| PDF / table extraction | **pdfplumber** + **camelot**, in-process | (no good PHP option — would have been AWS Textract) | Schedule of Investments and CAFR tables parse natively; no sidecar, no per-page bill *(2026-11-16: BDC Schedules are read from Inline XBRL tags, not PDFs; CAFR tables still need this.)* |
| Bulk data | **pandas** / **polars** | `COPY` + raw SQL via `DB::` | Form 5500 CSVs → clean → Postgres |
| LLM | **Anthropic Python SDK** (Sonnet-class bulk, Opus-class escalation) | Anthropic PHP SDK / plain HTTP | Structured outputs pair with Pydantic |
| Search / fuzzy match | **Meilisearch** Python client + **rapidfuzz** | Laravel Scout + Meilisearch | Entity/alias matching (Stage 1) and consumer search (Stage 7) |
| Classifier (experimental) | **Jev** (TypeSafe AI "System One" model) behind a hand-written `classify()` interface in `app/core/` | — (no equivalent) | Fast, cheap, calibrated true/false and pick-from-a-list answers for routing and second-opinion checks. **Never creates claims.** Adoption decided per role in build_roadmap.md Step 27b |
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
| **Press release wires** | RSS/scraping (PRNewswire, BusinessWire, GlobeNewswire) + Google News RSS per entity *(2026-11-08, engine "Press and EDGAR full-text connectors": wire feeds are discovery only and releases are stored from issuers' own sites, SEC exhibits or adviser pages; Google News is dropped, blocked by robots.txt and its terms)* | Acquisition announcements with dates — the acquisition-date feature comes from here |
| **DSO / rollup location pages** | Scraping | The clinic-level roster that links "Bright Smiles of Croton" to "Smile Brands Inc." |
| **WARN notices** | State DOL pages, mostly scraping/CSV | Post-acquisition layoff evidence for the worker-side surface |
| **CourtListener RECAP API** | Free/nonprofit API | Litigation touching sponsors/portcos without paying PACER by the page |
| **Local news** | Google News RSS, GDELT (free) *(dropped 2026-11-08: Google News is blocked; GDELT deferred; past coverage awaits "Research: Web search APIs for finding a brand's past coverage")* | Small-market acquisition coverage national wires miss |

### 3.3 PC Evidence Connectors
| Source | Access | Yields |
|---|---|---|
| **SEC EDGAR — BDC filings (10-K/10-Q, N-2)** | Free API | Schedule of Investments tables: which fund lends to which company, at what rate, non-accrual status. The core PC dataset *(2026-11-16: 10-K and 10-Q only, no N-2; "BDC connector and Schedule parser".)* |
| **Form ADV (SEC IAPD)** | Free bulk data downloads | Private fund advisers, AUM, fund lists |
| **DOL Form 5500 + Schedule H** | Free bulk datasets (annual CSVs) | Every private-sector retirement plan's investment lineup — the backbone of the 401(k) exposure checker |
| **Public pension CAFRs/ACFRs** | PDF downloads from each system's site | Alternatives allocation %, sometimes fund-level commitments. Top ~100 systems first |
| **NAIC statutory insurance filings** | Partially free, partially paid via aggregators | Insurer PC exposure — later phase, hardest access |

### 3.4 Explicitly Out of Bounds
- **PitchBook / Preqin / CB Insights** — licensing prohibits building on their data, they're secondary sources (breaks the provenance premise), and consumers can't verify their citations. At most, one internal seat later as a lead-checking aid, never as a displayed source.

---

## 4. Database Schema (migrations to write first)

**Conventions every table follows** (ticket 04, 2026-11-05):
- `id bigint` identity primary key, internal only. Rows that appear in a URL (`entities`, `documents`) also carry `public_id`: 12 random Crockford base32 characters, unique, never reused.
- Enums are text columns with a named CHECK constraint generated from the StrEnum in `app/core/contracts.py`. Every value change is a hand-written migration that drops and re-adds the constraint, and a test fails if a live CHECK and its StrEnum differ. (Alembic autogenerate detects neither CHECK expression changes nor native-enum value changes.)
- A reference to another row is a foreign-key column or a join table, never ids inside JSONB. JSONB holds only payloads that point at no row (`documents.meta`, `claims.value`).
- snake_case, plural table names, `<singular>_id` foreign keys, join tables named after both tables, `_at` timestamps (`timestamptz`, UTC), `_date` calendar dates, `is_`/`has_` booleans. One SQLAlchemy `naming_convention` names every constraint and index.
- `created_at` (database default) on every table; `updated_at` on tables whose rows change.
- No deletes and no soft-delete flags on evidence and identity tables (documents, claims, edges, events, aliases, identifiers, addresses, industries). Corrections go through status, `retracted_at` and events. Operational tables (cache, crawl state, cost log) may prune; their owning tickets set retention.
- Money is `numeric`, never float, with its currency stated.
- Indexes: every foreign-key column; every uniqueness rule as a unique index (claim hash, strong identifiers, public ids); `edges` on `from_entity_id`, `to_entity_id` and a partial index on non-retracted edges; a trigram index on aliases only if "Entity resolution algorithm" picks `pg_trgm`. Any other index needs a slow query behind it.
- Tables defined in their own tickets: fetch log ("Document storage, fetch log and last-confirmed"), extraction requests and claim reads ("Extraction execution"; no batch or cache tables), registry and crawl state ("Rosters, portfolio pages and the registry"), `api_costs` and operational alerts ("Operational identity, budgets and guardrail values"), `failed_tasks` ("Celery topology"), the search demand log ("Search and the demand log").

```
entities
  id, canonical_name, entity_type (brand|company|location|family|investment_firm|fund|
      retirement_plan|insurer),
      -- 2026-10-26: what a thing is, not its role; owner_kind per ADR 0001
      -- 2026-11-05 (ADR 0005): business and rollup replaced by brand|company|location; family =
      -- one person or a family owning in their own name (no individual profiles, no identifiers)
  public_id, jurisdiction (nullable), status (active|merged|closed), merged_into_id (nullable),
  owner_kind (nullable), owner_kind_confidence (nullable: verified|reported),
      -- 2026-11-07 (ticket 14): both computed by code from owner_kind_evidence (higher rank wins;
      -- a same-rank contradiction leaves owner_kind null = "owner type not confirmed"); only
      -- companies, investment firms, funds, families and insurers carry one, never brands or
      -- locations. Rank 1 → verified; ranks 2-3 → reported (ADR 0001).
      -- 2026-11-07 (ticket 65, "Funds and their investment firm"): a fund with no kind evidence of
      -- its own takes the owner_kind of the firm that manages it (current managed_by edge),
      -- computed by code with no evidence row; verified only if that edge and the firm's kind
      -- are both verified. Kind never flows up (fund → firm, or firm → listed parent). One
      -- investment_firm = the firm as the public names it, holding each adviser registration's
      -- crd; a listed parent (Blackstone Inc.) is a separate company above it by owned_by.
  created_at
      -- 2026-11-06 (ticket 13): status set only by code. closed = stopped existing (a moved
      -- location leaves a closed one); nothing sets it at launch, the store-map follow-up sets it
      -- from locator diffs. A merge adds a pointer and rewrites nothing: the duplicate gets
      -- status = merged + merged_into_id, keeps its claims and identity rows, and reads follow the
      -- pointer to the end. The older entity (lower id) survives; the duplicate's public_id
      -- redirects (301). Merges come only from code: an identity record whose strong identifiers
      -- belong to two same-type entities, a verified renamed_from, or "Entity resolution
      -- algorithm" rules; undone when the triggering identifier row or claim is retracted.
      -- Type changes: only company -> investment_firm|fund, when a Form ADV record matches.
      -- Merges, unmerges and type changes each write an events row.
      -- jurisdiction = place of formation, from a filing; company|fund|investment_firm only.
      -- canonical_name is picked by code from the entity's sourced names (ticket 12):
      -- company|fund|investment_firm|family: official filing > own site > own press_release >
      -- news; brand|location: own site first, then the same order; the newer document wins a tie.
      -- The input name (brand list, search, intake) shows until a document gives one.
      -- Names from Places are never stored.

entity_aliases
  id, entity_id, alias, alias_type (dba|legal_name|former_name), source_document_id,
      producer, producer_version, retracted_at (nullable)
      -- 2026-11-06 (ticket 13), all five identity tables (aliases, identifiers, addresses,
      -- industries, location_brands): never deleted; a newer document's value is current and
      -- old rows stay as history. retracted_at is set only when a whole producer +
      -- producer_version is withdrawn (one operator command after a code fix, then a re-run),
      -- with an events row; a retracted identifier undoes a merge it triggered.
      -- 2026-11-05: domain moved to entity_identifiers
      -- producer and producer_version: see claims (ticket 17); the same on every identity table

entity_identifiers             -- 2026-11-05 (ticket 12); replaces entities.place_id and .npi
  id, entity_id, scheme (cik|ticker|ein|crd|sec_file_number|private_fund_id|domain|phone|
      place_id|npi), value, source_document_id (nullable: place_id only, ADR 0003),
      ingest_item_id (nullable: domain only), producer, producer_version (both null when
      source_document_id is null), retracted_at
      -- (2026-11-06: the strong-scheme unique index skips rows with retracted_at set.)
      -- 2026-11-12 (ticket 30, "Rosters, portfolio pages and the registry"): a domain row may be
      -- sourced by a registry entry's intake item instead of a document (a CHECK allows
      -- ingest_item_id only on the domain scheme, and never together with source_document_id;
      -- place_id alone may have neither). Form ADV ingestion writes domain rows from the
      -- adviser's Website Address, skipping social media and reference sites (the monthly file
      -- keeps only the first of several websites, often LinkedIn). A registry entry's crd or cik
      -- only helps resolve it and is never written here. A domain removed from an entry gets
      -- retracted_at at the next sync, with an events row.
      -- strong schemes (cik, ein, crd, sec_file_number, private_fund_id, place_id, npi): one
      -- entity per (scheme, value); a second holder is a resolution or merge signal, never a
      -- second row. Weak schemes (ticker, domain, phone) may repeat. An entity may hold several
      -- values of one scheme: an investment firm holds one crd per adviser registration (ticket 65).
      -- sec_file_number = 801-|802-|814-; private_fund_id = 805-. phone only from stored
      -- documents, never Places. Added later: SoS entity number, license number and plan
      -- EIN+PN when their efforts start; trademark serial only if USPTO is
      -- adopted, which v1 doesn't do (ticket 64, 2026-11-17; the question moved to the parked
      -- non-PE owners map, ticket 88).

entity_addresses               -- 2026-11-05 (ticket 12)
  id, entity_id, kind (site|principal_office|mailing), street, city, state, postal_code,
      country, source_document_id, producer, producer_version, retracted_at
      -- site = a location's own address. Registered-agent addresses are never stored as an
      -- entity's address. Places-formatted addresses are never stored. Which address shows
      -- follows the canonical_name ranking above.

entity_industries              -- 2026-11-05 (ticket 12)
  id, entity_id, industry (one closed list in code), ingest_item_id (nullable),
      source_document_id (nullable), producer, producer_version (both null for an intake row),
      retracted_at
      -- brand|company|location only; zero or more each. Assigned by code from where the entity
      -- came in (an intake row, incl. a brand-list upload; or a document such as an NPPES record
      -- whose taxonomy code maps to an industry), never by the LLM, never a claim.
      -- 2026-11-05 (ticket 04): a CHECK requires exactly one of ingest_item_id and
      -- source_document_id. Chains values and display: chains-and-brands "Product categories" (2026-11-16: a brand's industries come only from the industry brand lists that include it, which are intake uploads; a brand can have several; the values are chosen in "Launch industries"; 2026-11-17, "Category brand lists and checked": lists only grow, a brand leaving its industry list only when discontinued or out of that industry).

location_brands                -- 2026-11-05 (ticket 15, "Predicate semantics")
  id, location_id, brand_id, source_document_id, producer, producer_version, retracted_at
      -- which brands a location trades under: identity data, never a claim, never an ownership
      -- hop, no confidence. Written only by code producers (store locators, rosters), so the
      -- source document is required. Unique (location_id, brand_id, source_document_id); a
      -- Taco Bell/KFC combo store has two rows. Retiring an old row: "Entity lifecycle".

documents                      -- immutable once written
  id, source_type (nppes|form5500|form_adv|sec_filing|irs_exempt_org|sos|license_board|cafr|
      company_site|press_release|news),   -- ADR 0003; fetch method (bulk|api) + connector go in meta
  public_id, url, retrieved_at, sha256, storage_path, mime_type, raw_text (nullable), meta JSONB,
  domain, published_on (nullable), last_seen_at, text_sha256, text_extractor_version,
  parent_document_id (nullable), speaker_entity_id (nullable)
      -- 2026-11-08 (ticket 24, "Source independence and syndication"; ADR 0002 amended):
      -- speaker_entity_id (nullable) = the organization whose words the document is: the entity
      -- holding the document's domain as an identifier, a press release's issuer (wherever the
      -- copy sits), an adviser or a filer; null means the domain itself is the speaker (a news
      -- outlet). Independence at scoring: one source per speaker group, where for a hop the owner,
      -- its controlling owners and the companies it controls (owned brand included) are one
      -- group, taken from the control relationships current when the edge is scored; the seller,
      -- advisers, outlets and regulators are separate. Within one edge's claims, the same quote of
      -- at least 80 characters (after normalization) from two speakers, or a wire tag in the text
      -- ("/PRNewswire/", "/GLOBE NEWSWIRE/", "(BUSINESS WIRE)"), makes the later document a copy
      -- with its original's speaker. No fuzzy matching. An edge's independent-source count is its
      -- number of separate groups.
      -- 2026-11-07 (ticket 20, "Document storage, fetch log and last-confirmed"): one row per URL,
      -- extracted text and extractor version: unique (url, text_sha256, text_extractor_version).
      -- sha256 = the stored bytes' hash; storage_path = documents/{sha256}, written once, never
      -- deleted, so identical bytes are stored once. domain = registrable domain (public suffix
      -- list), for "Source independence and syndication". retrieved_at = first fetch of this
      -- text; last_seen_at = the latest successful fetch of the same URL returning the same text
      -- (or a 304 Not Modified to a conditional request); new bytes with the same text are not
      -- stored. A URL's current version is its row with the newest last_seen_at; text that comes
      -- back after a change reuses its old row. ~~A hop's last-confirmed date is the newest
      -- last_seen_at among the documents its accepted claims cite.~~ (2026-11-12, ticket 30:
      -- corrected; see edges last_confirmed_on.) A real text change makes a new row, which the
      -- LLM re-reads whole.
      -- published_on: from structured fields only (SEC filing date, feed publication date,
      -- datePublished / article:published_time, a bulk file's release date); never the LLM or
      -- HTTP Last-Modified. An undated claim's as-of date is published_on, else retrieved_at.
      -- Parents and children: a filing, a full locator response or a bulk file is a parent
      -- holding the original bytes; each citable part (a Schedule row's parsed-table text, a
      -- rendered locator record, a header plus data line) is a child with its own raw_text and
      -- parent_document_id. A child's url is its parent's stable address plus #row=<row key> (for
      -- a bulk file whose URL changes each release, the connector supplies a stable dataset
      -- address), so an unchanged recurring record is the same child. Children inherit domain
      -- and published_on. verify_citations searches only raw_text.
      -- Text: keep all visible text (only scripts, styles and hidden elements dropped; no
      -- boilerplate removal); PDFs get a page marker at each page break; JavaScript pages are
      -- stored as the rendered DOM with capture settings in meta. (2026-11-12, ticket 30, Q9
      -- option e: a new HTML extractor version keeps the text of hidden elements too (closed
      -- dialogs, hidden modals and panels, CSS-hidden sections) and writes each image's alt, each
      -- link's title and each aria-label into the text where the element sits, as
      -- "[image: Arby's]" and "[link: Alexia]"; scripts and styles are still dropped; class names
      -- and data attributes never become text. Portfolio pages put names only in these attributes
      -- on five of eight surveyed sites.) A fixed extractor applies to new
      -- fetches; re-extracting old documents is a deliberate re-run that creates new rows.
      -- RawDocument (contracts.py) gains published_on; a child names its parent and row key.
      -- S3: document bytes under documents/; operational files (Anthropic batch files, crawl
      -- caches) under a separate prefix with retention set by their tickets; the production
      -- documents bucket uses versioning plus object lock ("Hosting, storage and deployment").

fetches                        -- 2026-11-07 (ticket 20); operational, rows kept 90 days
  id, url, fetched_at, outcome (ok|not_modified|failed|blocked|not_found), http_status
      (nullable), error (nullable), document_id (nullable)
      -- one row per fetch attempt; feeds the operator report and source_runs failed/blocked
      -- outcomes. Connectors send the server's ETag or Last-Modified back (conditional requests).
      -- After 90 days, documents.last_seen_at carries the confirmation record. (2026-11-12,
      -- ticket 30: for registry pages the saved ETag and Last-Modified live on crawl_targets;
      -- which sites block the bot, and since when, lives on site_access.)

claims                         -- atomic, cited assertions
  id, subject_name, subject_entity_id (nullable), predicate (acquired_by|owned_by|lends_to|
      holds_position|allocates_to|operated_by|renamed_from|managed_by),
      -- 2026-11-06 (ticket 18): subject_name/object_name = the name as written in the document
      -- (the LLM never returns ids; a keyed code-producer claim takes its identity record's main
      -- name). Claim content (names, quote, value, document) never changes. The entity ids are
      -- the resolver's current answer: the door fills them in the same call; null when a name
      -- is ambiguous (retried automatically when identity data changes, ADR 0002) or, for
      -- renamed_from, the object. Code may change an id when the resolver's rules improve, with
      -- an events row and an edge recompute. A null id never counts toward an edge. An unmatched
      -- name creates a company, or a family when the LLM marks the side as a person or family;
      -- claims never create brands, locations, investment firms, funds, insurers or plans.
      -- 2026-11-05 (ticket 15): operates_location_of renamed operated_by. Every claim reads
      -- subject → object. Role table (contracts.py), subject → object, hop?:
      --   owned_by, acquired_by: brand|company|investment_firm|insurer → company|fund|
      --     investment_firm|family; ownership hop (the two back the same hop)
      --   operated_by: location → company; ownership hop
      --   lends_to: fund → company; holds_position: fund|retirement_plan|insurer → company|fund;
      --   allocates_to: retirement_plan|insurer → fund; none of these three is a hop
      --   managed_by: fund → investment_firm (2026-11-07, ticket 65); never a hop; one manager at
      --     a time (a newer claim naming a different firm ends the older edge). Producers: the
      --     Form ADV ETL (archive fund rows; each in-graph firm's current IAPD PDF fund list), the
      --     LLM ("managed by", "advised by", "its affiliate, <fund>"), BDC 10-Ks.
      --   renamed_from: any entity → no object (2026-11-06, ticket 13); value.former_name is the
      --     old name, which must appear in the quote; an accepted claim makes code write a
      --     former_name alias; a same-type entity under the old name merges only once the rename
      --     is verified; never a hop. object_entity_id is nullable for renamed_from only.
      -- 2026-11-07 (ticket 65): the role-table check runs when edges are built, not when a claim
      -- is accepted. A claim whose quote passes is accepted; its edge forms only once the current
      -- entity types fit (a company later typed fund by a Form ADV record), as a null id never
      -- counts. A type mismatch no longer rejects with sanity_check_failed.
      -- ruled 2026-09-14: majority/minority stake is degree, not relationship —
      -- it lives in `value` (e.g. {"stake_pct": 65, "stake_type": "majority"}), matching
      -- how lends_to @ rate and allocates_to @ % already work. Canonical set: CLAUDE.md.
      -- 2026-11-06 (ticket 16): value schemas, one Pydantic model per predicate (extra="forbid"),
      -- used by ExtractedClaim and code producers; every field optional unless noted:
      --   owned_by, acquired_by: stake_pct (0-100), stake_type (majority|minority, only when the
      --     document uses the word), stake_basis (voting|economic). acquired_by adds deal_status
      --     (announced|completed|terminated); only completed backs an ownership hop; event_date is the
      --     announcement or closing date to match. owned_by's event_date is the as-of date the
      --     quote states; null means the document's date confirms the hop.
      --     2026-11-07 (ticket 25): owned_by adds holding (current|former, default current); a
      --     former claim records a seller or an exit ("acquired the company from affiliates of
      --     Wafra Inc.", "Realized: ..."). acquired_by adds expected_close_text on announced claims
      --     (the closing phrase as written, in the quote; ticket 26), which code maps to the pending
      --     edge's expected_close_from/to from a phrase table, relative phrases anchored to the
      --     document's date (published_on, else first fetch): a quarter or half, a month, "by
      --     {date}" or "by year-end", "in the coming days" +1 month, "in the coming weeks" +3
      --     months, "shortly/soon/promptly" +3 months, "in the coming months" +6 months, "later this
      --     year" to December 31, "early/mid/late {year}" Jan-Apr/May-Aug/Sep-Dec. Unknown phrases go
      --     to the operator report; a newer announced claim moves the range. terminated = the quote says the deal was called off; it
      --     ends a pending deal for that pair.
      --   lends_to: instrument (as written), reference_rate, spread_pct, interest_rate_pct,
      --     pik_rate_pct, floor_pct, principal, cost, fair_value, currency, scale, non_accrual,
      --     maturity_date, affiliation (non_affiliate|affiliate|control).
      --   holds_position: instrument, units, cost, fair_value, currency, scale, affiliation.
      --   2026-11-16 (ticket 36): lends_to and holds_position add other_name (a trailing dba, aka or
      --   bare parenthesis from the name cell, as written, e.g. "dba Dental365"); it never makes an
      --   ownership claim. A control-section equity row also gives owned_by (stake_basis voting, no
      --   stake_pct). Mapping from the tags: "BDC connector and Schedule parser" (§5).
      --   BDC rows: event_date = the Schedule's period end. Amounts in full units with currency
      --     (required when an amount is present) and scale (1|1000|1000000, the table's "(in
      --     thousands)" factor); rates are percent numbers (5.25 = 5.25%).
      --   renamed_from: former_name (required). operated_by: none. managed_by: none. allocates_to: defined when
      --     the retirement map unparks.
      -- Values over time are new claims, never edits: each filing gives a new claim; the edge
      -- shows the newest accepted claim by as-of date (event_date, else the document's date);
      -- same as-of date -> the later-filed document wins. A BDC is a fund with an 814- number.
      -- 2026-11-07 (ticket 25, "Conflict, succession and co-investors"; ADR 0001 and 0002 amended):
      -- Ownership stakes at the same as-of date: an official filing beats a non-official source,
      -- else the later-filed document; two non-official stakes on opposite sides of 50% make the
      -- hop's control sources_disagree. The newest stake decides control or minority; a stated
      -- 0% is an exit. A hop ends only by (1) a former claim for that pair (naming a firm as
      -- seller ends hops to the firm and all its funds), (2) a completed acquisition stating a
      -- stake that can't be true beside the owner's stated stake, or (3) 18 months without
      -- confirmation; every other overlap is co-ownership. A fund's stake for these rules is the
      -- sum of its firm's funds' stated stakes (except within one 13D or 13G joint filing, where the
      -- joint-filer rule applies: ticket 70). Within one document a current claim beats a
      -- former claim for the pair; a quote that names the seller and says it keeps a stake gives
      -- only the current claim (the hash ignores value). Undated claims take the document's own
      -- date, else the fetch date, and never restart a hop a dated claim ended. Dates compare at
      -- the coarser precision; a tie goes to the later-dated document. operated_by and
      -- managed_by hold one at a time: a newer claim naming a different company ends the older
      -- edge. Conflicts: stated stakes that can't all be true at once (or, for one-at-a-time
      -- predicates, two companies with the same date), plus loops; lends_to and holds_position
      -- never conflict.
      -- 2026-11-07 (ticket 27, "Category precedence and public companies"; ADR 0001 amended):
      -- above a public company, a minority ownership hop counts toward PE only when one of its
      -- claims comes from a 13D, or from a 13G not filed under Rule 13d-1(b). The 13G producer
      -- copies the rule box from the filing's structured field designateRulePursuantThisSchedule-
      -- Filed (and the reporting-person type) into document meta. Proxy-table claims confirm a
      -- holder but never create such a hop. A 13D or 13G amendment reporting 5% or less ends the
      -- holder's hop. Control uses the stated voting stake first (unstated basis = voting).
      -- Category precedence, co-owners, unconfirmed owners and confidence: ADR 0001.
  object_name (nullable), object_entity_id (nullable), event_date (nullable),
  event_date_precision (nullable: year|month|day),
      -- 2026-11-06 (ticket 21): event_date is the first day of the period the document gives
      -- ("2019" → 2019-01-01 with precision year), so a year is never read as January 1.
  value JSONB (amounts, %, rates),
  document_id, verbatim_quote TEXT, quote_start, quote_end, claim_hash,
      -- 2026-11-06 (ticket 18): quote_start/quote_end are character offsets into the document's
      -- stored raw_text (mapping from normalized text: "Citation verification rules"); page comes
      -- from page markers in the stored text. claim_hash = sha256 of [subject_name, predicate,
      -- object_name or "", document_id, verbatim_quote], whitespace collapsed; no entity ids,
      -- producer or value. Unique index on claim_hash where status <> 'retracted'.
  producer (llm|parser|etl|selector), producer_version, extraction_model (nullable), extracted_at,
  extraction_request_id (nullable),
      -- 2026-11-05 (ticket 17): producer_version = the prompt version (llm), a module constant
      -- (parser, etl) or the selector config revision; the producer declares it and golden-fixture
      -- tests force a bump when output changes. extraction_model is null except for llm. The task
      -- sets all three, never the model's output.
      -- 2026-11-15 (ticket 22): for llm, producer_version = the prompt version plus the model name
      -- sent (p8/deepseek-flash), so a model change is a new version; extraction_model = the model
      -- name the API returned (a change under the same sent name raises an alert);
      -- extraction_request_id = the request whose answer gave the claim (null for code producers).
      -- producer_version is the first version that found the claim; claim_reads lists every read
      -- that found it.
  status (pending|accepted|rejected|retracted),
  rejection_reason (nullable: quote_not_found|sanity_check_failed|unsupported)
      -- ruled 2026-10-26: pending = awaiting verify_citations; accepted = passed every check,
      -- eligible for edges; retracted = withdrawn by a later correction (events row).
      -- quote_verified BOOL dropped (implied by status). New filters add a reason, not a status.

edges                          -- the published graph (derived from claims)
  id, from_entity_id, to_entity_id, relation, effective_date,
      -- from = the claim's subject. relation is never acquired_by: acquired_by and owned_by
      -- claims publish one owned_by edge (ticket 15). managed_by edges (fund → firm) are never
      -- hops; a fund and its firm, or two funds of one firm, count as one PE owner (ticket 65).
  confidence (verified|reported|sources_disagree),
      -- 2026-11-07 (ticket 28): estimated dropped (no rule produced it; the retirement map may
      -- add it back when it unparks). unknown is not a confidence value.
      -- 2026-11-07 (ticket 25): sources_disagree marks a contested edge, never shown as fact; the
      -- card lists each side with links. A brand's category is sources_disagree only when the
      -- contested readings give different categories. A fund with disputed managers inherits a
      -- kind only if every disputed manager has the same kind.
      -- ownership_type removed 2026-10-26 (ADR 0001): owners carry owner_kind; each business's
      -- category + separation degree are computed by code from its ownership chains.
  published_at, retracted_at (nullable)
      -- 2026-11-05 (ticket 04): supporting_claim_ids JSONB replaced by edge_claims.
  phase (pending|active|unconfirmed|ended), started_on (nullable), started_on_precision
      (nullable: year|month|day), ended_on (nullable), ended_on_precision (nullable),
      end_reason (nullable: seller_or_exit|superseded_by_stake|replaced|absent_from_list|
      terminated|pending_expired|fund_closed), ended_by_document_id (nullable), last_confirmed_on,
      value_claim_id (nullable), value_document_id (nullable), expected_close_from (nullable),
      expected_close_to (nullable)
      -- 2026-11-16 (ticket 36, "BDC discovery and Schedule of Investments parsing"): one lends_to
      -- edge per BDC (or venture) and borrower pair, one holds_position edge per pair; each
      -- Schedule row is its own claim. For these edges value_document_id is the newest Schedule's
      -- filing, value_claim_id stays null, and the card reads that filing's claims for the pair
      -- (every tranche). fund_closed: the BDC filed an N-54C or Form 15; its open lends_to,
      -- holds_position and control owned_by edges end as of its last Schedule's period end.
      -- 2026-11-07 (ticket 26, "Edge lifecycle: ending, retraction and staleness"): one row per
      -- ownership period (sold in 2019, bought back in 2024: two rows); at most one open
      -- (non-ended, non-retracted) row per (from, to, relation). A row changes in place, with an
      -- events row per visible change (confidence, phase, end, value); effective_date is
      -- superseded by started_on. value_claim_id = the claim whose value the edge shows (the
      -- newest accepted claim by as-of date, ticket 16). pending = an announced acquired_by (never
      -- counts toward a category); the same row turns active on completion with started_on =
      -- the closing date; terminated or 18 months without completion (pending_expired) ends it.
      -- expected_close_from/to come from the claim's expected_close_text (below). unconfirmed =
      -- a daily Beat sweep found last_confirmed_on over 18 months old: shown as "last confirmed
      -- {date}", not counted toward categories, back to active when a later document confirms
      -- it; it is not an end. Only ended rows feed "formerly PE-owned {years}".
      -- ~~last_confirmed_on = the newest last_seen_at among the documents its accepted claims cite
      -- (ticket 20).~~ 2026-11-12 (ticket 30, Q14): last_confirmed_on = the newest confirmation
      -- among the edge's accepted claims, where a claim confirms by its document's source_type:
      -- company_site documents (portfolio, about, detail and paged pages, which state the
      -- present) confirm through the document's last_seen_at, so they confirm again each time
      -- the page is seen with the company still on it; every other source type (press_release,
      -- news, sec_filing and the other official types, which report a dated event or state a
      -- holding as of a date) confirms only as of the claim's own date: its event_date, else the
      -- document's published_on, else retrieved_at. A 2021 deal release still online confirms
      -- through 2021, however often it is fetched. Newsroom releases are stored as
      -- press_release, never company_site. Page dates are not used to tell the two apart
      -- (WordPress stamps publish dates on ordinary pages). ended_by_document_id = the document that showed the end (the former claim's
      -- document; the clean Schedule that lacked a holding); null for pending_expired.
      -- Retraction follows claims: an edge is never retracted directly. Code retracts claims or
      -- identity rows, and an edge left with no accepted, correctly typed claims gets
      -- retracted_at and an events row, so re-derivation can't resurrect it. Triggers (events
      -- reasons): producer_withdrawn, entity_merged, entity_unmerged, claim_re_resolved,
      -- entity_type_changed. No hand endpoint (ADR 0002); takedowns are out of scope.
      -- Withdrawing a producer version (one operator command): retract its claims (2026-11-15,
      -- ticket 22: only those no other non-retracted read found, by claim_reads, so a fixed
      -- version can run first and no edge drops in between), set
      -- retracted_at on its identity rows (undoing merges they triggered) and document reads,
      -- recompute affected edges, write one events row for the command plus one per edge or
      -- category that visibly changed (none per claim), and queue a re-run with the fixed version.
      -- Disappearance (2026-11-16, ticket 36: also a control owned_by hop backed only by Schedule
      -- rows, ADR 0001; "clean" = no failed rows and totals add up; a partial Schedule ends nothing):
      -- a lends_to or holds_position edge ends (absent_from_list) when the fund's
      -- next Schedule parses cleanly and lacks the holding, as of that period end; one miss is
      -- enough; an unparseable Schedule proves nothing. Ownership never ends by absence. Stores
      -- and roster locations close after two complete crawls in a row miss them. A 404 or 410
      -- never ends anything alone. Recompute mechanics: "Category storage and recompute".

edge_claims                    -- which claims support which edge (ticket 04)
  id, edge_id, claim_id        -- unique (edge_id, claim_id)

~~review_items~~               -- dropped 2026-10-26 (ADR 0002). Its reasons now live elsewhere:
      -- single_source → edge confidence = reported; conflict → edge confidence sources_disagree, and
      -- the category sources_disagree only when the readings differ (2026-11-07, ticket 25);
      -- low_confidence → claim rejection_reason = unsupported; community_flag → not in the MVP.

owner_kind_evidence            -- 2026-11-07 (ticket 14, ADR 0001 amended)
  id, entity_id, kind (nullable), rank (1|2|3), phrase (nullable: the describing phrase as
      written), match_state (nullable: mapped|unclear|unknown), document_id, verbatim_quote,
      quote_start, quote_end, producer, producer_version, status (pending|accepted|rejected|
      retracted), rejection_reason (nullable), retracted_at (nullable)
      -- Rank 1 rows come from code producers (Form ADV Any PE Funds = Y, a ticker from an SEC
      -- filing, the IRS exempt-org file, an 814- number); their phrase and match_state are null.
      -- 2026-11-07 (ticket 65): kinds private_equity (renamed from pe_firm), venture_capital and
      -- real_estate. More rank-1 rows: a fund's Form ADV archive Fund Type (Private Equity →
      -- private_equity, Real Estate → real_estate, Venture Capital → venture_capital, hedge,
      -- securitized asset, liquidity → other_investment_fund, Other Private Fund → no row); a
      -- firm's monthly counts by fund type (any PE fund → private_equity; all real estate or all
      -- VC → that kind; any other mix → other_investment_fund); Y on any of a firm's registrations
      -- counts. Starting terms moved: venture capital firm/fund → venture_capital; real estate
      -- investment firm, real estate fund → real_estate.
      -- Ranks 2-3 come from the LLM's owner_descriptions: rank 2 when the document is on one of
      -- the owner's own domain identifiers or is a press release it issued, else rank 3. Their
      -- kind is code's current answer from the term table (terms matched inside the phrase,
      -- case-insensitive, longest term wins; a negation or two kinds → no kind), recomputed when
      -- the table changes; phrase and quote never change. Rows enter through the door and quotes
      -- pass verify_citations. Within one source, the newer document wins.

document_reads                 -- 2026-11-07 (ticket 28, "What 'checked' means and coverage states")
  id, document_id, producer, producer_version, outcome (cited|no_evidence_found|unreadable|
      claims_rejected), read_at, retracted_at (nullable)
      -- one row per document per producer version, written in the producer's door call. cited =
      -- at least one accepted claim; no_evidence_found = read in a finished response, no claim
      -- cites it (ticket 21); unreadable = unparseable filing or failed response; claims_rejected
      -- = claims were made but all failed verify_citations. A new producer version leaves earlier
      -- rows standing; withdrawing a version sets retracted_at on its rows ("Edge lifecycle").
      -- 2026-11-15 (ticket 22), llm: a new version's finished read of a document supersedes the
      -- older version's read of it (retracted_at set) and retracts the claims only older reads
      -- found; a failed new read leaves the old one standing. A document read in windows still
      -- has one row: the outcome is set when every window finished, and one failed window makes it
      -- unreadable.

extraction_requests            -- 2026-11-15 (ticket 22, "Extraction execution")
  id, document_id, window_index, window_count, producer_version, model_sent,
  model_returned (nullable), host, attempt, status (succeeded|failed),
  failure_reason (nullable: connection|server_error|timeout|rate_limited|balance_empty|
      key_rejected|bad_request|output_limit|empty|refusal|bad_json), finish_reason (nullable), input_tokens, output_tokens, reasoning_tokens,
  cached_tokens, seconds, sent_at
      -- one row per API call: a read is one or more windows, each up to three attempts, plus
      -- fallback calls during a DeepSeek outage (ticket 77). failure_reason (ticket 77): connection
      -- = no answer; server_error = 500, 502, 503, 504; rate_limited = 429; balance_empty = 402;
      -- key_rejected = 401; bad_request = 400, 422. "Down" is connection, server_error or timeout. The raw response is written once to S3 at extraction-responses/{id}.json
      -- and kept for good. Dollar cost: one api_costs row per call carrying this id ("Operational
      -- identity, budgets and guardrail values"). No cache table: before calling, code looks for a
      -- finished document_reads row for the document under the version. No batch tables.

claim_reads                    -- 2026-11-15 (ticket 22)
  claim_id, document_read_id   (unique together)
      -- every read that found a claim, the first included, for every producer. The claim hash
      -- ignores the version, so a claim found again by a later read keeps its row and gains a row
      -- here. Supersession and withdrawal retract a claim only when no non-retracted read found it.

api_incidents                  -- 2026-11-15 (ticket 77, "Extraction prompt rules")
  id, provider (deepseek|openrouter), reason (down|balance_empty|key_rejected), opened_at,
  closed_at (nullable), fallback_state (nullable: in_use|out_of_funds|down), last_status
  (nullable), last_error (nullable)
      -- one row per incident that stopped or rerouted reads: DeepSeek down (three "down" attempts
      -- on one document), DeepSeek's balance empty (402) or its key rejected (401). Closed by the
      -- 5-minute test request or balance check. fallback_state follows OpenRouter during a
      -- DeepSeek outage. The operator surface shows open rows and the reads waiting.

source_runs                    -- 2026-11-07 (ticket 28)
  id, entity_id, source, started_at, finished_at (nullable), outcome (completed|failed|blocked)
      -- one row per entity per required source run (the required list per entity type is the
      -- product's: chains "Brand-level checked: required sources and freshness", split off "Category
      -- brand lists and brand-level checked" on 2026-11-17). completed only when
      -- every document the run found has a non-retracted read of cited or no_evidence_found;
      -- failed = errors after retries; blocked = robots.txt or site terms. Shared sources
      -- (registry sponsor pages, press feeds, Form ADV, BDC Schedules) count through their latest
      -- complete pass that finished after the entity was added; an incomplete pass leaves the
      -- previous one in force; a failing item leaves a pass's list only by a code change. An
      -- entity is checked when every required source has a completed run, judged against the
      -- list in force when it ran; the checked date is the oldest of those runs. Until then only
      -- pe_owned and pe_minority_stake can show; everything else reads not_yet_checked (ADR 0001).
      -- How the checked date reaches stored categories: "Category storage and recompute".

entity_categories              -- 2026-11-07 (ticket 68, "Category storage and recompute")
  id, entity_id (unique), category, confidence (verified|reported), checked_on (nullable),
      deciding_owner_id (nullable), computed_at
      -- one current row per brand (companies and locations only when a product needs them),
      -- changed in place. An events row only when category or confidence changes; checked_on
      -- (the oldest completed required run, ticket 28) advances quietly on each re-check. No
      -- complete check gives not_yet_checked unless PE was found; a withdrawal falls back through
      -- the same recompute. deciding_owner_id = the owner whose chain decided the category.

entity_pe_owner_periods        -- 2026-11-07 (ticket 68)
  id, entity_id, pe_owner_id, separation_degree, stake_role (control|minority), confidence,
      phase (active|unconfirmed|ended), started_on (nullable), ended_on (nullable),
      end_reason (nullable)
      -- one row per brand, PE owner and period (ADR 0001's stored row). pe_owner_id = the firm, or
      -- the fund when it has no managed_by edge (ticket 65); separation_degree = the shortest
      -- path; started_on = the latest of the chain's hop starts. Ended rows are the "formerly
      -- PE-owned {years}" history; an unconfirmed row shows "last confirmed {date}". Chains are
      -- not stored: the card walks the edges on read.
      -- Derivation order: owner kinds (including kinds funds inherit from their firm), then edges
      -- (re-derived only for the touched pairs and relations; events only on visible change),
      -- then categories and PE owner periods for every brand reached by walking edges downward
      -- from the changed entity, each brand in its own Celery task, queued in chunks (size:
      -- "Operational identity, budgets and guardrail values"). Triggers: a visible edge change
      -- (including phase), an owner kind change, a check completing or withdrawn, a merge,
      -- unmerge, type change or re-resolution. A recompute is a pure function of current edges,
      -- owner kinds and source runs. A nightly task recomputes every stored brand from scratch;
      -- any difference is fixed with events rows and raises an operational alert (a missed
      -- trigger is a bug).

ingest_batches / ingest_items  -- operator uploads only (decisions.md §15: no on-demand research)
  batch: id, name, status (running|done|halted)
      -- 2026-11-05 (ticket 04): halted = stopped by the spend cap or the operator; unfinished
      -- items keep a null result. No counts column (computed on read); submitted_by dropped.
  item: id, batch_id (required), input_name, input_entity_type (brand|company|location),
        input_industry, input_street, input_city, input_state, input_postal_code, input_domain,
        resolved_entity_id, result (resolved|ambiguous|failed)
      -- every input_* except input_name, resolved_entity_id and result are nullable.
      -- 2026-10-26: no "not found" (a miss creates an entity). The automatic re-attempt
      -- selects result = ambiguous.
      -- 2026-11-05 (ticket 04): stage dropped; result null = waiting or resolving. failed = an
      -- error during resolution after tenacity retries (→ dead letter); later failures belong
      -- to the entity's research. Raw CSV rows are not kept.

ingest_item_candidates         -- 2026-11-05 (ticket 04); replaces ingest_items.candidates JSONB
  id, ingest_item_id, entity_id, score   -- set only when result = ambiguous

registry_entries               -- 2026-11-12 (ticket 30, "Rosters, portfolio pages and the registry")
  id, slug, name, ingest_item_id, entity_id (nullable), synced_at, removed_at (nullable)
      -- one row per registry YAML file (registry/<slug>.yaml, one per organization), loaded by
      -- the registry sync command on deploy. Each sync sends the entry through the door as an
      -- operator intake item (name, identifiers, domains), resolved like any intake row;
      -- entity_id is that resolution's current answer. Crawl state, not evidence: rows change in
      -- place; an entry deleted from the repo gets removed_at.

registry_pages                 -- 2026-11-12 (ticket 30)
  id, registry_entry_id, url, role (portfolio|newsroom|about), render (http|browser),
      paging_param (nullable), detail_links (nullable), required, status_selector (nullable),
      removed_at (nullable)
      -- one row per page listed in an entry. render = browser for pages whose names appear only
      -- after JavaScript (L Catterton). paging_param names the query parameter for further pages
      -- (Golden Gate's sf_paged). detail_links = a URL pattern for per-company pages or releases
      -- to follow one level deep on the same site. required = false for a page walled when the
      -- entry was researched: tried every pass, not waited for. status_selector names the
      -- status-only selector config, where one exists ("Selector producers: store locators and
      -- rosters"); a server-side status filter view (TSG's ?status=exited) is listed as its own
      -- page with a selector. A page removed from the YAML gets removed_at.

crawl_targets                  -- 2026-11-12 (ticket 30); operational crawl state
  id, registry_page_id, url, discovered_on_target_id (nullable), etag (nullable),
      last_modified (nullable), last_fetched_at (nullable), last_outcome (nullable:
      ok|not_modified|failed|blocked|not_found), consecutive_failures, last_linked_at (nullable)
      -- one row per URL fetched again each pass: listed pages, their paged URLs and discovered
      -- detail pages (discovered_on_target_id = the page that linked it; null for listed pages).
      -- etag and last_modified are sent back as conditional requests. consecutive_failures feeds
      -- the operator report. last_linked_at = the last pass whose listing still linked a detail
      -- page; a detail page unlinked for two passes stops being fetched (its last confirmation
      -- stands). Release URLs are fetched once and are only documents, never targets. Changes in
      -- place; the evidence trail stays in documents and fetches.

affiliate_links                -- 2026-11-17 (chains "Alternatives and affiliate links")
  id, brand_id, store (the brand itself, or a retailer: amazon|walmart|target|...), url,
      program (direct, or the network: impact|cj|rakuten|...), ingest_item_id, added_at,
      removed_at (nullable)
      -- operator data uploaded in batches like brand lists; never through the claims door, never
      -- evidence. A link shows only while its brand qualifies as an alternative (a completed check,
      -- no PE in its ownership, no pending deal to a PE buyer); code hides it otherwise. A
      -- retailer link must land on the brand's own store or product pages there, never on search
      -- or category pages. Never a link for a PE-owned or PE minority stake brand. Dead links go
      -- to the operator report.

site_access                    -- 2026-11-12 (ticket 30); operational
  id, domain (unique), state (open|challenged|hard_blocked|robots_refused|rate_limited),
      blocker (nullable: cloudflare|vercel|akamai|imperva|datadome|other), blocked_since
      (nullable), last_checked_at, last_retry_cleared_at (nullable), required_pages,
      optional_pages
      -- one row per domain the bot fetches from; state from the latest pass. hard_blocked (an
      -- explicit refusal such as Cloudflare's "Sorry, you have been blocked", a plain 403) and a
      -- site asking us to stop both stop all fetching from the domain. last_retry_cleared_at =
      -- the last time the honest browser retry cleared a challenge. Feeds the blocked-sites
      -- dashboard ("API conventions and operator surface").

site_access_changes            -- 2026-11-12 (ticket 30); operational, kept indefinitely
  id, site_access_id, from_state, to_state, blocker (nullable), changed_at
      -- one row per state change only, so it stays small and gives each site's block history.
```

Key design points:
- **Claims are append-only; edges are derived.** Corrections retract an edge and add a new one — you never silently rewrite history, which is both your credibility story and your legal posture.
- **`verbatim_quote` + `status`/`quote_offset`** is the anti-hallucination mechanism, stored per claim.
- **`confidence`** on edges plus each owner's **owner kind** power the claim cards, including the honest "owner type not confirmed" and the Fiskars-isn't-PE taxonomy (ADR 0001).

---

## 5. Pipeline Flow — Step by Step (Celery tasks)

Everything below is a Celery task. Sequencing uses Celery `chain()` (≈ Laravel `Bus::chain()`), fan-out uses `group()` (≈ `Bus::batch()`), and "run X after all of these finish" uses `chord()` (≈ `Bus::batch()->then(...)`). Task names below use Python snake_case; the Laravel job-class name each replaces is shown in parentheses on first mention.

### Stage 0 — Intake
`create_ingest_batch` (was `CreateIngestBatch`) → accepts an operator upload of one row or a CSV of thousands (`name, entity_type, industry, street, city, state, postal_code, domain`; only `name` is required; ticket 04); pandas validates the CSV. Searches never create batches (decisions.md §15). Each row becomes an `ingest_item` and dispatches Stage 1 via a Celery `group()`. Queue: `intake` (monitored in Flower).

### Stage 1 — Entity Resolution (`resolve_entity`, was `ResolveEntityJob`)
1. Normalize input (strip punctuation, expand abbreviations).
2. Google Places lookup → address + place_id.
3. Healthcare? Match against the pre-loaded NPPES bulk census first (free, local); NPPES API only on census miss → organization NPI, authorized official, parent org name.
4. State SoS / OpenCorporates lookup → legal entity, registered agent, officers.
5. Fuzzy-match against existing `entities` + `entity_aliases` (Meilisearch + rapidfuzz scoring) to avoid duplicates.
6. Output: `entity_id` (created or matched) with aliases recorded. Ambiguous matches (score below threshold, deterministic tiebreakers exhausted) → item status `ambiguous`, candidates stored, nothing linked — never a guess, never a new duplicate (ADR 0002).

**This stage is where most real-world failure happens. Budget accordingly.**

### Stage 2 — Source Retrieval (`retrieve_{connector}` tasks, fan-out; was `Retrieve{Connector}Job`)
For the resolved entity + its aliases, dispatch one task per relevant connector inside a Celery `chord()` whose callback triggers Stage 3 (category-aware: a dental clinic triggers NPPES/DSO/portfolio/news connectors; a fund triggers EDGAR/ADV connectors).

Each connector task:
1. Queries/scrapes its source (httpx for APIs/static pages, Playwright for JS-heavy pages; per-domain rate limiting via a Redis token bucket; respect robots.txt; tenacity exponential backoff on 429/5xx). *(2026-11-15, engine "Form ADV and IRS exempt-org ingestion": robots.txt status codes follow RFC 9309 on every site: a 4xx other than 429 means no restrictions; a 5xx or an unreachable host means everything is treated as blocked and retried later.)*
2. Stores the raw document to S3 (boto3), computes sha256, writes a `documents` row via SQLAlchemy.
3. Extracts plain text (HTML → text via selectolax/BeautifulSoup; PDFs → pdfplumber; tables → camelot, structured JSON stored in `meta`). All in-process — no sidecar.
4. Skips documents whose sha256 already exists (dedup).

*(2026-11-07, engine "Document storage, fetch log and last-confirmed": dedup is by URL and extracted text, not by sha256 alone. A re-fetch with the same text advances `last_seen_at` and stores nothing; a changed text is a new version, re-read whole. Parsed tables become child documents with their own `raw_text`, not `meta`. Every attempt is logged in `fetches`. See §4 `documents`.)*

Celery Beat (≈ Laravel Scheduler): recurring crawls of sponsor portfolio pages, DSO rosters, and news RSS to catch *new* acquisitions — this feeds the Acquisition Alarm feature.

### Press connector (2026-11-08, engine "Press and EDGAR full-text connectors")

- Wire feeds (PR Newswire and GlobeNewswire subject feeds) are read only to learn that a release exists: title, date and issuer (`dc:contributor`). Items are matched against tracked entities' names and aliases (whole words, exact phrases, case-insensitive); unmatched items are dropped unstored. Feeds are polled faster than they turn over their 20 items, with a daily backfill from the wires' news sitemaps.
- A matched release is fetched and stored from the issuer's own site (found through its domain identifiers, newsroom or sitemap, by matching title and date), an SEC exhibit or an adviser's page, never from a wire site. A wire-only release can't be a source. A stored issuer copy with no date of its own takes the feed item's date as `published_on`.
- A page on a wire domain (prnewswire.com, prweb.com, newswire.ca, globenewswire.com, businesswire.com, accessnewswire.com, accesswire.com, einpresswire.com) is `press_release`; elsewhere a page on the issuer's own domain or carrying a wire tag ("/PRNewswire/", "(GLOBE NEWSWIRE)", "(BUSINESS WIRE)") is `press_release`, otherwise `news`. The issuer sets `speaker_entity_id`; a news article's speaker is its outlet.
- Bot rules: CLAUDE.md scrape etiquette. EDGAR full-text search and ownership filings: their own ticket.

### EDGAR full-text search and ownership filings (2026-11-08, engine "EDGAR full-text search and ownership filings")

- Full-text search (`efts.sec.gov/LATEST/search-index`, undocumented; all electronic filings since 2001) runs per brand: one exact-phrase query per brand and company name, over 8-K with EX-99, S-1, S-4, 424B prospectuses, 10-K with Exhibit 21, 10-Q, DEF 14A, DEFM14A, SC TO and 425. Form D, 13D/13G (own reader) and BDC filings (the BDC parser) are left out. First run: newest first since 2001, up to 100 hits per name; refreshes fetch only filings since the last run. The SEC's 10 requests a second is shared across EDGAR connectors.
- Each hit's file is its own document: `meta` holds accession, form, filer CIK and filing date; `published_on` is the filing date. An EX-99 press release is `press_release` spoken by its issuer (ADR 0003); everything else is `sec_filing` and self-verifies. Every hit is read whole by the LLM, however long (developer's ruling; spend: "Operational identity, budgets and guardrail values").
- 13D and 13G: for each public company in the graph, its filings and amendments. Structured filings (since December 2024) are read by a `parser` producer: each reporting person is a child document rendered as sorted `field: value` lines, giving `owned_by` claims (holder name and CIK, percent of class, event date); the rule box (`designateRulePursuantThisScheduleFiled`) goes into document `meta`. Older text filings: code reads the cover-page checkbox; a box it can't read never makes the company PE minority stake; a 13D has no box and always counts.
- Joint filers: within one 13D or 13G, the owner's stake is the larger of the largest single aggregate amount and the sum of the reporting persons' sole voting power, with the percent from the same share count (a fund, its general partner, the firm and its listed parent usually report the same shares, so a plain sum double-counts). A newer filing replaces an older one by event date; an amendment reporting 5% or less ends the hop; 0% is an exit; percent of class counts as voting unless a proxy or prospectus gives voting power.

### Registry crawler (2026-11-12, engine "Rosters, portfolio pages and the registry")

- **The registry** is one YAML file per organization in the repo (`registry/<slug>.yaml`): investment firms, companies and brands whose own pages the engine reads. Fields: `name`; `identifiers` (crd or cik, used only to find the entity; *2026-11-15, engine "Form ADV and IRS exempt-org ingestion": an entry may list several CRDs, meaning those adviser registrations are one firm, and code merges their entities into one `investment_firm` under the entity-lifecycle merge rules*); `domains` (every domain the organization's own pages sit on); `pages`, each with `url`, `role` (`portfolio`, `newsroom` or `about`) and crawl fields (`render`, `paging_param`, `detail_links`, `required`, `status_selector`); and `research` (kind, parent, evidence URLs, `documented|reported|inferred` confidence, notes), which code never reads. Claude researches entries with the registry-research skill and the developer approves each by committing it (ADR 0002 allows this: the registry only decides where to look). `registry sync` loads the files into `registry_entries` and `registry_pages` and sends each entry through the door as an operator intake item; its domains become `domain` identifier rows (§4 `entity_identifiers`). Replaces the registry-research skill's old format and build_roadmap.md's `{domain, roster_url, selectors, js_required}`.
- **Who gets an entry:** every company or investment firm on a listed brand's ownership chain that has a portfolio page, newsroom or about page, plus each listed brand's own newsroom and about page. An operator gap report lists owners with no entry and listed brands with no newsroom or about page. Launch target: every owner on a listed brand's chain that publishes a portfolio page or newsroom has an entry.
- **Nothing from the registry reaches extraction.** The LLM sees a registry page like any page (text, URL, domain); the entry's role, name and research block never reach the prompt. A page's speaker is the entity holding its domain.
- **Portfolio and about pages** are `company_site` documents read by the LLM each time their text changes. Detail pages matching `detail_links` are followed one level deep on the same site; each is its own document, re-fetched every pass with conditional requests. Further pages come from `paging_param` (page 2, 3 and so on until a page adds no new items, capped at 50; value: "Operational identity, budgets and guardrail values"). Sitemaps are not used for portfolio pages. Where a page's items carry status only in markup (Roark's hidden "previous" section, LLCP's `data-status`, about 22 of 73 pages surveyed) or only through a server-side status filter (Golden Gate, BC Partners, Permira, Princeton, Freeman Spogli, TSG), a status-only selector writes name and status records alongside the LLM's read (Q9 option e; "Selector producers: store locators and rosters").
- **Listed means current** unless the page marks the item former in text; a page that says it mixes current and former holdings without marking which gives no claim for unmarked items, and their status comes from other sources ("Extraction execution" writes this into the prompt). A name missing from a page means nothing: ownership never ends by absence ("Edge lifecycle"), whether or not the page lists only current holdings.
- **Newsrooms:** the first crawl pages back through the index to the end of the archive; later passes fetch the index from the newest end and stop at the first index page with no new release links. Each release linked from the index (by `detail_links`) is fetched once as a `press_release` document spoken by the domain's entity; PDFs are read as PDFs; the LLM reads every release it hasn't read before (first-crawl spend cap: "Operational identity, budgets and guardrail values"). Releases are never re-fetched for confirmation (they confirm only as of their own date, §4 `edges`); checks that receipt links still work: "Retrieval fan-out, tracked entities and refresh cadence".
- **JavaScript:** `render: browser` pages are fetched by the bot's own Playwright browser and stored as the rendered page; everything else uses the plain HTTP client.
- **Challenges (Q11):** a fetch that returns a challenge page (Cloudflare's "Just a moment", `cf-mitigated: challenge`, Vercel's Security Checkpoint) gets one retry per page per pass in the bot's own Playwright browser: the bot's user agent, the browser as it ships (no stealth plugins, no faked fingerprint), no proxies, no solving services, no clicks or typing, waiting up to a fixed time (30 s suggested; value: "Operational identity, budgets and guardrail values") for the page to clear by itself. A page that clears is stored like any rendered page, with the cleared challenge noted in `meta`. A checkbox, a puzzle or a page that doesn't clear in time counts as blocked, and the next pass tries once more. A hard block or a site asking us to stop ends all fetching from that domain. robots.txt is read before any page, directly or through the same retry; if it can't be read, the whole site is blocked. Measured 2026-11-12 from a home IP: of 93 PE firm sites, 88 served a plain request, Warburg Pincus served the honest browser though it challenged the plain client, Ares had moved to an open domain, and Neuberger Berman (Vercel), Partners Group (hard block) and Anchorage (robots.txt) stayed closed (`.scratch/engine/research/portfolio-wall-survey.md`). The survey is re-run from production IPs before launch ("Hosting and deployment"). The project applies to Cloudflare's verified bot program with a Web Bot Auth signature ("Operational identity, budgets and guardrail values"). Getting around blocks stays out (CLAUDE.md); what to do about sites still walled is fog on the engine map ("Walled sites, later").
- **Passes:** one `source_runs` row per pass covers every required registry page plus the new releases its newsrooms list (a shared source, §4 `source_runs`). A page walled when its entry is researched is written with `required: false`; the operator report says when it starts serving, and a code change makes it required. A required page that gets walled later stays required until the operator report flags it and a code change marks it. Pass cadence: "Retrieval fan-out, tracked entities and refresh cadence".
- **The "sponsor registry crawl index"** (research_flows.md) is dropped: each pass reads every registry page whole, so nothing searches stored pages for a name.

### Form ADV connector (2026-11-15, engine "Form ADV and IRS exempt-org ingestion")
- **Advisers, monthly:** both SEC monthly files ("Information About Registered Investment Advisers and Exempt Reporting Advisers": registered advisers and exempt reporting advisers) are loaded each month by the `etl` producer. Only advisers that advise private funds come in: registered advisers answering Item 7.B yes (about 6,086 of 17,263 in November 2026) and every exempt reporting adviser (6,848). Each row gives an `investment_firm` identity record (CRD, SEC#, CIK, primary and legal names), rank-1 owner-kind evidence (`Any PE Funds = Y` and the counts by fund type, ticket 65), and a `domain` row from the first website (ticket 30). The first load runs before the first seeding pass. Each file is a parent; each adviser row is a recurring child keyed by the dataset address plus the CRD. Unchanged rows only advance `last_seen_at`, and an adviser that drops out keeps its entity and evidence.
- **Funds and advisers from the archive, once:** the FOIA archive (complete through 2024-12-31) gives the latest Schedule D 7.B.(1) row per 805- ID: a fund identity record, a `managed_by` claim to its adviser, and rank-1 kind evidence from Fund Type. Every adviser whose last filing reported a private fund also gets an identity record and kind evidence from that filing, dated with it, so firms that stopped filing are known.
- **Funds after 2024:** for each firm in a tracked brand's ownership chain (any phase, pending included), a `parser` producer reads the firm's current IAPD Form ADV PDF (`reports.adviserinfo.sec.gov/reports/ADV/{CRD}/PDF/{CRD}.pdf`): each fund's name, 805- ID and general partner come through as text, and the fund-type checkbox does not, so these funds take the firm's kind. It is read first when the firm enters a tracked chain, then again whenever the firm's Latest ADV Filing Date changes in the monthly file. A firm that leaves every tracked chain stops being re-read. Large firms' PDFs run to hundreds of pages (Leonard Green: 509 pages, 23 MB), read page by page.
- **One firm, several registrations:** joined only through the firm's registry entry, which lists its CRDs. Nothing groups registrations automatically; umbrella registrations are already one row.
- **Not loaded:** advisers without private funds; the IRS exempt-org file, moved to the local-businesses map (Form ADV ticket Q4).

### BDC connector and Schedule parser (2026-11-16, engine "BDC discovery and Schedule of Investments parsing")
- **Universe, monthly:** every entity with an `814-` file number that files a 10-K or 10-Q, listed, non-traded or private (about 187). The `etl` producer takes the union of the SEC BDC data-set CIKs and the yearly BDC Report, confirms each by an `814-` file number on a 10-K or 10-Q in its submissions JSON, and emits a `fund` identity record (`cik`, `sec_file_number`) plus rank-1 `owner_kind_evidence` for `other_investment_fund`.
- **Filings:** every 10-K and 10-Q; an amendment only when it carries a tagged Schedule (then it is a later-filed document for the period). No N-2s or prospectuses. A daily check of each BDC's submissions JSON finds new filings, parsed the same day. History: every tagged Schedule since the BDC began Inline XBRL tagging (August 2022 to May 2023 by BDC; about 2,400 filings). Untagged filings before that are not read.
- **Lender and borrower:** the lender is the BDC (a `fund`); its adviser connects only through `managed_by`, which the `llm` producer reads from each 10-K's Item 1 Business section, cut out by code as its own child document (internally managed BDCs give none). The LLM reads nothing else in BDC filings. The borrower is the company the row names. Chain: brand → company ← lends_to ← BDC → managed_by → investment firm.
- **Parser (`parser` producer, module `bdc_soi`):** reads the filing's own Inline XBRL document. One table row is one holding; values come from that row's tags with their scale (`scale` 3 = 1,000, 6 = 1,000,000); the name comes from the visible row. Each row is a child document keyed by the holding's identifier string; its `raw_text` is the row's visible cells in order, with name and description cells copied down from the borrower's first row where the filer left them blank, rendered by code. The claim quotes the whole `raw_text`. The hidden identifier groups a row's tags and is never quoted or used as a name. The SEC BDC data set is not a source.
- **Rows into claims:** loan rows give `lends_to` (BDC → borrower), equity rows give `holds_position`; an equity row under "Control investments" also gives `owned_by` (company → BDC) with `stake_basis: voting` and no `stake_pct`. Affiliation comes from section headings or footnote markers (filers never tag it per holding). Name as written: the name cell after the copy-down, minus footnote markers and appended tranche words; two names joined by "and" or "&", each ending in an entity suffix, give one claim per company with the same quote. A trailing parenthesis comes off the name: f/k/a or fka gives a `renamed_from` claim; dba, aka and bare parentheses go to `value.other_name` as written, never an ownership claim.
- **Joint ventures:** a venture schedule tagged inside the 10-Q is read with the venture as lender: the venture is a `fund` identity record named as written (schedule heading or identifier ending, e.g. "Emerald JV LP"), its rows give `lends_to` from the venture, and the BDC's stake row gives `holds_position` (BDC → venture). Untagged EX-99 venture schedules are not read.
- **Layouts:** generic rules first (blank name copies down; trailing "(n)" is a footnote; a heading or footnote matching a fixed phrase list sets affiliation); per-filer overrides in code, each with a real fixture from that filer, only where the rules fail. No hand step in production.
- **Outcomes per Schedule** (the BDC's own and each venture's): a row fails when its shown numbers differ from its tags after scaling, it has no name after the copy-down, or the door rejects its claim. Clean = no failed rows and fair values add up to the tagged total within the filer's rounding: claims publish and pairs missing from it end their edges. Partial = failed rows at or below the threshold, or totals off: claims publish, no edge ends from it, operational alert. Failed = above the threshold: nothing publishes, the read is `unreadable`, operational alert (ADR 0002). Threshold value: "Operational identity and guardrails".
- **Cross-check:** the SEC's monthly BDC data set is the independent copy. Build tests match each fixture filing's holdings to its rows (count and fair value per holding, by identifier); in production each monthly file is compared with that month's parsed filings and any difference raises an operational alert, never changing or withholding claims.
- **Closed BDCs:** an N-54C or Form 15 ends the BDC's open `lends_to`, `holds_position` and control `owned_by` edges as of its last Schedule's period end (`fund_closed`).

### Producers and the door (2026-11-05, engine "Claim producers and the claims door")

Four producers turn stored documents into output. Each one records itself in `producer`:

- `llm` is the default. It reads any page or filing text, sponsor portfolio pages included (Stage 3).
- `parser` reads BDC Schedules of Investments.
- `etl` reads bulk official files: Form ADV now, Form 5500 and NPPES when their efforts unpark.
- `selector` reads long lists where every record has the same fields, such as store locators and location rosters, through a per-site registry config. Store-locator JSON endpoints are allowed when robots.txt permits them and they feed the brand's public locator page.

Every claim, whatever produced it, quotes a stored document, enters as `pending` and passes `verify_citations`. Confidence comes from the source type, never from the producer. What counts as the quote:

- Page or filing text: an exact span of the document's text.
- A bulk row (header line + data line): the whole data line, exactly as in the file.
- A BDC holding: the row's parsed-table text. If the parser reads the SEC BDC dataset, each holding is a bulk row. *(2026-11-16, engine "BDC discovery and Schedule of Investments parsing": the parser reads the filing's own tags, never the data set; the row text is the visible row with blank name cells copied down, rendered by code, as in "BDC connector and Schedule parser".)*
- A roster item on an HTML page: the item's text, which must appear in the page's text.
- A store-locator JSON record: one document per record. Code writes the record's text as one `field: value` line per field, sorted, with nested fields dotted (`address.city: Atlanta`) and list items indexed (`brands.0: Dunkin'`). The quote is the lines the claim uses. `meta` records the rendering format's version and points at the full response, which is stored as the original.

**Identity records.** Code producers (`etl`, `parser`, `selector`) also emit identity records: what one document states about one entity's identity (names, identifiers, addresses, phone, domain, industry code, and for a location the names of its brands, which become `location_brands` rows). The LLM emits only claims. Identity records replace the old "resolution hints", "structured hints" and "enrichment structs". Nothing records "where to look next"; fan-out reads identity rows and claims.

**The door** is one in-process function in `app/core`, validated against `contracts.py`. There is no HTTP route. A producer makes one call per run: one per document for code producers, one per request for the LLM. Each call is one transaction and is idempotent. A call carries the ids of the documents the request read, producer and version, identity records and claims; code gives each read document that no claim cites the outcome `no_evidence_found` (ticket 21). Each identity record has a key such as `r1` that is only valid inside the call, and a code producer's claim can name its subject or object by that key. The door:

1. checks every identity value, as found, against the cited document's text (the quote normalization), and does not write a record with a missing value;
2. resolves each identity record to an entity and writes the sourced alias, identifier, address and industry rows, normalized for storage;
3. writes claims as `pending`, with each name as written resolved to an entity id in the same call (null when ambiguous; ticket 18). Their quotes are checked in Stage 4, after names are resolved.

**Code producer failures.** Every `etl` run first compares the file header with the expected columns and reads columns by name. Every `selector` run first checks that items still come back with the expected fields and roughly the usual count. A failed shape check stops the run before it writes anything and raises an alert. A per-record failure (a rejected claim or an unwritten identity record) raises an alert naming the producer, version and document, and the run keeps going. When per-record failures in one run pass the spec's threshold, the rest of the run stops. Rows already written can be found by `producer_version`.

### Stage 3 — LLM Extraction (`extract_claims`, was `ExtractClaimsJob`)
*(2026-11-15, engine "Extraction execution": rewritten. It replaced per-entity multi-document calls, Claude through the Anthropic SDK and Sonnet/Opus tiering. Measured on 157 test documents: research/extraction-model-comparison.md.)* Runs per document, not per entity: each stored document version is read once per producer version, whatever entity it was fetched for.

*(Experimental, Step 27b)* **Jev pre-filter:** before extraction, Jev answers a true/false question per document ("does this contain ownership, acquisition or lending evidence about X?"). Only positives are sent to Claude. It is adopted only if A/B testing shows near-zero loss of evidence-bearing documents.

1. One document per request, with no brand or entity named and nothing from the registry. A document up to 200,000 tokens goes whole; a longer one is read in windows of up to 150,000 tokens, split at block line breaks with 2,000 tokens of overlap. Quotes are checked against the whole stored text.
2. Call DeepSeek V4.1 Flash on DeepSeek's own API with httpx: JSON mode with the schema written in the system prompt, thinking on, output limit 120,000 tokens, 15-minute timeout. The system prompt comes first and the document last, so DeepSeek's automatic prefix cache covers the prompt. The answer is parsed item by item into Pydantic models; a bad item is dropped and logged before it can reach the DB (2026-11-15: `document_label` is gone; code sets the document from the request):
   - Emit claims only in the fixed predicate vocabulary.
   - **Every claim must include a verbatim quote copied exactly from the provided document.**
   - *(2026-11-15, engine "Extraction prompt rules")* The production prompt is the v8 test prompt plus that ticket's rules: a brand's owner is whoever owns its name (trademark notices claimed, licensors not licensees); no claims from "Prior to <firm>" sections, team experience, deals advised on or loans; phrases that name no owner ("privately owned", "run by family", "an affiliate of" alone, franchised stores, copyright lines) give nothing; a claim per named group member, never the group's stake; a shut-down business is a former holding. Approval is the developer's commit of the prompt file (`.scratch/engine/research/extraction-prompt-p9.md` until the build, then `app/core/` unchanged), after the approval check recorded in that ticket; every later prompt or model version passes the same check. *(2026-11-15, engine "Task: Draft prompt p9 and run the approval check": p9 also says that "we" in a company's own voice on its own site names the company, that supporting offices or practices is not owning their brands, that an agreed sale that has not closed is not an exit, and that "affiliate" counts only for an owner or seller named as an affiliate or a company formed for a deal.)*
   - ~~Classify ownership_type~~ — removed 2026-10-26 by ADR 0001 (`docs/adr/0001-ownership-category-computed-by-code.md`): the LLM never classifies ownership categories. It may only extract a quoted self-description of an owner (e.g. "Oak Ridge is a private equity firm"), the lowest-ranked owner-kind source. *(2026-11-07, engine "Owner kind": the response gains `owner_descriptions`, each with the owner's name as written, the describing phrase as written, the document label and the quote; a term table in code maps the phrase to a kind, never the model.)*
   - ~~If the documents contain no ownership/exposure evidence, return an explicit `no_evidence_found` result~~ *(2026-11-06, engine "ExtractedClaim and the extraction result envelope": the response is only `claims: list[ExtractedClaim]`, possibly empty. Code gives each document in the request that no claim cites the outcome `no_evidence_found`, and only from a response that finished and parsed. A bad item is dropped and logged; a response that stopped at the token limit or doesn't parse fails as a request and is retried, giving no document an outcome; a document cited only by dropped items gets no outcome.)*
3. ~~Model tiering: Sonnet-class for bulk; escalate to Opus-class when documents conflict or classification is ambiguous.~~ *(2026-11-15: one model, no escalation tier.)* Failures: an HTTP error or timeout, an output-limit stop, empty content, a refusal or content filter, or JSON that doesn't parse into the envelope. Up to three attempts with backoff; an output-limit stop is split in half once. ~~When the attempts fail on availability (server error, rate limit, timeout, payment error), one try through the fallback, DeepSeek V4.1 Flash 1017 through OpenRouter on DeepInfra, InferenceNet or CoreWeave (its reads carry their own version name, such as `p8/deepseek-v4.1-flash-1017`); a bad answer never switches. Then the read is `unreadable`, an alert fires and the source run stays incomplete.~~ *(2026-11-15, engine "Extraction prompt rules" Q11 to Q17, replacing that trigger:)* A bad answer (bad JSON, an output-limit stop, empty content, a refusal) or a request error (400, 422) never switches: after the attempts the read is `unreadable`, an alert fires and the source run stays incomplete. A daily sweep retries `unreadable` reads of the current version for 7 days.
   - **The fallback is only for DeepSeek being down:** no answer (a connection failure, the 15-minute timeout, DeepSeek's own close after 10 minutes without starting) or HTTP 500, 502, 503 or 504. A 429 slows down and retries on DeepSeek. A 402 (balance empty) or 401 (key rejected) pauses every DeepSeek read with an `api_incidents` row and an alert; a free balance check every 5 minutes resumes them once fixed.
   - **Outage:** three "down" attempts on one document open an `api_incidents` row for DeepSeek. While it is open, single new documents from routine crawls go straight to the fallback, DeepSeek V4.1 Flash 1017 through OpenRouter on DeepInfra, InferenceNet or CoreWeave (its reads carry their own version name, such as `p9/deepseek-v4.1-flash-1017`), and bulk work (the seeding pass, version re-reads, the daily sweep) waits for DeepSeek or the developer's command. A tiny test request every 5 minutes closes the row when DeepSeek answers, and waiting reads go back to it. When OpenRouter answers 402 or 403 for credits or the key limit, or is down, the row's `fallback_state` records it and reads wait; a free key-balance check every 5 minutes resumes them after a top-up. An outage never makes a read `unreadable`. About $0.009 per document through the fallback; the OpenRouter key limit is the spending cap.
   - **Alerts:** when an incident opens, when the fallback runs out of funds, and daily while one is open.
   - **Operator commands:** status (open incidents, waiting reads, the last test of DeepSeek and of the OpenRouter balance); check DeepSeek now; use the fallback (shows the waiting reads, their estimated cost and the key's remaining limit, and asks to confirm; funds running out leaves the rest waiting, and DeepSeek coming back takes the rest back); back to DeepSeek. A manual resume keeps the off-peak hold for bulk work unless it is run with "now" (peak price). The surface (CLI or page) is "API conventions and operator surface"'s.
4. ~~Write raw response to the claim rows (`extraction_model`, `extracted_at`).~~ *(2026-11-05: claims go through the door above; the task sets `producer = llm`, `producer_version` and `extraction_model`, never the model's output. 2026-11-15: also `extraction_request_id`; one `extraction_requests` row per call, raw response in S3, cost in `api_costs`.)*
5. Timing *(2026-11-15)*: bulk work (the first seeding pass, re-reads after a new version, the daily sweep) waits for DeepSeek's off-peak hours (prices double 01:00–04:00 and 06:00–10:00 UTC on weekdays); single new documents from routine crawls go at once.
6. Portfolio re-read *(2026-11-15)*: a document fetched from a registry `portfolio` page whose answer has no claim naming the page's owner is read once more, and both answers' claims are kept. Code triggers it from the registry role; nothing from the registry enters the prompt. A second read of every document is revisited with production numbers (it found about 5% more known facts in testing, at double the cost).
7. New versions *(2026-11-15)*: a new prompt or model version re-reads every document older versions read, queued when it ships, under the spend cap; each finished new read supersedes the older read of that document, and `claim_reads` keeps the claims both found. A weekly golden-document check alerts when answers drift; a silent model change behind DeepSeek's `deepseek-flash` name shows only there. Measured cost: about $0.0044 per document off-peak, about $45 to $54 per 10,000 documents.

### Stage 4 — Mechanical Citation Verification (`verify_citations`, was `VerifyCitationsJob`)
Pure Python, no AI:
1. For each claim, string-search `verbatim_quote` (whitespace-normalized) in the stored document text.
2. Found → record offset (status becomes `accepted` once all checks pass). Not found → **auto-reject** (`rejected`, reason `quote_not_found`) and log for prompt tuning.
3. Sanity checks: cited document actually mentions the subject alias; event_date is plausible; numeric values in `value` appear in the quote for PC claims.
4. *(Experimental, Step 27b)* **Jev claim-support check:** for claims that passed steps 1–3, Jev answers "does this verified quote support predicate P between S and O?" Low confidence sets the claim's status to `unsupported`: kept, never counted toward an edge (ADR 0002). Jev can only remove a claim from publication; it can never verify, publish or downgrade one.

### Stage 5 — Confidence Scoring & Edge Publication (`score_and_publish`, was `ScoreAndPublishJob`)
1. Group verified claims by (subject, predicate, object). *(2026-11-06, "Claim value schemas": an edge's value comes from its newest accepted claim by as-of date; older claims are its history.)* *(2026-11-05, "Predicate semantics": `acquired_by` and `owned_by` claims for the same pair form one group, published as an `owned_by` edge; `acquired_by` supplies the start date.)*
2. **Two independent documents agree → publish edge as `verified`.** ("Independent" = different `source_type` or different domains — a press release syndicated to five sites counts once.)
3. One source → publish as `reported` (labeled as one source on the card).
4. Conflicting claims (different controlling owners over overlapping dates) → no publication as fact; shown as "sources disagree" with links to each. *(Both updated by ADR 0002 (`docs/adr/0002-no-manual-review.md`).)* *(2026-11-07, engine "Conflict, succession and co-investors", ADR 0002 amended: a conflict is stated stakes that can't all be true at once; co-owners with no stated stakes never conflict; the contested edges get confidence `sources_disagree`.)*
4b. Recompute each affected business's category and separation degree from its chains and owners' owner kinds (ADR 0001 (`docs/adr/0001-ownership-category-computed-by-code.md`)).
5. `no_evidence_found` → business category `no_pe_evidence_found` *(2026-11-06: computed from the per-document outcomes by "Checked and coverage states")*, shown as "No PE evidence found (checked {date})" — never "independent" (ADR 0001).

### Stage 6 — Human Review (Starlette-Admin/SQLAdmin panel or small Vue app; ≈ Filament)
> **Superseded 2026-10-26 by ADR 0002 (`docs/adr/0002-no-manual-review.md`): there is no manual review.** Kept for history; the open items it used to absorb are listed in the ADR.

Reviewers see: the claim, the quote highlighted in the source document, the conflicting evidence if any. Actions: approve (publish edge), edit-and-approve, reject, request more retrieval. Every action audited. ~~Community submissions (from the Verified Ledger feature) enter this same queue~~ (community submissions not in the MVP, 2026-10-26) as `source_type = submission` documents and count as one source — they can corroborate but never solo-publish a `verified` edge.

### Stage 7 — Serving
- `GET /api/entities/{id}/card` → claim card: business category (+ separation degree per PE firm), sponsor, acquisition date, N sources with links *(2026-11-07, engine "Brand card, receipt and edge shapes": now the **brand card**. Sections, each shown only when non-empty: verdict (category, confidence, checked date or "not yet checked", ticker when a public company is in the deciding chain); PE owners (firm, funds, degree, control or minority, confidence; a listed parent or GP-stakes holder as a label on the firm); other owners; PE holders of a public company; disputes; pending deals with expected closing; last confirmed; "formerly PE-owned {years}"; the franchise note. Passive 13d-1(b) holdings never show. The walk branches at every owner and each path stops at its first PE owner; active chains show hop by hop. Each fact opens a **receipt**: verbatim quote, source name, domain and type, live link, `published_on`, first fetch and last-seen dates; archived copies are never served publicly except the row text of an official filing's or bulk file's child document; a dead link gets a fixed note; no reader label. Edges carry from, to, relation, phase, confidence, start and end with precision, `end_reason`, `last_confirmed_on`, current value, expected closing, independent-source count and receipts. The graph endpoint: "Graph endpoint and non-brand output shapes".)* + quotes, confidence.
- `GET /api/entities/{id}/graph` → recursive CTE (via SQLAlchemy `text()`) walking edges for the ownership-chain / money-flow visualization (cap depth, label each hop with confidence). FastAPI routers ≈ Laravel API controllers.
- Retraction/correction endpoint feeds a public changelog — corrections displayed, not hidden.

---

## 6. PE vs. PC: Same Pipeline, Different Muscles

| | PE evidence | PC evidence |
|---|---|---|
| Dominant problem | **Extraction from scattered prose** (press releases, portfolio pages, registries) | **Table parsing from structured filings** (Schedule of Investments, CAFR allocation tables, Form 5500) |
| Key stage | Stage 2 breadth (many connectors) + Stage 3 classification | camelot/pdfplumber table extraction *before* Stage 3; LLM interprets parsed tables |
| Claim shape | Ownership edges (`acquired_by`/`owned_by`, `operated_by`) | Financial edges with values (`lends_to` @ rate, `allocates_to` @ %, `holds_position` @ amount) |
| Extra layer | Ownership-type taxonomy (the misattribution fix) | Jargon decoder content keyed to claim types (gates, PIK, non-accrual) — written once, attached to every relevant card |
| Easiest wins | Sponsor/DSO rosters (national PE layer) × NPPES bulk census (national denominator) — their join is the launch map | Form 5500 bulk CSVs (no scraping!) + top-100 pension CAFRs |

Form 5500 deserves emphasis: it's a **bulk annual CSV download**, not a scrape — with pandas/polars you can load the entire universe of private-sector plan lineups into Postgres in a weekend, with no LLM involved (the government CSV *is* the structure). It's the fastest path to a working MyRetirementX-Ray demo.

---

## 7. Operational & Legal Guardrails

- **Immutable document archive** — every published claim links to a stored copy with retrieval date and checksum. This is the answer to both "prove it" and takedown pressure.
- **Two-source rule in code**, not policy (Stage 5).
- **Public corrections log** — retraction workflow, never silent edits. In a market allergic to overclaiming, visible corrections are a feature.
- **Scrape etiquette** — per-domain rate limits, identified user agent, robots.txt respect, prefer official APIs/bulk data wherever they exist. Most of your best sources (EDGAR, NPPES, Form 5500, CourtListener) are official and free — lead with those.
- **Cost controls** — ~~LLM spend is per-document-set per entity; cache extractions by document sha256 so re-runs are free; batch API pricing for the big seeding runs. Rough planning figure: a few cents to a few tens of cents per entity depending on document volume — real money at 100k entities, trivial at pilot scale.~~ *(2026-11-15, engine "Extraction execution": each document version is read once per producer version, whatever entity it serves, and a same-text re-fetch costs nothing; bulk reads wait for DeepSeek's off-peak hours. Measured: about $0.0044 per document, $45 to $54 per 10,000 documents; a new prompt or model version re-reads everything at that price. Every call's cost goes to `api_costs`.)*
- **Defamation posture** — publish only quote-verified, sourced claims; label confidence honestly; show the evidence inline. "PE-owned (verified — 3 sources)" with clickable receipts is a fundamentally different legal and trust position than a bare pin on a map.

---

## 8. Build Order (prototype → wedge → scale)

> **Build order note (ruled 2026-10-16):** where this section and `build_roadmap.md` differ, the roadmap wins. In particular the first connector is **press-release RSS** (roadmap Step 10) — the simplest source on which to learn the full pipeline; sponsor portfolio pages follow in Step 14.

**Phase 1 — Prove the trust loop (1–2 weeks of effort)**
Alembic migrations for the schema above; one connector (press-release RSS per build_roadmap.md Step 10; originally planned as sponsor portfolio pages for ~20 known DSO/vet rollup sponsors); `extract_claims` + `verify_citations` tasks; a *minimal* review view (Starlette-Admin or Streamlit is fine at this stage). Add roughly a week to the estimate for stack ramp-up. Success = a claim card for a real clinic with verified quotes. **The citation-verification loop is the premise — prototype it first.**

**Phase 2 — Healthcare wedge**
Load the NPPES bulk census (national); add the NPPES API, state SoS for launch states, press-release RSS, and lazy Google Places resolution. Match DSO/sponsor rosters against the census for the national baseline, then run a deep batch of every dental + vet practice in one launch state. Measure: % verified, % reported, % no_evidence_found, % ambiguous, % sources_disagree — these numbers tell you real coverage.

**Phase 3 — Batch scale + alerts**
CSV batch intake at thousands-of-entities scale; Celery Beat re-crawls; diff detection on portfolio pages/rosters → new-acquisition events → Acquisition Alarm notifications.

**Phase 4 — PC layer**
Form 5500 bulk load (pandas); camelot BDC Schedule of Investments parsing; *(2026-11-16: Inline XBRL, not camelot)* top-100 pension CAFR ingestion; PC claim types + jargon decoder content. This is where the Python choice pays back most visibly. This lights up MyRetirementX-Ray on the same graph.

**Phase 5 — Graph depth**
Cross-link the layers (sponsor → PC lender → pension LP where public evidence exists, `estimated` edges labeled as such; *2026-11-07: `estimated` was dropped from edge confidence (engine "What 'checked' means and coverage states"); the retirement map may add it back*); expose the money-flow graph views; ~~open community submissions into the review queue~~ (not in the MVP, 2026-10-26).

---

## 9. What This Deliberately Does Not Do

- No PitchBook/Preqin data (licensing + provenance premise).
- No LLM answers beyond the corpus — "no evidence found" is always preferred over inference.
- No claims from a classifier. Jev (if adopted) routes work and labels or flags quote-verified claims; it cannot produce quotes, so it can never be the source of a published fact.
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