# Research: Category audit — dollar and discount stores

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (UTC) · Method copied from [category-audit-pilot.md](../category-audit-pilot.md). Ownership facts come from primary sources only. Trade press supplies the ranking only.

**Short answer**

| | Dollar, discount variety and closeout (rows 1–13) | All rows, with off-price added (rows 1–25) |
|---|---|---|
| PE-owned plus PE minority stake (confirmed) | **0 / 13 (0.0%)** | **0 / 25 (0.0%)** |
| Owned by investment firms whose PE status waits on Form ADV | 1 / 13 (7.7%): Family Dollar (Brigade, Macellum) | 2 / 25 (8.0%): Family Dollar, and Gabe's (lender group led by Brigade, Arbour Lane, Anchorage) |
| Upper bound if the assembler's Form ADV check flags those firms | 1 / 13 (7.7%); 14.5% of the known core sales | 2 / 25 (8.0%) |
| Strict count upper bound (public company with a 5%+ holder whose ADV might report PE funds; see "Category share") | 3 / 13 (23.1%) | 6 / 25 (24.0%) |
| Owner not found / owner type not confirmed | 5 (Big Lots!, Roses, Maxway, Ocean State Job Lot, Daiso) | 5 |
| Brand-direct affiliate programs | none found | none found (Nordstrom Rack is on network listings only, unverified) |

- **Fewer than 30 national chains exist.** The dollar, discount-variety and closeout segment has 13 operating national or large regional brands. Five more chains closed in 2023–2025, and three of those were PE-owned at some point (see "Closed or excluded chains"). To reach a list near 30, I added the 12 US off-price brands as a second block (rows 14–25), and I report every share both ways.
- **The PE story here is mostly about 2025 deals, not long-held positions.** Family Dollar was sold by Dollar Tree to Brigade and Macellum (closed 2025-07-05). Gabe's passed from Warburg Pincus (lead) to a lender group led by Brigade (closed 2025-08-25). Brigade sits in both chains. Neither buyer calls itself private equity in the sources read. Brigade calls itself "a global asset management firm" and "a leading independent alternative asset manager". Only NRF (trade press) calls the Family Dollar buyers "private equity".
- **Former PE owners of today's public chains:** Dollar General (KKR, exited 2013) and Burlington (Bain Capital, 2006 acquisition). Ollie's has a CCMP managing director as lead independent director, but CCMP holds no 5%+ stake.

## How this was sourced (read first)

- **Ranking:** NRF 2026 Top 100 Retailers (compiled by Kantar), trade-association list, used for the ranking only. Below its cutoff I ranked brands by the store count in their own filing, release or site. See "Ranking".
- **Ownership facts:** SEC filings (10-K, DEF 14A, 8-K, 20-F), company sites and company press releases. Two rows rest on less direct pages, and each is flagged in its notes:
  - Gabe's: a law-firm release (Debevoise & Plimpton), because the company's Business Wire release returns 403.
  - Variety Wholesalers: its owners' family foundation history page.
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist, Private Equity Vet, PitchBook, Preqin and CB Insights. A CB Insights result came up in searches and was not opened.
- **Leads only, never cited:** mergr, privateequityinfo and dealroom (deal directories), Wikipedia and its mirrors, and FlexOffers, UpPromote and LinkClicky (affiliate-network listings).
- **SEC access:**
  - User agent: every SEC request (www.sec.gov, efts.sec.gov, data.sec.gov) used `EvidenceEngine ownership-research bot (category audit)`, which carries no email or other contact detail.
  - Results: all 38 SEC requests were served HTTP 200.
  - Rate: one request per 0.6 s or slower.
- **Robots:** I read robots.txt before the first curl to each new site.
  - Ocean State Job Lot sets `Crawl-delay: 5`, so its fetches were spaced 5 s apart.
  - fivebelow.com served a Cloudflare challenge (403) even for robots.txt, so I fetched nothing else there.
  - One robots.txt (daisous.com) contained instructions addressed to AI agents, and one search result contained text aimed at an AI. Both were treated as page data and ignored.
- **Quote self-check:** all 76 quotes below were string-matched with a script against the text of the pages I downloaded (tags stripped, whitespace collapsed, case-sensitive, curly quotes kept), and 76 of 76 were found.
  - One quote sits in an HTML `<meta name="description">` tag rather than visible text: Bealls (DS19).
  - One quote comes from an icon label ("660+ Stores", DS19).
- **Owner kinds are research notes for a human, not engine classifications** (ADR 0001 governs the product). "PE-owned" means control, or a PE owner with no stated stake. Counts are by brand row: TJX is 5 rows, Variety Wholesalers 3 and Ross Stores 2.

## Dollar and discount stores

**Ranking:** No free ranking lists the top 30 US dollar and discount brands, so this is a composite, built the way the pilot built gyms.
- **(a) NRF top 100.** Rows ranked by 2025 US retail sales come from the National Retail Federation, "NRF Top 100 Retailers 2026 List", compiled by Kantar, published 2026-07-01 (page `datePublished`): https://nrf.com/research-insights/top-retailers/top-100-retailers/top-100-retailers-2026-list.
  - What it ranks by: the page says it "ranks the industry’s largest companies according to sales". Its columns are "2025 USA retail sales (billions)".
  - In-scope entries: Dollar General #17 ($43.13B), Dollar Tree #29 ($18.93B), Family Dollar #43 ($11.91B) and Five Below #89 ($4.76B).
  - Off-price entries: TJX Companies #15 ($46.30B, all TJX US banners), Ross Stores #22 ($22.70B), Nordstrom #33 ($14.90B, full-line and Rack together) and Burlington #45 ($11.48B).
  - NRF has no segment column, so it does not group off-price with discount stores.
- **(b) Below NRF's cutoff,** brands are ordered by the US store count stated in their own 10-K, release or site, cited in Evidence. Where no count was found, the brand is placed last in its block and marked "count not found".
- **Rejected ranking:** ScrapeHero, "The Largest Discount Stores in the US" (https://www.scrapehero.com/largest-discount-stores-in-us/, "Last Updated: March 9, 2026"). Its store counts date from 2020 (Dollar General 16,952), so it was not used. It is the only ranking found that groups off-price (TJ Maxx) with dollar stores, and it also groups in warehouse clubs.

**Scope, as built:**
- **Rows 1–13 (core):** dollar stores, discount-variety stores and general-merchandise closeout chains.
- **Rows 14–25 (added):** off-price apparel and home chains. They are added because the core has only 13 operating brands and because the one grouping source (ScrapeHero) puts TJ Maxx with discount stores. The developer can read either block's share alone.
- **Excluded:**
  - discount grocers: Aldi, Save-A-Lot, Grocery Outlet (NRF #91), Marc's;
  - supercenters and warehouse clubs: Walmart, Target, Meijer, Costco, Sam's Club, BJ's;
  - thrift stores;
  - footwear off-pricers: DSW, Rack Room, Off Broadway;
  - closed chains, listed below.
- **Not exhaustive below about 100 stores.** Small regional off-pricers (for example Hamrick's and Forman Mills) were not checked.

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dollar General | Dollar General Corporation | public company (formerly PE-owned: KKR, exited Dec 2013) | none at 5%+ (Vanguard 11.4%, BlackRock 6.9%, State Street 5.0%) | not checked (brand native to parent) | DG (NYSE) | company-operated (20,959 stores incl. 17 in Mexico) | none found (homepage) | DS1 |
| 2 | Dollar Tree | Dollar Tree, Inc. | public company; 5%+ activist holder | none controlling; Mantle Ridge LP 7.0% (ADV not checked) | not checked | DLTR (Nasdaq) | company-operated (~9,000 US stores) | not checked (homepage returned an error page to curl) | DS2 |
| 3 | Family Dollar | 1959 Holdings, LLC, the vehicle through which Brigade Capital Management and Macellum Capital Management "partner to acquire" Family Dollar | investment-firm owned; PE status not confirmed (Brigade: "alternative asset manager"; Macellum: "investment firm"; NRF, trade press only, says "private equity") | Brigade Capital Management, LP; Macellum Capital Management, LLC | 2025-07-05 | — | not found (company-operated per 10-K history, not re-sourced) | none found (familydollar.com has no about page) | DS3 |
| 4 | Five Below | Five Below, Inc. | public company | none at 5%+ (BlackRock 9.0%) | not checked | FIVE (Nasdaq) | company-operated (1,921 stores) | blocked (Cloudflare 403) | DS4 |
| 5 | Ollie's Bargain Outlet | Ollie's Bargain Outlet Holdings, Inc. | public company | none confirmed (FMR 12.24%, BlackRock 8.72%, Kayne Anderson Rudnick 6.06%, Summit Trail Advisors 5.62%, Vanguard Capital Mgmt 5.28%); a CCMP managing director is lead independent director | not checked | OLLI (Nasdaq) | company-operated (645 stores) | none found (homepage) | DS5 |
| 6 | Big Lots! | Variety Wholesalers, Inc. (stores bought out of the Big Lots, Inc. bankruptcy via Gordon Brothers) | Owner type not confirmed (Variety is private; family business per its owners' foundation, with no current ownership statement) | none found | 2025-01-03 (sale to Gordon Brothers closed, enabling Variety's purchase) | — | company-operated (219 stores) | none found (homepage) | DS6 |
| 7 | Ocean State Job Lot | Ocean State Job Lot, "privately held" (owner not named) | Owner type not confirmed | none named | n/a (founded 1977) | — | 177 stores, 11 states | none found (homepage) | DS7 |
| 8 | Roses (incl. Roses Express) | Variety Wholesalers, Inc. | Owner type not confirmed (as row 6) | none found | not found (lead: 1997, secondary sources) | — | count not stated (Variety: "more than 400 stores" incl. 219 Big Lots!) | none found (homepage) | DS8 |
| 9 | Maxway | Variety Wholesalers, Inc. | Owner type not confirmed (as row 6) | none found | not found | — | count not stated | not checked (no own site found) | DS9 |
| 10 | pOpshelf | Dollar General Corporation | public company (DG format) | none (as row 1) | 2020 (launched) | DG (NYSE) | company-operated; expansion paused 2025; 45 closed Q1 2025; count not stated | none found (DG homepage) | DS10 |
| 11 | Daiso (US) | Daiso USA LLC (site operator and trademark holder); parent not confirmed | Owner type not confirmed (lead: Daiso Industries, Japan) | not found | not found | — | count not found | none found (about page) | DS11 |
| 12 | MINISO (US) | MINISO Group Holding Ltd | public company, founder-controlled (Guofu Ye 63.7% with Yunyun Yang) | none (Norges Bank 5.0%) | n/a | MNSO (NYSE), 9896 (HKEX) | directly operated in North America; US count not stated in 20-F | not checked | DS12 |
| 13 | Bi-Mart | Bi-Mart, "owned by its employees since 2004" | other: employee-owned | none | 2004 | — | membership discount stores in OR, WA, ID; count not stated | none found (homepage) | DS13 |
| 14 | T.J. Maxx (off-price) | The TJX Companies, Inc. | public company | none at 5%+ (BlackRock 8.9%, Vanguard 8.44%) | 1976 (founded by TJX) | TJX (NYSE) | company-operated (2,603 TJ Maxx + Marshalls) | not checked (site error page to curl) | DS14 |
| 15 | Marshalls (off-price) | The TJX Companies, Inc. | public company | none at 5%+ | 1995 (acquired by TJX) | TJX (NYSE) | company-operated (in the 2,603 above) | not checked (site error page) | DS15 |
| 16 | Ross Dress for Less (off-price) | Ross Stores, Inc. | public company | none at 5%+ (Vanguard 12.2%, BlackRock 7.0%) | not checked | ROST (Nasdaq) | company-operated (1,904 stores) | none found (homepage) | DS16 |
| 17 | Burlington (off-price) | Burlington Stores, Inc. | public company (formerly PE-owned: Bain Capital, 2006 acquisition) | none confirmed (Capital International 13.9%, JPMorgan Chase 10.8%, BlackRock 10.3%, Vanguard 10.2%) | not checked | BURL (NYSE) | company-operated (1,212 stores) | none found (homepage) | DS17 |
| 18 | HomeGoods (off-price) | The TJX Companies, Inc. | public company | none at 5%+ | 1992 (introduced) | TJX (NYSE) | company-operated (963 stores) | none found (homepage) | DS18 |
| 19 | bealls (off-price; ex-Bealls Outlet and Burkes Outlet) | Bealls, Inc., "still owned by the founding family" | family | none | n/a (founded 1915) | — | 660+ stores (all Bealls, Inc. banners) | none found (homepage) | DS19 |
| 20 | Citi Trends (off-price) | Citi Trends, Inc. | public company; 31.1% holder (Fund 1 Investments, LLC) | Fund 1 Investments / Pleasant Lake Partners 31.1%; Divisadero Street Capital 5.7%; Shay Capital 5.1% (ADV not checked) | not checked | CTRN (Nasdaq) | company-operated (590 stores) | none found (homepage) | DS20 |
| 21 | dd's DISCOUNTS (off-price) | Ross Stores, Inc. | public company | none at 5%+ | not checked | ROST (Nasdaq) | company-operated (363 stores) | not checked | DS21 |
| 22 | Nordstrom Rack (off-price) | Nordstrom Holdings, Inc., formed by the Nordstrom family group and El Puerto de Liverpool | other: family plus foreign public company (no PE) | none | 2025-05-20 (take-private) | — (delisted; Liverpool is listed in Mexico) | company-operated (277 stores at 2025-02-01) | network listings only (FlexOffers and others), unverified; no brand-direct page found | DS22 |
| 23 | Gabe's (off-price) | ad hoc lender group (Brigade Capital Management, Arbour Lane Capital Management, Anchorage Capital Advisors) are "now the majority owners" | lender-owned (credit funds); PE status not confirmed; formerly PE-owned (Warburg Pincus, lead) | Brigade, Arbour Lane, Anchorage (lender group); Warburg Pincus before 2025 (lead) | 2025-08-25 | — | "more than 150 stores" (Debevoise) / "more than 140" incl. Old Time Pottery (company site) | none found (about page) | DS23 |
| 24 | Sierra (off-price) | The TJX Companies, Inc. | public company | none at 5%+ | 2012 (acquired) | TJX (NYSE) | company-operated (145 stores) | not checked (site error page) | DS24 |
| 25 | Homesense (off-price) | The TJX Companies, Inc. | public company | none at 5%+ | 2017 (US launch) | TJX (NYSE) | company-operated (79 US stores) | not checked | DS25 |

### Evidence
- **DS1 Dollar General**
  - Owner: "Our common stock is traded on the New York Stock Exchange under the symbol “DG.”" — [Dollar General Corp, Form 10-K FY2025, filed 2026-03-20](https://www.sec.gov/Archives/edgar/data/29534/000110465926032325/dg-20260130x10k.htm)
  - Former PE owner: "In November 2009 our common stock again became publicly traded on the New York Stock Exchange under the symbol “DG”, and in December 2013 the entity controlled by investment funds affiliated with KKR sold its remaining shares of our common stock." — [same 10-K](https://www.sec.gov/Archives/edgar/data/29534/000110465926032325/dg-20260130x10k.htm)
  - Since: not checked (brand native to the listed parent)
  - Model: "As of February 27, 2026, we operated 20,959 retail stores, including those located in 48 U.S. states as listed in the table below and 17 stores in Mexico." — [same 10-K](https://www.sec.gov/Archives/edgar/data/29534/000110465926032325/dg-20260130x10k.htm)
  - 5% holders: "The following table pertains to shareholders known to us on March 19, 2026, to beneficially own more than 5% of our common stock." — [Dollar General, DEF 14A, filed 2026-04-07](https://www.sec.gov/Archives/edgar/data/29534/000110465926040394/tm261322-1_def14a.htm) (table lists The Vanguard Group 11.4%, BlackRock 6.9%, State Street 5.0%)
  - Affiliate: none found (no affiliate link on the dollargeneral.com homepage)
  - BDC names: "Dollar General Corporation"
- **DS2 Dollar Tree**
  - Owner: "Our common stock is traded on The Nasdaq Global Select Market ® under the symbol “DLTR.”" — [Dollar Tree, Inc., Form 10-K FY2025, filed 2026-03-16](https://www.sec.gov/Archives/edgar/data/935703/000093570326000025/dltr-20260131.htm)
  - Model: "We are a leading operator of retail discount stores operating under the brand names of Dollar Tree and Dollar Tree Canada. At January 31, 2026, we operated approximately 9,000 stores across 48 states and the District of Columbia and approximately 275 stores across seven Canadian provinces." — [same 10-K](https://www.sec.gov/Archives/edgar/data/935703/000093570326000025/dltr-20260131.htm)
  - 5% holders: "Mantle Ridge LP 712 Fifth Ave., Suite 17F New York, New York 10019 13,640,904 (18) 7.0%" — [Dollar Tree, DEF 14A, filed 2026-05-01](https://www.sec.gov/Archives/edgar/data/935703/000110465926053500/tm261374-1_def14a.htm). The same table lists The Vanguard Group 12.2%, FMR LLC 8.3% and BlackRock 7.9%. Director Paul C. Hilal is shown with 7.0%, which overlaps Mantle Ridge's shares.
  - Since: not checked
  - Affiliate: not checked (dollartree.com returned a near-empty page to curl)
  - BDC names: "Dollar Tree, Inc.", "Dollar Tree Stores, Inc."
  - Notes: Mantle Ridge is an activist holder, not a controller. Its Form ADV `Any PE Funds` value decides the strict count.
- **DS3 Family Dollar**
  - Owner: "Dollar Tree, Inc. (NASDAQ: DLTR) today announced that the Company has reached an agreement under which Brigade Capital Management, LP (“Brigade”) and Macellum Capital Management, LLC (“Macellum”) will partner to acquire the Company’s Family Dollar business segment." — [Dollar Tree press release, March 26, 2025, Form 8-K Ex. 99.2, filed 2025-03-26](https://www.sec.gov/Archives/edgar/data/935703/000093570325000012/ex992dollartreepressreleas.htm)
  - Buyer entity: "On July 5, 2025, Dollar Tree, Inc. (the “Company”) completed its previously announced sale of all of the issued and outstanding membership interests of Family Dollar Stores, LLC, a Delaware limited liability company (“Family Dollar”) to 1959 Holdings, LLC, a Delaware limited liability company (the “Buyer”)" — [Dollar Tree, Form 8-K (Item 2.01), filed 2025-07-07](https://www.sec.gov/Archives/edgar/data/935703/000093570325000038/dltr-20250705.htm)
  - Brigade's tie to the Buyer: "In connection with the execution of the Purchase Agreement, Brigade Capital Management, LP, a Delaware limited partnership, delivered a limited guarantee in favor of Seller guaranteeing the payment of such termination fee and certain other fees, costs and expenses of Seller." — [Dollar Tree, Form 8-K (Item 1.01), filed 2025-03-28](https://www.sec.gov/Archives/edgar/data/935703/000110465925029393/tm2510014d2_8k.htm)
  - Owner kind (Brigade): "Brigade Capital Management is a global asset management firm founded in 2006 with over $27 billion in assets under management." and "As an SEC registered investment advisor, Brigade is a leading independent alternative asset manager with a 48-person investment team." — [Dollar Tree press release, March 26, 2025](https://www.sec.gov/Archives/edgar/data/935703/000093570325000012/ex992dollartreepressreleas.htm)
  - Owner kind (Macellum): "Macellum Capital Management is an investment firm founded in 2009 that invests in undervalued companies that it believes can appreciate significantly in value through changes in strategy, capital allocation and improvements in operations." — [same release](https://www.sec.gov/Archives/edgar/data/935703/000093570325000012/ex992dollartreepressreleas.htm)
  - Current (as of the FY2025 10-K): "On July 5, 2025, we completed our previously announced sale of the Family Dollar business to 1959 Holdings, LLC." — [Dollar Tree, Form 10-K FY2025, filed 2026-03-16](https://www.sec.gov/Archives/edgar/data/935703/000093570326000025/dltr-20260131.htm)
  - Since: 2025-07-05 (8-K above)
  - Ranking note (trade press, not an owner source): "Notes : Reflects Dollar Tree’s sale of Family Dollar to private equity, Family Dollar is included as a separate retailer in our coverage, effective fiscal year 2025." — [NRF Top 100 Retailers 2026 List](https://nrf.com/research-insights/top-retailers/top-100-retailers/top-100-retailers-2026-list)
  - Model: not found (familydollar.com/about-us returned 404, and the static sitemap has no about or newsroom page)
  - Financing: "Wells Fargo, RBC Capital Markets, and WhiteHawk Capital Partners are providing financing for the transaction." — [Dollar Tree press release, March 26, 2025](https://www.sec.gov/Archives/edgar/data/935703/000093570325000012/ex992dollartreepressreleas.htm)
  - Affiliate: none found
  - BDC names: "Family Dollar Stores, LLC", "Family Dollar", "1959 Holdings, LLC"
  - Notes:
    - The equity split between Brigade and Macellum is not stated in any source read. "Partner to acquire" names both as buyers, so under the glossary this is a hop with no stated stake, which counts as control.
    - Whether either firm is PE depends on its Form ADV `Any PE Funds` value (not checked by this worker).
    - Lead for the BDC pass: EDGAR full-text search for "1959 Holdings" Brigade also returns an NPORT-P filed 2025-11-25 by Cliffwater Enhanced Lending Fund (CIK 1842754), an interval fund rather than a BDC. Not opened.
    - No primary source after the March 2026 10-K re-confirms ownership. Trade press reports about 350 closures in July 2025 to May 2026 (not cited).
- **DS4 Five Below**
  - Owner: "Our common stock is listed on the Nasdaq Global Select Market under the symbol “FIVE.”" — [Five Below, Inc., Form 10-K FY2025, filed 2026-03-19](https://www.sec.gov/Archives/edgar/data/1177609/000117760926000010/five-20260131.htm)
  - Model: "As of January 31, 2026, we operated 1,921 stores in 46 states." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1177609/000117760926000010/five-20260131.htm)
  - 5% holders: "5% Shareholders Not Listed Below: BlackRock, Inc. (1) 4,955,682 9.0 %" — [Five Below, DEF 14A, filed 2026-05-01](https://www.sec.gov/Archives/edgar/data/1177609/000119312526199315/d86361ddef14a.htm)
  - Since: not checked
  - Affiliate: blocked (fivebelow.com served a Cloudflare challenge, HTTP 403, even for robots.txt)
  - BDC names: "Five Below, Inc."
- **DS5 Ollie's Bargain Outlet**
  - Owner: "Our common stock is traded on NASDAQ under the symbol “OLLI.”" — [Ollie's Bargain Outlet Holdings, Form 10-K FY2025, filed 2026-03-19](https://www.sec.gov/Archives/edgar/data/1639300/000114036126010409/ef20060524_10k.htm)
  - Model: "On January 31, 2026, we operated 645 stores in 34 states, as depicted in the map below." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1639300/000114036126010409/ef20060524_10k.htm)
  - Sales: "Net sales increased to $2.649 billion in 2025 from $2.272 billion in 2024" — [same 10-K](https://www.sec.gov/Archives/edgar/data/1639300/000114036126010409/ef20060524_10k.htm)
  - 5% holders: "5% Stockholder Not Listed Below: FMR LLC 7,427,167.74 (1) 12.24% BlackRock, Inc. 5,287,909 (2) 8.72% Kayne Anderson Rudnick Investment Management LLC 3,674,154 (3) 6.06% Summit Trail Advisors, LLC 3,410,580 (4) 5.62% Vanguard Capital Management 3,223,420 (5) 5.28%" — [Ollie's, DEF 14A, filed 2026-04-30](https://www.sec.gov/Archives/edgar/data/1639300/000114036126018292/ny20064676x2_def14a.htm)
  - PE link (board, not a stake): "Mr. Zannino is a Managing Director of CCMP and a member of CCMP’s Investment Committee." — [same DEF 14A](https://www.sec.gov/Archives/edgar/data/1639300/000114036126018292/ny20064676x2_def14a.htm). Richard Zannino is lead independent director and holds 12,289 shares (less than 1%).
  - Since: not checked
  - Affiliate: none found (the only "affiliates" text on ollies.us is SMS-consent wording; "Ollie affiliate program" search results are for a different company, myollie.com)
  - BDC names: "Ollie's Bargain Outlet Holdings, Inc.", "Ollie's Holdings, Inc."
- **DS6 Big Lots!**
  - Owner: "Today, Variety operates more than 400 stores across 18 states, its retail brands include Big Lots!, Roses Discount Stores, Roses Express and Maxway." — [Big Lots!, About Us page, accessed 2026-11-07](https://biglots.com/about-us/)
  - Model: "Today, Big Lots! operates 219 stores across 15 states throughout the Midwest, Southeast, and Mid-Atlantic, and continues to grow." — [same page](https://biglots.com/about-us/)
  - Since: "Big Lots, Inc. (the “Company”) today announced that it has successfully closed its previously announced sale agreement with Gordon Brothers Retail Partners, LLC (“Gordon Brothers”) that will enable Variety Wholesalers, Inc. (“Variety Wholesalers”) to acquire between 200 and 400 Big Lots stores, which it plans to operate under the Big Lots brand, and up to two distribution centers." — [Big Lots, Inc. press release, Form 8-K Ex. 99.1, filed 2025-01-06](https://www.sec.gov/Archives/edgar/data/768835/000076883525000002/ex991pressrelease_biglot.htm)
  - Date: "BIG LOTS CLOSES SALE TO GORDON BROTHERS RETAIL PARTNERS COLUMBUS, Ohio, January 3, 2025" — [same release](https://www.sec.gov/Archives/edgar/data/768835/000076883525000002/ex991pressrelease_biglot.htm)
  - Variety's owners (history, not a current ownership statement): "Raised in rural North Carolina, he entered the family business running his father’s five discount-variety stores after World War II." and "Following John William Pope Sr.’s death in 2006, his youngest son, Art, became Chairman and CEO of Variety Wholesalers and Chairman and President of the Pope Foundation." — [John William Pope Foundation, Our History, accessed 2026-11-07](https://jwpf.org/about/our-history/)
  - Affiliate: none found
  - BDC names: "Variety Wholesalers, Inc.", "Big Lots", "Big Lots Stores, LLC"
  - Notes:
    - Variety's site domain (varietywholesalers.com) is parked.
    - The April 2025 Business Wire release on the reopening returned 403.
    - Secondary sources (Wikipedia; not cited) say the Pope family owns Variety privately. No primary source read states current ownership, hence "Owner type not confirmed". No investment firm is named anywhere.
    - The old Big Lots, Inc. (now "Former BL Stores Inc", CIK 768835) is in Chapter 11 and has no brand.
- **DS7 Ocean State Job Lot**
  - Owner: "Founded in 1977, Ocean State Job Lot (OSJL) is a growing, privately held discount retail chain with 177 stores in Rhode Island, Massachusetts, Connecticut, New Hampshire, Vermont, Maine, New York, New Jersey, Pennsylvania, Maryland, and Delaware, nearly 7,000 employees, and annual sales exceeding $900 million." — [Ocean State Job Lot press release, "Ocean State Job Lot Purchases Former Big Lots Location in Hamilton, New York…", accessed 2026-11-07](https://news.oceanstatejoblot.com/ocean-state-job-lot-purchases-former-big-lots-location-in-hamilton-new-york-with-plans-to-open-in-spring-2027/)
  - Ownership wording on the site: "From Ocean State Job Lot ownership to our thousands of associates, the team is guided by the commitment outlined in the company’s Mission, Vision and Values" — [OSJL, History page](https://about.oceanstatejoblot.com/history). The owner is not named.
  - Since: n/a (founded 1977, same release)
  - Affiliate: none found
  - BDC names: "Ocean State Job Lot", "Ocean State Jobbers, Inc." (site footer: "Copyright © 2018-2026 Ocean State Jobbers.")
  - Notes: secondary sources (not cited) say the Perlman family owns it, and no PE is named anywhere. 5 fetches.
- **DS8 Roses (incl. Roses Express)**
  - Owner: "Today, Variety operates more than 400 stores across 18 states. Its retail brands include Big Lots!, Roses Discount Stores, Roses Express and Maxway." — [Roses Discount Stores, About Us, accessed 2026-11-07](https://rosesdiscountstores.com/about-us/)
  - Model: "Today, Roses operates stores across the Southeast and Mid-Atlantic, with more locations on the way." — [same page](https://rosesdiscountstores.com/about-us/)
  - Since: not found (lead: Variety bought Roses in 1997, NCpedia, secondary)
  - Affiliate: none found
  - BDC names: "Variety Wholesalers, Inc.", "Roses Discount Stores"
  - Notes:
    - Roses Express is counted as a format of Roses, not a separate row, the way DG Market sits under Dollar General. Counted separately, Variety would have 4 rows.
    - Count by subtraction: Variety's "more than 400" minus 219 Big Lots! leaves 180-plus Roses, Roses Express and Maxway stores. That is arithmetic, not a stated figure.
    - Owner kind as DS6.
- **DS9 Maxway**
  - Owner: same sentence as DS8 ("Its retail brands include Big Lots!, Roses Discount Stores, Roses Express and Maxway.") — [Roses Discount Stores, About Us](https://rosesdiscountstores.com/about-us/)
  - Since / model / count: not found
  - Affiliate: not checked (no Maxway site found)
  - BDC names: "Variety Wholesalers, Inc."
- **DS10 pOpshelf**
  - Owner: "including, without limitation, Dollar General®, DG®, Clover Valley®, trueliving®, pOpshelf®, and Mi Super Dollar General®" — [Dollar General, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/29534/000110465926032325/dg-20260130x10k.htm) (trademarks DG owns)
  - Since: "In 2020 we launched pOpshelf, our unique small-box retail concept that focuses primarily on non-consumables." — [same 10-K](https://www.sec.gov/Archives/edgar/data/29534/000110465926032325/dg-20260130x10k.htm)
  - Model: "Beginning in 2025, we paused new pOpshelf store expansion while we evaluate and evolve its go-forward strategy and performance." and "In the first quarter of 2025, we closed 45 pOpshelf stores and converted an additional six to Dollar General stores" — [same 10-K](https://www.sec.gov/Archives/edgar/data/29534/000110465926032325/dg-20260130x10k.htm)
  - Affiliate: none found
  - BDC names: "Dollar General Corporation"
  - Notes: the current pOpshelf count is not stated in the 10-K or the DEF 14A.
- **DS11 Daiso (US)**
  - Owner (operator): "These terms of service are entered into by and between you and Daiso USA LLC" — [Daiso US, Terms of Service, effective 2026-08-19](https://daisous.com/pages/terms-of-service)
  - Trademarks: "The Daiso name, the terms Daiso USA LLC, Daiso Holding USA Inc., the Daiso logo, and all related names, logos, product and service names, designs, and slogans used on the Website are trademarks or registered trademarks of Daiso USA LLC" — [same page](https://daisous.com/pages/terms-of-service)
  - Parent: not found. daiso-sangyo.co.jp/english returned 404, and the /en page did not mention the US.
  - Since / count: not found (the About Us page has no ownership or count sentence)
  - Affiliate: none found
  - BDC names: "Daiso USA LLC", "Daiso Holding USA Inc."
  - Notes: 6 fetches. The ultimate parent (lead: Daiso Industries Co., Ltd., Japan, privately held) is not confirmed by a primary source read. daisous.com's robots.txt contains instructions addressed to AI agents; they were ignored.
- **DS12 MINISO (US)**
  - Owner: "Our ADSs currently trade on The New York Stock Exchange under the symbol “MNSO.”" — [MINISO Group Holding Ltd, Form 20-F FY2025, filed 2026-04-24](https://www.sec.gov/Archives/edgar/data/1815846/000110465926048172/mnso-20251231x20f.htm)
  - Control: "a company jointly controlled by our controlling shareholders, Mr. Guofu Ye and Ms. Yunyun Yang" — [same 20-F](https://www.sec.gov/Archives/edgar/data/1815846/000110465926048172/mnso-20251231x20f.htm)
  - Stake: "Guofu Ye (1) 789,541,061 63.7 %" — [same 20-F](https://www.sec.gov/Archives/edgar/data/1815846/000110465926048172/mnso-20251231x20f.htm) (Major Shareholders table, as of March 31, 2026; Norges Bank 5.0%)
  - Model: "In strategic markets with large population and huge market potential such as North America, we typically enter the markets by opening and operating stores on our own" — [same 20-F](https://www.sec.gov/Archives/edgar/data/1815846/000110465926048172/mnso-20251231x20f.htm)
  - Since: n/a
  - Affiliate: not checked
  - BDC names: "MINISO Group Holding Limited"
  - Notes: the 20-F gives only global and overseas counts (about 3,583 MINISO stores overseas), not a US count.
- **DS13 Bi-Mart**
  - Owner: "As a regional retailer owned by its employees since 2004, Bi-Mart is unique." — [Bi-Mart, Company page, accessed 2026-11-07](https://www.bimart.com/company)
  - Model: "Since that time, we’ve steadily opened stores throughout Oregon, Washington and Idaho." — [same page](https://www.bimart.com/company)
  - Since: 2004 (same sentence)
  - Affiliate: none found
  - BDC names: "Bi-Mart Corporation"
  - Notes: the store count is not on the company page.
- **DS14 T.J. Maxx**
  - Owner: "Common Stock, par value $1.00 per share TJX New York Stock Exchange" — [The TJX Companies, Form 10-K FY2026 (year ended 2026-01-31), filed 2026-03-31](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm) (cover-page table)
  - Since / model: "Our TJ Maxx and Marshalls chains in the United States (“Marmaxx”) are collectively the largest off-price retailer in the United States with a total of 2,603 stores. We founded TJ Maxx in 1976 and acquired Marshalls in 1995." — [same 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
  - 5% holders: "BlackRock, Inc. (1) 50 Hudson Yards New York, NY 10001 99,658,272 8.9 % The Vanguard Group, Inc. (2) 100 Vanguard Boulevard Malvern, PA 19355 96,205,314 8.44 %" — [TJX, DEF 14A, filed 2026-04-30](https://www.sec.gov/Archives/edgar/data/109198/000010919826000015/tjx-20260430.htm)
  - Affiliate: not checked (tjmaxx.tjx.com returned a "Something went wrong" page to curl)
  - BDC names: "The TJX Companies, Inc."
- **DS15 Marshalls**
  - Owner / since / model: same 10-K sentence as DS14 ("acquired Marshalls in 1995"; 2,603 Marmaxx stores) — [TJX, Form 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
  - Affiliate: not checked (marshalls.com returned the same error page)
  - BDC names: "The TJX Companies, Inc."
- **DS16 Ross Dress for Less**
  - Owner: "Our stock is traded on The Nasdaq Global Select Market ® under the symbol ROST." — [Ross Stores, Form 10-K FY2025, filed 2026-03-31](https://www.sec.gov/Archives/edgar/data/745732/000074573226000006/rost-20260131.htm)
  - Model: "As of January 31, 2026, we operated a total of 2,267 stores, comprised of 1,904 Ross stores and 363 dd’s DISCOUNTS stores." — [same 10-K](https://www.sec.gov/Archives/edgar/data/745732/000074573226000006/rost-20260131.htm)
  - 5% holders: "The Vanguard Group 100 Vanguard Boulevard Malvern, PA 19355 39,182,382 (2) 12.2 % BlackRock, Inc. 50 Hudson Yards New York, NY 10001 22,616,546 (2) 7.0 %" — [Ross Stores, DEF 14A, filed 2026-04-07](https://www.sec.gov/Archives/edgar/data/745732/000074573226000013/rost-20260406.htm)
  - Since: not checked
  - Affiliate: none found (rossstores.com homepage)
  - BDC names: "Ross Stores, Inc."
- **DS17 Burlington**
  - Owner: "Our common stock is listed on the New York Stock Exchange under the symbol “BURL.”" — [Burlington Stores, Form 10-K FY2025, filed 2026-03-19](https://www.sec.gov/Archives/edgar/data/1579298/000119312526116001/burl-20260131.htm)
  - Model: "Since then, we have expanded our store base to 1,212 stores as of January 31, 2026, in 46 states, Washington D.C. and Puerto Rico." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1579298/000119312526116001/burl-20260131.htm)
  - Former PE owner: "as a result of purchase accounting related to the April 13, 2006 Bain Capital acquisition of Burlington Coat Factory Warehouse Corporation" — [same 10-K](https://www.sec.gov/Archives/edgar/data/1579298/000119312526116001/burl-20260131.htm)
  - 5% holders: "Capital International Investors (2) 8,727,750 13.9 % JPMorgan Chase & Co. (3) 6,809,671 10.8 % BlackRock, Inc. (4) 6,479,470 10.3 % The Vanguard Group (5) 6,410,671 10.2 %" — [Burlington, DEF 14A, filed 2026-04-02](https://www.sec.gov/Archives/edgar/data/1579298/000119312526140144/burl-20260402.htm)
  - Since: not checked (Bain's exit year was not sourced)
  - Affiliate: none found
  - BDC names: "Burlington Stores, Inc.", "Burlington Coat Factory Warehouse Corporation"
- **DS18 HomeGoods**
  - Owner / since / model: "HomeGoods, introduced in 1992, is the leading off-price retailer of home fashions in the U.S. Through its 963 stores" — [TJX, Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
  - Affiliate: none found (homegoods.com homepage; its only "affiliate" string is an iOS app-banner meta tag)
  - BDC names: "The TJX Companies, Inc."
- **DS19 bealls**
  - Owner: "Bealls, Inc. is a privately held company, rich in tradition, still owned by the founding family." — [Bealls, Inc., Company FAQs page, accessed 2026-11-07](https://www.beallsinc.com/beallsinc/company-faqs). **This sentence is in the page's `<meta name="description">` tag, not the visible text.**
  - Brand: "bealls is a leading, off-price retailer. We save families money with our relentless pursuit of great deals." — [Bealls, Inc. home page](https://www.beallsinc.com/)
  - Model / count: "660+ Stores" — [Bealls, Inc., Fast Facts](https://www.beallsinc.com/beallsinc/fast-facts) (icon label; covers all Bealls, Inc. banners, not only the off-price "bealls" stores)
  - Since: n/a (founded 1915, same meta description)
  - Affiliate: none found (bealls.com homepage)
  - BDC names: "Bealls, Inc.", "Bealls Outlet Stores, Inc.", "Burkes Outlet Stores L.L.C."
- **DS20 Citi Trends**
  - Owner: "Our common stock is traded on The NASDAQ Stock Market under the symbol “CTRN.”" — [Citi Trends, Form 10-K FY2025, filed 2026-04-15](https://www.sec.gov/Archives/edgar/data/1318484/000110465926043813/ctrn-20260131x10k.htm)
  - Model: "As of January 31, 2026, we operated 590 stores in 33 states." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1318484/000110465926043813/ctrn-20260131x10k.htm)
  - 31% holder: "Fund 1 Investments, LLC (1) 100 Carr 115 Unit 1900, Rincon, Puerto Rico 00677 2,573,486 31.1%" — [Citi Trends, DEF 14A, filed 2026-05-01](https://www.sec.gov/Archives/edgar/data/1318484/000110465926053458/ctrn-20260610xdef14a.htm)
  - Holder detail: "The securities listed are held for the benefit of private investment funds for which Pleasant Lake Partners LLC (“PLP”) serves as investment advisor. Fund 1 Investments LLC (“Fund 1”) serves as managing member of PLP." — [same DEF 14A](https://www.sec.gov/Archives/edgar/data/1318484/000110465926053458/ctrn-20260610xdef14a.htm)
  - Other 5% holders: "Divisadero Street Capital Management, LP (3) 3480 Main Highway, Suite 204 Miami, Florida, USA 33133 472,151 5.7%" and "Shay Capital (4) 280 Park Avenue, 5th Floor West, New York, New York, USA 10017 549,594 5.1%" — [same DEF 14A](https://www.sec.gov/Archives/edgar/data/1318484/000110465926053458/ctrn-20260610xdef14a.htm). CEO Kenneth D. Seipel holds 8.2%.
  - Since: not checked
  - Affiliate: none found
  - BDC names: "Citi Trends, Inc."
  - Notes: Fund 1 has a cooperation agreement (board seats, March 2025) but is not stated to control. Pleasant Lake Partners' Form ADV `Any PE Funds` value decides the strict count for this row.
- **DS21 dd's DISCOUNTS**
  - Owner / model: same Ross 10-K sentence as DS16 ("363 dd’s DISCOUNTS stores") — [Ross Stores, Form 10-K](https://www.sec.gov/Archives/edgar/data/745732/000074573226000006/rost-20260131.htm)
  - Affiliate: not checked
  - BDC names: "Ross Stores, Inc."
- **DS22 Nordstrom Rack**
  - Owner: "Parent and Acquisition Sub were formed by certain members of the Nordstrom family and related trusts and family-controlled investment vehicles (the “ Family Group ”) and El Puerto de Liverpool S.A.B. de C.V., a Mexican publicly traded corporation" — [Nordstrom, Inc., Form 8-K, filed 2025-05-20](https://www.sec.gov/Archives/edgar/data/72333/000110465925050982/tm2515470d12_8k.htm)
  - Since: "As a result of the Merger, a change in control of the Company occurred, and the Company became a wholly owned subsidiary of Parent." — [same 8-K](https://www.sec.gov/Archives/edgar/data/72333/000110465925050982/tm2515470d12_8k.htm) (merger effective May 20, 2025)
  - Model: "As of February 1, 2025, Nordstrom Rack includes the following physical and digital properties: • 277 Nordstrom Rack stores" — [Nordstrom, Form 10-K FY2024, filed 2025-03-21](https://www.sec.gov/Archives/edgar/data/72333/000007233325000039/jwn-20250201.htm) (last 10-K before deregistration; Form 15-12G filed 2025-06-02)
  - Affiliate: network listings only (FlexOffers, UpPromote and LinkClicky pages surfaced in search; they disagree on the network). Not verified, and no brand-direct page was found. nordstromrack.com returned a script-only page to curl.
  - BDC names: "Nordstrom, Inc.", "Nordstrom Holdings, Inc."
  - Notes: the equity split between the family group and Liverpool is in the 8-K funding paragraph (cash contribution and a shareholder loan from Liverpool) but was not computed. No investment firm is named.
- **DS23 Gabe's**
  - Owner: "Pursuant to the restructuring, the ad hoc group of lenders that Debevoise represented are now the majority owners of Gabe’s." — [Debevoise & Plimpton LLP, "Debevoise Advises Ad Hoc Group of Lenders to Gabe’s in Connection with Change of Control Transaction and New Financing", 2 September 2025](https://www.debevoise.com/news/2025/09/debevoise-advises-ad-hoc-group)
  - Owner names and since: "Debevoise & Plimpton LLP has advised an ad hoc group of lenders consisting of Brigade Capital Management, Arbour Lane Capital Management, and Anchorage Capital Advisors, in connection with a restructuring transaction of Gabriel Brothers, Inc. (“Gabe’s”) which closed on August 25, 2025." — [same page](https://www.debevoise.com/news/2025/09/debevoise-advises-ad-hoc-group)
  - Model: "Founded in 1961 in Morgantown, West Virginia, Gabe's is a leading off-price retailer with more than 150 stores across 20 U.S. states." — [same page](https://www.debevoise.com/news/2025/09/debevoise-advises-ad-hoc-group). The company site says: "Today, more than 140 Gabe’s and Old Time Pottery store locations are found across 20 states" — [Gabe's, About Gabe's](https://gabesstores.com/about-gabes/)
  - Old Time Pottery: "Old Time Pottery, a Tennessee-based home merchandise store, became a part of the Gabe’s family in 2023." — [Gabe's, About Gabe's](https://gabesstores.com/about-gabes/)
  - Affiliate: none found
  - BDC names: "Gabriel Brothers, Inc.", "Gabe's", "Old Time Pottery"
  - Notes:
    - This is a law-firm release, not a company or sponsor release. The company's own release on Business Wire (2025-08-25) was not fetched because businesswire.com returns 403.
    - Leads, not fetched or not cited: search snippets of that release say the lenders "converted more than 75% of Gabe’s outstanding term loan obligations into equity, acquiring it from Warburg Pincus", and that "Second Avenue Capital Partners and Ares Credit funds will continue to provide an ABL facility". Warburg Pincus's 2016 acquisition release is a PDF on warburgpincus.com.
    - Ares Credit funds are a BDC lead for the assembler.
    - The Gabe's site does not name its owner.
- **DS24 Sierra**
  - Owner / since: "Sierra, acquired in 2012 and rebranded from Sierra Trading Post in 2018, is a leading off-price retailer of brand name active and outdoor apparel, footwear, and gear" — [TJX, Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
  - Model: "Sierra operates 145 retail stores in the U.S. and sierra.com." — [same 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
  - Affiliate: not checked (sierra.com returned a "Something went wrong" page to curl)
  - BDC names: "The TJX Companies, Inc."
- **DS25 Homesense**
  - Owner / since / model: "In 2017, we launched our Homesense chain in the U.S. Our 79 Homesense stores complement HomeGoods" — [TJX, Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm)
  - Affiliate: not checked
  - BDC names: "The TJX Companies, Inc."

### Rollups and groups that are not brands
Not counted in the rows above.
- **Variety Wholesalers, Inc.** (Henderson, NC): groups Big Lots!, Roses, Roses Express and Maxway. Owner not stated. The Pope Foundation history calls it the family business, and Art Pope became chairman and CEO in 2006 (DS6).
- **The TJX Companies, Inc.**: groups T.J. Maxx, Marshalls, HomeGoods, Sierra and Homesense. Public (TJX).
- **Ross Stores, Inc.**: groups Ross Dress for Less and dd's DISCOUNTS. Public (ROST).
- **1959 Holdings, LLC**: the Family Dollar buyer entity. Brigade and Macellum are the named buyers (DS3).
- **Nordstrom Holdings, Inc.**: the Nordstrom family group and El Puerto de Liverpool (DS22).
- **Bealls, Inc.** (with Bealls Stores, Inc., Bealls Outlet Stores, Inc. and Burkes Outlet Stores L.L.C.): founding family (DS19).
- **Daiso USA LLC / Daiso Holding USA Inc.**: parent not confirmed (DS11).
- **Gordon Brothers Retail Partners, LLC**: bought Big Lots assets in the bankruptcy and enabled Variety's purchase (DS6). Not a current owner of any brand row.

### Closed or excluded chains (not counted)
- **Bargain Hunt** (extreme-discount, Southeast): PE-owned when it closed.
  - Owner: "ACON Investments, L.L.C. and its affiliates (“ACON”) announced the recapitalization and acquisition of Bargain Holdings, L.L.C. (“Bargain Hunt”), an extreme discount retailer in the southeastern region of the U.S." — [ACON Investments, release dated February 11, 2020](https://aconinvestments.com/?p=500)
  - Closure: trade press reports Chapter 11 and liquidation of all 92 stores in early 2025 (retailtouchpoints.com, not fetched).
  - Lead only: Thomas H. Lee Partners was the earlier owner (2015).
- **Dirt Cheap** (Channel Control Merchants): Chapter 11 in October 2024, all stores closed (trade press, not fetched). Owner not researched.
- **99 Cents Only Stores**: closed all stores in 2024 (lead: owned by Ares and CPPIB, not researched).
- **Tuesday Morning** and **Christmas Tree Shops**: closed in 2023, not researched.
- **Saks OFF 5TH**: parent Saks Global filed Chapter 11 on 2026-01-14. Trade press reports most Off 5th stores closing (about 12 of 70 kept). Excluded as no longer a national chain; not researched further.
- **Marc's** (Ohio): excluded as a discount grocer. mymarcs.com did not respond.

### Category share
**Core (rows 1–13: dollar, discount variety, closeout), N = 13:**
- **PE-owned (control), confirmed: 0 / 13 = 0.0%.** No owner in this block calls itself private equity in a primary source.
- **Investment-firm control, PE status pending Form ADV: 1 / 13 = 7.7%.** Family Dollar (Brigade Capital Management, LP; Macellum Capital Management, LLC; closed 2025-07-05). If the assembler's ADV check reports `Any PE Funds = Y` for either firm, this row becomes PE-owned.
- **PE minority stake: 0.**
- **Public company: 6 / 13 = 46.2%.**
  - The rows: Dollar General, pOpshelf (DG), Dollar Tree, Five Below, Ollie's, MINISO.
  - Rows with a 5%+ holder whose ADV still needs checking:
    - Dollar Tree: Mantle Ridge LP 7.0%.
    - Ollie's: Kayne Anderson Rudnick 6.06% and Summit Trail Advisors 5.62%; FMR 12.24% is an index/asset-manager type.
  - Dollar General, Five Below and MINISO have only index managers or a sovereign fund at 5%+.
  - Formerly PE-owned: Dollar General (KKR, exited December 2013).
- **Other: employee-owned 1 / 13 = 7.7%** (Bi-Mart).
- **Owner type not confirmed: 5 / 13 = 38.5%.**
  - Big Lots!, Roses and Maxway: Variety Wholesalers, private; family business per its owners' foundation.
  - Ocean State Job Lot: "privately held", owner not named.
  - Daiso: operator named, parent not confirmed.
  - No investment firm is named for any of the five.
- **Upper bound (PE-owned plus PE minority stake):**
  - 1 / 13 = 7.7% if Brigade or Macellum is flagged.
  - Strict count: 3 / 13 = 23.1% if Mantle Ridge (Dollar Tree) and one of Ollie's non-index holders are also flagged.
- **By parent company:** 10 parents; investment-firm-controlled 1 / 10 (1959 Holdings).
  - The parents: Dollar General, Dollar Tree, 1959 Holdings, Five Below, Ollie's, Variety Wholesalers, Ocean State Job Lot, Daiso USA, MINISO, Bi-Mart.
- **By sales (rows with a figure):**
  - Known 2025 sales: Dollar General $43.13B, Dollar Tree $18.93B, Family Dollar $11.91B and Five Below $4.76B (NRF); Ollie's $2.649B (10-K); Ocean State Job Lot over $0.9B (its release). Total about $82.3B.
  - Family Dollar is **14.5%** of that.
  - No sales figure was found for Big Lots!, Roses, Maxway, Daiso, MINISO US or Bi-Mart. pOpshelf sits inside Dollar General's figure.

**All rows (core plus off-price, rows 1–25), N = 25:**
- **PE-owned (control), confirmed: 0 / 25 = 0.0%.**
- **Investment-firm control, PE status pending Form ADV: 2 / 25 = 8.0%.**
  - Family Dollar.
  - Gabe's: lender group of Brigade, Arbour Lane and Anchorage, "majority owners" since 2025-08-25; formerly Warburg Pincus (lead).
- **PE minority stake: 0.**
- **Public company: 15 / 25 = 60.0%.** The 6 core rows plus 5 TJX rows, 2 Ross rows, Burlington and Citi Trends.
  - Off-price rows with a non-index 5%+ holder whose ADV needs checking: Citi Trends (Fund 1 Investments / Pleasant Lake Partners 31.1%; Divisadero Street 5.7%; Shay Capital 5.1%).
  - Burlington's holders are Capital International and JPMorgan Chase, plus index managers.
  - Formerly PE-owned: Burlington (Bain Capital, 2006 acquisition).
- **Other: 3 / 25 = 12.0%.**
  - Family: bealls.
  - Family plus foreign public company: Nordstrom Rack.
  - Employee-owned: Bi-Mart.
- **Owner type not confirmed: 5 / 25 = 20.0%** (as in the core).
- **Upper bound:**
  - 2 / 25 = 8.0% if the Family Dollar and Gabe's owners are flagged.
  - Strict count: 6 / 25 = 24.0% if Dollar Tree, Ollie's, Citi Trends and Burlington holders are flagged too. Burlington is only reached if JPMorgan or Capital International is treated as PE; the pilot did not treat them so.
- **By parent company:** 17 parents; investment-firm-controlled 2 / 17 (1959 Holdings, Gabriel Brothers).
- **By sales:** not computed for off-price. NRF reports TJX and Nordstrom at company level (all banners), and no figure was found for Gabe's or bealls.

**Sources disagree:**
- On owners: none.
- Two framing or count differences:
  - Family Dollar's buyers: NRF (trade press) says "private equity". Dollar Tree's release calls Brigade an "asset management firm" and "alternative asset manager", and Macellum an "investment firm". The identity agrees, and only the label differs.
  - Gabe's store count: Debevoise (Sept 2025) says "more than 150 stores across 20 U.S. states". The company site says "more than 140 Gabe’s and Old Time Pottery store locations are found across 20 states".

**Same firm across rows:** Brigade Capital Management is a named owner of both Family Dollar and Gabe's.

### Firms named
Every investment firm named as an owner, buyer or 5%+ holder, as the sources name it, for the assembler's Form ADV check:

- **Current owners or buyers (control):**
  - Brigade Capital Management, LP: Family Dollar; also Gabe's, as "Brigade Capital Management".
  - Macellum Capital Management, LLC: Family Dollar.
  - Arbour Lane Capital Management: Gabe's.
  - Anchorage Capital Advisors: Gabe's.
- **5%+ holders of public parents (not control):**
  - Mantle Ridge LP: Dollar Tree, 7.0%.
  - Fund 1 Investments, LLC and Pleasant Lake Partners LLC: Citi Trends, 31.1%.
  - Divisadero Street Capital Management, LP: Citi Trends, 5.7%.
  - Shay Capital (the footnote names Shay Capital LLC and Shay Capital Holdings LLC): Citi Trends, 5.1%.
  - Kayne Anderson Rudnick Investment Management LLC: Ollie's, 6.06%.
  - Summit Trail Advisors, LLC: Ollie's, 5.62%.
  - Capital International Investors: Burlington, 13.9%.
  - JPMorgan Chase & Co.: Burlington, 10.8%.
  - FMR LLC: Ollie's 12.24%; Dollar Tree 8.3%.
  - Index and asset managers, listed for completeness: The Vanguard Group, Inc. / Vanguard Capital Management, BlackRock, Inc. and State Street Corporation.
  - Norges Bank: MINISO, 5.0% (sovereign; no ADV expected).
- **Former owners or board links (not current):**
  - KKR (Kohlberg Kravis Roberts & Co. L.P.): Dollar General, exited 2013.
  - Bain Capital: Burlington, 2006.
  - CCMP: Ollie's, a managing director is a director.
  - Warburg Pincus: Gabe's, until 2025 (lead).
  - ACON Investments, L.L.C.: Bargain Hunt, closed.
  - Thomas H. Lee Partners: Bargain Hunt, 2015 (lead).
- **Lenders or other named parties (not owners):**
  - WhiteHawk Capital Partners: Family Dollar financing.
  - Gordon Brothers Retail Partners, LLC: Big Lots asset buyer.
  - Leads only: Second Avenue Capital Partners and Ares Credit funds (Gabe's ABL).

### Worker log
- **Time:** start 2026-11-07T16:35:14Z, end 2026-11-07T16:59Z, about 24 minutes for 25 rows (including the ranking, writing and the quote self-check).
- **Calls:** WebSearch 19, WebFetch 1, curl 119 HTTP requests.
  - WebFetch: Business Wire, which returned 403.
  - 38 of the curl requests went to SEC: 11 submissions JSON, 2 EDGAR full-text searches, 2 filing indexes and 23 documents (10-K ×9, DEF 14A ×8, 20-F, 8-K ×3 and 8-K exhibits ×2).
  - The other 81 curl requests: 34 robots.txt checks and 47 company, foundation, law-firm, sponsor and ranking pages.
  - Status of all 119: 111 × 200, 4 × 404, 2 × no response, 1 × 403 (fivebelow.com) and 1 × redirect failure (rosesdiscountstores.com with www).
  - SEC pacing: one request per 0.6 s or slower.
- **What was cheap:** public parents. One 10-K plus one DEF 14A settled each of Dollar General, Dollar Tree, Five Below, Ollie's, Ross (2 rows), Burlington, Citi Trends and TJX (5 rows), and the 20-F settled MINISO. That is 15 rows from 17 SEC documents, all with mechanically checkable quotes. Family Dollar took 4 SEC requests: the full-text search found the buyer entity, and the 8-K exhibit release named the firms.
- **What made brands slow:**
  - Private chains whose sites never name an owner: Ocean State Job Lot ("privately held"; 5 fetches), Variety Wholesalers (parked domain; brand sites name Variety but not its owners; 4 fetches plus a foundation page), Daiso (6 fetches; US site names only the operating LLC; parent site has no US page).
  - 2025 ownership changes announced only on Business Wire, which returns 403: Gabe's (settled through a law-firm release), Big Lots' reopening and Family Dollar's 2026 updates.
  - Chain closures that the trade lists still mention (Bargain Hunt, Dirt Cheap, 99 Cents Only, Tuesday Morning, Christmas Tree Shops, Saks OFF 5TH). Each cost a search to rule out.
  - Store counts for format brands (pOpshelf, Roses Express, Maxway, MINISO US), which the parents don't break out.
  - The ranking: NRF covers only the 4 largest dollar brands, so the rest had to be placed by counts from their own sources.
- **Which kinds of brands had no primary source for the owner:**
  - Family or founder-held private chains whose sites describe themselves without naming owners: Ocean State Job Lot, Variety Wholesalers' brands.
  - Foreign-parented US subsidiaries whose parent's site doesn't cover the US: Daiso.
  - In both kinds no investment firm was named anywhere.
- **Affiliate programs:**
  - Checked: homepage or about-page HTML for "affiliat" links on 20 brand sites, plus two web searches.
  - Found: no brand-direct program.
  - Nordstrom Rack appears on affiliate-network listings (FlexOffers, UpPromote, LinkClicky), unverified.
  - Unreadable to curl: Dollar Tree, TJ Maxx, Marshalls, Sierra and Nordstrom Rack returned error or script-only pages, and Five Below is behind Cloudflare.
  - As in restaurants, the dollar and discount segment looks like a near-zero affiliate category. Its PE-linked rows (Family Dollar, Gabe's) have no affiliate pages.
- **Quote caveats for the assembler:**
  - SEC quotes were taken from curl'd text with tags stripped, whitespace collapsed and zero-width spaces removed. Some 10-K text has zero-width spaces (U+200B) between sentences (Dollar General), and table-cell quotes (5% holder rows) depend on whitespace collapsing.
  - The Bealls ownership sentence is in a `<meta name="description">` tag (DS19). The "660+ Stores" figure is an icon label.
  - No quotes came from WebFetch summaries; every quote is from a curl'd page.
- **Blocked or unusable:**
  - 403: businesswire.com (WebFetch), fivebelow.com.
  - 404: familydollar.com/about-us, gabesstores.com/newsroom, daiso-sangyo.co.jp/english, and the am590theanswer.com reprint of the Gabe's release.
  - No response: mymarcs.com, business.minstercommunitypost.com.
  - Parked: varietywholesalers.com.
  - Error pages to curl: dollartree.com, tjmaxx.tjx.com, marshalls.com, sierra.com; nordstromrack.com is script-only.
  - Competitor sites, Reddit, WhoIsMyDentist and Private Equity Vet were not opened. A CB Insights result surfaced in a Gabe's search and was not opened.
