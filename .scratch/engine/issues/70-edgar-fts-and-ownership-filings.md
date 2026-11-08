# EDGAR full-text search and ownership filings

Type: grilling
Status: resolved
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

## Comments

### Round 1 (2026-11-08)

Facts read ("Research: EDGAR access, BDC identification and SoI formats"): full-text search is documented only as a UI; its JSON endpoint (`efts.sec.gov/LATEST/search-index`) is undocumented; it covers all electronic filings since 2001, exhibits included; exact phrases, `NEAR`, form, entity and date filters; 100 hits per page, 10,000-result cap; the SEC's limit is 10 requests a second; the SEC asks bots to declare a contact in the user agent (sent to "Operational identity, budgets and guardrail values").

- **Role** (Q1): a per-brand source searching EDGAR for a brand's and its company's names (whether it's required: chains "Category brand lists and brand-level checked"). Each hit's file is stored as its own document, `meta` holding accession, form, filer CIK and filing date, `published_on` = the filing date. An EX-99 press release is a `press_release` spoken by its issuer (ADR 0003); everything else is `sec_filing`, official and self-verifying (Jersey Mike's prospectus on Blackstone's 76.5% voting power is verified alone).
- **Forms** (Q2): 8-K with EX-99; S-1, S-4, 424B prospectuses; 10-K with Exhibit 21; 10-Q; DEF 14A, DEFM14A; SC TO, 425. Left out: Form D (related persons are officers), 13D and 13G (own reader), BDC filings (the BDC parser).
- **Queries and caps** (Q3): one exact-phrase query per brand and company name, filtered to those forms; the first run covers everything since 2001, newest first, up to 100 hits per name; refresh runs fetch filings since the last run. Unrelated hits end as `no_evidence_found` for that document. The SEC rate is shared across EDGAR connectors.
- **Long filings** (Q4, option a, the developer's ruling): every hit is read whole by the LLM however long the filing; reading windows around each mention was turned down. Noted on "Operational identity, budgets and guardrail values" for the spend guardrails.
- **13D and 13G** (Q5): for each public company in the graph, its 13Ds, 13Gs and amendments, through its EDGAR filing list (where filings about a company are listed is a build check). Structured filings (since December 2024) are read by a `parser` producer: each reporting person becomes a child document rendered as sorted `field: value` lines, giving `owned_by` claims quoting the holder's name and CIK, percent of class and event date, with the rule box in document `meta`. Older text filings: code reads the cover-page checkbox; a box it can't read never makes the company PE minority stake; a 13D has no box and always counts. The four filings (3G, Trian, Leonard Green, TPG) are checked at build.
- **Joint filers and amendments** (Q6, revised after the developer asked whether the sum is more accurate): reporting persons in one filing usually report the same shares (a fund, its general partner, the firm and the listed parent each control the same block), so summing double-counts (4 × 8% = 32% for one 8% stake); but two funds holding different shares with no parent row need the sum. Rule: the owner's stake is the larger of the largest single aggregate amount and the sum of the reporting persons' sole voting power, with the percent from the same share count. A newer filing replaces an older one by event date; an amendment reporting 5% or less ends the hop; 0% is an exit. Percent of class counts as voting unless a proxy or prospectus gives voting power.

## Answer

Resolved 2026-11-08 in a grilling session (one round with a revision, recorded under Comments).

- **Full-text search:** a per-brand source; one exact-phrase query per brand and company name over 8-K with EX-99, S-1, S-4, 424B, 10-K with Exhibit 21, 10-Q, DEF 14A, DEFM14A, SC TO and 425; first run since 2001, newest first, up to 100 hits per name; refreshes fetch only new filings. Each hit's file is its own document (filing details in `meta`, `published_on` = filing date). EX-99 is `press_release`; everything else `sec_filing` (official). Every hit is read whole (developer's ruling), budgeted in "Operational identity, budgets and guardrail values".
- **13D and 13G:** each public company's filings and amendments; structured filings read by a `parser` producer, one rendered child document per reporting person, rule box in `meta`; older text filings by a checkbox read, where an unreadable box never makes PE minority stake; a 13D always counts.
- **Joint filers:** the owner's stake is the larger of the largest single aggregate amount and the sum of sole voting power (never a plain sum: a fund, its GP, the firm and its parent report the same shares). Newer filings replace older ones; 5% or less ends the hop; 0% is an exit; percent of class counts as voting unless a proxy or prospectus gives voting power.
- Docs: evidence_layer_plan.md (EDGAR section and the stake-sum exception); conformance-tests skill. No ADR, no glossary change.

Handed on:
- "Retrieval fan-out, tracked entities and refresh cadence": per-brand runs, 13D/13G re-read cadence.
- "Entity resolution algorithm": reporting persons and filers by CIK.
- "Extraction execution": whole filings across several calls.
- "BDC discovery and Schedule of Investments parsing": BDC filings stay with the parser.
- chains "Category brand lists and brand-level checked": full-text search as a candidate required source.
