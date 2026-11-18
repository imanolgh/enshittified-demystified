# Follow-up audit: thrift and resale stores (every multi-state brand)

Ticket: [93 Research: Follow-up audits of four industries](../../issues/93-research-follow-up-audits-four-industries.md), item 3 · Worker report, 2026-11-17 (fetches logged 2026-11-17 23:56 to 2026-11-18 00:09 UTC) · Builds on the [industry screen 2 thrift section](../industry-screen-2/a-grocery-thrift-crafts.md). Every reused row and quote was re-checked against that worker's saved pages, which were fetched earlier the same day.

## Short answer

| | Thrift and resale (N = 23 multi-state brand rows) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **5 / 23 (21.7%)**. All five are PE-owned, none minority: Savers, Value Village, 2nd Ave and Unique (Savers Value Village, Inc., Ares funds 61.5%) and America's Thrift Stores (TZP Group). |
| Donation-based thrift only (11 rows) | **5 / 11 (45.5%)** |
| Buy-sell and consignment resale only (12 rows) | **0 / 12 (0%)** |
| Owner not found | **3 / 23 (13.0%)**: Clothes Mentor, Crossroads and Fashionphile. Each names its company but not who owns it. Also, St. Vincent de Paul's name holder (the national council) could not be read because its site blocks this bot. The local councils that run the stores were read. |
| Brands found | 23 multi-state brands confirmed or inferred (2 of them, Style Encore and Music Go Round, are inferred; see the rows). Another **11 candidates could not be confirmed** as multi-state, or their pages were blocked (see "Couldn't confirm"). **4 checked and excluded** as single-state. |

- **The result depends on counting Savers' banners as separate rows.** The brief says rows are store names consumers see. Savers Value Village runs four US banners, and each operates in at least two states (Savers in many; Value Village in WA and MD; 2nd Ave in MD, NJ and VA; Unique in MD and VA). Counted as one row, the share is **2 / 20 (10.0%)**, exactly on the bar.
- Other sensitivities:
  - Without the two Winmark brands whose multi-state presence is inferred: 5 / 21 (23.8%).
  - Without luxury resale (Fashionphile, The RealReal): 5 / 21 (23.8%).
  - If all 11 unconfirmed candidates turned out multi-state and non-PE: 5 / 34 (14.7%), or 2 / 31 (6.5%) with Savers as one row.
- **Fewer than 30 national brands exist**, so this is the count of every national brand that "Launch industries" asks for under 20%.
- **Biggest finding:** in this industry, PE sits only in for-profit donation-based thrift. The two largest for-profit thrift chains are PE-owned (Ares, TZP). No buy-sell or consignment franchise or chain shows PE. The largest of them, Winmark's five brands, belong to a public company with only passive 13G holders, and the next largest (BaseCamp, NTY, Buffalo Exchange, Crossroads) are founder-, family- or individual-held.

## How this was sourced (read first)

- **List (blind to ownership):**
  - the screen's 13 rows;
  - InvestigateWest, "There's big business in thrift" (2020-10-30), a survey of "at least 20 regional or national branded chains" of for-profit thrift. It was used for leads only and is cited for no ownership fact;
  - three WebSearch result pages on thrift chains and resale franchises (directories and trade press; leads only);
  - the brands' own locators and franchise pages;
  - Winmark's and Savers Value Village's 10-Ks.
  - No association member list was usable. NARTS was not reached, and the national St. Vincent de Paul site is blocked.
- **Scope:** stores whose main business is selling secondhand goods, either donated (thrift) or bought or consigned from the public (resale), operating in two or more US states.
  - Rows are store names consumers see, so a company's banners are separate rows (Savers Value Village gives 4).
  - Winmark's five resale franchises are all in, including Play It Again Sports (sporting goods) and Music Go Round (instruments), because Winmark calls them all resale brands.
  - Out of scope, not checked: used-book and media chains (Half Price Books, 2nd & Charles, Vintage Stock), pawn shops, online-only resale (ThredUp, Poshmark), and pop-up consignment events (Just Between Friends, Rhea Lana's), which are not stores.
- **Order:** by each brand's own US store count where one was found. Winmark states counts for the US and Canada combined, and they are shown as given. Goodwill's and Habitat's counts were not stated on the pages read, so they are placed by trade-press figures (flagged). Rows with no count come last.
- **How each row is run:**
  - Goodwill, Habitat ReStore and St. Vincent de Paul: networks of independent local nonprofits under one name (one row each).
  - Winmark's, BaseCamp's and NTY's brands: 100% franchised. The owner is the franchisor, never the franchisees.
- **Ownership facts** come from SEC filings (10-K, DEF 14A, Schedules 13G and 13D), a sponsor press release and portfolio page (TZP), and company about pages, footers and franchise pages. Trade press supplied leads and counts only, flagged where used.
- **SEC access:** 11 requests (2 robots.txt, 9 documents) to www.sec.gov and data.sec.gov, all with `EvidenceEngine ownership-research bot (follow-up audits)`, spaced at least 1.1 s apart. All returned 200. The screen worker's Savers Value Village and Winmark filings (fetched earlier today) were reused from its cache.
- **Robots:**
  - Every host's robots.txt was read and parsed by a separate command before the first page request (`robots.py`, then `fetch.py`, which refuses any host not yet read and never follows a redirect).
  - On a redirect, the new host's robots.txt was read in a separate command before anything was fetched there: texasthrift.com, clothesmentor.com, buffaloexchange.com, valueworld.com, bcfranchise.com, ragstock.com, familythriftcenter.com, musicgoround.com, style-encore.com and svdpgeorgia.org.
  - Crawl-delays were obeyed: 10 s at crossroadstrading.com, kidtokid.com, uptowncheapskate.com, bcfranchise.com, outofthecloset.org, voaohin.org and svdpgeorgia.org, and 10 s for ClaudeBot at musicgoround.com and style-encore.com.
  - robots.txt returned 4xx, meaning no restrictions: data.sec.gov (404), assistanceleague.org (403), purpleheartfoundation.org (403), svdpcincinnati.org (403), locations.outofthecloset.org (403).
- **One slip (bot rules):** the one honest browser retry of www.svdpseattle.org's challenge page (status 511) landed on svdpseattle.org, without www. Playwright followed that redirect before I had read svdpseattle.org's robots.txt. I read it right after: `User-Agent: *` / `Disallow:` (nothing disallowed). The fetched page was allowed, but the order broke the rule. No other request went to that host.
- **Blocked or failed (not retried):**
  - www.purpleheartfoundation.org: 403 to the homepage.
  - www.assistanceleague.org: Cloudflare challenge; one browser retry with no clicks did not clear, so blocked.
  - www.svdpcincinnati.org: 403.
  - www.svdp.us (St. Vincent de Paul, Lane County): robots.txt disallows `/` for ClaudeBot, so not fetched.
  - www.redwhiteandbluethrift.com: robots.txt unreachable, so treated as blocked and not fetched.
  - svdpusa.org: not attempted. The screen found it redirects to ssvpusa.org, whose robots.txt disallows ClaudeBot.
  - www.rebag.com/stores: 404 (the one Rebag fetch).
  - www.thrifttown.com: a parked-domain page (a script redirect to `/lander`).
- **Permission refusals:** none. The session's permission check refused no request.
- **JS-only locators (no store data in the HTML):** savers.com, americasthrift.com, familythriftcenter.com, outofthecloset.org, supportthevets.org (AMVETS), childrensorchard.com, style-encore.com and musicgoround.com.
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist, Private Equity Vet, PitchBook, Preqin and CB Insights. A PrivCo page and Crunchbase and ZoomInfo results came up in searches and were not opened.
- **Owner kinds are research notes, not engine classifications.** "PE-owned" means control or a PE hop with no stated stake. "Private, owner not stated" means a primary source names the company or founders but not the owner, and no PE evidence was found.

## Rows

| # | Brand (US stores, source) | Model | Owner (as stated) | Owner kind (note) | PE status | Since | Ev. |
|---|---|---|---|---|---|---|---|
| 1 | Goodwill (count not stated on pages read; trade press about 3,300) | donation thrift; 150 independent local Goodwill organizations | Goodwill Industries International (name); local member nonprofits run the stores | nonprofit (many independent members) | none | | T1 |
| 2 | The Salvation Army Thrift Stores (887, salvationarmyusa.org) | donation thrift | The Salvation Army | nonprofit | none | | T2 |
| 3 | Habitat for Humanity ReStore (count not stated; trade press about 900) | donation thrift (home goods, building materials); stores run by local affiliates | Habitat for Humanity International owns the name; "independently owned" by local affiliates | nonprofit (many independent affiliates) | none | | T3 |
| 4 | Plato's Closet (526, US and Canada, Winmark 10-K) | resale franchise | Winmark Corporation (Nasdaq: WINA), franchisor | public company | none (5%+ holders all passive or individual) | 1999 (screen) | T4 |
| 5 | Once Upon A Child (441, US and Canada) | resale franchise | Winmark | public company | none | | T4 |
| 6 | Play It Again Sports (309, US and Canada) | resale franchise (sporting goods) | Winmark | public company | none | | T4 |
| 7 | Uptown Cheapskate (160+ in 29 states, brand site) | resale franchise | BaseCamp Franchising LLC; co-CEOs Tyler and Zach Gordon "partnering with BaseCamp's founding family" (2022) | individuals and family (no stake stated) | none found | 2022 | T5 |
| 8 | Savers (179 US stores across all four banners; Savers itself at most about 155, derived) | for-profit donation thrift (buys donations from nonprofits) | Savers Value Village, Inc. (NYSE: SVV); Ares funds 61.5% | public company, PE majority | **PE-owned** (Ares over 50%; ADV Y) | public since 2023; 13G/A filed 2026-11-16 | T6 |
| 9 | Clothes Mentor (130+, brand site; 103 open all of 2025 per FDD Item 19, quoted on its franchise page) | resale franchise | NTY (franchise page: "NTY Resale Franchise"); current owner not stated; site history names Ronald G. Olson as an earlier acquirer | not found | none found | | T7 |
| 10 | Kid to Kid ("over 100 stores", including Canada, Portugal and Spain) | resale franchise | BaseCamp Franchising LLC | individuals and family | none found | 2022 | T5 |
| 11 | Style Encore (67, US and Canada) | resale franchise | Winmark ("registered trademark of Winmark Corporation") | public company | none | | T4; multi-state inferred, not stated |
| 12 | Deseret Industries (46 in 2024, DI site) | donation thrift and job training | The Church of Jesus Christ of Latter-day Saints | nonprofit (church) | none | 1938 | T8 |
| 13 | Buffalo Exchange ("around 40", brand site) | buy-sell-trade resale chain | Buffalo Exchange, LTD.; founders' daughter Rebecca Block runs it as CEO | family-run (owner not stated) | none found | 1974 | T9 |
| 14 | Crossroads Trading (38, brand site) | buy-sell-trade resale chain | Crossroads Trading; founded 1991 by Jerry Block and Chip Gerken; current owner not stated | not found | none found | | T10 |
| 15 | Music Go Round (35, US and Canada) | resale franchise (instruments) | Winmark | public company | none | | T4; multi-state inferred, not stated |
| 16 | America's Thrift Stores (24 in 2022 per TZP; site: "36 Southeastern markets", 5 states) | for-profit donation thrift | TZP Group (led a majority recapitalization) with Nuveen Global Impact Fund | PE firm | **PE-owned** (majority; ADV Y) | 2022-02-15 | T11 |
| 17 | Value Village, US (at least 15, derived: all 14 WA stores plus at least 1 in MD) | for-profit donation thrift | Savers Value Village, Inc. | public company, PE majority | **PE-owned** | as row 8 | T6 |
| 18 | Value World (13 in Ohio and Michigan, plus Texas stores) | for-profit donation thrift | Value World; "Family-owned and operated, for over 65 years" | family | none found | 1955 | T12 |
| 19 | Fashionphile (9 US locations: flagships and salons in CA, NY, TX, GA, FL, PA, UT) | luxury resale | Fashionphile Group, LLC; owners not stated | not found (trade press: Neiman Marcus minority since 2019; not cited) | none found | | T13 |
| 20 | 2nd Ave (at least 7, derived: 5 NJ plus MD and VA) | for-profit donation thrift | Savers Value Village, Inc. | public company, PE majority | **PE-owned** | as row 8 | T6 |
| 21 | St. Vincent de Paul thrift stores (count not found) | donation thrift run by independent local councils (WA and GA read) | local St. Vincent de Paul councils; the national name holder's site is blocked | nonprofit (local councils; 501(c)(3) status not stated on pages read) | none found | | T14 |
| 22 | The RealReal (count not stated; flagships in CA and NY plus neighborhood stores) | luxury consignment with stores | TheRealReal, Inc. (Nasdaq: REAL) | public company | none (FMR 10.45% passive; Divisadero 7.6% on a 13d-1(c) 13G but ADV N; the Kanen and Philotimo 13D ended at 3.9%) | | T15 |
| 23 | Unique (at least 2, derived: MD and VA) | for-profit donation thrift | Savers Value Village, Inc. | public company, PE majority | **PE-owned** | as row 8 | T6 |

- Derived banner counts: the 10-K gives US stores by state, not by banner. The store directory's brand filter per state shows WA: Value Village only; CA and NY: Savers only; NJ: 2nd Ave only; MD: Savers, Value Village, Unique and 2nd Ave; VA: Savers, Unique and 2nd Ave. Only 6 of the 31 directory states were read. So Value Village is at least 15 (all 14 WA stores plus MD), 2nd Ave at least 7, Unique at least 2, and Savers at most 155.
- Donation-based rows (11): 1, 2, 3, 8, 12, 16, 17, 18, 20, 21, 23. Resale rows (12): 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 19, 22.

### Couldn't confirm (not counted)

| Candidate | What was found | Why not counted |
|---|---|---|
| AMVETS Thrift Stores | supportthevets.org: "AMVETS National Service Foundation provides support to Veterans through service programs"; "100% of proceeds are used for AMVETS Veterans programs." | Locator is JS-only, so no states were read. A nonprofit name either way. |
| Purple Heart Thrift Stores | purpleheartfoundation.org returned 403 | Blocked |
| Out of the Closet (AIDS Healthcare Foundation) | about page: founded 1990 for AHF, a 501(c)(3) | Locator is JS-only, so no states were read. Nonprofit either way. |
| Assistance League thrift shops | Cloudflare challenge did not clear | Blocked |
| Volunteers of America thrift stores | VOA Ohio & Indiana: "When you shop at VOA Thrift Stores in Ohio…"; only Ohio regions are listed | Only one state confirmed for the affiliate read; other VOA affiliates not checked |
| Children's Orchard (NTY) | homepage and JS-only locator | No states read |
| Rebag (luxury resale) | /stores 404 | Not confirmed. Investors named in search results (General Catalyst, Crosslink, FJ Labs) all report `Any PE Funds` N; Novator is absent from Form ADV |
| Red, White & Blue Thrift (also trades as Valley Value, Mile High, World Thrift per 2020 trade press) | robots.txt unreachable | Blocked |
| Thrift Town | thrifttown.com is a parked-domain page; trade press (2020) says 4 stores in TX and NM | Not confirmed |
| DAV thrift stores, Ragstock | not fetched (budget) | Not checked |
| Goodwill-style regional names (Arc thrift stores, Hospice and Junior League shops) | names vary by chapter | Not one brand |

**Checked and excluded as single-state:**
- Texas Thrift: 17 Texas stores; footer "© BVTS LLC dba Texas Thrift.". The screen's lead that Brightmore Brands, backed by Beach Point (ADV Y), bought it was not verified, and it would be out of scope anyway.
- Family Thrift Center: the site's location menu lists only Texas regions. InvestigateWest (2020) said Texas and Arizona.
- Carolina Value Village (NC), Value Village Atlanta (GA), Sunshine Thrift (FL), Southern Thrift (TN) and Thrift Stores of Ohio: single-state per InvestigateWest 2020; not re-checked.

## Evidence

- **T1 Goodwill.** [Goodwill, About](https://www.goodwill.org/about/), saved by the screen worker after a browser retry; its challenge cleared by itself.
  - "Goodwill Industries International supports a network of 150 local Goodwill® organizations."
  - "Goodwill Industries International is a 501(C)(3) Nonprofit registered in the US under EIN: 53-0196517"
  - Store count: not on the pages read (the about page and annual-impact-report page).
- **T2 Salvation Army.** [Salvation Army USA, Thrift Stores](https://www.salvationarmyusa.org/thrift-stores/) (screen cache): "887 thrift stores across the United States, which fund local programs that help improve lives"
- **T3 Habitat ReStore.** [Habitat, ReStores](https://www.habitat.org/restores) (screen cache): "Habitat ReStores are independently owned reuse stores operated by local Habitat for Humanity organizations."
- **T4 Winmark brands** (rows 4, 5, 6, 11, 15).
  - [Winmark 10-K FY2025](https://www.sec.gov/Archives/edgar/data/908315/000090831526000007/wina-20251227x10k.htm) (screen cache):
    - "At December 27, 2025, there were 1,378 franchises in operation in the United States and Canada"
    - Table rows "Plato’s Closet 515 18 (7) 526", "Once Upon A Child 430 17 (6) 441", "Play It Again Sports 302 15 (8) 309", "Style Encore 69 2 (4) 67", "Music Go Round 34 3 (2) 35"
    - "All stores are owned and operated by franchisees. Winmark does not own or operate any corporate stores."
    - "Of the 1,378 total franchised stores as of December 27, 2025, 165 were located in Canada."
  - [Style Encore site](https://style-encore.com/locations/): "Style Encore is a registered trademark of Winmark Corporation® based in Minneapolis, MN. Each franchise is independently owned and operated."
  - Holders:
    - [Proxy 2026](https://www.sec.gov/Archives/edgar/data/908315/000090831526000010/wina-20260304xdef14a.htm) table: BlackRock 12.1%, Ronald G. Olson 11.1% (individual), Neuberger Berman Group 8.2%, Renaissance 5.8%, Vanguard 5.2%.
    - On Neuberger: "We have relied on information provided by Neuberger Berman Group LLC on Form 13F-HR filed on February 13, 2026." NB's adviser reports PE funds, but Winmark's filing index shows no 13G or 13D from it, so it is not counted (a proxy table never creates a stake).
    - The newest 13G filings, all with the Rule 13d-1(b) box checked:
      - [First Trust, 13G/A 2026-10-30](https://www.sec.gov/Archives/edgar/data/908315/000144554626008249/xslSCHEDULE_13G_X02/primary_doc.xml)
      - [AltraVue, 13G 2026-01-21](https://www.sec.gov/Archives/edgar/data/908315/000174083726000003/xslSCHEDULE_13G_X01/primary_doc.xml) (4.9%)
      - [Renaissance, 13G/A 2026-11-12](https://www.sec.gov/Archives/edgar/data/908315/000103738926000071/xslSCHEDULE_13G_X02/primary_doc.xml) (5.02%)
      - [BlackRock, 13G/A 2025-04-17](https://www.sec.gov/Archives/edgar/data/908315/000157641925000821/xslSCHEDULE_13G_X01/primary_doc.xml)
    - No 13D appears in Winmark's filing index (data.sec.gov submissions, screen cache).
  - Multi-state: per-state counts are not stated anywhere read. Plato's Closet, Once Upon A Child and Play It Again Sports each have more stores than all of Winmark's 165 Canadian stores combined. Style Encore (67) and Music Go Round (35) are inferred multi-state; their locators are JS-only.
- **T5 BaseCamp brands** (Uptown Cheapskate, Kid to Kid).
  - [BaseCamp Franchising](https://bcfranchise.com/):
    - "BaseCamp Franchising is the parent company of two upscale thrift concepts, Uptown Cheapskate and Kid to Kid."
    - "With over 300 stores open and another 50+ under development"
    - "Visit one of our 270+ locations nationwide"
    - "Our stores are 100% franchised"
  - [Uptown about](https://www.uptowncheapskate.com/about/): "Today, Uptown Cheapskate has expanded to over 160+ locations in 29 states."
  - [Kid to Kid about](https://kidtokid.com/about/):
    - "Our franchise recycles millions of items each year in over 100 stores."
    - "Kid to Kid has bought and sold hundreds of millions of quality childrens’ items in stores all across the United States."
  - [BaseCamp release, 2022-09-06](https://www.prweb.com/releases/basecamp-franchising-llc-appoints-tyler-gordon-and-zach-gordon-as-co-ceos-880027925.html) (screen cache, browser retry):
    - "Tyler and Zach are partnering with BaseCamp's founding family"
    - "over 200 stores across 31 U.S. states, Canada, Portugal and Spain"
  - Search results (leads only) describe the Gordon brothers buying a majority stake in 2022, and found no PE investor in 2025 or 2026. No stake is stated in a primary source.
- **T6 Savers Value Village banners** (rows 8, 17, 20, 23).
  - [SVV 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1883313/000188331326000014/svv-20260103.htm) (screen cache):
    - "we operate a total of 367 stores under the Savers®, Value Village®, Value Village Boutique™, Village des ValeursMD, Unique® and 2nd Ave.® banners."
    - "As of January 3, 2026, we had 179 stores in the U.S., 170 stores in Canada and 18 stores in Australia."
    - "As of January 3, 2026, we had 179 U.S. retail stores located in 30 states" (Washington 14, New Jersey 5, Maryland 13, Virginia 6, …)
    - "We own federally registered trademarks related to our brands, including SAVERS®, VALUE VILLAGE®, UNIQUE®, UNIQUE THRIFT STORE®, 2ND AVE®. and 2ND AVE VALUE STORES® in the U.S."
    - "We are a “controlled company” and majority owned and controlled by certain funds, investment vehicles and accounts managed or advised by the Private Equity Group of Ares Management Corporation (the “Ares Funds”)"
  - [Ares 13G/A, filed 2026-11-16](https://www.sec.gov/Archives/edgar/data/1883313/000110465926128617/xslSCHEDULE_13G_X02/primary_doc.xml):
    - cover for "Names of Reporting Persons Ares Management LLC": 94,449,188 shares, 61.5%;
    - the Rule 13d-1(d) box is checked;
    - "based upon 153,616,403 shares of Common Stock outstanding as of November 2, 2026".
    - Re-confirmed: SVV's filing index (data.sec.gov, screen cache, today) shows no later Ares amendment.
  - [Savers store directory](https://stores.savers.com/):
    - "With stores throughout the United States, Canada and Australia, chances are there's a Savers, Value Village, Unique, or 2nd Ave. thrift store near you."
    - "We are a for-profit company that champions reuse."
    - "Copyright © TVI, Inc. dba Savers Value Village stores."
    - The directory lists 31 US states (adds North Carolina and Tennessee to the 10-K's list).
  - State pages ([WA](https://stores.savers.com/wa/), [CA](https://stores.savers.com/ca/), [MD](https://stores.savers.com/md/), [NY](https://stores.savers.com/ny/), [NJ](https://stores.savers.com/nj/), [VA](https://stores.savers.com/va/)): brand-filter values in the page data, read from raw HTML, e.g. `"name":"Value Village","specialty_short_name":null,"group":"Brands"` (WA and MD), `"name":"2nd Ave",…` (MD, NJ, VA) and `"name":"Unique",…` (MD, VA).
- **T7 Clothes Mentor.**
  - [About](https://clothesmentor.com/pages/about-us):
    - "you can step into any of our 130+ locations across the United States"
    - "After rapid expansion, Ronald G. Olson, president of Grow Biz International, acquired the company." This sentence follows the founding of the first Once Upon A Child store. Grow Biz was Winmark's earlier name, so it reads as history, not a statement of who owns Clothes Mentor's franchisor today.
  - [Own a store](https://clothesmentor.com/pages/own-a-store):
    - "As an NTY Resale Franchise owner, you make more money faster"
    - "$819,550 is the average net sales of the 103 Clothes Mentor® stores in operation for the entire calendar year ended December 31, 2025." (citing its FDD dated April 6, 2026)
  - [Homepage](https://clothesmentor.com/): "Our products are available online and at our local, independently owned Clothes Mentor stores."
  - The FDD itself was not read: state registries serve PDFs, and there is no PDF text tool in this environment.
- **T8 Deseret Industries.** [About](https://www.deseretindustries.org/about-us):
  - "Deseret Industries is a nonprofit thrift store and donation center."
  - "DI is owned and operated by The Church of Jesus Christ of Latter-day Saints."
  - "Stores: 46"
  - "The Deseret Industries Thrift Store and Donation Center in Houston, Texas, which opened in 2021."
  - Multi-state also shown historically: "1963: Nine Deseret Industries stores are in operation: six in Utah, two in California, and one in Arizona."
- **T9 Buffalo Exchange.**
  - [Locations](https://buffaloexchange.com/location/):
    - "We have around 40 locations across the US."
    - "Visit our newest locations in Austin (SoCo), East Nashville, Houston, Pasadena & St. Paul!"
  - [About](https://buffaloexchange.com/about-us/): "Today, Kerstin and Spencer’s daughter, Rebecca Block, continues to run the company as CEO"
  - Footer: "© 2026 Buffalo Exchange, LTD."
- **T10 Crossroads Trading.**
  - [Homepage](https://crossroadstrading.com/): "We have 38 store locations across the US." Its region menu lists Northern and Southern California, Pacific Northwest, Colorado, Midwest, East Coast and Texas.
  - [About](https://crossroadstrading.com/about-us-2/): "Founded in 1991 by Jerry Block and Chip Gerken, Crossroads Trading was one of the first to pioneer the idea of secondhand clothing as an alternative to traditional retail."
  - Current owner: not stated. Search leads showed no deal.
- **T11 America's Thrift Stores.**
  - [TZP release, 2022-02-15](https://www.prnewswire.com/news-releases/tzp-group-leads-majority-recapitalization-of-americas-thrift-stores-301482201.html) (screen cache):
    - "TZP GROUP LEADS MAJORITY RECAPITALIZATION OF AMERICA'S THRIFT STORES"
    - "TZP Group LLC, ("TZP"), a multi-strategy private equity firm, announced today that it has led a recapitalization of America's Thrift Stores"
    - "With 24 locations across five states"
  - [TZP portfolio](https://www.tzpgroup.com/portfolio/) (screen cache, today): "America’s Thrift Stores Thrift retail with community impact Current"
  - [America's Thrift about](https://www.americasthrift.com/about/):
    - "Founded in 1984, America’s Thrift Stores is a for-profit company that supports numerous children’s health and addiction recovery charities."
    - "we are able to give back to our six charity partners across the five states we operate in."
  - [Homepage](https://www.americasthrift.com/): "Delivering an elevated thrift experience in 36 Southeastern markets and counting."
- **T12 Value World.**
  - [About](https://valueworld.com/about/):
    - "Family-owned and operated, for over 65 years"
    - "Today, we have 13 thrift store locations throughout Ohio and Michigan."
    - "we’re still family-owned"
  - [Homepage](https://valueworld.com/):
    - "Or view all stores in: Michigan, Ohio, Texas"
    - "Our new Barker Cypress location is now open!" (Houston)
- **T13 Fashionphile.** [Locations](https://www.fashionphile.com/pages/locations):
  - Addresses including "Carlsbad, CA 92011", "New York, NY 10001" and "Dallas, TX 75231", plus salons in Atlanta, San Francisco, Boca Raton, Philadelphia and Lehi, and one in the UK.
  - Footer "© 2026 Fashionphile Group, LLC".
  - No owner is stated.
- **T14 St. Vincent de Paul.**
  - [SVdP Seattle | King County](https://svdpseattle.org/) (browser retry; see the slip under "How this was sourced"):
    - "For over 100 years, St Vincent de Paul of Seattle | King County has provided critical aid"
    - "Thrift Store Donations Click here for information about thrift store hours of operation, donation hours, and accepted items"
  - [SVdP Georgia](https://svdpgeorgia.org/): navigation "What We Do Housing Hunger Health Essential Services Thrift Stores".
  - The national council (svdpusa.org, which redirects to ssvpusa.org) is blocked, and so are two other councils (svdp.us by robots, svdpcincinnati.org by 403).
- **T15 The RealReal.**
  - [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1573221/000157322126000010/real-20251231.htm): "we operate several larger footprint flagship stores in San Francisco, California, Los Angeles, California and New York, New York". No store total was found in the text.
  - [Proxy 2026](https://www.sec.gov/Archives/edgar/data/1573221/000157322126000036/real-20260427.htm): the only 5% holder is FMR LLC, 10.45% ("As reported in a statement on a Schedule 13G filed with the SEC on January 8, 2026 by FMR LLC.").
  - [Divisadero 13G, 2026-06-30](https://www.sec.gov/Archives/edgar/data/1573221/000091957426004168/xslSCHEDULE_13G_X02/primary_doc.xml): 7.6%, Rule 13d-1(c) box checked. Divisadero's ADV says `Any PE Funds` N, so it is not PE.
  - [Kanen and Philotimo 13D/A No. 2, event 2025-01-28](https://www.sec.gov/Archives/edgar/data/1573221/000092189525000206/xslSCHEDULE_13D_X01/primary_doc.xml): Kanen Wealth Management 3.9%, at or under 5%, so it ends. Both advisers' ADVs say N.

## Firms named

| Firm | Where | Role |
|---|---|---|
| Ares Management | Savers, Value Village, 2nd Ave, Unique | 61.5% holder (13G/A, 13d-1(d)) |
| TZP Group | America's Thrift Stores | led majority recapitalization, 2022; portfolio page "Current" |
| Nuveen (Global Impact Fund) | America's Thrift Stores | co-investor, 2022; stake not stated |
| Alpine Investors | America's Thrift Stores | 2012 buyer and 70% owner per InvestigateWest (2020); not cited, and not a current hop on any primary source read |
| Neuberger Berman | Winmark | 8.2% per 13F only; no 13G or 13D, so not counted |
| Beach Point Capital | Texas Thrift (screen lead) | not verified; row excluded as single-state |
| Divisadero Street Capital; Kanen Wealth Management; Philotimo | The RealReal | 13G (13d-1(c)) and an ended 13D; not PE |
| General Catalyst, Crosslink, FJ Labs, Novator | Rebag (search leads) | VC; row not confirmed |

## Form ADV results (November 2026 rosters, local copy)

| Firm | Legal name | CRD | Roster | Any PE Funds | # PE funds |
|---|---|---|---|---|---|
| Ares | Ares Management LLC | 130074 | RIA | Y | 157 |
| TZP | TZP Management Associates, LLC | 160907 | RIA | Y | 48 |
| Nuveen | Nuveen Alternatives Advisors LLC (which adviser runs the Global Impact Fund is not stated) | 160255 | RIA | Y | 5 |
| Alpine Investors | Alpine Management Services III, LLC | 157255 | RIA | Y | 16 |
| Neuberger Berman | Neuberger Berman Investment Advisers LLC | 124687 | RIA | Y | 11 |
| Beach Point | Beach Point Capital Management LP | 148885 | RIA | Y | 4 |
| Divisadero | Divisadero Street Capital Management, LP | 317392 | RIA | N | — |
| Kanen | Kanen Wealth Management LLC | 282746 | RIA | N | — |
| Philotimo | Philotimo Ventures, LLC | 340944 | ERA | N | — |
| Renaissance | Renaissance Technologies LLC | 106661 | RIA | N | — |
| (name match) | Renaissance Technologies AI Supercomputing Hedge Capital Ltd. | 338503 | ERA | Y | 1 |
| First Trust | First Trust Advisors LP | 107027 | RIA | N | — |
| AltraVue | AltraVue Capital, LLC | 283260 | RIA | N | — |
| General Catalyst | General Catalyst Group Management, LLC | 162548 | RIA | N | — |
| Crosslink | Crosslink Capital, Inc. | 109948 | RIA | N | — |
| FJ Labs | FJ Labs Management LP | 312920 | ERA | N | — |
| Novator | not found (the only match, Innovator Capital Management, is unrelated) | | | | |

## Rows resting on documents older than 18 months

- **America's Thrift Stores:** the deal release is from 2022-02-15, but TZP's portfolio page, seen today, lists it as "Current", so the hop is confirmed current.
- **No other PE row is stale.** Savers Value Village rests on a 13G/A filed 2026-11-16.
- **Non-PE row resting on an old document:** BaseCamp's ownership statement (2022 release). Its current pages name no owner.

## Surprises

- **Savers' banners decide the result:** 21.7% with four banner rows, 10.0% with one.
- **Resale franchises are PE-free.** None of the 12 resale rows shows PE, even though resale franchising is a usual PE target. Winmark is public with passive holders only. BaseCamp went to individual operators (the Gordons) in 2022, not to a fund.
- **Clothes Mentor's own history names Ronald G. Olson,** Winmark's second-largest holder (11.1%, as an individual), as an acquirer. That link between Clothes Mentor and Winmark's holder remains unexplained without the FDD.
- **America's Thrift now says "36 Southeastern markets"** against 24 locations at the 2022 deal.
- **Texas Thrift is Texas-only today** (17 stores). It was a multi-state chain in 2020 under several names, per InvestigateWest.
- **Value World has expanded to Houston,** which makes it multi-state; it is still family-owned.
- **A Form ADV exempt-reporting entry named "Renaissance Technologies AI Supercomputing Hedge Capital Ltd." reports a PE fund.** Its link to Renaissance Technologies LLC is unconfirmed. It changes nothing here, because Renaissance's Winmark 13G is filed under 13d-1(b).

## Open questions for the developer

1. **Savers' banners:** count Savers, Value Village, 2nd Ave and Unique as four rows (21.7%, by the "store names consumers see" rule in the brief) or as one brand (10.0%)? Either way the industry is at or above the 10% bar, but only the four-row count clears it with room.
2. **Scope:** keep Play It Again Sports, Music Go Round and the two luxury resale rows in thrift and resale? Dropping all four gives 5 / 19 (26.3%).
3. **Unconfirmed candidates:** should the 11 unconfirmed names (AMVETS, Purple Heart, Out of the Closet, Assistance League, VOA, Children's Orchard, Rebag, Red White & Blue, Thrift Town, DAV, Ragstock) be checked further, mostly with a browser for JS locators? None shows PE evidence. Adding all 11 would lower the share to 14.7% (four Savers rows) or 6.5% (one).
4. **St. Vincent de Paul:** the national name holder is blocked to this bot. Is "local councils (nonprofit)" enough for the row, given the local council pages read do not state 501(c)(3) status?

## Cost

- **Fetches:** 69 page requests (67 curl, 2 browser) plus 53 robots.txt requests. Of these, 11 went to SEC hosts (2 robots.txt, 9 documents).
- **Searches and reuse:** 6 WebSearch queries (leads only). About 20 of the screen worker's pages were reused from its cache, not refetched.
- **Tokens:** about 150k in this worker session.

## Quote check

- **93 of 93 quotes were found verbatim in the saved page text.** The check is case-sensitive after normalizing whitespace, curly quotes, dashes, non-breaking and zero-width characters.
- **93 of 93 altered copies failed**, as they should: each has one word changed.
- Ten checks run against raw HTML, not visible text: the nine Savers brand-filter values and thrifttown.com's lander script.
- **Not covered:** values read from tables or filing cover pages. These are Ares's 61.5% and 94,449,188 shares, the Winmark and RealReal holder percentages, the 13G rule boxes (read from checkbox image alt text) and Fashionphile's salon list.
- Script and quote list: `$SCR/scripts/fu-thrift/check_quotes.py` and `quotes.tsv`; pages in `$SCR/pages/fu-thrift/` (index.tsv, robots-log.tsv, robots/) and `$SCR/pages/screen2-a/` (`$SCR` = the session scratchpad).
