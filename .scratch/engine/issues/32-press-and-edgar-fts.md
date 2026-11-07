# Press and EDGAR full-text connectors

Type: grilling
Status: open
Blocked by: 08, 10, 24  (Research: EDGAR access, BDC identification and SoI formats; Research: Press-release and news feed sources; Source independence and syndication)
Map: [engine](../map.md)

## Question

How do the press-release/news connector and the EDGAR full-text search connector find, fetch, classify and store documents?

## Context

- Feed list and Google News query format; resolving Google News redirect URLs (from "Research: Press-release and news feed sources").
- **Classifying a domain** as `press_release` vs `news` (wire-domain list) — ties to "Source independence and syndication".
- **Matching general feed items** against hundreds of thousands of entity names for "instant refresh on mention" (research_flows.md:114).
- Poll cadence: 6-hourly per tracked entity (research_flows.md:110) — rate limits.
- EDGAR FTS: endpoint/params/form types/pagination; which files of a hit to store; EX-99 stored as `press_release` (ADR 0003:10); SEC user agent + ~10 req/s (from "Research: EDGAR access…").
- GDELT is in the Beat table (research_flows.md:110) but deferred — drop.
- Query construction and caps: which aliases, quoting, location terms, max hits per connector, max documents per entity.
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): rank 2 owner-kind evidence includes a press release the owner issued, so the press connector must record a release's issuer in a form code can match to an entity.
