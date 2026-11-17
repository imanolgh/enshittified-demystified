# Research: Where PE owns consumer brands

Type: research
Status: resolved
Blocked by: none
Map: [chains-and-brands](../map.md)

## Question

Starting from what PE firms own rather than from a guessed list, which consumer-facing industries hold the most PE-owned brands, and which of them neither category audit nor the industry screen has measured?

## Context

- Added 2026-11-16 in "Product categories: vocabulary and assignment" (Q11). The developer asked how the screen's twelve industries were chosen; answer: Claude named them from general knowledge plus the developer's bowling example, so both candidate lists (the pivot proposal's thirteen and the screen's twelve) were guesses that were then measured. This ticket finds candidates bottom-up. The developer wants to run it right after "Product categories".
- Already measured: thirteen industries in [category-audit-pilot](../research/category-audit-pilot.md) and [category-audit-full](../research/category-audit-full.md), twelve in [industry-screen](../research/industry-screen.md).
- Estimated cost approved: roughly 1 to 2M tokens (not sized against real portfolios).

## Find out

1. **Portfolio pages:** the current portfolio pages of the PE firms with the most PE funds in the SEC's monthly Form ADV files, plus consumer-focused firms (Roark, Sycamore, L Catterton, TSG and similar), about 50 to 100 firms. Sort each consumer-facing portfolio company into an industry and count companies and brands per industry. Note rollups whose locations keep local names separately.
2. **BDC borrowers:** counts by the Industry Sector column of the latest SEC BDC data set (`soi.tsv`), as a cross-check of where PE-backed borrowers cluster.
3. **Screen anything new:** for each industry with several PE-owned consumer brands that isn't already measured, the top ~10 brands as in "Research: Industry screen".

## Rules

- Same rules as "Research: Industry screen": public primary sources only, trade press for rankings only, no PitchBook, Preqin, CB Insights or paywalled sources, competitor sites never sources, never fetch WhoIsMyDentist, Private Equity Vet or Reddit; robots.txt followed, SEC user agent `EvidenceEngine ownership-research bot (pe consumer scan)` with no email, at or under 2 per second; owner types are research notes, not engine classifications.
- Industry sorting here is a research note for a human decision, not the engine's industry assignment (which comes only from industry brand lists).
- Findings go to `.scratch/chains-and-brands/research/pe-consumer-scan.md`.

## Answer

Resolved 2026-11-16 by ten background workers in three passes (about 2.72M tokens). Findings: [pe-consumer-scan](../research/pe-consumer-scan.md), with the worker reports in [research/pe-consumer-scan/](../research/pe-consumer-scan/).

- **Bottom-up scan (step 1):** 73 of 88 PE firms gave a readable current portfolio, about 735 distinct consumer-facing US companies. It confirms the measured industries (restaurants 70 listings, home services 57, gyms 24, dental 22, women's apparel 18, vet, car washes, auto service, urgent care, child care, physical therapy) and surfaces unmeasured clusters (specialty physician practices, packaged food, beauty, behavioral health, home care, personal care, pet food, beverages, primary care, med spas, education).
- **Twelve new industries screened (step 3), PE share of the top brands:** med spas and beauty services 100%, behavioral health 77%, education and youth activities 58%, home care and hospice 43% (all worth a full audit); primary care 25%, pet food 20% (company rows), sporting goods 10%, apparel 7%; beauty, personal care, packaged food and beverages 0% at top 10 with dozens of PE brands below.
- **Biggest firms without a portfolio list:** true on their sites; their retail PE funds' SEC filings give only an industry mix; newsroom rebuilds found 15 current US consumer companies for Blackstone, 12 for Apollo, 20 for Bain, 4 for Ares and none for Brookfield, an overcount because exits are rarely announced. They add grocery, thrift stores, arts and crafts retail and casinos as unmeasured clusters.
- **Step 2 dropped:** the SEC BDC data set's per-holding industry field is filled on 3% of holdings.
- **Rulings during the ticket:** Q12 all twelve industries (developer chose (b) over Claude's eight); Q13 newsroom rebuild; Q14 Kumon and Huntington evidence dropped (read on browser retries after a 403).
- **Bot slips** by research workers are recorded in the findings (redirects followed before reading robots.txt, a disallowed path, crawl-delay misses, 403 retries, one loop of 401s); a redirect and 403 rule was proposed on engine "Operational identity and guardrails".

Handed on:
- "Launch industries": every result above, the unmeasured clusters (grocery, thrift stores, arts and crafts, specialty physician practices, hotels), how to count product industries (top 10 vs long tail), and the counting questions collected from the screen and the scan.
- engine "Operational identity and guardrails": the redirect and 403 rule.

## Comments

### 2026-11-16 run

- **Firm selection.** Ranking advisers by PE fund count in the SEC's November 2026 adviser files (4,594 advisers report PE funds) is noisy at the top: SPV platforms (MicroAngel 833, EquityBee 581), fund-of-funds and secondaries managers (Hamilton Lane, StepStone, Adams Street, HarbourVest), wealth managers, venture and software firms, and infrastructure managers. Claude kept the buyout firms from that ranking and added consumer-focused firms and the firms the audits and the screen found owning consumer brands: 88 firms in four groups of 22.
- **Step 2 dropped.** In the August 2026 SEC BDC data set, the per-holding industry field (`Investment, Industry Sector [Extensible Enumeration]`) is filled on 4,483 of 143,266 holding rows (3%), and the Industry Sector Axis sits on subtotal rows, so a sector count of BDC borrowers isn't a useful cross-check without parsing the filings.
- **Step 1 done** (about 1.0M tokens): [pe-consumer-scan](../research/pe-consumer-scan.md), with the four worker reports in [research/pe-consumer-scan/](../research/pe-consumer-scan/). 73 of 88 firms gave a usable current list; about 735 distinct consumer-facing companies. Unmeasured clusters with the most listings: specialty physician practices (about 40, mostly local-name rollups), packaged food (40), beauty and cosmetics (37), hotels (36, franchised brands), behavioral health (about 28), apparel (about 23), sporting goods and outdoor (about 23), home care and hospice (about 20), personal care (17), pet food and products (17), beverages (16), primary care (16), med spas and beauty services (about 16). Step 3 waits on the developer's choice of industries and budget.
- **Step 3 scope** (Q12): the developer chose option (b), all twelve new industries (med spas and beauty services, beauty and cosmetics, personal care, home care and hospice, behavioral health, primary care, packaged food, beverages, pet food and products, education and youth activities, apparel other than women's, sporting goods and outdoor) over Claude's eight; launched 2026-11-16 as four background workers (about 1.1M tokens; ticket total about 2.1M). Product industries also report how many scan-found PE brands sit outside their top 10, because their top 10 by sales are mostly large public companies' brands.
- **The biggest firms without a portfolio list** (the developer asked whether that's true and whether the lists exist elsewhere): checked 2026-11-16. Bain's sitemap (about 2,750 URLs), Blackstone's sitemaps (pages, people, news, funds) and Apollo's site have no portfolio list (Apollo states "190+ portfolio companies"). Elsewhere: Blackstone (BXPE, CIK 1930054), KKR (K-PEC, 1957845) and Brookfield (Brookfield Private Equity Fund LP, 2074065) run retail PE funds that file 10-Ks and 10-Qs, but BXPE's 2026-09-30 schedule names only its largest positions and groups the rest as "Other Investment(s) in Equity" by industry and region, so it gives an industry mix, not a company list; Apollo's retail fund (Apollo Aligned Alternatives) files no reports; Bain has no such PE fund. The firms' own newsrooms announce their deals (e.g. Bain's "Guidehouse ... to be acquired by Bain Capital Private Equity"), so a portfolio can be rebuilt from acquisitions minus announced exits, with a start year because quiet sales stay invisible. Proposed to the developer as Q13 (Blackstone, Apollo, Bain, Brookfield, Ares; about 0.5M tokens; ticket total about 2.6M), pending.
- **Step 3 done** (about 1.19M tokens; ticket total about 2.2M): med spas and beauty services 10 of 10 (100%), behavioral health 10 of 13 (77%), education and youth activities 7 of 12 (58%), home care and hospice 6 of 14 (43%) all judged worth a full audit; primary care 25%, pet food 20% by company row, sporting goods 10%, apparel 7%, beauty, personal care, packaged food and beverages 0% at top 10 (PE sits in the long tail). Seven new counting questions handed to "Launch industries". Bot slips recorded in the findings. Q13 (the biggest firms' newsrooms) still pending; the ticket stays open until the developer answers it.
- **Q13 approved** (2026-11-16): the newsroom rebuild for Blackstone, Apollo, Bain, Brookfield and Ares launched as two background workers (about 0.5M tokens; ticket total about 2.7M). Deals since 2015 from each firm's own newsroom, filtered by title in code, consumer targets kept, exits checked; private equity, growth and hybrid funds only (real estate, credit and infrastructure deals noted separately). Workers were told to check robots.txt before following any redirect and never to retry a plain 403.
- **Q14** (2026-11-16; the developer asked whether the robots slips mattered, since most sites allowed the bot anyway; answered: most were process slips where the site's answer was yes, but three broke a site's stated rule (Bregal Partners `Disallow: /`, one request; BAYADA's disallowed `/archive/`, one request; Harvest and Transom's 10-second crawl-delay, a few requests; nothing from the banned pages used) and the Kumon and Huntington browser retries after a 403 are a gray area): the Kumon and Huntington evidence is dropped and both rows read "not found" until sourced again from a page the site serves normally. No PE share changes.
- **Newsroom rebuild done** (about 0.53M tokens; ticket total about 2.72M): Blackstone 15, Apollo 12, Bain 20, Ares 4 current US consumer companies, Brookfield 0; exits rarely announced, so current overstates; new clusters grocery, thrift stores, arts and crafts, casinos. One slip: a loop of six requests to Ares's content API kept going after a 401. Ticket resolved.
