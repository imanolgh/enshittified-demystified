# EDGAR full-text search and ownership filings

Type: grilling
Status: open
Blocked by: 08, 24  (Research: EDGAR access, BDC identification and SoI formats; Source independence and syndication)
Map: [engine](../map.md)

## Question

How does the EDGAR full-text search connector find and store filings that mention a brand or its owners, and how does a 13D/13G connector read beneficial-ownership filings (rule box, stake, amendments), including older filings without the structured format?

## Context

- Split from "Press and EDGAR full-text connectors" on 2026-11-08 (developer ruling, to keep each ticket to one session).
- **Moved from that ticket:** EDGAR full-text search endpoint, parameters, form types and pagination; which files of a hit to store; EX-99 press-release exhibits stored as `press_release` (ADR 0003); SEC user agent and about 10 requests a second ("Research: EDGAR access, BDC identification and SoI formats": the full-text search JSON is undocumented); query construction and caps (which aliases, quoting, max hits per brand).
- **From "Category precedence and public companies"** (2026-11-07; ADR 0001 amended): above a public company, a PE firm's minority stake counts only from a 13D, or a 13G not filed under Rule 13d-1(b); proxy tables only confirm a holder; a 13D or 13G amendment reporting 5% or less ends the holder's hop. Checked 2026-11-07: T. Rowe Price Associates' SCHEDULE 13G of 2026-11-06 (accession 0000080255-26-000673, Pacific Biosciences, 10.8%) has `designateRulePursuantThisScheduleFiled` = `Rule 13d-1(b)` and `typeOfReportingPerson` = `IA` in `primary_doc.xml`. Which producer reads these filings, how they are found, and how older filings without the structured format are read, is this ticket's.
- **To confirm** (stated from memory, not checked): pre-IPO sponsors usually file 13Gs under Rule 13d-1(d) and activists file 13Ds; check 3G (Restaurant Brands), Trian (Wendy's), Leonard Green and TPG (Life Time) when building, since their category depends on it.
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07): `published_on` for a filing is its filing date; a filing is a parent document and its exhibits or rows are children.
- **From "Source independence and syndication"** (2026-11-08): a filing's speaker is its filer; an EX-99 press release's speaker is its issuer.
- **From "Press and EDGAR full-text connectors"** (2026-11-08): the bot rules apply (own bot name, robots.txt path by path, never get around a block, stop when asked); SEC requests use the identified contact-free user agent.
