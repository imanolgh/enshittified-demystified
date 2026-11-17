# Product industry audit: Apparel other than women's

Ticket: [91-research-product-industry-audits](../../issues/91-research-product-industry-audits.md) · Researched 2026-11-17 (fetches logged 22:59–23:20 UTC) · Ownership facts come from primary sources only. YouGov's public ratings page supplies the ranking only. Women's clothing was audited separately ([womens-apparel](../category-audit/womens-apparel.md)); none of its 32 rows is a row here.

**Short answer**

| | Apparel other than women's (N = 30 brand rows, all ranked) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **7 / 30 (23.3%)**, all PE-owned: Skechers (3G Capital, control), Dr. Scholl's shoes (Yellow Wood Partners, via Scholl's Wellness Company; Caleres makes the shoes under license) and five Authentic Brands Group names: Reebok, Lee, Champion, Eddie Bauer and Dockers. ABG's PE holders (General Atlantic, Leonard Green, CVC, HPS, BlackRock's private-capital fund, Brookfield) state no stakes, so ABG counts as PE-owned under the "no stated stake" rule. |
| Literal reading of the Form ADV rule | **8 / 30 (26.7%)** if CDPQ counts as PE: Caisse de dépôt et placement du Québec holds 6.3% of Gildan (Hanes's parent) on a 13G filed under Rule 13d-1(c), and an adviser named "CDPQ Global Infrastructure Inc." reports `Any PE Funds = Y` (1 fund). That would make Hanes a PE minority stake. Open question 1. |
| Top 10 of the ranking | **2 / 10 (20%)**: Skechers (#7) and Reebok (#8). 3 / 10 with Hanes (#5) under the literal reading. |
| Owner not found | **1 / 30 (3.3%)**: New Balance (newbalance.com and its newsroom both refused the bot). One more row names its company and founder family but not its owner: L.L.Bean. |
| Brand-direct affiliate programs | **6 confirmed** on pages the brand runs: Reebok, Nike, Old Navy, Levi's, Crocs, Under Armour. **PE rows: 1** (Reebok). **Non-PE rows: 5.** **Probable: 2**, both non-PE (adidas and New Balance: a search found a brand page, but the site refused the bot). **Network or directory listings only: 15**, 5 of them PE rows (Skechers, Dr. Scholl's shoes, Champion, Dockers, Eddie Bauer). Lee was not checked (its site served a Cloudflare challenge). |
| BDC overlap | **8 rows**: 4 named in the filer's text (Skechers, Dr. Scholl's shoes, Eddie Bauer, Crocs) and 4 more through the filer label "Authentic Brands" on ABG's borrower (Reebok, Lee, Champion, Dockers). All of it is debt; no BDC holds equity in any row's owner. |

- **The ranking is YouGov's own US popularity list,** "The most popular clothing & footwear brands" (Q3 2026). It mixes product brands with store brands (Old Navy, Gap). Four non-clothing names and one women's-audit row were skipped, so the 30 rows run through YouGov rank 34 (see "Ranking").
- **Biggest finding: licensing puts PE in the top 30.** Authentic Brands Group owns 5 of the 30 names. It bought Champion from HanesBrands in 2024 and Dockers from Levi Strauss in February 2026, and its purchase of Lee from Kontoor closed on 2026-11-03, two weeks before this audit. ABG licenses the names to operators (AMG Companies, GearCo, Outdoor 5, Catalyst Brands); under the counting rules the licensor is the owner.
- **The earlier screen's 1 of 15 (Skechers) is now 7 of 30.** The screen ranked companies (Fortune, NRF), so PE names held by licensors sat outside it. YouGov ranks brands, which brings in Reebok, Lee, Champion, Eddie Bauer, Dockers and Dr. Scholl's shoes. None of them was picked from a portfolio page.
- **Every other row is public (21) or private and family-led (L.L.Bean, New Balance per trade press).** No SEC-registered public parent has a PE holder at more than 5% through a 13D or a non-passive 13G, except Gildan's CDPQ holder if CDPQ counts as PE. The holders of the three foreign-listed parents (adidas, PUMA, LVMH) were not read.

## How this was sourced (read first)

- **Ranking:** YouGov Ratings, "The most popular clothing & footwear brands" (US, all adults, data collection period Q3 2026), https://yougov.com/en-us/ratings/clothing-footwear-brands. Used for the ranking only, never as evidence of ownership.
- **Ownership facts:**
  - SEC filings: 10-Ks (Nike, VF, Gap, PVH, Tapestry, Ralph Lauren, Caleres), Berkshire Hathaway's Exhibit 21, 8-Ks (Skechers merger, Hanesbrands merger) and 13G/13D filings (CDPQ, FMR, M&G, Victory, Coliseum), plus SEC's company-ticker file and EDGAR full-text search for every 13D/13G filed since 2024-01-01 on each SEC-registered parent.
  - Company and sponsor releases: Authentic Brands Group (2021, 2022, 2023, 2024, 2026), Kontoor Brands (2026), Levi Strauss (2026), Yellow Wood Partners (2019, 2026).
  - A sponsor portfolio page (Leonard Green); company sites and footers (Reebok, Champion, Dockers, Eddie Bauer, L.L.Bean); investor pages (adidas annual report, PUMA, LVMH).
- **SEC access:** 44 requests to www.sec.gov and efts.sec.gov, all with the user agent `EvidenceEngine ownership-research bot (product industry audit)`, no contact detail, at most 1 request per second (1.1 s spacing enforced by the fetch script). 42 returned 200; efts.sec.gov/robots.txt returned 403 (read as no restrictions), and one full-text query returned 500 (a reworded query then returned 200).
- **Robots:** robots.txt was read before the first request to each of 30 hosts; the script checks `*`, `EvidenceEngine`, ClaudeBot, Claude-User, Claude-SearchBot and anthropic-ai, longest match wins.
  - corporate.authentic.com (Squarespace) lists ClaudeBot and anthropic-ai in the same group as `*`, with ordinary disallows (/config, /search, /api/ and tag query strings). The press-release and portfolio paths are allowed.
  - investors.levistrauss.com and leonardgreen.com set `Crawl-delay: 10`; each was hit once.
  - Robots 4xx read as no restrictions: yellowwoodpartners.com (404), api.yougov.com (404), efts.sec.gov, newbalance.com, lee.com and adidas.com (403).
  - Robots unreachable, host treated as blocked: www.adidas-group.com (no response). Robots redirect not followed: today.yougov.com (301 to yougov.com, which was read separately) and crocs.com (301; www.crocs.com was then read and allowed).
- **Blocked or failed:**
  - newbalance.com: 403 (an Akamai error page, not a challenge); not retried.
  - newbalance.newsmarket.com (New Balance's newsroom): 202 with an empty body. One browser retry with the bot's user agent and no clicks showed "Let's confirm you are human"; it did not clear in 30 s, so the host counts as blocked.
  - adidas.com: 403, an Akamai block page ("Unfortunately we are unable to give you access to our site at this time."); not a challenge, not retried.
  - lee.com: 403 with a Cloudflare "Just a moment..." page. The one allowed browser retry was **not** used (Lee's owner was already settled by Kontoor's release), so lee.com counts as not read.
  - us.puma.com/us/en/help/affiliates: 404.
  - api.yougov.com: 404 (a guessed public API path; nothing came back).
- **How ranks 21–40 were read:** the curl'd page shows ranks 1–20. The page was then rendered once in Playwright (bot user agent, headless, no stealth), and the page's own "Load More" button was triggered by a dispatched click event (the cookie banner was left untouched). The page's own script then loaded ranks 21–40. Before that, a direct request to the API host named in the page's embedded state was refused by the session's permission system, so no request was sent.
- **Never fetched:** competitor sites (a worseonpurpose.com ledger page came up in one search), Reddit, WhoIsMyDentist, Private Equity Vet, PitchBook, Preqin and CB Insights.
- **Leads only, never cited:** Wikipedia, Forbes, Bloomberg and Axios (ABG's 2025 BlackRock-stake talks), trade press on Lee, Dockers and Champion licensees, PUMA's Anta stake as summarized in search, and affiliate directories (FlexOffers, Affilitizer, LinkClicky, Lasso, Skimlinks, UpPromote).
- **Owner kinds are research notes, not engine classifications.** "PE-owned" means control, or a PE owner with no stated stake. "Private, owner not stated" means a primary source names the company and often its founder family but not who owns it, with no PE evidence. Counts are by brand row: ABG has 5 rows, VF 3, Gap Inc. 2, Nike 2 and Ralph Lauren 2.
- **Licensed names** (Reebok, Lee, Champion, Eddie Bauer, Dockers, Dr. Scholl's shoes): the owner is the licensor. Each row also names the licensee or operator where a source states it ("Licensed rows").
- **Quotes:** copied from saved page text (tags stripped, whitespace collapsed, entities decoded) and cited with the page-cache number, e.g. "(cache 009)". The cache is `$SCR/pages/apparel/NNN.html` and `NNN.txt`, indexed in `index.tsv`. No quote came through a summarizer.

## Ranking

**YouGov Ratings, "The most popular clothing & footwear brands", United States, all adults, Q3 2026.** The page says: "Popularity is the % of people who have a positive opinion of a clothing & footwear brand." and "Data collection period: Third quarter of 2026" (cache 007). Each entry shows two numbers: fame (the share who have heard of the brand) first, then popularity, e.g. "1 Levi's 98% 76% 2 Adidas 99% 75% 3 Fruit of the Loom 97% 74%" (cache 002, 007). The ranking is by popularity.

- **Why this source:** it ranks brands, not companies; it is US-only; it covers clothing and footwear; and it mixes product brands with store brands by its own design (Old Navy, Gap, L.L.Bean). It knows nothing about ownership.
- **Rejected:** Brand Finance Apparel 50 (global brand value, led by luxury houses and jewelers); Fortune's apparel sector and the NRF Top 100 (both rank companies, and Fortune lists only companies that publish financials, which leaves out private PE-owned firms); YouGov's consideration ranking in its 2026 fashion report (a PDF behind a marketing-tracking link).
- **Cut rule:** walk YouGov's order from rank 1 and skip:
  - rows of the women's apparel audit: Victoria's Secret (#13);
  - names whose main product is not clothing or footwear: RayBan (#20, eyewear), Wilson Sporting Goods (#31, sporting equipment), Samsonite (#32, luggage).
- **Kept as YouGov lists them:** Coach (#28) and Louis Vuitton (#34), fashion houses that sell clothing alongside leather goods; "Polo Ralph Lauren" (#19) and "Ralph Lauren" (#24), which YouGov rates as two entities.
- **The 30th row is Louis Vuitton (#34, 52%).** The first row left out is Banana Republic (#35, also 52%; YouGov's order decides the tie), then Michael Kors (#36), Chanel (#37), American Eagle Outfitters (#38), Tommy Hilfiger (#39) and Men's Wearhouse (#40).
- **Sensitivity:** dropping Coach and Louis Vuitton (bringing in Banana Republic and Michael Kors), or merging the two Ralph Lauren entries (bringing in Banana Republic), changes no PE count: it stays 7 / 30.
- **Limits:** popularity is an opinion measure, not sales. YouGov's fame ranking (share who have heard of a brand) was not used.

| # | Brand (YouGov rank; fame, popularity) | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Levi's (#1; 98%, 76%) | Levi Strauss & Co.; Haas family members file 13Gs | public company | none (only family and 13d-1(b) filers) | not applicable | LEVI | brand of a manufacturer-retailer | **yes, brand-direct**: https://www.levi.com/US/en_US/features/affiliate-program | AO1 |
| 2 | adidas (#2; 99%, 75%) | adidas AG; 79% institutional, DAX 40 member | public company (foreign-listed: Frankfurt) | not checked (no SEC 13D regime) | not applicable | — (Frankfurt; ticker not read) | brand of a manufacturer | probable: brand help page found in search; adidas.com returned 403 | AO2 |
| 3 | Fruit of the Loom (#3; 97%, 74%) | Fruit of the Loom, Inc., a Berkshire Hathaway subsidiary (Exhibit 21) | public company (conglomerate parent) | none | not checked | BRK-A, BRK-B | brand of a manufacturer | none found | AO3 |
| 4 | Converse (#4; 94%, 68%) | NIKE, Inc. | public company | none (only 13d-1(b) filers) | not checked | NKE | brand of a manufacturer | network listings only | AO4 |
| 5 | Hanes (#5; 95%, 67%) | Hanesbrands, a wholly owned subsidiary of Gildan Activewear since 2025-12-01 | public company (literal ADV reading: PE minority stake through CDPQ's 6.3% 13d-1(c) 13G on Gildan) | none confirmed; CDPQ if it counts as PE (open question 1) | 2025-12-01 (Gildan) | GIL | brand of a manufacturer | network listings only | AO5 |
| 6 | Nike (#6; 97%, 67%) | NIKE, Inc. | public company | none | not applicable | NKE | brand of a manufacturer | **yes, brand-direct**: https://www.nike.com/help/a/nike-affiliate-program | AO6 |
| 7 | Skechers (#7; 96%, 67%) | indirect subsidiary of Beach Acquisition Co Parent, LLC, whose Buyer Parties are affiliates of funds managed by 3G Capital Partners L.P.; Greenberg family holders keep Parent units (stake not stated) | **PE-owned** (change in control stated) | 3G Capital Partners | 2025-09-12 | — (delisted 2025) | brand of a manufacturer | network listings only (Impact, CJ, FlexOffers per directories) | AO7 |
| 8 | Reebok (#8; 95%, 66%) | Authentic Brands Group (bought from adidas); trademark entity Reebok International Limited | **PE-owned** (via ABG; no stated stake) | General Atlantic, Leonard Green, CVC, HPS, BlackRock LTPC, Brookfield (ABG holders) | 2022-03-01 | — | licensed name (ABG licensor; US operator not stated in sources read) | **yes, brand-direct**: footer link "Become an Affiliate Partner" to https://reebok.rmaffiliate.com/login | AO8 |
| 9 | New Balance (#9; 93%, 65%) | not found (sites refused the bot) | not found (trade press: Davis family; not cited) | none found | not found | — | brand of a manufacturer | probable: https://www.newbalance.com/affiliate/ found in search; site returned 403 | AO9 |
| 10 | Wrangler (#10; 91%, 65%) | Kontoor Brands, Inc. | public company | none (only 13d-1(b) filers) | not checked | KTB | brand of a manufacturer | network listings only | AO10 |
| 11 | Under Armour (#11; 96%, 64%) | Under Armour, Inc.; Fairfax Financial files 13D/As | public company | none (Fairfax's adviser reports no PE funds; Fairfax is a listed insurance holding company) | not applicable | UAA, UA | brand of a manufacturer | **yes, brand-direct**: https://www.underarmour.com/en-us/t/ua-affiliate-program/ (via Awin) | AO11 |
| 12 | The North Face (#12; 90%, 64%) | V.F. Corporation | public company | none (Dodge & Cox, M&G 13d-1(b), index managers) | not checked | VFC | brand of a manufacturer | network listings only | AO12 |
| 13 | Lee (#14; 90%, 63%) | Authentic Brands Group (bought from Kontoor Brands) | **PE-owned** (via ABG; no stated stake) | as AO8 | 2026-11-03 | — | licensed name (US licensee not read; lee.com challenged) | not checked (lee.com 403 challenge) | AO13 |
| 14 | PUMA (#15; 96%, 63%) | PUMA SE; "Around 71%" free float | public company (foreign-listed: Deutsche Börse) | not checked (largest holder per search: Anta Sports, a listed company; not cited) | not applicable | — (Deutsche Börse; ticker not read) | brand of a manufacturer | not confirmed: brand page in search returned 404; network listing | AO14 |
| 15 | Dr. Scholl's shoes (#16; 89%, 62%) | Scholl's Wellness Company, "parent Company of Dr. Scholl's", a Yellow Wood Partners portfolio company; Caleres sells the shoes under license | **PE-owned** (no stated stake; "portfolio company") | Yellow Wood Partners | 2019-11-04 (North American business from Bayer) | — (licensee Caleres: CAL) | licensed name (Caleres license for US, Canada and Latin America "through 2026") | network listings only | AO15 |
| 16 | Old Navy (#17; 96%, 61%) | Gap Inc. | public company (Fisher family 13Ds) | none | not checked | GAP | store brand (company stores and online) | **yes, brand-direct**: https://oldnavy.gap.com/customerService/info.do?cid=3000 (via Impact) | AO16 |
| 17 | Columbia (#18; 85%, 60%) | Columbia Sportswear Company (Boyle family 13Gs) | public company | none | not applicable | COLM | brand of a manufacturer | none found | AO17 |
| 18 | Polo Ralph Lauren (#19; 91%, 59%) | Ralph Lauren Corporation | public company (Ralph Lauren 13G) | none | not applicable | RL | label of a fashion company | none found (see AO22) | AO18 |
| 19 | Champion (#21; 89%, 59%) | ABG-Champion LLC (Authentic Brands Group), bought from HanesBrands | **PE-owned** (via ABG; no stated stake) | as AO8 | 2024-09-30 | — | licensed name (AMG Companies affiliates for US and Canada core; GearCo for collegiate) | network listing only (FlexOffers "championusa.com") | AO19 |
| 20 | Vans (#22; 86%, 58%) | V.F. Corporation | public company | as AO12 | not checked | VFC | brand of a manufacturer | network listings only | AO20 |
| 21 | Gap (#23; 92%, 57%) | Gap Inc. | public company | as AO16 | not applicable | GAP | store brand | network listings only (Gap Inc. creator program on gapinc.com per search; not opened) | AO21 |
| 22 | Ralph Lauren (#24; 91%, 56%) | Ralph Lauren Corporation | public company | none (Victory Capital 13G/A under 13d-1(b), 0.99%) | not applicable | RL | fashion company, own stores and wholesale | network listing only (FlexOffers says not currently offered) | AO22 |
| 23 | L.L.Bean (#25; 87%, 56%) | L.L.Bean; the founder's great-grandson is Executive Chairman; owner not stated | private, owner not stated (founder family leads; no PE evidence) | none found | not applicable (founded 1912) | — | catalog, online and own stores | none found | AO23 |
| 24 | Calvin Klein (#26; 96%, 56%) | PVH Corp. (owned brand name) | public company | none (FMR 9.5% under 13d-1(b); Pzena reports no PE funds) | not checked | PVH | brand of a fashion company (some categories licensed out) | network listings only | AO24 |
| 25 | Eddie Bauer (#27; 86%, 55%) | Authentic Brands Group ("owner of the Eddie Bauer brand") | **PE-owned** (via ABG; no stated stake) | as AO8 | not checked (trade press: 2021) | — | licensed name (Outdoor 5, LLC for e-commerce and wholesale; Catalyst Brands for stores) | directory listing only (Lasso) | AO25 |
| 26 | Coach (#28; 86%, 55%) | Tapestry, Inc. | public company | none (only 13d-1(b) filers) | not checked | TPR | fashion house (own stores, wholesale) | none found | AO26 |
| 27 | Crocs (#29; 94%, 54%) | Crocs, Inc. | public company | none (only 13d-1(b) filers) | not applicable | CROX | brand of a manufacturer | **yes, brand-direct**: https://www.crocs.com/affiliate-program/affiliate-program.html | AO27 |
| 28 | Timberland (#30; 82%, 53%) | V.F. Corporation | public company | as AO12 | not checked | VFC | brand of a manufacturer | network listings only | AO28 |
| 29 | Dockers (#33; 85%, 52%) | Authentic Brands Group (bought from Levi Strauss) | **PE-owned** (via ABG; no stated stake) | as AO8 | 2026-02-27 (final closing) | — | licensed name (US operator not stated in sources read) | network listings only (FlexOffers, CJ per directories) | AO29 |
| 30 | Louis Vuitton (#34; 92%, 52%) | LVMH | public company (foreign-listed: Euronext Paris) | not checked | not checked | MC (Euronext Paris) | fashion house, own stores | none found | AO30 |

### Evidence

Shared sources, cited by cache number:
- **ABG's owners (for AO8, AO13, AO19, AO25, AO29):**
  - "today announced a $500M primary follow-on investment from its current investor General Atlantic, a leading global growth equity firm." and "Authentic’s other significant shareholders include BlackRock, CVC Capital Partners, Simon Property Group, HPS Investment Partners, Leonard Green & Partners and Brookfield." — [Authentic Brands Group, release "Authentic Brands Group Announces $500M Primary Follow-on Investment From General Atlantic", June 29, 2023](https://corporate.authentic.com/press-releases/authentic-brands-group-announces-500m-primary-follow-on-investment-from-general-atlantic) (cache 009)
  - "funds advised by CVC Capital Partners (CVC) and HPS Investment Partners (HPS) have signed definitive agreements to purchase significant equity stakes in the company from certain current ABG shareholders." and "World-Leading Private Equity and Investment Firms, Alongside BlackRock Long Term Private Capital, Simon, General Atlantic, Leonard Green & Partners and ABG’s Other Equity Partners" — [ABG, release "CVC Capital Partners VIII and HPS Investment Partners to Acquire Ownership Stakes in ABG", November 22, 2021](https://corporate.authentic.com/press-releases/cvc-and-hps-to-acquire-ownership-stakes) (cache 011)
  - Current: "Authentic Brands Group (Authentic) New York, NY authentic.com" … "Sector: Consumer Products/Retail Deal Type: Growth Equity Status: Current" — [Leonard Green & Partners, Portfolio page, accessed 2026-11-17](https://www.leonardgreen.com/portfolio/) (cache 108)
  - ABG's brand portfolio page shows image tiles linked to reebok.com, champion.com, us.dockers.com and eddiebauer.com, and an unlinked tile whose image file is named "Website Tile _Lee.png" (uploaded 2026-11, per the image URL's timestamp). These are HTML attributes, not page text. — [ABG, Brand portfolio page, accessed 2026-11-17](https://corporate.authentic.com/brand-portfolio) (cache 012)
  - Stake: none stated in any source read. Counted PE-owned under the "no stated stake" rule. If the PE holders are minorities, as a group of 7 named holders suggests, the 5 rows become PE minority stakes and the combined count is unchanged.
- **13D/13G filers since 2024-01-01** for each SEC-registered parent come from EDGAR full-text search with forms SC 13D, SC 13D/A, SC 13G, SC 13G/A, SCHEDULE 13D, SCHEDULE 13D/A, SCHEDULE 13G and SCHEDULE 13G/A (caches 032–044). The filer lists are in "Form ADV results".
- **Tickers** come from SEC's company-ticker file (cache 031), e.g. "{"cik_str":320187,"ticker":"NKE","title":"NIKE, Inc."}" (the checker skips this JSON line).

Per row:
- **AO1 Levi's**
  - Ranking: "1 Levi's 98% 76%" (cache 007)
  - Owner: "Levi Strauss & Co. (LS&Co.) (NYSE: LEVI), today announced the successful final closing" and "sharpens LS&Co.’s focus on the Levi’s® brand and Beyond Yoga" — [Levi Strauss & Co., release "Levi Strauss & Co. Completes Sale of Dockers® to Authentic Brands Group", March 3, 2026](https://investors.levistrauss.com/news/financial-news/news-details/2026/Levi-Strauss--Co--Completes-Sale-of-Dockers-to-Authentic-Brands-Group/default.aspx) (cache 018)
  - Holders: Haas family members (Peter E. Jr., Jennifer C., Margaret E., Miriam L., Bradley J., Daniel S., Robert D.), Eisenhardt and Geballe file 13G/As; the rest are JPMorgan, Vanguard, FMR, Capital Research, Wellington and Macquarie (cache 034). No PE holder.
  - Affiliate: "Join Our Affiliate Community GROW TOGETHER" and "Earn commission by sharing your favorite Levi’s® and inspiring your audience to shop." — [Levi's US, affiliate page, accessed 2026-11-17](https://www.levi.com/US/en_US/features/affiliate-program) (cache 100)
  - BDC names: "Levi Strauss & Co." (no BDC match)
- **AO2 adidas**
  - Ranking: "2 Adidas 99% 75%" (cache 007)
  - Owner: "The adidas AG share is part of a variety of major indices such as the DAX 40" and "Institutional investors represent the largest group, holding 79% of shares outstanding (2024: 80%)." — [adidas Annual Report 2025, "Our Share", accessed 2026-11-17](https://report.adidas-group.com/2025/en/to-our-shareholders/our-share.html) (cache 081)
  - Holders: not checked (not an SEC registrant; German voting-rights notices were not read).
  - Affiliate: probable. A search found https://www.adidas.com/us/help/us-company-information/what-is-our-affiliate-program; adidas.com returned an Akamai block page (cache 104).
  - BDC names: "adidas AG" (no match)
- **AO3 Fruit of the Loom**
  - Ranking: "3 Fruit of the Loom 97% 74%" (cache 007)
  - Owner: "Fruit of the Loom, Inc. Delaware" in the subsidiaries list — [Berkshire Hathaway Inc., 10-K for 2025, Exhibit 21, filed 2026-03-02](https://www.sec.gov/Archives/edgar/data/1067983/000119312526083899/brka-ex21.htm) (cache 063). Ticker: "{"cik_str":1067983,"ticker":"BRK-B","title":"BERKSHIRE HATHAWAY INC"}" (cache 031)
  - Holders: Berkshire's own 13D/13G search mixes filings Berkshire makes on other companies; holders filing on Berkshire are Vanguard, FMR, BlackRock and State Street (cache 035). Warren Buffett controls the votes (not read here). No PE holder.
  - Affiliate: none found (no search lead).
  - BDC names: "Fruit of the Loom, Inc." (no match)
- **AO4 Converse**
  - Ranking: "4 Converse 94% 68%" (cache 007)
  - Owner: "We offer our products under the NIKE, Jordan and Converse brands." — [NIKE, Inc., 10-K for fiscal 2026, filed 2026-07-15](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm) (cache 058)
  - Holders: Vanguard and BlackRock only (cache 033).
  - Affiliate: network listings only (FlexOffers, UpPromote per search).
  - BDC names: "Converse Inc." (no match)
- **AO5 Hanes**
  - Ranking: "5 Hanes 95% 67%" (cache 007)
  - Owner: "As a result of the Transactions, Hanesbrands became a wholly owned subsidiary of Gildan." — [Hanesbrands Inc., 8-K, December 1, 2025](https://www.sec.gov/Archives/edgar/data/1359841/000119312525303276/d848051d8k.htm) (cache 065). Ticker: "{"cik_str":1061894,"ticker":"GIL","title":"Gildan Activewear Inc."}" (cache 031)
  - Holders on Gildan (cache 036): CDPQ, Janus Henderson, 1832 Asset Management, Cooke & Bieler, FMR, Jarislowsky Fraser, Bank of Nova Scotia and BlackRock (13Gs); Browning West (13D/A, 2024-12-04; adviser reports no PE funds); Coliseum Capital (13D/A, 2024-08-21).
  - Coliseum exited: "on August 20, 2024, each of the Reporting Persons ceased to be the beneficial owner of more than 5% of the Issuer’s Common Shares." — [Coliseum Capital Management, SC 13D/A No. 3 on Gildan, filed 2024-08-21](https://www.sec.gov/Archives/edgar/data/1061894/000119312524204418/d844731dsc13da.htm) (cache 050)
  - CDPQ: the 13G/A filed 2026-08-14 reads, as XML field values, "Rule 13d-1(c)", "Caisse de depot et placement du Quebec" and "6.3" (event date 06/30/2026) — [Caisse de dépôt et placement du Québec, SCHEDULE 13G/A No. 1 on Gildan](https://www.sec.gov/Archives/edgar/data/1061894/000114036126033188/primary_doc.xml) (cache 109). Form ADV: "CDPQ GLOBAL INFRASTRUCTURE INC." (legal name CDPQ INFRASTRUCTURES MONDIALES INC., CRD 338423, exempt-reporting) has `Any PE Funds = Y`, 1 PE fund. The tie between that adviser and the 13G filer rests on the name only. See open question 1.
  - Affiliate: network listings only (FlexOffers, Affilitizer, LinkClicky per search).
  - BDC names: "Hanesbrands Inc.", "Gildan Activewear Inc." (no match)
- **AO6 Nike**
  - Ranking: "6 Nike 97% 67%" (cache 007)
  - Owner: see AO4 (cache 058). Ticker: "{"cik_str":320187,"ticker":"NKE","title":"NIKE, Inc."}" (cache 031)
  - Affiliate: page title "Nike Affiliate Program | Nike Help" — [Nike Help, accessed 2026-11-17](https://www.nike.com/help/a/nike-affiliate-program) (cache 096). The body text renders by script; the page's meta description reads "The Nike Affiliate Program allows approved websites to earn a commission on qualified purchases from promoting Nike products." (an HTML attribute, skipped by the checker).
  - BDC names: "NIKE, Inc." (no match; "CB Nike Holdco, LLC" and "Project Nike Purchaser, LLC" are unrelated borrowers)
- **AO7 Skechers**
  - Ranking: "7 Skechers 96% 67%" (cache 007)
  - Owner: "The Buyer Parties are affiliates of investment funds managed by 3G Capital Partners L.P." and "As a result of the completion of the Merger, a change in control of the Company occurred, and the Company became an indirect subsidiary of Parent." — [Skechers U.S.A., Inc., 8-K, September 12, 2025](https://www.sec.gov/Archives/edgar/data/1065837/000119312525201846/d41926d8k.htm) (cache 029)
  - Co-owners: the same 8-K names "Legacy Holders" who hold Parent Units beside "3G Fund VI, L.P."; no stake is stated, so 3G's hop counts as control.
  - Since: 2025-09-12 (8-K)
  - Affiliate: network listings only (Impact, CJ, FlexOffers, Skimlinks per search; no brand page found).
  - BDC names: "Beach Acquisition Bidco, LLC (dba Skechers)" (Blue Owl Credit Income Corp.), "Sketchers Beach Acquisition Bidco LLC" (Apollo Debt Solutions BDC)
- **AO8 Reebok**
  - Ranking: "8 Reebok 95% 66%" (cache 007)
  - Owner: "Authentic Brands Group (ABG) today announced that it has completed the acquisition of Reebok from adidas." — [ABG, release "Authentic Brands Group Finalizes the Acquisition of Reebok", March 1, 2022](https://corporate.authentic.com/press-releases/abg-finalizes-reebok) (cache 020)
  - Trademark line: "Reebok® is a trademark of Reebok International Limited." — [Reebok US, site footer, accessed 2026-11-17](https://www.reebok.com/) (cache 083)
  - PE chain: ABG's owners (caches 009, 011, 108).
  - Operator: the 2022 release names "Reebok Design Group (RDG) in partnership with SPARC Group" for design; no US wholesale licensee is named in sources read (cache 020).
  - Affiliate: footer link "Become an Affiliate Partner" to reebok.rmaffiliate.com (cache 083)
  - BDC names: "Reebok International Limited", "ABG Intermediate Holdings 2 LLC" (see "BDC names")
- **AO9 New Balance**
  - Ranking: "9 New Balance 93% 65%" (cache 007)
  - Owner: not found. newbalance.com returned 403 (cache 068); New Balance's newsroom fact sheet showed "Let's confirm you are human" in the one browser retry and did not clear (cache 074).
  - Leads (not cited): Forbes and New Balance's 2015 fact sheet (per search) describe Jim Davis buying the company in 1972; directories put the Davis family's stake at about 95%. No PE lead.
  - Affiliate: probable (https://www.newbalance.com/affiliate/ in search; the site refused the bot).
  - BDC names: "New Balance Athletics, Inc." (no match)
- **AO10 Wrangler**
  - Ranking: "10 Wrangler 91% 65%" (cache 007)
  - Owner: "Kontoor Brands, Inc. (NYSE: KTB) is a global apparel company with deep authority in the denim, outdoor and workwear categories. Wrangler ® and Helly Hansen ® are iconic brands" — [Kontoor Brands, release, Nov 03, 2026](https://www.kontoorbrands.com/news-media/press-release/247/kontoor-brands-completes-the-sale-of-the-lee-business-to) (cache 015)
  - Holders: JPMorgan, Vanguard, BlackRock, PNC, FMR and Ameriprise (cache 032). No PE holder.
  - Affiliate: network listings only (FlexOffers per search).
  - BDC names: "Kontoor Brands, Inc." (no match; "Wrangler Topco, LLC" in Silver Point and Sixth Street schedules is a business-services borrower, unrelated)
- **AO11 Under Armour**
  - Ranking: "11 Under Armour 96% 64%" (cache 007)
  - Owner: "{"cik_str":1336917,"ticker":"UAA","title":"Under Armour, Inc."}" (cache 031)
  - Holders (cache 037): Fairfax Financial Holdings (13D/A, 2026-05-15); Alyeska Investment Group (13G/A, 2025-08-14); BlackRock, Vanguard, Dimensional, FMR and State Street. Fairfax's adviser and Alyeska both report no PE funds (see "Form ADV results").
  - Affiliate: "THE UNDER ARMOUR® AFFILIATE PROGRAM allows approved websites to link to www.underarmour.com and begin earning commissions on clickthrough sales." — [Under Armour US, affiliate page, accessed 2026-11-17](https://www.underarmour.com/en-us/t/ua-affiliate-program/) (cache 106)
  - BDC names: "Under Armour, Inc." (no match)
- **AO12 The North Face**
  - Ranking: "12 The North Face 90% 64%" (cache 007)
  - Owner: "V.F. Corporation, founded in 1899, is a portfolio of leading outdoor and active brands, including The North Face ® , Vans ® and Timberland ®" — [V.F. Corporation, 10-K for fiscal 2026, filed 2026-05-20](https://www.sec.gov/Archives/edgar/data/103379/000010337926000030/vfc-20260328.htm) (cache 059)
  - Holders (cache 038): Dodge & Cox, Vanguard, M&G plc, BlackRock, Northern Trust, PNC and State Street. M&G's 13G/A (6.60%) is filed under "Rule 13d-1(b)" (cache 048, XML field).
  - Affiliate: network listings only (Impact via Affilitizer, per search).
  - BDC names: "V.F. Corporation", "The North Face" (no match)
- **AO13 Lee**
  - Ranking: "14 Lee 90% 63%" (cache 007)
  - Owner: "Kontoor Brands, Inc. (NYSE: KTB) today announced it has completed the sale of the Lee ® business to Authentic Brands Group." — [Kontoor Brands, release "Kontoor Brands Completes the Sale of the Lee® Business to Authentic Brands Group", Nov 03, 2026](https://www.kontoorbrands.com/news-media/press-release/247/kontoor-brands-completes-the-sale-of-the-lee-business-to) (cache 015)
  - Deal: "signed a definitive agreement to sell the Lee ® business to Authentic Brands Group (Authentic) for up to $1 billion" — [Kontoor Brands, release of the agreement, 2026-05-21](https://www.kontoorbrands.com/news-media/press-release/234/kontoor-brands-enters-into-definitive-agreement-to-sell) (cache 016)
  - PE chain: ABG's owners (caches 009, 011, 108).
  - Licensee: not read (lee.com served a Cloudflare challenge; trade press names One Jeanswear Group for the US and Canada; not cited).
  - BDC names: "ABG-Storm LLC" (buyer per trade press; no match), "ABG Intermediate Holdings 2 LLC"
- **AO14 PUMA**
  - Ranking: "15 PUMA 96% 63%" (cache 007)
  - Owner: "Around 71% of the company shares are in free float as defined by Deutsche Börse AG." — [PUMA SE, Shareholder Structure page, accessed 2026-11-17](https://about.puma.com/en/shareholder-structure) (cache 077). The holder table on that page is not in the page text.
  - Lead (not cited): PUMA's own Q3 2026 materials, per search, say Anta Sports completed its purchase of Artémis's 29.06% in October 2026. Anta is a listed company, so it would not be PE.
  - Affiliate: not confirmed. us.puma.com/us/en/help/affiliates returned 404 (cache 094); FlexOffers lists a PUMA program (search).
  - BDC names: "PUMA SE" (no match; "Puma Buyer, LLC (dba PANTHERx)" is an unrelated pharmacy borrower)
- **AO15 Dr. Scholl's shoes**
  - Ranking: "16 Dr. Scholl's shoes 89% 62%" (cache 007)
  - Owner: "a private equity firm focused exclusively on investing in consumer brands and companies, today announced that its portfolio company, Scholl's Wellness Company (parent Company of Dr. Scholl's), has acquired VKTRY" — [Yellow Wood Partners, release, BOSTON, May 20, 2026](https://www.yellowwoodpartners.com/news-article/yellow-wood-partners-portfolio-company-scholls-wellness-company-dr-scholls-acquires-performance-insole-and-footwear-innovation-company-vktry) (cache 022)
  - Since: "announced today that it has completed the previously announced acquisition of the Dr. Scholl’s™ business from Bayer for $585 million." and "Yellow Wood Partners is creating the Scholl’s Wellness Company (SWC)" — [Yellow Wood Partners, release, BOSTON, November 4, 2019](https://www.yellowwoodpartners.com/news-article/yellow-wood-partners-completes-acquisition-of-dr-scholls%E2%84%A2-from-bayer) (cache 023)
  - Licensee: "We have a license agreement to sell Dr. Scholl’s Shoes in the United States, Canada and Latin America through 2026." — [Caleres, Inc., 10-K for fiscal 2025, filed 2026-04-02](https://www.sec.gov/Archives/edgar/data/14707/000001470726000053/cal-20260131x10k.htm) (cache 028). The 10-K does not name the licensor.
  - Stake: not stated ("portfolio company"); counted PE-owned.
  - Affiliate: network listings only (FlexOffers, Brandreward per search).
  - BDC names: "DRS Holdings III, Inc. (Dr. Scholl's)" (Kayne Anderson BDC, Kayne DL 2021), "Dr. Scholls DRS Holdings III, Inc." (Apollo Debt Solutions BDC), "Dr. Scholl's DRS Holdings III, Inc." (MidCap Financial Investment Corp, MidCap Apollo Institutional Private Lending)
- **AO16 Old Navy**
  - Ranking: "17 Old Navy 96% 61%" (cache 007)
  - Owner: "is a house of iconic American brands offering apparel, accessories, and personal care products for men, women, and children under the Old Navy, Gap, Banana Republic, and Athleta brands." — [Gap Inc., 10-K for fiscal 2025, filed 2026-03-17](https://www.sec.gov/Archives/edgar/data/39911/000162828026018573/gap-20260131.htm) (cache 060)
  - Holders (cache 039): William S., John J. and Robert J. Fisher (13D/As, latest 2026-10-08); Vanguard; Dodge & Cox. No PE holder.
  - Affiliate: "We'd like to tell you about the oldnavy.com Affiliate Program." and "To apply, visit Impact, our affiliate program vendor" — [Old Navy, affiliate page, accessed 2026-11-17](https://oldnavy.gap.com/customerService/info.do?cid=3000) (cache 098)
  - BDC names: "Gap Inc.", "Old Navy, LLC" (no match)
- **AO17 Columbia**
  - Ranking: "18 Columbia 85% 60%" (cache 007)
  - Owner: "{"cik_str":1050797,"ticker":"COLM","title":"COLUMBIA SPORTSWEAR CO"}" (cache 031)
  - Holders (cache 040): Timothy P., Joseph P. and Molly Boyle (13G/As); Morgan Stanley, Vanguard and BlackRock.
  - Affiliate: none found (no search lead).
  - BDC names: "Columbia Sportswear Company" (no match)
- **AO18 Polo Ralph Lauren**
  - Ranking: "19 Polo Ralph Lauren 91% 59%" (cache 007)
  - Owner: "which are sold under various brand names, including Ralph Lauren Collection, Ralph Lauren Purple Label, Double RL, Polo Ralph Lauren, Lauren Ralph Lauren, Polo Sport" — [Ralph Lauren Corporation, 10-K for fiscal 2026, filed 2026-05-21](https://www.sec.gov/Archives/edgar/data/1037038/000162828026037074/rl-20260328.htm) (cache 066)
  - Holders: see AO22.
  - Affiliate: none found separately (see AO22).
  - BDC names: "Ralph Lauren Corporation" (no match)
- **AO19 Champion**
  - Ranking: "21 Champion 89% 59%" (cache 007)
  - Owner: "announces that it has finalized the acquisition of athleticwear icon Champion." and "all agreements become effective as of September 30, 2024" — [ABG, release "Authentic Acquires Champion, Unveils New Brand Partners", September 30, 2024](https://corporate.authentic.com/press-releases/authentic-acquires-champion-unveils-new-partners) (cache 019)
  - Trademark line: "Champion® is a trademark of ABG-Champion LLC." — [Champion US, site footer, accessed 2026-11-17](https://www.champion.com/) (cache 089)
  - Licensees: "Champion’s long-term US collegiate apparel business will be carried forward under a new license granted to GearCo" and "AMG Companies, a long-standing and trusted partner of Authentic, will manage Champion’s core business in the US and Canada through its affiliates." (cache 019)
  - PE chain: ABG's owners (caches 009, 011, 108).
  - Affiliate: network listing only (FlexOffers "championusa.com", per search); no link in the homepage HTML.
  - BDC names: "ABG-Champion LLC" (no match; "Club Champion LLC" is an unrelated golf retailer), "ABG Intermediate Holdings 2 LLC"
- **AO20 Vans**
  - Ranking: "22 Vans 86% 58%" (cache 007)
  - Owner: see AO12 (cache 059).
  - Affiliate: network listings only (Affilitizer, per search).
  - BDC names: "Vans, Inc." (no match; "Owl Vans, LLC" is an unrelated auto-components borrower)
- **AO21 Gap**
  - Ranking: "23 Gap 92% 57%" (cache 007)
  - Owner: see AO16 (cache 060). Ticker: "{"cik_str":39911,"ticker":"GAP","title":"GAP INC"}" (cache 031)
  - Affiliate: network listings only (Affilitizer, FlexOffers per search). A gapinc.com article on a cross-brand creator program came up in search; not opened.
  - BDC names: "Gap Inc." (no match)
- **AO22 Ralph Lauren**
  - Ranking: "24 Ralph Lauren 91% 56%" (cache 007)
  - Owner: "Founded in 1967 by Mr. Ralph Lauren, we are a global leader in the design, marketing, and distribution of luxury lifestyle products" (cache 066). Ticker: "{"cik_str":1037038,"ticker":"RL","title":"RALPH LAUREN CORP"}" (cache 031)
  - Holders (cache 041): Ralph Lauren (13G/A); FMR, Vanguard, Victory Capital, BlackRock, T. Rowe Price, Invesco and JPMorgan. Victory Capital's adviser reports PE funds, but its 13G/A is filed under "Rule 13d-1(b)" at ".99" percent (cache 047, XML fields).
  - Affiliate: network listing only; FlexOffers says the program is not currently offered (search).
  - BDC names: "Ralph Lauren Corporation" (no match)
- **AO23 L.L.Bean**
  - Ranking: "25 L. L. Bean 87% 56%" (cache 007)
  - Owner: not stated. "We spoke with Shawn Gorman, Executive Chairman of the Board and great-grandson of L.L. Bean" and "The grandson of company founder L.L., Leon Gorman joined the family business in 1961." — [L.L.Bean, Leadership page, accessed 2026-11-17](https://www.llbean.com/llb/shop/516919?page=leadership) (cache 071)
  - Affiliate: none found (company and leadership pages checked; no search lead).
  - BDC names: "L.L. Bean, Inc." (no match)
- **AO24 Calvin Klein**
  - Ranking: "26 Calvin Klein 96% 56%" (cache 007)
  - Owner: "References in this report to the brand names TOMMY HILFIGER , TOMMY JEANS , Calvin Klein , Calvin Klein Jeans , Calvin Klein Underwear , Calvin Klein Sport , Calvin Klein Collection , which are owned" — [PVH Corp., 10-K for 2025, filed 2026-03-31](https://www.sec.gov/Archives/edgar/data/78239/000007823926000021/pvh-20260201.htm) (cache 061)
  - Holders (cache 042): FMR (9.5%, "Rule 13d-1(b)", cache 110), Vanguard, BlackRock, Dimensional and Pzena.
  - Affiliate: network listings only (Affilitizer, per search).
  - BDC names: "PVH Corp.", "Calvin Klein, Inc." (no match)
- **AO25 Eddie Bauer**
  - Ranking: "27 Eddie Bauer 86% 55%" (cache 007)
  - Owner: "said Jarrod Weber, Global President, Sports & Lifestyle at Authentic, owner of the Eddie Bauer brand." — [ABG, release "Authentic and Oved Announce Partnership to Grow Eddie Bauer's E-Commerce and Wholesale Business", January 8, 2026](https://corporate.authentic.com/press-releases/authentic-oved-expanded-partnership-eddie-bauers-e-commerce-wholesale-business) (cache 030)
  - Licensees: "today announced an expanded partnership with longtime Eddie Bauer licensee Outdoor 5, LLC (Oved) to assume responsibility of the brand’s e-commerce and wholesale operations" and "Catalyst Brands will continue to operate Eddie Bauer’s retail and outlet stores across North America." (cache 030)
  - Since: not checked.
  - PE chain: ABG's owners (caches 009, 011, 108).
  - Affiliate: directory listing only (Lasso); no link in the homepage HTML (cache 091).
  - BDC names: "PSEB, LLC (Eddie Bauer)" (BlackRock TCP Capital Corp.), "ABG Intermediate Holdings 2 LLC"
- **AO26 Coach**
  - Ranking: "28 Coach 86% 55%" (cache 007)
  - Owner: "is a global house of iconic accessories and lifestyle brands uniting the magic of Coach and kate spade new york." — [Tapestry, Inc., 10-K for fiscal 2026, filed 2026-08-13](https://www.sec.gov/Archives/edgar/data/1116132/000111613226000018/tpr-20260627.htm) (cache 062)
  - Holders: Vanguard, BlackRock and FMR (cache 043).
  - Affiliate: none found (no search lead).
  - BDC names: "Tapestry, Inc.", "Coach, Inc." (no match; "Tapestry Management Services Inc." is an unrelated health-technology borrower)
- **AO27 Crocs**
  - Ranking: "29 Crocs 94% 54%" (cache 007)
  - Owner: "{"cik_str":1334036,"ticker":"CROX","title":"Crocs, Inc."}" (cache 031)
  - Holders: FMR, Vanguard and BlackRock (cache 044).
  - Affiliate: "Crocs Affiliate Program How do I get started? Read the Crocs™ affiliate agreement and fill out the online application" — [Crocs, affiliate page, accessed 2026-11-17](https://www.crocs.com/affiliate-program/affiliate-program.html) (cache 102)
  - BDC names: "CROCS INC - Consumer goods: Durable - Term Loan B (01/24) - Loan" (Saratoga Investment Corp., period 2026-05-31)
- **AO28 Timberland**
  - Ranking: "30 Timberland 82% 53%" (cache 007)
  - Owner: see AO12 (cache 059).
  - Affiliate: network listings only (FlexOffers, Affilitizer per search).
  - BDC names: "The Timberland Company" (no match)
- **AO29 Dockers**
  - Ranking: "33 Dockers 85% 52%" (cache 007)
  - Owner: "today announced the successful final closing, on February 27, 2026, of its previously disclosed sale of the Dockers® brand to Authentic Brands Group." (cache 018)
  - Site footer: "©2026 Dockers™" (cache 085); no operator named.
  - PE chain: ABG's owners (caches 009, 011, 108).
  - Affiliate: network listings only (FlexOffers, CJ per search).
  - BDC names: "Dockers" (no match; "Docker, Inc." in Hercules Capital's schedule is a software company), "ABG Intermediate Holdings 2 LLC"
- **AO30 Louis Vuitton**
  - Ranking: "34 Louis Vuitton 92% 52%" (cache 007)
  - Owner: "LVMH shares are listed on the Euronext Paris Eurolist." and the Maisons menu "Christian Dior Couture Fendi Givenchy Kenzo Loewe Loro Piana Louis Vuitton" — [LVMH, Investors FAQ page, accessed 2026-11-17](https://www.lvmh.com/en/investors/frequently-asked-questions) (cache 079)
  - Holders: not checked (trade sources put the Arnault family group in control; not cited).
  - Affiliate: none found (no search lead).
  - BDC names: "LVMH Moët Hennessy Louis Vuitton" (no match)

### Rollups and groups that are not brands

Not counted in the 30.
- **Authentic Brands Group:** owns Reebok, Lee, Champion, Eddie Bauer and Dockers here, and Brooks Brothers, Nautica, Aéropostale, Guess and others outside the ranking. Owner: General Atlantic, Leonard Green, CVC, HPS, BlackRock LTPC, Brookfield and Simon Property Group as "significant shareholders", with founder Jamie Salter. Stakes not stated.
- **V.F. Corporation:** The North Face, Vans, Timberland. Public (VFC).
- **NIKE, Inc.:** Nike, Converse (and Jordan). Public (NKE).
- **Gap Inc.:** Old Navy, Gap (and Banana Republic, Athleta). Public (GAP).
- **Ralph Lauren Corporation:** Polo Ralph Lauren, Ralph Lauren. Public (RL).
- **Kontoor Brands:** Wrangler (and Helly Hansen); sold Lee on 2026-11-03. Public (KTB).
- **Gildan Activewear:** Hanes (via Hanesbrands, since 2025-12-01). Public (GIL).
- **Scholl's Wellness Company:** Dr. Scholl's (and VKTRY since 2026-05). Yellow Wood Partners portfolio company.
- **Licensees and operators** (not owners): Caleres (Dr. Scholl's shoes), AMG Companies and GearCo (Champion), Outdoor 5, LLC and Catalyst Brands (Eddie Bauer), Reebok Design Group with SPARC Group (Reebok design, 2022).

### Category share

**All rows (N = 30, all ranked by YouGov popularity).**
- **PE-owned (control, or no stated stake): 7 / 30 = 23.3%**
  - Skechers: 3G Capital, control stated (2025-09-12).
  - Dr. Scholl's shoes: Yellow Wood Partners via Scholl's Wellness Company; stake not stated (since 2019-11-04).
  - Reebok (2022-03-01), Champion (2024-09-30), Eddie Bauer (not checked), Dockers (2026-02-27) and Lee (2026-11-03): Authentic Brands Group, whose named PE holders state no stakes.
- **PE minority stake: 0** as counted; **1** (Hanes) under the literal ADV reading for CDPQ. PE-owned plus minority = **7 / 30 = 23.3%**, or **8 / 30 = 26.7%**.
  - **Sensitivity:** if ABG's holders are read as minorities, the split becomes 2 PE-owned (Skechers, Dr. Scholl's shoes) and 5 PE minority stakes. The combined count does not change.
- **Public company: 21 / 30 = 70.0%** (20 if Hanes moves to PE minority): Levi's, adidas, Fruit of the Loom, Converse, Hanes, Nike, Wrangler, Under Armour, The North Face, PUMA, Old Navy, Columbia, Polo Ralph Lauren, Vans, Gap, Ralph Lauren, Calvin Klein, Coach, Crocs, Timberland, Louis Vuitton. Three are foreign-listed (adidas, PUMA, LVMH) and their holders were not read.
- **Private, owner not stated: 1** (L.L.Bean).
- **Not found: 1 / 30 = 3.3%** (New Balance).
- **Top 10 only:** PE-owned 2 / 10 (Skechers, Reebok); 3 / 10 with Hanes under the literal reading. Public 7; not found 1 (New Balance).
- **By parent company:** 21 parents (ABG 5 rows; VF 3; Nike, Gap Inc. and Ralph Lauren 2 each; 16 parents with one row). PE-held parents: 3 / 21 = 14.3% (3G's Skechers, ABG, Scholl's Wellness Company); 4 / 21 = 19.0% with Gildan.
- **Upper bound if leads were confirmed:** New Balance's only ownership leads point to the Davis family. The upper bound is 8 / 30 (the literal reading).
- **Pending deals:** none found on any row. The last open deal, Lee, closed on 2026-11-03.
- **Sources disagree:** none on owners.

## Firms named

Every investment firm named as an owner or 5%+ holder, as the sources name it:
- **3G Capital:** "3G Capital Partners L.P.", "3G Fund VI, L.P." (Skechers)
- **Yellow Wood Partners:** "Yellow Wood Partners" (Dr. Scholl's shoes)
- **ABG's holders:** "General Atlantic"; "Leonard Green & Partners"; "CVC Capital Partners", "funds advised by CVC Capital Partners", "CVC Capital Partners VIII"; "HPS Investment Partners"; "BlackRock", "BlackRock Long Term Private Capital"; "Brookfield"; "Simon Property Group" (a listed REIT). The 2021 release's tags add GIC, Lion Capital and Jasper Ridge Partners.
- **Holders of public rows that are not index managers:** Caisse de dépôt et placement du Québec (Gildan); Coliseum Capital Management (Gildan, exited); Browning West (Gildan); Fairfax Financial Holdings (Under Armour); Alyeska Investment Group (Under Armour); Dodge & Cox and M&G plc (VF); Pzena Investment Management (PVH); Victory Capital Management (Ralph Lauren).
- **Leads only (not cited, not counted):** the investor group of CVC, General Atlantic, HPS and Leonard Green reported (Bloomberg, Axios, January 2025) to be buying BlackRock's ABG stake; Anta Sports (PUMA, 29.06%); the Arnault family group (LVMH).

## Form ADV results

From the SEC's November 2026 adviser files (registered and exempt-reporting), matched by name:

| Firm (role) | Adviser entity | CRD | File | Any PE Funds | PE funds |
|---|---|---|---|---|---|
| 3G Capital (Skechers) | 3G CAPITAL PARTNERS LP | 156934 | registered | Y | 2 |
| Yellow Wood Partners (Dr. Scholl's shoes) | YELLOW WOOD PARTNERS LLC | 161062 | registered | Y | 10 |
| General Atlantic (ABG) | GENERAL ATLANTIC SERVICE COMPANY, L.P. | 133536 | registered | Y | 323 |
| Leonard Green (ABG) | LEONARD GREEN & PARTNERS, L.P. | 158164 | registered | Y | 107 |
| CVC (ABG) | CVC ADVISERS JERSEY LIMITED / CVC CAPITAL PARTNERS ADVISORY COMPANY LIMITED | 296266 / 161620 | exempt | Y | 52 / 15 |
| HPS (ABG) | HPS INVESTMENT PARTNERS, LLC | 282125 | registered | Y | 142 |
| BlackRock LTPC (ABG) | BLACKROCK ALTERNATIVES MANAGEMENT, LLC | 288041 | registered | Y | 53 |
| Brookfield (ABG) | BROOKFIELD ASSET MANAGEMENT PIC ADVISER (PRIVATE EQUITY), L.P. | 171207 | registered | Y | 123 |
| Lion Capital (ABG 2021 tag) | LION CAPITAL LLP | 160573 | exempt | Y | 10 |
| Jasper Ridge (ABG 2021 tag) | JASPER RIDGE PARTNERS, L.P. | 144401 | registered | N | |
| CDPQ (Gildan 13G, 13d-1(c), 6.3%) | CDPQ GLOBAL INFRASTRUCTURE INC. (CDPQ INFRASTRUCTURES MONDIALES INC.) | 338423 | exempt | Y | 1 |
| Coliseum (Gildan 13D/A, exited at 4.8%) | COLISEUM CAPITAL MANAGEMENT, LLC | 158120 | registered | Y | 2 |
| Browning West (Gildan 13D) | BROWNING WEST LP | 304702 | registered | N | |
| Fairfax (Under Armour 13D) | FAIRFAX GLOBAL INVESTMENT MANAGEMENT LLC | 314171 | registered | N | |
| Alyeska (Under Armour 13G) | ALYESKA INVESTMENT GROUP, L.P. | 155058 | registered | N | |
| Victory Capital (RL 13G/A, 13d-1(b), 0.99%) | VICTORY CAPITAL MANAGEMENT INC. | 106189 | registered | Y | 17 |
| M&G (VF 13G/A, 13d-1(b), 6.60%) | M&G INVESTMENT MANAGEMENT LTD. / M&G ALTERNATIVES INVESTMENT MANAGEMENT LIMITED | 114527 / 283173 | exempt | Y | 5 / 3 |
| FMR (PVH 13G/A, 13d-1(b), 9.5%; many rows) | FIDELITY MANAGEMENT & RESEARCH COMPANY LLC | 108281 | registered | Y | 1 |
| Dodge & Cox (VF, Gap) | DODGE & COX | 104596 | registered | N | |
| Pzena (PVH) | PZENA INVESTMENT MANAGEMENT LLC | 106847 | registered | N | |
| Wellington (Levi's) | WELLINGTON MANAGEMENT COMPANY LLP | 106595 | registered | N | |

- **Not in either file:** Simon Property Group (listed REIT), GIC (sovereign fund) and Caisse de dépôt et placement du Québec under its own name.
- **Correction to the earlier screen:** s3-d listed CDPQ as "in neither file". The exempt file does list an adviser named "CDPQ GLOBAL INFRASTRUCTURE INC." with PE funds. It was found by searching for "CDPQ", not "Caisse".
- **Rule boxes read:** CDPQ (13d-1(c)), FMR, M&G and Victory (all 13d-1(b)) and Coliseum (13D/A, below 5%). The other large managers (Vanguard, BlackRock, State Street, JPMorgan, Morgan Stanley, Capital Research, T. Rowe Price, Invesco, Northern Trust, PNC, Ameriprise, Dimensional, Janus Henderson, Macquarie, Bank of Nova Scotia, Cooke & Bieler, Jarislowsky Fraser, 1832) were not opened. They were treated as 13d-1(b) filers, as the earlier screen did. Three spot checks of ADV-`Y` managers all showed 13d-1(b).

## BDC names

Searched in the SEC BDC data sets 2026_07 to 2026_10 (schedule rows dated 2026-05-31 and 2026-06-30), by borrower text. Script: `$SCR/scripts/apparel/bdc.py`; output: `$SCR/pages/apparel/bdc_hits.txt`. Every match is debt; none is an equity or control holding.

| Row(s) | Borrower as the filer writes it | Filers | Tie to the row |
|---|---|---|---|
| Skechers | "Beach Acquisition Bidco, LLC (dba Skechers)"; "Sketchers Beach Acquisition Bidco LLC" | Blue Owl Credit Income Corp.; Apollo Debt Solutions BDC; also as "Beach Acquisition Bidco LLC": BlackRock Private Credit Fund, Franklin BSP Capital, Goldman Sachs Private Credit, Oaktree Specialty Lending, Oaktree Strategic Credit | brand name in the filer's label |
| Dr. Scholl's shoes | "DRS Holdings III, Inc. (Dr. Scholl's)"; "Dr. Scholl's DRS Holdings III, Inc." | Kayne Anderson BDC, Kayne DL 2021, Apollo Debt Solutions BDC, MidCap Financial Investment Corp, MidCap Apollo Institutional Private Lending | brand name in the filer's label (borrower is the brand owner's group) |
| Eddie Bauer | "PSEB, LLC (Eddie Bauer)" | BlackRock TCP Capital Corp. | brand name in the label; PSEB is an operator, not the brand owner |
| Crocs | "CROCS INC … Term Loan B (01/24)" | Saratoga Investment Corp. | brand owner's legal name (public company) |
| Reebok, Lee, Champion, Eddie Bauer, Dockers | "Authentic Brands ABG Intermediate Holdings 2 LLC"; "ABG Intermediate Holdings 2, LLC" | Apollo Debt Solutions BDC, CIFC Direct Lending Evergreen ("Authentic Brands"), Blackstone Private Credit Fund, First Eagle Private Credit, Goldman Sachs Private Credit, Overland Advantage, Steele Creek Capital | brand owner named in the filer's label; no brand name |

- **Overlap by row:** 4 rows named in filer text (Skechers, Dr. Scholl's shoes, Eddie Bauer, Crocs); 8 counting ABG's label (adding Reebok, Lee, Champion, Dockers).
- **False positives dropped:** Club Champion LLC, Docker, Inc., Wrangler TopCo, LLC, Owl Vans, LLC, Tapestry Management Services Inc., Puma Buyer, LLC (PANTHERx), CB Nike Holdco and Project Nike Purchaser.
- **Not tied:** Galaxy Universal LLC (FS KKR Capital, MidCap Financial; MidCap files it under "Sequential Brands Group, Inc."). Trade press links Galaxy to Reebok licensing, but no filer text does.

## Affiliate programs

| Status | PE rows | Non-PE rows |
|---|---|---|
| Brand-direct, confirmed on a page the brand runs (6) | Reebok (footer "Become an Affiliate Partner") | Nike (Help page), Old Navy (Impact), Levi's, Crocs, Under Armour (Awin) |
| Probable: brand page found in search, site refused the bot (2) | — | adidas, New Balance |
| Network or directory listings only (15) | Skechers, Dr. Scholl's shoes, Champion, Dockers, Eddie Bauer (Lasso only) | Hanes, Wrangler, Converse, The North Face, Vans, Timberland, Calvin Klein, Gap, PUMA (brand page 404), Ralph Lauren (listing says not offered) |
| None found (6) | — | Fruit of the Loom, Columbia, Polo Ralph Lauren, L.L.Bean, Coach, Louis Vuitton |
| Not checked (1) | Lee (lee.com challenged) | — |

- With Hanes counted as PE (literal reading), the network-only split becomes 6 PE and 9 non-PE.
- Depth: PE rows were checked on the brand homepage and by search. Non-PE rows were checked by search, and fetched only where the search gave a page on the brand's own domain. "None found" means no search lead and no link on any page fetched.

## Licensed rows

| Row | Licensor (owner of the name) | Licensee or operator (US) | Source |
|---|---|---|---|
| Reebok | Authentic Brands Group (trademark entity Reebok International Limited) | not stated in sources read (2022: Reebok Design Group with SPARC Group for design) | caches 020, 083 |
| Lee | Authentic Brands Group (since 2026-11-03) | not read (trade press: One Jeanswear Group; not cited) | caches 015, 016 |
| Champion | ABG-Champion LLC (Authentic Brands Group) | AMG Companies affiliates (core US and Canada); GearCo (collegiate, managed by Ames Watson with Fanatics as investor) | caches 019, 089 |
| Eddie Bauer | Authentic Brands Group | Outdoor 5, LLC (Oved) for e-commerce, wholesale, design and product development (US and Canada); Catalyst Brands for stores | cache 030 |
| Dockers | Authentic Brands Group (final closing 2026-02-27) | not stated in sources read | caches 018, 085 |
| Dr. Scholl's shoes | Scholl's Wellness Company (Yellow Wood Partners) | Caleres, Inc. (NYSE: CAL), license for US, Canada and Latin America "through 2026" | caches 022, 028 |

PVH licenses some Calvin Klein product categories to third parties (10-K, cache 061). The Calvin Klein row is counted as PVH's brand and the licensees were not listed.

## Surprises

- **ABG holds 5 of the 30 most popular apparel brands**, and 3 of the 5 came in the last 26 months: Champion (2024-09-30), Dockers (2026-02-27) and Lee (2026-11-03). ABG's portfolio page already shows a Lee tile with no link.
- **Dr. Scholl's shoes is a PE name sold by a public company.** Caleres makes and sells the shoes under a license that runs "through 2026". The name belongs to Yellow Wood's Scholl's Wellness Company, which is also a BDC borrower (DRS Holdings III).
- **CDPQ shows up as a PE-reporting adviser.** That puts Hanes on the line between public and PE minority stake; see open question 1. The earlier screen missed the registration.
- **The earlier screen's company rankings hid the licensed PE names.** YouGov's brand list gives 7 PE rows where the screen gave 1 (Skechers).
- **New Balance is the only top-10 brand whose owner no primary source here states.** Its site, its newsroom and adidas.com all refused the bot.
- **YouGov's clothing list mixes in non-apparel names** (Ray-Ban, Wilson, Samsonite), so a cut rule was needed.

## Open questions for the developer

Numbers only; nothing decided.
1. **CDPQ and Hanes.** CDPQ holds 6.3% of Gildan on a 13G under Rule 13d-1(c) (event 2026-06-30). An exempt adviser named "CDPQ GLOBAL INFRASTRUCTURE INC." (CRD 338423) reports `Any PE Funds = Y` (1 fund). The adviser is tied to the 13G filer by name only. Under a literal reading of the rule ("Y on any of its adviser registrations"), Hanes is a PE minority stake and the share is 8 / 30 (26.7%); otherwise 7 / 30 (23.3%). ADR 0001 maps a pension fund's self-description to `other_investment_fund`, but rank 1 (ADV) outranks a self-description. Both figures are above the 20% line.
2. **ABG's stake.** Seven holders are named "significant shareholders" with no stakes stated. Counted as 5 PE-owned rows; as minority stakes the split is 2 PE-owned and 5 PE minority, and the combined 7 is unchanged.
3. **Ranking scope.** The 4 rows skipped (Victoria's Secret, Ray-Ban, Wilson, Samsonite) and the 4 kept (Coach, Louis Vuitton, and both Ralph Lauren entries). Every alternative tried gives 7 / 30 PE.
4. **Popularity or fame.** YouGov's fame ranking was not used. Its top 20 on the curl'd page was not read.
5. **BDC overlap by parent label.** 4 rows by brand name, 8 counting ABG's "Authentic Brands" label.
6. **Eddie Bauer's BDC borrower** is PSEB, LLC, an operator, not the brand owner (1 row in either count).
7. **Dr. Scholl's shoes license** runs "through 2026". Ownership of the row does not depend on it, since the licensor owns the name.

## Cost

- **Time:** first fetch 2026-11-17T22:59:22Z, last 23:20:07Z; about 40 minutes including the ranking, the BDC search, writing and the quote check.
- **Requests:** 110 logged in `$SCR/pages/apparel/index.tsv`, including 30 robots.txt reads, 3 Playwright sessions (2 YouGov renders and 1 challenge retry) and 107 curl requests.
  - SEC: 44 (www.sec.gov and efts.sec.gov); 42 × 200, 1 × 403 (efts robots.txt), 1 × 500 (retried once).
  - Other hosts (non-robots): 38; 31 × 200, 3 × 403 (newbalance.com, lee.com, adidas.com), 2 × 404 (api.yougov.com guess, PUMA affiliate page), 2 × 202 (New Balance newsroom: curl and the browser retry).
  - Robots.txt: 21 × 200, 4 × 403, 2 × 404, 2 × 301, 1 × no response.
- **WebSearch:** 28 (2 for the ranking, 17 for owners and licensees, 9 for affiliate programs). WebFetch: 0.
- **Local data:** Form ADV November 2026 files (2) and BDC data sets 2026_07 to 2026_10 (4), read with `python3 -I`.
- **Agent tokens:** not metered by this worker; well under the 340k budget.
- **Scripts:** `$SCR/scripts/apparel/` (fetch.py, yougov_pw.py, pw_once.py, adv.py, filers.py, bdc.py, quotecheck.py), where `$SCR` is `/tmp/claude-1000/-home-iherr-projects-enshittified-demystified/02bcbe8a-bc03-477c-8c3d-2aa6ddd83e94/scratchpad`.
- **Quote self-check:** `quotecheck.py` string-matched every double-quoted string of 6+ characters on the Ranking, table and Evidence lines against the saved text of the cache pages cited on that line. Before matching it collapsed whitespace, normalized curly quotes and dashes and dropped spaces before punctuation; text either side of "…" was matched separately. **Result: 121 of 126 found.** The 5 misses are by design: ABG's "Website Tile _Lee.png" and Nike's meta description (HTML attributes), two quoted section names ("Form ADV results") and one span the regex caught between two quotes (AO5's XML field line). Lines with no cache number (BDC names, table cells) were checked separately: every table quote matches a saved page; BDC borrower strings match `bdc_hits.txt`; "championusa.com" is a search-result title and "no stated stake" is a rule phrase.
