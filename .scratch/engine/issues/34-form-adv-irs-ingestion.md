# Form ADV and IRS exempt-org ingestion

Type: grilling
Status: resolved
Blocked by: 07, 14, 65  (Research: Form ADV and IRS exempt-org bulk data; Owner kind: storage, evidence and the PE-firm test; Funds and their investment firm)
Map: [engine](../map.md)

## Question

How are Form ADV and IRS exempt-org data ingested to set owner kinds (and fund→firm links) at rank 1?

## Context

- In scope by map ruling 2026-10-26 (without Form ADV no business can be verified PE-owned under ADR 0001:9–10,14).
- Neither has a roadmap step nor a deferred-list entry (build_roadmap.md:173); evidence_layer_plan.md:73,158 ("a fund triggers EDGAR/ADV connectors").
- Bulk format, private-fund-type field, adviser/fund identifiers, refresh cadence (from "Research: Form ADV and IRS exempt-org bulk data"); storage per "Owner kind…".
- Matching ADV advisers/funds and EO-BMF orgs to existing entities (resolution path).
- **From "Claim producers and the claims door"** (2026-11-05; summary in evidence_layer_plan.md "Producers and the door"): Form ADV is an `etl` producer. Each run checks the file header and reads columns by name before writing anything; one document per row; each claim quotes the whole data line; it emits identity records for advisers (and funds, from the archive); `producer_version` is a module constant.
- **From "Entity lifecycle"** (2026-11-06; notes in evidence_layer_plan.md §4 `entities`): a Form ADV identity record that matches an entity typed `company` changes it to `investment_firm` (adviser) or `fund` (private fund) by code, with an events row.
- **From "Owner kind: storage, evidence and the PE-firm test"** (2026-11-07; ADR 0001 amended; table in evidence_layer_plan.md §4 `owner_kind_evidence`): the Form ADV ETL emits rank-1 `owner_kind_evidence` rows for advisers with `Any PE Funds = Y` (quote = the whole data line); `N` emits nothing. The IRS exempt-org file emits rank-1 `nonprofit` rows matched by EIN. Rows ride in the same door call as the identity records.
- **From "Funds and their investment firm"** (2026-11-07; ADR 0001 amended; notes in evidence_layer_plan.md §4): (1) archive fund rows give fund identity records (name, `805-` id), a `managed_by` claim to the adviser, and rank-1 evidence from the fund's `Fund Type` (Private Equity → `private_equity`, Real Estate → `real_estate`, Venture Capital → `venture_capital`, hedge, securitized asset, liquidity → `other_investment_fund`, Other Private Fund → none). (2) For each firm in the graph, read its current IAPD Form ADV PDF for its fund list (names and `805-` numbers as text; type checkboxes not readable), typing funds and linking them; cadence is this ticket's. (3) Group a firm's adviser registrations into one `investment_firm` from Schedule D Section 7.A (related advisers); whether the bulk files carry it, and how current, is this ticket's; joint-venture advisers (FS/KKR Advisor) stay their own firm. (4) A firm's kind from the monthly counts by fund type: any PE fund → `private_equity`, all real estate or all VC → that kind, any other mix → `other_investment_fund`; `Y` on any registration counts. This ticket is no longer blocked by "Funds and their investment firm".
- **From "Document storage, fetch log and last-confirmed"** (2026-11-07; notes in evidence_layer_plan.md §4 `documents` and `fetches`): each monthly file is a parent; each adviser row is a recurring child whose identity is a stable dataset address the connector supplies (such as the SEC's monthly-adviser page) plus the CRD, so an unchanged row next month advances `last_seen_at` and makes no new claims.
- **From "Rosters, portfolio pages and the registry"** (2026-11-12; notes in evidence_layer_plan.md §4 `entity_identifiers`): ingestion writes a `domain` identifier row from each adviser's `Website Address`, sourced by the adviser's row, skipping social media and reference sites (linkedin.com, facebook.com, twitter.com, x.com, youtube.com, instagram.com, wikipedia.org, podbean.com and the like). The monthly file holds only the first of several websites: for about 40 of the roughly 100 audited firms it is LinkedIn, Facebook, YouTube or Wikipedia. Registry entries add a firm's other domains through intake items.

## Comments

- 2026-11-15, claimed. Facts checked:
  - SEC monthly files, November 2026 (`ia110226-registered.zip`, `ia11022026-exempt.zip`; sec.gov information-about-registered-investment-advisers-exempt-reporting-advisers). Registered: 17,263 rows, 448 columns; 6,086 answer Item 7.B yes (advise private funds); 1,049 are umbrella registrations, whose relying advisers have no row of their own. ERAs: 6,848 rows, 171 columns; Any PE Funds = Y for 2,017, Any VC Funds = Y for 2,760. Both files carry CRD, additional CRD, SEC#, CIK, primary and legal names, the first website, Latest ADV Filing Date, and Any/Total counts by fund type. For related advisers (Item 7.A) they carry only counts, never names.
  - Leonard Green, CRD 158164: PE funds 107; the file's website is LinkedIn.
  - IAPD PDF for Leonard Green (https://reports.adviserinfo.sec.gov/reports/ADV/158164/PDF/158164.pdf): 23 MB, 509 pages, 117 distinct 805- IDs. Fund name, 805- ID and general partner names come through as text. The fund-type and related-adviser checkboxes (control, common control, kind of related person) do not; every option prints for every entry. Related-person names and file numbers do come through. pdfplumber ran out of memory on this file; pypdf page by page worked.
  - EINs: no connector writes `ein` identifiers today, so the IRS file, which matches only by EIN, would match nothing at launch.
- Round 1 asked (Q1 to Q4).
- 2026-11-15 (developer, "yes to q1 through q4"), settled:
  - Q1: load every adviser that advises private funds (registered with Item 7.B yes, about 6,086, plus every exempt reporting adviser, about 6,848) from both monthly files each month, before the first seeding pass: an investment_firm identity record (CRD, SEC#, CIK, primary and legal names), rank-1 owner-kind evidence as ruled in tickets 14 and 65, and the domain row from ticket 30. Advisers without private funds are not loaded. Unchanged rows only advance last_seen_at; an adviser that drops out keeps its entity and evidence.
  - Q2: funds come once from the FOIA archive (latest row per 805- ID through 2024-12-31: identity, managed_by claim to the adviser, rank-1 kind from Fund Type), then, for firms in a tracked brand's ownership chain, from the firm's current IAPD PDF read by a code parser (fund name, 805- ID, general partner; post-2024 funds take the firm's kind), re-read whenever the firm's Latest ADV Filing Date changes in the monthly file.
  - Q3: a firm's separate registrations join one investment_firm through its registry entry, which lists its CRDs (approved by the developer's commit); no automatic grouping; a firm without a registry entry stays one entity per registration; umbrella registrations are already one row.
  - Q4: the IRS exempt-org file is deferred to the local-businesses map (nothing writes EINs at launch; few nonprofit owners in the launch categories). The rank-1 nonprofit rule stays recorded. The engine destination drops IRS exempt-org ingestion.
- 2026-11-15, round 2 asked (Q5 to Q7). Facts: reports.adviserinfo.sec.gov returns S3 "AccessDenied" (403) for robots.txt, i.e. no file; adviserinfo.sec.gov robots.txt blocks only form-view, brochure and lock paths, and points its sitemap at the reports host. Blackstone has 29 registrations in the November file.
- 2026-11-15 (developer, "yes to q5 through q7"), settled:
  - Q5: the bot follows RFC 9309 on every site: a robots.txt answer of 4xx other than 429 means no restrictions; 5xx or an unreachable host means everything is treated as blocked and retried later. SEC fair access still applies (declared user agent, at most 10 requests a second).
  - Q6: advisers that stopped filing before 2025 come in once from the archive: every adviser whose last filing reported a private fund gets an identity record and rank-1 kind evidence from that filing, dated with it.
  - Q7: a firm's IAPD PDF is first read when the firm enters a tracked brand's ownership chain in any phase (pending included), then re-read on filing-date changes; a firm that leaves every tracked chain stops being re-read and keeps what was read.

## Answer

Resolved 2026-11-15 in one grilling session (two rounds, Q1 to Q7; facts under Comments).

- **Advisers (Q1):** each month, load every adviser that advises private funds from both SEC monthly files. That is registered advisers answering Item 7.B yes (about 6,086 of 17,263) and every exempt reporting adviser (6,848). Each gets an `investment_firm` identity record (CRD, SEC#, CIK, primary and legal names), rank-1 owner-kind evidence as ruled in "Owner kind" and "Funds and their investment firm", and a `domain` row as ruled in "Rosters, portfolio pages and the registry". The first load runs before the first seeding pass, so claims resolve to firms whose kind is already known. Advisers without private funds are not loaded. Unchanged rows only advance `last_seen_at`. An adviser that drops out of the file keeps its entity and evidence, because absence proves nothing.
- **Funds (Q2):** the FOIA archive is loaded once, taking the latest row per 805- ID through 2024-12-31. Each row gives a fund identity record, a `managed_by` claim to its adviser, and rank-1 kind evidence from its Fund Type. After that, a code parser reads a firm's current IAPD PDF (`reports.adviserinfo.sec.gov/reports/ADV/{CRD}/PDF/{CRD}.pdf`) for each fund's name, 805- ID and general partner. Fund-type checkboxes don't come through as text, so post-2024 funds take the firm's kind. The PDF is re-read whenever the firm's Latest ADV Filing Date changes in the monthly file.
- **When a PDF is read (Q7):** first when the firm enters a tracked brand's ownership chain in any phase, pending included; then on filing-date changes. A firm that leaves every tracked chain stops being re-read and keeps what was already read.
- **Advisers that stopped filing (Q6):** the archive also gives, once, an identity record and rank-1 kind evidence from the last filing of every adviser whose last filing reported a private fund. These are dated with that filing.
- **Grouping (Q3):** a firm's separate registrations join one `investment_firm` through its registry entry, which gains a list of the firm's CRDs, approved by the developer's commit. There is no automatic grouping: related-adviser names in the monthly files are counts only, and the PDFs' control checkboxes don't come through as text. A firm without a registry entry stays one entity per registration. Umbrella registrations are already one row. Blackstone, for example, has 29 registrations. Mechanically, code merges the listed registrations' entities into one `investment_firm` under the "Entity lifecycle" merge rules (a pointer, nothing rewritten). This adds a merge trigger beside the ones that ticket listed.
- **Robots (Q5, applies to every site):** the bot follows RFC 9309. A robots.txt answer of 4xx other than 429 means no restrictions; a 5xx or an unreachable host means everything is treated as blocked and retried later. The IAPD PDF host returns 403 for robots.txt, meaning there is no file. SEC fair access still applies: a declared user agent and at most 10 requests a second.
- **IRS exempt-org file (Q4):** deferred to the local-businesses map as "IRS exempt-org file and nonprofit owners". The file matches only by EIN, nothing in the engine writes EINs at launch, and the launch categories have few nonprofit owners. The rank-1 nonprofit rule in ADR 0001 stays. The engine destination drops IRS exempt-org ingestion.
- **Docs:** `evidence_layer_plan.md` gets a new "Form ADV connector" section, the registry entry's CRD list, and the robots rule. CLAUDE.md's scrape-etiquette line gets the robots rule. No ADR.

Handed on:
- **"Entity resolution algorithm":** matching extracted names to the preloaded firms, whose names are uppercase legal names such as "LEONARD GREEN & PARTNERS, L.P.", and grouping by registry CRDs.
- **"Retrieval fan-out, tracked entities and refresh cadence":** polling the monthly files, and the PDF triggers.
- **"Celery topology":** the monthly load, the one-time archive load and the PDF parser tasks.
- **"Operational identity, budgets and guardrail values":** shape-check alerts for the monthly files and the SEC user agent.
- **"Testing and acceptance":** fixtures, meaning real monthly rows, archive rows and one IAPD PDF.

### Amended 2026-11-21 (from "Cost cuts before revenue")

- The monthly Form ADV load runs as the first step of the operator pass when a new month's file is out, instead of on a monthly schedule; IAPD PDF re-reads on a changed filing date run in the same pass.
