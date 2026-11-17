# Industry screen 2, worker B: home furnishings, casinos

Ticket: [92 Research: Screen of five more industries](../../issues/92-research-screen-five-more-industries.md) · Worker report, 2026-11-17. Saved pages, scripts and logs are in the session scratchpad (temporary): pages under `pages/screen2-b/` (NNN.html raw, NNN.txt visible text, `index.tsv`, `robots.tsv`, `robots/`), scripts under `scripts/screen2-b/` (`fetch.py`, `adv.py`, `subs.py`, `qcheck.py`, `quotes.tsv`).

Every ownership fact comes from a primary source: SEC filings (10-K, DEF 14A, DEFM14A, Schedules 13D and 13G, the SEC's XBRL revenue frames), company pages and releases, sponsor portfolio pages, Form ADV. One release (At Home's) was read as a reprint on a third-party host, flagged where it appears. Trade press (Home News Now) supplies the furniture ranking and one ownership lead (World Market), flagged. No paywalled source, competitor site, Reddit or aggregator was opened.

Counting: PE-owned means a chain to a PE firm (Form ADV `Any PE Funds = Y` on any of its adviser registrations) with no minority hop; a hop with no stated stake counts as control. Above a public company, a PE minority stake comes only from a PE firm's 13D or a 13G not filed under Rule 13d-1(b); an amendment at 5% or less ends it. A brand belongs to whoever owns the name, never a licensee.

## 1. Home furnishings

**Ranking:** Home News Now, "HNN 125 Furniture and Bedding Retailers 2025" (2026-05-31 to 2026-06-22, four installments read), measured by estimated 2025 US furniture and bedding sales: "The 125 listing is based on estimated 2025 furniture and bedding sales in the U.S. and includes both brick-and-mortar stores and e-tailers." ([nos. 1-25](https://homenewsnow.com/blog/2026/06/22/home-news-now-125-furniture-bedding-retailers-2025-nos-1-25/), [26-50](https://homenewsnow.com/blog/2026/06/14/home-news-now-125-furniture-bedding-retailers-2025-nos-26-50/), [51-75](https://homenewsnow.com/blog/2026/06/07/home-news-now-125-furniture-bedding-retailers-2025-nos-51-75/), [76-100](https://homenewsnow.com/blog/2026/05/31/home-news-now-125-furniture-bedding-retailers-2025-nos-76-100/)). Furniture Today's Top 100 was not used: its full list didn't surface free of charge.

Rows are the top 10 home furnishings specialists in that ranking, in order. Left out of the rows:
- general merchants, which aren't home furnishings brands: Amazon (#3), Walmart (#5), Costco (#6), Target (#13), Sam's Club (#15), Home Depot (#22), TJX (#24, including HomeGoods and HomeSense), Lowe's (#26);
- mattress specialists, a separate industry: Mattress Firm (#4), Sleep Number (#17);
- Berkshire Hathaway's furniture division (#12), a rollup of regional names (listed below).

Sales are 2025 estimates in $ millions; store counts are HNN's US counts.

| # | Brand (HNN rank; 2025 sales; stores) | Owner (as stated) | Owner type | PE status | Since | Evidence |
|---|---|---|---|---|---|---|
| 1 | Ashley (#1; $6,257.3M; 854) | Ashley Furniture Industries, Wanek family | family | none | | [About](https://www.ashleyfurniture.com/about-us): "Ashley is a proud family-owned company with over 80 years of strong history in home furnishings." |
| 2 | Wayfair, with AllModern, Joss & Main, Birch Lane and Perigold (#2; $5,955.0M; 19) | Wayfair Inc. (NYSE: W); co-founders Niraj Shah and Steven Conine hold 33.59% of voting power each | public company | none (5% holders: Capital World Investors, FMR, Vanguard; ADV N or 13G filers) | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/1616707/000161670726000074/w-20260331.htm): "Holders of our Class B common stock are entitled to ten votes for each share held as of the Record Date on each proposal." Table: Shah 33.59% and Conine 33.59% of total voting power |
| 3 | Rooms To Go (#7; $3,278.1M; 148) | privately held; founded by Jeffrey and Morty Seaman; owner not named | not found | not found | 1990 | [About](https://www.roomstogo.com/about-us): "Rooms To Go is an American furniture retailer founded by Jeffrey and Morty Seaman in 1990." "Today, Rooms To Go remains a privately held company headquartered in Seffner, Florida," |
| 4 | Williams Sonoma brands: Pottery Barn, West Elm, Williams Sonoma Home and others (#8; $2,900.0M; 473) | Williams-Sonoma, Inc. (NYSE: WSM) | public company | none (BlackRock 9.6%, Aristotle 7.8%, Blackhill 6.5%, State Street 5.2%; all 13G, ADV N) | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/719955/000071995526000109/wsm-20260506.htm): "Information regarding our non-management 5% stockholders is derived from the most recently available 13G filings." |
| 5 | IKEA (#9; $2,810.0M; 55) | brand: Inter IKEA Systems B.V. (franchisor), ultimately the Inter IKEA Foundation; US stores run by a franchisee (Ingka, not checked) | foundation | none | 2023 (foundation split) | [Inter IKEA release](https://www.inter.ikea.com/en/newsroom/new-owner-of-inter-ikea-group): "The new Inter IKEA Foundation will be the ultimate owner of Inter IKEA Holding B.V., the IKEA related business." [IKEA US footer](https://www.ikea.com/us/en/this-is-ikea/about-us/): "© Inter IKEA Systems B.V. 1999-2026" |
| 6 | RH (#10; $2,335.0M; 105) | RH (NYSE: RH); Gary Friedman 24.3% (13D) | public company | none: FMR 14.7%, BlackRock 7.0%, Citadel 5.0% (ADV N); Susquehanna's broker-dealers (5.3% in the proxy) fell to 4.0% on 2026-11-16, which ends that holder | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/1528849/000110465926054988/rh-20260618xdef14a.htm): "The Susquehanna Reporting Persons stated that G1, SIG and Susquehanna Securities are affiliated independent broker-dealers that may be deemed a group." [Friedman 13D/A](https://www.sec.gov/Archives/edgar/data/1528849/000110465926082033/xslSCHEDULE_13D_X02/primary_doc.xml) (23.88%). [Susquehanna 13G/A, 4.0%](https://www.sec.gov/Archives/edgar/data/1528849/000144658026000115/xslSCHEDULE_13G_X02/primary_doc.xml): "G1 Execution Services, LLC, SIG Brokerage, LP, Susquehanna Investment Group and Susquehanna Securities, LLC are affiliated independent broker-dealers" |
| 7 | Bob's Discount Furniture (#11; $2,332.5M; 209) | Bob's Discount Furniture, Inc. (NYSE: BOBS), controlled by Bain Capital, about 73% | PE firm | **PE-owned** | before the 2026-02 IPO (Bain's purchase date not read) | [10-K FY2025](https://www.sec.gov/Archives/edgar/data/2085187/000162828026019015/a2025bdfannualfinancialsta.htm): "We are controlled by Bain Capital, which owns approximately 73% of our common stock." "Bain Capital controls a majority of our outstanding common stock." [IPO prospectus](https://www.sec.gov/Archives/edgar/data/2085187/000162828026005868/bobsdiscountfurnitureinc42.htm) (2026-02-05); no later offering found in its filing list |
| 8 | Raymour & Flanigan (#14; $1,655.0M; 148) | Goldberg family | family | none | | [2025 giving post](https://www.raymourflanigan.com/blog/community/giving-back/2025-community-giving): "community has always been at the heart of our family-owned business." |
| 9 | La-Z-Boy Furniture Galleries, with Joybird (#16; $1,421.5M; 351) | La-Z-Boy Inc. (NYSE: LZB) | public company | none (BlackRock 15.3%, Vanguard 7.0% and 5.4%, Dimensional 6.6%; all 13G) | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/57131/000005713126000024/lzb-20260714.htm): "The following table provides information about entities that beneficially owned more than 5% of our common stock, as of June 26, 2026, according to reports filed with the SEC." |
| 10 | Arhaus (#18; $1,124.0M; 107) | Arhaus, Inc. (NASDAQ: ARHS); founder John Reed 48.69% of combined voting power, Reed family trusts 45.4% more | public company (founder-controlled) | none; Freeman Spogli has exited | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/1875444/000119312526138942/d45561ddef14a.htm): "Mr. Roth was not compensated for his services as a director because of his affiliation with Freeman Spogli, a former investor in the Company." "36,470,752 shares of Class B common stock held by the 2018 Reed Dynasty Trust, of which Messrs. Adams and Beargie are trustees" |

**Next specialists in the ranking (not rows; owners not checked unless stated):** Crate & Barrel (#19; HNN says Otto Group), American Furniture Warehouse (#20), Living Spaces (#21), City Furniture (#23), Lovesac (#25, public), Havertys (#27, public), QVC Group's Frontgate, Ballard Designs and Grandin Road (#28), Room & Board (#29), At Home (#30, checked below), Ethan Allen (#32, public), Design Within Reach in MillerKnoll (#34), Bassett (#46), **World Market (#49)**: HNN says "Part of investment firm Kingswood Capital Management out of Los Angeles." (trade press); "World Market" is on [Kingswood's portfolio page](https://www.kingswood-capital.com/portfolio/), which has no current or exited marker. Kingswood reports PE funds on Form ADV (Y, 15).

**Scan leads (checked, outside the top 10):**

| Lead | Owner | Owner type | PE status | Evidence |
|---|---|---|---|---|
| At Home (HNN #30; 229 stores, "At Home operates across 39 states and online.") | a group of its lenders since its exit from Chapter 11 (Hellman & Friedman's equity cancelled) | investment funds (Redwood, Farallon and Anchorage all ADV N) | none | [Release, 2025-10-24](https://aall.investorroom.com/news?item=559), a reprint on a Cision investorroom host that appears to be a demo site, not At Home's own: "In connection with its emergence, the Company has executed a transition of ownership of At Home to a group of its lenders, including funds affiliated with Redwood Capital Management, LLC, Farallon Capital Management, L.L.C. and Anchorage Capital Advisors, L.P." |
| The Shade Store (window treatments; not in HNN) | Leonard Green & Partners | PE firm | PE-owned (no stake stated; LGP calls it growth equity) | [LGP portfolio](https://www.leonardgreen.com/portfolio/): "The Shade Store is a leading omni-channel provider of custom window treatments in the United States." Fields: "Deal Type: Growth Equity", "Status: Current" |
| Visual Comfort & Co. (lighting, sold mainly through trade channels; not in HNN) | Leonard Green & Partners (trade press names AEA and Goldman Sachs as co-owners; not checked) | PE firm | PE-owned | [LGP portfolio](https://www.leonardgreen.com/portfolio/): "Visual Comfort is a leading provider of decorative and functional lighting as well as ceiling fan products primarily serving the residential end-market." Fields: "Deal Type: Buyout", "Status: Current" |
| Brooklinen (DTC bedding; not in HNN) | Freeman Spogli (2021 investment and Summit Partners' retained stake per trade press; no stakes stated) | PE firm | PE-owned by the no-stake default (weak: the portfolio page lists it with no status) | [Freeman Spogli portfolio](https://www.freemanspogli.com/portfolio/): "Brooklinen" appears in the list |

**Rollups with local names:** Berkshire Hathaway's furniture division (HNN #12, $1,915.0M, 33 stores: Nebraska Furniture Mart, Jordan's, RC Willey, Star Furniture; owner a public company). Ashley licensees run Ashley-named stores (Broad River Retail, Factory Direct Enterprises, 1915 South, The Wellsville Group, The Parrott Group and others in HNN); the Ashley name belongs to Ashley, so these aren't separate brands. Multi-name regional groups (Regency Management Services, Furniture Mart USA) were not checked.

**PE share by brand row:** 1 of 10 (10%): Bob's Discount Furniture (PE-owned). Owner not found: 1 (Rooms To Go, privately held, owner not named). Sales share of the PE row: $2,332.5M of $30,068.4M in the ten rows (7.8%).

**National brands:** about 35 names a 30-brand audit could draw on, counting each retailer once:
- about 25 multi-state specialists in the HNN 125: the ten rows plus Crate & Barrel, Lovesac, Havertys, Living Spaces, Room & Board, At Home, Ethan Allen, Design Within Reach, Bassett, World Market, Frontgate and Ballard Designs, Bed Bath & Beyond (online), Roche Bobois, Mor, Slumberland;
- about 10 decor and DTC brands HNN doesn't measure, because accessories, rugs and textiles are excluded from its sales: HomeGoods, Kirkland's, The Shade Store, Visual Comfort, Brooklinen, Article, Burrow, Castlery, Serena & Lily, Parachute (only the first five were looked at).
Sub-brands such as Pottery Barn and West Elm would add more. At least four PE-owned names sit outside the top 10 (World Market, The Shade Store, Visual Comfort, Brooklinen).

**Verdict:** audit candidate (10% to 20%). One PE row (Bob's, Bain) at 10 brands; a 30-brand audit would draw on about 35 national names, at least five of them PE-owned on this screen's evidence.

## 2. Casinos

**Consumer-facing brand: the operator's brand.** Rows are casino operators (Caesars, MGM, PENN and so on), not property names (Bellagio, Borgata), applied the same way to every row. Reasons:
- the operator's name is the one name that spans its casinos;
- property names run to hundreds, most of them single sites, which behave like rollup locations with local names;
- the only free size measure found, SEC revenue, is reported per operator.

The cost of this rule: three of the ten operators run casinos that mostly keep local names (Boyd, Churchill Downs, Golden), so they sit close to rollups. They are kept as rows here, and the alternative count is under open questions. A REIT that owns casino buildings (VICI, GLPI) is never the brand owner.

**Ranking:** no free trade-press ranking of US casino operators turned up in seven searches (AGA's State of the States ranks markets, and CDC Gaming ranks properties outside Nevada and Mississippi only). Rows are therefore ordered by 2025 total revenue from the SEC's XBRL frames, an official data set that knows nothing about ownership ([Revenues](https://data.sec.gov/api/xbrl/frames/us-gaap/Revenues/USD/CY2025.json), [ASC 606 excl. tax](https://data.sec.gov/api/xbrl/frames/us-gaap/RevenueFromContractWithCustomerExcludingAssessedTax/USD/CY2025.json), [incl. tax](https://data.sec.gov/api/xbrl/frames/us-gaap/RevenueFromContractWithCustomerIncludingAssessedTax/USD/CY2025.json)). Las Vegas Sands is left out, having had no US casinos since its 2022 Las Vegas sale. MGM's and Wynn's totals include Macau. The method is flagged: it covers only operators that file with the SEC, so large tribal and private operators can't be placed (listed after the table).

| # | Brand (2025 revenue) | Owner (as stated) | Owner type | PE status | Since | Evidence |
|---|---|---|---|---|---|---|
| 1 | MGM Resorts (incl. MGM Grand, Bellagio, Borgata) ($17,538M) | MGM Resorts International (NYSE: MGM); IAC 25.73% by 13D | public company (IAC is itself public) | none (Vanguard 11.91%, Davis 10.48% (ADV N), BlackRock 5.02%) | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/789570/000119312526129074/d899213ddef14a.htm): "Based on Schedule 13D/A filed by IAC, Inc. with the SEC on December 9, 2025. Reflects sole voting power and sole dispositive power of 65,822,350 shares." |
| 2 | Caesars (incl. Harrah's, Horseshoe) ($11,486M) | Caesars Entertainment, Inc. (NASDAQ: CZR); **pending** take-private by Fertitta Gaming Holdco (Tilman Fertitta's Fertitta Entertainment) | public company (pending: family) | none (BlackRock 13.5%, Pentwater 5.60% by 13G (ADV N), Vanguard 5.06%) | merger agreement 2026-05-27; still listed (no delisting filing as of 2026-11-17) | [Merger proxy, 2026-08-26](https://www.sec.gov/Archives/edgar/data/1590895/000119312526365696/d143368ddefm14a.htm): "The board of directors of the Company (the “Board”) has approved an Agreement and Plan of Merger, dated as of May 27, 2026" … "wholly owned subsidiary of Fertitta Gaming Holdco, LLC". "Landry’s Fertitta, LLC (the “Parent Guarantor”) is a Texas limited liability company and subsidiary of Fertitta Entertainment, Inc." |
| 3 | Wynn and Encore ($7,138M) | Wynn Resorts, Limited (NASDAQ: WYNN) | public company | none (Tilman Fertitta 12.11%, Vanguard 10.44%, Capital World 9.21%, Elaine Wynn Family Trust 9.17%, Galaxy Entertainment group 5.00%) | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/1174922/000119312526124077/d26334ddef14a.htm): "Blossom is a wholly-owned subsidiary of Herobright, which itself is wholly owned by Galaxy." |
| 4 | PENN (Hollywood Casino, Ameristar, Argosy and others) ($6,961M) | PENN Entertainment, Inc. (NASDAQ: PENN) | public company | none (BlackRock 13.2%, Vanguard 12.3%) | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/921738/000114036126016846/ny20062568x1_def14a.htm): "Beneficial Owners of 5% or more of our common stock:" BlackRock and Vanguard only |
| 5 | Boyd Gaming ($4,092M) | Boyd Gaming Corp. (NYSE: BYD); Boyd family (William S. Boyd 8.34%, Marianne Boyd Johnson 17.87%) | public company (family-led) | none (BlackRock 8.92%, Vanguard 9.87%, Cohen & Steers 5.46% (ADV N)) | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/906553/000119312526116798/d917131ddef14a.htm): "5% or Greater Stockholders" table as given |
| 6 | Churchill Downs ($2,926M) | Churchill Downs Inc. (NASDAQ: CHDN) | public company | none (Vanguard 9.65%, BlackRock 9.58%) | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/20212/000119312526104118/d123994ddef14a.htm): "We are not aware of any pledge of our Common Stock or any other arrangements the operation of which may at a subsequent date result in a change in control of our Company." |
| 7 | Bally's ($2,436M; "20 casinos globally", 11 US states) | Bally's Corporation (NYSE: BALY), controlled by Standard General, 66.8% | PE firm (ADV Y, 5 PE funds) | **PE-owned** | majority since the 2025 merger (its 2024-10-17 merger proxy; closing date not read) | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/1747079/000174707926000028/baly-20260409.htm): "As of the record date, entities affiliated with Standard General L.P. (“Standard General”) beneficially owned an aggregate of 66.8% of our outstanding common shares." [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1747079/000174707926000019/baly-20251231.htm): "As of February 28, 2026, we own and operate 20 casinos globally, including in the United Kingdom (“UK”) and in 11 states"; "Bally’s is an iconic brand with broad recognition in the gaming industry." (Bally's is listed as its own brand; the licensed brands it names are others, such as Hard Rock for Hard Rock Biloxi.) |
| 8 | Station Casinos (Red Rock Resorts) ($2,011M) | Red Rock Resorts, Inc. (NASDAQ: RRR); Fertitta family entities above 50% of votes | family | none | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/1653653/000119312526173964/d52675ddef14a.htm): "The Fertitta Family Entities hold more than 50% of the voting power of our shares eligible to vote." |
| 9 | Golden Entertainment (The STRAT, others) ($635M, its last year as a public company) | Argento, LLC, controlled by Blake Sartini, owns the operations; VICI took the real estate | family | none | delisted 2026-04-30 | [Merger proxy](https://www.sec.gov/Archives/edgar/data/1071255/000119312526096620/d26120ddefm14a.htm): "OpCo Buyer is controlled by Blake Sartini, the Chief Executive Officer and Chairman of the Board." [GAMCO 13D/A, 2026-05-04](https://www.sec.gov/Archives/edgar/data/1071255/000080724926000047/xslSCHEDULE_13D_X02/primary_doc.xml): "As a result of the completion of the acquisition of the Issuer by VICI Properties, Inc., the Reporting Persons no longer have beneficial ownership of any of the Issuer's shares." |
| 10 | Century Casinos ($573M) | Century Casinos, Inc. (NASDAQ: CNTY) | public company | none (13G holders Vanguard, Royce, Veradace and Rice Hall James, all ADV N); Brigade (ADV Y) has a board nomination agreement but no 5% stake | | [Proxy 2026](https://www.sec.gov/Archives/edgar/data/911147/000091114726000012/cnty-20251231xdef14a.htm): "Royce & Associates, LP has sole voting and dispositive power with respect to 1,585,158 shares." "the Company entered into a nomination and standstill agreement (the “Nomination Agreement”) with Brigade" |

Next in the frames (not rows): Monarch Casino ($545M), Full House Resorts ($302M); owners not checked.

**Large operators with no public revenue figure (not placed; two checked):**
- **The Venetian Resort Las Vegas.** The operator is Apollo funds, per [VICI 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1705696/000170569626000034/vici-20251231.htm): "Funds managed by Apollo Global Management, Inc." But the name is licensed. [Las Vegas Sands 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1300514/000130051426000013/lvs-20251231.htm): "We have licensed the “Venetian” and “Palazzo” brands and certain other trademarks related to the Las Vegas Operations pursuant to the agreements effecting the Las Vegas Sale." Under the licensing rule the brand belongs to Las Vegas Sands (public), so it is not a PE brand even if placed.
- **Hard Rock.** Seminole Tribe of Florida (tribal government), per [Hard Rock release, 2022-06-14](https://www.hardrock.com/blog/hard-rock-international-wraps-up-its-50th-anniversary-with-activations-all-over-the-world): "the Seminole Tribe of Florida acquired the Hard Rock brand". Not PE.
- **Not checked:** Mohegan (tribal; it stopped filing 10-Ks after FY2022), Resorts World (Genting), Cordish (Live!), Rush Street (Rivers), Foxwoods (tribal), Fontainebleau Las Vegas, and multi-casino tribal operators such as the Choctaw and Chickasaw Nations.

**Rollups with local names:** under the operator-brand rule every operator is a row, but Boyd (Orleans, Sam's Town and others), Churchill Downs (Derby City Gaming, Oxford and others) and Golden (The STRAT, Arizona Charlie's, PT's taverns) mostly keep local property names. The PE-owned row (Bally's) is the reverse case: per its 10-K it has "undertaken a comprehensive rebranding initiative across our casinos".

**PE share by brand row:** 1 of 10 (10%): Bally's (PE-owned). Owner not found: 0. Revenue share of the PE row: $2,436M of $55,796M in the ten rows (4.4%).

**National brands:** about 15 to 20 operators run casinos in more than one state. Seen in this screen: Caesars, MGM, PENN, Boyd, Bally's, Churchill Downs, Wynn (Nevada and Massachusetts), Century, Hard Rock. Known but not checked: Full House, Monarch, Cordish, Rush Street, Genting, Mohegan, Jacobs Entertainment, Delaware North, Maverick Gaming. A 30-brand operator audit would run out of multi-state operators and need single-state operators, tribal operators or property brands.

**Verdict:** audit candidate (10% to 20%). One PE row (Bally's, Standard General 66.8%). The scan's Venetian lead doesn't count, because Apollo's operator licenses the name from Las Vegas Sands. A 30-brand audit has about 15 to 20 multi-state operators to draw on, so it would first need the brand rule settled (operators or property names).

## Form ADV check (SEC `ia110226-registered`, `ia11022026-exempt`, November 2026)

| Firm (role) | Adviser entity | CRD | Type | Any PE Funds | PE funds |
|---|---|---|---|---|---|
| Bain Capital (Bob's) | Bain Capital Private Equity, LP | 145653 | RIA | Y | 36 |
| Standard General (Bally's) | Standard General L.P. | 151831 | RIA | Y | 5 |
| Leonard Green (The Shade Store, Visual Comfort) | Leonard Green & Partners, L.P. | 158164 | RIA | Y | 107 |
| Kingswood (World Market) | Kingswood Capital Management, L.P. | 304649 | RIA | Y | 15 |
| Freeman Spogli (Brooklinen; Arhaus, former) | Freeman Spogli Management Co., L.P. | 156819 | RIA | Y | 7 |
| Summit Partners (Brooklinen, trade press only) | Summit Partners, L.P. | 135271 | RIA | Y | 87 |
| Apollo (Venetian operator, licensee) | Apollo Capital Management, L.P. | 143161 | RIA | Y | 214 |
| Hellman & Friedman (At Home, equity cancelled 2025) | Hellman & Friedman LLC | 158614 | RIA | Y | 45 |
| Brigade (Century nomination agreement, no 5% stake) | Brigade Capital Management, LP | 144078 | RIA | Y | 2 |
| Redwood (At Home) | Redwood Capital Management, LLC | 158243 | RIA | N | |
| Farallon (At Home) | Farallon Capital Management, L.L.C. | 107322 | RIA | N | |
| Anchorage (At Home) | Anchorage Capital Advisors, L.P.; Anchorage Capital Group, L.L.C. | 328998; 135657 | RIA | N | |
| Pentwater (Caesars 13G) | Pentwater Capital Management LP | 156873 | RIA | N | |
| Davis (MGM 13G) | Davis Selected Advisers LP | 108674 | RIA | N | |
| Capital World Investors (Wayfair, Wynn) | Capital Research and Management Company | 110885 | RIA | N | |
| Citadel (RH 13G) | Citadel Advisors LLC | 148826 | RIA | N | |
| Aristotle (Williams-Sonoma 13G) | Aristotle Capital Management, LLC | 109876 | RIA | N | |
| Blackhill (Williams-Sonoma 13G) | Blackhill Capital, Inc. | 105208 | RIA | N | |
| Cohen & Steers (Boyd 13G) | Cohen & Steers Capital Management, Inc. | 106266 | RIA | N | |
| Veradace (Century 13G) | Veradace Capital Management LLC | 301703 | ERA | N | |
| Royce (Century 13G) | Royce & Associates, LP | 107689 | RIA | N | |
| Rice Hall James (Century 13G) | Rice Hall James & Associates LLC | 125410 | RIA | N | |

Not advisers, or not in either file: Susquehanna (none of its entities), IAC and Galaxy Entertainment (public companies), Fertitta Entertainment and Argento (family), the Seminole Tribe, Inter IKEA, VICI (a REIT). Two Australian ERAs named "Anchorage Capital Partners" report PE funds, but their domain is anchoragecapital.com.au, a different firm from At Home's US lender (anchoragecapital.com).

## Quote check

50 of 50 quotes found verbatim in the saved page text (whitespace, curly quotes, dashes and zero-width characters normalized); 7 of 7 altered quotes failed. Not covered: values read from tables or form fields (proxy percentages, XBRL revenues, HNN sales and store counts, 13D/13G cover-page percentages such as Susquehanna's 4.0% and Friedman's 23.88%, LGP's "Status: Current" fields).

## Robots and blocked pages

- robots.txt was read before the first request to each of 14 hosts and checked for `*`, `EvidenceEngine`, ClaudeBot, Claude-User, Claude-SearchBot and anthropic-ai. Only raymourflanigan.com names Claude agents, and it allows them.
- Crawl delays were honored: leonardgreen.com 10 s, kingswood-capital.com 1 s, raymourflanigan.com 0.7 s. data.sec.gov's robots.txt returned 404 (no restrictions).
- Redirects were not followed blindly. kingswood-capital.com returned 301 to www.kingswood-capital.com, whose robots.txt was read before the request. ashleyfurniture.com returned 308 to the same path without the trailing slash, on the same host.
- One judgment call: aall.investorroom.com's robots.txt returned 302 to a not-found page; it was treated as no robots file (a 4xx-equivalent), and one page was fetched.
- No 401, 403 or 429 responses, no challenge pages, no Playwright use.
- SEC requests were paced at one every 1.2 s or slower.
- Bot slips: none known.

## Surprises

- **The Venetian is a licensed name.** Las Vegas Sands licenses "Venetian" and "Palazzo" to the Apollo-owned operator. Under the licensing rule the brand is Sands', so the scan's only casino lead is not a PE brand.
- **Caesars is being taken private by Tilman Fertitta** (merger agreement 2026-05-27, $31.00 a share in cash, special meeting 2026-09-22, not yet closed). He is a family owner, not PE, so the casino count doesn't change when it closes. He also holds 12.11% of Wynn.
- **Bally's is PE-owned:** Standard General holds 66.8%, and its Form ADV reports 5 PE funds.
- **Golden Entertainment went private in 2026,** with operations to Blake Sartini and real estate to VICI.
- **Bob's Discount Furniture listed in February 2026** and is still about 73% Bain.
- **At Home is now owned by credit funds** (Redwood, Farallon, Anchorage, all ADV N) after Hellman & Friedman's equity was cancelled in Chapter 11, so that lead no longer counts.
- **Freeman Spogli has left Arhaus;** its own proxy calls FSP "a former investor".
- **Leonard Green owns two of the scan's leads** (The Shade Store, Visual Comfort). Neither is a furniture retailer, so neither is in the sales ranking.
- **HNN names Kingswood as World Market's owner** (#49).
- **RH briefly had a 5.3% Susquehanna holder,** which fell to 4.0% on 2026-11-16. That ends the hop under the 5% rule, whatever Susquehanna's kind.

## Open questions for the developer (numbers only; nothing decided)

1. **Casino row rule:** with operator brands (this report), 1 of 10 (10%). Treating Boyd, Churchill Downs and Golden as rollups because their casinos mostly keep local names gives 1 of 7 (14.3%). Property-name rows would need a property ranking, and none is free for Nevada.
2. **Casino ranking coverage:** SEC filers only. Adding Hard Rock and The Venetian as rows gives 1 of 12 (8.3%) under the licensing rule, or 2 of 12 (16.7%) if the Venetian's operator (Apollo) were read as the brand owner.
3. **Licensed casino names:** the Venetian (Sands licenses the name to Apollo's operator) and Hard Rock (it licenses its name to other operators, such as Bally's Hard Rock Biloxi) both separate the name's owner from the casino's operator.
4. **Home furnishings scope:** HNN measures furniture and bedding sales only, so decor-led chains rank low or not at all. HomeGoods sits inside TJX (#24), At Home is #30 (not PE), World Market is #49 (PE), and Kirkland's isn't in the top 100. The DTC leads (The Shade Store, Visual Comfort, Brooklinen, all PE) aren't measured at all.
5. **Rooms To Go:** the one owner not found (privately held, founder-led).
6. **Audit pools:** home furnishings has about 35 national names (at least 5 PE-owned found here: Bob's, World Market, The Shade Store, Visual Comfort, Brooklinen). Casinos have about 15 to 20 multi-state operators (1 PE-owned row found here, plus the Venetian licensee case).

## Cost

- 63 page fetches (61 OK, one 301, one 308; 0 refused): 46 from SEC hosts (24 www.sec.gov, 22 data.sec.gov) and 17 from 12 other hosts.
- 15 robots.txt requests (14 hosts plus one redirect hop) and 17 web searches.
- Roughly 170k tokens; about 45 minutes.
