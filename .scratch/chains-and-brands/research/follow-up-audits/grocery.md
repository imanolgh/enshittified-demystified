# Follow-up audit: Grocery (30 banners)

Ticket: [93-research-follow-up-audits-four-industries](../../issues/93-research-follow-up-audits-four-industries.md), item 1 · Researched 2026-11-17/18 (fetches logged 2026-11-17T23:58Z to 2026-11-18T00:18Z) · Ownership facts come from primary sources only (SEC filings, company sites and store directories, Kroger's own 8-K). NRF's Top 100 supplies the ranking; search leads supply a few store counts used only to place rows, each marked.

**Short answer**

| | Grocery (N = 30 multi-state banner rows) |
|---|---|
| PE-owned plus PE minority stake, by banner row | **6 / 30 (20.0%)**, all **PE minority stake**: Albertsons Companies' Safeway, Albertsons, Jewel-Osco, Vons, ACME and Shaw's. Cerberus Capital Management holds 31.0% (proxy, June 2026) on a Schedule 13G filed under Rule 13d-1(d); no later Cerberus amendment is on file; its Form ADV says `Any PE Funds = Y` (9 PE funds). **PE-owned (control): 0.** |
| Sensitivity | Shaw's is row 30 (est. $4.59B, $0.09B above Ingles). Adding Whole Foods (Amazon; left out because NRF folds it into Amazon) or counting single-state H-E-B pushes Shaw's to row 31: **5 / 30 (16.7%)**. Every 30-banner variant tried stays at or above 16.7%, so grocery clears the 10% bar on this audit. |
| Owner not found | **2 / 30 (6.7%)**: Trader Joe's (its about page returned 403) and WinCo Foods (robots.txt disallows ClaudeBot for the whole site). Three more rows name a company or founders but no owner: Market Basket, Piggly Wiggly (C&S) and Smart & Final (Chedraui USA); Aldi's "family" rests on a founder sentence. |
| BDC overlap | **0 / 30.** No BDC Schedule of Investments row (SEC BDC data sets, July to October 2026) names any of the 30 banners or their parents. Just below the cut: Northeast Grocery Inc. (Tops, Price Chopper; Great Elm Capital Corp., first-lien loan), Southeastern Grocers LLC (Winn-Dixie; Silver Point funds) and Heritage Grocers Group (formerly Tony's Fresh Market / Cardenas, Apollo; OFS, Hancock Park, Fidelity). |
| Brand-direct affiliate programs | **Not checked**; none came up on any page read. Grocery banners sell through stores, not referral links. |

- **The share rests entirely on one owner.** Six Albertsons banners make the 30; nothing else in the top 30 has a PE holder. Every other row is a public company with only passive holders (Kroger, Ahold Delhaize, Sprouts, Weis), a family, an employee owner, a cooperative, or a private company with no PE evidence.
- **Kroger's banners count 5 of the 30** (Kroger, Harris Teeter, Smith's, Fred Meyer, Food 4 Less) and Ahold Delhaize's 5 (Food Lion, Stop & Shop, The GIANT Company, Hannaford, Giant Food). Neither has a PE holder found: Kroger has no 13D on file and its largest 13G holder checked (Berkshire Hathaway) files under Rule 13d-1(b); Ahold Delhaize is not an SEC filer.
- **Pending, not counted:** Kroger agreed on 2026-07-01 to buy Giant Eagle (family-owned), closing expected in 2027. C&S Wholesale Grocers proposes to become majority owner of Winn-Dixie (below the cut).

## How this was sourced (read first)

- **Ranking:** NRF, "Top 100 Retailers 2026 List" (compiled by Kantar), 2025 US retail sales by company, read from the screen worker's saved copy (`pages/screen2-a/002`). NRF does not label segments, so it does not "treat" Walmart, Costco, Target, Amazon, BJ's or dollar stores as grocers; they are left out (see "Ranking"). Banners are then sized as described under "Ranking".
- **Ownership facts:** SEC filings (10-K, 10-Q, DEF 14A, 8-K, Schedules 13G/13G/A), Albertsons' and Kroger's banner and corporate pages, Albertsons' banner store directories (`local.<banner>.com`), Ahold Delhaize's brand pages, company about pages, and Form ADV (November 2026 rosters, local copy).
- **Reused from the screen worker** (saved pages re-read, quotes re-checked against `pages/screen2-a/`): NRF list; Kroger 10-K and 2026 proxy; Albertsons 10-K, 2026 proxy and the Cerberus 13G/A; Publix 10-K; Ahold Delhaize brands page and Food Lion page; Aldi history page; Meijer newsroom; Wakefern; Hy-Vee; Wegmans; Amazon 10-K; Whole Foods company page. The screen's other rows were re-checked where the follow-up added a filing (Albertsons' October 10-Q and EDGAR filing index; Kroger's filing index).
- **SEC access:** 26 requests to www.sec.gov, data.sec.gov and efts.sec.gov, all HTTP 200, under the user agent `EvidenceEngine ownership-research bot (follow-up audits)`, spaced at 1.1 s or more per host (at or under 1 request per second).
- **Robots:** robots.txt was read and parsed for every host in an earlier, separate command before any page request (35 robots requests). The fetcher refuses any host without a stored robots reading and stops on a redirect to an unread host; one redirect (Jewel-Osco's about page to `http://www.jewelosco.com`) stopped there and was not followed. Rules checked for `*`, `EvidenceEngine`, ClaudeBot, Claude-User, Claude-SearchBot and anthropic-ai. albertsonscompanies.com and shopmarketbasket.com set `Crawl-delay: 10`, obeyed.
- **Blocked or failed (not retried, no other route tried):**
  - wincofoods.com: robots.txt disallows `/` for ClaudeBot. WinCo not fetched.
  - harristeeter.com, fredmeyer.com, smithsfoodanddrug.com, food4less.com, kroger.com: robots.txt request got no answer (timeout), treated as blocked. Kroger's banner store counts therefore come from no company source (see "Ranking").
  - savealot.com: robots.txt 429, blocked. winndixie.com: robots.txt redirects to an error page, treated as blocked. Both are below the cut.
  - traderjoes.com: robots.txt 403 (no restrictions); the about page returned 403 and was not retried.
  - gianteagle.com/about-us: client-rendered (no text). One Playwright load with the bot's own user agent was sent to `unsupported.html` ("Unsupported Browser"); not retried with another user agent.
  - shopmarketbasket.com: the timeline and store list load by script on click; one Playwright load each, no clicks, gave only the first timeline entry.
  - efts.sec.gov full-text search for the 2019 Smart & Final / Chedraui 8-K returned no hits.
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist, Private Equity Vet; PitchBook, CB Insights, Preqin; Progressive Grocer and Supermarket News (not needed; NRF used); Wikipedia and data-aggregator store-count pages (ScrapeHero, Grepsr), which appeared only in search results.
- **No permission refusals** from the session's permission check.
- **Leads only, never cited for ownership:** WebSearch summaries (Winn-Dixie sale in 2025; Chedraui USA's 384 US stores; Tops' ~147 stores; Harris Teeter ~260–269 and Fred Meyer ~126–132 stores; Kroger–Giant Eagle deal details; WinCo ESOP).
- **Owner kinds are research notes, not engine classifications.** "PE minority stake" follows the engine's public-company rule (a PE firm's 13D, or 13G not under Rule 13d-1(b)). "Private, owner not stated" means a primary source names the company or founders but not the owner.

## Ranking

**Source.** NRF Top 100 Retailers 2026 (2025 US retail sales, by company): "The NRF Top 100 Retailers list ranks the industry’s largest companies according to sales." — [NRF, Top 100 Retailers 2026 List](https://nrf.com/research-insights/top-retailers/top-100-retailers/top-100-retailers-2026-list)

**Which NRF companies count as grocers.** NRF gives no segment column. I took every company in the Top 100 whose stores are supermarkets (24 companies, from Kroger at #4 to Save-A-Lot at #100), the same set as the screen. Left out because NRF does not treat them as grocers and the brief keeps general merchandise and clubs out unless the ranking does: Walmart, Costco, Target, BJ's, Amazon (and with it Whole Foods Market, which NRF folds into Amazon), dollar stores, drugstores, convenience chains, and the military commissary agency. Meijer (supercenters) stays in, as in the screen.

**Multi-state filter.** Banners operating in one state are out: H-E-B and Central Market (Texas; NRF #16, $44.16B), Stater Bros (California), Kroger's Ralphs, King Soopers, Fry's, Dillons, Pick 'n Save and Mariano's (one state each per Kroger's divisions page), and Albertsons' Tom Thumb, Randalls, United, Pavilions, Star Market, Carrs and Haggen. H-E-B and Stater Bros were judged single-state from general knowledge, not from a page read.

**Banner sizing (the cross-company order).** For each banner: estimated 2025 sales = the company's NRF 2025 US sales × (banner stores ÷ company stores). Within a company this orders banners by store count, as the brief asks; across companies it puts every banner on one dollar scale. Store counts come from the company's own filing or site, except where marked "lead":

| Company (NRF rank, 2025 US sales) | Company stores used | Per-store | Banner store counts (source) |
|---|---|---|---|
| Kroger (#4, $154.74B) | 2,697 supermarkets (10-K) | $57.37M | **No company count readable** (banner sites unreachable; thekrogerco.com and the 10-K give none). Harris Teeter ~260–269 (lead), Fred Meyer ~126–132 (lead), Kroger banner, Smith's, Food 4 Less not found. A Kroger banner makes the 30 at 80 stores or more. |
| Albertsons (#10, $81.77B) | 2,244 (10-K) | $36.44M | Safeway 912 (+2 Pak N Save), Albertsons 360, Jewel-Osco 190, Vons 185, Shaw's 126 (store directories); ACME 164 (ACME about page) |
| Publix (#12, $62.75B) | 1,432 (10-K) | — | one banner (GreenWise Market, a handful of stores, not separated) |
| Ahold Delhaize USA (#13, $59.83B) | 2,017 (sum of brand pages) | $29.66M | Food Lion 1,110; Stop & Shop 362; The GIANT Company 194; Hannaford 188; Giant Food 163 (Ahold Delhaize brand pages) |
| Aldi (#14, $58.36B incl. Trader Joe's and Winn-Dixie/Harveys) | Aldi "more than 2,400" (Aldi) + Trader Joe's ~600 (lead) | $19.45M | Winn-Dixie and Harveys left out of the base (sold by Aldi in 2025 per leads); Trader Joe's stays in the 30 at any count above ~205 |
| Meijer (#21), Hy-Vee (#35), Wegmans (#38), WinCo (#47), Giant Eagle (#48), Sprouts (#53), Piggly Wiggly (#78), Market Basket (#81), Weis (#92), Ingles (#94) | — | — | one main banner each; company sales used whole |
| Wakefern (#28, $19.57B) | "more than 380" (Wakefern) | $51.50M | ShopRite count not stated; it stays in the 30 at any count above ~89 stores |
| Chedraui USA (#57, $7.73B) | 384 (lead: 254 Smart & Final, 70 El Super, 60 Fiesta) | $20.13M | Smart & Final 253 (Smart & Final site) |
| Grocery Outlet (#91, $4.69B) | 570 (10-K) | $8.23M | Grocery Outlet Bargain Market 531, United Grocery Outlet 39 (10-K) |
| Northeast Grocery (#55, $7.96B) | ~277 (lead) | — | Tops ~147 (lead) → ~$4.2B, below the cut |

**Limits.** The allocation assumes equal sales per store inside each company, which flatters small-box banners in big-box companies (Food Lion inside Ahold) and the reverse. It is a model, not reported banner sales. Kroger's four non-namesake banners are placed by leads or by the 80-store threshold, not by a company count.

**Rows 31 onward (not rows):** Ingles $4.50B; Grocery Outlet $4.37B; Tops ~$4.2B (lead); Schnucks $4.10B; Save-A-Lot $4.06B; Raley's banner (company $5.63B across Raley's, Bel Air, Nob Hill; banner split not read, likely about $3–4B); Price Rite Marketplace (Wakefern) ~$3B; QFC (Kroger, WA and OR; about 55–60 stores per general knowledge, ~$3.2B); Price Chopper/Market 32; Winn-Dixie and Harveys; El Super; City Market; Kings; Market Street; Balducci's.

| # | Banner (est. 2025 sales) | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | States | Affiliate | Ev. |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Kroger (count not read; largest Kroger banner by elimination) | The Kroger Co. | public company | none (Berkshire Hathaway 5.9% on a 13G under Rule 13d-1(b); proxy also lists BlackRock 7.5%, State Street 5.1%; no 13D) | — | KR | company-operated | multi (Kroger divisions in GA, IN, IL, OH, TN, AR, MS, KY, MI, WV, VA, AL, TX) | not checked | GR1 |
| 2 | Publix ($62.75B; 1,432) | Publix Super Markets, Inc.; stock held by employees, ESOP and 401(k) | employee-owned | none | founded 1930 | — (not traded) | company-operated | FL, GA, AL, SC, NC, TN, VA, KY | not checked | GR2 |
| 3 | Aldi (~$46.7B; 2,400+) | Aldi (Aldi Süd group); founding Albrecht family named | family (no explicit current-owner sentence) | none | 1976 in US | — | company-operated | 38 states | not checked | GR3 |
| 4 | **Safeway** ($33.23B; 912) | Albertsons Companies, Inc. ("a banner of Albertsons Companies") | **PE minority stake** (public company; Cerberus 31.0%) | **Cerberus Capital Management, L.P.** | pre-IPO holder; 13G/A 2024-02-14; proxy 2026-06-22 | ACI | company-operated | multi (Safeway directory; 10-K state table) | not checked | GR4 |
| 5 | Food Lion ($32.93B; 1,110) | Koninklijke Ahold Delhaize N.V. | public company (foreign-listed; not an SEC filer) | not checked (no 13D/13G route) | — | — (Euronext Amsterdam: AD) | company-operated | multi (10 states per general knowledge; brand page gives none) | not checked | GR5 |
| 6 | Meijer ($22.82B) | Meijer family | family | none | 1934 | — | company-operated (supercenters) | six states | not checked | GR6 |
| 7 | ShopRite (~$15B; count not stated) | Wakefern Food Corp., a cooperative of 45 member companies; stores owned by members | cooperative (name owned by the co-op; stores independently owned) | none | 1946 (co-op); ShopRite name 1951 | — | member-operated | NJ, NY, CT, PA, DE, MD (+ MA, NH, RI for the co-op) | not checked | GR7 |
| 8 | Harris Teeter (~$15B; ~260–269 lead) | The Kroger Co. (merger 2014) | public company | none | 2014 | KR | company-operated | Mid-Atlantic (Kroger history page) | not checked | GR8 |
| 9 | Hy-Vee ($14.19B) | Hy-Vee, Inc., owned by employees | employee-owned | none | 1930 | — | company-operated | nine Midwestern states | not checked | GR9 |
| 10 | Wegmans ($13.36B; 110+) | Wegman family | family | none | founded by Walter and John Wegman | — | company-operated | East Coast (multi) | not checked | GR10 |
| 11 | **Albertsons** ($13.12B; 360) | Albertsons Companies, Inc. | **PE minority stake** | **Cerberus** | as GR4 | ACI | company-operated | 16 states (directory) | not checked | GR11 |
| 12 | Trader Joe's (~$11.7B; ~600 lead) | not found (NRF folds it into Aldi's line) | not found | not found | — | — | company-operated | 42 states + DC (store locator) | not checked | GR12 |
| 13 | Stop & Shop ($10.74B; 362) | Ahold Delhaize | public company (foreign) | not checked | — | — | company-operated | multi (general knowledge) | not checked | GR13 |
| 14 | WinCo Foods ($10.65B) | not found (site disallows ClaudeBot) | not found (trade press: ESOP since 1985; not cited) | none found | — | — | company-operated | multi (trade press: 10 states; lead) | not checked | GR14 |
| 15 | Giant Eagle (≤$10.63B) | Giant Eagle, Inc., "a leading family-owned food and pharmacy retailer" (Kroger 8-K); Kroger purchase pending | family | none | — | — | company-operated | OH, PA, WV, MD, IN | not checked | GR15 |
| 16 | Sprouts Farmers Market ($8.81B; 477) | Sprouts Farmers Market, Inc. | public company | none (5%+: Vanguard 11.3%, FMR 10.5%, BlackRock 9.9%; no 13D) | — | SFM | company-operated | 24 states | not checked | GR16 |
| 17 | Smith's (count not found; in at 80+) | The Kroger Co. (Smith's Food & Drug Centers, Inc. division) | public company | none | — (Kroger since 1999 Fred Meyer merger per general knowledge) | KR | company-operated | UT, NV metro areas listed (multi) | not checked | GR17 |
| 18 | Fred Meyer (~$7.4B; ~126–132 lead) | The Kroger Co. (Fred Meyer Stores, Inc. division) | public company | none | 1999 merger (Kroger history page names Fred Meyer, Inc.) | KR | company-operated (multi-department stores) | OR, WA metro areas listed (multi) | not checked | GR18 |
| 19 | **Jewel-Osco** ($6.92B; 190) | Albertsons Companies, Inc. (banner named in the 10-K) | **PE minority stake** | **Cerberus** | as GR4 | ACI | company-operated | IL 184, IN 5, IA 1 | not checked | GR19 |
| 20 | **Vons** ($6.74B; 185) | Albertsons Companies, Inc. ("a banner of Albertsons Companies") | **PE minority stake** | **Cerberus** | as GR4 | ACI | company-operated | CA 177, NV 8 | not checked | GR20 |
| 21 | **ACME Markets** ($5.98B; 164) | Albertsons Companies (parent AB Acquisition LLC) | **PE minority stake** | **Cerberus** | as GR4 | ACI | company-operated | PA, NJ, DE, NY, CT, MD | not checked | GR21 |
| 22 | Piggly Wiggly ($5.85B; 500+) | name: Piggly Wiggly, LLC and C&S Wholesale Grocers, LLC (licensor); stores independently owned and operated | private, owner not stated (C&S: founders Cohen and Siegel; "Rooted in a Family Legacy"; no PE evidence) | none found | C&S bought Piggly Wiggly Carolina 2014 and Midwest 2021 | — | licensed name; independent operators plus some C&S stores | 18 states | not checked | GR22 |
| 23 | The GIANT Company ($5.75B; 194) | Ahold Delhaize | public company (foreign) | not checked | — | — | company-operated | multi (general knowledge) | not checked | GR23 |
| 24 | Hannaford ($5.58B; 188) | Ahold Delhaize | public company (foreign) | not checked | — | — | company-operated | multi (general knowledge) | not checked | GR24 |
| 25 | Market Basket ($5.54B) | not stated (Demoulas founders named) | private, owner not stated (no PE evidence) | none found | 1908 family history | — | company-operated | MA, NH, ME (general knowledge; store list loads by script) | not checked | GR25 |
| 26 | Smart & Final (~$5.09B; 253) | Chedraui USA ("Parent of Smart & Final, El Super, Fiesta Mart") | owner type not confirmed (top parent not read; trade press: Grupo Comercial Chedraui, BMV-listed) | none found | 2019 (trade press; not cited) | — | company-operated | CA, NV, AZ | not checked | GR26 |
| 27 | Giant Food ($4.84B; 163) | Ahold Delhaize | public company (foreign) | not checked | — | — | company-operated | multi (general knowledge) | not checked | GR27 |
| 28 | Weis Markets ($4.69B; 202) | Weis Markets, Inc.; Weis family controls about 61% of the vote | public company (family-controlled) | none (13G/A 2026: Vanguard) | 1912 | WMK | company-operated | PA, MD, NJ, NY, VA, DE, WV | not checked | GR28 |
| 29 | Food 4 Less (count not found; in at 80+) | The Kroger Co. (Food 4 Less division) | public company | none | — | KR | company-operated (price-impact warehouse) | CA, NV, IL metro areas listed | not checked | GR29 |
| 30 | **Shaw's** ($4.59B; 126) | Albertsons Companies (parent AB Acquisition LLC, from SUPERVALU 2013) | **PE minority stake** | **Cerberus** | as GR4 | ACI | company-operated | ME, MA, NH, RI, VT | not checked | GR30 |

Rows 1, 8, 17, 18 and 29 (Kroger) and 3 and 12 (Aldi line) are placed partly on leads or thresholds; each is inside the 30 on any plausible count, and none of them is PE. Food 4 Less is the least certain: if it has fewer than 80 stores, Ingles (public; the two 5%+ holders checked file under Rule 13d-1(b)) takes row 30 and Shaw's moves to row 29; the PE count does not change.

### Evidence

- **GR1 Kroger**
  - Owner and size: "As of January 31, 2026, Kroger operated, either directly or through its subsidiaries, 2,697 supermarkets" and "Kroger operates supermarkets under a variety of local banner names in 35 states and the District of Columbia." — [Kroger 10-K FY2025](https://www.sec.gov/Archives/edgar/data/56873/000110465926037723/kr-20260131x10k.htm)
  - Banner: "Division Office Addresses—Kroger" heads the Kroger-named divisions (Atlanta, Central, Cincinnati/Dayton, Columbus, Delta, Louisville, Michigan, Mid-Atlantic, Nashville, Houston, Dallas) — [Kroger, Our Divisions, accessed 2026-11-17](https://www.thekrogerco.com/contact-us/our-divisions/)
  - 5%+ holders: proxy table (screen copy) lists Berkshire Hathaway 7.0%, BlackRock 7.5%, State Street 5.1% — [Kroger DEF 14A 2026](https://www.sec.gov/Archives/edgar/data/56873/000110465926060250/tm261573d1_def14a.htm). Latest Berkshire 13G/A (event 09/30/2026): "Berkshire Hathaway Inc." at "5.9 %", box checked for Rule 13d-1(b) (HTML checkbox attribute) — [Schedule 13G/A, 2026-11-16](https://www.sec.gov/Archives/edgar/data/56873/000119312526464214/xslSCHEDULE_13G_X02/primary_doc.xml). The 2026-02-10 13G/A is "Wellington Management Group LLP" at "3.2 %", also 13d-1(b) — [Schedule 13G/A](https://www.sec.gov/Archives/edgar/data/56873/000090221926000016/xslSCHEDULE_13G_X01/primary_doc.xml). EDGAR's Kroger index shows no 13D since 2025-06.
  - Count: not found for the Kroger banner (see Ranking).
  - BDC names: "The Kroger Co.", "Kroger"
- **GR2 Publix**
  - Owner: "The Company’s common stock is not traded on an established securities market." and "common stock is provided to employees through the Employee Stock Ownership Plan (ESOP)." — [Publix 10-K FY2025](https://www.sec.gov/Archives/edgar/data/81061/000008106126000038/ck0000081061-20251227.htm)
  - Size and states: "operating 1,432 supermarkets in the southeast region of the United States as of December 27, 2025" and "in the business of operating retail food supermarkets in Florida, Georgia, Alabama, South Carolina, North Carolina, Tennessee, Virginia and Kentucky" — [same 10-K](https://www.sec.gov/Archives/edgar/data/81061/000008106126000038/ck0000081061-20251227.htm)
  - BDC names: "Publix Super Markets, Inc."
- **GR3 Aldi**
  - Owner: "In 1961, the Albrecht Family founded the world’s first discount grocery store in Germany." — [Aldi US, history, accessed 2026-11-17 (screen copy)](https://corporate.aldi.us/about-us/aldi-history)
  - Size: "we have grown to more than 2,400 stores across 38 states with more than 45,000 employees" — [same page](https://corporate.aldi.us/about-us/aldi-history)
  - Notes: no sentence names today's owner, so "family" rests on the founder statement (as in the screen). NRF's line: "Includes Trader Joe’s and Aldi Sued and the acquisition of Winn-Dixie and Harveys." — [NRF](https://nrf.com/research-insights/top-retailers/top-100-retailers/top-100-retailers-2026-list)
  - BDC names: "ALDI Inc.", "Aldi"
- **GR4 Safeway**
  - Banner owner: "Today, Safeway operates as a banner of Albertsons Companies" — [Safeway, About Us, accessed 2026-11-17](https://www.safeway.com/about-us.html)
  - Banner list: "We operate 22 well known banners including Albertsons, Safeway, Vons, Pavilions, Randalls, Tom Thumb, Carrs, Jewel-Osco, ACME, Shaw's, Star Market, United Supermarkets, Market Street, Haggen, Kings Food Markets and Balducci's Food Lovers Market" — [Albertsons 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1646972/000164697226000032/aci-20260228.htm); unchanged in the 10-Q: "with 2,240 stores across 35 states and the District of Columbia as of September 12, 2026." — [Albertsons 10-Q, 2026-10-20](https://www.sec.gov/Archives/edgar/data/1646972/000164697226000065/aci-20260912.htm)
  - Company stores: "As of February 28, 2026, we operated 2,244 stores located in 35 states and the District of Columbia" — [Albertsons 10-K](https://www.sec.gov/Archives/edgar/data/1646972/000164697226000032/aci-20260228.htm)
  - Count: "914 Safeway Locations in" — [Safeway store directory, accessed 2026-11-18](https://local.safeway.com/index.html); the directory's links carry `data-count="(912)"` for Safeway and `(2)` for Pak N Save (HTML attributes).
  - **PE stake (Cerberus):**
    - 13G/A box: "☒ Rule 13d-1(d)" and "Reporting Person may be deemed to beneficially own 151,818,680 shares of Common Stock, or 26.4% of the shares of Common Stock" — [Cerberus Schedule 13G/A, 2024-02-14](https://www.sec.gov/Archives/edgar/data/1646972/000149315224006609/formsc13ga.htm)
    - Proxy: "Cerberus Capital Management, L.P. (“Cerberus”), our largest stockholder, has the right to designate up to four directors for election to our Board." Beneficial ownership table: "Cerberus Capital Management, L.P.(1)" … "31.0%" — [Albertsons DEF 14A, 2026-06-22](https://www.sec.gov/Archives/edgar/data/1646972/000114036126025819/ny20070872x2_def14a.htm)
    - Re-confirmation: EDGAR's Albertsons filing index (fetched 2026-11-17) lists no Cerberus 13G/A after 2024-02-14; the 13G filings since then are BlackRock ("BlackRock, Inc.", 13d-1(b)) — [Schedule 13G, 2025-04-24](https://www.sec.gov/Archives/edgar/data/1646972/000205211325001570/xslSCHEDULE_13G_X01/primary_doc.xml), Vanguard, and FMR ("FMR LLC" at "4.5 %", 13d-1(b)) — [Schedule 13G/A, 2025-11-05](https://www.sec.gov/Archives/edgar/data/1646972/000031506625002682/xslSCHEDULE_13G_X01/primary_doc.xml). The October 2026 10-Q does not mention Cerberus.
    - Form ADV: Cerberus Capital Management, L.P., CRD 152175, `Any PE Funds = Y`, 9 PE funds.
  - Since: Cerberus held its stake before the June 2020 IPO; the 2024-02-14 filing amends an earlier 13G (original not opened). Newest confirming source: the 2026-06-22 proxy.
  - BDC names: "Albertsons Companies, Inc.", "Safeway Inc.", "Albertsons Safeway LLC", "New Albertsons L.P."
- **GR5 Food Lion**
  - Owner: "Ahold Delhaize is a family of great local brands serving millions of customers each week in the United States, Europe and Indonesia." — [Ahold Delhaize, brands, accessed 2026-11-17 (screen copy)](https://aholddelhaize.com/brands/); footer "Copyright statement: © 2001-2025 Koninklijke Ahold Delhaize N.V. and its Affiliates" — [Food Lion brand page](https://aholddelhaize.com/brands/food-lion/)
  - Count: field text "1110" "stores" — [same Food Lion page](https://aholddelhaize.com/brands/food-lion/)
  - Notes: Euronext listing not quoted (general knowledge). Ahold Delhaize is not an SEC registrant, so the engine's 13D/13G route doesn't apply; its Dutch substantial-holdings register was not read.
  - BDC names: "Food Lion, LLC", "Ahold Delhaize USA"
- **GR6 Meijer**
  - Owner: "Meijer is a privately-owned and family-operated company that began in 1934 during the Great Depression" — [Meijer newsroom, Who We Are (screen copy)](https://newsroom.meijer.com/who-we-are)
  - States: "Meijer employs 70,000 team members in six states" — [same page](https://newsroom.meijer.com/who-we-are)
  - BDC names: "Meijer, Inc."
- **GR7 ShopRite**
  - Owner: "Today, Wakefern is the largest retailer-owned cooperative in the United States, comprising 45 member companies who independently own and operate more than 380 retail supermarkets under the ShopRite, Price Rite Marketplace, The Fresh Grocer, Dearborn Market, Gourmet Garage, Fairway Market, Di Bruno Bros. and Morton Williams banners in New Jersey, New York, Connecticut, Pennsylvania, Delaware, Maryland, Massachusetts, New Hampshire, and Rhode Island markets." — [Wakefern, Who We Are (screen copy)](https://www2.wakefern.com/who-we-are/)
  - Count: ShopRite's own count not stated; sized at Wakefern's per-store average (see Ranking).
  - BDC names: "Wakefern Food Corp.", "ShopRite"
- **GR8 Harris Teeter**
  - Owner: "In 2001, we merged with Baker’s, followed by mergers with Harris Teeter in 2014 and Roundy’s, Pick ‘N Save, Metro Markets and Mariano’s in 2015. This expanded our reach through the Mid-Atlantic states and the northern Midwest." — [Kroger, Our History, accessed 2026-11-18](https://www.thekrogerco.com/about/history/)
  - Count: ~260–269 (search leads only; harristeeter.com unreachable).
  - BDC names: "Harris Teeter Supermarkets, Inc.", "Harris Teeter, LLC"
- **GR9 Hy-Vee**
  - Owner: "Hy-Vee is employee-owned by direct stockholders" — [Hy-Vee, Our Company (screen copy)](https://www.hy-vee.com/corporate/our-company/)
  - States: "Hy-Vee operates more than 540 business units across nine Midwestern states." — [same page](https://www.hy-vee.com/corporate/our-company/)
  - BDC names: "Hy-Vee, Inc."
- **GR10 Wegmans**
  - Owner: "Wegmans is a values-based family company that was founded by brothers Walter and John Wegman in Rochester, New York." (raw HTML, page data) — [Wegmans, About Us (screen copy)](https://www.wegmans.com/about-us)
  - Size: "More than 110 stores in the East Coast Region" (raw HTML, page data) — [same page](https://www.wegmans.com/about-us)
  - BDC names: "Wegmans Food Markets, Inc."
- **GR11 Albertsons (banner)**
  - Banner owner: "Today, Albertsons operates as a banner of Albertsons Companies" — [Albertsons, About Us, accessed 2026-11-17](https://www.albertsons.com/about-us.html)
  - Count: "360 Albertsons Locations in" — [Albertsons store directory, accessed 2026-11-18](https://local.albertsons.com/index.html); state links (HTML attributes) cover AZ, AR, CA, CO, ID, LA, MT, NV, NM, ND, OK, OR, TX, UT, WA, WY.
  - PE stake: as GR4.
- **GR12 Trader Joe's**
  - Owner: not found. The about page (https://www.traderjoes.com/home/about-us) returned 403. The only source read is NRF's note: "Includes Trader Joe’s and Aldi Sued and the acquisition of Winn-Dixie and Harveys." — [NRF](https://nrf.com/research-insights/top-retailers/top-100-retailers/top-100-retailers-2026-list)
  - States: the store locator's state list names 42 states and the District of Columbia ("Locations By State") — [Trader Joe's Locations, accessed 2026-11-17](https://locations.traderjoes.com/)
  - Notes: widely reported as owned by an Albrecht family trust (Aldi Nord side); not cited. NRF folding it into "Aldi" is a ranking choice, not an ownership source.
  - BDC names: "Trader Joe's Company"
- **GR13 Stop & Shop**
  - Owner: as GR5 (Ahold Delhaize brands page). Count: field text "362" "stores" — [Ahold Delhaize, Stop & Shop, accessed 2026-11-17](https://aholddelhaize.com/brands/stop-shop/)
  - BDC names: "The Stop & Shop Supermarket Company LLC"
- **GR14 WinCo Foods**
  - Owner: not found. wincofoods.com's robots.txt disallows `/` for ClaudeBot; nothing was fetched there, and no other route was tried. No WinCo release on PR Newswire or Business Wire turned up in search.
  - Notes: trade press (not cited) calls it employee-owned through an ESOP since 1985. If confirmed it is non-PE (employee-owned).
  - BDC names: "WinCo Holdings, Inc.", "WinCo Foods, LLC"
- **GR15 Giant Eagle**
  - Owner: "Giant Eagle, headquartered in Pennsylvania, is a leading family-owned food and pharmacy retailer. Giant Eagle operates stores in Ohio, Pennsylvania, West Virginia, Maryland and Indiana." — [Kroger 8-K, 2026-07-01](https://www.sec.gov/Archives/edgar/data/56873/000110465926079552/tm2619434d1_8k.htm)
  - Pending: "The acquisition is expected to close in 2027" — [same 8-K](https://www.sec.gov/Archives/edgar/data/56873/000110465926079552/tm2619434d1_8k.htm). A pending deal doesn't count; on closing the row becomes Kroger (public, non-PE).
  - Notes: gianteagle.com/about-us is client-rendered and redirected the bot's browser to an "Unsupported Browser" page. NRF's $10.63B includes Market District and GetGo for part of 2025 (GetGo sold to Couche-Tard mid-2025 per leads).
  - BDC names: "Giant Eagle, Inc."
- **GR16 Sprouts Farmers Market**
  - Size: "Headquartered in Phoenix with 477 stores in 24 states as of December 28, 2025" — [Sprouts DEF 14A, 2026-04-07](https://www.sec.gov/Archives/edgar/data/1575515/000157551526000013/sfm-20260407.htm)
  - Holders: table lists "The Vanguard Group(13)" 11.3%, "FMR LLC (14)" 10.5%, "BlackRock, Inc. (15)" 9.9% — [same proxy](https://www.sec.gov/Archives/edgar/data/1575515/000157551526000013/sfm-20260407.htm). EDGAR's Sprouts index since 2024-11 shows only 13G/13G/A filings (FMR, BlackRock, Vanguard entities); no 13D.
  - BDC names: "Sprouts Farmers Market, Inc."
- **GR17 Smith's**
  - Owner: the Kroger divisions page lists "Smith’s Food & Drug Centers, Inc." with metro areas "Salt Lake City, UT" and "Las Vegas, NV" — [Kroger, Our Divisions](https://www.thekrogerco.com/contact-us/our-divisions/)
  - Count: not found (smithsfoodanddrug.com unreachable).
  - BDC names: "Smith's Food & Drug Centers, Inc."
- **GR18 Fred Meyer**
  - Owner: the divisions page lists "Fred Meyer Stores, Inc." with "Portland, OR" and "Seattle, WA" — [Kroger, Our Divisions](https://www.thekrogerco.com/contact-us/our-divisions/)
  - Count: ~126–132 (search leads only).
  - BDC names: "Fred Meyer Stores, Inc."
- **GR19 Jewel-Osco**
  - Owner: named in Albertsons' banner list (GR4 quote).
  - Count: "190 Jewel-Osco Locations in" — [Jewel-Osco store directory, accessed 2026-11-18](https://local.jewelosco.com/index.html); state links (HTML attributes): Illinois (184), Indiana (5), Iowa (1).
  - PE stake: as GR4.
  - BDC names: "Jewel-Osco", "Jewel Food Stores, Inc."
- **GR20 Vons**
  - Owner: "Today, Vons operates as a banner of Albertsons Companies" — [Vons, About Us, accessed 2026-11-17](https://www.vons.com/about-us.html)
  - Count: "185 Vons Locations in" — [Vons store directory, accessed 2026-11-18](https://local.vons.com/index.html); California (177), Nevada (8) (HTML attributes).
  - PE stake: as GR4.
  - BDC names: "Vons Companies", "Vons"
- **GR21 ACME Markets**
  - Owner: "In 1999, parent company AB Acquisition LLC acquired American Stores, the company under which ACME Markets had operated since 1917" — [ACME Markets, About Us, accessed 2026-11-17](https://www.acmemarkets.com/about-us.html)
  - Count and states: "ACME Markets has grown and expanded to operate 164 stores throughout its native Pennsylvania, as well as serving shoppers in nearby New Jersey, Delaware, New York, Connecticut, and Maryland." — [same page](https://www.acmemarkets.com/about-us.html)
  - PE stake: as GR4.
  - BDC names: "Acme Markets, Inc."
- **GR22 Piggly Wiggly**
  - Owner of the name: "Today there are more than 500 Piggly Wiggly® stores serving communities in 18 states. Piggly Wiggly® Stores are independently owned and operated under license of Piggly Wiggly®, LLC and C&S Wholesale Grocers, LLC" — [Piggly Wiggly, home page, accessed 2026-11-17](https://www.pigglywiggly.com/)
  - C&S: "Rooted in a Family Legacy" and "Lester's son Rick, current Executive Chairman, joins C&S." — [C&S, Our Story, accessed 2026-11-18](https://www.cswg.com/about/our-story/). C&S raises Rule 144A debt ("For existing investors or prospective investors who are qualified institutional buyers under Rule 144A under the Securities Act, a protected site has been established") — [C&S, Investor Relations](https://www.cswg.com/news-media/investor-relations/); no equity holder is named.
  - Notes: NRF's line "Piggly Wiggly" carries C&S's Keene, NH headquarters. Stores are independently owned; the brand row belongs to the licensor. C&S is also the proposed majority owner of Winn-Dixie: "C&S Wholesale Grocers, LLC (C&S) has announced a proposed transaction to be the majority owner of The Winn-Dixie Company (Winn-Dixie)." — [C&S home page](https://www.cswg.com/)
  - BDC names: "C&S Wholesale Grocers, LLC", "Piggly Wiggly, LLC", "Piggly Wiggly Alliance"
- **GR23 The GIANT Company**
  - Owner: as GR5. Count: field text "194" "stores" — [Ahold Delhaize, The GIANT Company](https://aholddelhaize.com/brands/the-giant-company/)
  - BDC names: "The GIANT Company", "Giant Food Stores, LLC"
- **GR24 Hannaford**
  - Owner: as GR5. Count: field text "188" "stores" — [Ahold Delhaize, Hannaford](https://aholddelhaize.com/brands/hannaford/)
  - BDC names: "Hannaford Bros. Co., LLC"
- **GR25 Market Basket**
  - Owner: not stated. Founders: "Athanasios and Efrosini Demoulas immigrate from Kalambaka, Greece and settle in Lowell, Massachusetts." — [Market Basket, Company History & Timeline (Playwright render, no clicks), accessed 2026-11-18](https://www.shopmarketbasket.com/timeline/)
  - Notes: the about page has no text; later timeline entries load on click and were not read. NRF lists the company as "My Demoulas". Trade press (not cited): owned by the Arthur T. Demoulas branch of the family since 2014.
  - BDC names: "Demoulas Super Markets, Inc.", "DeMoulas Market Basket"
- **GR26 Smart & Final**
  - Parent: "Parent of Smart & Final, El Super, Fiesta Mart plots growth, remodels, new DC" (headline about "Chedraui USA") — [Smart & Final, Newsroom, accessed 2026-11-18](https://www.smartandfinal.com/sm/pickup/rsid/522/newsroom)
  - Count and states: "Today, Smart & Final operates 253 stores across California, Nevada and Arizona, with more than 11,000 employees." — [Smart & Final, About Us](https://www.smartandfinal.com/sm/pickup/rsid/522/about-us)
  - Notes: Chedraui USA's own parent (Grupo Comercial Chedraui, Mexican-listed and family-controlled per trade press) was not confirmed. Apollo owned Smart & Final before 2019 (general knowledge); no PE holder found today.
  - BDC names: "Smart & Final Stores LLC", "Chedraui USA, Inc."
- **GR27 Giant Food**
  - Owner: as GR5. Count: field text "163" "stores" — [Ahold Delhaize, Giant Food](https://aholddelhaize.com/brands/giant-food/)
  - BDC names: "Giant of Maryland LLC"
- **GR28 Weis Markets**
  - Owner: "The Weis family, consisting of Jonathan H. Weis, Chairman, President and Chief Executive Officer" … "control approximately 61% of the voting power of the Company." — [Weis DEF 14A 2026](https://www.sec.gov/Archives/edgar/data/105418/000010541826000025/wmk-20260430xdef14a.htm)
  - Count and states: "for a total of 202 retail food stores operating under the Weis Markets trade name" and "located in Pennsylvania and six surrounding states: Delaware, Maryland, New Jersey, New York, Virginia, and West Virginia." — [Weis 10-K FY2025](https://www.sec.gov/Archives/edgar/data/105418/000010541826000024/wmk-20251227x10k.htm)
  - Holders: EDGAR's Weis index since 2024-09 shows family 13D/As (2025-06) and Vanguard's 13G/A (2026-03); no PE filer.
  - BDC names: "Weis Markets, Inc."
- **GR29 Food 4 Less**
  - Owner: the divisions page lists "Food 4 Less" with "Los Angeles, CA", "Las Vegas, NV" and "Chicago, IL" — [Kroger, Our Divisions](https://www.thekrogerco.com/contact-us/our-divisions/)
  - Count: not found (food4less.com unreachable). The division also runs Foods Co (Northern California), a separate banner.
  - BDC names: "Food 4 Less Holdings, Inc."
- **GR30 Shaw's**
  - Owner: "In 2013, our parent company, AB Acquisition LLC, acquired Shaw’s from SUPERVALU, a transaction bringing all Albertsons stores under singular ownership again." — [Shaw's, About Us, accessed 2026-11-17](https://www.shaws.com/about-us.html)
  - Count: "126 Shaw's Locations in" — [Shaw's store directory, accessed 2026-11-18](https://local.shaws.com/index.html); Maine (19), Massachusetts (55), New Hampshire (25), Rhode Island (8), Vermont (19) (HTML attributes). The about page's "Shaw’s operates 150 stores throughout New England" — [Shaw's, About Us](https://www.shaws.com/about-us.html) — names Star Market as a sister company in the same paragraph and likely counts both; the directory figure (126) is used.
  - PE stake: as GR4.
  - BDC names: "Shaw's Supermarkets, Inc."

### Category share

- **PE minority stake: 6 / 30 = 20.0%** (Safeway, Albertsons, Jewel-Osco, Vons, ACME, Shaw's; all Cerberus via Albertsons Companies).
- **PE-owned (control): 0.** PE-owned plus minority = **6 / 30 = 20.0%.**
- **Public company (no PE holder): 12 / 30**: Kroger's 5 (Kroger, Harris Teeter, Smith's, Fred Meyer, Food 4 Less), Ahold Delhaize's 5 (Food Lion, Stop & Shop, The GIANT Company, Hannaford, Giant Food; foreign, holders not read), Sprouts, Weis (family-controlled, 61% of the vote).
- **Family: 4** (Aldi, Meijer, Wegmans, Giant Eagle). **Employee-owned: 2** (Publix, Hy-Vee). **Cooperative: 1** (ShopRite).
- **Private, owner not stated: 2** (Piggly Wiggly / C&S; Market Basket). **Owner type not confirmed: 1** (Smart & Final / Chedraui USA).
- **Not found: 2 / 30 = 6.7%** (Trader Joe's, WinCo). Neither has any PE lead: both are reported as family-trust and employee-owned.
- **By parent company:** 16 parents for 30 rows (Kroger 5, Ahold Delhaize 5, Albertsons 6, the rest 1 each). PE parents: 1 / 16 = 6.3% (Albertsons Companies).
- **By estimated sales:** the six Albertsons rows hold about $70.6B of the 30 rows' estimated ~$470B (about 15%; the total includes leads for Kroger's and Wakefern's banners, so treat it as rough).
- **Sensitivities (by banner row):**
  - Whole Foods Market added (Amazon's 2025 physical-stores net sales were $22.56B, mostly Whole Foods; ~#6): Shaw's falls to #31 → **5 / 30 = 16.7%**.
  - H-E-B counted although single-state ($44.16B, family): same effect → **5 / 30**. Both added → Weis and Shaw's out → **5 / 30**.
  - Food 4 Less under 80 stores: Ingles replaces it, Shaw's stays → **6 / 30**.
  - Screen method (one lead banner per company, 11 rows): 1 / 11 (9.1%); two lead banners per multi-banner grocer: 2 / 14 (14.3%).
  - Walmart's grocery formats (Walmart Neighborhood Market) would also enter if a grocer ranking were used instead of NRF; Walmart is public and Walton-controlled, non-PE, and would push out another row near the bottom (Weis or Shaw's).
- **Sources disagree:** none on owners. Framing note: Shaw's about page says 150 stores, its directory 126 (Star Market likely in the first).

## Firms named

Every investment firm named as an owner or 5%+ holder of a row's parent, as the sources name it:
- **Cerberus Capital Management, L.P.** (Albertsons, 31.0%; 13G under Rule 13d-1(d)). The proxy names Cerberus designees Frank Bruno ("CEO and Chief Investment Officer of Cerberus Capital Management, L.P.") and Mr. Wille ("leads the firm’s Retail, Consumer, and Industrial private equity strategies") — [Albertsons DEF 14A, 2026-06-22](https://www.sec.gov/Archives/edgar/data/1646972/000114036126025819/ny20070872x2_def14a.htm).
- Passive holders of public parents (13G under Rule 13d-1(b), not PE stakes under the engine's rules): Kroger: Berkshire Hathaway Inc. (with Warren E. Buffett, National Indemnity Company; public holding company), BlackRock, Inc., State Street, Vanguard, Wellington Management Group LLP (3.2%, below 5%). Albertsons: BlackRock, Inc., Vanguard, FMR LLC (4.5%). Sprouts: The Vanguard Group, FMR LLC, BlackRock, Inc. Weis: Vanguard. 
- Below the cut, for the assembler: Grocery Outlet (T. Rowe Price Investment Management 19.0%, BlackRock 14.4%, FMR 5.1%, all 13d-1(b); **Pertento Partners LLP / Pertento Advisors LLC 6.2% on a 13G under Rule 13d-1(c)**; J. Goldman & Co LP 3.5%, 13d-1(b)); Ingles (Brandes Investment Partners 9.1%, American Century 5.3%, both 13d-1(b)).
- Leads only, not counted: Kingswood Capital (Save Mart, Lucky California, FoodMaxx; screen lead), Apollo (The Fresh Market; Heritage Grocers Group, formerly Cardenas and Tony's), Onex (Save-A-Lot, older reports), Stripes (Erewhon, minority), the 2025 Winn-Dixie buyer consortium (Anthony Hucker and C&S), Great Elm Capital Corp. (lender to Northeast Grocery), Silver Point (lender to Southeastern Grocers).

## Form ADV results (November 2026 rosters, registered and exempt)

| Firm (role) | Adviser entity | CRD | Roster | Any PE Funds | PE funds |
|---|---|---|---|---|---|
| Cerberus (Albertsons 13G, 13d-1(d)) | Cerberus Capital Management, L.P. | 152175 | RIA | **Y** | 9 |
| Pertento (Grocery Outlet 13G, 13d-1(c); row 32, not in the 30) | Pertento Advisors LLC | 335545 | RIA | N | — |
| Pertento | Pertento Partners LLP | 317498 | ERA | N | — |
| J. Goldman (Grocery Outlet 13G/A, 13d-1(b), 3.5%) | J. Goldman & Co., L.P. | 157465 | RIA | N | — |
| Kingswood (Save Mart lead) | Kingswood Capital Management, L.P. | 304649 | RIA | Y | 15 |
| Onex (Save-A-Lot lead) | Onex Partners Manager LP | 160923 | RIA | Y | 35 |
| Apollo (Heritage Grocers, The Fresh Market leads) | Apollo Capital Management, L.P. | 143161 | RIA | Y | 214 |

Pertento reports no PE funds on either registration and does not describe itself as a PE firm in anything read, so Grocery Outlet would stay non-PE even inside the 30. Index and asset managers filing under 13d-1(b) were not looked up (their filings are passive whatever their ADV says).

## BDC names (overlap check)

- Searched the SEC BDC data sets for July, August, September and October 2026 (`soi.tsv`, identifier and affiliation fields) for every banner and parent in the 30 plus 40 more grocery names. **No hit for any of the 30 rows or their parents.**
- Hits below the cut: "Northeast Grocery Inc" (Great Elm Capital Corp., 1st lien secured loan, acquired 08/08/2024); "Southeastern Grocers LLC" (Silver Point Private Credit Fund and Silver Point Specialty Lending Fund, 1st lien term loan); "Heritage Grocers Group, LLC (F/K/A Tony's Fresh Market / Cardenas Markets)" (OFS Capital, debt and equity; Hancock Park Corporate Income; Fidelity Private Credit Fund via "Cardenas Merger Sub LLC").
- False positives discarded: "Charps, LLC" (a pipeline contractor, matched "Harps"), "SingleStore" (matched "Ingles"), jewelry companies (matched "Jewel").
- BDC names per row are listed in each Evidence entry for the assembler's own match.

## Rows resting on documents older than 18 months

- **None among the PE rows.** The Cerberus 13G/A is dated 2024-02-14 (older than 18 months), but the Albertsons proxy of 2026-06-22 restates Cerberus as a 31.0% holder, so the newest confirming source is five months old.
- Non-PE rows older than 18 months: none used as the newest source (all from 2025–2026 filings or pages read this month).

## Surprises

- **Kroger is buying Giant Eagle** (8-K, 2026-07-01; closing expected 2027). Not counted while pending; on closing, Giant Eagle becomes a sixth Kroger row (non-PE).
- **Aldi sold Winn-Dixie and Harveys in 2025** (leads) and C&S Wholesale Grocers now proposes to become Winn-Dixie's majority owner (C&S home page). NRF's 2025 Aldi line still includes them.
- **Albertsons' own banner directories are the cleanest store-count source** in the industry (exact counts by state, server-rendered). Kroger's banner sites, by contrast, don't answer a bot at all.
- **Cerberus has not amended its 13G since February 2024** while its stake rose from 26.4% to 31.0% through Albertsons' buybacks (26.0 million shares repurchased in the first 28 weeks of fiscal 2026 per the 10-Q).
- **Grocery Outlet's largest non-index new holder is a 13d-1(c) filer** (Pertento, 6.2%), the only non-(b) 13G found on any public parent read; its ADV says N.
- WinCo, the 14th-largest banner, cannot be read at all: its robots.txt shuts out ClaudeBot.

## Open questions for the developer (numbers only; nothing decided)

1. **Whole Foods and other grocery banners of non-grocer companies.** Base (left out, as NRF folds them into Amazon or Walmart): 6 / 30 (20.0%). With Whole Foods: 5 / 30 (16.7%). With Whole Foods and Walmart Neighborhood Market: 5 / 30.
2. **Single-state banners.** Base (out): 6 / 30. Counting H-E-B ($44.16B), Ralphs, King Soopers and Fry's (Kroger, all non-PE) would push Weis, Food 4 Less, Giant Food and Shaw's out: 5 / 30 (16.7%).
3. **Kroger's banner counts** could not be read from any Kroger source. Rows 8, 17, 18 and 29 rest on leads or an 80-store threshold. No outcome above changes the PE count by more than one row (Shaw's).
4. **Sizing rule.** Store-weighted allocation of NRF company sales (base) vs. ranking by store count alone: by store count, Aldi (2,400+), Food Lion (1,110), Safeway (912), Piggly Wiggly (500+) and Grocery Outlet (531) rise and Wegmans (110+) and Market Basket fall; not computed in full.

## Worker log (cost)

- **Time:** first request 2026-11-17T23:58Z (SEC robots.txt); last fetch 2026-11-18T00:18Z; write-up and quote check after.
- **Requests:**
  - Page requests: 66 logged in `pages/fu-grocery/index.tsv` (63 curl, 3 Playwright; 1 more line records a redirect the fetcher refused to follow; page number 037 is unused, a Playwright launch that failed before any request).
  - robots.txt requests: 35, each in its own robots-only command before the first page request to that host.
  - SEC: 26 requests (www.sec.gov 19, data.sec.gov 6, efts.sec.gov 1), all 200, ≤1 per second.
  - WebSearch: 16 (leads only).
  - Reused saved pages from the screen worker: 17 (no refetch).
  - Status mix (non-SEC page requests, 40): 30 × 200 by curl; 6 × 301 (5 followed after a robots check on the target, 1 to http://www.jewelosco.com refused by the fetcher); 1 × 403 (Trader Joe's about page); 3 Playwright loads with no clicks (Giant Eagle sent to an "Unsupported Browser" page; Market Basket's timeline and store list rendered without the needed text).
  - Agent tokens: not metered by this worker; roughly 250–300k.
- **Files:** pages under the session scratchpad `pages/fu-grocery/` (NNN.html, NNN.txt, `index.tsv`, `robots-log.tsv`, `robots/`); scripts under `scripts/fu-grocery/` (`robots.py`, `fetch.py`, `pw.py`, `g13.py`, `adv.py`, `bdc.py`, `check_quotes.py`).

## Quote check

- **Script** (`scripts/fu-grocery/check_quotes.py`): for every report line that cites a URL, each double-quoted string (split at "…") is matched against the saved text of the cited page(s), then against its raw HTML (tags stripped, entities decoded). Both sides are normalized the same way: NFKC, curly quotes and dashes to plain, non-breaking and zero-width characters removed, whitespace collapsed, spaces before punctuation dropped. Matching is case-sensitive. Pages are looked up by requested or final URL in both `pages/fu-grocery/index.tsv` and `pages/screen2-a/index.tsv` (HTTP 200 rows only).
- **Result: 94 of 94 quoted segments found; 94 of 94 altered copies (one middle character changed) failed.**
- **Checked by hand** (quotes on lines without a URL): the table-cell quotes ("a banner of Albertsons Companies", "a leading family-owned food and pharmacy retailer", "Rooted in a Family Legacy", "Parent of Smart & Final, El Super, Fiesta Mart", "more than 2,400", "more than 380") are substrings of checked Evidence quotes and were found in pages fu-grocery 015/017, 043, 055, 063 and screen2-a 075, 077; "Unsupported Browser" is the title in fu-grocery 038 (HTML); "My Demoulas" is in screen2-a 002; the BDC strings ("Northeast Grocery Inc", "Southeastern Grocers LLC", "Heritage Grocers Group, LLC (F/K/A Tony's Fresh Market / Cardenas Markets)", "Cardenas Merger Sub LLC", "Charps, LLC") were found in the August or October 2026 `soi.tsv`.
- **Not quotes, read from structure:** store counts by state on the Albertsons directories (`data-count` attributes), Ahold Delhaize brand-page store counts (field text "1110" / "stores"), the 13G rule boxes (`alt="Checkbox checked"` images in the SEC renderings; the 2024 Cerberus filing uses a "☒" character), proxy percentages (table cells), NRF sales figures (table fields), and the Trader Joe's state count (42 states plus DC, counted from the locator's state list).
- **Tag-boundary note:** Wegmans' two quotes sit in the page's embedded data, so they match the raw HTML, not the visible text (as in the screen).
