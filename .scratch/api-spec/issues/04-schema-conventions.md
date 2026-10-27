# Schema conventions

Type: grilling
Status: open
Map: [api-spec](../map.md)

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
