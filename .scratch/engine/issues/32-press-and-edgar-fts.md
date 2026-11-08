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
- **From "Category precedence and public companies"** (2026-11-07; ADR 0001 amended): above a public company, a PE firm's minority stake counts only from a 13D, or a 13G not filed under Rule 13d-1(b); proxy tables only confirm a holder. So 13Ds and 13Gs need a connector that copies the rule box into document meta. Checked 2026-11-07: T. Rowe Price Associates' SCHEDULE 13G of 2026-11-06 (accession 0000080255-26-000673, Pacific Biosciences, 10.8%) has the structured field `designateRulePursuantThisScheduleFiled` = `Rule 13d-1(b)` and `typeOfReportingPerson` = `IA` in its `primary_doc.xml`. A 13D or 13G amendment reporting 5% or less ends the holder's hop. Which producer reads these filings, how they are found, and how older filings without the structured format are read, is this ticket's.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): connectors fill `published_on` from structured fields only: a feed item's publication date, an SEC filing date, or a page's `datePublished` / `article:published_time`.
- **To confirm** (stated from memory in "Category precedence and public companies", 2026-11-07, not checked): PE sponsors that held shares before an IPO usually file their 13G under Rule 13d-1(d), and activists file a 13D; which box 3G (Restaurant Brands), Trian (Wendy's), Leonard Green and TPG (Life Time) actually used was not checked. Only Rule 13d-1(b) was verified, on T. Rowe Price's filing. Check these four filings when building the 13D and 13G connector, since their category depends on it.
- **From "Brand card, receipt and edge shapes"** (2026-11-07; formerly "Claim card and graph output shapes"; glossary "Brand card" and "Receipt"): receipts never re-serve archived copies of press releases or news; they show the quote, source, live link and dates. Whether storing wire copies at all fits the wire services' terms (flagged by "Research: Press-release and news feed sources") is still an open legal call for the developer.
- **From "Source independence and syndication"** (2026-11-08; ADR 0002 amended; notes in evidence_layer_plan.md §4 `documents`): a press release's speaker is its issuer wherever the copy sits, so the press connector must read the issuer (the wire's "SOURCE" line or the release's own byline) and set `speaker_entity_id`; a wire tag in the text ("/PRNewswire/", "/GLOBE NEWSWIRE/", "(BUSINESS WIRE)") marks a reposted release as a copy. A news article's speaker is its outlet (null speaker, domain). This ticket is now takeable.
