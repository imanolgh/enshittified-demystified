# Research: Category audit, car washes

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (16:35–17:11 UTC) · Ownership facts come from primary sources only; an M&A advisory firm's public list supplies the ranking only.

**Question:** For the top ~30 US car wash brands (express/conveyor, full-service and flex), who owns each today, what share is PE-owned or PE-backed, and which have brand-direct affiliate programs?

**Short answer**

| | Car washes (30 brand rows) |
|---|---|
| PE-owned plus PE minority stake, where a source read here (or the pilot's Form ADV pass) labels the owner PE | **10 / 30 (33.3%)**; 54.0% of top-30 locations |
| The same, if the 5 rows whose investment-firm owner awaits a Form ADV check turn out PE (FS&Co, Access Holdings ×2, Susquehanna Private Capital, Point72 Private Investments) | **15 / 30 (50.0%)**; 64.8% of locations |
| Upper bound, also counting the 2 Wildcat-platform rows (single-family office plus a Sculptor Real Estate investment with no stated stake) | 17 / 30 (56.7%) |
| Strict count (public company with a 5%+ PE-flagged holder counts as minority) | same as above: **no public company is left in the top 30**. Mister Car Wash was taken private by Leonard Green funds on 2026-05-19 |
| Owner not found | **1** (Sam's Xpress). 6 more rows name a private parent or founder family but no source states who owns it |
| Brand-direct affiliate programs | **none found**. Some brands run customer refer-a-friend programs, which aren't affiliate programs |

- **Category character:** car washes are almost all company-operated chains, and the large ones are sponsor-built platforms. Every one of the top 4 has an investment firm in the chain: Oaktree, Leonard Green, KKR/Seidler (minority) and Golden Gate.
- **Ranking caveat:** the free ranking used counts sites "in development", and for several lower rows it is 2–3 times the brand's own count (Splash Car Wash & Oil Change 80 vs 27, Big Dan's 57 vs 27, Mr. Clean 49 vs 19). Rows 17–30 are less reliable than rows 1–16.
- **Rollups:** four of the ranking's entries are rollups, not brands (MOJO/Mammoth, Spotless, Express Wash Concepts, Summit Wash). They are listed separately. Three of their brands (Cobblestone, Clean Express Auto Wash, Flagship) were placed in the 30 by their own counts.

## How this was sourced (read first)

- **Ranking:** Car Wash Advisory's public "Top Car Wash Companies" page (an M&A advisory firm), used for the ranking only. The trade-press list, PC&D's Top 50, could not be used (see Ranking).
- **Ownership facts:** SEC filings (Mister Car Wash 8-K and 10-K, Driven Brands 8-K), company press releases (company sites, PR Newswire, EIN Presswire), sponsor portfolio pages and sponsor releases, and company sites. One company release was readable only as a trade-association reprint (Tsunami, carwash.org), flagged in its row.
- **Leads only, never cited:** Car Wash Advisory's per-company "Financial Sponsor" fields, Dealseam, WashIndex, PrivSource, Mergr, PitchBook, Crunchbase and CB Insights results that appeared in searches (none opened except Car Wash Advisory company pages).
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist, Private Equity Vet.
- **Robots:** carwash.com (PC&D) disallows ClaudeBot and anthropic-ai in robots.txt (it allows Claude-User). It was never fetched with curl. One WebFetch of the 2025 Top 50 page returned HTTP 403, and the site was not used after that. kget.com disallows anthropic-ai and was not fetched. spotlessbrands.com and summitwashholdings.com returned 403 to curl, including robots.txt. They were read only through WebFetch.
- **Quote self-check:** all 90 quotes taken from curl'd pages were string-matched against the downloaded text (HTML stripped, whitespace collapsed, curly quotes and dashes normalized), and 90 of 90 were found. Negative control: 3 deliberately altered quotes all failed. Not mechanically checked: the WebFetch-only quotes (Spotless Brands, Summit Wash, marked "WebFetch") and portfolio-tile fields.
- **Owner kinds are research notes, not engine classifications** (ADR 0001 governs the product). "PE-owned" means control, or a PE owner with no stated stake. Counts are by brand row.

## Car washes

**Ranking:** Car Wash Advisory LLC, "Top Car Wash Companies: Definitive ranking of the top carwash companies in the U.S. by site count", https://www.carwashadvisory.com/top-car-wash-companies, fetched 2026-11-07; its FAQ dates the data "As of May 2026". It ranks by site count: "Our top car wash companies list is ranked by the number of locations each car wash business operates." Its counts include pipeline sites: "*Site Count data includes sites in development." Car Wash Advisory is an M&A advisory firm, not a publication, and it was used for the ranking only.

**Why not trade press:** Professional Carwashing & Detailing's annual "Top 50 Conveyor Carwash Chains" (carwash.com; the 2025 edition ranks by projected year-end locations, and the 2026 edition is not out until December) is on a site whose robots.txt disallows ClaudeBot and anthropic-ai. WebFetch returned 403. DRB's reprint pages return "Page Not Found". ScrapeHero lists only 10.

**How the 30 brand rows were built:**
- **Brand entries:** Car Wash Advisory entries that are a single consumer-facing name keep its count and order.
- **Rollup entries:** entries that are rollups were moved to "Rollups and groups that are not brands": Mammoth Holdings (now MOJO Family of Brands), Spotless Brands, Express Wash Concepts and Summit Wash Holdings. Each of their brands was placed by its own count where a primary source gives one:
  - Cobblestone (Spotless): 119 location pages on cobblestone.com, my tally, which includes some "Coming Soon" pages.
  - Clean Express Auto Wash (EWC): 61, from EWC's 2026-10-23 release.
  - Flagship Carwash (Spotless): "more than 50", from the Spotless site.
- **ClearWater entry:** "ClearWater Express Wash" (83) covers two brands: ClearWater (30 own) and BlueWave Express (53), per ClearWater's release. BlueWave takes the row; ClearWater (30) falls below the cutoff.
- **Ties:** brands at the same count keep Car Wash Advisory's page order. Clean Express (not on that page) ties Golden Nozzle at 61 and is placed first, so that the Ev. ids run in row order.
- **Cutoff:** the cutoff falls at 50.
  - Just below it: #31 Mr. Clean Car Wash (49 on Car Wash Advisory; its own site says "19 locations across Georgia & Florida"; "Certain trademarks used under license from The Procter & Gamble Company or its affiliates."; owner not found) and #32 Prestige Car Wash (49; owner not checked).
- **Not exhaustive:** rollup brands with no stated count could belong above the cutoff. Unchecked: Moo Moo Express, Flying Ace, Green Clean and Bee Clean (EWC), Speeders and Waters (Summit), and MOJO's 21 brands.

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Whistle Express Car Wash (530) | funds managed by Oaktree Capital Management (majority); AMCO material minority (2023) | PE-owned (Oaktree invests "in credit, private equity, real assets and listed equities"; ADV check pending) | Oaktree Capital Management; A&M Capital Opportunities Fund (minority) | 2023-07-25 | — | company-operated | none found | CW1 |
| 2 | Mister Car Wash (518; 548 per 10-K) | MCW Parent, LP, indirectly controlled by funds affiliated with Leonard Green & Partners | PE-owned (take-private) | Leonard Green & Partners | 2026-05-19 (LGP funds held ~67% before) | none (was MCW, delisted 2026) | company-operated | none found | CW2 |
| 3 | Quick Quack Car Wash (365) | founders keep control (Seidler page); KKR and Seidler Equity Partners hold minority stakes | PE minority stake | KKR; Seidler Equity Partners | KKR 2024 (Seidler year not found) | — | not found | none found (customer Refer-A-Friend only) | CW3 |
| 4 | Tidal Wave Auto Spa (338) | Golden Gate Capital (recapitalization; founder "a significant shareholder") | PE-owned (stake not stated; last primary confirmation 2020) | Golden Gate Capital | 2020-12-30 | — | company-operated | none found (customer refer-a-friend page only) | CW4 |
| 5 | Tommy's Express Car Wash (283) | "A Visionquest Company" | Owner type not confirmed (private group; no PE evidence found) | none found | not found | — | franchise (4% royalty) | none found | CW5 |
| 6 | Club Car Wash (280) | Wildcat Capital Management's car wash platform; Sculptor Real Estate growth investment (2023) | Owner type not confirmed (single-family office; Sculptor stake not stated) | Sculptor Real Estate (investor, stake not stated) | Sculptor 2023-10-16; Wildcat year not found | — | not found | none found | CW6 |
| 7 | ZIPS Car Wash (197; also runs Rocket Express, Jet Brite) | "a group of its existing institutional investors" | lender-owned (post-Chapter 11) | none named | 2025-04-30 | — | company-operated | none found | CW7 |
| 8 | Super Star Car Wash (192) | TSG Consumer Partners (majority) | PE-owned | TSG Consumer Partners | 2021 (signed 2021-11-15) | — | company-operated ("Express car wash operator") | none found | CW8 |
| 9 | GO Car Wash (164) | Imperial Capital (Fund VII), "Status Active" | PE-owned | Imperial Capital | 2019 | — | not found | none found | CW9 |
| 10 | WhiteWater Express Car Wash (144) | Freeman Spogli & Co. (investment Dec 2021; stake not stated) | PE-owned if FS&Co passes ADV check (no PE label in pages read; page doesn't separate current from realized) | Freeman Spogli & Co. | 2021-12 | — | not found | none found | CW10 |
| 11 | ModWash (130) | not stated; "Founded by Karen Hutton" | founder-led, owner not stated (no PE evidence found) | none found | — | — | not found | none found | CW11 |
| 12 | Cobblestone Auto Spa / Cobblestone Car Wash (~119, my tally) | Spotless Brands, "a portfolio company of Access Holdings" | PE-owned if Access passes ADV check (Access: "investment firm") | Access Holdings | 2020-01 (joined Spotless) | — | not found | none found | CW12 |
| 13 | El Car Wash (110) | Warburg Pincus (acquired the company) | PE-owned (last primary confirmation 2022) | Warburg Pincus | 2022-08-04 | — | company-operated | none found | CW13 |
| 14 | Autobell Car Wash (91) | Howard family ("owner & CEO Chuck Howard") | family | none | not applicable (founded 1969) | — | not found | none found | CW14 |
| 15 | LUV Car Wash (87) | Susquehanna Private Capital (launched the platform; stake not stated) | PE-owned if SPC passes ADV check (no PE label in source) | Susquehanna Private Capital | 2021-11-15 | — | not found | none found | CW15 |
| 16 | Tsunami Express Car Wash (83; 74 per 2025 release) | "backed by an affiliate of Point72 Private Investments" (stake not stated) | PE-owned if Point72 PI passes ADV check | Point72 Private Investments (affiliate) | not found (stated 2025-09-12) | — | company-operated | none found | CW16 |
| 17 | Splash Car Wash & Oil Change, Arkansas (80; own site: 27) | "An Arkansas, family-owned business" | family | none | not applicable | — | not found | none found | CW17 |
| 18 | Splash Car Wash, Northeast (77) | AEA Investors Small Business Private Equity (majority) | PE-owned | AEA Investors (bought from Palladin Consumer Retail Partners) | 2025-04-25 | — | company-operated ("car wash operator") | none found | CW18 |
| 19 | Caliber Car Wash (64) | Percheron Capital (majority); Eagle Merchant Partners minority (2021) | PE-owned (last primary confirmation 2021) | Percheron Capital; Eagle Merchant Partners (minority) | 2021-12-16 (signed) | — | not found | none found | CW19 |
| 20 | Crew Carwash (63) | "Still owned by the Dahm Family" | family | none | not applicable | — | not found | none found | CW20 |
| 21 | Clean Express Auto Wash (61) | Express Wash Concepts, part of Wildcat Capital Management's car wash platform | Owner type not confirmed (single-family office; Sculptor stake not stated) | Sculptor Real Estate (investor, stake not stated) | not found | — | company-operated (EWC "operates") | none found | CW21 |
| 22 | Golden Nozzle Car Wash (61) | Nouria ("part of the nouria family") | Owner type not confirmed (founder-led c-store company; owner not stated; no PE evidence found) | none found | not found | — | not found | none found | CW22 |
| 23 | Splash In (ECO) Car Wash (60) | subsidiary of The Wills Group, "family-owned and operated" | family | none | not applicable | — | not found | none found | CW23 |
| 24 | Jax Kar Wash (59) | TRP Capital Partners (Fund TRP V) | PE-owned (stake not stated) | TRP Capital Partners | 2022 | — | company-operated ("Operator of car washes") | none found | CW24 |
| 25 | Big Dan's Car Wash (57; own site: 27) | not stated; "Big Dan" Shadday is the founder figure | founder family implied, owner not stated (no PE evidence found) | none found | — | — | not found | none found | CW25 |
| 26 | Champion Xpress Carwash (55) | not stated; "Run by family" | family-run, owner not stated (no PE evidence found) | none found | — | — | not found | none found | CW26 |
| 27 | BlueWave Express (53) | ClearWater Express Wash (via Texas Express Wash LLC); "privately owned" | private company, owner not stated (no PE evidence found; lender WhiteHorse Capital) | none found (WhiteHorse is a lender) | 2025-11-26 | — | not found | none found | CW27 |
| 28 | Brown Bear Car Wash (51) | "We are proud to be family-owned." (Car Wash Enterprises, Inc.) | family | none | not applicable (1957) | — | company-operated (does not franchise) | none found | CW28 |
| 29 | Flagship Carwash (more than 50) | Spotless Brands, "a portfolio company of Access Holdings" | PE-owned if Access passes ADV check | Access Holdings | 2021-08 (joined Spotless) | — | not found | none found | CW29 |
| 30 | Sam's Xpress Car Wash (50) | not found | not found | not found | — | — | company-operated ("we proudly operate") | none found | CW30 |

### Evidence
- **CW1 Whistle Express Car Wash**
  - Owner (2023): "As part of the transaction, Oaktree has acquired a majority ownership position in the Company." — [Magnolia Wash Holdings release, PR Newswire, 2023-07-25](https://www.prnewswire.com/news-releases/magnolia-wash-holdings-announces-growth-capital-investment-301885551.html)
  - Minority: "A&M Capital Opportunities Fund ("AMCO") will maintain a material minority ownership stake in the enterprise." — [same release](https://www.prnewswire.com/news-releases/magnolia-wash-holdings-announces-growth-capital-investment-301885551.html)
  - Brand link (Magnolia = Whistle): "is working to consolidate its operations under the Whistle Express banner" — [same release](https://www.prnewswire.com/news-releases/magnolia-wash-holdings-announces-growth-capital-investment-301885551.html)
  - Since: "today announced it has received a growth capital investment from funds managed by Oaktree Capital Management, L.P." (dateline "CHARLOTTE, N.C. , July 25, 2023") — [same release](https://www.prnewswire.com/news-releases/magnolia-wash-holdings-announces-growth-capital-investment-301885551.html)
  - Owner kind: "The firm emphasizes an opportunistic, value-oriented and risk-controlled approach to investments in credit, private equity, real assets and listed equities." — [same release, About Oaktree](https://www.prnewswire.com/news-releases/magnolia-wash-holdings-announces-growth-capital-investment-301885551.html)
  - Current: "Whistle Express, which is backed by funds managed by Oaktree Capital Management" — [Whistle Express, Take 5 closing release (Business Wire), on whistleexpresscarwash.com, 2025](https://whistleexpresscarwash.com/news/whistle-express-signs-definitive-agreement-to-acquire-take-5-car-wash-creating-the-largest-express-car-wash-company-in-the-united-states/). The URL slug says "signs definitive agreement", but the page carries the closing release.
  - Model and count: "The newly combined company now operates 530 locations across 23 states, making it the largest express car wash company in the United States." — [same page](https://whistleexpresscarwash.com/news/whistle-express-signs-definitive-agreement-to-acquire-take-5-car-wash-creating-the-largest-express-car-wash-company-in-the-united-states/)
  - Take 5 purchase: "today announced the completion of the sale of its U.S. car wash business to Express Wash Operations, LLC dba Whistle Express Car Wash" — [Driven Brands, Form 8-K Ex. 99.1, filed 2025-04-16 (release dated April 10, 2025)](https://www.sec.gov/Archives/edgar/data/1804745/000180474525000036/a991drivenbrands_whistle.htm)
  - Affiliate: none found
  - BDC names: "Express Wash Operations, LLC", "Whistle Express Car Wash", "Magnolia Wash Holdings"
  - Notes:
    - Owner kind rests on Oaktree's own description (it invests in private equity among other things). The Form ADV check is the assembler's.
    - AMCO's stake is from 2023 and was not reconfirmed.
    - Whistle later sold 53 former Take 5 sites to Tsunami Express (CW16).
- **CW2 Mister Car Wash**
  - Owner: "As a result of the Merger, the Company became a wholly owned subsidiary of Parent, which is indirectly controlled by private investment funds affiliated with Leonard Green & Partners, L.P." — [Mister Car Wash, Form 8-K, filed 2026-05-19](https://www.sec.gov/Archives/edgar/data/1853513/000119312526229866/d128344d8k.htm)
  - Since: "On May 19, 2026, pursuant to that certain Agreement and Plan of Merger" — [same 8-K](https://www.sec.gov/Archives/edgar/data/1853513/000119312526229866/d128344d8k.htm)
  - Before the merger: LGP's funds "who on the date of the Merger Agreement collectively held approximately 67% of our common stock" — [Mister Car Wash, Form 10-K FY2025, filed 2026-02-27](https://www.sec.gov/Archives/edgar/data/1853513/000119312526078965/mcw-20251231.htm)
  - Count: "is the largest national car wash brand, with 548 locations in 21 states" — [same 10-K](https://www.sec.gov/Archives/edgar/data/1853513/000119312526078965/mcw-20251231.htm)
  - Model: "we operated 548 car washes in 21 states" — [same 10-K](https://www.sec.gov/Archives/edgar/data/1853513/000119312526078965/mcw-20251231.htm)
  - Delisting: EDGAR lists a Form 25-NSE (2026-05-19) and a Form 15-12G (2026-05-29) for CIK 1853513 ([submissions JSON](https://data.sec.gov/submissions/CIK0001853513.json)); the documents themselves were not opened.
  - Affiliate: none found
  - BDC names: "Mister Car Wash Holdings, Inc." (the "Borrower" in the 8-K), "Hotshine IntermediateCo, Inc.", "MCW Parent, LP"
  - Notes:
    - Form ADV (pilot §5): Leonard Green & Partners, L.P. (CRD 158164) reports `Any PE Funds = Y`.
    - In the pilot method, a public company that a PE fund controls counts as PE-owned. Mister now isn't public at all.
- **CW3 Quick Quack Car Wash**
  - Owner (control): "They listened carefully to our needs and structured an investment that helped us achieve three critical objectives: maintain our control of the business, provide liquidity to early investors, and provide growth capital." — [Seidler Equity Partners, Founder Story: Quick Quack Car Wash, accessed 2026-11-07](https://sepfunds.com/founder-story/quick-quack-car-wash/)
  - Stake kind: "Minority partnership" (page tile) — [same page](https://sepfunds.com/founder-story/quick-quack-car-wash/)
  - KKR: "Our recent strategic partnership with KKR, combined with our deep relationship with Seidler Equity Partners has made this dream a reality" — [Quick Quack blog, "Quick Quack Unveils New Ownership Program", 2024-10-16](https://www.quickquack.com/blog/quick-quack-unveils-new-ownership-program)
  - Since: KKR in 2024, per the blog's "recent strategic partnership". KKR's release ("Quick Quack Announces Strategic Investment by KKR") is at [media.kkr.com](https://media.kkr.com/rss-feed/news-release?news_id=eb966bf9-7758-4c39-91c8-f6ca38cb7dc3) but renders only with JavaScript, so its "significant minority" wording (seen in search snippets) is not quoted. Seidler's investment year was not found.
  - Model: not found
  - Affiliate: none found. The site footer has a customer "Refer-A-Friend" link, which is not an affiliate program.
  - BDC names: "Quick Quack Car Wash" (EDGAR full-text search hits in Golub Capital BDC filings)
  - Notes: Form ADV (pilot §5): KKR (CRD 144533) reports `Any PE Funds = Y`. Seidler is a PE firm by common description, but no page read here labels it, so the assembler's ADV check applies.
- **CW4 Tidal Wave Auto Spa**
  - Owner: "Golden Gate Capital, a leading private equity investment firm, and Tidal Wave Auto Spa Founder and CEO, Scott Blackstock, today announced the recapitalization of Tidal Wave" — [Golden Gate Capital news, 2020-12-30](https://goldengatecap.com/golden-gate-capital-partners-with-founder-and-ceo-scott-blackstock-on-recapitalization-of-tidal-wave-auto-spa/)
  - Founder stake: "Blackstock will continue to lead the Company as CEO and will remain a significant shareholder." — [same release](https://goldengatecap.com/golden-gate-capital-partners-with-founder-and-ceo-scott-blackstock-on-recapitalization-of-tidal-wave-auto-spa/)
  - Since: 2020-12-30 (release date)
  - Count and model: "Leading Conveyor Car Wash Company Reaches 338 Locations Across 30 States" (release dated October 29, 2026) and "Tidal Wave now operates 332 locations across" (September 17, 2026) — [Tidal Wave news page, accessed 2026-11-07](https://www.tidalwaveautospa.com/news/)
  - Affiliate: none found (the sitemap has a customer /refer-a-friend/ page)
  - BDC names: "Tidal Wave Auto Spa"
  - Notes:
    - No stake size is stated, so the row counts as PE-owned under the pilot's rule.
    - Current status is not reconfirmed. goldengatecap.com/portfolio loads its tiles with JavaScript, and the WordPress API exposes no portfolio type.
    - No later sale was found, and the company's 2026 releases don't name an owner.
- **CW5 Tommy's Express Car Wash**
  - Owner: "A Visionquest Company" (site footer) — [Tommy's Express, Franchise Opportunities page, accessed 2026-11-07](https://www.tommys-express.com/franchise)
  - Model: "Our franchise partners enjoy a great value for their 4% royalty and 1% brand fund fees." — [same page](https://www.tommys-express.com/franchise)
  - Since: not found
  - Affiliate: none found
  - BDC names: "Tommy's Express", "Tommy Car Wash Systems", "Visionquest"
  - Notes: no page read says who owns Visionquest. The /about URL returned 404 and the sitemap has no about page. 5 fetches.
- **CW6 Club Car Wash**
  - Owner: "its car wash platform – which includes Club Car Wash and Express Wash Concepts – has received a significant growth investment from Sculptor Real Estate" — [Wildcat Capital Management release, PR Newswire, 2023-10-16](https://www.prnewswire.com/news-releases/wildcat-capital-management-backed-car-wash-platform-receives-strategic-growth-investment-from-sculptor-real-estate-301956675.html)
  - Owner kind: "Wildcat was established in 2011 as a single-family investment office." — [same release](https://www.prnewswire.com/news-releases/wildcat-capital-management-backed-car-wash-platform-receives-strategic-growth-investment-from-sculptor-real-estate-301956675.html)
  - Since: Sculptor 2023-10-16; Wildcat's entry year not found
  - Model: not found. clubcarwash.com/about-us is a JavaScript-only ServiceNow page.
  - Affiliate: none found
  - BDC names: "Club Car Wash" (EDGAR full-text hits in HPS Corporate Lending Fund and MidCap Financial filings)
  - Notes:
    - The release names no stake for Sculptor, an "alternative asset management firm".
    - A tracker (lead only, not cited) mentions an April 2026 Wildcat continuation-vehicle process. No primary source was found.
    - Wildcat is a family office and may file no Form ADV.
- **CW7 ZIPS Car Wash**
  - Owner: "ZIPS emerges under the ownership of a group of its existing institutional investors, who are highly supportive of the Company’s go-forward strategy." — [ZIPS press, "successful restructuring", 2025-05-01](https://zipscarwash.com/press/successful-restructuring)
  - Since: "emerged from its chapter 11 process on April 30, 2025" — [same release](https://zipscarwash.com/press/successful-restructuring)
  - Model: "operating approximately 230 locations under three brands: ZIPS Car Wash, Rocket Express Car Wash, and Jet Brite Car Wash." — [same release](https://zipscarwash.com/press/successful-restructuring)
  - Affiliate: none found
  - BDC names: "Zips Car Wash, LLC" (EDGAR full-text hits in PennantPark Investment, PennantPark Floating Rate, HPS Corporate Lending Fund, Capital Southwest, Onex Direct Lending and MSC Income Fund filings)
  - Notes:
    - The release does not name the investor group.
    - The former sponsor (Atlantic Street Capital, per search results) is not named in any primary source read.
    - The BDC filings may show post-emergence equity positions; the assembler's DERA pass can test that.
- **CW8 Super Star Car Wash**
  - Owner: "today announced that it has signed a definitive agreement to acquire a majority stake in Super Star Car Wash" — [TSG Consumer Partners news, 2021-11-15](https://www.tsgconsumer.com/news/tsg-consumer-partners-to-acquire-super-star-car-wash/)
  - Owner kind: "a leading private equity firm" — [same release](https://www.tsgconsumer.com/news/tsg-consumer-partners-to-acquire-super-star-car-wash/)
  - Founder stake: "Following the transaction, Founder and President Reza Amirrezvani and the management team will remain significant investors and continue to lead the company." — [same release](https://www.tsgconsumer.com/news/tsg-consumer-partners-to-acquire-super-star-car-wash/)
  - Current: portfolio tile "Express car wash operator", "Investment Year 2021", "Status Current" — [TSG portfolio page, accessed 2026-11-07](https://www.tsgconsumer.com/portfolio/) (tile fields, not sentences)
  - Affiliate: none found
  - BDC names: "Super Star Car Wash" (EDGAR full-text hit in Carlyle Secured Lending)
  - Notes: Form ADV (pilot §5): TSG Consumer Partners LP (CRD 160826) reports `Any PE Funds = Y`.
- **CW9 GO Car Wash**
  - Owner and current status: "Investment Date 2019 – Fund VII Status Active" — [Imperial Capital, GO Car Wash investment page, accessed 2026-11-07](https://www.imperialcap.com/investments/go-car-wash)
  - Brand: "Headquartered in Denver, Colorado, GO Car Wash delivers superior washes" — [same page](https://www.imperialcap.com/investments/go-car-wash)
  - Owner kind: "Based in Toronto, we are a private equity firm with a focus on partnership opportunities in the U.S. and Canadian mid-market" — [Imperial Capital home page](https://www.imperialcap.com/)
  - Since: 2019
  - Model: not found
  - Affiliate: none found
  - BDC names: "GO Car Wash" (EDGAR full-text hits in MidCap Financial, Golub and Blackstone BDC filings)
  - Notes:
    - A December 2023 growth investment from a privately held firm appears in search results (not cited, stake not stated).
    - Imperial is Canadian, so it may not appear in the SEC adviser files.
- **CW10 WhiteWater Express Car Wash**
  - Owner: "WhiteWater Express Partners with Freeman Spogli & Co." (news item on the portfolio page) — [Freeman Spogli & Co., WhiteWater Express portfolio page, accessed 2026-11-07](https://www.freemanspogli.com/portfolio/whitewater-express/)
  - Since: "Investment Date December 2021" (page field) — [same page](https://www.freemanspogli.com/portfolio/whitewater-express/)
  - Model: not found
  - Affiliate: none found
  - BDC names: "WhiteWater Express" (EDGAR full-text hits in Bain Capital Specialty Finance and Bain Capital Private Credit)
  - Notes:
    - The FS&Co pages read carry no "private equity" self-label, and the meta description is "We partner with exceptional founders and management teams in the consumer and distribution sectors to build enduring businesses."
    - The portfolio page mixes current and realized companies (e.g. Petco, Boot Barn) with no status field, so current ownership is not separately confirmed.
    - whitewaterexpress.com is an unrelated rafting company.
- **CW11 ModWash**
  - Owner: not stated. "Founded by Karen Hutton and headquartered in Chattanooga, TN, ModWash has grown to more than 123 locations nationwide in just five years." — [ModWash LLC release, EIN Presswire, 2025-09-15](https://www.einpresswire.com/article/849360324/modwash-celebrates-grand-opening-in-maumee-oh-with-free-washes-and-community-fun)
  - Since: not applicable
  - Model: not found
  - Affiliate: none found
  - BDC names: "ModWash"
  - Notes: press coverage (not cited) says the Hutton real-estate company owns about 75% and a business-journal correction says ModWash is not PE-backed. No primary page states the split. 4 fetches and 2 searches.
- **CW12 Cobblestone Auto Spa / Cobblestone Car Wash**
  - Owner: "Founded in 2020, Spotless Brands is a portfolio company of Access Holdings." — [Spotless Brands home page, WebFetch, accessed 2026-11-07](https://www.spotlessbrands.com/)
  - Brand link: "including Flagship Carwash, Cobblestone Auto Spa, Cobblestone Car Wash, Ultimate Shine Car Wash, and Okie Express Auto Wash." — [same page, WebFetch](https://www.spotlessbrands.com/)
  - Since: "Cobblestone Auto Spa joined Spotless Brands in January 2020, bringing a strong foundation of 24 Phoenix locations" — [same page, WebFetch](https://www.spotlessbrands.com/)
  - Current: under "CURRENT PORTFOLIO": "Fast-growing express and flex car wash platform leveraging subscriptions and industry fragmentation to scale nationwide." — [Access Holdings, Investments page, accessed 2026-11-07](https://accessholdings.com/portfolio/investments/)
  - Owner kind: "Formed in 2013, Access Holdings is a research-led, data-driven investment firm" — [Access Holdings home page](https://www.accessholdings.com/)
  - Count: 119 location links on [cobblestone.com/locations/all-locations/](https://cobblestone.com/locations/all-locations/) (55 AZ, 49 CO, 14 ID, 1 OR). This is my tally, not a company figure, and the page also shows 9 "Coming Soon" labels.
  - Model: not found
  - Affiliate: none found
  - BDC names: "Spotless Brands" (EDGAR full-text hits in KKR, Carlyle, Golub and other BDC filings)
  - Notes:
    - spotlessbrands.com returns 403 to curl (robots.txt included), so the Spotless quotes came through WebFetch's summarizer and could not be mechanically checked.
    - Access's home page carries the headline "For private equity, that moment is now." but no self-label as a PE firm, so the ADV check is pending.
- **CW13 El Car Wash**
  - Owner: "today announced that Warburg Pincus has acquired the company from affiliates of Wafra Inc." — [El Car Wash press, "El Car Wash Announces Acquisition by Warburg Pincus", Published Aug 04, 2022](https://elcarwash.com/press/el-car-wash-announces-acquisition-by-warburg-pincus)
  - Owner kind: "Founded in 1966, Warburg Pincus has raised 21 private equity and 2 real estate funds" — [same release](https://elcarwash.com/press/el-car-wash-announces-acquisition-by-warburg-pincus)
  - Since: "Published Aug 04, 2022" — [same page](https://elcarwash.com/press/el-car-wash-announces-acquisition-by-warburg-pincus)
  - Model: "El Car Wash will assume ownership and operations of three locations" — [El Car Wash press, Splash Express release, 2026-03-26](https://elcarwash.com/press/el-car-wash-partners-with-splash-express-car-wash-expanding-central-florida-footprint)
  - Affiliate: none found
  - BDC names: "El Car Wash"
  - Notes:
    - warburgpincus.com returned 403.
    - El's 2026 releases carry no owner in their About text. The current status rests on the 2022 release, which is still on the company's press page, and no later sale was found.
- **CW14 Autobell Car Wash**
  - Owner: "This is the story of the Howard family’s love of clean and shiny cars." and the 2018 timeline entry "owner & CEO Chuck Howard" — [Autobell, Company History page, accessed 2026-11-07](https://www.autobell.com/autobell-car-wash-company-history/)
  - Since: not applicable (founded 1969)
  - Model: not found
  - Affiliate: none found
  - BDC names: "Autobell Car Wash, Inc."
  - Notes: the page renders with JavaScript (Gatsby). The text was read from [its page-data JSON](https://www.autobell.com/page-data/autobell-car-wash-company-history/page-data.json), where the ampersand is stored as `&amp;`. 6 fetches.
- **CW15 LUV Car Wash**
  - Owner: "Susquehanna Private Capital today announced that it is joining forces with seasoned industry leaders Darren Skarecky and JT Thomson to launch a nationwide express car wash platform" — [LUV Car Wash release, PR Newswire, 2021-11-15](https://www.prnewswire.com/news-releases/susquehanna-private-capital-teams-up-with-industry-veterans-to-launch-luv-car-wash-301423875.html)
  - Owner kind: "Susquehanna Private Capital was founded in 2016 and is funded by the founders of Susquehanna International Group, LLP" — [same release](https://www.prnewswire.com/news-releases/susquehanna-private-capital-teams-up-with-industry-veterans-to-launch-luv-car-wash-301423875.html)
  - Since: 2021-11-15
  - Model: not found
  - Affiliate: none found
  - BDC names: "LUV Car Wash"
  - Notes:
    - No stake is stated; SPC launched the company.
    - The boilerplate describes buying companies with "$3 million to $15 million in EBITDA" but uses no "private equity" label, so the ADV check is pending.
    - susquehannaprivatecapital.com serves a parked-domain robots.txt.
- **CW16 Tsunami Express Car Wash**
  - Owner: "Tsunami Express, backed by an affiliate of Point72 Private Investments" — [International Carwash Association news, reprint of the company release, 2025-09-12](https://www.carwash.org/car-wash-news/tsunami-express-car-wash-closes-acquisition-of-53-car-wash-locations-from-whistle-express)
  - Model and count: "With this acquisition, Tsunami Express grows its operations to 74 locations across 9 states" — [same page](https://www.carwash.org/car-wash-news/tsunami-express-car-wash-closes-acquisition-of-53-car-wash-locations-from-whistle-express)
  - Since: not found
  - Affiliate: none found
  - BDC names: "Tsunami Express Car Wash"
  - Notes:
    - The source is a trade-association reprint of the company's release; its original wire copy was not found.
    - tsunamiexpress.com names no owner.
    - Point72 Private Investments' own page now redirects to Point72 Ventures, so the ADV check is pending.
- **CW17 Splash Car Wash & Oil Change (Arkansas)**
  - Owner: "An Arkansas, family-owned business" — [Splash Car Wash home page (cleancarfast.com), accessed 2026-11-07](https://cleancarfast.com/)
  - Count: "See all 27 locations" — [same page](https://cleancarfast.com/)
  - Since: not applicable
  - Affiliate: none found
  - BDC names: "Splash Car Wash" (Arkansas)
  - Notes: the brand name collides with CW18 (an unrelated Northeast chain). Car Wash Advisory lists 80 sites (5 in development) against the company's own 27, which may count oil-change sites. If the company's own count is used, this brand falls out of the top 30.
- **CW18 Splash Car Wash (Northeast)**
  - Owner: "received a strategic majority investment from funds associated with AEA Investors" — [Splash Car Wash release, PR Newswire, 2025-04-25](https://www.prnewswire.com/news-releases/splash-car-wash-announces-aea-investors-has-acquired-majority-position-from-palladin-consumer-retail-partners-302438099.html)
  - Owner kind: "Small Business Private Equity strategy" — [same release](https://www.prnewswire.com/news-releases/splash-car-wash-announces-aea-investors-has-acquired-majority-position-from-palladin-consumer-retail-partners-302438099.html)
  - Model and count: "Splash is a premier car wash operator with over 65 locations across Connecticut" — [same release](https://www.prnewswire.com/news-releases/splash-car-wash-announces-aea-investors-has-acquired-majority-position-from-palladin-consumer-retail-partners-302438099.html)
  - Since: 2025-04-25 (release date); seller Palladin Consumer Retail Partners
  - Affiliate: none found
  - BDC names: "Splash Car Wash"
  - Notes: the pilot (§5) did not find AEA Investors by name in the ADV files.
- **CW19 Caliber Car Wash**
  - Owner: "today announced that it has signed a definitive agreement to acquire a majority stake in Caliber Car Wash" — [Percheron Capital media, 2021-12-16](https://percheron.com/media/percheron-capital-to-acquire-leading-express-wash-platform-caliber-car-wash/)
  - Owner kind: "a private equity firm focused on partnering with high-quality essential services businesses" — [same release](https://percheron.com/media/percheron-capital-to-acquire-leading-express-wash-platform-caliber-car-wash/)
  - Minority: Eagle Merchant Partners "will retain a minority interest in the company." — [same release](https://percheron.com/media/percheron-capital-to-acquire-leading-express-wash-platform-caliber-car-wash/)
  - Count: "With over 60 locations across Florida, Georgia, North Carolina, South Carolina, Alabama, and Texas" — [Caliber, About us, accessed 2026-11-07](https://calibercarwash.com/about-us/)
  - Since: 2021-12-16 (signing; closing date not found)
  - Model: not found
  - Affiliate: none found
  - BDC names: "Caliber Car Wash"
  - Notes: Percheron's portfolio tiles load with JavaScript, so current status is not reconfirmed. Caliber's site names no owner.
- **CW20 Crew Carwash**
  - Owner: "Still owned by the Dahm Family, Crew Carwash continues to grow and innovate" — [Crew Carwash, The Crew Story, accessed 2026-11-07](https://crewcarwash.com/the-crew-story/)
  - Since: not applicable
  - Model: not found
  - Affiliate: none found
  - BDC names: "Crew Carwash"
  - Notes: the site is a JavaScript (Vue) app, and the quote was read from the WordPress API ([pages?slug=the-crew-story](https://crewcarwash.com/wp-json/wp/v2/pages?slug=the-crew-story)). 5 fetches.
- **CW21 Clean Express Auto Wash**
  - Count: "The acquisition expands EWC's portfolio to 149 express car wash locations across six states, including 61 Clean Express Auto Wash locations" — [Express Wash Concepts release, PR Newswire, 2026-10-23](https://www.prnewswire.com/news-releases/express-wash-concepts-strengthens-pittsburgh-presence-with-acquisition-of-mt-pleasant-mach-1-express-wash-302918083.html)
  - Brand link: "Express Wash Concepts (EWC) operates 149 award-winning express car wash locations across six states under the following brands" — [same release](https://www.prnewswire.com/news-releases/express-wash-concepts-strengthens-pittsburgh-presence-with-acquisition-of-mt-pleasant-mach-1-express-wash-302918083.html)
  - Owner: EWC is part of Wildcat's platform, per the 2023 Wildcat release quoted in CW6 ("which includes Club Car Wash and Express Wash Concepts")
  - Since: not found
  - Affiliate: none found
  - BDC names: "Express Wash Concepts" (EDGAR full-text hits in Blackstone Private Credit Fund, HPS Corporate Lending Fund, FS KKR Capital and other filings)
  - Notes: EWC's 2026-10-09 release gives "147 ... including 63 Clean Express Auto Wash locations" ([PR Newswire](https://www.prnewswire.com/news-releases/express-wash-concepts-expands-metro-detroit-footprint-with-acquisition-of-three-cleanhub-car-wash-locations-302903522.html)); the later figure (61) is used. Neither 2026 release names an owner.
- **CW22 Golden Nozzle Car Wash**
  - Owner: "We've grown exponentially since becoming part of the nouria family" — [Golden Nozzle home page, accessed 2026-11-07](https://goldennozzlecarwash.com/)
  - Count: "60+ Locations in 5 States" — [same page](https://goldennozzlecarwash.com/)
  - Parent: "Nouria now operates 302 convenience stores and 90 car wash locations" and "Tony founded Nouria Energy Corporation in 1989" — [Nouria, About page](https://nouria.com/about/)
  - Since: not found
  - Model: not found
  - Affiliate: none found
  - BDC names: "Golden Nozzle", "Nouria Energy Corporation"
  - Notes: Nouria's page has a "The Nouria Family" heading and names its founder, but it never states who owns the company.
- **CW23 Splash In (ECO) Car Wash**
  - Owner: "Splash In is a subsidiary of The Wills Group, a family-owned and operated business with deep roots in the Mid-Atlantic region" — [Splash In, About page, accessed 2026-11-07](https://www.splashin.com/about-splash-in-car-wash)
  - Owner kind: "As a privately held company, our focus is on long-term growth" — [same page](https://www.splashin.com/about-splash-in-car-wash)
  - Count: "has grown to over 60 washes" — [same page](https://www.splashin.com/about-splash-in-car-wash)
  - Since: not applicable (founded 2007)
  - Affiliate: none found
  - BDC names: "Splash In", "The Wills Group"
- **CW24 Jax Kar Wash**
  - Owner and since: "Investment Year: 2022 Fund: TRP V" — [TRP Capital Partners, Jax portfolio page, accessed 2026-11-07](https://www.trpfund.com/jaxcarwash)
  - Model: "Description: Operator of car washes with a focus on the Southern Michigan market" — [same page](https://www.trpfund.com/jaxcarwash)
  - Owner kind: "We are a transportation sector-focused private equity fund" — [TRP Capital Partners home page](https://www.trpfund.com/)
  - Affiliate: none found
  - BDC names: "Jax Kar Wash"
  - Notes:
    - No stake is stated, and trade press (not cited) reports a majority.
    - "Jax" is also one of the 21 names in the MOJO Family of Brands list (Rollups). Whether that is the same chain was not checked, so the name may collide.
- **CW25 Big Dan's Car Wash**
  - Owner: not stated. "Shadday, taught us long ago that car washing isn’t just about washing cars" — [Big Dan's, About page, accessed 2026-11-07](https://www.bigdanscarwash.com/about-us/)
  - Count: "We’ve expanded our Big Dan’s Car Wash family to include 27 locations" — [same page](https://www.bigdanscarwash.com/about-us/)
  - Since: not applicable
  - Affiliate: none found
  - BDC names: "Big Dan's Car Wash"
  - Notes:
    - Car Wash Advisory's sponsor field (lead only) says "Shadday Family Office".
    - Car Wash Advisory counts 57 against the company's 27. If the company count is used, the brand falls out of the top 30.
    - Tidal Wave's sitemap has a "big-dans-columbia" page, and Tidal Wave announced a Columbia, SC acquisition on 2026-10-29. That may be a former Big Dan's site (not checked).
- **CW26 Champion Xpress Carwash**
  - Owner: not stated. "Built on faith. Run by family. Washed with care." — [Champion Xpress, About page, accessed 2026-11-07](https://champxpress.com/about/)
  - Since: "Champion Xpress Carwash was established in 2015 with roots in New Mexico" — [same page](https://champxpress.com/about/)
  - Affiliate: none found
  - BDC names: "Champion Xpress Carwash"
- **CW27 BlueWave Express**
  - Owner: "today announced that its controlled entity, Texas Express Wash LLC, closed the full acquisition of BlueWave Express" — [ClearWater Express Wash release, EIN Presswire, 2025-12-12](https://www.einpresswire.com/article/874717823/clearwater-express-wash-completes-acquisition-of-bluewave-express)
  - Since: "on November 26, 2025" — [same release](https://www.einpresswire.com/article/874717823/clearwater-express-wash-completes-acquisition-of-bluewave-express)
  - Count: "uniting ClearWater’s 30 locations with BlueWave’s 53 locations" — [same release](https://www.einpresswire.com/article/874717823/clearwater-express-wash-completes-acquisition-of-bluewave-express)
  - Owner kind: "Immediate creation of the largest privately owned express car wash operator in Texas" — [same release](https://www.einpresswire.com/article/874717823/clearwater-express-wash-completes-acquisition-of-bluewave-express)
  - Lender: "WhiteHorse Capital Provides Financing to Texas Express Wash" — [H.I.G. Capital news, 2026-01-12](https://hig.com/news/whitehorse-capital-provides-financing-to-texas-express-wash/)
  - Affiliate: none found
  - BDC names: "Texas Express Wash LLC", "ClearWater Express Wash", "BlueWave Express" (WhiteHorse Finance is a BDC)
  - Notes: the release says both brands' sites stay up ("visit clearwaterexpresswash.com or bluewaveexpress.com"). ClearWater's owners are not named.
- **CW28 Brown Bear Car Wash**
  - Owner: "We are proud to be family-owned." — [Brown Bear, Support (FAQ) page, accessed 2026-11-07](https://brownbear.com/support/)
  - Model: "Does Brown Bear Car Wash franchise? Not at this time." — [same page](https://brownbear.com/support/)
  - Since: not applicable (1957)
  - Affiliate: none found
  - BDC names: "Brown Bear Car Wash", "Car Wash Enterprises, Inc."
- **CW29 Flagship Carwash**
  - Owner: "Founded in 2020, Spotless Brands is a portfolio company of Access Holdings." — [Spotless Brands home page, WebFetch](https://www.spotlessbrands.com/); Access lists Spotless under "CURRENT PORTFOLIO" (see CW12)
  - Since: "Flagship Carwash joined Spotless Brands in August 2021" — [same page, WebFetch](https://www.spotlessbrands.com/)
  - Count: "Since joining Spotless Brands, Flagship has expanded its footprint to more than 50 locations" — [same page, WebFetch](https://www.spotlessbrands.com/)
  - Model: not found
  - Affiliate: none found
  - BDC names: "Spotless Brands", "Flagship Carwash Center"
- **CW30 Sam's Xpress Car Wash**
  - Owner: not found
  - Model: "Today, we proudly operate locations throughout North Carolina" — [Sam's Xpress, About page, accessed 2026-11-07](https://samsxpresscarwash.com/about/)
  - Affiliate: none found
  - BDC names: "Sam's Xpress Car Wash, LLC", "Sam's Holdings, LLC"
  - Notes: the About page names no owner. A LinkedIn page (not fetched; lead only) names an individual owner through Sam's Holdings, LLC.

### Rollups and groups that are not brands
Not counted in the 30. Each groups locations under several consumer-facing names.
- **MOJO Family of Brands (formerly Mammoth Holdings)**, 250 sites on Car Wash Advisory.
  - "The MOJO Family of Brands (formerly Mammoth Holdings) operates a growing network of express car washes across the United States." — [MOJO, transition announcement (undated; footer © 2025)](https://www.mojocarwash.com/mammoth-holdings-announces-transition-to-the-mojo-family-of-brands/)
  - Brands: "MOJO Family of Brands Include: Busy Bee, Coastal, Finish Line, In & Out, Jax, LuLu’s, Marc-1, MOJO, Mr. Squeaky, Pals, PitStop, PureMagic, Silverstar, Speedy Clean, SUDS, Swifty, The Wash, Today’s, Ultra, Wash Me Fast, and Wiggy Wash." (same page). The MOJO name itself has only about 4 location pages in the site's sitemap.
  - Owners:
    - "announced that it had completed an equity capital raise with CCMP Growth Advisors" ([Mammoth Holdings release, PR Newswire, 2023-01-17](https://www.prnewswire.com/news-releases/mammoth-holdings-raises-equity-capital-to-fuel-growth-301722456.html)).
    - Red Dog Equity, through Tom Pritzker's family business interests, "provides the equity for Mammoth Holdings' corporate development initiatives." (same release).
    - The same release says "Red Dog Equity LLC is a private equity firm that invests in lower middle-market companies". It calls CCMP Growth "a New York based growth-oriented private equity firm".
    - Stakes are not stated.
- **Spotless Brands**, 220 sites on Car Wash Advisory.
  - Brands: Flagship Carwash (CW29), Cobblestone Auto Spa and Cobblestone Car Wash (CW12), Ultimate Shine Car Wash (17 locations in 2022) and Okie Express Auto Wash (10 when it joined in 2020).
  - Owner: Access Holdings, current portfolio (see CW12).
- **Express Wash Concepts (EWC)**, 149 locations per its 2026-10-23 release.
  - Brands: Moo Moo Express Car Wash, Flying Ace Express Car Wash, Clean Express Auto Wash (CW21), Green Clean Express Auto Wash and Bee Clean Express Car Wash. Counts are stated only for Clean Express. The EWC brand portal is a JavaScript-only Salesforce site.
  - Owner: Wildcat Capital Management's car wash platform, with a Sculptor Real Estate growth investment in 2023 (see CW6).
- **Summit Wash Holdings**, 100 sites on Car Wash Advisory.
  - Owner: New Mountain Capital, from its portfolio page fields "Status Current", "Private Equity Flagship Control" and "Investment Date July 2022", plus "was initially formed through a partnership with Russell Speeder’s Car Wash" ([New Mountain Capital, Summit Wash Holdings page](https://www.newmountaincapital.com/portfolio/summit-wash-holdings/)).
  - Brands: Speeders / Russell Speeder's and Waters Car Wash (logos on [summitwashholdings.com](https://summitwashholdings.com/), WebFetch only, because curl got 403). Brand counts were not found.
- **Wildcat Capital Management's car wash platform**: the group over Club Car Wash (CW6) and EWC (CW21). It is a family-office holding, not a consumer name.
- **Other parents named in rows** (companies, not car wash rollups): Visionquest (Tommy's), Nouria (Golden Nozzle), The Wills Group (Splash In), ClearWater Express Wash (BlueWave; also a ~30-site brand below the cutoff), Car Wash Enterprises, Inc. (Brown Bear).
- **Gone from the list:** Take 5 Car Wash. Driven Brands sold its U.S. car wash business to Whistle on 2025-04-10 (CW1).

### Category share
N = 30 (composite above). Counts by brand row unless stated.
- **PE-owned (control, or a PE owner with no stated stake), owner labeled PE in a source read or by the pilot's ADV pass: 9 / 30 = 30.0%.**
  - The rows: Whistle (Oaktree), Mister (LGP), Tidal Wave (Golden Gate), Super Star (TSG), GO (Imperial), El (Warburg Pincus), Splash Northeast (AEA SBPE), Caliber (Percheron), Jax (TRP).
  - 3 of these rest on deal releases from 2020–2022 with no current confirmation: Tidal Wave, El and Caliber.
- **PE minority stake: 1 / 30 = 3.3%.** Quick Quack: KKR and Seidler hold minorities, and the founders keep control.
- **PE-owned plus PE minority stake: 10 / 30 = 33.3%.**
- **Investment-firm control, PE label not in sources read (Form ADV check pending): 5 / 30 = 16.7%.**
  - The rows: WhiteWater (Freeman Spogli & Co.), Cobblestone and Flagship (Access Holdings), LUV (Susquehanna Private Capital), Tsunami (Point72 Private Investments affiliate).
  - If all five pass, PE-owned plus minority = **15 / 30 = 50.0%**.
- **Family-office platform with an asset-manager investor of unstated stake: 2 / 30 = 6.7%.**
  - The rows: Club Car Wash and Clean Express Auto Wash (Wildcat; Sculptor Real Estate).
  - Upper bound if these counted: 17 / 30 = 56.7%.
- **Public company: 0 / 30.** The strict count therefore equals the counts above.
- **Lender-owned: 1 / 30 = 3.3%** (ZIPS, after Chapter 11).
- **Family: 5 / 30 = 16.7%**: Autobell, Splash Car Wash & Oil Change (AR), Crew, Splash In (Wills Group), Brown Bear.
- **Private, owner not stated, no PE evidence found: 6 / 30 = 20.0%**: Tommy's Express (Visionquest), ModWash, Golden Nozzle (Nouria), Big Dan's, Champion Xpress, BlueWave (ClearWater).
- **Not found: 1 / 30 = 3.3%**: Sam's Xpress.
- **By parent company** (28 parents; Wildcat and Access each count once):
  - PE-owned plus minority: 10 / 28 = 35.7%.
  - With the ADV-pending owners: 14 / 28 = 50.0%.
  - With Wildcat: 15 / 28 = 53.6%.
- **By locations** (ranking counts, 4,472 sites across the 30 rows; sales were not available):
  - PE-owned 2,052 (45.9%).
  - Plus minority (Quick Quack): 2,417 (54.0%).
  - Plus ADV-pending: 2,900 (64.8%).
  - Plus Wildcat: 3,241 (72.5%).
- **Sources disagree:**
  - On owners: none among the primary sources read.
  - On counts:
    - Mister: 518 on Car Wash Advisory vs 548 in its 10-K.
    - Tsunami: 83 vs 74 (2025 release).
    - Splash (AR): 80 vs 27 on its own site.
    - Big Dan's: 57 vs 27 on its own site.
    - Mr. Clean (#31): 49 vs 19 on its own site.
    - Clean Express: 63 vs 61 in two EWC releases two weeks apart.
  - The ranking source counts sites in development, which explains part of the gap.

### Firms named
Every investment firm named as an owner, investor or 5%+ holder, as the sources name it, for the assembler's Form ADV pass:
- **Control owners:**
  - Leonard Green & Partners, L.P. (Mister; pilot ADV: CRD 158164, Y)
  - Oaktree Capital Management, L.P. (Whistle)
  - Golden Gate Capital (Tidal Wave)
  - TSG Consumer Partners (Super Star; pilot ADV: CRD 160826, Y)
  - Imperial Capital (GO; Toronto)
  - Freeman Spogli & Co. (WhiteWater)
  - Access Holdings (Spotless: Cobblestone, Flagship)
  - Warburg Pincus (El)
  - Susquehanna Private Capital (LUV)
  - Point72 Private Investments (Tsunami, "an affiliate of")
  - AEA Investors, Small Business Private Equity strategy (Splash Northeast; pilot found no AEA match by name)
  - Percheron Capital (Caliber)
  - TRP Capital Partners (Jax)
  - Wildcat Capital Management (Club, EWC; single-family office)
- **Minority or no-stated-stake investors:**
  - KKR (Quick Quack; pilot ADV: CRD 144533, Y)
  - Seidler Equity Partners (Quick Quack)
  - A&M Capital Opportunities Fund ("AMCO"), part of Alvarez & Marsal Capital (Whistle, 2023)
  - Eagle Merchant Partners (Caliber, 2021)
  - Sculptor Real Estate / Sculptor Capital Management, Inc. (Wildcat platform, 2023)
- **Rollup owners (not counted rows):** CCMP Growth Advisors, LP and Red Dog Equity LLC with The Pritzker Organization (MOJO/Mammoth); New Mountain Capital (Summit Wash).
- **Former owners and sellers named:** Palladin Consumer Retail Partners, LLC (Splash Northeast, sold 2025); Wafra Inc., Audrose Partners, Fireside Investments (El, sold 2022); Driven Brands Holdings Inc. (Take 5 Car Wash, sold 2025).
- **Lender, not owner:** WhiteHorse Capital (H.I.G.) for ClearWater/BlueWave.

### BDC leads for the assembler
These are EDGAR full-text search hits (2023-01-01 to 2026-11-07), not verified holding rows:

| Name searched | Total hits | BDC and credit-fund filers named |
|---|---|---|
| Quick Quack | 248 | Golub Capital BDC family, Cliffwater, StepStone |
| Spotless Brands | 561 | KKR, Carlyle, Golub, T Series, Phillip Street |
| Mammoth Holdings | 191 | First Eagle, OHA, Morgan Stanley Direct Lending, Monroe Capital, Cliffwater |
| Zips Car Wash | 242 | PennantPark, HPS, Capital Southwest, Onex, MSC Income |
| GO Car Wash | 217 | MidCap/Apollo, Golub, Blackstone Secured Lending, Blackstone Private Credit |
| Club Car Wash | 119 | HPS, MidCap/Apollo, Partners Group, iDirect |
| Express Wash Concepts | 84 | Blackstone Private Credit, HPS, Cliffwater, 5C, SLR, FS KKR |
| WhiteWater Express | 35 | Bain Capital Specialty Finance, Bain Capital Private Credit |
| Super Star Car Wash | 20 | Carlyle Secured Lending |
| Summit Wash | 9 | New Mountain Private Credit Fund |

- ClearWater/BlueWave borrows from WhiteHorse Capital (H.I.G.'s credit arm, whose BDC is WhiteHorse Finance).
- Mister Car Wash's borrower is "Mister Car Wash Holdings, Inc." under a Jefferies-agented first-lien facility. Its BDC presence was not searched.

### Worker log (car washes)
- **Time:** 2026-11-07T16:35:14Z to 2026-11-07T17:11Z, about 36 minutes, including writing and the quote self-check.
- **Calls:**
  - WebSearch: 32.
  - WebFetch: 8, of which 5 returned usable text (Spotless ×2, Mammoth, Cobblestone, Summit) and 3 failed (carwash.com 403, expresswashconcepts.com redirect to a portal, brownbear.com/about-us 404).
  - curl: 203 requests: 185 × 200, 11 × 404, 5 × 403, 2 × no response.
  - **SEC: 19 requests** to www.sec.gov, efts.sec.gov and data.sec.gov (14 full-text searches, 1 submissions JSON, 4 documents), all HTTP 200, under the contact-free user agent `EvidenceEngine ownership-research bot (category audit)` with at least 0.6 s between requests.
  - Agent tokens were not metered.
- **What was cheap:**
  - EDGAR full-text search. One pass over 14 names gave every BDC lead and surfaced Mister Car Wash's 2026 take-private: an SC 13E3 hit under "Whistle Express" led to the 8-K.
  - Sponsor pages with server-rendered fields: TSG (status "Current"), Imperial ("Status Active"), New Mountain ("Status Current"), TRP, Access ("CURRENT PORTFOLIO" section).
  - Company releases on PR Newswire, which loads without JavaScript.
- **What made brands slow** (5–6 fetches each):
  - Sponsor pages that render tiles with JavaScript or lack a status field: Golden Gate, Percheron, Freeman Spogli and KKR's media site. Current status for Tidal Wave, Caliber and WhiteWater rests on 2020–2021 deal releases or a status-less portfolio page.
  - Company sites built as JavaScript apps: Autobell (Gatsby; read via page-data JSON), Crew (Vue; read via the WordPress API), Club Car Wash (ServiceNow), the EWC portal (Salesforce), Quick Quack's newsroom.
  - Ranking-source counts that disagree with brands' own counts.
  - Rollup brands with no stated per-brand counts (EWC, MOJO, Summit). Placing them took extra fetches and left the 25–30 band uncertain.
  - 403s to curl: spotlessbrands.com, summitwashholdings.com, warburgpincus.com.
- **Which kinds of brands had no primary source for the owner:**
  - Founder- or family-run regional chains whose sites tell the founder story but never say who owns the company: Big Dan's, Champion Xpress, ModWash, Sam's Xpress.
  - Private parents that are themselves unowned on paper: Visionquest (Tommy's), Nouria (Golden Nozzle), ClearWater (BlueWave).
  - The lender group that took ZIPS out of bankruptcy, whose members the company does not name.
- **Robots and etiquette:**
  - carwash.com disallows ClaudeBot and anthropic-ai and was not curled (one WebFetch got 403). kget.com disallows anthropic-ai and was not fetched.
  - Several sites set `Crawl-delay: 10`. On goldengatecap.com, cobblestone.com, accessholdings.com and crewcarwash.com the delay was kept between page requests. On modwash.com and nouria.com two page requests were 1–2 s apart, and on several sites the first page request followed the robots.txt request within a second. These are minor lapses.
- **Competitor and paywalled sites:** none opened. PitchBook, Crunchbase and CB Insights results appeared in searches and were not opened. Car Wash Advisory's company pages were opened only for sponsor and website leads, and no fact here rests on them.
- **Affiliate:** one category-wide search plus brand-site browsing during owner checks. No brand-direct affiliate program was found, and none of the top-30 sites links to one. Customer refer-a-friend programs exist (Quick Quack, Tidal Wave), but they pay members, not publishers. On the evidence seen, car washes look like a near-zero affiliate category.
- **Quote-check caveats for the assembler:**
  - The Spotless Brands quotes (CW12, CW29) and Summit Wash logo names come through WebFetch's summarizer. curl gets 403 there, so a curl-based re-check will fail for reasons unrelated to the quotes.
  - Autobell (CW14) and Crew (CW20) quotes match the JSON endpoints named in their rows, not the HTML pages, which render with JavaScript.
  - Portfolio-tile fields (TSG, Imperial, FS&Co, TRP, New Mountain) are field values, not sentences.
  - My text extraction inserts a space where an inline tag ends (e.g. "Connecticut , Massachusetts"). Quotes were chosen to avoid those spots.
