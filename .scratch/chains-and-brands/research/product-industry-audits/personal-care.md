# Product industry audit: Personal care

Ticket: [91-research-product-industry-audits](../../issues/91-research-product-industry-audits.md) · Worker report, researched 2026-11-17 (fetches logged 22:59–23:28 UTC) · Scope: soap, body care, deodorant, shaving and similar (the earlier screen's section 3); makeup, skin care sold as beauty, hair care and oral care left out. Ownership facts come from primary sources only; YouGov and Happi (Circana tables) supply the ranking only.

**Short answer**

| | Personal care (N = 30 brand rows, composite ranking) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **4 / 30 (13.3%)**, all PE-owned, none minority: Suave (Yellow Wood Partners, through Evermark, since 2023), Blue Lizard (Hildred Capital, through Crown Laboratories, since 2017), Supergoop! (Blackstone Growth, majority, since late 2021) and Certain Dri (Charlesbank, through Bridges Consumer Healthcare). Each firm's Form ADV says `Any PE Funds = Y`. |
| Owner not found | **2 / 30 (6.7%)**: Degree (every primary source tried was blocked), Sun Bum (SC Johnson's 2019 release announces a signed agreement only; no closing found). Another 2 rows name a private company but no owner (Lume, under Mammoth Brands; eos), and 1 row's owner type is not confirmed (Mitchum: Revlon, majority-owned by unnamed former lenders). |
| Brand-direct affiliate programs | **3 found on brand pages**: Lume (Impact), Native (P&G's creator affiliate terms) and Supergoop! (a college-ambassador program with a "Personal affiliate link"). **Split: PE 1 (Supergoop!, restricted to ambassadors), non-PE 2.** Network listings only: 2 (Dr. Squatch, Bath & Body Works). Not checked because the site blocked the bot: 6 rows. |
| BDC overlap | **2 rows tie by name**: Supergoop! ("Supergoop, LLC", BlackRock Direct Lending Corp.) and Suave ("Suave Silk Holdings III Corp." in 5 Apollo-managed BDCs, plus common equity in "Suave Silk Holdings I Corp." at MidCap Financial Investment Corp.). **Near match, not counted:** Certain Dri's owner is "Bridges Consumer Healthcare, LLC"; Antares and Nuveen Churchill BDCs lend to "Bridges Consumer Healthcare Intermediate LLC". |

- **The bar:** 4 of 30 clears the 3-of-30 (10%) launch bar, with one row to spare. Two of the four PE rows come from the sun care table and one from the composite's last tier (see Open questions: two scope choices each move the count to 3 of 30, which is exactly 10%).
- **The top of the list carries no PE.** Rows 1–11 (YouGov's consideration top 25) are all public companies: Unilever, P&G, Bath & Body Works, Henkel, Sanofi, Kao and Colgate-Palmolive. PE sits in a mass brand that Unilever sold (Suave), in sun care (Blue Lizard, Supergoop!) and in an OTC clinical antiperspirant (Certain Dri).
- **Biggest finding:** Suave in the US belongs to Yellow Wood Partners, not Unilever. Unilever sold the North American business in 2023, and on 2026-01-20 Yellow Wood merged it with Elida Beauty into Evermark, LLC; suave.com's footer now reads "© 2026 Evermark, LLC". Suave sits 10th in Circana's deodorant table.
- **Formerly PE-owned:** Dr. Squatch went from Summit Partners (ADV `Y`) to Unilever on 2025-09-02 (98.7%). Third Point (ADV `Y`) held Bath & Body Works on a 13D until it fell to 3.65% in October 2024. Neither counts today.

## How this was sourced (read first)

- **Ranking:** a composite of three ownership-blind sources (YouGov BrandIndex consideration, YouGov Ratings popularity, and Circana sales tables printed by Happi), stated exactly under "Ranking". No PE portfolio page and none of the scan's long-tail PE brands was used to pick rows. Of those long-tail brands (DUDE Wipes, Every Man Jack and others), none is in any of the sources.
- **Ownership facts:** SEC filings (P&G, Colgate, Edgewell and Bath & Body Works 10-Ks, Unilever and Sanofi 20-Fs, Kenvue's 10-K, Kimberly-Clark's 8-K exhibit, Revlon 8-K exhibit, Schedule 13D/13G XML), sponsor releases and portfolio pages (Yellow Wood, Hildred, Blackstone, Charlesbank), company pages (footers, terms, privacy policies, about pages, investor pages of Henkel, Kao and Beiersdorf) and one company release on PR Newswire (SC Johnson).
- **SEC access:** 46 requests to www.sec.gov, data.sec.gov and efts.sec.gov (robots reads included), all with the user agent `EvidenceEngine ownership-research bot (product industry audit)`, no contact detail, at least 1.1 s apart. 43 returned 200; data.sec.gov's and efts.sec.gov's robots.txt returned 404 and 403 (read as no restrictions), and one full-text search URL returned 500 (not retried in that form).
- **Robots:**
  - robots.txt was read before the first request to each of 64 hosts, including every redirect target (www.jergens.com → us.jergens.com, www.secret.com → secret.com, www.yellowwoodpartners.com, nativecos.com → www., bluelizardsunscreen.com, certaindri.com, gillette.com, oldspice.com, thrivecap.com).
  - gillette.com and oldspice.com set `Crawl-delay: 10`; requests to each were spaced 10–11 s.
  - amazon.com disallows ClaudeBot, Claude-User and Claude-SearchBot, so its best-seller pages were never fetched (robots.txt only).
  - 12 hosts answered robots.txt with 403 or 404 (Akamai hosts of Unilever and Kenvue brands, globenewswire.com, a CloudFront host, data.sec.gov, efts.sec.gov, yellowwoodpartners.com); per the rules a 4xx means no restrictions.
  - suave.com's robots.txt carries text addressed to AI agents; it was treated as content.
- **Blocked or failed:**
  - Akamai "Access Denied" (403, not a challenge page, no retry): unilever.com, unileverusa.com, vaseline.com, degreedeodorant.com, axe.com, johnsonsbaby.com, lubriderm.com, globenewswire.com.
  - Cloudflare "Just a moment" on two blackstone.com pages (the 2021 Supergoop! release and the Growth page). Not retried in the browser, because Blackstone's 2022 release and a current people page gave the facts.
  - bathandbodyworks.com: PerimeterX captcha (307). One Playwright visit with the bot's user agent and no clicks did not clear it, so the site counts as blocked. (Index line 130 records a browser that failed to launch before any request was made.)
  - scjohnson.com returned 429; not retried.
  - yougov.com's "Load more" data sits behind an internal API host; that request was refused before it was sent, so only the 20 server-rendered rows per YouGov Ratings list were used.
  - Dead or wrong pages: drsquatch.com/pages/affiliates (404), thrivecap.com/companies (404), a guessed YouGov API path (404), a Beiersdorf Aquaphor path (redirected to a 404 page). eos.com belongs to EOS Data Analytics, not the lip-balm brand; the brand's site is evolutionofsmooth.com.
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist and Private Equity Vet (none came up); PitchBook, Preqin, Crunchbase, Tracxn and privateequityinfo results that came up in searches; amazon.com pages.
- **Leads only, never cited:** trade press on deals (Beauty Matter, Retail Dive, WWD, Cosmetics Business, Happi news items), deal directories (mergr, privsource), affiliate directories (Lasso, FlexOffers, Commissiondex, JEBCommerce) and content-farm ownership pages.
- **Owner kinds are research notes, not engine classifications.** "PE-owned" means control or a PE owner with no stated stake. "Private, owner not stated" means a primary source names the company but not who owns it. Counts are by brand row.
- **Quotes:** copied from saved page text (tags stripped, whitespace collapsed). Two pages (blackstone.com) were re-extracted with lxml after the first extractor stopped early. Field-style quotes (13G XML fields, YouGov list rows, Circana table rows, portfolio tiles) are marked as such.

## Ranking

**No free brand-level ranking of US personal care reaches 30.** Checked and not used:
- YouGov Ratings' "Load more" rows (behind an internal API; see above) and its crossBreak (men, women, generation) pages, which robots.txt disallows.
- Amazon best sellers (robots.txt disallows Claude agents).
- Similarweb's free Beauty & Personal Care table: 5 rows, sorted by gain, mostly skin care.
- Happi's other Circana tables: the 2024 soap article prints its table as an image, and the 2026 deodorant article gives category totals only.
- YouGov's 2025 personal care report (download-gated) and its women-by-generation article (2026; no personal-care name outside the consideration top 25).

**Composite used (row number = tier order, then the source's own order; brands already listed are skipped):**

(a) **Rows 1–11: YouGov BrandIndex, "U.S. personal care and beauty brand rankings 2026"** (article, 2026-10-20, https://yougov.com/en-us/articles/55760-us-personal-care-rankings-2026; data from its Datawrapper CSV https://datawrapper.dwcdn.net/rN7qX/4/dataset.csv). Measure: share of US adults who would consider the brand next time. "Dove (skin care) ranks first in YouGov’s U.S. personal care and beauty brand rankings 2026, with 48.9% of U.S. adults saying they would consider the brand the next time they are in the market." Every personal-care row of the top 25 is taken, in rank order: Dove (skin care) #1, Vaseline #5, Gillette #8, Bath & Body Works #10, Dove Men + Care #14, Secret #15, Dial #17, Gold Bond #20, Old Spice #22, Jergens #24, SoftSoap #25. Split as in the earlier screen: oral care (Colgate #2, Crest #4, Listerine #6) is left out; hair care, makeup and face skin care (Dove hair care, Neutrogena, CeraVe, Olay, Head & Shoulders, Nivea, Pantene, Burt's Bees, Aveeno, Maybelline, L'Oréal Paris) go to the beauty audit.

(b) **Rows 12–17: Circana deodorant sales, regular segment, top 10 brands by dollar sales,** printed by Happi, "Wellness-Inspired Ingredients & Whole-Body Coverage Drive Deodorant Sales" (2025-02-01, https://www.happi.com/wellness-inspired-ingredients-whole-body-coverage-drive-deodorant-sales/): "Total US multi-outlets with c-stores, inclusive of grocery, drug, mass market, convenience, military and select club and dollar retailers for the 52 weeks ending Dec. 1, 2024." Table order: Dove $1,150,581,728; Old Spice $946,668,764; Degree $718,374,852; Secret $658,766,268; Native $379,148,471; Gillette $192,259,520; Axe $155,564,453; Lume $150,006,773; Dr Squatch $95,409,399; Suave $93,970,113. New rows: Degree, Native, Axe, Lume, Dr Squatch, Suave. (Happi's February 2026 deodorant article prints category totals only, so this is the latest brand table found.)

(c) **Rows 18–24: Circana sun care sales, "Suntan Lotion & Oil" segment, all branded rows,** printed by Happi, "Neutrogena’s First BEMT Formulas Hit the US Market" (2026-09-17, https://www.happi.com/exclusives/neutrogenas-first-bemt-formulas-hit-the-us-market/): "According to Circana, sales of suntan products in US multi-outlets rose 7.5% to nearly $2.8 billion for the 52-weeks ended Sept. 6, 2026." Rows: Neutrogena $378,460,186 (beauty audit); Banana Boat $273,882,418; Sun Bum $272,124,109; Private Label $194,969,696 (not a brand); Hawaiian Tropic $193,528,002; Coppertone $147,446,891; La Roche Posay $143,996,377 (beauty audit); Blue Lizard $124,682,631; Elta MD $122,004,179; Supergoop $108,660,727. The table's separate "Sunscreen/Insect Repellent" segment (Bullfrog, $4,225) is not used.

(d) **Rows 25–27: YouGov Ratings, "The most popular skincare & cosmetics brands" (Q3 2026),** the 20 rows the page serves (https://yougov.com/en-us/ratings/skincare-cosmetics-brands): "popularity is the % of people who have a positive opinion of a skincare & cosmetics brand." Personal-care rows not already listed: "7Johnson's Baby90%59%", "10Aquaphor77%58%", "20Lubriderm78%53%" (field rows: rank, name, fame, popularity). The fame-sorted top 20 (`?sortBy=fame`) and the household & personal care lists (popularity and fame) add no new personal-care name.

(e) **Row 28: YouGov's "Top 10 biggest improvers" in the same 2026 article** (https://yougov.com/en-us/articles/55760-us-personal-care-rankings-2026; CSV https://datawrapper.dwcdn.net/m3LUZ/4/dataset.csv): "3,eos,8.7,6.0,2.7" (rank, brand, 2026 %, 2025 %, change). Its other personal-care rows (Vaseline, Dove Men + Care, Dove skin care, Old Spice, Native, Aquaphor, Bath & Body Works) are already listed.

(f) **Rows 29–30: the same Circana deodorant table's "Clinical Deodorant" segment,** brands not already listed, in table order: Certain Dri $11,059,554; Mitchum $167,463.

- **Limits.** Consideration and popularity are not sales. Circana covers multi-outlet retail and misses specialty stores, DTC and Amazon, which undercounts Bath & Body Works, Dr. Squatch and Lume. Shaving and soap have no tier of their own: Gillette is the only shaving brand, and Dove, Dial and Softsoap the only soap brands. Tiers (b) and (f) date from 2024 data; tier (c) is September 2026.
- **The composite is exactly 30 rows.** Every brand any tier names, inside the scope rules, is in. No row was added from outside the sources.

| # | Brand (source, value) | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dove (skin care) (YG #1, 48.9%) | Unilever | public company | none (no 13D since 2018) | not checked | UL (NYSE ADS) | brand of a consumer-products company | none found (dove.com) | PC1 |
| 2 | Vaseline (YG #5, 38.0%) | Unilever | public company | none | not checked | UL | brand of a consumer-products company | not checked (site 403) | PC2 |
| 3 | Gillette (YG #8, 27.8%; Circana deo #6) | Procter & Gamble | public company | none (13Gs 13d-1(b) only) | not checked | PG | brand of a consumer-products company | none found | PC3 |
| 4 | Bath & Body Works (YG #10, 26.4%) | Bath & Body Works, Inc. | public company | none current (Third Point 13D ended 2024-10-23 at 3.65%) | not applicable | BBWI | own stores (1,927 in US and Canada) plus e-commerce | network listing only (Rakuten per directories); site blocked | PC4 |
| 5 | Dove Men+Care (YG #14, 23.6%) | Unilever | public company | none | not checked | UL | brand of a consumer-products company | none found (dove.com) | PC5 |
| 6 | Secret (YG #15, 23.2%; Circana deo #4) | Procter & Gamble | public company | none | not checked | PG | brand of a consumer-products company | none found | PC6 |
| 7 | Dial (YG #17, 23.0%) | Henkel (Henkel Corporation in the US) | public company, family pool 61.85% of ordinary shares | none | not checked | Henkel (German exchanges) | brand of a consumer-products company | none found | PC7 |
| 8 | Gold Bond (YG #20, 21.7%) | Gold Bond Co LLC, retained by Sanofi | public company | none (L'Oréal 7.27%, a public company) | not checked | SNY (Nasdaq ADS) | brand of a pharma group | none found | PC8 |
| 9 | Old Spice (YG #22, 21.1%; Circana deo #2) | Procter & Gamble | public company | none | not checked | PG | brand of a consumer-products company | none found | PC9 |
| 10 | Jergens (YG #24, 19.9%) | Kao Corporation (Andrew Jergens Company acquired 1988) | public company (holders not checked) | none found | 1988 | 4452 (Tokyo) | brand of a consumer-products company | none found | PC10 |
| 11 | Softsoap (YG #25, 19.5%) | Colgate-Palmolive | public company | none (13Gs 13d-1(b) only) | not checked | CL | brand of a consumer-products company | none found | PC11 |
| 12 | Degree (Circana deo #3, $718.4M) | not found (brand site 403; Unilever's 20-F names Rexona, not Degree) | not found (trade press: Unilever; not cited) | none found | not found | — | not found | not checked (site 403) | PC12 |
| 13 | Native (Circana deo #5, $379.1M) | Procter & Gamble | public company | none | not checked | PG | DTC plus retail | **yes, brand-direct**: P&G creator affiliate terms on nativecos.com | PC13 |
| 14 | Axe (Circana deo #7, $155.6M) | Unilever (a Personal Care "Power Brand") | public company | none | not checked | UL | brand of a consumer-products company | not checked (site 403) | PC14 |
| 15 | Lume (Circana deo #8, $150.0M) | Lume Deodorant, LLC, acquired 2021 by Mammoth Brands (Harry's); Mammoth's owners not stated | private, owner not stated | none confirmed (leads: Mammoth's reported VC investors, several with ADV `Y`) | 2021 (Mammoth) | — | DTC plus retail | **yes, brand-direct**: lumedeodorant.com/affiliate-program (Impact) | PC15 |
| 16 | Dr. Squatch (Circana deo #9, $95.4M) | Unilever (98.7% acquired 2025-09-02) | public company (formerly PE-owned: Summit Partners) | none current | 2025-09-02 | UL | DTC plus retail | network listing only (Pepperjam per JEBCommerce, FlexOffers); /pages/affiliates 404 | PC16 |
| 17 | Suave (Circana deo #10, $94.0M) | Evermark, LLC (Suave Brands Company merged with Elida Beauty, 2026-01-20), a Yellow Wood Partners portfolio company | **PE-owned** (no stated stake) | Yellow Wood Partners | 2023 (Unilever's disposal; Evermark 2026-01-20) | — | brand of a consumer-products company | none found | PC17 |
| 18 | Banana Boat (sun $273.9M) | Edgewell Personal Care | public company | none (13Gs 13d-1(b) only) | 2007 (Playtex) | EPC | brand of a consumer-products company | none found | PC18 |
| 19 | Sun Bum (sun $272.1M) | not found (footer: Sun Bum LLC; SC Johnson signed to acquire it in 2019, closing not found) | not found (lead: SC Johnson, "a family company") | none found | not found | — | brand of a manufacturer | none found (ambassador page has no commission) | PC19 |
| 20 | Hawaiian Tropic (sun $193.5M) | Edgewell Personal Care | public company | none | 2007 (Playtex) | EPC | brand of a consumer-products company | none found | PC20 |
| 21 | Coppertone (sun $147.4M) | Beiersdorf | public company; maxingvest group holds 54.4% (kind not stated) | none | not checked | Beiersdorf (Frankfurt) | brand of a consumer-products company | none found | PC21 |
| 22 | Blue Lizard (sun $124.7M) | Crown Laboratories Inc., "a Revance Company"; Hildred Capital portfolio company | **PE-owned** (no stated stake; Hildred describes "control-oriented investments") | Hildred Capital | 2017 (Hildred's investment year) | — | brand of a skincare manufacturer | none found | PC22 |
| 23 | EltaMD (sun $122.0M) | Colgate-Palmolive (CP Skin Health Group, Inc.) | public company | none | not checked | CL | professional-channel skin health brand | none found | PC23 |
| 24 | Supergoop! (sun $108.7M) | Supergoop!; majority held by funds managed by Blackstone Growth | **PE-owned** (majority stated) | Blackstone (Blackstone Growth) | late 2021 | — | DTC plus beauty retail | **yes, brand-direct, restricted**: college ambassadors get a "Personal affiliate link" | PC24 |
| 25 | Johnson's Baby (YG Ratings #7) | Kenvue, acquired by Kimberly-Clark 2026-11-02 | public company | none (13Gs 13d-1(b) only) | 2026-11-02 (K-C) | KMB | brand of a consumer-products company | not checked (site 403) | PC25 |
| 26 | Aquaphor (YG Ratings #10) | Beiersdorf (Derma category, with Eucerin) | public company; maxingvest 54.4% | none | not checked | Beiersdorf (Frankfurt) | brand of a consumer-products company | none found (raw HTML; footer is script-rendered) | PC26 |
| 27 | Lubriderm (YG Ratings #20) | Kenvue → Kimberly-Clark | public company | none | 2026-11-02 (K-C) | KMB | brand of a consumer-products company | not checked (site 403) | PC27 |
| 28 | eos (YG improvers #3) | eos Products, LLC; owner not stated | private, owner not stated | none found | not found | — | brand of a consumer-products company | none found (ambassador program pays coins, not commission) | PC28 |
| 29 | Certain Dri (Circana clinical deo, $11.1M) | Bridges Consumer Healthcare, LLC (trademark owner), a Charlesbank "Current" investment | **PE-owned** (no stated stake) | Charlesbank Capital Partners | 2020 (Charlesbank's investment year in Bridges) | — | OTC brand within a consumer-health platform | none found | PC29 |
| 30 | Mitchum (Circana clinical deo, $167K) | Revlon Consumer Products LLC; Revlon majority-owned by its former lenders (not named) | owner type not confirmed | none confirmed (lenders named only in trade press; one has ADV `Y`) | 2023-05 (lender ownership) | — | brand of a beauty company | none found | PC30 |

### Evidence
- **PC1 Dove (skin care)**
  - Owner: "This Desire at Scale approach is being led by brands like Dove and Vaseline, both of which grew strongly in 2025." — [Unilever 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Listing: "Unilever’s shares are also traded on the New York Stock Exchange (UL) in the form of American Depositary Shares" — [same 20-F](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Footer: "This website is directed only to U.S. consumers for products and services of Unilever United States." — [Dove US home page, accessed 2026-11-17](https://www.dove.com/us/en/home.html)
  - 5% holders: Unilever's EDGAR list shows its last third-party 13D/A on 2018-12-14 (the earlier screen identified the filer as the Leverhulme Trust); its only 2026 Schedule 13G (2026-02-10) is one Unilever filed on another issuer ("Rule 13d-1(d)", "UNILEVER PLC", "19.85"). [submissions JSON](https://data.sec.gov/submissions/CIK0000217410.json); [13G XML](https://www.sec.gov/Archives/edgar/data/217410/000110465926012464/primary_doc.xml)
  - Affiliate: none found in dove.com's links.
  - BDC names: "Unilever", "Conopco", "Dove"
- **PC2 Vaseline**
  - Owner: the "Dove and Vaseline" quote in PC1 (Unilever 20-F 2025).
  - Affiliate: not checked; vaseline.com returned Akamai "Access Denied" (403).
  - BDC names: "Unilever", "Vaseline"
- **PC3 Gillette**
  - Owner: "Our global blades and razors market share is more than 60%, primarily behind our Gillette and Venus brands." — [P&G 10-K FY2026](https://www.sec.gov/Archives/edgar/data/80424/000008042426000103/pg-20260630.htm)
  - Listing: "P&G trades on the New York Stock Exchange under the stock symbol PG." — [same 10-K](https://www.sec.gov/Archives/edgar/data/80424/000008042426000103/pg-20260630.htm)
  - Footer: "© 2026 Procter & Gamble" — [Gillette US home page, accessed 2026-11-17](https://gillette.com/)
  - 5% holders: no 13D in P&G's EDGAR list (back to 2022-08); its 2026 13Gs are Vanguard Capital Management ("Rule 13d-1(b)", "7.52") and The Vanguard Group (13G/A, "0"). [submissions JSON](https://data.sec.gov/submissions/CIK0000080424.json); [13G XML](https://www.sec.gov/Archives/edgar/data/80424/000210011926000950/primary_doc.xml)
  - Affiliate: none found on the home page.
  - BDC names: "Procter & Gamble", "Gillette"
- **PC4 Bath & Body Works**
  - Owner and listing: "Common Stock, $0.50 Par Value BBWI The New York Stock Exchange" — [BBWI 10-K FY2025](https://www.sec.gov/Archives/edgar/data/701985/000070198526000008/bbwi-20260131.htm)
  - Model: "in-store experiences at 1,927 company-operated stores in the United States of America (“U.S”) and Canada" — [same 10-K](https://www.sec.gov/Archives/edgar/data/701985/000070198526000008/bbwi-20260131.htm)
  - Former 13D holder: "The Shares represent approximately 3.65% of the Issuer’s Common Stock outstanding." and "the Reporting Persons ceased to be the beneficial owners of more than five percent of the shares of Common Stock" — [Third Point LLC, Schedule 13D/A No. 3, 2024-10-25](https://www.sec.gov/Archives/edgar/data/701985/000119312524244316/d874148dsc13da.htm). Third Point's ADV says `Y`, but the hop ended on 2024-10-23.
  - Current 13Gs, all "Rule 13d-1(b)": FMR LLC "13.3"; Vanguard Portfolio Management "7.53"; Vanguard Capital Management "5.32"; AQR "3.79"; The Vanguard Group "0". [13G XML (FMR)](https://www.sec.gov/Archives/edgar/data/701985/000031506626002692/primary_doc.xml)
  - Affiliate: network listing only (Rakuten, per directories; not opened). bathandbodyworks.com served a PerimeterX captcha to curl and to one Playwright visit.
  - BDC names: "Bath & Body Works", "L Brands"
- **PC5 Dove Men+Care**
  - Owner: "Introduced in the US in 2024 under Dove and Dove Men+Care" — [Unilever 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Affiliate: none found (shares dove.com).
- **PC6 Secret**
  - Owner: "Personal Care (Antiperspirants and Deodorants, Personal Cleansing) Native, Old Spice, Safeguard, Secret" — [P&G 10-K FY2026](https://www.sec.gov/Archives/edgar/data/80424/000008042426000103/pg-20260630.htm)
  - Footer: "© 2026 Procter & Gamble" — [Secret US home page, accessed 2026-11-17](https://secret.com/en-us)
  - Affiliate: none found.
- **PC7 Dial**
  - Owner: "©2026 Henkel Corporation. All rights reserved." — [Dial home page, accessed 2026-11-17](https://www.dialsoap.com/)
  - Holders: "61.85 percent of our ordinary shares (as of March 19, 2026) are held by members of the Henkel family share-pooling agreement." — [Henkel, Shares page](https://www.henkel.com/investors-and-analysts/shares)
  - Listing: "Henkel preferred shares have been publicly listed since 1985, the ordinary shares since 1996." — [same page](https://www.henkel.com/investors-and-analysts/shares)
  - Affiliate: none found.
  - BDC names: "Henkel Corporation", "Dial"
- **PC8 Gold Bond**
  - Owner: "In particular, Sanofi retained Gold Bond Co LLC and its business, and provided for the allocation of retained assets and liabilities accordingly." — [Sanofi 20-F 2025](https://www.sec.gov/Archives/edgar/data/1121404/000162828026008403/sny-20251231.htm)
  - Footer: "© 2026 Gold Bond® Co LLC, Inc. All rights reserved." — [Gold Bond home page, accessed 2026-11-17](https://www.goldbond.com/)
  - Holder: "as of December 31, 2025 L’Oréal held 7.27% of Sanofi’s share capital" — [Sanofi 20-F](https://www.sec.gov/Archives/edgar/data/1121404/000162828026008403/sny-20251231.htm). Listing (cover field): "SNY NASDAQ Global Select Market".
  - Notes: Gold Bond stayed with Sanofi when CD&R bought Opella (the earlier screen; re-checked here).
  - BDC names: "Gold Bond Co LLC", "Sanofi"
- **PC9 Old Spice**
  - Owner: P&G 10-K line in PC6.
  - Footer: "Copyright © Procter & Gamble" — [Old Spice home page, accessed 2026-11-17](https://oldspice.com/)
  - Affiliate: none found.
- **PC10 Jergens**
  - Owner: "1988 Kao acquires the Andrew Jergens Company (U.S.)." — [Kao, Company history](https://www.kao.com/global/en/corporate/history/company-history/)
  - Listing: "Kao's ticker code is 4452." — [Kao, IR FAQ](https://www.kao.com/global/en/investor-relations/faq/)
  - Site: "ALL YOUR FAVORITE KAO BRANDS, 1 EASY CHECKOUT" — [Jergens US home page, accessed 2026-11-17](https://us.jergens.com/)
  - 5% holders: not checked (Japanese filings).
  - Affiliate: none found.
  - BDC names: "Kao USA", "Kao Brands Company", "Andrew Jergens Company"
- **PC11 Softsoap**
  - Owner: "Irish Spring, Palmolive, Sanex and Softsoap shower gels" — [Colgate-Palmolive 10-K FY2025](https://www.sec.gov/Archives/edgar/data/21665/000002166526000006/cl-20251231.htm)
  - Listing: "Common Stock, $1.00 par value CL New York Stock Exchange" — [same 10-K](https://www.sec.gov/Archives/edgar/data/21665/000002166526000006/cl-20251231.htm)
  - Footer: "© 2026 Colgate-Palmolive Company. All rights reserved." — [Softsoap home page, accessed 2026-11-17](https://www.softsoap.com/en-us)
  - 5% holders: no 13D; 2026 13Gs: Vanguard Capital Management ("Rule 13d-1(b)", "7.52"), The Vanguard Group ("0"). [13G XML](https://www.sec.gov/Archives/edgar/data/21665/000210011926000347/primary_doc.xml)
  - Affiliate: none found.
- **PC12 Degree**
  - Owner: not found. degreedeodorant.com, unilever.com and unileverusa.com all returned Akamai "Access Denied". Unilever's 20-F lists "Rexona" (Degree's name outside the US) among its Power Brands but never names Degree; an EDGAR full-text search found no usable hit.
  - Notes: Happi's 2026 deodorant article calls Degree part of Unilever's portfolio (trade press; not cited). Counted as owner not found.
  - BDC names: "Degree"
- **PC13 Native**
  - Owner: P&G 10-K line in PC6 ("Native, Old Spice, Safeguard, Secret").
  - Footer: "Copyright © 2026, Native" — [Native home page, accessed 2026-11-17](https://www.nativecos.com/)
  - Affiliate: "Procter & Gamble (P&G) Affiliate Terms and Conditions for Creators — Native" and "(including that you may earn commission)" — [Native, Creators Terms and Conditions](https://www.nativecos.com/pages/creators-terms-and-conditions). Creators earn commission on approved platforms; counted as brand-direct.
  - BDC names: "Native Cos", "Native"
- **PC14 Axe**
  - Owner: "Our Power Brands: Axe Closeup Dove Lifebuoy Lux Pepsodent Rexona" (field text) — [Unilever 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Affiliate: not checked (axe.com 403).
- **PC15 Lume**
  - Owner: "© 2026 Lume Deodorant, LLC" — [Lume home page, accessed 2026-11-17](https://lumedeodorant.com/)
  - Parent: "In 2021, we acquired Lume — an OBGYN founded, deodorant brand that you can use anywhere on your body" — [Mammoth Brands home page, accessed 2026-11-17](https://www.mammothbrands.com/)
  - Parent's owners: not stated on the page. Trade directories and press (not cited) name Harry's venture and growth investors. Thrive Capital, Tiger Global, Alliance Consumer Growth and SurgoCap all report PE funds on Form ADV, but no page read shows any of them holding Mammoth today. The ACG portfolio page renders by script, and Thrive's /companies path returned 404.
  - Affiliate: "To join the Lume Affiliate Program, please sign up here." — [Lume, Affiliate Program](https://lumedeodorant.com/affiliate-program). The page sends applicants to Impact.
  - BDC names: "Lume Deodorant, LLC", "Mammoth Brands", "Harry's, Inc."
- **PC16 Dr. Squatch**
  - Owner: "On 2 September 2025, Unilever acquired 98.7% of the shares of Dr. Squatch, a US-based company specialising in natural personal care products." — [Unilever 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Footer: "DR. SQUATCH is a registered trademark of Dr. Squatch, LLC © 2026, Dr. Squatch, LLC All rights reserved." — [Dr. Squatch home page, accessed 2026-11-17](https://www.drsquatch.com/)
  - Former owner: Summit Partners (Unilever's 2025 release names it as seller; unilever.com is blocked, so it is not quoted). Summit Partners, L.P.'s ADV says `Y`. Formerly PE-owned; the 1.3% Unilever did not buy is unexplained.
  - Affiliate: network listing only (Pepperjam, per JEBCommerce's launch post; FlexOffers). /pages/affiliates returned 404.
  - BDC names: "Dr. Squatch, LLC"
- **PC17 Suave**
  - Owner: "© 2026 Evermark, LLC. All rights reserved." — [Suave home page, accessed 2026-11-17](https://www.suave.com/)
  - PE: "today announced that they have completed a merger to create Evermark, LLC" and "Both businesses are portfolio companies of Yellow Wood Partners ("Yellow Wood"), a leading consumer-focused private equity investment firm." — [Yellow Wood, news "Yellow Wood Partners Portfolio Companies Suave Brands and Elida Beauty Complete Merger to Create Evermark", 20 Jan. 2026](https://www.yellowwoodpartners.com/news-article/yellow-wood-partners-portfolio-companies-suave-brands-and-elida-beauty-complete-merger-to-create-evermark-a-leading-global-platform-of-personal-care-brands)
  - Since: "2023 includes a gain of €497 million related to the disposal of Suave." — [Unilever 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm). The 1 May 2023 date and the buyer's name are in Unilever's 2023 filings and release (not read; unilever.com blocked).
  - Stake: none stated; counts as control.
  - Territory: Unilever's 2023 release (lead, not read) says Unilever keeps Suave outside the US and Canada. That is a territorial split of the name, not a licence. The US row belongs to Evermark.
  - Affiliate: none found.
  - BDC names: "Suave Brands Company", "Evermark, LLC", "Suave Silk Holdings I Corp.", "Suave Silk Holdings III Corp." (both in the BDC data; see BDC names)
- **PC18 Banana Boat**
  - Owner: "We market sun care products under the Banana Boat and Hawaiian Tropic brands and believe these brands, on a combined basis, hold a leading market share position in the U.S. sun care category." — [Edgewell 10-K FY2026 (filed 2026-11-13)](https://www.sec.gov/Archives/edgar/data/1096752/000162828026073923/epc-20260930.htm)
  - Listing: "Common Stock, par value $0.01 per share EPC New York Stock Exchange" — [same 10-K](https://www.sec.gov/Archives/edgar/data/1096752/000162828026073923/epc-20260930.htm)
  - Footer: "© 2026 Edgewell. All Rights Reserved." — [Banana Boat home page, accessed 2026-11-17](https://www.bananaboat.com/)
  - 5% holders: no 13D. Every 2025–2026 13G is "Rule 13d-1(b)": Brandes Investment Partners "14.4"; American Century "11.7"; Rubric Capital Management "8.56"; Vanguard Portfolio Management "6.56"; Vanguard Capital Management "5.09"; Dimensional "4.0"; The Vanguard Group "0". Rubric's ADV says `Y`, but a 13d-1(b) filing never counts. [13G XML (Rubric)](https://www.sec.gov/Archives/edgar/data/1096752/000110465926062489/primary_doc.xml)
  - Affiliate: none found.
  - BDC names: "Edgewell Personal Care", "Banana Boat"
- **PC19 Sun Bum**
  - Owner: not found. The footer reads "© 2026 Sun Bum LLC. All Rights Reserved" — [Sun Bum home page, accessed 2026-11-17](https://www.sunbum.com/). The [privacy policy](https://www.sunbum.com/pages/privacy-policy) mentions "our parent company" without naming it.
  - Lead: "SC Johnson today announced that it has signed an agreement to acquire Sun Bum®" and "SC Johnson is a family company" — [SC Johnson release on PR Newswire, 14 Jun 2019](https://www.prnewswire.co.uk/news-releases/sc-johnson-signs-agreement-to-acquire-sun-bum-r--861457712.html). That is a signing, not a closing, and scjohnson.com returned 429. Under the pending-deal rule this stays unconfirmed. Either way it is not PE.
  - Affiliate: none found. /pages/ambassadors offers rewards points, not commission.
  - BDC names: "Sun Bum LLC"
- **PC20 Hawaiian Tropic**
  - Owner: Edgewell 10-K line in PC18; footer "© 2026 Edgewell. All Rights Reserved." — [Hawaiian Tropic home page, accessed 2026-11-17](https://www.hawaiiantropic.com/)
  - Affiliate: none found.
- **PC21 Coppertone**
  - Owner: "Copyright © Beiersdorf 2026" — [Coppertone home page, accessed 2026-11-17](https://www.coppertone.com/); "Coppertone was the first sun care brand launched in the U.S. and a pioneer from the start." — [Beiersdorf, Other iconic brands](https://www.beiersdorf.com/brands/other-iconic-brands)
  - Holders: "With a share of 54.4% maxingvest group holds the majority of issued shares." and "The remaining 36.4% of the shares are attributed to the free float." — [Beiersdorf, Shareholder structure](https://www.beiersdorf.com/investor-relations/shares/shareholder-structure). The page doesn't say what maxingvest is.
  - Affiliate: none found.
  - BDC names: "Beiersdorf", "Coppertone"
- **PC22 Blue Lizard**
  - Owner: "©Copyright 2026, Crown Laboratories Inc., a Revance Company" — [Blue Lizard home page, accessed 2026-11-17](https://bluelizardsunscreen.com/)
  - Trademark: "The "Crown" logo, PanOxyl and Blue Lizard are registered trademarks of Crown Laboratories, Inc." — [Hildred, news "Crown Laboratories Completes Acquisition of Revance Therapeutics", February 7, 2025](https://www.hildred.com/news/crown-laboratories-completes-acquisition-of-revance-therapeutics)
  - PE: "Crown Laboratories, Inc. ("Crown"), a Hildred Capital portfolio company and privately held, global innovative leader in the skincare industry, announced the closing of its acquisition of Revance Therapeutics, Inc." and "Hildred Capital is a healthcare-focused private equity firm that specializes in operationally intensive, control-oriented investments in lower middle-market companies." — [same release](https://www.hildred.com/news/crown-laboratories-completes-acquisition-of-revance-therapeutics)
  - Current: "Investment year: 2017 Status: Partial exit (HCP I), Private (HPP I & HEP III)" (field text; page title "Hildred™ Portfolio | Crown") — [Hildred, portfolio entry "Revance"](https://www.hildred.com/portfolio/revance)
  - Stake: none stated; counts as control. One Hildred fund partly exited; two still hold.
  - Affiliate: none found.
  - BDC names: "Crown Laboratories, Inc.", "Revance Therapeutics, Inc.", "Revance"
- **PC23 EltaMD**
  - Owner: "EltaMD, Filorga and PCA SKIN skin health products" — [Colgate-Palmolive 10-K FY2025](https://www.sec.gov/Archives/edgar/data/21665/000002166526000006/cl-20251231.htm)
  - Footer: "© 2026 CP Skin Health Group, Inc. All rights reserved. EltaMD is a registered trademark of EltaMD, Inc." — [EltaMD home page, accessed 2026-11-17](https://eltamd.com/)
  - Affiliate: none found ("Become a practice" is a professional-channel account, not an affiliate program).
  - BDC names: "EltaMD, Inc.", "CP Skin Health Group"
- **PC24 Supergoop!**
  - PE: "These partnerships follow a majority investment in Supergoop! by funds managed by Blackstone Growth (BXG) in late 2021" — [Blackstone, press release "Supergoop! and Blackstone Growth (BXG) Partner with New Investors…", May 24, 2022](https://www.blackstone.com/news/press/supergoop-and-blackstone-growth-bxg-partner-with-new-investors-to-teach-even-more-people-about-the-importance-of-daily-spf/)
  - Current: "Ms. Chung currently serves on the Board of Directors of Oatly, Spanx and Supergoop." — [Blackstone, Ann Chung profile, accessed 2026-11-17](https://www.blackstone.com/people/ann-chung/)
  - Footer: "© Supergoop! 2026" — [Supergoop! home page](https://supergoop.com/)
  - Stake: majority stated, so control. The 2022 minority investors (celebrities and entrepreneurs) are individuals.
  - Affiliate: "Discounts & Commission 10% discount code Personal affiliate link" — [Supergoop!, Supergoop Superstars (college ambassadors)](https://supergoop.com/pages/supergoop-superstars). Brand-run, but limited to college ambassadors; network listings (Sovrn, FlexOffers "Deactivated") were not opened.
  - BDC names: "Supergoop, LLC" (in the BDC data)
- **PC25 Johnson's Baby**
  - Owner: "(NASDAQ: KMB), a core S&P 500 component, today announced that it has completed its acquisition of Kenvue." and "Huggies, Listerine, Cottonelle, Neutrogena, Depend, Tylenol, Kleenex, Johnson’s Baby, Kotex and Scott" — [Kimberly-Clark 8-K exhibit 99.1, November 2, 2026](https://www.sec.gov/Archives/edgar/data/55785/000110465926120990/tm2628636d1_ex99-1.htm)
  - Name ownership: "J&J has transferred ownership of the intellectual property rights related to the “Johnson’s®” brand to us, unless prohibited by law in a particular jurisdiction." — [Kenvue 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1944048/000194404826000030/kvue-20251228.htm). Kenvue (now K-C) owns the name; J&J licenses only its own "Johnson & Johnson" name and signature.
  - K-C 5% holders: no 13D; 2026 13Gs all "Rule 13d-1(b)": BlackRock "8.8", Vanguard Capital Management "7.5", State Street "6.5", FMR "5.9", The Vanguard Group "0". [13G XML (BlackRock)](https://www.sec.gov/Archives/edgar/data/55785/000201238326001498/primary_doc.xml)
  - Affiliate: not checked (johnsonsbaby.com 403).
  - BDC names: "Kenvue", "Johnson & Johnson Consumer", "Kimberly-Clark"
- **PC26 Aquaphor**
  - Owner: "Alongside Eucerin, the portfolio also includes brands such as Aquaphor, Hansaplast, and NIVEA." and "Aquaphor and Eucerin are part of Beiersdorf AG and are grouped under the Derma category." — [Beiersdorf, Eucerin brand page](https://www.beiersdorf.com/brands/eucerin)
  - Holders: as PC21.
  - Affiliate: none found in aquaphorus.com's raw HTML; the footer is rendered by script.
- **PC27 Lubriderm**
  - Owner: "Major brands in the segment include Aveeno®, Dr.Ci:Labo®, Le Petit Marseillais®, Lubriderm®, Neutrogena®, OGX®, and Rogaine®." — [Kenvue 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1944048/000194404826000030/kvue-20251228.htm); Kenvue now part of Kimberly-Clark (PC25).
  - Affiliate: not checked (lubriderm.com 403).
- **PC28 eos**
  - Owner: not stated. "eos Products, LLC (“EOS,” “us,” “our,” and “we”) cares about your privacy." — [eos, Privacy Policy](https://evolutionofsmooth.com/pages/privacy). The footer reads "© 2026 eos".
  - Notes: a case-study page (not cited) says co-founder Jonathan Teller controls about 85% and that a sale was being explored in 2025. No PE lead.
  - Affiliate: none counted. "Not your average ambassador program." — [eos, ambassador page](https://evolutionofsmooth.com/pages/brand-ambassador-program). It pays coins and discounts, not commission.
  - BDC names: "eos Products, LLC"
- **PC29 Certain Dri**
  - Owner: "Terms of Use”) are entered into by and between you (“you”, “your”, or “user”) and Bridges Consumer Healthcare, LLC" and "The Company’s name “Bridges Consumer Healthcare,” “Certain Dri®”, along with all related names, logos, product and service names, designs, and slogans are trademarks of the Company" — [Certain Dri, Terms and Conditions](https://certaindri.com/terms-and-conditions/)
  - PE: "Bridges Consumer Healthcare OTC healthcare products Current" (tile) — [Charlesbank, Investments](https://www.charlesbank.com/investments/); "Year of Investment 2020 Sector(s) Business & Consumer Services Status Current" (fields) — [Charlesbank, Bridges Consumer Healthcare](https://www.charlesbank.com/investments/bridges-consumer-healthcare/)
  - Since: Charlesbank 2020. The [same page](https://www.charlesbank.com/investments/bridges-consumer-healthcare/) lists a related release titled "Bridges Consumer Healthcare, Portfolio Company of Charlesbank Capital Partners, Acquires Clarion B…" (Clarion Brands owned Certain Dri; the release on globenewswire.com returned 403).
  - Stake: none stated; counts as control.
  - Affiliate: none found.
  - BDC names: "Bridges Consumer Healthcare, LLC", "Bridges Consumer Healthcare Intermediate LLC" (near match in the BDC data), "Clarion Brands"
- **PC30 Mitchum**
  - Owner: "operated by Revlon Consumer Products LLC and our subsidiaries and affiliates" — [Mitchum, Terms of Use](https://www.mitchum.com/pages/terms-of-use). The footer reads "©2026 Mitchum. All Rights Reserved."
  - Revlon's owners: "The majority of the Company’s equity will be owned by its former lenders." and "brands such as Revlon, Revlon Professional, Elizabeth Arden, Almay, Mitchum, CND, American Crew…" — [Revlon 8-K exhibit 99.2 (plan confirmation release, April 2023)](https://www.sec.gov/Archives/edgar/data/887921/000114036123016005/brhc10050829_ex99-2.htm). The emergence 8-K (May 2023) names no holders.
  - Owner kind: not confirmed, because the lenders are unnamed in any primary source read. Trade press (not cited) names Glendon, King Street, Angelo Gordon, Oak Hill and Cyrus. Their ADVs: TPG Angelo Gordon `Y`; Glendon, King Street, Oak Hill and Cyrus `N`.
  - Affiliate: none found.
  - BDC names: "Revlon Consumer Products LLC", "Revlon Group Holdings"

### Rollups and groups that are not brands
Not counted in the 30.
- **Unilever PLC:** Dove, Vaseline, Dove Men+Care, Axe, Dr. Squatch (and Degree by trade press). Public (UL).
- **Procter & Gamble:** Gillette, Secret, Old Spice, Native. Public (PG).
- **Colgate-Palmolive:** Softsoap, EltaMD (CP Skin Health Group). Public (CL).
- **Edgewell Personal Care:** Banana Boat, Hawaiian Tropic. Public (EPC). It sold Feminine Care to Essity, closed 2026-02-02.
- **Beiersdorf AG:** Coppertone, Aquaphor. Listed; maxingvest group 54.4%.
- **Kenvue (Kimberly-Clark since 2026-11-02):** Johnson's Baby, Lubriderm. Public (KMB).
- **Evermark, LLC (Yellow Wood Partners):** Suave, plus Q-tips, ChapStick, Pond's, Caress, St. Ives, Noxzema and TIGI. None of the others is a row.
- **Crown Laboratories / Revance (Hildred Capital):** Blue Lizard, PanOxyl, StriVectin, SkinPen.
- **Bridges Consumer Healthcare (Charlesbank):** Certain Dri and 9 other OTC brands.
- **Mammoth Brands:** Lume, Harry's, Flamingo, Mando, Coterie. Private; owners not stated.
- **Revlon Group Holdings:** Mitchum, Revlon, Elizabeth Arden, Almay and others. Private; majority held by former lenders.
- Henkel (Dial), Sanofi (Gold Bond), Kao (Jergens) and Bath & Body Works are one row each.

### Category share
- **PE-owned (control, or no stated stake): 4 / 30 = 13.3%**
  - Suave: Yellow Wood via Evermark (no stated stake).
  - Blue Lizard: Hildred via Crown (no stated stake).
  - Supergoop!: Blackstone Growth (majority stated).
  - Certain Dri: Charlesbank via Bridges (no stated stake).
- **PE minority stake: 0.** PE-owned plus minority = **4 / 30 = 13.3%**.
- **Public company: 21 / 30 = 70.0%**:
  - Unilever 5 (Dove skin care, Vaseline, Dove Men+Care, Axe, Dr. Squatch);
  - P&G 4 (Gillette, Secret, Old Spice, Native);
  - Colgate 2 (Softsoap, EltaMD);
  - Edgewell 2 (Banana Boat, Hawaiian Tropic);
  - Beiersdorf 2 (Coppertone, Aquaphor);
  - Kimberly-Clark 2 (Johnson's Baby, Lubriderm);
  - Bath & Body Works, Henkel (Dial), Sanofi (Gold Bond), Kao (Jergens).
  - No current 5%+ holder of the SEC filers counts: every 2025–2026 13G read is 13d-1(b), and there is no current 13D. Kao's holders and Beiersdorf's maxingvest were not classified.
- **Private, owner not stated: 2** (Lume under Mammoth Brands; eos). **Owner type not confirmed: 1** (Mitchum).
- **Not found: 2 / 30 = 6.7%** (Degree, Sun Bum). Neither has a PE lead: trade press names Unilever and SC Johnson.
- **By tier:**
  - YouGov consideration rows 1–11: 0 PE.
  - Circana deodorant regular top 10: 1 PE (Suave), $94.0M of the ten brands' $4,540.8M (2.1%), and 1.8% of the $5,192.0M regular segment.
  - Circana sun care rows: 2 PE of 7 (Blue Lizard, Supergoop!), $233.3M of those seven brands' $1,242.3M (18.8%), and 8.3% of the $2,799.9M suntan segment.
  - YouGov Ratings rows: 0. Improvers row (eos): 0.
  - Clinical deodorant rows: 1 PE of 2 (Certain Dri, 4.1% of the $270.7M clinical segment).
- **By parent company:** 19 parents (Unilever, P&G, Colgate, Edgewell, Beiersdorf, Kimberly-Clark, Bath & Body Works, Henkel, Sanofi, Kao, Evermark, Crown, Supergoop!, Bridges, Mammoth, eos, Revlon, and the two not-found rows counted as their own). PE-held parents: 4 / 19 = 21.1%.
- **Upper bound if leads were confirmed: 6 / 30 (20.0%).**
  - Lume (+1) if a primary source shows a Mammoth investor with ADV `Y` (Thrive Capital, Tiger Global, Alliance Consumer Growth, SurgoCap) holding today.
  - Mitchum (+1) if a primary source names TPG Angelo Gordon (ADV `Y`) among Revlon's controlling lenders.
  - Degree, Sun Bum and eos have no PE lead.
- **Sources disagree:** none on owners.

**Affiliate income:**
- **Brand-direct programs found (3):** Lume (Impact), Native (P&G creator affiliate terms) and Supergoop! (college ambassadors' "Personal affiliate link").
- **By PE status:** PE 1 (Supergoop!, restricted); non-PE 2 (Lume; Native).
- **Network listings only (2):** Dr. Squatch (Pepperjam; FlexOffers), Bath & Body Works (Rakuten per directories; site blocked).
- **Not checked, site blocked (6):** Vaseline, Degree, Axe, Johnson's Baby, Lubriderm, Bath & Body Works (also listed above).
- **None found (20):** every other row; links on the home page or footer were checked. The ambassador pages of Sun Bum (points) and eos (coins) pay no commission and are not counted.

## Firms named
Every investment firm named as an owner, former owner or 5%+ holder, as the sources name it:
- **Yellow Wood Partners** ("Yellow Wood Partners", Evermark release): Suave
- **Hildred Capital** ("Hildred Capital", "Hildred Capital Partners"; funds HCP I, HPP I, HEP III): Blue Lizard
- **Blackstone Growth (BXG)** ("funds managed by Blackstone Growth (BXG)"): Supergoop!
- **Charlesbank Capital Partners**: Certain Dri, via Bridges
- **Summit Partners** (former owner of Dr. Squatch; seller per Unilever's 2025 release, not read)
- **Third Point LLC** (BBWI 13D, ended 2024-10-23)
- 13G filers under 13d-1(b), which never count:
  - Edgewell: Brandes Investment Partners, American Century, Rubric Capital Management, Vanguard (three entities), Dimensional.
  - Bath & Body Works: FMR, AQR, Vanguard.
  - Kimberly-Clark: BlackRock, State Street, FMR, Vanguard.
  - P&G and Colgate: Vanguard.
- Leads only (not cited, not counted):
  - Mammoth/Harry's investors: Thrive Capital, Tiger Global, Alliance Consumer Growth, SurgoCap, Highland Capital Partners.
  - Revlon's former lenders: Glendon, King Street, Angelo Gordon, Oak Hill, Cyrus.
  - Encore Consumer Capital and SWAT Equity (rolled Supergoop! stakes in 2021, per trade press).
  - L'Oréal (7.27% of Sanofi; a public company).

## Form ADV results
SEC adviser files, November 2026 (registered and exempt rosters), matched by legal or business name.

| Firm (as named) | Adviser matched | CRD | Roster | Any PE Funds | PE funds | Row effect |
|---|---|---|---|---|---|---|
| Yellow Wood Partners | YELLOW WOOD PARTNERS LLC | 161062 | registered | **Y** | 10 | Suave PE-owned |
| Hildred Capital | HILDRED CAPITAL MANAGEMENT, LLC | 301293 | registered | **Y** | 17 | Blue Lizard PE-owned |
| Blackstone Growth | BLACKSTONE GROWTH ADVISORS L.L.C. (also BLACKSTONE MANAGEMENT PARTNERS L.L.C., CRD 136979, Y, 36) | 305708 | registered | **Y** | 8 | Supergoop! PE-owned |
| Charlesbank Capital Partners | CHARLESBANK CAPITAL PARTNERS, LLC | 160256 | registered | **Y** | 31 | Certain Dri PE-owned |
| Summit Partners | SUMMIT PARTNERS, L.P. | 135271 | registered | Y | 87 | none (exited Dr. Squatch 2025) |
| Third Point | THIRD POINT LLC | 137927 | registered | Y | 7 | none (13D ended 2024) |
| Rubric Capital Management | RUBRIC CAPITAL MANAGEMENT LP | 285090 | registered | Y | 2 | none (Edgewell 13G under 13d-1(b)) |
| Brandes Investment Partners | BRANDES INVESTMENT PARTNERS, LP | 105404 | registered | N | — | none |
| American Century | AMERICAN CENTURY INVESTMENT MANAGEMENT INC | 105778 | registered | N | — | none |
| Thrive Capital (lead) | THRIVE CAPITAL MANAGEMENT, LLC (website x.com/thrivecapital) | 162771 | registered | Y | 2 | Lume upper bound only |
| Tiger Global (lead) | TIGER GLOBAL MANAGEMENT, LLC | 160318 | registered | Y | 28 | Lume upper bound only |
| Alliance Consumer Growth (lead) | ALLIANCE CONSUMER GROWTH, LLC | 163639 | registered | Y | 9 | Lume upper bound only |
| SurgoCap (lead) | SURGOCAP PARTNERS LP | 323078 | registered | Y | 1 | Lume upper bound only |
| Highland Capital Partners (lead) | HIGHLAND CAPITAL PARTNERS LLC | 161205 | exempt | N | — | none |
| Angelo Gordon (lead) | ANGELO, GORDON & CO., L.P. (TPG Angelo Gordon) | 131940 | registered | Y | 32 | Mitchum upper bound only |
| Glendon (lead) | GLENDON CAPITAL MANAGEMENT L.P. | 166119 | registered | N | — | none |
| King Street (lead) | KING STREET CAPITAL MANAGEMENT, L.P. | 156785 | registered | N | — | none |
| Oak Hill Advisors (lead) | OAK HILL ADVISORS, L.P. | 125352 | registered | N | — | none |
| Cyrus Capital (lead) | CYRUS CAPITAL PARTNERS, L.P. | 136713 | registered | N | — | none |

- A second "THRIVE CAPITAL MANAGEMENT, LLC" (CRD 281347, website thrivefinancialservices.com, `N`) is an unrelated adviser.
- Blackstone has many adviser registrations: real estate ones say `N`, and the PE, growth and credit ones say `Y`. Any `Y` counts.

## BDC names
SEC BDC data sets 2026-07 to 2026-10 (bulk Q2 file 2026_08), searched in "Investment, Identifier Axis" for each row's brand, owner and borrower names.
- **Supergoop! (counts; brand name in borrower):** "Supergoop, LLC". BlackRock Direct Lending Corp. holds a first-lien term loan and a senior secured revolver (periods 2025-12-31 and 2026-06-30).
- **Suave (counts; brand name in borrower):** "Suave Silk Holdings III Corp." First-lien term loans and revolvers are held by Apollo Debt Solutions BDC, Apollo Origination II (Levered) Capital Trust, Apollo Origination II (UL) Capital Trust, MidCap Apollo Institutional Private Lending and MidCap Financial Investment Corp. MidCap Financial Investment Corp. also holds "Suave Silk Holdings I Corp. Common Equity - Common Stock". That is BDC-held equity, which never counts as PE; the ownership already counts through Yellow Wood.
- **Certain Dri (near match, not counted):** "Bridges Consumer Healthcare Intermediate LLC", held by Antares Private Credit Fund, Antares Strategic Credit Fund, Antares Strategic Credit Fund II, Nuveen Churchill Direct Lending Corp. and Nuveen Churchill Private Capital Income Fund. Certain Dri's terms name "Bridges Consumer Healthcare, LLC", which is not the same legal name (see Open questions).
- **No hit:** the other 27 rows and their parents. Matches on "Degree" (Degreed, Inc.; NTH Degree Purchaser Inc.) are unrelated and excluded.

## Affiliate programs
| Row | PE? | Program | Where | Notes |
|---|---|---|---|---|
| Lume | no (private, owner not stated) | brand-direct | https://lumedeodorant.com/affiliate-program | applicants sign up through Impact |
| Native | no (P&G) | brand-direct (creator affiliate terms) | https://www.nativecos.com/pages/creators-terms-and-conditions | commission on approved platforms |
| Supergoop! | **yes** (Blackstone Growth) | brand-direct, restricted | https://supergoop.com/pages/supergoop-superstars | college ambassadors only: "Personal affiliate link" |
| Dr. Squatch | no (Unilever) | network listing only | Pepperjam (JEBCommerce launch post), FlexOffers | brand page /pages/affiliates 404 |
| Bath & Body Works | no | network listing only | Rakuten (directories) | site blocked (captcha) |

## Licensed rows
- **None of the 30 rows is a licensed name.**
- **Suave:** the name is split by territory. Evermark (Yellow Wood) owns the US and Canadian business, and Unilever keeps Suave elsewhere, per Unilever's 2023 release (lead; unilever.com blocked). The US row belongs to Evermark.
- **Johnson's Baby:** Kenvue (now Kimberly-Clark) owns the "Johnson's" brand IP, transferred from J&J. J&J licenses only its "Johnson & Johnson" name and signature (Kenvue 10-K).
- **Gold Bond:** Gold Bond Co LLC, retained by Sanofi (not a licence).

## Surprises
- **Suave is PE-owned in the US** (Yellow Wood, through Evermark since 2026-01-20; Unilever's disposal was in 2023), and it borrows from Apollo BDCs.
- **Dr. Squatch left PE** (Summit Partners) for Unilever on 2025-09-02, and **Third Point's activist 13D on Bath & Body Works ended** in October 2024. Both are "formerly PE" history.
- **Blue Lizard's maker now calls itself "a Revance Company".** Crown Laboratories bought Revance (Nasdaq: RVNC) in February 2025, and Hildred's portfolio lists the combined business as "Revance", "Partial exit (HCP I), Private (HPP I & HEP III)": a continuation fund still holds it.
- **Rubric Capital (ADV `Y`) holds 8.56% of Edgewell** but filed under Rule 13d-1(b), so it doesn't count.
- **Kimberly-Clark closed its Kenvue purchase on 2026-11-02**, which puts Johnson's Baby, Lubriderm and Neutrogena under KMB.
- **The PE in personal care is in mid-sized and challenger names** (Suave, Supergoop!, Blue Lizard, Certain Dri), as the screen predicted, but three of the four reach the list through Circana sales tables rather than YouGov's consideration ranking.

## Open questions for the developer
Numbers only; nothing decided.
1. **Oral care.** Left out to match the earlier screen. Taking Colgate (#2), Crest (#4) and Listerine (#6) into tier (a) pushes out rows 28–30 (eos, Certain Dri, Mitchum), and PE goes from 4/30 (13.3%) to 3/30 (10.0%).
2. **The clinical-deodorant tail.** Rows 29–30 come from a $270.7M segment, with Mitchum at $167K. Without tier (f) the list is 28 rows and PE is 3/28 (10.7%).
3. **Sun care as personal care.** 7 rows come from the sun care table, 2 of them PE (Blue Lizard, Supergoop!). If sun care went to the beauty audit, personal care would need 7 replacement rows from a source not found here. Supergoop! is a prestige SPF brand sold at Sephora, the closest to "skin care sold as beauty".
4. **Lume.** It counts as private, owner not stated. Four of Mammoth Brands' reported investors have ADV `Y`; if one is confirmed as a current holder, the count becomes 5/30 (16.7%).
5. **Mitchum.** It counts as owner type not confirmed. If a primary source names TPG Angelo Gordon (ADV `Y`) among Revlon's controlling lenders, the count becomes 5/30. With Lume as well, 6/30 (20.0%).
6. **Sun Bum.** It counts as owner not found, because SC Johnson's 2019 release is a signing and no closing source was read.
7. **Degree.** It counts as owner not found, because every primary source tried was blocked.
8. **BDC near match.** "Bridges Consumer Healthcare Intermediate LLC" vs "Bridges Consumer Healthcare, LLC" (Certain Dri's terms). If it counts, BDC overlap goes from 2 to 3.
9. **Supergoop!'s affiliate program.** It is brand-run but limited to college ambassadors. Counted as brand-direct; otherwise the split is PE 0, non-PE 2.

## Cost
- **Time:** 22:59–23:28 UTC for fetching (about 30 minutes), plus ranking searches before and writing after.
- **Web searches:** 29 (12 for the ranking; 17 for owners, affiliate programs and URLs).
- **Page fetches:** 129 logged in index.tsv (128 by curl and 1 Playwright visit), plus one index line (130) for a browser that never launched. Of the curl fetches, 112 returned 200, 10 returned 403, 4 returned 404 and 1 each returned 307, 429 and 500.
- **HTTP requests by curl:** 213 in requests.log, including 64 robots.txt reads and redirect hops. SEC: 46.
- **WebFetch:** 0. Every quote comes from curl-saved text.
- **Tokens:** not metered by this worker; roughly 300k.
- **Page cache:** `$SCR/pages/personal-care/` (NNN.html and NNN.txt, index.tsv, requests.log, robots.tsv, robots/). Scripts are in `$SCR/scripts/personal-care/`, where `$SCR` is `/tmp/claude-1000/-home-iherr-projects-enshittified-demystified/02bcbe8a-bc03-477c-8c3d-2aa6ddd83e94/scratchpad`.
- **Quote self-check:** `qcheck.py` (in the scripts folder) string-matched every double-quoted string of 12 or more characters against the saved text and HTML of the cached pages cited on the same line. It collapses whitespace, normalizes curly quotes and dashes, and matches text on either side of "…" separately.
  - 110 found. 14 "misses" are by design: the regex picked up text between two quoted values on the 13G holder lines, so they are not quotes.
  - The 66 skipped strings sit on lines with no cached URL: BDC-name lists, cross-references and summary lines.
  - Negative control: altering the end of each quote made all of them fail.
  - 13G percentages and rule boxes are XML field values, too short to check (under 12 characters); they can be read in the cited XML files.
- **What was fast:** public parents (one 10-K or 20-F settles 2–5 rows each); 13G XML files, which state the 13d-1(b) box as a field; and sponsor pages served as plain HTML (Charlesbank, Hildred, Yellow Wood).
- **What was slow:** the ranking (no single free source reaches 30); Akamai blocks on every Unilever and Kenvue brand site; and Sun Bum and Degree, whose owners' own sites refused the bot.
