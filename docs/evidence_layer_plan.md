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
| PDF / table extraction | **pdfplumber** + **camelot**, in-process | (no good PHP option — would have been AWS Textract) | Schedule of Investments and CAFR tables parse natively; no sidecar, no per-page bill |
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

**Conventions every table follows** (ticket 04, 2026-11-05):
- `id bigint` identity primary key, internal only. Rows that appear in a URL (`entities`, `documents`) also carry `public_id`: 12 random Crockford base32 characters, unique, never reused.
- Enums are text columns with a named CHECK constraint generated from the StrEnum in `app/core/contracts.py`. Every value change is a hand-written migration that drops and re-adds the constraint, and a test fails if a live CHECK and its StrEnum differ. (Alembic autogenerate detects neither CHECK expression changes nor native-enum value changes.)
- A reference to another row is a foreign-key column or a join table, never ids inside JSONB. JSONB holds only payloads that point at no row (`documents.meta`, `claims.value`).
- snake_case, plural table names, `<singular>_id` foreign keys, join tables named after both tables, `_at` timestamps (`timestamptz`, UTC), `_date` calendar dates, `is_`/`has_` booleans. One SQLAlchemy `naming_convention` names every constraint and index.
- `created_at` (database default) on every table; `updated_at` on tables whose rows change.
- No deletes and no soft-delete flags on evidence and identity tables (documents, claims, edges, events, aliases, identifiers, addresses, industries). Corrections go through status, `retracted_at` and events. Operational tables (cache, crawl state, cost log) may prune; their owning tickets set retention.
- Money is `numeric`, never float, with its currency stated.
- Indexes: every foreign-key column; every uniqueness rule as a unique index (claim hash, strong identifiers, public ids); `edges` on `from_entity_id`, `to_entity_id` and a partial index on non-retracted edges; a trigram index on aliases only if "Entity resolution algorithm" picks `pg_trgm`. Any other index needs a slow query behind it.
- Tables defined in their own tickets: fetch log ("Document storage, fetch log and last-confirmed"), Anthropic batch jobs and extraction cache ("Extraction execution"), registry and crawl state ("Rosters, portfolio pages and the registry"), `api_costs` and operational alerts ("Operational identity, budgets and guardrail values"), `failed_tasks` ("Celery topology"), the search demand log ("Search and the demand log").

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
      producer, producer_version (both null when source_document_id is null), retracted_at
      -- (2026-11-06: the strong-scheme unique index skips rows with retracted_at set.)
      -- strong schemes (cik, ein, crd, sec_file_number, private_fund_id, place_id, npi): one
      -- entity per (scheme, value); a second holder is a resolution or merge signal, never a
      -- second row. Weak schemes (ticker, domain, phone) may repeat. An entity may hold several
      -- values of one scheme: an investment firm holds one crd per adviser registration (ticket 65).
      -- sec_file_number = 801-|802-|814-; private_fund_id = 805-. phone only from stored
      -- documents, never Places. Added later: SoS entity number, license number and plan
      -- EIN+PN when their efforts start; trademark serial only if USPTO is adopted (ticket 64).

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
      -- source_document_id. Chains values and display: chains-and-brands "Product categories".

location_brands                -- 2026-11-05 (ticket 15, "Predicate semantics")
  id, location_id, brand_id, source_document_id, producer, producer_version, retracted_at
      -- which brands a location trades under: identity data, never a claim, never an ownership
      -- hop, no confidence. Written only by code producers (store locators, rosters), so the
      -- source document is required. Unique (location_id, brand_id, source_document_id); a
      -- Taco Bell/KFC combo store has two rows. Retiring an old row: "Entity lifecycle".

documents                      -- immutable once written
  id, source_type (nppes|form5500|form_adv|sec_filing|irs_exempt_org|sos|license_board|cafr|
      company_site|press_release|news),   -- ADR 0003; fetch method (bulk|api) + connector go in meta
  public_id, url, retrieved_at, sha256, storage_path, mime_type, raw_text (nullable), meta JSONB

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
      --     Wafra Inc.", "Realized: ..."). terminated = the quote says the deal was called off; it
      --     ends a pending deal for that pair.
      --   lends_to: instrument (as written), reference_rate, spread_pct, interest_rate_pct,
      --     pik_rate_pct, floor_pct, principal, cost, fair_value, currency, scale, non_accrual,
      --     maturity_date, affiliation (non_affiliate|affiliate|control).
      --   holds_position: instrument, units, cost, fair_value, currency, scale, affiliation.
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
      -- sum of its firm's funds' stated stakes. Within one document a current claim beats a
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
      -- 2026-11-05 (ticket 17): producer_version = the prompt version (llm), a module constant
      -- (parser, etl) or the selector config revision; the producer declares it and golden-fixture
      -- tests force a bump when output changes. extraction_model is null except for llm. The task
      -- sets all three, never the model's output.
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
  confidence (verified|reported|estimated|sources_disagree),
      -- 2026-11-07 (ticket 25): sources_disagree marks a contested edge, never shown as fact; the
      -- card lists each side with links. A brand's category is sources_disagree only when the
      -- contested readings give different categories. A fund with disputed managers inherits a
      -- kind only if every disputed manager has the same kind.
      -- ownership_type removed 2026-10-26 (ADR 0001): owners carry owner_kind; each business's
      -- category + separation degree are computed by code from its ownership chains.
  published_at, retracted_at (nullable)
      -- 2026-11-05 (ticket 04): supporting_claim_ids JSONB replaced by edge_claims.

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
1. Queries/scrapes its source (httpx for APIs/static pages, Playwright for JS-heavy pages; per-domain rate limiting via a Redis token bucket; respect robots.txt; tenacity exponential backoff on 429/5xx).
2. Stores the raw document to S3 (boto3), computes sha256, writes a `documents` row via SQLAlchemy.
3. Extracts plain text (HTML → text via selectolax/BeautifulSoup; PDFs → pdfplumber; tables → camelot, structured JSON stored in `meta`). All in-process — no sidecar.
4. Skips documents whose sha256 already exists (dedup).

Celery Beat (≈ Laravel Scheduler): recurring crawls of sponsor portfolio pages, DSO rosters, and news RSS to catch *new* acquisitions — this feeds the Acquisition Alarm feature.

### Producers and the door (2026-11-05, engine "Claim producers and the claims door")

Four producers turn stored documents into output. Each one records itself in `producer`:

- `llm` is the default. It reads any page or filing text, sponsor portfolio pages included (Stage 3).
- `parser` reads BDC Schedules of Investments.
- `etl` reads bulk official files: Form ADV now, Form 5500 and NPPES when their efforts unpark.
- `selector` reads long lists where every record has the same fields, such as store locators and location rosters, through a per-site registry config. Store-locator JSON endpoints are allowed when robots.txt permits them and they feed the brand's public locator page.

Every claim, whatever produced it, quotes a stored document, enters as `pending` and passes `verify_citations`. Confidence comes from the source type, never from the producer. What counts as the quote:

- Page or filing text: an exact span of the document's text.
- A bulk row (header line + data line): the whole data line, exactly as in the file.
- A BDC holding: the row's parsed-table text. If the parser reads the SEC BDC dataset, each holding is a bulk row.
- A roster item on an HTML page: the item's text, which must appear in the page's text.
- A store-locator JSON record: one document per record. Code writes the record's text as one `field: value` line per field, sorted, with nested fields dotted (`address.city: Atlanta`) and list items indexed (`brands.0: Dunkin'`). The quote is the lines the claim uses. `meta` records the rendering format's version and points at the full response, which is stored as the original.

**Identity records.** Code producers (`etl`, `parser`, `selector`) also emit identity records: what one document states about one entity's identity (names, identifiers, addresses, phone, domain, industry code, and for a location the names of its brands, which become `location_brands` rows). The LLM emits only claims. Identity records replace the old "resolution hints", "structured hints" and "enrichment structs". Nothing records "where to look next"; fan-out reads identity rows and claims.

**The door** is one in-process function in `app/core`, validated against `contracts.py`. There is no HTTP route. A producer makes one call per run: one per document for code producers, one per request for the LLM. Each call is one transaction and is idempotent. A call carries the ids of the documents the request read, producer and version, identity records and claims; code gives each read document that no claim cites the outcome `no_evidence_found` (ticket 21). Each identity record has a key such as `r1` that is only valid inside the call, and a code producer's claim can name its subject or object by that key. The door:

1. checks every identity value, as found, against the cited document's text (the quote normalization), and does not write a record with a missing value;
2. resolves each identity record to an entity and writes the sourced alias, identifier, address and industry rows, normalized for storage;
3. writes claims as `pending`, with each name as written resolved to an entity id in the same call (null when ambiguous; ticket 18). Their quotes are checked in Stage 4, after names are resolved.

**Code producer failures.** Every `etl` run first compares the file header with the expected columns and reads columns by name. Every `selector` run first checks that items still come back with the expected fields and roughly the usual count. A failed shape check stops the run before it writes anything and raises an alert. A per-record failure (a rejected claim or an unwritten identity record) raises an alert naming the producer, version and document, and the run keeps going. When per-record failures in one run pass the spec's threshold, the rest of the run stops. Rows already written can be found by `producer_version`.

### Stage 3 — LLM Extraction (`extract_claims`, was `ExtractClaimsJob`)
Runs per entity once its retrieval chord completes (the `chord()` callback ≈ `Bus::batch()->then(...)`).

*(Experimental, Step 27b)* **Jev pre-filter:** before extraction, Jev answers a true/false question per document ("does this contain ownership, acquisition or lending evidence about X?"). Only positives are sent to Claude. It is adopted only if A/B testing shows near-zero loss of evidence-bearing documents.

1. Assemble the document set (text + parsed tables) for the entity, chunked to context limits.
2. Call Claude (Anthropic Python SDK) with a strict system prompt; the response is parsed straight into Pydantic `Claim` models — anything that fails validation is dropped and logged before it can reach the DB:
   - Emit claims only in the fixed predicate vocabulary.
   - **Every claim must include a verbatim quote copied exactly from the provided document.**
   - ~~Classify ownership_type~~ — removed 2026-10-26 by ADR 0001 (`docs/adr/0001-ownership-category-computed-by-code.md`): the LLM never classifies ownership categories. It may only extract a quoted self-description of an owner (e.g. "Oak Ridge is a private equity firm"), the lowest-ranked owner-kind source. *(2026-11-07, engine "Owner kind": the response gains `owner_descriptions`, each with the owner's name as written, the describing phrase as written, the document label and the quote; a term table in code maps the phrase to a kind, never the model.)*
   - ~~If the documents contain no ownership/exposure evidence, return an explicit `no_evidence_found` result~~ *(2026-11-06, engine "ExtractedClaim and the extraction result envelope": the response is only `claims: list[ExtractedClaim]`, possibly empty. Code gives each document in the request that no claim cites the outcome `no_evidence_found`, and only from a response that finished and parsed. A bad item is dropped and logged; a response that stopped at the token limit or doesn't parse fails as a request and is retried, giving no document an outcome; a document cited only by dropped items gets no outcome.)*
3. Model tiering: Sonnet-class for bulk; escalate to Opus-class when documents conflict or classification is ambiguous.
4. Write raw response to the claim rows (`extraction_model`, `extracted_at`). *(2026-11-05: claims go through the door above; the task sets `producer = llm`, `producer_version` and `extraction_model`, never the model's output.)*

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
- `GET /api/entities/{id}/card` → claim card: business category (+ separation degree per PE firm), sponsor, acquisition date, N sources with links + quotes, confidence.
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
- **Cost controls** — LLM spend is per-document-set per entity; cache extractions by document sha256 so re-runs are free; batch API pricing for the big seeding runs. Rough planning figure: a few cents to a few tens of cents per entity depending on document volume — real money at 100k entities, trivial at pilot scale.
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
Form 5500 bulk load (pandas); camelot BDC Schedule of Investments parsing; top-100 pension CAFR ingestion; PC claim types + jargon decoder content. This is where the Python choice pays back most visibly. This lights up MyRetirementX-Ray on the same graph.

**Phase 5 — Graph depth**
Cross-link the layers (sponsor → PC lender → pension LP where public evidence exists, `estimated` edges labeled as such); expose the money-flow graph views; ~~open community submissions into the review queue~~ (not in the MVP, 2026-10-26).

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