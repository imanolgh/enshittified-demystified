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
- **From "Schema conventions"** (2026-11-05; conventions in evidence_layer_plan.md §4; no on-demand research per decisions.md §15): a search never re-researches an entity, so the A2 staleness question is moot; refresh is scheduled or operator-seeded only.
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): "where to look next" hints are dropped. Fan-out reads identity rows and claims.
- **From "What 'checked' means and coverage states"** (2026-11-07; ADR 0001 amended; tables `document_reads` and `source_runs` in evidence_layer_plan.md §4): each required source writes a `source_runs` row per entity run; shared sources count through their latest complete pass, and only a pass completed after a brand was added counts for it, so pass cadence sets how soon a new brand is checked. Cadences are this ticket's.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): connectors send conditional requests (the server's `ETag` or `Last-Modified`), and only a changed extracted text triggers an LLM re-read, so refresh cadence mostly costs fetches, not extraction.
- **From "Edge lifecycle: ending, retraction and staleness"** (2026-11-07; notes in evidence_layer_plan.md §4 `edges`): the developer's rule for pending deals: a pending edge carries `expected_close_from`/`expected_close_to` (mapped from the release's closing phrase); while today falls inside that range, plus a lead time before it and a grace period after, the brand's own sources (SEC searches for the parties, the buyer's and seller's newsrooms and portfolio pages) run faster than normal; they return to normal when the range passes, the deal completes or is called off, and speed up again if a newer claim moves the range later. The lead time, grace period and faster pace are this ticket's. Press feeds are already polled about hourly.
