# Schema conventions

Type: grilling
Status: resolved
Map: [engine](../map.md)

## Question

Which cross-cutting schema conventions does every table follow, and what are the value sets for the ingest tables?

## Context (mostly defaultable — consider accepting a slate)

- **Primary keys / public ids**: card URLs are shared, so ids must be stable. Default: bigint identity + opaque public id.
- **Enum storage**: native PG enums vs varchar + CHECK generated from the StrEnums (Alembic autogenerate handles native-enum changes poorly).
- **Join tables vs JSONB**: `edges.supporting_claim_ids JSONB` (evidence_layer_plan.md §4) has no FKs and makes "which edges does this claim support" a scan; default `edge_claims` join table.
- **Ingest tables**: batch `status`, `counts`, `submitted_by` (no accounts exist) and item `stage` have no values (evidence_layer_plan.md:126–127); research_flows.md:25 uses item status `queued` beside the new `result` column; intake CSV has `name, address, city, state, category` (evidence_layer_plan.md:145) but `ingest_items` stores only name + address. Are A2 tickets ingest items or their own table?
- **Implied tables never listed**: registry, crawl state, Anthropic batch jobs, extraction cache, API cost log, operational alerts, dead letters, fetch log — confirm which exist (several are decided in their own tickets; this ticket owns naming/conventions).
- **Indexes**: trigram/GIN on aliases (if Meilisearch dropped), edges on (from) and (to), partial index on active edges.
- **Timestamps, soft-delete policy** (none — append-only), naming conventions.
- **From "What a business entity is"** (2026-11-05, [ADR 0005](../../../docs/adr/0005-brands-companies-locations-separate.md)): three new tables need names and conventions: `entity_identifiers`, `entity_addresses`, `entity_industries` (evidence_layer_plan.md §4). The value set for `entity_industries.origin` (brand list, intake column, NPPES taxonomy) is not fixed yet.

## Comments

**2026-11-05 grilling, round 1** (developer accepted all six recommendations):
1. Scope: each owning ticket decides whether its table exists and its columns; this ticket sets the conventions they follow, plus the ingest tables. Owners: fetch log → "Document storage, fetch log and last-confirmed"; Anthropic batch jobs and extraction cache → "Extraction execution"; registry and crawl state → "Rosters, portfolio pages and the registry"; `api_costs` and operational alerts → "Operational identity, budgets and guardrail values"; dead letters (`failed_tasks`) → "Celery topology".
2. Ids: `bigint` identity primary key on every table, internal only. Rows that appear in a URL also get `public_id`: 12 random Crockford base32 characters (60 bits), unique index, never reused. For now `entities` and `documents`. Readable URL names → "Website pages and shareable cards"; where a merged entity's public id leads → "Entity lifecycle".
3. Enums: text column + named CHECK constraint generated from the StrEnum (`Enum(..., native_enum=False, create_constraint=True, name=...)`); every value change is a hand-written migration that drops and re-adds the constraint; a test compares each live CHECK with its StrEnum in `contracts.py` and fails on drift. Facts (Context7, Alembic and SQLAlchemy 2.0 docs): autogenerate never detects CHECK expression changes; native PG enum values need `ALTER TYPE ... ADD VALUE` in an `autocommit_block` and can't be removed without rebuilding the type.
4. References: a reference to another row is a foreign-key column or a join table, never ids inside JSONB. `edge_claims (edge_id, claim_id)` replaces `edges.supporting_claim_ids`. JSONB only for payloads that point at no row (`documents.meta`, `claims.value`). `ingest_items.candidates` → round 2.
5. Names, time, deletes, money: snake_case; plural tables; `<singular>_id` FKs; join tables named after both tables; `_at` timestamps, `_date` dates, `is_`/`has_` booleans; one SQLAlchemy `naming_convention` for constraints and indexes. `created_at timestamptz` (UTC, database default) everywhere, `updated_at` on tables whose rows change; real-world dates are `date`. No deletes or soft-delete flags on evidence and identity tables (documents, claims, edges, events, aliases, identifiers, addresses, industries); corrections via status, `retracted_at` and events. Operational tables (cache, crawl state, cost log) may prune; retention set by their owning tickets. Money is `numeric`, never float, with its currency stated.
6. Indexes: every FK column; every uniqueness rule as a unique index (claim hash, strong identifiers, public ids); `edges` on `from_entity_id`, `to_entity_id` and a partial index on non-retracted edges; trigram on aliases only if "Entity resolution algorithm" picks `pg_trgm`; any other index needs a slow query behind it.

**2026-11-05 grilling, round 2** (developer accepted all; Q7 was replaced after the developer ruled out on-demand research):
- **Product ruling (developer, 2026-11-05): no on-demand research.** The data set grows only by operator-seeded batches (categories, brand lists, locations). Searches that find nothing ready (not in the data, or in the data but not yet checked) are logged so a demand dashboard can show what to seed next. Recorded in decisions.md §15; the log's design is engine "Search and the demand log" (ticket 40, renamed), the dashboard is "API conventions, internal auth and operator surface". Places facts given to the developer: only `place_id` may be stored (ToS §3.2.3(a)(iii) bans saving names and addresses); IDs-only Text Search is free; a name shown on the dashboard costs $0.017 (Place Details Pro) with the Google logo and is not saved; showing Places results to searchers is $0.032 per search after 5,000 free a month; for brands a Places result is one nearby store, so place ids scatter one brand's demand.
7. Every ingest item belongs to an operator batch: `batch_id` required, no public id on items, `GET /api/entities/pending/{ticket}` dropped. The demand log is its own table, owned by ticket 40.
8. Item `stage` dropped. `result` null = waiting or resolving; a value = finished. Research progress belongs to the entity. `failed` now means an error during resolution only (narrows the 2026-10-26 meaning); later failures belong to the entity's research and its dead letter. research_flows.md:25 fixed to match.
9. `ingest_item_candidates (ingest_item_id, entity_id, score)` with foreign keys replaces `ingest_items.candidates JSONB`.
10. Batches: `name` (operator label), `status` = `running | done | halted` (halted = stopped by the spend cap or the operator; unfinished items keep a null result). No `counts` column (computed on read). `submitted_by` dropped. Resume → "API conventions…"; cap → "Operational identity…".
11. Item inputs: `input_name` (required), optional `input_entity_type` (`brand | company | location`), `input_industry`, `input_street`, `input_city`, `input_state`, `input_postal_code`, `input_domain`. Intake CSV header: `name, entity_type, industry, street, city, state, postal_code, domain`, only `name` required. Raw rows not kept.
12. `entity_industries.origin` replaced by two nullable FKs, `ingest_item_id` and `source_document_id`, with a CHECK requiring exactly one.
13. Recording and routing as above, plus context lines on the tickets that assumed on-demand research, and `monetizationideas.md` :43/:81 to "Product docs: competitors and stale claims".

## Answer

Resolved 2026-11-05 by grilling (rounds above). The conventions and the ingest tables are recorded in `docs/evidence_layer_plan.md` §4; the on-demand ruling made during this ticket is `docs/decisions.md` §15.

- **Scope**: this ticket sets the conventions; each owning ticket decides whether its table exists and its columns (fetch log, batch jobs and cache, registry and crawl state, `api_costs` and alerts, `failed_tasks`, demand log).
- **Ids**: internal `bigint` identity keys; `public_id` (12 random Crockford base32 characters, unique, never reused) on `entities` and `documents`.
- **Enums**: text + named CHECK from the StrEnum, hand-written migrations for value changes, a drift test against `contracts.py`.
- **References**: foreign keys or join tables, never ids in JSONB; `edge_claims` replaces `supporting_claim_ids`; `ingest_item_candidates` replaces `candidates JSONB`.
- **Names, time, deletes, money, indexes**: snake_case plural tables, `_id`/`_at`/`_date`/`is_` suffixes, one `naming_convention`; `created_at` everywhere, `updated_at` where rows change; no deletes on evidence and identity tables; `numeric` money with currency; FK and uniqueness indexes, edge from/to and active-edge partial index, trigram only if `pg_trgm` is picked.
- **Ingest tables**: operator batches only (no on-demand research). Batch `name`, `status` = `running | done | halted`, counts computed on read, no `submitted_by`. Item: required `batch_id`, `input_name` plus optional `input_entity_type`, `input_industry`, address fields and `input_domain`; `stage` dropped; `result` null while resolving, `failed` = resolution errors only. Intake CSV header `name, entity_type, industry, street, city, state, postal_code, domain`.
- **Industry origin**: two nullable foreign keys (`ingest_item_id`, `source_document_id`), exactly one set.
- **No on-demand research** (developer ruling): searches never start research; misses go to a demand log for a seeding dashboard. Ticket 40 retitled "Search and the demand log"; context lines added to 13, 15, 19, 20, 22, 27, 28, 30, 37, 38, 41, 42 and chains 61, 62.
