# Category audit: Women's apparel

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (fetches logged 16:59–17:20 UTC) · Ownership facts come from primary sources only. No free top-30 ranking exists, so the brand list is a composite built from each brand's own store count (see Ranking).

**Short answer**

| | Women's apparel (32 rows) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **12 / 32 (37.5%)**: 10 PE-owned (Sycamore: Torrid plus 7 KnitWell brands; Summit: Princess Polly; Permira: Reformation) and 2 PE minority stakes (J.Jill: TowerBrook 49.2%; Lulus: H.I.G. Growth Partners 32.1%) |
| Glossary-strict count (public company whose 5%+ holder's Form ADV reports PE funds) | **12 / 32** as counted. It rises to 13 if Aldebaran Capital, LLC (Cato, 6.2%) reports PE funds, and to 15 if BBRC International (Victoria's Secret and PINK, 9.8–13.0%) does. The assembler must check both. |
| PE owner on record, current status not reconfirmed | 2 more: maurices (OpCapita, 2019; OpCapita's website domain is now parked) and Madewell (Anchorage Capital Group, majority owner of J.Crew Group since 2020). **Upper bound 14 / 32 (43.8%).** |
| Owner not found | **5**: Rainbow, Altar'd State, Shein, Fashion Nova, Skims |
| Brand-direct affiliate programs | **5 found**: Windsor, Rainbow, maurices, Aerie (ae.com) and Reformation. Reformation is PE-owned, and maurices is PE-owned on the 2019 record. Network listings only for Talbots, LOFT, Chico's, Ann Taylor, Lilly Pulitzer, Madewell, J.Jill and Anthropologie US. |

- **Sycamore Partners is the category's largest owner.** It controls 8 of the 32 rows: Torrid (58.59%, NYSE-listed and a "controlled company") and the 7 ranked brands of KnitWell Group (Ann Taylor, LOFT, Lane Bryant, Talbots, Chico's, White House Black Market and Soma). KnitWell's June 2026 release calls itself "A portfolio company of Sycamore Partners".
- **The row count is 32, not 30.** The composite has 17 chains with a store count from a primary source, 9 large chains whose own sources give no count, and 6 online-first brands. Dropping any of them would have meant guessing at size. Every share here is out of 32; the assembler can re-base.
- **Live changes:** Francesca's (about 400–475 stores) filed its second Chapter 11 in February 2026 and is liquidating (trade press), so it is not a row. Victoria's Secret changed its ticker from VSCO to VSXY on 2026-06-02 (10-Q).
- **BDC lead for the assembler:** EDGAR full-text search for "Knitwell" returns 10-Qs of HPS Corporate Lending Fund and HPS Corporate Capital Solutions Fund (2024–2026). The Chico's 8-K names "Knitwell Borrower LLC" as borrower under a term loan agented by HPS Investment Partners, LLC.

## How this was sourced (read first)

- **Rankings:** no ranking was used as evidence of ownership. The trade sources checked were rejected as rankings (see Ranking).
- **Ownership facts:**
  - SEC filings: 10-K, DEF 14A, 10-Q, 8-K and Schedule 13D/A for 9 public parents, plus completion 8-Ks for the Talbots (2012), Ascena (2020) and Chico's (2024) deals.
  - Sponsor and company press releases on PR Newswire: KnitWell 2023, 2024 and 2026, and J.Crew 2020. The Sycamore Partners news page mirrors the 2024 release.
  - Permira's portfolio page.
  - Company sites: maurices, Windsor, Rainbow, YM Inc., Charlotte Russe terms, Fashion Nova and Evereve.
  - Aritzia's own quarterly release (a PDF on its IR CDN).
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist, Private Equity Vet, PitchBook, Preqin and CB Insights. A CB Insights page and Wikipedia came up in searches and were not opened or used.
- **Leads only, never cited:** Wikipedia (Rainbow's owner family), FlexOffers, Admitad, UpPromote and LinkClicky affiliate listings, mergr, and trade press on Francesca's, Charlotte Russe and maurices.
- **SEC access:** every SEC request (www, data.sec.gov, efts) used the user agent `EvidenceEngine ownership-research bot (category audit)` with no contact detail, slept 0.6 s between requests, and was served HTTP 200.
- **Robots.txt:** checked before the first curl fetch of every new site. None disallowed the pages fetched.
  - aritzia.com, altardstate.com, anthropologie.com, freepeople.com, lillypulitzer.com, francescas.com, investors.jcrew.com and blackstone.com returned 403 or 423 to robots.txt and to the page itself, so nothing from those sites is cited.
  - investors.aritzia.com sets `Crawl-delay: 10`; one request was made there.
- **Quote handling:**
  - SEC and site quotes were copied from curl'd HTML converted to text (tags stripped, entities unescaped, whitespace collapsed). Inline tags can split a sentence, as in "$1 .6 billion" in the J.Crew release, so quotes keep the extracted spacing.
  - Table rows are quoted as the flattened row text, for example "Company-Operated: U.S. 766 782".
  - The Aritzia quote comes from pypdf text of a PDF.
- **Owner kinds are research notes, not engine classifications** (ADR 0001 governs the product).
  - "PE-owned" means control, or a PE hop with no stated stake.
  - A public company that a PE fund controls (Torrid, a.k.a. Brands) counts as PE-owned.
  - Counts are by brand row: KnitWell is 7 rows and Urban Outfitters is 3.

## Ranking

**No free top-30 ranking was found.** Three searches looked for one. Two trade pages were opened and rejected:
- **Retailboss, "The Top 10 Women's Clothing Stores in USA (2026 Ranking)"** (2026-01-09, https://retailboss.co/the-top-10-womens-clothing-stores-in-usa-2026-ranking/): a weighted score, 40% of it social media. Only 10 names are free, and it mixes in department stores (Nordstrom) and unisex chains (Zara, H&M, Abercrombie).
- **xmap.ai, "largest apparel & accessory stores in the United States"** (2025-09-22, https://www.xmap.ai/blog/largest-apparel-stores-in-the-united-states): location counts, but none of its top 10 is a women's specialty chain.
- **Paywalled sources:** IBISWorld and Statista hold women's-clothing-store data. Not used.

**Composite (built here, like the pilot's gyms list).** The candidates are women-focused apparel brands that sell mainly through their own stores or sites. They came from the parents' 10-Ks, the KnitWell portfolio and the leads above, and the list is not exhaustive. The rows fall in three groups:
- **Rows 1–17** are ordered by the store count in the brand's own filing or site, as of the date in the Brand cell. Six of the counts are not US-only, as the Brand cells say: maurices, Victoria's Secret, PINK, Torrid, Aritzia and FP Movement.
- **Rows 18–26** are large store chains whose own sources gave no store count, listed alphabetically. Store finders for Chico's and Soma are JavaScript-only. LOFT's and Ann Taylor's directories redirect to the shop sites. Talbots' and WHBM's store subdomains did not resolve.
- **Rows 27–32** are online-first brands with few or no stores, listed alphabetically. No common sales measure exists: Lulus and a.k.a. Brands file revenue, while Shein, Fashion Nova, Skims and Reformation do not.

**Considered and left out:**
- Francesca's: liquidating in 2026 (trade press).
- Spanx: a product brand sold largely through wholesale. Blackstone has held a majority since 2021, per the titles of Blackstone's releases; blackstone.com and Business Wire returned 403, so this is not cited.
- Adore Me, Petal & Pup and Haven Well Within: small brands of Victoria's Secret, a.k.a. and KnitWell.
- Versona and Cache: Cato banners. Their stores are inside Cato Corp's 1,069 and no separate count was found.
- It's Fashion: Cato's family-apparel banner.
- Evereve: a multi-brand boutique.
- Lululemon, Abercrombie & Fitch, Old Navy, Fabletics, Alo, Vuori and rue21: unisex or family brands.
- Vince: men's and women's, wholesale-heavy.

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Cato (incl. Cato Fashions, Cato Plus; 1,069 stores for all Cato Corp banners, 31 states, 2026-01-31) | Cato Corporation; John P. D. Cato holds 53.3% of voting power | public company (family-controlled; NYSE "controlled company" exemption available) | none known; Aldebaran Capital, LLC 6.2% (ADV not checked) | not checked (brand native to parent) | CATO | company stores | none found (no link in homepage HTML) | WA1 |
| 2 | maurices (900 locations, U.S. and Canada) | an affiliate of OpCapita LLP (2019); Ascena kept ~49.6% of that affiliate | PE owner on record (2019), current status not reconfirmed | OpCapita | 2019-05-06 | — | company stores | yes: maurices.com "Affiliate Program" (Rakuten LinkShare) | WA2 |
| 3 | Rainbow (over 800 stores, U.S., PR, USVI) | not found | not found | not found | not found | — | company stores | yes: footer "Affiliate Program" link to a CJ branded sign-up | WA3 |
| 4 | Victoria's Secret (766 U.S. company-operated VS and PINK stores, 2026-01-31) | Victoria's Secret & Co. | public company | none known (BlackRock 13.8%, BBRC International 13.0% (9.8% by 2026-07-28), Vanguard 5.9%) | not checked | VSXY (VSCO until 2026-06-02) | company-operated in U.S.; franchise, license and wholesale abroad | none found (network listings for MX, KSA, UK only) | WA4 |
| 5 | PINK (stores counted with Victoria's Secret) | Victoria's Secret & Co. | public company | as row 4 | not checked | VSXY | as row 4 | none found | WA4 |
| 6 | Torrid (483 stores, U.S., PR and Canada) | Torrid Holdings Inc., controlled by Sycamore Partners Management, L.P. (58.59%) | PE-owned (public, Sycamore-controlled) | Sycamore Partners | not found (Sycamore controlled it at the 2021-07-01 IPO) | CURV | company stores | none found (homepage 403) | WA5 |
| 7 | Lane Bryant (362 stores in its own store directory) | KnitWell Group, "A portfolio company of Sycamore Partners" | PE-owned (via KnitWell) | Sycamore Partners | 2020-12-23 | — | company stores | network listings only | WA6 |
| 8 | Windsor (over 350+ stores) | Zekaria family ("owned and operated by generations of the Zekaria family") | family | none | not applicable (family since 1937) | — | company stores | yes: windsorstore.com/pages/affiliate | WA7 |
| 9 | Aerie (332 stand-alone stores, plus 184 side-by-sides with AE) | American Eagle Outfitters, Inc. | public company | none (BlackRock 13.88%, Jay Schottenstein 7.65%, Dimensional 6.57%, Vanguard 6.23%) | not checked | AEO | company stores; licensed abroad | yes: ae.com footer "Affiliate Program" link to a Rakuten sign-up | WA8 |
| 10 | J.Jill (256 stores in 42 states) | J.Jill, Inc.; TowerBrook affiliates hold 49.2% | PE minority stake (public; TowerBrook ceased majority control in June 2024) | TowerBrook Capital Partners | 2015 (services agreement dated 2015-05-08) | JILL | company stores | network listings only (CJ) | WA9 |
| 11 | Athleta (252 North America stores) | Gap Inc. | public company (Fisher family ~46% combined) | none (Vanguard 6.95%, BlackRock 5.14%) | 2008 | GAP | company stores plus franchise abroad | none found | WA10 |
| 12 | Anthropologie (234 North America stores) | Urban Outfitters, Inc. | public company | none (BlackRock 9.07%, FMR 5.56%, David A. Hayne 5.11%) | not checked | URBN | company stores; franchise in Middle East | UK site page only (anthropologie.com/en-gb); US network listing only | WA11 |
| 13 | Free People (167 North America stores) | Urban Outfitters, Inc. | public company | none | not checked | URBN | company stores | none found (site 403) | WA11 |
| 14 | Aritzia (146 boutiques, U.S. and Canada; U.S. is 66.6% of Q2 revenue) | Aritzia Inc. | public company (TSX) | 5%+ holders not checked (SEDAR+ filer, no DEF 14A) | not checked | ATZ (TSX) | company boutiques | none found (site 403) | WA12 |
| 15 | FP Movement (88 stores, all North America) | Urban Outfitters, Inc. | public company | none | not checked | URBN | company stores | none found | WA11 |
| 16 | Johnny Was (78 locations: 75 full-price, 3 outlets) | Oxford Industries, Inc. | public company | none (FMR 15.0%, BlackRock 13.8%, Vanguard 7.1%, Schwab 5.1%) | not checked | OXM | 81% direct to consumer; rest wholesale | none found | WA13 |
| 17 | Lilly Pulitzer (67 full-price stores, plus 42 independent Signature Stores) | Oxford Industries, Inc. | public company | none | not checked | OXM | own stores and site, Signature Stores (wholesale), department stores | network listing only (FlexOffers) | WA13 |
| 18 | Altar'd State | not found | not found | not found | not found | — | not found | none found (site 403) | WA14 |
| 19 | Ann Taylor | KnitWell Group (Sycamore portfolio company) | PE-owned (via KnitWell) | Sycamore Partners | 2020-12-23 | — | company stores | network listing only (FlexOffers) | WA6 |
| 20 | Charlotte Russe | YM Inc. (Toronto); site operated by CR Clicks (2019) LLC "from Toronto" | other: private company; YM's owners not stated | none known | not found (2019 per trade press) | — | company stores | none found | WA15 |
| 21 | Chico's | KnitWell Group (Sycamore portfolio company) | PE-owned (via KnitWell) | Sycamore Partners | 2024-01-05 | — (Chico's FAS taken private 2024) | company stores | network listing only (FlexOffers) | WA6 |
| 22 | LOFT | KnitWell Group (Sycamore portfolio company) | PE-owned (via KnitWell) | Sycamore Partners | 2020-12-23 | — | company stores | network listings only (FlexOffers, CJ) | WA6 |
| 23 | Madewell | J.Crew Group; "Anchorage Capital Group, L.L.C. ("Anchorage") has become the majority owner" (2020) | investment-firm owner (debt-for-equity), current status not reconfirmed | Anchorage Capital Group (PE status not confirmed; ADV check) | 2020-09-10 | — | company stores | network listings only (CJ, Admitad) | WA16 |
| 24 | Soma | KnitWell Group (Sycamore portfolio company) | PE-owned (via KnitWell) | Sycamore Partners | 2024-01-05 | — | company stores | none found | WA6 |
| 25 | Talbots | KnitWell Group (Sycamore portfolio company) | PE-owned (via KnitWell) | Sycamore Partners | 2012-08-03 | — | company stores | network listings only | WA6 |
| 26 | White House Black Market | KnitWell Group (Sycamore portfolio company) | PE-owned (via KnitWell) | Sycamore Partners | 2024-01-05 | — | company stores | none found | WA6 |
| 27 | Fashion Nova | not found | not found | not found | not found | — | online-first (started as one LA store, 2006) | none found (no link in homepage HTML) | WA17 |
| 28 | Lulus | Lulu's Fashion Lounge Holdings, Inc.; H.I.G. Growth Partners 32.1%, IVP 17.6%, CPPIB 17.5% | PE minority stake (public) | H.I.G. Growth Partners (holder, not controller) | not checked (holder before the 2021 IPO) | LVLU | online | none found (homepage 403) | WA18 |
| 29 | Princess Polly (online; 13 U.S. stores opened 2023–2025) | a.k.a. Brands Holding Corp., controlled by Summit Partners (56.0%) | PE-owned (public, Summit-controlled) | Summit Partners | July 2018 (joined a.k.a.; Summit's entry date not checked) | AKA | online plus stores and wholesale | none found | WA19 |
| 30 | Reformation | Permira (portfolio page "Status Current", investment year 2019) | PE-owned (stake not stated on page) | Permira | 2019 | — | 85% direct to consumer | yes: thereformation.com/ref-affiliates.html | WA20 |
| 31 | Shein | not found (US site and app "provided by SHEIN US Services, LLC") | not found | not found | not found | — | online | none found | WA21 |
| 32 | Skims | not found | not found | not found | not found | — | online plus own stores | none found | WA22 |

### Evidence
- **WA1 Cato**
  - Owner and count: "The Company, founded in 1946, operated 1,069 fashion specialty stores at January 31, 2026, in 31 states, principally in the southeastern United States, under the names “Cato,” “Cato Fashions,” “Cato Plus,” “It’s Fashion,” “It’s Fashion Metro” and “Versona.”" — [Cato Corp, Form 10-K FY2025, filed 2026-03-25](https://www.sec.gov/Archives/edgar/data/18255/000156276226000041/cato-20260131.htm)
  - Listing: "The Company’s Class A Common Stock trades on the New York Stock Exchange (“NYSE”) under the symbol CATO." — same 10-K
  - Control: "Further, we qualify for exemption as a “controlled company” from compliance with certain New York Stock Exchange corporate governance listing standards" — same 10-K
  - 5% holders: the ownership table reads "John P. D. Cato (2) 1,404,251 7.8 1,763,652 100.0 53.3" and "Aldebaran Capital, LLC (3) 1,123,131 6.2 — — 3.1" — [Cato Corp, DEF 14A, filed 2026-04-10](https://www.sec.gov/Archives/edgar/data/18255/000120677426000206/cato4585991-def14a.htm). The last figure is percent of total voting power.
  - Affiliate: none found (catofashions.com homepage HTML has no affiliate link).
  - BDC names: "Cato Corporation", "The Cato Corporation", "CATO CORP"
  - Notes: It's Fashion is family apparel ("for the entire family"), and Versona has no separate count, so neither is its own row. Form ADV for Aldebaran Capital, LLC not checked.
- **WA2 maurices**
  - Owner: "today announced that it has completed the sale of Maurices Incorporated (“maurices”) to an affiliate of OpCapita LLP (“OpCapita”)." — [ascena retail group, Exhibit 99.1, "ascena retail group Completes Sale of maurices", May 6, 2019](https://www.sec.gov/Archives/edgar/data/1498301/000149830119000036/a991mauricesfinal.htm)
  - Stake: "The Company received approximately $210 million in cash before expenses, and an approximately 49.6% interest in the OpCapita affiliate that is now the owner of maurices." — same exhibit
  - Owner kind: "OpCapita is a sector-focused private equity firm that specializes in transforming operationally underperforming businesses in the retail, consumer and leisure sectors." — same exhibit
  - Since: 2019-05-06 (dateline "MAHWAH, N.J., May 6, 2019").
  - Count: "We call 900 locations across the U.S. and Canada our hometowns." — [maurices, About page, accessed 2026-11-07](https://www.maurices.com/about-us)
  - Affiliate: "If you have a website, you can make money by referring customers to maurices.com. It's easy and it's free to join." — [maurices, Affiliate Program page](https://www.maurices.com/customer-service/affiliate-program). The same page names Rakuten LinkShare as the network.
  - BDC names: "Maurices Incorporated", "maurices"
  - Notes: current status not reconfirmed.
    - The maurices site doesn't name an owner.
    - opcapita.com now serves a domain-registrar parking page; WebFetch found no investments content, and www.opcapita.com doesn't resolve. A search snippet (not verified) said OpCapita's old investments page listed maurices as current.
    - Ascena, the 49.6% holder, later liquidated in bankruptcy; what happened to its stake was not checked.
- **WA3 Rainbow**
  - Owner: not found. The About page names no owner.
  - Count: "Rainbow started in Brooklyn in 1935 with one goal: make great style affordable for everyone. Almost 90 years later, we are still doing that with over 800 stores across the United States, Puerto Rico, and the U.S. Virgin Islands." — [Rainbow Shops, About page, accessed 2026-11-07](https://www.rainbowshops.com/pages/about-us)
  - Affiliate: the footer's embedded data includes `"text":"Affiliate Program","url":"https:\/\/signup.cj.com\/member\/signup\/publisher\/?cid=4615270#\/branded?_k=fzjcrj"` — same page's HTML (embedded JSON, not rendered text)
  - BDC names: "Rainbow Shops", "Rainbow USA, Inc." (name unverified)
  - Notes: Wikipedia (lead only) names the Chehebar family as owners. One web search found no primary source for that.
- **WA4 Victoria's Secret and PINK**
  - Owner: "Victoria’s Secret & Co. (together with its subsidiaries unless the context otherwise requires, “we”, “us”, “our” or the “Company”) is a specialty retailer of women’s intimates and other apparel and beauty products marketed under the Victoria’s Secret, PINK and Adore Me brand names." — [Victoria's Secret & Co., Form 10-K FY2025, filed 2026-03-20](https://www.sec.gov/Archives/edgar/data/1856437/000185643726000004/vsco-20260131.htm)
  - PINK: "PINK is a playful, bold and irreverent lifestyle brand for young women." — same 10-K
  - Count: store table "Company-Operated: U.S. 766 782 Canada 24 24" (January 31, 2026 vs. February 1, 2025) — same 10-K
  - Ticker: "The Company’s common stock began trading under the new ticker symbol VSXY on the New York Stock Exchange when markets opened on June 2, 2026." — [Victoria's Secret & Co., Form 10-Q for the quarter ended 2026-08-01, filed 2026-09-04](https://www.sec.gov/Archives/edgar/data/1856437/000185643726000021/vsco-20260801.htm)
  - 5% holders: "BlackRock, Inc. (3) 10,936,720 — 10,936,720 13.8 % BBRC International Pte Limited (4) 10,310,631 — 10,310,631 13.0 % Vanguard Portfolio Management (5) 4,707,006 — 4,707,006 5.9 %" — [Victoria's Secret & Co., DEF 14A, filed 2026-05-01](https://www.sec.gov/Archives/edgar/data/1856437/000119312526201438/vsco-20260430.htm)
  - Later holder change: Schedule 13D/A No. 7 (event date 07/28/2026) reports BBFIT Investments Pte Ltd, The BB Family International Trust, BBRC International Pte Ltd and Brett Blundy at 9.8% — [Schedule 13D/A, filed 2026-07-29](https://www.sec.gov/Archives/edgar/data/1856437/000121390026082834/primary_doc.xml) (XML form fields, no prose quote)
  - Model: "Additionally, we have more than 560 stores in approximately 70 countries operating under franchise, license and wholesale arra" (sentence continues "ngements") — 10-K above
  - Affiliate: none found for the US. Search returned network listings for VS Mexico, Saudi Arabia and UK only.
  - BDC names: "Victoria's Secret & Co."
  - Notes: BBRC is described in the 13D as a family trust structure (Brett Blundy). Its Form ADV status is not known, and it may not be an SEC filer. The assembler should check it for the strict count.
- **WA5 Torrid**
  - Owner: "As of January 31, 2026, Sycamore Partners Management, L.P. (“Sycamore”) controlled the voting power of a majority of our common stock. As a result, we are a “controlled company” within the meaning of the applicable stock exchange corporate governance standards." — [Torrid Holdings Inc., Form 10-K FY2025, filed 2026-03-31](https://www.sec.gov/Archives/edgar/data/1792781/000179278126000007/thi-20260131.htm)
  - 5% holders: "Sycamore Partners Management LP 58,295,694 — 58,295,694 58.59% Fund 1 Investments, LLC 10,433,112 — 10,433,112 10.49% Nomura Holdings Inc. 6,233,022 — 6,233,022 6.26%" — [Torrid Holdings Inc., DEF 14A, filed 2026-04-20](https://www.sec.gov/Archives/edgar/data/1792781/000179278126000021/thi-20260416.htm)
  - Listing: "Our common stock is listed on the New York Stock Exchange under the symbol “CURV” and began trading on July 1, 2021." — 10-K above
  - Count: "As of January 31, 2026, we operated 483 stores in the U.S., Puerto Rico and Canada." — 10-K above
  - Category: "is a direct-to-consumer brand in North America dedicated to offering a diverse assortment of stylish apparel, intimates, and accessories skillfully designed for curvy women." — 10-K above
  - Since: not found in the documents read. Sycamore was the controlling holder at the 2021 IPO, and the 10-K names Hot Topic, Inc. as a Sycamore affiliate.
  - Affiliate: none found (torrid.com homepage returned 403).
  - BDC names: "Torrid Holdings Inc.", "Torrid LLC"
- **WA6 KnitWell Group brands: Lane Bryant, Ann Taylor, LOFT, Talbots, Chico's, White House Black Market, Soma**
  - Owner (current): "KnitWell Group is a multi-brand retail company comprised of the iconic American apparel brands Ann Taylor, Chico's, Haven Well Within, Lane Bryant, LOFT, Soma, Talbots, and White House Black Market. A portfolio company of Sycamore Partners, KnitWell Group serves more than 21 million loyal customers nationwide" — [KnitWell Group, "KnitWell Group Appoints Jessica Sibley to Board of Directors", PR Newswire, June 23, 2026](https://www.prnewswire.com/news-releases/knitwell-group-appoints-jessica-sibley-to-board-of-directors-302808034.html)
  - Owner kind: "Sycamore Partners, a private equity firm specializing in consumer, distribution, and retail-related investments, today announced the formation of KnitWell Group ("KnitWell"), a new holding company comprising industry-leading apparel brands Ann Taylor , LOFT, and Talbots." — [Sycamore Partners and KnitWell Group, PR Newswire, Aug. 30, 2023](https://www.prnewswire.com/news-releases/iconic-apparel-brands-ann-taylor-loft-and-talbots-come-together-as-knitwell-group-301913882.html)
  - Lane Bryant in 2023: "The Company will also continue to provide oversight and shared services to Lane Bryant , a leading plus-size women's apparel brand." — same 2023 release. In 2026 KnitWell lists Lane Bryant among its brands (above).
  - Since, Ann Taylor, LOFT and Lane Bryant: "with Premium Apparel LLC (the “Purchaser”), an affiliate of Sycamore Partners Management, L.P. Pursuant to the Asset Purchase Agreement, on December 23, 2020, the Sellers completed their sale of assets relating to their Ann Taylor, LOFT, Lane Bryant and Lou & Grey brands to the Purchaser (the “363 Sale”) for approximately $540.0 million" — [Ascena Retail Group, Form 8-K, filed 2020-12-23](https://www.sec.gov/Archives/edgar/data/1498301/000110465920139140/tm2039145d1_8k.htm)
  - Since, Talbots: "As a result of the acceptance of the Shares tendered into the Offer on August 3, 2012, a change of control of the Company occurred." and "The funds used to consummate the Offer and the Merger were from equity contributions by Sycamore Partners, L.P. and Sycamore Partners A, L.P." — [Talbots Inc., Form 8-K, filed 2012-08-03](https://www.sec.gov/Archives/edgar/data/912263/000119312512334872/d391063d8k.htm)
  - Since, Chico's, WHBM and Soma: "On January 5, 2024, the Buyer Parties completed the acquisition of the Company." and "As a result of the consummation of the Merger, a change in control of the Company occurred, and the Company became a wholly owned subsidiary of Parent. Parent is an affiliate of Sycamore Partners Management, L.P." — [Chico's FAS, Inc., Form 8-K, filed 2024-01-05](https://www.sec.gov/Archives/edgar/data/897429/000095014224000046/eh240435596_8k.htm)
    - "today announced it has added Chico's, White House Black Market and Soma to its portfolio" and "This combination follows the sale of Chico's FAS to Sycamore Partners, a leading private equity firm specializing in consumer, distribution, and retail-related investments." — [KnitWell Group, PR Newswire, Jan. 5, 2024](https://www.prnewswire.com/news-releases/knitwell-group-adds-chicos-white-house-black-market-and-soma-302027182.html). Sycamore's own news page carries the same text: [sycamorepartners.com/news/article/2076](https://www.sycamorepartners.com/news/article/2076).
  - Count, Lane Bryant: 362 individual store-page links (pattern `state/city/address`) on the root directory [stores.lanebryant.com](https://stores.lanebryant.com/), accessed 2026-11-07. This is counted from links, not a stated figure. No other KnitWell brand gave a count. KnitWell's site says "3,000 retail stores" for all brands together ([knitwellgroup.com](https://www.knitwellgroup.com/)).
  - Model: company stores (KnitWell's site and the brand sites; no franchising found).
  - Affiliate: none found in the homepage HTML of talbots.com, loft.com, lanebryant.com, chicos.com, whitehouseblackmarket.com or soma.com. anntaylor.com redirected. Searches returned only network listings (FlexOffers, CJ) for Talbots, LOFT, Chico's and Ann Taylor.
  - BDC names:
    - Group: "KnitWell Group", "Knitwell Borrower LLC", "Knitwell Guarantor LLC" (the Chico's 8-K names these as borrower and holdings under a term loan agented by HPS Investment Partners, LLC);
    - Sycamore acquisition vehicles: "Premium Apparel LLC", "Daphne Parent LLC";
    - Operating companies and brands: "Premium Brands OpCo LLC" (the operating company named in a CA Transparency Act PDF linked from loft.com and anntaylor.com), "Chico's FAS, Inc.", "The Talbots, Inc.", "Lane Bryant".
  - Notes: an advisor exhibit in Walgreens' 2025 Schedule 13E-3 lists Sycamore's Ann Taylor/LOFT (2020) and Talbots (2012) investments as "Current" and says "Lane Bryant to be operated separately". This was not used as primary evidence; [d946494dex99c1.htm](https://www.sec.gov/Archives/edgar/data/1618921/000119312525079623/d946494dex99c1.htm).
- **WA7 Windsor**
  - Owner: "From the beginning, Windsor has been owned and operated by generations of the Zekaria family." — [Windsor, Our Story, accessed 2026-11-07](https://www.windsorstore.com/pages/our-story)
  - Count: "Windsor continues to bring this Oasis experience to you in over 350+ stores and through our online shop." — same page
  - Affiliate: "Become a Windsor Affiliate!" and "Joining Windsor Store's Affiliate Program is the perfect stepping stone for emerging Influencers and anyone looking to get their foot in the door for a career in fashion." — [Windsor, Affiliate page](https://www.windsorstore.com/pages/affiliate)
  - BDC names: "Windsor", "Windsor Fashions" (name unverified)
- **WA8 Aerie**
  - Owner and listing: 'Our common stock is traded on the NYSE under the symbol "AEO."' — [American Eagle Outfitters, Form 10-K FY2025, filed 2026-03-30](https://www.sec.gov/Archives/edgar/data/919012/000119312526132097/aeo-20260131.htm)
  - Brand: "Aerie offers the comfiest intimates, apparel, swim and accessories made to wear in and out." — same 10-K
  - Count: "As of January 31, 2026, we operated 332 Aerie brand stand-alone stores, inclusive of 47 OFFLINE stand-alone stores and 52 OFFLINE side-by-side stores connected to an Aerie brand location." — same 10-K. The 10-K also counts 184 Aerie side-by-sides inside AE stores.
  - 5% holders: "5% Beneficial Owners BlackRock, Inc. (4) 23,255,460 — 23,255,460 13.88 % Jay L. Schottenstein (5) (8) 10,931,325 2,047,602 12,978,927 7.65 % Dimensional Fund Advisors LP (6) 11,005,075 — 11,005,075 6.57 % Vanguard Portfolio Management (7) 10,440,147 — 10,440,147 6.23 %" — [AEO, DEF 14A, filed 2026-05-15](https://www.sec.gov/Archives/edgar/data/919012/000119312526227158/d70088ddef14a.htm)
  - Affiliate: ae.com, which also sells Aerie, embeds a footer string `"footer.affiliateProgram":"<a href=\"https://auth.rakutenmarketing.com/...\" class=\"footer-link-affiliate-program\" ...>Affiliate Program</a>"` — [ae.com homepage HTML, accessed 2026-11-07](https://www.ae.com/). This is JavaScript-embedded, not rendered text.
  - BDC names: "American Eagle Outfitters, Inc."
- **WA9 J.Jill**
  - Holder: "TowerBrook’s ownership percentage of our common stock was 49.2% as of April 6, 2026." — [J.Jill, Inc., DEF 14A, filed 2026-04-10](https://www.sec.gov/Archives/edgar/data/1687932/000119312526151285/d31291ddef14a.htm)
  - Holder entity: "TI IV JJill Holdings, LP (“ TI IV ”), an affiliate of TowerBrook Capital Partners L.P. (“ TowerBrook ”)" — same DEF 14A
  - 5% table: "Entities affiliated with TowerBrook (1) 7,338,933 49.2 % Royce & Associates LP (2) 1,204,103 8.1 % Paradigm Capital Management Inc. (3) 921,300 6.2 %" — same DEF 14A
  - Not control: "As a result, TowerBrook no longer controls a majority of the voting power of the Company’s outstanding voting stock and, therefore, the Company no longer qualifies as a “controlled company”" — [J.Jill, Form 10-K FY2025, filed 2026-03-31](https://www.sec.gov/Archives/edgar/data/1687932/000119312526134566/jill-20260131.htm)
  - Since: "10.17 Services Agreement, dated as of May 8, 2015, by and between Jill Acquisition LLC and TowerBrook Capital Partners L.P" — same 10-K (exhibit index)
  - Listing: "Our common stock began trading publicly on the NYSE under the symbol “JILL” on March 9, 2017." — same 10-K
  - Count: "As of January 31, 2026, we operated 256 stores in 42 states." — same 10-K
  - Affiliate: none found on the site. A LinkClicky listing (lead) shows a CJ program.
  - BDC names: "J.Jill, Inc.", "Jill Acquisition LLC", "J. Jill"
- **WA10 Athleta**
  - Owner: "Founded in 1998 and acquired by Gap Inc. in 2008, Athleta is certified as a benefit corporation ("B Corp") that bridges product innovation with style for women and girls." — [Gap Inc., Form 10-K FY2025, filed 2026-03-17](https://www.sec.gov/Archives/edgar/data/39911/000162828026018573/gap-20260131.htm)
  - Listing: 'The principal market on which our common stock is traded is the New York Stock Exchange (“NYSE”) under the symbol "GAP".' — same 10-K
  - Count: store table "Athleta North America 260 (8) 252 1.0" (fiscal 2025: start, net change, end, sq. ft.) — same 10-K
  - 5% holders: Robert J. Fisher 15.39%, William S. Fisher 16.09%, "John J. Fisher (8) 53,798,697 — 53,798,697 14.73 % The Vanguard Group (9) 25,386,921 — 25,386,921 6.95 % BlackRock, Inc. (10) 18,779,836 — 18,779,836 5.14 %" — [Gap Inc., DEF 14A, filed 2026-03-27](https://www.sec.gov/Archives/edgar/data/39911/000162828026021740/gps-20260325.htm)
  - Affiliate: none found (no link in athleta.gap.com homepage HTML).
  - BDC names: "Gap Inc.", "The Gap, Inc."
- **WA11 Anthropologie, Free People, FP Movement**
  - Owner and listing: "Our common shares are traded on the NASDAQ Global Select Market under the symbol “URBN.”" — [Urban Outfitters, Inc., Form 10-K FY2026, filed 2026-04-01](https://www.sec.gov/Archives/edgar/data/912615/000119312526137916/urbn-20260131.htm)
  - Anthropologie: "The Anthropologie brand tailors its merchandise and inviting store environment to sophisticated and contemporary women aged 28 to 45." — same 10-K
  - Anthropologie count: "As of January 31, 2026, we operated 254 Anthropologie stores, of which 234 were located in North America and 20 were located in Europe, and sold merchandise through franchisee-owned stores in the Middle East." — same 10-K
  - Free People: "The Free People brand focuses its product offering on private label merchandise targeted to contemporary women aged 25 to 30" — same 10-K
  - Free People and FP Movement count: "As of January 31, 2026, we operated 180 Free People brand stores, of which 167 were located in North America and 13 were located in Europe, and 88 FP Movement brand stores all located in North America." — same 10-K
  - 5% holders: "BlackRock, Inc. 55 East 52nd Street New York, NY 10005 8,018,860 (1) 9.07 % FMR LLC 245 Summer Street, Boston, Massachusetts 02210 4,916,110.59 (2) 5.56 % David A. Hayne 5000 Broad Street, Philadelphia, PA 19112 4,521,587 (3) 5.11 %" — [URBN, DEF 14A, filed 2026-04-01](https://www.sec.gov/Archives/edgar/data/912615/000119312526137990/d42640ddef14a.htm)
  - Affiliate: anthropologie.com/en-gb/become-an-affiliate came up in search (UK site; not fetched, as anthropologie.com returned 403). US: FlexOffers listing only. Free People and FP Movement: none found.
  - BDC names: "Urban Outfitters, Inc."
- **WA12 Aritzia**
  - Owner and listing: "VANCOUVER, October 8, 2026 – Aritzia Inc. (TSX: ATZ, "Aritzia", the "Company", "we" or "our"), a design house with an innovative global platform offering covetable styles online, on its app and in its boutiques" — [Aritzia, "Aritzia Reports Second Quarter Fiscal 2027 Financial Results", PDF on Aritzia's IR CDN](https://s21.q4cdn.com/489771965/files/doc_financials/2027/q2/Aritzia-Inc-Q2-2027-ER.pdf)
  - Count: "Boutique count3 at the end of Q2 2027 totaled 146 compared to 134 boutiques at the end of Q2 2026." — same PDF. The "3" is a footnote marker in the pypdf text, and the count covers the U.S. and Canada.
  - US weight: "Results continue to be driven by performance in the United States, where net revenue increased 57.7% to $1.42 billion, compared to $899.1 million in YTD 2026." — same PDF
  - 5% holders: not checked (Canadian filer; the circular is on SEDAR+).
  - Affiliate: none found (aritzia.com returned 403).
  - BDC names: "Aritzia Inc.", "Aritzia LP"
- **WA13 Johnny Was and Lilly Pulitzer**
  - Owner and listing: 'Our common stock is listed and traded on the New York Stock Exchange under the symbol "OXM."' — [Oxford Industries, Form 10-K FY2025, filed 2026-03-27](https://www.sec.gov/Archives/edgar/data/75288/000007528826000026/oxm-20260131.htm)
  - Lilly Pulitzer: "Lilly Pulitzer designs, sources, markets and distributes upscale collections of women’s and girl’s dresses, sportswear and related products." — same 10-K
  - Johnny Was: "During Fiscal 2025, approximately 90% of the net sales of Johnny Was were for women’s apparel" — same 10-K
  - Counts: store table "Lilly Pulitzer full-price retail stores 67 64 60 59 Johnny Was full-price retail stores 75 77 72 65 Johnny Was outlets 3 3 3 2 Total Johnny Was locations 78 80 75 67" — same 10-K. Also "As of January 31, 2026, there were 42 Lilly Pulitzer Signature Stores."
  - Model: "The Johnny Was direct to consumer distribution channel, which consists of e-commerce, full-price retail and outlet store operations, represented 81% of the Johnny Was net sales in Fiscal 2025." — same 10-K
  - Still held: the 10-Q for the quarter ended 2026-08-01 (filed 2026-09-04) reports Johnny Was as a segment ("Johnny Was Net sales $ 41,404"), with no sale or discontinued-operations language found — [10-Q](https://www.sec.gov/Archives/edgar/data/75288/000007528826000084/oxm-20260801.htm)
  - 5% holders: "FMR LLC 245 Summer Street Boston, MA 02210 2,231,608 (2) 15.0 % BlackRock, Inc. 50 Hudson Yards New York, NY 10001 2,058,807 (3) 13.8 % The Vanguard Group 100 Vanguard Blvd. Malvern, PA 19355 1,050,816 (4) 7.1 % Charles Schwab Investment Management Inc. 9800 Schwab Way Lone Tree, CO 80124 754,762 (5) 5.1 %" — [Oxford Industries, DEF 14A, filed 2026-05-13](https://www.sec.gov/Archives/edgar/data/75288/000007528826000032/oxm-20260513.htm)
  - Affiliate: none found in johnnywas.com homepage HTML. lillypulitzer.com returned 403; FlexOffers listing only.
  - BDC names: "Oxford Industries, Inc."
- **WA14 Altar'd State**
  - Owner: not found. altardstate.com returned 403 to robots.txt and the homepage, and one web search returned nothing relevant.
  - BDC names: "Altar'd State"
- **WA15 Charlotte Russe**
  - Owner: "Today, the Company has grown to include Urban Planet, Stitches, Urban Behavior, Sirens, Forever 21, Urban Kids, West 49, Amnesia, Bluenotes, Aeropostale, Thriftys, Suzy Shier, Le Chateau, Charlotte Russe, Mandee, and Rue 21." — [YM Inc., homepage ("Message From The Chairman"), accessed 2026-11-07](https://www.ym-inc.com/)
  - Site operator: the terms "apply to the use by you of the website at charlotterusse.com (the “ Site ”) of CR Clicks (2019) LLC (“ Company ”, “ we ” “ our ” or “ us ”)." and "This Site is controlled and operated by Company from Toronto, Ontario, Canada." — [Charlotte Russe, Terms and Conditions](https://www.charlotterusse.com/pages/terms-conditions)
  - Since: not found in a primary source (trade press: 2019, after Charlotte Russe's bankruptcy).
  - Affiliate: none found.
  - BDC names: "YM Inc.", "CR Clicks (2019) LLC", "Charlotte Russe"
  - Notes: YM's site doesn't state who owns YM. The Charlotte Russe About page has no body text in its HTML.
- **WA16 Madewell**
  - Owner: "As part of its financial restructuring, the Company has equitized more than $1 .6 billion of secured indebtedness, and Anchorage Capital Group, L.L.C. ("Anchorage") has become the majority owner of the Company." — [J.Crew Group, "J.Crew Group Successfully Emerges From Financial Restructuring Process…", PR Newswire, Sept. 10, 2020](https://www.prnewswire.com/news-releases/jcrew-group-successfully-emerges-from-financial-restructuring-process-positioned-for-sustainable-and-profitable-growth-301127788.html)
  - Brand in group: "We are energized by the opportunity ahead for the Madewell brand and ready to continue our momentum as we enter into a new phase of growth," said Libby Wadle , Chief Executive Officer of Madewell. — same release. Madewell.com's footer links "Belonging at J.Crew Group".
  - Lenders, not owners: "J.Crew Group is capitalized with a $400 million exit term loan due 2027 provided by Anchorage, as well as GSO Capital Partners LP and Davidson Kempner Capital Management LP, among others." — same release
  - Current: not reconfirmed. investors.jcrew.com returned 403.
  - Affiliate: none found on madewell.com. CJ and Admitad listings are leads only.
  - BDC names: "J.Crew Group, Inc.", "J.Crew Group, LLC", "Chinos Holdings" (unverified), "Madewell Inc."
  - Notes:
    - Anchorage's Form ADV flag decides whether this counts as PE.
    - A search snippet (not verified) says a successor adviser replaced Anchorage Capital Group in 2022.
    - Madewell also sells menswear. It is kept because it is women-led.
- **WA17 Fashion Nova**
  - Owner: not found. The About page tells the history without naming an owner: "What started in 2006 as one LA store has grown into a worldwide phenomenon." — [Fashion Nova, About page](https://www.fashionnova.com/pages/about-us)
  - Affiliate: none found in homepage HTML.
  - BDC names: "Fashion Nova, LLC" (unverified)
- **WA18 Lulus**
  - Owner and listing: "Our common stock is currently listed on the Nasdaq Capital Market under the symbol “LVLU” and began trading on the Nasdaq Global Market on November 11, 2021." — [Lulu's Fashion Lounge Holdings, Form 10-K FY2025, filed 2026-03-30](https://www.sec.gov/Archives/edgar/data/1780201/000110465926036884/lvlu-20251228x10k.htm)
  - Category: "Lulus is a women’s clothing brand offering modern, feminine styles at accessible prices for every occasion." — same 10-K
  - Holders: "As of April 15, 2026, entities affiliated with H.I.G. Growth Partners beneficially owned 32.1% of our common stock, entities affiliated with CPPIB beneficially owned 17.5% of our common stock and entities affiliated with IVP Holdcos beneficially owned 17.6% of our common stock." — [Lulus, DEF 14A, filed 2026-04-23](https://www.sec.gov/Archives/edgar/data/1780201/000114036126016365/ny20064169x2_def14a.htm)
  - Holder names: "entities affiliated with H.I.G Capital, LLC (“H.I.G.”), Institutional Venture Partners (“IVP”) and the Canada Pension Plan Investment Board (“CPPIB”)" — 10-K above
  - Affiliate: none found (lulus.com homepage returned 403).
  - BDC names: "Lulu's Fashion Lounge Holdings, Inc.", "Lulu's Fashion Lounge, LLC"
  - Notes:
    - The three holders are parties to a Stockholders Agreement and hold about 67% together.
    - No "controlled company" statement was found.
    - Counted as a PE minority stake: H.I.G. is the largest holder at 32.1%, short of control.
- **WA19 Princess Polly**
  - Owner: "a.k.a. Brands currently consists of four brands: two women’s brands, Princess Polly and Petal & Pup, and two streetwear brands, Culture Kings and mnml." — [a.k.a. Brands Holding Corp., Form 10-K FY2025, filed 2026-03-05](https://www.sec.gov/Archives/edgar/data/1865107/000186510726000008/aka-20251231.htm)
  - Control: "As of March 3, 2026, Summit Partners LP (“Summit”) beneficially owned approximately 56.0% of our common stock which means that, based on its percentage voting power, Summit controls the vote of all matters submitted to a vote of our Board or stockholders" — same 10-K. Also "Summit controls a majority of the voting power of our outstanding common stock. As a result, we are a “controlled company” within the meaning of the corporate governance standards of the NYSE."
  - Since: "Princess Polly Founded in Australia in 2010, Princess Polly joined a.k.a. Brands in July 2018." — same 10-K
  - Listing: "Our common stock has traded on the NYSE under the symbol “AKA” since our initial public offering on September 22, 2021." — same 10-K
  - Stores: "Princess Polly expanded its physical retail footprint by opening five stores across the United States in 2024 and seven additional stores in the United States and one store in Australia in 2025." — same 10-K
  - Affiliate: none found in homepage HTML.
  - BDC names: "a.k.a. Brands Holding Corp.", "Princess Polly"
- **WA20 Reformation**
  - Owner: "Headquartered in Los Angeles and founded in 2009, Reformation is a digitally-led women’s contemporary apparel brand." and "DETAILS Sector Consumer Country or Region USA Status Current Website www.thereformation.com 2019 Investment year 85% Direct to consumer" — [Permira, Portfolio: Reformation, accessed 2026-11-07](https://www.permira.com/portfolio/reformation)
  - Owner kind: "We are a specialist Private Equity and Credit platform with a transatlantic focus." — same page (site header)
  - Stake: not stated on the page. Counted as control under the "no stated stake" rule.
  - Affiliate: "You’re probably here for info about our affiliate program. Basically if you love us, you can write about us and earn a commission when your readers buy something from Ref." — [Reformation, Ref Affiliates](https://www.thereformation.com/ref-affiliates.html)
  - BDC names: "Reformation", "The Reformation"
- **WA21 Shein**
  - Owner: not found.
  - US operator: "In the United States, the Site and the App are provided by SHEIN US Services, LLC." — us.shein.com page data (privacy-policy text embedded in [Terms-and-Conditions-a-282.html](https://us.shein.com/Terms-and-Conditions-a-282.html) HTML; the page renders only with JavaScript)
  - Affiliate: none checked beyond search.
  - BDC names: "SHEIN US Services, LLC", "Roadget Business Pte. Ltd." (unverified)
  - Notes: Shein is headquartered outside the US. It is kept as the largest online-first seller of women's apparel to US shoppers, and the developer may drop it.
- **WA22 Skims**
  - Owner: not found. The skims.com About page HTML names no owner.
  - Affiliate: none found in homepage HTML.
  - BDC names: "SKIMS Body, Inc." (unverified)

### Rollups and groups that are not brands
Not counted in the 32.
- **KnitWell Group:** owned by Sycamore Partners ("A portfolio company of Sycamore Partners", 2026). Brands: Ann Taylor, LOFT, Lane Bryant, Talbots, Chico's, White House Black Market, Soma and Haven Well Within. Premium Apparel LLC (2020 buyer) and Daphne Parent LLC (2024 buyer) are Sycamore acquisition vehicles. "Chico's FAS" is now a former public parent inside KnitWell.
- **Victoria's Secret & Co.:** public (VSXY). Brands: Victoria's Secret, PINK, Adore Me, DailyLook.
- **Urban Outfitters, Inc.:** public (URBN). Brands: Anthropologie, Free People, FP Movement, and Urban Outfitters (unisex, not a row).
- **Gap Inc.:** public (GAP). Brands: Athleta, plus the unisex Old Navy, Gap and Banana Republic (not rows).
- **American Eagle Outfitters, Inc.:** public (AEO). Brands: Aerie and OFFLINE, plus American Eagle (unisex, not a row).
- **Oxford Industries, Inc.:** public (OXM). Brands: Lilly Pulitzer and Johnny Was, plus Tommy Bahama (not a row).
- **Cato Corporation:** public (CATO), family-controlled. Banners: Cato, It's Fashion, Versona, Cache.
- **a.k.a. Brands Holding Corp.:** public (AKA), controlled by Summit Partners. Brands: Princess Polly, Petal & Pup, Culture Kings, mnml.
- **J.Crew Group:** Anchorage Capital Group majority owner since 2020 (not reconfirmed). Brands: Madewell, J.Crew.
- **YM Inc.:** private, owners not stated. Banners: Charlotte Russe, rue21, Urban Planet and others.
- **Torrid Holdings Inc.:** public, Sycamore-controlled. One brand (Torrid).

### Category share
N = 32 brand rows.
- **PE-owned (control): 10 / 32 = 31.3%.**
  - Via Sycamore Partners (8): Torrid (58.59%, NYSE-listed), Lane Bryant, Ann Taylor, LOFT, Talbots, Chico's, White House Black Market, Soma.
  - Princess Polly: Summit Partners, 56.0% of a.k.a. Brands (NYSE-listed).
  - Reformation: Permira, stake not stated.
- **PE minority stake: 2 / 32 = 6.3%.**
  - J.Jill: TowerBrook 49.2%. Not a controlled company since June 2024.
  - Lulus: H.I.G. Growth Partners 32.1%. IVP holds 17.6% and CPPIB 17.5%.
- **PE-owned plus PE minority stake: 12 / 32 = 37.5%.**
- **PE or investment-firm owner on record, current status not reconfirmed: 2 / 32 = 6.3%.**
  - maurices: OpCapita affiliate, 2019.
  - Madewell: Anchorage Capital Group majority of J.Crew Group, 2020. Anchorage's PE status depends on its Form ADV.
- **Upper bound if both are reconfirmed: 14 / 32 = 43.8%.**
- **Public company, no PE holder found: 11 / 32 = 34.4%.**
  - The rows: Cato; Victoria's Secret and PINK; Aerie; Athleta; Anthropologie, Free People and FP Movement; Johnny Was and Lilly Pulitzer; Aritzia (5%+ holders not checked).
  - Two of these have a 5%+ holder whose ADV status is unknown:
    - Cato: Aldebaran Capital, LLC, 6.2%. If it reports PE funds, the strict count adds 1 row.
    - Victoria's Secret and PINK: BBRC International Pte Limited, 13.0% in the proxy and 9.8% by July 2026. It is a family-trust vehicle and adds 2 rows if flagged, which is unlikely.
- **Other: 2 / 32 = 6.3%.**
  - Windsor: family-owned (Zekaria).
  - Charlotte Russe: private company YM Inc., whose owners are not stated.
- **Not found: 5 / 32 = 15.6%.** Rainbow, Altar'd State, Shein, Fashion Nova and Skims.
- **Glossary-strict count:**
  - As counted: 12 / 32 (37.5%). The 4 public rows with PE holders (Torrid, Princess Polly, J.Jill, Lulus) are already in the share above.
  - Range: 12–15 / 32, depending on the Aldebaran and BBRC ADV checks.
- **By parent company:** the 32 rows have 22 distinct parents or owners.
  - PE-controlled: 4 / 22 parent companies. They are Torrid Holdings and KnitWell Group (both Sycamore), a.k.a. Brands (Summit) and Reformation (Permira). That is three sponsors.
  - PE minority stake: J.Jill and Lulus, 2 / 22.
  - **Together: 6 / 22 = 27.3%.**
  - Upper bound with the maurices owner and J.Crew Group: 8 / 22 = 36.4%.
- **By sales:** not computed. Brand-level US sales aren't public for most rows. Two figures for scale:
  - KnitWell said its brands generate "approximately $6 billion in annual sales" (January 2024 release).
  - Aritzia's US net revenue was C$1.42 billion for the first half of fiscal 2027.
- **Sources disagree:** none. Lane Bryant differs on framing only. In 2023 KnitWell "provide[s] oversight and shared services" to Lane Bryant; in 2026 KnitWell lists Lane Bryant as one of its brands. Both put Sycamore in the chain.
- **Formerly PE-owned among the other rows:** not checked. Aritzia and Victoria's Secret had earlier sponsor or parent histories that were not part of this audit.

## Firms named
Every investment firm named as an owner, 5%+ holder or relevant lender, as the sources name it, for the assembler's Form ADV check:
- **Owners or controlling holders:**
  - Sycamore Partners Management, L.P. Also "Sycamore Partners, L.P." and "Sycamore Partners A, L.P." (2012 Talbots funding).
  - Summit Partners LP. The DEF 14A names fund entities including "Summit Partners, L.P.", "Summit Partners Growth Equity Fund IX-A AIV, L.P." and "Excelerate, L.P.".
  - Permira (Reformation).
  - OpCapita LLP (maurices, 2019).
  - Anchorage Capital Group, L.L.C. (J.Crew Group/Madewell, 2020).
- **PE minority holders:**
  - TowerBrook Capital Partners L.P., via TI IV JJill Holdings, LP (J.Jill, 49.2%).
  - H.I.G. Growth Partners and H.I.G Capital, LLC (Lulus, 32.1%).
  - Institutional Venture Partners (IVP Holdcos) (Lulus, 17.6%).
  - Canada Pension Plan Investment Board (Lulus, 17.5%).
- **Other 5%+ holders of public parents:**
  - Fund 1 Investments, LLC (Torrid, 10.49%).
  - Nomura Holdings Inc. (Torrid, 6.26%).
  - Aldebaran Capital, LLC (Cato, 6.2%).
  - BBRC International Pte Limited, BBFIT Investments Pte Ltd and The BB Family International Trust (Victoria's Secret, 13.0% then 9.8%).
  - Royce & Associates LP (J.Jill, 8.1%).
  - Paradigm Capital Management Inc. (J.Jill, 6.2%).
  - Dimensional Fund Advisors LP (AEO, 6.57%).
  - Charles Schwab Investment Management Inc. (Oxford, 5.1%).
  - FMR LLC (Oxford 15.0%, URBN 5.56%).
  - BlackRock, Inc., and The Vanguard Group or Vanguard Portfolio Management (several parents).
- **Lenders named (not owners):**
  - HPS Investment Partners, LLC: agent on the Knitwell Borrower LLC term loan.
  - GSO Capital Partners LP and Davidson Kempner Capital Management LP: J.Crew 2020 exit term loan.
- **Named in a lead only (not a row):** Blackstone (Spanx majority, 2021; release pages returned 403).

## Worker log
- **Time:** start 2026-11-07T16:59:12Z, end 2026-11-07T17:24Z, about 25 minutes for 32 rows including writing and a self-check.
- **Calls:**
  - 21 WebSearch.
  - 7 WebFetch: 2 ranking candidates read and rejected, 1 parked-domain page, 1 DNS failure, 3 blocked with 403 (Business Wire twice, Blackstone once).
  - 170 direct HTTP requests with curl, logged one per line.
- **SEC requests: 50.**
  - 1 ticker map and 11 submissions JSONs.
  - 22 10-K and DEF 14A documents.
  - 2 10-Qs (VS ticker check, Oxford Johnny Was check) and 2 Schedule 13D/A XML files.
  - 5 EDGAR full-text searches: Knitwell; Lane Bryant/Sycamore 2020–21; Talbots/Sycamore 2012; J.Crew twice.
  - 5 8-Ks: Ascena twice, Talbots twice, Chico's once.
  - 2 exhibits: Ascena's maurices release and the Walgreens 13E-3 advisor deck.
  - All returned HTTP 200.
- **The other 120 requests** were robots.txt checks (about 45 sites) and brand, sponsor and press-release pages.
- **Self-check:** a script string-matched 93 of the quotes cited above against the saved page or filing text, and 93 of 93 were found. Two altered quotes (a negative control) were not found.
  - Not in the script: the JavaScript-embedded strings, which were checked separately against raw HTML (Shein and Rainbow found; Aerie by eye), and the 13D/A XML fields.
- **Ranking cost:** 3 searches and 2 fetches. No ranking was usable.
- **What was cheap:**
  - Public parents: 2 EDGAR documents (10-K and DEF 14A) settled 15 rows from 9 parents, store counts included, with machine-checkable quotes.
  - Sycamore's KnitWell: one 2026 PR Newswire release settled current ownership of 7 rows. Three completion filings (Talbots 2012, Ascena 2020, Chico's 2024) gave the since-dates.
  - Family and private chains that state their own story: Windsor's "Our Story" page settled owner and count in one fetch.
- **What made brands slow:**
  1. **Store counts for private brands.** The KnitWell brands' store finders are JavaScript-only or redirect, and two store subdomains don't resolve. Only Lane Bryant's Yext-style directory could be counted. This cost about 14 requests and settled one count.
  2. **Old PE deals with no current confirmation.** maurices' sponsor (OpCapita) now has a parked domain. J.Crew's investor site returns 403. The last primary statements are from 2019 and 2020.
  3. **Blocked sponsor and newswire pages.** Blackstone (Cloudflare), Business Wire and newswire.ca returned 403 to curl and WebFetch. That left Spanx's 2021 deal unquotable, which is one reason Spanx is not a row.
  4. **Sites returning 403 to curl:** aritzia.com, altardstate.com, anthropologie.com, freepeople.com, lillypulitzer.com, lulus.com, torrid.com, investors.jcrew.com and francescas.com (423). The public-company owners were settled from EDGAR anyway; Altar'd State was not.
  5. **No free ranking.** The composite rests on each brand's own count, so 15 rows can't be strictly ordered. Six online-first brands have no shared measure.
- **Which kinds of brands had no primary source for the owner:**
  - Founder- or family-held private chains whose sites don't name an owner: Rainbow, Altar'd State.
  - Large online-first private brands: Shein (only the US operating LLC is named), Fashion Nova, Skims.
  - A private Canadian group's owners: YM Inc., which owns Charlotte Russe.
- **Affiliate programs:**
  - Checked with homepage-HTML greps on 30 brand domains and 2 site-restricted searches.
  - Five brand-direct programs found: Windsor, Rainbow (CJ link), maurices (Rakuten), Aerie (Rakuten link on ae.com) and Reformation.
  - Most Knitwell, URBN and Oxford brand sites render their footers with JavaScript, so a program could exist and not show. FlexOffers and CJ listings for Talbots, LOFT, Chico's, Ann Taylor, Lilly Pulitzer, Madewell, J.Jill and Anthropologie US suggest they do (leads only).
  - Women's apparel looks like a high-affiliate category compared with restaurants. Of the 5 confirmed programs, 1 is on a PE-owned row (Reformation) and 1 on a PE-on-record row (maurices).
- **Quote caveats for the assembler:**
  - JavaScript-embedded quotes are not in rendered text. They are in the raw HTML: Rainbow and Aerie footer affiliate JSON, and Shein's "SHEIN US Services, LLC" sentence. Match them against raw HTML, not visible text.
  - The Aritzia quote comes from a PDF (pypdf text), including the footnote marker "count3".
  - The Lane Bryant count of 362 is computed from links, not quoted.
  - The J.Crew release has "$1 .6 billion" with a stray space from an inline tag.
  - SEC table rows are quoted as flattened text.
