# Follow-up audit: Home furnishings

Ticket: [93-research-follow-up-audits-four-industries](../../issues/93-research-follow-up-audits-four-industries.md), item 2 · Worker report, researched 2026-11-17 (fetches logged 2026-11-17T23:55Z to 2026-11-18T00:12Z) · Ownership facts come from primary sources only. Two trade or vendor pages (Home News Now, StorageCafe) supply the ranking only.

Saved pages, scripts and logs are in the session scratchpad (temporary): pages under `pages/fu-home/` (NNN.html raw, NNN.txt visible text, `index.tsv`, `robots.tsv`, `robots/`), reused screen pages under `pages/screen2-b/`, scripts under `scripts/fu-home/` (`robots.py`, `fetch.py`, `pw.py`, `adv.py`, `bdc.py`, `ctx.py`, `qcheck.py`, `quotes.tsv`).

**Short answer**

| | Home furnishings (N = 30 brand rows, composite of two rankings) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **2 / 30 (6.7%)**: Bob's Discount Furniture (Bain Capital, about 73% of a listed company) and World Market (Kingswood Capital, current on its portfolio page). Both PE-owned; no PE minority stake. |
| Owner not found | **0 / 30.** Rooms To Go names its founders and says it is privately held but not who owns it (1 row "owner not stated"; the screen counted it as not found, which would give 1 / 30). |
| By parent company | 2 / 15 parents (13.3%). The 30 rows belong to 15 parents; Williams-Sonoma (8 rows), Wayfair (5), Berkshire Hathaway (3), La-Z-Boy (2) and TJX (2) hold 20 of them. |
| By sales | 7.5%: $2,581.5M of $34,527.4M (HNN 2025 US furniture and bedding sales of the 15 parents). |
| Brand-direct affiliate programs | **0 confirmed.** PE rows: World Market (footer checked, none; network listings in search only), Bob's (homepage is script-only; none found). Non-PE: Wayfair and Ashley footers checked, none. Network listings came up in search for Wayfair, La-Z-Boy, Rooms To Go and Crate & Barrel (leads, not opened). 24 rows not checked. |
| BDC overlap | **1 row:** RH ("Restoration Hardware, Inc.", Apollo Debt Solutions BDC, first-lien term loan). None for the two PE rows. Off-list, the screen's DTC leads both borrow from BDCs (The Shade Store, LLC: three Blue Owl BDCs; Visual Comfort, as VC GB Holdings I Corp: Apollo Debt Solutions BDC). |

- **No free ranking measures direct-to-consumer home brands.** The list is a composite of a furniture-and-bedding sales ranking (HNN 125) and a home-décor store-count ranking (StorageCafe). DTC brands enter only where those rankings name them (Wayfair's online brands, Joybird). The screen's three DTC PE leads (The Shade Store, Visual Comfort, Brooklinen) are in no ranking found, so they are not rows.
- **Every blind variant lands near 7%.** The banner walk (this list) and a one-row-per-parent list both give 2 PE rows of 30 and no PE minority stake; the next 17 rows past the cut add no PE row. The share passes 10% only if the DTC leads are counted (5 / 30, 16.7%, if they replaced the walk's last three rows) or if Frontgate's new owner (after QVC Group's 2026 deregistration) turns out to be PE in the one-row-per-parent list (3 / 30, 10.0%).
- **The rule "each consumer-facing name is a row" fills the list with large public companies' banners.** 22 of 30 rows are public-company banners (Williams-Sonoma 8, Wayfair 5, Berkshire 3, La-Z-Boy 2, TJX 2, RH, Arhaus). None of their 5%+ holders is a PE firm filing a 13D or a non-passive 13G.
- **Two Form ADV `Y` holders turned up and neither counts.** Fidelity Management & Research Company LLC reports PE funds (1), but FMR LLC's 13Gs on Wayfair (14.0%) and RH (14.999%) are filed under Rule 13d-1(b). Hood River Capital Management (Y, 3 funds) holds 6.76% of Lovesac (a next row) under Rule 13d-1(b).

## How this was sourced (read first)

- **Ranking:** composite of Home News Now's "HNN 125 Furniture and Bedding Retailers 2025" and StorageCafe's "The 10 Largest Home Décor Brands in the U.S." (2026-05-06). Both used for the ranking only, never as ownership evidence. See "Ranking".
- **Ownership facts** come from SEC filings (10-K, DEF 14A, Schedules 13D and 13G), sponsor releases and portfolio pages (Kingswood), company pages (Otto Group, AFW, Slumberland, Mor, Room & Board, World Market) and Form ADV. Pages the screen worker saved on 2026-11-17 were reused without refetching: Ashley, Rooms To Go, IKEA, Inter IKEA, Raymour & Flanigan, the Bob's 10-K, the Wayfair, Williams-Sonoma, RH, La-Z-Boy and Arhaus proxies, the RH Schedule 13G/A of Susquehanna, the At Home release (a reprint, flagged), and the Leonard Green and Freeman Spogli portfolio pages.
- **SEC access:** 25 requests (17 www.sec.gov, 8 data.sec.gov), all HTTP 200, user agent `EvidenceEngine ownership-research bot (follow-up audits)` with no contact detail, paced at one request per 1.25 s or slower.
- **Robots:**
  - Every host's robots.txt was read and parsed by `robots.py` in a separate, earlier command; `fetch.py` refuses any host whose robots.txt has not been read and never requests robots.txt itself. Redirects were never followed (curl without -L).
  - Rules for `*`, EvidenceEngine, ClaudeBot, Claude-User, Claude-SearchBot and anthropic-ai were all applied; a path had to pass every one.
  - Crawl delays honored: afw.com 2 s, livingspaces.com 1 s, roomandboard.com 10 s, homepagenews.com 3 s.
  - today.yougov.com's robots.txt returned 301 to yougov.com/en-us/robots.txt. yougov.com/robots.txt (allows `/` for `*`) and then the redirect target (404, so no restrictions) were read in later, separate commands before any yougov.com page. No today.yougov.com page was requested.
  - www.joybird.com's robots.txt returned 301 to joybird.com; that host was never requested.
  - robots.txt returned 403 at www.storagecafe.com, www.crateandbarrel.com and www.athome.com (no restrictions under RFC 9309). Only StorageCafe was then requested (see next point).
- **Blocked or failed:**
  - **rankings.newsweek.com disallows ClaudeBot and anthropic-ai** (`Disallow: /`), so Newsweek's America's Best Online Shops and Retailers rankings were not used.
  - **farmershomefurniture.com disallows ClaudeBot and anthropic-ai**, so Farmer's Home Furniture (a next row) was not fetched.
  - **StorageCafe** answered curl with HTTP 403 and a "Just a moment..." challenge page. It got one retry in the Playwright browser (own user agent, no clicks, 15 s wait), which cleared by itself and returned the article (page 007). **Judgment call for the developer:** the brief says 403 means no, and also that a challenge page gets one browser retry; this was a challenge page served with 403.
  - 404s: homenewsnow.com (one guessed URL), livingspaces.com/about-us, slumberland.com/about-us, roomandboard.com/about (the 404 page still carries the site footer, which is quoted). morfurniture.com/about-us returned 301 to the same host's /pages/about-us, which was then fetched.
  - Similarweb's free furniture ranking shows only 5 sites; YouGov's free specialty-retail ranking shows 11 rows, none of them home stores; HomePage News' Top 50 covers housewares (appliances, cookware, tabletop), not home furnishings.
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist, Private Equity Vet; PitchBook, CB Insights and Preqin results; crateandbarrel.com and athome.com (robots 403, likely bot walls; no page tried); Business Wire.
- **Leads only, never cited:** Wikipedia and its mirrors, trade press on deals, affiliate-network directories (FlexOffers, Awin, Impact listings, affi.io, revshare), xMap's store-count blog (data unreliable: it ranks "Cramco" and "PackTowl" as furniture stores).
- **Owner kinds are research notes, not engine classifications.** "PE-owned" means control or a PE owner with no stated stake. Counts are by brand row.
- **Quotes** are copied from saved curl or Playwright text with whitespace collapsed; see "Quote check".

## Ranking

**No single free ranking covers furniture, décor chains and DTC brands.** Checked and rejected: Similarweb's US furniture website ranking (top 5 free only), Newsweek/Statista online-shop and retailer rankings (robots disallow ClaudeBot), YouGov Ratings (free list too short, no home category), Home Textiles Today's Top 50 (not free; latest summary is 2024), HomePage News' Top 50 Housewares Retailers (housewares, not furniture or décor), Digital Commerce 360's Top 1000 (paywalled beyond a top 5), xMap's store-count blog (unreliable data). No ranking of DTC home brands by sales, traffic or popularity was found free of charge.

**Composite used.**

(a) **StorageCafe, "The 10 Largest Home Décor Brands in the U.S.", 2026-05-06** ([page 007](https://www.storagecafe.com/blog/top-us-home-decor-brands-and-stores/)): "This article ranks the 10 largest U.S.-born home décor brands by number of physical locations nationwide as of 2026." Its rows: 1 Michaels (~1,238), 2 Hobby Lobby (~1,057), 3 HomeGoods (~967), 4 Ashley HomeStore (~769), 5 World Market (~246), 6 At Home (~220), 7 Pottery Barn (~173), 8 West Elm (~109), 9 Homesense (~77), 10 RH (~75). Michaels and Hobby Lobby are arts-and-crafts chains (a separate screened industry) and are left out. **All 8 home rows are in.**

(b) **Home News Now, "HNN 125 Furniture and Bedding Retailers 2025"** (five installments, 2026-05-26 to 2026-06-22; [1-25](https://homenewsnow.com/blog/2026/06/22/home-news-now-125-furniture-bedding-retailers-2025-nos-1-25/), [26-50](https://homenewsnow.com/blog/2026/06/14/home-news-now-125-furniture-bedding-retailers-2025-nos-26-50/), [51-75](https://homenewsnow.com/blog/2026/06/07/home-news-now-125-furniture-bedding-retailers-2025-nos-51-75/), [76-100](https://homenewsnow.com/blog/2026/05/31/home-news-now-125-furniture-bedding-retailers-2025-nos-76-100/), [101-125](https://homenewsnow.com/blog/2026/05/26/home-news-now-125-furniture-bedding-retailers-2025-nos-101-125/)): "The 125 listing is based on estimated 2025 furniture and bedding sales in the U.S. and includes both brick-and-mortar stores and e-tailers." and "Accessories, rugs and other revenue sources are not included." **It fills the other 22 rows**, walked in rank order:
- **Banners are rows.** HNN ranks companies. Each company's home-furnishings banners enter at the company's rank. Order within a company: by the parent's stated revenue by brand where it reports one (Williams-Sonoma's 10-K), otherwise in the order the parent's 10-K or the HNN entry lists them. Banners come from the HNN entry or the parent's latest 10-K.
- **Left out of the walk:**
  - general merchants: Amazon (#3), Walmart (#5), Costco (#6), Target (#13), Sam's Club (#15), Home Depot (#22), Lowe's (#26), QVC and HSN within QVC Group (#28), Macy's Furniture Gallery (#69), Etsy (#72), Big Lots (#113). TJX (#24) is a general merchant, but **HomeGoods and Homesense are home-only banners** (TJX's 10-K runs them as a separate segment, and StorageCafe ranks both), so they are rows; T.J. Maxx, Marshalls and Sierra are out;
  - mattress specialists (their own industry): Mattress Firm, Sleep Number, Saatva, 3Z Brands, Avocado, Mattress Warehouse, Tempur Sealy, Casper, Purple, Tuft & Needle and the other bedding chains;
  - single-state chains (the grocery item's multi-state test, applied here too): City Furniture (#23, "operates throughout Florida"), Star Furniture (Texas; Berkshire), Homemakers (Iowa; NFM);
  - Ashley licensee groups and multi-name store operators, which own no brand of their own (Broad River Retail, Factory Direct Enterprises, 1915 South, The Wellsville Group, The Parrott Group, Regency Management Services, Furniture Mart USA);
  - banners that are not home furnishings or not consumer-facing: Williams Sonoma (the kitchen brand; Williams Sonoma Home is a row), Mark and Graham (monogrammed gifts), Wayfair Professional (business buyers), Garnet Hill (apparel).
- **Not exhaustive.** DTC home brands that no ranking found here measures: The Shade Store, Visual Comfort, Brooklinen, Parachute, Article, Burrow, Castlery, Lulu and Georgia, Serena & Lily, Boll & Branch, Cozy Earth; window-covering brands sold through dealers (Hunter Douglas, Levolor, Bali, Budget Blinds); lighting chains (Lamps Plus); Kirkland's and The Container Store (now in Bed Bath & Beyond, Inc. per HNN #53).

**Resulting cut:** row 30 is World Market. The walk's next rows are CB2, Crate & Kids and Hudson Grace (Crate & Barrel's banners), then American Furniture Warehouse (#20) and Living Spaces (#21); see "Next rows".

| # | Brand (source rank) | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Ashley (HNN #1, $6,257.3M; SC #4, ~769 stores) | Ashley Furniture Industries ("family-owned company") | family | none | n/a | — | maker-retailer; company-owned and dealer-owned (licensed) stores | none found (homepage HTML) | HF1 |
| 2 | Wayfair (HNN #2, $5,955.0M) | Wayfair Inc.; co-founders Shah and Conine 33.59% of voting power each | public company | none (FMR 14.0%, 13d-1(b)) | n/a | W | e-commerce plus stores | none found on homepage; network listings in search only | HF2 |
| 3 | AllModern | Wayfair Inc. | public company | none | n/a | W | e-commerce plus stores | not checked | HF2 |
| 4 | Birch Lane | Wayfair Inc. | public company | none | n/a | W | e-commerce plus stores | not checked | HF2 |
| 5 | Joss & Main | Wayfair Inc. | public company | none | n/a | W | e-commerce plus stores | not checked | HF2 |
| 6 | Perigold | Wayfair Inc. | public company | none | n/a | W | e-commerce plus stores | not checked | HF2 |
| 7 | Rooms To Go (HNN #7, $3,278.1M) | "privately held"; founders Jeffrey and Morty Seaman named; owner not stated | private, owner not stated | none found | n/a (founded 1990) | — | company stores | not checked (Awin listing in search) | HF3 |
| 8 | Pottery Barn (HNN #8 as Williams Sonoma, $2,900.0M; SC #7) | Williams-Sonoma, Inc. | public company | none (5% holders all 13G) | n/a | WSM | stores, e-commerce, catalog | not checked | HF4 |
| 9 | West Elm (SC #8) | Williams-Sonoma, Inc. | public company | none | n/a | WSM | stores, e-commerce | not checked | HF4 |
| 10 | Williams Sonoma Home | Williams-Sonoma, Inc. | public company | none | n/a | WSM | e-commerce, stores | not checked | HF4 |
| 11 | Pottery Barn Kids | Williams-Sonoma, Inc. | public company | none | n/a | WSM | stores, e-commerce | not checked | HF4 |
| 12 | Pottery Barn Teen | Williams-Sonoma, Inc. | public company | none | n/a | WSM | e-commerce, stores | not checked | HF4 |
| 13 | Rejuvenation | Williams-Sonoma, Inc. (acquired 2011) | public company | none | 2011 | WSM | stores, e-commerce; own factory | not checked | HF4 |
| 14 | GreenRow | Williams-Sonoma, Inc. | public company | none | n/a | WSM | e-commerce | not checked | HF4 |
| 15 | Dormify | Williams-Sonoma, Inc. (bought the IP in 2025; launched April 2026) | public company | none | 2025 | WSM | e-commerce | not checked | HF4 |
| 16 | IKEA (HNN #9, $2,810.0M) | brand: Inter IKEA Systems B.V., ultimately the Inter IKEA Foundation; US stores run by a franchisee (Ingka Group, per HNN) | foundation (brand owner) | none | 2023 (foundation) | — | franchised name | not checked | HF5 |
| 17 | RH (HNN #10, $2,335.0M; SC #10) | RH; Gary Friedman 23.88% (13D) | public company | none (FMR 14.999%, 13d-1(b); Susquehanna 4.0%, ended) | n/a | RH | galleries, outlets, e-commerce | not checked | HF6 |
| 18 | Bob's Discount Furniture (HNN #11, $2,332.5M) | Bob's Discount Furniture, Inc., "controlled by Bain Capital, which owns approximately 73%" | **PE-owned** | Bain Capital | before the 2026-02 IPO (purchase date not read) | BOBS | company showrooms, e-commerce | none found (homepage script-only) | HF7 |
| 19 | Nebraska Furniture Mart (HNN #12 as Berkshire furniture division, $1,915.0M) | Berkshire Hathaway Inc. | public company | not checked (5% holders not read) | n/a | BRK-A, BRK-B | company stores (NE, IA, KS, TX) | not checked | HF8 |
| 20 | R.C. Willey | Berkshire Hathaway Inc. | public company | not checked | n/a | BRK-A, BRK-B | company stores (UT, ID, NV, CA) | not checked | HF8 |
| 21 | Jordan's | Berkshire Hathaway Inc. | public company | not checked | n/a | BRK-A, BRK-B | company stores (MA, NH, RI, ME, CT) | not checked | HF8 |
| 22 | Raymour & Flanigan (HNN #14, $1,655.0M) | "our family-owned business" | family | none | n/a | — | company stores | not checked | HF9 |
| 23 | La-Z-Boy Furniture Galleries (HNN #16, $1,421.5M) | La-Z-Boy Inc. | public company | none (BlackRock, Vanguard, Dimensional; 13G) | n/a | LZB | about 60% company-owned, the rest dealer-owned (licensed) | not checked (FlexOffers listing in search) | HF10 |
| 24 | Joybird | La-Z-Boy Inc. | public company | none | n/a | LZB | e-commerce plus 15 small stores | not checked | HF10 |
| 25 | Arhaus (HNN #18, $1,124.0M) | Arhaus, Inc.; founder John Reed and family trusts control the vote | public company (founder-controlled) | none (Freeman Spogli "a former investor") | n/a | ARHS | showrooms, e-commerce | not checked | HF11 |
| 26 | Crate & Barrel (HNN #19, $1,045.0M) | Otto Group ("becomes a shareholder" 1998; stake not stated); Otto Group majority held by the Michael Otto Foundation | foundation / family (no stated stake: counts as control) | none | 1998 | — | stores, e-commerce, franchises abroad | not checked (Impact listing in search; site robots 403) | HF12 |
| 27 | HomeGoods (HNN #24 inside TJX, $700.0M; SC #3, ~967) | The TJX Companies, Inc. | public company | none (BlackRock 8.9%, Vanguard 8.44%) | n/a | TJX | off-price stores | not checked | HF13 |
| 28 | Homesense (SC #9, ~77) | The TJX Companies, Inc. | public company | none | n/a | TJX | off-price stores | not checked | HF13 |
| 29 | At Home (HNN #30, $550.0M; SC #6, ~220) | a group of its lenders (funds of Redwood, Farallon, Anchorage) since 2025-10 | investment funds, not PE (all three advisers' Form ADV say N) | none (Hellman & Friedman's equity cancelled in Chapter 11) | 2025-10-24 | — | company stores in 39 states | not checked (site robots 403) | HF14 |
| 30 | World Market (HNN #49, $249.0M; SC #5, ~246) | Kingswood Capital Management (acquired 2021-01-19; "current" on its portfolio page) | **PE-owned** | Kingswood Capital Management | 2021-01-19 | — | company stores, e-commerce | none found in footer; network listings (CJ, FlexOffers) in search only | HF15 |

### Evidence
- **HF1 Ashley**
  - Owner: "Ashley is a proud family-owned company with over 80 years of strong history in home furnishings." — [Ashley, About page, accessed 2026-11-17 (screen page 047)](https://www.ashleyfurniture.com/about-us)
  - Model: "Furniture manufacturer and retailer with more than 1,100 company-owned and dealer-owned Ashley Stores and Ashley Outlets in over 75 countries." — HNN 1-25 (ranking source; model only)
  - Licensed: dealer-owned Ashley stores use Ashley's name, so they are not separate brands.
  - Affiliate: none in the homepage HTML (page 049).
  - BDC names: "Ashley Furniture Industries, LLC", "Ashley Furniture Industries, Inc." (no BDC hit)
- **HF2 Wayfair, AllModern, Birch Lane, Joss & Main, Perigold**
  - Brands: "•AllModern: Modern made simple. •Birch Lane: Classic style for joyful living. •Joss & Main: The ultimate style edit for home. •Perigold: The destination for luxury home." and "Our Wayfair brand represents a significant majority of our net revenue" — [Wayfair Inc., Form 10-K FY2025, filed 2026-02-19](https://www.sec.gov/Archives/edgar/data/1616707/000161670726000027/w-20251231.htm)
  - Listing: "Class A Common Stock, $0.001 par value W The New York Stock Exchange" — same 10-K (cover table)
  - Control: "Holders of our Class B common stock are entitled to ten votes for each share held as of the Record Date on each proposal." — [Wayfair, DEF 14A 2026](https://www.sec.gov/Archives/edgar/data/1616707/000161670726000074/w-20260331.htm) (screen page 036). The table gives Niraj Shah 33.59% and Steven Conine 33.59% of total voting power (table values).
  - 5% holder: FMR LLC, "Percent of class represented by amount in row (9) 14.0 %", Rule 13d-1(b) box checked — [FMR LLC, Schedule 13G/A on Wayfair, filed 2026-11-05](https://www.sec.gov/Archives/edgar/data/1616707/000031506626002887/xslSCHEDULE_13G_X02/primary_doc.xml). The box is read from the form's checkbox image (`alt="Checkbox checked"`), not visible text.
  - Affiliate: none in the wayfair.com homepage HTML (page 048). Search showed FlexOffers "Wayfair North America" listings (not opened).
  - BDC names: "Wayfair Inc.", "Wayfair LLC" (no BDC hit)
- **HF3 Rooms To Go**
  - Owner: "Rooms To Go is an American furniture retailer founded by Jeffrey and Morty Seaman in 1990." and "Today, Rooms To Go remains a privately held company headquartered in Seffner, Florida," — [Rooms To Go, About page, accessed 2026-11-17 (screen page 045)](https://www.roomstogo.com/about-us)
  - Notes: the page names founders, not owners; no PE evidence. Counted "private, owner not stated", not "not found".
  - BDC names: "Rooms To Go", "RTG Furniture Corp." (no BDC hit)
- **HF4 Williams-Sonoma banners (Pottery Barn, West Elm, Williams Sonoma Home, Pottery Barn Kids, Pottery Barn Teen, Rejuvenation, GreenRow, Dormify)**
  - Brands: "Our brands — Williams Sonoma, Pottery Barn, Pottery Barn Kids, Pottery Barn Teen, West Elm, Williams Sonoma Home, Rejuvenation, Mark and Graham, and GreenRow — represent distinct merchandise strategies" — [Williams-Sonoma, Inc., Form 10-K FY2025 (FYE 2026-02-01), filed 2026-03-26](https://www.sec.gov/Archives/edgar/data/719955/000071995526000059/wsm-20260201.htm)
  - Order within the parent (revenue by brand, $000s): "Pottery Barn $ 2,999,332 $ 3,039,939 West Elm 1,859,501 1,840,582 Williams Sonoma 2 1,362,308 1,302,821 Pottery Barn Kids and Teen 1,138,051 1,107,057 Other 3 447,624 421,142" (footnote 2 says Williams Sonoma includes Williams Sonoma Home) and "Primarily consists of net revenues from Rejuvenation, Mark and Graham, our international franchise operations and GreenRow." — same 10-K. Kids and Teen share one figure and are listed in the 10-K's order; the "Other" brands follow in the 10-K's list order.
  - Dormify: "in 2025, we acquired the intellectual property of Dormify and are in the process of launching it as a new brand." — same 10-K; HNN (ranking source) adds "In April 2026, the company launched its newest brand, Dormify".
  - Listing: "Common Stock, par value $.01 per share WSM New York Stock Exchange, Inc." — same 10-K (cover)
  - 5% holders: "Information regarding our non-management 5% stockholders is derived from the most recently available 13G filings." — [WSM, DEF 14A 2026 (screen page 037)](https://www.sec.gov/Archives/edgar/data/719955/000071995526000109/wsm-20260506.htm). BlackRock 9.6%, Aristotle 7.8%, Blackhill 6.5%, State Street 5.2% (screen's table read); Aristotle and Blackhill ADV N; BlackRock and State Street file 13Gs under 13d-1(b).
  - Excluded banners: Williams Sonoma (kitchen) and Mark and Graham (gifts); see "Ranking".
  - BDC names: "Williams-Sonoma, Inc.", "Pottery Barn, LLC", "West Elm" (no BDC hit)
- **HF5 IKEA**
  - Brand owner: "© Inter IKEA Systems B.V. 1999-2026" — [IKEA US, About page footer (screen page 046)](https://www.ikea.com/us/en/this-is-ikea/about-us/)
  - Ultimate owner: "The new Inter IKEA Foundation will be the ultimate owner of Inter IKEA Holding B.V., the IKEA related business." — [Inter IKEA, "New owner of Inter IKEA Group" (screen page 048)](https://www.inter.ikea.com/en/newsroom/new-owner-of-inter-ikea-group)
  - Franchisee: "Part of the Ingka Group, total 2025 revenues were $5.3 billion for fiscal year ending August 31." — HNN 1-25 (ranking source; Ingka not checked from a primary page)
  - BDC names: "Inter IKEA Systems B.V.", "Ingka Holding B.V." (no BDC hit)
- **HF6 RH**
  - Holders: FMR LLC "Percent of Class: 14.999%", filed as "FMR LLC, is a parent holding company in accordance with Section 240.13d-1(b)(1)(ii)(G)." — [FMR LLC, Schedule 13G/A No. 15 on RH, filed 2024-11-12](https://www.sec.gov/Archives/edgar/data/1528849/000031506624002911/0000315066-24-002911.txt). The 2026 proxy shows FMR at 14.7%, BlackRock 7.0%, Citadel 5.0% ([screen page 038](https://www.sec.gov/Archives/edgar/data/1528849/000110465926054988/rh-20260618xdef14a.htm)); Gary Friedman 23.88% by 13D/A (screen page 041, cover value).
  - Ended holder: "G1 Execution Services, LLC, SIG Brokerage, LP, Susquehanna Investment Group and Susquehanna Securities, LLC are affiliated independent broker-dealers" — [Susquehanna, Schedule 13G/A at 4.0%, 2026-11-16 (screen page 063)](https://www.sec.gov/Archives/edgar/data/1528849/000144658026000115/xslSCHEDULE_13G_X02/primary_doc.xml). At 5% or less, the hop ends.
  - BDC: Apollo Debt Solutions BDC lists "Restoration Hardware, Inc." under "Household Durables", first-lien term loan (SEC BDC data set 2026_08, period 2026-06-30). The filer's text names the borrower "Restoration Hardware", which ties it to RH. "RH Buyer, Inc." (26North BDC, HPS) is an aerospace and defense borrower, not this RH.
  - BDC names: "Restoration Hardware, Inc.", "RH"
- **HF7 Bob's Discount Furniture**
  - Owner: "We are controlled by Bain Capital, which owns approximately 73% of our common stock." and "Bain Capital controls a majority of our outstanding common stock." — [Bob's Discount Furniture, Inc., Form 10-K FY2025 (screen page 035)](https://www.sec.gov/Archives/edgar/data/2085187/000162828026019015/a2025bdfannualfinancialsta.htm)
  - PE test: Bain Capital Private Equity, LP, Form ADV `Any PE Funds = Y` (36). A public company with a PE holder above 50% reads PE-owned.
  - Since: before the 2026-02-05 IPO; Bain's purchase date not read.
  - Affiliate: mybobs.com's homepage HTML is a script shell (57 characters of text); no program found in search.
  - BDC names: "Bob's Discount Furniture, Inc.", "Bob's Discount Furniture, LLC" (no BDC hit)
- **HF8 Nebraska Furniture Mart, R.C. Willey, Jordan's**
  - Owner: "The home furnishings retailing businesses consist of Nebraska Furniture Mart Inc. (“NFM”), R.C. Willey Home Furnishings (“R.C. Willey”), Star Furniture Company (“Star”) and Jordan’s Furniture, Inc. (“Jordan’s”)." — [Berkshire Hathaway Inc., Form 10-K FY2025, filed 2026-03-02](https://www.sec.gov/Archives/edgar/data/1067983/000119312526083899/brka-20251231.htm)
  - Multi-state test (same 10-K): NFM "located in Omaha, Nebraska, Clive, Iowa, Kansas City, Kansas and The Colony, Texas."; R.C. Willey "four stores located in Utah, one store in Meridian, Idaho, three stores in Nevada (Las Vegas and Reno) and two stores in the Sacramento, California area."; Jordan's "in stores located in Massachusetts, New Hampshire, Rhode Island, Maine and Connecticut."; excluded: "Star operates home furnishings retail stores in Texas."
  - Ticker: BRK-A and BRK-B (NYSE), from SEC's submissions record. 5%+ holders not read.
  - BDC names: "Nebraska Furniture Mart, Inc.", "R.C. Willey Home Furnishings", "Jordan's Furniture, Inc." (no BDC hit)
- **HF9 Raymour & Flanigan**
  - Owner: "community has always been at the heart of our family-owned business." — [Raymour & Flanigan, 2025 community giving post (screen page 044)](https://www.raymourflanigan.com/blog/community/giving-back/2025-community-giving)
  - BDC names: "Raymour & Flanigan", "Raymours Furniture Company, Inc." (no BDC hit)
- **HF10 La-Z-Boy Furniture Galleries, Joybird**
  - Owner: "growth of our consumer brands, La-Z-Boy and Joybird" — [La-Z-Boy Inc., DEF 14A 2026 (screen page 039)](https://www.sec.gov/Archives/edgar/data/57131/000005713126000024/lzb-20260714.htm)
  - 5% holders: "The following table provides information about entities that beneficially owned more than 5% of our common stock, as of June 26, 2026, according to reports filed with the SEC." — same proxy (BlackRock 15.3%, Vanguard 7.0% and 5.4%, Dimensional 6.6%, per the screen)
  - Model: "Approximately 60% of the La-Z-Boy Furniture Galleries are company-owned." — HNN 1-25 (ranking source). The rest are dealer-owned stores under La-Z-Boy's name.
  - BDC names: "La-Z-Boy Incorporated", "Joybird" (no BDC hit)
- **HF11 Arhaus**
  - Former PE: "Mr. Roth was not compensated for his services as a director because of his affiliation with Freeman Spogli, a former investor in the Company." — [Arhaus, Inc., DEF 14A 2026 (screen page 040)](https://www.sec.gov/Archives/edgar/data/1875444/000119312526138942/d45561ddef14a.htm)
  - Control: "36,470,752 shares of Class B common stock held by the 2018 Reed Dynasty Trust, of which Messrs. Adams and Beargie are trustees" — same proxy (John Reed 48.69% of combined voting power, per the screen's table read)
  - BDC names: "Arhaus, Inc.", "Homeroots Furniture" (no BDC hit)
- **HF12 Crate & Barrel**
  - Owner: "1998 The Otto Group becomes a shareholder of the furniture company Crate & Barrel from Chicago and therefore also does business on the US market." — [Otto Group, History and founder, accessed 2026-11-17](https://www.ottogroup.com/en/ueber-uns/historie-und-gruender.php); the group-companies page lists it: "Brand Concepts Bonprix Crate and Barrel Witt-Gruppe" — [Otto Group, Group companies](https://www.ottogroup.com/en/ueber-uns/konzernfirmen.php)
  - Otto Group's owner: "2015 Michael Otto founded the public-benefit–oriented Michael Otto Foundation, into which he contributed the majority of the company shares of the Otto Group." — [Otto Group, History and founder](https://www.ottogroup.com/en/ueber-uns/historie-und-gruender.php)
  - Notes: no page states Otto's stake in Crate & Barrel. Under the rules, a hop with no stated stake counts as control. HNN (ranking source) says "owned by the Germany-based Otto Group".
  - BDC names: "Crate and Barrel Holdings", "Euromarket Designs, Inc." (no BDC hit)
- **HF13 HomeGoods, Homesense**
  - Owner: "Our HomeGoods segment operates HomeGoods and Homesense chains in the U.S." — [The TJX Companies, Inc., Form 10-K FY2026 (FYE 2026-01-31), filed 2026-03-31](https://www.sec.gov/Archives/edgar/data/109198/000010919826000008/tjx-20260131.htm); listing: "Common Stock, par value $1.00 per share TJX New York Stock Exchange" (cover)
  - 5% holders: "each person known by us to be the beneficial owner of more than 5% of our outstanding common stock" — [TJX, DEF 14A, filed 2026-04-30](https://www.sec.gov/Archives/edgar/data/109198/000010919826000015/tjx-20260430.htm): BlackRock, Inc. 8.9% and The Vanguard Group, Inc. 8.44% (table values); both 13d-1(b) filers.
  - Decision: TJX is a general merchant, but HomeGoods and Homesense sell only home goods, have their own 10-K segment and are ranked by name in StorageCafe, so each is a row.
  - BDC names: "The TJX Companies, Inc.", "HomeGoods, Inc." (no BDC hit)
- **HF14 At Home**
  - Owner: "In connection with its emergence, the Company has executed a transition of ownership of At Home to a group of its lenders, including funds affiliated with Redwood Capital Management, LLC, Farallon Capital Management, L.L.C. and Anchorage Capital Advisors, L.P." — [At Home release 2025-10-24, as reprinted on aall.investorroom.com (screen page 052)](https://aall.investorroom.com/news?item=559). **Flag:** a reprint on a Cision host, not At Home's own domain (athome.com's robots.txt returned 403; Business Wire blocks bots).
  - Kind: Redwood (CRD 158243), Farallon (107322), Anchorage Capital Group (135657) and Anchorage Capital Advisors (328998) all report `Any PE Funds = N`, with no PE self-description in the release. Two Australian "Anchorage Capital Partners" ERAs report Y but are a different firm (anchoragecapital.com.au).
  - Footprint: "At Home operates across 39 states and online." — HNN 26-50 (ranking source)
  - BDC names: "At Home Group Inc.", "At Home Holding III Inc." (no BDC hit; "Choice Health at Home" and "Kindred at Home" are unrelated)
- **HF15 World Market**
  - Owner: "Kingswood Capital Management, LP (together with its affiliates, “Kingswood”) announced today that it has completed its acquisition of Cost Plus World Market (“World Market” or the “Company”), a national specialty retailer of home products sourced from around the world." — [Kingswood, release "Kingswood Capital Management Completes Acquisition of Cost Plus World Market"](https://www.kingswood-capital.com/kingswood-capital-management-completes-acquisition-of-cost-plus-world-market/)
  - Since: "LOS ANGELES, CA, January 19, 2021" (dateline, same release)
  - Owner kind: "Kingswood Capital Management, LP is a private investment firm primarily focused on investing in businesses in transition." (same release); Form ADV CRD 304649 `Any PE Funds = Y` (15).
  - Current: the portfolio page has the filter "Investment Status All Current Exited", and the World Market tile carries `data-status=".current."` and class `company-status-current` — [Kingswood, Portfolio, accessed 2026-11-18](https://www.kingswood-capital.com/portfolio/). That is an HTML attribute, not visible text; seen today, so it confirms the hop as current.
  - Brand: "Copyright ©2026 World Market" — [worldmarket.com homepage footer](https://www.worldmarket.com/); no affiliate link in the footer.
  - Lead: HNN 26-50 says "Part of investment firm Kingswood Capital Management out of Los Angeles." (trade press; ranking source only).
  - BDC names: "Cost Plus, Inc.", "Cost Plus World Market", "World Market" (no BDC hit)

### Next rows (past the cut; not counted in the 30)
The walk's next 17 rows, researched lighter (about 2 fetches each), to show what a deeper or differently built list would add:

| Next # | Brand (HNN rank) | Owner (as stated) | Owner kind | PE | Evidence |
|---|---|---|---|---|---|
| 31-33 | CB2, Crate & Kids, Hudson Grace (#19) | Crate & Barrel, Otto Group | foundation / family | none | "Crate and Kids, (formerly Land of Nods) focuses on creating inspiring spaces for babies and children"; "CB2 is known in the USA and Canada for high-quality designer furniture"; "Hudson Grace curates unique, authentic and functional products that enhance customers' everyday lives." — [Otto Group story, 2025-07-23](https://www.ottogroup.com/en/stories/story/bpk25/inspire-our-customers-to-build-a-home-with-purpose.php) |
| 34 | American Furniture Warehouse (#20) | family | family | none | "Still family-owned and operated, AFW has become one of the top retail furniture companies in the U.S." and "we’ve grown to 18 locations across Colorado, Arizona, and Texas." — [AFW, About](https://www.afw.com/about-us) |
| 35 | Living Spaces (#21) | not found | not found | none found | /about-us returned 404; 1 search. HNN: "Home furnishings retailer currently operating 42 showrooms, including two Outlets, across eight states in the West, Midwest and Southwest regions." |
| 36 | Lovesac (#25) | The Lovesac Company (public) | public company | none: Hood River (ADV Y) at 6.76% files under 13d-1(b) | "5% Stockholders: BlackRock, Inc.(1) 1,174,234 — 1,174,234 8.03% Anson Funds(2) 1,045,665 — 1,045,665 7.15% FMR LLC(3) 1,041,060 — 1,041,060 7.12% Hood River Capital Management(4) 987,744 — 987,744 6.76%" — [Lovesac DEF 14A 2026](https://www.sec.gov/Archives/edgar/data/1701758/000130817926000324/love015445-def14a.htm); Hood River's box: "An investment adviser in accordance with § 240.13d-1(b)(1)(ii)(E);" checked, Rule 13d-1(b) checked — [13G/A 2026-02-17](https://www.sec.gov/Archives/edgar/data/1701758/000121465926001755/xslSCHEDULE_13G_X01/primary_doc.xml) |
| 37 | Havertys (#27) | Haverty Furniture Companies (public); founder descendants control Class A | public company (family-controlled) | none | "Villa Clare Partners, L.P. 780 Johnson Ferry Road, NE, Atlanta, GA 30342 — — 603,497 (8) 49.9 %" and "The Class A Common stock includes designation rights for up to 75% of our Board, 10 votes per share on other matters" — [Havertys DEF 14A 2026](https://www.sec.gov/Archives/edgar/data/216085/000162828026021584/hvt-20260327.htm) |
| 38-40 | Frontgate, Ballard Designs, Grandin Road (#28) | not found: HNN names QVC Group's Cornerstone Brands ("CBI consists of home brands Frontgate, Ballard Designs and Grandin Road as well as apparel brand, Garnet Hill."), but QVC Group's SEC record now reads "Old QVC Group, Inc.", with no ticker and a Form 15-12G filed 2026-08-21 | not found | unknown | [QVC Group submissions record](https://data.sec.gov/submissions/CIK0001355096.json); successor owner not read |
| 41 | Room & Board (#29) | employee-owned | employee-owned | none | "100% Employee-ownedCertified B® Corporation" (site footer, read from the footer of a 404 page) — [roomandboard.com](https://www.roomandboard.com/about) |
| 42 | Ethan Allen (#32) | Ethan Allen Interiors (public) | public company | none: the 2026 13D filer is DGB Investment, Inc. (Doug Bergeron's company; not in Form ADV), "Percent of class represented by amount in Row (11) 4.2 %" | [13D/A 2026-11-09](https://www.sec.gov/Archives/edgar/data/896156/000092189526002982/xslSCHEDULE_13D_X02/primary_doc.xml); its nominees won three board seats on 2026-11-06 |
| 43 | Design Within Reach (#34, MillerKnoll) | MillerKnoll (public) | public company | none | "BlackRock, Inc. 10,413,184 (1) 15.15 %" (then Vanguard 7.51%, Dimensional 5.20%) — [MillerKnoll DEF 14A 2026](https://www.sec.gov/Archives/edgar/data/66382/000006638226000143/mlkn-20260828.htm) |
| 44 | Slumberland (#38) | family | family | none | "We are still family-owned with Ken's son, Kenny, at the helm" — [Slumberland, About](https://www.slumberland.com/pages/about-us); 68 of 119 stores franchised (HNN) |
| 45 | Mor Furniture for Less (#43) | an unnamed supplier since 2020 | not found | unknown | "Originally a family owned and operated company, Mor was acquired by one of our suppliers in 2020" — [Mor, About](https://www.morfurniture.com/pages/about-us) |
| 46 | Farmer's Home Furniture (#45) | not fetched (robots.txt disallows ClaudeBot and anthropic-ai); HNN says "Employee-owned" (trade press) | not found | unknown | — |
| 47 | Bassett (#46) | Bassett Furniture Industries (public) | public company | none: GAMCO 13D at 10.8% (Gabelli and GAMCO advisers all ADV N); Auto Services Company, Inc. 8.7% (13D/A 2026-11-02 shows 5.5% after a buyback) | "GAMCO Investors, Inc., et al. One Corporate Center Rye, NY 10580 934,150 (1) 10.8 %" — [Bassett DEF 14A 2026](https://www.sec.gov/Archives/edgar/data/10329/000143774926003747/bset20260206_def14a.htm) |

Next rows: 0 PE of 17; owner not found 6 (Living Spaces, Frontgate, Ballard Designs, Grandin Road, Mor, Farmer's).

### Rollups and groups that are not brands
- **Williams-Sonoma, Inc.:** 8 rows (HF4), plus Williams Sonoma and Mark and Graham (excluded by scope). Public (WSM).
- **Wayfair Inc.:** 5 rows (HF2), plus Wayfair Professional (excluded). Public (W), founder-controlled vote.
- **Berkshire Hathaway's furniture division:** 3 rows (HF8), plus Star and Homemakers (single-state). Public (BRK).
- **Otto Group / Crate and Barrel:** 1 row plus 3 next rows. Foundation-majority German group.
- **TJX:** 2 rows (HF13). Public.
- **La-Z-Boy Inc.:** 2 rows (HF10). Public.
- **Bed Bath & Beyond, Inc.** (HNN #53, $220.0M): per HNN, it now owns Bed Bath & Beyond, Overstock, buybuy BABY, Kirkland's and The Container Store. Not reached by the walk.
- **Ashley licensee groups** (Broad River Retail and others): run Ashley-named stores; the name is Ashley's.

### Category share
**All rows (N = 30).**
- **PE-owned: 2 / 30 = 6.7%**: Bob's Discount Furniture (Bain Capital, about 73% of a listed company, 10-K FY2025) and World Market (Kingswood, control by acquisition, current on the portfolio page today).
- **PE minority stake: 0.** PE-owned plus minority = **2 / 30 = 6.7%.**
- **Public company: 22 / 30 = 73.3%**: Wayfair's 5, Williams-Sonoma's 8, Berkshire's 3, La-Z-Boy's 2, TJX's 2, RH, Arhaus. No 5%+ holder is a PE firm filing a 13D or a non-passive 13G.
- **Other: 6 / 30 = 20.0%**: family 2 (Ashley, Raymour & Flanigan); foundation 2 (IKEA as brand owner, Crate & Barrel via Otto Group); investment funds, not PE, 1 (At Home); private, owner not stated 1 (Rooms To Go).
- **Not found: 0 / 30.**
- **By parent:** 15 parents; PE-held 2 / 15 = 13.3% (Bain's Bob's, Kingswood's World Market).
- **By sales (HNN furniture and bedding, parents of the 30 rows):** PE rows $2,581.5M of $34,527.4M = 7.5%. HNN's figures exclude accessories, rugs and décor, which understates World Market, HomeGoods and At Home.
- **Variants:**
  - **One row per parent** (each ranked company once, plus StorageCafe's separately ranked banners), walked to 30: adds AFW, Living Spaces, Lovesac, Havertys, Frontgate, Room & Board, Ethan Allen, Design Within Reach, Slumberland, Mor, Farmer's, Bassett and Levin (HNN #50, not checked). PE 2 / 30 (6.7%); owner not found 4, not checked 1.
  - **DTC leads counted** (the screen's The Shade Store and Visual Comfort, both Leonard Green "Status: Current", and Brooklinen, Freeman Spogli, no status). Leonard Green's portfolio page (screen page 058): "The Shade Store is a leading omni-channel provider of custom window treatments in the United States." and "Visual Comfort is a leading provider of decorative and functional lighting as well as ceiling fan products primarily serving the residential end-market." Counted: 5 / 30 (16.7%) if they replace the walk's last three rows (Joybird, Arhaus, Crate & Barrel); 5 / 33 (15.2%) if added.
  - **Frontgate's owner:** if QVC Group's successor owner of Cornerstone Brands is PE, the one-row-per-parent variant reads 3 / 30 (10.0%); the banner walk does not reach those rows.
- **Sources disagree:** none.

**Affiliate income:**
- **Brand-direct programs confirmed: 0.**
- **PE rows (2):** World Market: no affiliate link in the homepage footer; network listings (CJ, FlexOffers, Sovrn) seen in search only. Bob's: homepage is script-only; nothing in search.
- **Non-PE rows checked (2):** Wayfair and Ashley: no affiliate link in homepage HTML. Network listings seen in search only for Wayfair (FlexOffers), La-Z-Boy (FlexOffers, Sovrn), Rooms To Go (Awin) and Crate & Barrel (Impact).
- **Not checked: 24 rows.** Most big home retailers here run affiliate programs through networks rather than a page on their own site, as far as the search results show.

## Firms named
Every investment firm named as an owner or 5%+ holder, as the sources name it:
- **Bain Capital** (Bob's): "Bain Capital"
- **Kingswood Capital Management** (World Market): "Kingswood Capital Management, LP (together with its affiliates, “Kingswood”)"
- **At Home's lenders:** "Redwood Capital Management, LLC", "Farallon Capital Management, L.L.C.", "Anchorage Capital Advisors, L.P."; former owner Hellman & Friedman (equity cancelled)
- **Freeman Spogli** (Arhaus, former; Brooklinen, lead)
- **Leonard Green & Partners** (The Shade Store, Visual Comfort; leads, not rows)
- 5%+ holders of public rows: FMR LLC (Wayfair, RH, Lovesac); Capital World Investors (Wayfair); The Vanguard Group (Wayfair, TJX, LZB, Havertys, Bassett); BlackRock, Inc. (WSM, TJX, RH, LZB, Lovesac, MillerKnoll, Havertys, Bassett); Aristotle Capital Management, Blackhill Capital, State Street (WSM); Citadel Advisors, Susquehanna broker-dealers (RH); Dimensional Fund Advisors (LZB, MillerKnoll, Havertys, Bassett); Anson Funds, Hood River Capital Management, Springhouse Capital, Arrowstreet Capital, Senvest Management, Kanen Wealth Management (Lovesac); Pzena Investment Management, The Burton Partnership, Villa Clare Partners (Havertys); GAMCO Investors / Gabelli Funds, Aegis Financial Corporation, Auto Services Company, Inc. (Bassett); DGB Investment, Inc. (Ethan Allen).
- Not investment firms: Otto Group and the Michael Otto Foundation (Crate & Barrel), Inter IKEA Foundation, Berkshire Hathaway, the Wanek family (Ashley; named in StorageCafe's history and the screen, not in an ownership quote), the Goldberg family (Raymour & Flanigan; per the screen), the Jabs family (AFW), the Larson family (Slumberland).

## Form ADV results
From the November 2026 SEC files (`ia110226-registered`, `ia11022026-exempt`):

| Firm (role) | Adviser entity | CRD | Type | Any PE Funds | PE funds |
|---|---|---|---|---|---|
| Bain Capital (Bob's) | Bain Capital Private Equity, LP | 145653 | RIA | Y | 36 |
| Kingswood (World Market) | Kingswood Capital Management, L.P. | 304649 | RIA | Y | 15 |
| Leonard Green (DTC leads) | Leonard Green & Partners, L.P. | 158164 | RIA | Y | 107 |
| Freeman Spogli (Arhaus former; Brooklinen lead) | Freeman Spogli Management Co., L.P. | 156819 | RIA | Y | 7 |
| Summit Partners (Brooklinen, trade press only) | Summit Partners, L.P. | 135271 | RIA | Y | 87 |
| **Fidelity (FMR LLC's 13Gs)** | Fidelity Management & Research Company LLC | 108281 | RIA | **Y** | 1 |
| **Hood River (Lovesac 13G)** | Hood River Capital Management LLC | 166089 | RIA | **Y** | 3 |
| Redwood (At Home) | Redwood Capital Management, LLC | 158243 | RIA | N | |
| Farallon (At Home) | Farallon Capital Management, L.L.C. | 107322 | RIA | N | |
| Anchorage (At Home) | Anchorage Capital Group, L.L.C.; Anchorage Capital Advisors, L.P. | 135657; 328998 | RIA | N | |
| Capital World Investors (Wayfair) | Capital Research and Management Company | 110885 | RIA | N | |
| Citadel (RH) | Citadel Advisors LLC | 148826 | RIA | N | |
| Aristotle (WSM) | Aristotle Capital Management, LLC | 109876 | RIA | N | |
| Blackhill (WSM) | Blackhill Capital, Inc | 105208 | RIA | N | |
| Dimensional (several) | Dimensional Fund Advisors LP | 106482 | RIA | N | |
| BlackRock (several) | BlackRock Fund Advisors; BlackRock Advisors, LLC | 105247; 106614 | RIA | N | |
| Vanguard (several) | The Vanguard Group, Inc.; Vanguard Portfolio Management, LLC | 105958; 338003 | RIA | N | |
| Pzena (Havertys) | Pzena Investment Management LLC | 106847 | RIA | N | |
| Anson Funds (Lovesac) | Anson Funds Management LP; Anson Advisors Inc. | 125109; 167637 | RIA; ERA | N | |
| Springhouse (Lovesac) | Springhouse Capital Management, LP | 163080 | RIA | N | |
| Senvest (Lovesac) | Senvest Management, LLC | 137312 | RIA | N | |
| Kanen (Lovesac) | Kanen Wealth Management LLC | 282746 | RIA | N | |
| Arrowstreet (Lovesac) | Arrowstreet Capital, Limited Partnership | 111298 | RIA | N | |
| Gabelli / GAMCO (Bassett) | Gabelli Funds, LLC; GAMCO Asset Management Inc.; Gabelli & Company Investment Advisers | 104949; 104950; 137024 | RIA | N | |
| Aegis (Bassett) | Aegis Financial Corporation | 111587 | RIA | N | |

Not in either file: The Burton Partnership (Havertys), DGB Investment, Inc. (Ethan Allen), State Street (searched as "State Street Global Advisors"; it files 13Gs under 13d-1(b) in any case), Susquehanna's entities, Otto Group. **The two `Y` holders don't create stakes:** FMR LLC's 13Gs on Wayfair (filed 2026-11-05) and RH (2024-11-12) and Hood River's on Lovesac (2026-02-17) are all filed under Rule 13d-1(b).

## BDC names
From the SEC BDC data sets 2026_07 to 2026_10 (`Investment, Identifier Axis`), searched for every row and next-row name plus the DTC leads:
- **RH:** Apollo Debt Solutions BDC, "Restoration Hardware, Inc.", Household Durables, first-lien term loans (two rows, S+261 and S+335), period 2026-06-30. Ties to RH by name.
- **Next row:** MillerKnoll, Inc. (Design Within Reach's parent): Apollo Debt Solutions BDC, Barings Private Credit Corp, Blackstone Private Credit Fund (via Emerald JV LP), Steele Creek Capital Corp; first-lien term loans.
- **DTC leads (not rows):** "The Shade Store, LLC" (Blue Owl Capital Corp, Blue Owl Capital Corp II, Blue Owl Credit Income Corp; first lien); "Visual Comfort VC GB Holdings I Corp" (Apollo Debt Solutions BDC; first lien).
- **No hit:** Ashley, Wayfair, Rooms To Go, Williams-Sonoma or its brands, IKEA, Bob's, Raymour, La-Z-Boy or Joybird, Arhaus, Crate & Barrel, AFW, HomeGoods or TJX, At Home, World Market or Cost Plus, Living Spaces, Lovesac, Havertys, Room & Board, Ethan Allen, Slumberland, Mor, Bassett, Brooklinen, Kirkland's, Frontgate or Cornerstone.
- False matches set aside: "RH Buyer, Inc." (aerospace and defense), "Choice Health at Home", "Kindred at Home".

## Rows resting on documents older than 18 months
- **PE rows: none.** Bob's rests on its FY2025 10-K (2026). World Market's acquisition release is from 2021-01-19, but Kingswood's portfolio page, seen 2026-11-18 with the tile marked current, confirms it.
- Non-PE rows with an older document: RH's FMR 13G/A (2024-11-12) is the newest FMR filing on RH; the 2026 proxy restates FMR at 14.7%. Ethan Allen's newest DEF 14A in the filing list is 2025-09-26 (a next row; its 2026 13D filings are recent).

## Surprises
- **QVC Group deregistered in 2026.** Its SEC record now reads "Old QVC Group, Inc." with no ticker, and it filed Form 15-12G on 2026-08-21. HNN (published in June) still lists it as the publicly held owner of Frontgate, Ballard Designs and Grandin Road. Who owns those three names now is unread.
- **Mor Furniture for Less** says it "was acquired by one of our suppliers in 2020" without naming the supplier.
- **Fidelity's main adviser reports a PE fund on Form ADV** (Y, 1). Under the ADV rule that makes Fidelity a PE firm, so every FMR 13G needs its box checked; here all were 13d-1(b).
- **Hood River Capital Management** (Y, 3 PE funds) holds 6.76% of Lovesac, but as a 13d-1(b) adviser.
- **Ethan Allen lost a proxy fight in November 2026:** DGB Investment (Doug Bergeron) holds 4.2% by 13D and won three board seats on 2026-11-06. It is not a Form ADV adviser.
- **Bed Bath & Beyond, Inc.** now owns Kirkland's and The Container Store (HNN #53).
- **Newsweek's ranking site and Farmer's Home Furniture disallow ClaudeBot.**
- **The StorageCafe challenge cleared by itself** in the honest browser.
- **The Shade Store and Visual Comfort, both Leonard Green and both outside every ranking found, borrow from BDCs.**

## Open questions for the developer (numbers only; nothing decided)
1. **Banner ordering:** with banners entered at the parent's rank (this list), 2 / 30 (6.7%). One row per parent gives 2 / 30 (6.7%) with 4 not found. By parent within this list, 2 / 15 (13.3%).
2. **DTC gap:** no free blind ranking measures DTC home brands. Counting the screen's three DTC PE leads gives 5 / 30 (16.7%) in place of the walk's last three rows, or 5 / 33 (15.2%) on top.
3. **Multi-state test:** it drops Star and Homemakers (Berkshire, #12) and City Furniture (#23). Keeping them adds Star and Homemakers ahead of the cut, which pushes out Arhaus and Crate & Barrel (City Furniture falls past the cut): still 2 / 30.
4. **StorageCafe guarantee:** the 8 décor rows are in regardless of HNN rank. Without the guarantee, HomeGoods and Homesense (TJX, #24), At Home (#30) and World Market (#49) fall out and the walk ends at American Furniture Warehouse (#20): 1 / 30 (3.3%).
5. **Frontgate, Ballard Designs, Grandin Road:** 3 next rows with no current owner found after QVC Group's deregistration; if PE, the one-row-per-parent variant reads 3 / 30 (10.0%).
6. **Rooms To Go:** owner not stated (counted 0 not found here; 1 / 30 under the screen's convention).
7. **StorageCafe browser retry:** 1 page fetched after a 403 challenge cleared in the browser; if that breaks the 403 rule, the décor leg needs another source and rows 27-30 lose their guarantee (see 4).

## Cost
- **Requests:** 51 logged page requests (50 curl, 1 Playwright): 25 SEC (17 www.sec.gov, 8 data.sec.gov), 26 to 20 other hosts. Status mix: 45 × 200, 4 × 404, 1 × 301, 1 × 403 (the StorageCafe challenge). 27 robots.txt reads (26 hosts plus one redirect target). 16 web searches (9 for the ranking, 7 for owners and affiliates). Pages reused from the screen without refetching: about 25.
- **Tokens:** roughly 250k (under the 340k budget).
- **Time:** about 35 minutes of logged fetching (23:55Z to 00:12Z page requests, plus searches before and the write-up after); under an hour in all.

## Quote check
- **Method:** `scripts/fu-home/qcheck.py` string-matches every quote in `scripts/fu-home/quotes.tsv` (the quotes used on the Ranking, Evidence and Next-rows lines, each tagged with its saved page) against that page's saved text. Before matching it applies NFKC, collapses whitespace, normalizes curly quotes and dashes, and drops zero-width characters.
- **Result: 79 of 79 found.** A second script confirmed that every quote in the file appears in this report word for word (after the same normalization).
- **Negative control:** the same 79 quotes, each with one word altered, all failed (0 of 79 found).
- **Not covered:** values read from tables or form fields (proxy percentages, HNN sales and store counts, 13D and 13G cover percentages, checkbox states read from `alt` text, Kingswood's `data-status` attribute, the SEC submissions record's tickers and former names, BDC data-set fields).
