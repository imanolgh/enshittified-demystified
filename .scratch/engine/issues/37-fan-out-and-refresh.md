# Retrieval fan-out, tracked entities and refresh cadence

Type: grilling
Status: open
Blocked by: 30, 32, 34, 36  (Rosters, portfolio pages and the registry; Press and EDGAR full-text connectors; Form ADV and IRS exempt-org ingestion; BDC discovery and Schedule of Investments parsing)
Map: [engine](../map.md)

## Question

Given an entity, which connectors run (the routing matrix), how far research recurses, how partial failures are handled, which entities are "tracked", and what the full refresh schedule is?

## Context

- **Routing matrix**: entity type × vertical × state → connector set; only two examples exist (evidence_layer_plan.md:158).
- **Recursion**: after finding the rollup, research the PE firm, then the fund? What stops it?
- **Partial failure**: per Celery docs, any chord header task that raises fails the callback (ChordError). Retrieve tasks return failure markers instead of raising? How does a failed connector affect "checked"?
- **"Tracked"**: "tracked entity / sponsor names / CIK" (research_flows.md:110–112,162) has no membership rule.
- **Beat jobs missing from cadence tables**: last-confirmed sweep, ambiguous retries, batch poller, events consumer, Form ADV / IRS refresh.
- **Moved out 2026-11-04 (ADR 0004 split)**: the quarterly no-evidence refresh at census scale and the NPPES reload, census re-match and vet board refresh jobs are in local-businesses "Local fan-out and refresh cadence"; the Form 5500 date is in retirement "Form 5500 ingestion and the headline exposure number". Blockers on parked tickets (31, 33, 35) were dropped.
- Staleness of known entities: does an A2 search re-research an entity checked N months ago?
