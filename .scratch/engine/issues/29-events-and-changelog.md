# Events and the public changelog

Type: grilling
Status: open
Blocked by: 26, 27, 68  (Edge lifecycle: ending, retraction and staleness; Category precedence and public companies; Category storage and recompute)
Map: [engine](../map.md)

## Question

What is the `events` table (columns, event-type vocabulary, idempotency, consumers), and what does the public changelog expose?

## Context

- Named everywhere (build_roadmap.md:61,73,129,157; research_flows.md:102,162,178; ADR 0001:15; CLAUDE.md:25), defined nowhere.
- Candidate event types: published, ended, retracted, confidence_changed, category_changed, owner_kind_changed, acquisition_event (research_flows.md:102), filing_withheld. What counts as an acquisition event — only `acquired_by`, or new roster locations too?
- Payload, correlation id, idempotency key (retries must not double-emit), consumer cursors, card-cache invalidation (research_flows.md:178).
- **Changelog**: retractions only or all events? Global or per entity? Which fields are public?
- Alerts to users are out of scope (map ruling 2026-10-26); operational alerts to the developer are in — events may feed them.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): event kinds this adds: entity merged, entity unmerged, entity type changed, and producer version withdrawn (identity rows retracted). Whether any of them appear in the public changelog is this ticket's.
- **From "Claim identity"** (2026-11-06; notes in evidence_layer_plan.md §4 `claims`): new event kind: a claim re-resolved (its subject or object id changed by code).
- **From "Claim value schemas"** (2026-11-06; schemas in evidence_layer_plan.md §4 `claims`): candidate events: a loan turning non-accrual between two quarterly claims, and an announced deal (`acquired_by` with `deal_status = announced`), which suits the public deal feed.
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): new event kind: an entity's computed owner kind changed (new evidence, a retraction, or a term-table change that re-mapped stored descriptions).
- **From "Conflict, succession and co-investors"** (2026-11-07; ADR 0001 and ADR 0002 amended; notes in evidence_layer_plan.md §4 `claims` and `edges`): events rows are needed when an ownership hop ends (a `former` claim, a stake that can't be true beside it, or 18 months unconfirmed), when a stake change moves a brand between PE-owned and PE minority stake, when an edge becomes or stops being `sources_disagree`, and when a pending deal is terminated or stops showing as pending. Whether each reaches the public changelog is this ticket's.
- **From "Edge lifecycle: ending, retraction and staleness"** (2026-11-07; notes in evidence_layer_plan.md §4 `edges`): events rows are written for each visible edge change (confidence, phase, end, value), for each retraction with its reason (`producer_withdrawn`, `entity_merged`, `entity_unmerged`, `claim_re_resolved`, `entity_type_changed`), for the staleness sweep, and once per producer-version withdrawal command (with counts, none per claim). Which reach the public changelog is this ticket's.
- **From "Category storage and recompute"** (2026-11-07; tables `entity_categories` and `entity_pe_owner_periods` in evidence_layer_plan.md §4): events rows are written when a brand's category or category confidence changes and when a PE owner period starts, changes phase or ends; a new `checked_on` alone writes none; fixes made by the nightly drift check write events rows too. This ticket is now takeable.
