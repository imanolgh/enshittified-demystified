# API conventions, internal auth and operator surface

Type: grilling
Status: open
Map: [engine](../map.md)

## Question

What are the cross-cutting HTTP conventions, how are `/internal` and `/admin` protected, and how does the operator (the developer) trigger loads, matches and replays now that the review panel is gone?

## Context

- Implied endpoints: `GET /health`, `GET /api/entities/{id}/card`, `GET /api/entities/{id}/graph`, `GET /api/search`, `GET /api/entities/pending/{ticket}`, `POST /internal/claims`, `POST /internal/edges/{id}/retract`, `POST /admin/ingest-batches`; implied without a path: public changelog, batch report, document receipts. (The employer→plan lookup moved to retirement "Form 5500 ingestion and the headline exposure number" on 2026-11-04.)
- **Auth**: user accounts are out of scope (map ruling); `fastapi-users` vs JWT (evidence_layer_plan.md:42; stack_fastapi.md:28) only matters later. For /internal and /admin: static API key from settings, not publicly exposed (default).
- **Admin surface** (build_roadmap.md:133,181; research_flows.md:22,77 "batch dashboard"; evidence_layer_plan.md:41): any UI, or endpoints + CLI + Flower only?
- Defaultables: `/api/v1`, error format, cursor pagination, CORS, ETag + Redis card cache invalidated by events, OpenAPI in production; batch report format (counts per build_roadmap.md:103, updated vocabulary).
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): `GET /api/entities/pending/{ticket}` is dropped. Two items join the operator surface: the **demand dashboard** (what people search for that is not seeded yet; the log itself is "Search and the demand log"), and resuming a batch whose status is `halted`. Batch counts are computed on read (no counts column).
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): `POST /internal/claims` is dropped; the door is an in-process function. A source-link submission sends a URL to fetch, not claims.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): a merged entity's `public_id` URL answers 301 to the survivor's page, never 404, and the id is never reused. The operator surface gains one command: withdraw a `producer` + `producer_version` (retracts its identity rows; its claims per "Edge lifecycle"), then re-run. There is no merge, split or single-row retract command (ADR 0002 amended).
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): the operator surface gains an unknown-phrases report: owner descriptions no term matched, sorted by how many owners use them (launch-list brands first), with example quotes and a model-suggested kind that never counts as evidence. Adding a term is a code change, followed by a re-map with no new LLM calls.
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): the operator surface needs a report of unchecked brands and the sources holding them up (failed, blocked, unreadable or claims-rejected documents, items failing in a shared pass).
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): the `fetches` log (outcomes `ok|not_modified|failed|blocked|not_found`, kept 90 days) feeds the operator report of failed and blocked fetches.
- **From "Edge lifecycle: ending, retraction and staleness"** (2026-11-07; notes in evidence_layer_plan.md §4 `edges`): the operator surface needs the one command that withdraws a producer version (claims, identity rows, document reads, edge recompute, re-run), and a report of closing phrases the phrase table doesn't know. There is no hand edge-retraction endpoint.
- **From "Category storage and recompute"** (2026-11-07; tables `entity_categories` and `entity_pe_owner_periods` in evidence_layer_plan.md §4): drift-check differences (a missed recompute trigger) raise an operational alert that the operator surface shows.
- **From "Brand card, receipt and edge shapes"** (2026-11-07; formerly "Claim card and graph output shapes"; glossary "Brand card" and "Receipt"): output models read from database rows (Pydantic `from_attributes`); the API needs a brand card response and a receipt response (quote, source name, domain and type, live link, `published_on`, first fetch, last seen).
