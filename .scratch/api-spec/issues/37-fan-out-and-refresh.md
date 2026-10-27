# Retrieval fan-out, tracked entities and refresh cadence

Type: grilling
Status: open
Blocked by: 30, 31, 32, 33, 34, 35, 36  (Rosters, portfolio pages and the registry; NPPES census load and census match; Press and EDGAR full-text connectors; SoS and vet license board connectors; Form ADV and IRS exempt-org ingestion; Form 5500 ingestion and the headline exposure number; BDC discovery and Schedule of Investments parsing)
Map: [api-spec](../map.md)

## Question

Given an entity, which connectors run (the routing matrix), how far research recurses, how partial failures are handled, which entities are "tracked", and what the full refresh schedule is?

## Context

- **Routing matrix**: entity type × vertical × state → connector set; only two examples exist (evidence_layer_plan.md:158).
- **Recursion**: after finding the rollup, research the PE firm, then the fund? What stops it?
- **Partial failure**: per Celery docs, any chord header task that raises fails the callback (ChordError). Retrieve tasks return failure markers instead of raising? How does a failed connector affect "checked"?
- **"Tracked"**: "tracked entity / sponsor names / CIK" (research_flows.md:110–112,162) has no membership rule.
- **Quarterly no-evidence refresh** (research_flows.md:114) at census scale (hundreds of thousands of entities): full fan-out or roster re-match only?
- **Beat jobs missing from cadence tables**: NPPES monthly reload, census re-match after each roster crawl, last-confirmed sweep, ambiguous retries, batch poller, events consumer, Form 5500 date, vet board refresh, Form ADV / IRS refresh.
- Staleness of known entities: does an A2 search re-research an entity checked N months ago?
