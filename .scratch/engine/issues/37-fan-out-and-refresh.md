# Retrieval fan-out, tracked entities and refresh cadence

Type: grilling
Status: resolved
Blocked by: 30, 32, 34, 36, 70, 71, 73  (Rosters, portfolio pages and the registry; Press and EDGAR full-text connectors; Form ADV and IRS exempt-org ingestion; BDC discovery and Schedule of Investments parsing; EDGAR full-text search and ownership filings; Research: Web search APIs for finding a brand's past coverage; Task: Test search API coverage of older deals)
Map: [engine](../map.md)

## Question

Given an entity, which connectors run (the routing matrix), how far research recurses, how partial failures are handled, which entities are "tracked"?

*(2026-11-20, round 1 Q0: split. The past-coverage route's details went to [118 "Past coverage through DeepSeek Search"](118-past-coverage-through-deepseek-search.md), and every interval, the pending-deal pace and the card's next-check date went to [119 "Refresh schedule and next-check date"](119-refresh-schedule-and-next-check-date.md). This ticket keeps the routing matrix, recursion, tracked entities and failures. The title is kept so other tickets' references still resolve.)*

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
- **From "Press and EDGAR full-text connectors"** (2026-11-08; scrape etiquette in CLAUDE.md; press-connector note in evidence_layer_plan.md): the wire subject feeds are polled for all tracked entities at once, faster than each turns over its 20 items, with a daily news-sitemap backfill; the intervals are this ticket's. Matching uses tracked entities' names and aliases, so which entities are tracked sets what the feeds can catch. Past coverage (a 2021 deal) has no route yet: "Research: Web search APIs for finding a brand's past coverage" reports first, and the historical route is decided here. This ticket also waits on "EDGAR full-text search and ownership filings".
- **From "Research: Web search APIs for finding a brand's past coverage"** (2026-11-08; findings in research/web-search-apis.md): Google's Custom Search JSON API (closed to new customers, ends 2027-01-01) and Bing (retired 2025-08-11; its successor bars crawling result links) are out; scraping resellers are out. Usable: Mojeek (£2 per 1,000 with a 1-hour cache, £3 with indefinite storage; AI and commercial use allowed; terms expect customers to fetch result URLs; exact phrase not documented), Brave ($5 per 1,000; transient storage only without a storage-rights plan, price unpublished), Exa and Perplexity (storage terms unclear). About 1,496 queries a quarterly run for 374 brands costs roughly $2–11 a run on any of them. No vendor documents index depth for 2015–2024 pages; testing needs an account. Which route, if any, is this ticket's; whether keeping a result URL counts as storing results is in chains "Legal review before launch".
- **From "Task: Test search API coverage of older deals"** (2026-11-19; hit table in that ticket): the developer chose **DeepSeek Search as the only web search API** (one vendor for every AI integration, and it is the cheapest at $0.75 per 1,000 requests for up to 50 results). The developer also ruled that its results may be kept and shown, since the terms don't ban it. Over 13 deals from 2015 to 2024, `"<owner>" "<brand>"` found a primary page for all 13 (the known page for 8). Brand plus "acquisition" found one for 6. The brand alone found none. A date window ranks the page first but drops pages DeepSeek misdates. So search confirms and dates owners we already know of, and discovers about half of the unknown ones. The engine's crawler fetches each result URL, with `need_content: false`. There is no fallback search if DeepSeek is down. Whether search is the historical route stays this ticket's decision.
- **From "EDGAR full-text search and ownership filings"** (2026-11-08; section in evidence_layer_plan.md): full-text search runs per brand (a first run since 2001, then only filings since the last run), and each public company's 13Ds and 13Gs are re-read for new filings and amendments; both cadences are this ticket's, within the SEC's 10 requests a second shared across EDGAR connectors.
- **From "Rosters, portfolio pages and the registry"** (2026-11-12; notes in evidence_layer_plan.md "Registry crawler" and §4 `edges`): the registry pass (every required portfolio, about and newsroom page, with their detail and paged pages, plus the new releases newsrooms list) is a shared source whose cadence is this ticket's. Detail pages are re-fetched every pass with conditional requests (a 100-page firm at a 10-second crawl delay takes about 17 minutes). Releases are fetched once and never re-fetched for confirmation, since they confirm only as of their own date; a periodic check that receipt links still work (for the dead-link note) is this ticket's. Confirmation now depends on source type: `company_site` pages confirm whenever seen again with the company on them; releases, news and filings only as of their own dates.
- **From "Form ADV and IRS exempt-org ingestion"** (2026-11-15; evidence_layer_plan.md "Form ADV connector"): the SEC monthly adviser files are polled each month and loaded before the first seeding pass; the FOIA archive is loaded once; a firm's IAPD PDF is read when the firm enters a tracked brand's ownership chain in any phase, and again whenever its Latest ADV Filing Date changes in the monthly file; a firm that leaves every tracked chain stops being re-read.
- **From "BDC discovery and Schedule of Investments parsing"** (2026-11-16; section "BDC connector and Schedule parser" in evidence_layer_plan.md §5): BDC sources to schedule: a daily check of each BDC's submissions JSON (about 187 requests; new 10-K, 10-Q or amendment with a tagged Schedule parsed the same day); a monthly universe job (SEC BDC data sets plus BDC Report, confirmed in submissions JSON); a monthly comparison of each new SEC BDC data-set file with that month's parsed filings; a one-time load of about 2,400 tagged filings since 2022–23.
- **From chains "What would change this"** (2026-11-18): brand cards show "Next check due {Mon YYYY}", so the refresh schedule must give each brand a next scheduled check date the card can read.

## Comments

**2026-11-20, round 1 (developer: yes to all; Q2 option b):**
- **Q0, split:** 118 (past coverage through DeepSeek Search) and 119 (refresh schedule and next-check date), both blocked by 37; chains 94 is blocked by 37, 118 and 119.
- **Q1, tracked:** every brand listed on an industry page, plus every entity reached from one through a pending, active or unconfirmed hop. Ended hops don't count. Membership is recomputed whenever edges change. An entity that stops being tracked stops its own runs, and its documents, claims and edges stay. Entities named only in documents (a firm's other portfolio companies) are never tracked. BDCs and Form ADV advisers are loaded by their own whole-universe jobs regardless.
- **Q2, climbing (option b):** research keeps climbing through companies and investment firms wherever a source names an owner: Form ADV Schedules A and B, 13D/13G for listed firms, releases. It stops at families and governments (nothing above them), at funds (their investors are the parked retirement side), where no owner is found, and at a hop cap against loops (value: "Operational identity, budgets and guardrail values"). It never goes down. Verdicts still come from the chain up to the first private equity owner (ADR 0001 unchanged). Owners above the first PE owner are tracked and get their own reads, but aren't matched in the wire feeds. The developer's reason: a fuller graph from day one for a later paid research tier for researchers and journalists.
- **Q3, routing table:**
  - brand: EDGAR full-text search on its names; its registry entry (newsroom, about page); wire-feed matching; DeepSeek Search (118); USPTO check in the 7 licensing-prone industries (waiting on chains 105);
  - company: full-text search on its names; its registry entry if any; 13D/13G if public; wire-feed matching;
  - investment firm: its registry entry; Form ADV (monthly file plus IAPD PDF); wire-feed matching;
  - fund: Form ADV (archive plus its firm's IAPD PDF); the BDC connector if a BDC;
  - location: nothing at launch.

  Full-text search runs on every tracked brand and every tracked company, not only a brand's direct owner (reading ticket 70's "per brand and company name" broadly).
- **Q4, failures:**
  - sources run independently, and claims from finished sources publish at once;
  - a failed re-run of a per-entity source leaves its earlier completed run in force, as for shared passes;
  - a failed run is retried daily for up to 7 days, then only at its normal interval, and stays on the operator report until it completes;
  - blocked runs aren't retried early (robots.txt is re-read at each normal run; a site that asked us to stop stays stopped);
  - Celery mechanics (ChordError) are ticket 38's.
- **Q5, past coverage:** DeepSeek Search is added alongside EDGAR full-text search; details in 118. Comparison run 2026-11-20 on the same 13 private test deals: EDGAR found no deal document for any. Brand-name hits were lenders' schedules (FS KKR for Dental365, Carlyle Secured Lending for Super Star), landlords' tenant lists, mortgage-pool prospectuses and a licensee (Caleres for Dr. Scholl's), with Lap of Love at 0 hits. Owner plus brand gave two possible second sources after ticket 70's exclusions. DeepSeek found a primary page for all 13.
- **Side finding for "Operational identity, budgets and guardrail values":** full-text search on a big brand name returns hundreds to thousands of hits (Aspen Dental 2,095, Natrol 1,543, MB2 Dental 1,408), mostly lenders, landlords and mortgage pools. Ticket 70 reads every hit whole, so most of that spend goes to noise, and the newest-first 100-hit cap can push older real filings out.

**2026-11-20, round 2 (developer: yes to all as revised):**
- **Q2 reversed (replaces round 1's option b):** the developer reversed the climb above private equity owners on cost grounds. Research stops where the verdict is settled. It climbs through brands, companies with no known kind, conglomerates and public companies (one more level, to their 13D/13G holders). It stops at any investment firm or fund, a family, a government, a nonprofit, a trust, a cooperative or an employee-owned owner, and wherever no owner is found. The hop cap stays (value in 42), and nothing climbs down. Stopping at *every* owner kind was ruled out with real chains: Petco → Petco Health and Wellness (public, Nasdaq: WOOF; CVC and CPP Investments control 64.4% of votes through Scooby Aggregator) and Dunkin' → Inspire Brands → Roark Capital would lose their PE owner. Dropped as moot: a Form ADV Schedule A/B reader, a stake-range schema change, and hiding above-PE owners on cards. A later research tier can add the climb back; the schedules are printed in the IAPD PDFs we already fetch (checked 2026-11-20 on JAB Capital Management's PDF: name, person or entity, title, month acquired, ownership code NA/A–E, control flag, CRD; Schedule B codes C–F).
- **Q6:** a newly tracked entity's own sources (full-text search, 13D/13G, Form ADV PDF, DeepSeek Search) run as soon as it becomes tracked. Shared passes count from the next complete pass.
- **Q10:** the registry pass skips pages of entries whose entity is no longer tracked. The YAML file stays, and the pages come back on their own if the entity is tracked again.
- **Q11 (corrected):** a 13G filed under Rule 13d-1(b), the institutional box, is stored as a claim and edge and can be shown, but doesn't make the holder tracked and never counts toward a category (ticket 27). Holders on a 13D, or on a 13G under (c) or (d), count and are tracked as usual. A correction during the round: ticket 27's line is (b) only, so a (c) filing from a firm classed private equity counts.
- **Q13:** new chains ticket [121 "Large shareholders of public owners on the card"](../../chains-and-brands/issues/121-large-shareholders-of-public-owners-on-the-card.md), recommending every 5%+ holder with listed asset managers marked.
- **Q14:** a second route into tracked: investment firms on an operator list are tracked even when no listed brand's chain reaches them. They get wire-feed matching and Form ADV reads, and their holdings in tracked public companies and their BDC loans arrive through those companies' filings and the BDC connector. The list starts with BlackRock, Vanguard and State Street, and grows by operator upload. Whether Vanguard is in the Form ADV load (only advisers with private funds load) is unchecked.
- **Q15:** the full asset-manager feature (13F, N-PORT look-through, firm pages, labels) is parked as its own map, [Asset Managers](../../asset-managers/map.md); ADR 0004 gains "Asset managers parked".
- **Q16:** the developer asked why BlackRock, State Street and Fidelity are classed private equity. Ticket 14's rank-1 rule ("any PE fund → private_equity", across every registration) catches them (BlackRock reports 125 PE funds), and ticket 27 patched only their 13d-1(b) stakes. New v1 engine ticket [120 "The private equity firm test and asset managers"](120-pe-firm-test-and-asset-managers.md). A background Form ADV fund-mix check feeds it (research/adv-fund-type-mix.md).

## Answer

Resolved 2026-11-20 in a grilling session (two rounds, recorded under Comments). Split in round 1: past coverage → [118](118-past-coverage-through-deepseek-search.md), intervals and the next-check date → [119](119-refresh-schedule-and-next-check-date.md). Recorded in evidence_layer_plan.md §5 Stage 2 (with notes in the press, EDGAR, registry and Form ADV sections and §4 `source_runs`) and the glossary entry "Tracked".

- **Tracked:**
  - every brand listed on an industry page;
  - every entity reached from one through a pending, active or unconfirmed hop, as far as research climbs;
  - every investment firm on the operator's tracking list (BlackRock, Vanguard and State Street to start).

  Membership is recomputed whenever edges change. Leaving stops an entity's runs and keeps its data. A holder whose 13G is filed under 13d-1(b) isn't tracked through that filing. Entities named only in documents are never tracked.
- **Climbing:** research looks for the owners of brands, companies with no known kind, conglomerates and public companies (to their 13D/13G holders). It stops at investment firms and funds, families, governments, nonprofits, trusts, cooperatives, employee-owned owners and dead ends, with a hop cap. It never goes down. The developer first chose to climb above PE owners, then reversed it on cost; stopping at every owner kind was ruled out because Petco (public) and Dunkin' (Inspire Brands) would lose their PE owner.
- **Routing:**
  - brand: full-text search, registry entry, feed matching, DeepSeek Search, USPTO in 7 industries;
  - company: full-text search, registry entry, 13D/13G if public, feed matching;
  - investment firm: registry entry, Form ADV, feed matching (list-only firms: feed matching and Form ADV);
  - fund: Form ADV, and the BDC connector if a BDC;
  - location: nothing.

  Full-text search covers every tracked brand and company.
- **Start:** a newly tracked entity's own sources run at once. The registry pass skips entries whose entity isn't tracked.
- **Failures:** sources run independently, and a failed re-run leaves the last completed run in force. Failed runs are retried daily for up to 7 days, and blocked runs aren't retried early.
- **Past coverage:** DeepSeek Search is added alongside EDGAR full-text search. On 13 private test deals, EDGAR found no deal document and DeepSeek found a primary page for all 13.

Handed on:
- 118: queries, result filtering, wire results, re-runs.
- 119: every interval, the pending-deal pace, link checks, the remaining Beat jobs, the card's next-check date, the 7-day retry inside the schedule.
- New engine [120 "The private equity firm test and asset managers"](120-pe-firm-test-and-asset-managers.md): the Form ADV rule classes BlackRock, State Street, Fidelity, J.P. Morgan and T. Rowe Price as private equity firms.
- New chains [121 "Large shareholders of public owners on the card"](../../chains-and-brands/issues/121-large-shareholders-of-public-owners-on-the-card.md).
- New parked map [Asset Managers](../../asset-managers/map.md), with ADR 0004 amended.
- "Operational identity, budgets and guardrail values": the hop cap; full-text search noise.
- "Celery topology": independent sources.
- chains "Brand-level checked: required sources and freshness": the routing table and failure rules.

