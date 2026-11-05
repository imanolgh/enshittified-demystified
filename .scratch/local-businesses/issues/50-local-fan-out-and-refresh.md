# Local fan-out and refresh cadence

Type: grilling
Status: open
Blocked by: engine/37, 31, 33  (Retrieval fan-out, tracked entities and refresh cadence; NPPES census load and census match; SoS and vet license board connectors)
Map: [local-businesses](../map.md)

## Question

Which local connectors run for a local business (by vertical and state), how often is the census-scale no-evidence set refreshed, and on what schedule do the NPPES, census-match and vet board jobs run?

## Context

Split out of engine "Retrieval fan-out, tracked entities and refresh cadence" on 2026-11-04 (ADR 0004). The bullets below were moved word for word.

- **Quarterly no-evidence refresh** (research_flows.md:114) at census scale (hundreds of thousands of entities): full fan-out or roster re-match only?
- **Beat jobs missing from cadence tables** (local ones): NPPES monthly reload, census re-match after each roster crawl, vet board refresh.
- The routing matrix's vertical × state rows for SoS, vet boards and NPPES follow the general matrix fixed in the engine ticket.
