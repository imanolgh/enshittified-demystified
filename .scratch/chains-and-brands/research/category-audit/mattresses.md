# Category audit: Mattresses

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (fetches logged 16:59–17:22 UTC) · Ownership facts come from primary sources only. Trade press supplies the ranking only.

**Short answer**

| | Mattresses (30 brand rows) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **8 / 30 (26.7%)**. All eight are PE-owned (control, or no stated stake): Brooklyn Bedding, Helix Sleep, Birch, Bear Mattress, Nolah and Leesa (3Z Brands, Cerberus), and Mattress Warehouse and Sleep Outfitters (Wynnchurch Capital). None is a minority stake. |
| Strict count (public company with a 5%+ holder whose Form ADV reports PE funds) | **Pending one firm.** Purple (Nasdaq: PRPL) has Coliseum Capital Management at 49.6%, and its 10-K says Coliseum "exercises substantial control". If Coliseum's Form ADV reports PE funds, Purple moves to PE and the share becomes **9 / 30 (30.0%)**. Somnigroup's 5%+ holders are FMR, Vanguard and BlackRock. |
| Owner not found or owner type not confirmed | **10 / 30 (33.3%)**. Four Serta Simmons Bedding rows (Serta, Beautyrest, Simmons, Tuft & Needle) are in this bucket: the brand owner is known, but its owners since the 2023 Chapter 11 exit are not stated. |
| Share of company sales on PE-owned rows | **8.8%** ($914M of $10,438M; figures mix HNN retail estimates and one 10-K wholesale segment; no-figure rows left out) |
| Brand-direct affiliate programs | **10 found**: Saatva, Leesa, Bear, Brooklyn Bedding, Purple, Nectar, DreamCloud, Avocado, Brentwood Home and Mattress Warehouse. **4 of the 10 sit on PE-owned rows** (Leesa, Bear, Brooklyn Bedding and Mattress Warehouse). Helix and Mattress Firm were blocked (HTTP 403). |

- **Two 2026 ownership changes that the ranking predates.**
  - **Sleep Number** sold substantially all its assets in a Chapter 11 sale to SNBR, Inc., a subsidiary of Sleep Country Canada Inc. The sale closed on 2026-07-31 (Sleep Number 8-K). Sleep Country is owned by Fairfax Financial Holdings, an insurance holding company. Sleep Number deregistered (Form 15, 2026-08-03).
  - **Somnigroup** (Tempur-Pedic, Sealy, Stearns & Foster, Mattress Firm) completed its acquisition of Leggett & Platt on 2026-08-26. Leggett is a components supplier, not a consumer brand.
- **No PE firm in the largest chain.** Somnigroup (NYSE: SGI) owns the #1 retailer (Mattress Firm, 2,174 stores) and three of the biggest product brands, and has no PE holder at 5%+.
- **PE sits in the online and mid-size retail tier.** Cerberus's 3Z Brands owns six direct-to-consumer names. Wynnchurch's Mattress Warehouse became the #2 mattress-store chain (531 stores) after buying 73 Mattress Firm stores and the Sleep Outfitters chain from Somnigroup on 2025-05-01.
- **Formerly PE:** Casper (Durational Capital Management, 2022 to 2024, then sold to Carpenter Co.). Serta Simmons Bedding's January 2023 restructuring release lists counsel to Advent International. Advent's majority since 2012 is from trade press only.

## How this was sourced (read first)

- **Ranking:** composite (see "Ranking" below). Home News Now's "Top 125" list of furniture and bedding retailers (estimated 2025 US sales) supplies the retail and direct-to-consumer rows. Somnigroup's 10-K supplies one wholesale figure. Neither is used as evidence of ownership.
- **Ownership facts:** SEC filings (10-K, DEF 14A, 8-K and an 8-K exhibit), company and sponsor press releases, sponsor portfolio pages, and company sites. One fact rests on a law-firm deal page (Torys LLP for Fairfax's purchase of Sleep Country Canada), because the company release on newswire.ca returned HTTP 403 and Sleep Country's own site is robots-disallowed. It is flagged in row MT5.
- **SEC access:** all SEC requests (www.sec.gov, data.sec.gov, efts.sec.gov) used the user agent `EvidenceEngine ownership-research bot (category audit)` with no contact detail, with a 0.6 s sleep per request (under 2 per second). All returned HTTP 200.
- **Robots:** robots.txt was read before each new site fetched with curl, for `*`, ClaudeBot, anthropic-ai and Claude-Web.
  - **Not used, robots-disallowed:** furnituretoday.com (disallows anthropic-ai and Claude-Web; never fetched beyond robots.txt) and sleepcountry.ca (names ClaudeBot and anthropic-ai; never fetched beyond robots.txt).
  - **Blocked:** beddingnewsnow.com (CleanTalk HTTP 403), newswire.ca (403), helixsleep.com (403), mattressfirm.com (403). Not retried.
  - **No response:** bedmart.com.
  - **3zbrands.com:** its robots.txt lists ClaudeBot and anthropic-ai in the same group as `*`, which disallows only paths such as /config and /search. The homepage is allowed and was used.
- **Never fetched:**
  - competitor sites (a Worse on Purpose ledger page for Saatva came up in search and was not opened), Reddit, WhoIsMyDentist and Private Equity Vet;
  - PitchBook, Preqin and CB Insights results that came up in search.
- **Leads only, never cited:** deal directories (mergr, privsource, privateequityinfo, mergerlinks, multiples.vc) and affiliate-network or directory listings (FlexOffers, UpPromote, affilimate, LinkClicky, revshare) were read as search snippets only.
- **Owner kinds are research notes, not engine classifications.**
  - "PE-owned" means control, or a PE owner with no stated stake. A public company that a PE fund controls would count as PE-owned.
  - Counts are by brand row: Somnigroup is 5 rows, 3Z Brands is 6, Serta Simmons Bedding is 4, and Ashley is 3.
  - "Not found / owner type not confirmed" also covers rows where the brand's parent is known but nothing states who owns the parent (Serta Simmons Bedding, Carpenter Co.).
- **Quotes:** copied from the curl'd page text with HTML tags removed, entities decoded and whitespace collapsed. No WebFetch calls were made, so no quote passed through a summarizer.

## Ranking

**No free, current, robots-permitted top-30 ranking of US mattress brands was found.**
- Furniture Today's "Top 15/20 Bedding Producers" (by US wholesale shipments) is the trade ranking for producers. Search results show editions only up to 2021 (2020 data). furnituretoday.com's robots.txt disallows anthropic-ai and Claude-Web, so it was not used.
- Bedding News Now (beddingnewsnow.com) returned an anti-spam 403. BedTimes (ISPA) and Statista surfaced no free current list.

**Composite used.** Rows are ordered by the most recent US sales figure for each brand's company, from two sources:
- (a) **Home News Now (HNN) "Home News Now 125 furniture & bedding retailers 2025"**, published in five parts from 2026-05-26 to 2026-06-22. It ranks retailers, including e-tailers, by estimated 2025 US furniture and bedding sales ($ millions).
  - Parts: [Nos. 1–25 (2026-06-22)](https://homenewsnow.com/blog/2026/06/22/home-news-now-125-furniture-bedding-retailers-2025-nos-1-25/), [26–50 (2026-06-14)](https://homenewsnow.com/blog/2026/06/14/home-news-now-125-furniture-bedding-retailers-2025-nos-26-50/), [51–75 (2026-06-07)](https://homenewsnow.com/blog/2026/06/07/home-news-now-125-furniture-bedding-retailers-2025-nos-51-75/), [76–100 (2026-05-31)](https://homenewsnow.com/blog/2026/05/31/home-news-now-125-furniture-bedding-retailers-2025-nos-76-100/), [101–125 (2026-05-26)](https://homenewsnow.com/blog/2026/05/26/home-news-now-125-furniture-bedding-retailers-2025-nos-101-125/).
  - The page says: "The 125 listing is based on estimated 2025 furniture and bedding sales in the U.S." and "All sales figures are estimated in millions of dollars and were compiled from a variety of sources including retailer input, publicly held company SEC filings, news releases, store websites and industry news reports."
  - Every mattress specialist or mattress brand on the list was taken. General furniture stores with a mattress sub-banner (Mathis Sleep, GW Mattress, Levin Mattress) and mass merchants were left out.
  - The rows taken, with HNN rank, 2025 sales ($M) and 2025 stores: 4 Mattress Firm 3,582.0 (2,174); 17 Sleep Number 1,270.0 (600); 31 3Z Brands 519.0 (12); 33 Saatva 515.0 (29); 37 Avocado Green Brands 410.0 (14); 39 Mattress Warehouse 395.0 (531); 44 Casper Sleep 293.5 (40); 48 Purple 251.0 (55); 64 Tuft & Needle 154.5 (store count not stated); 65 America's Mattress 148.0 (96); 73 The Original Mattress Factory 118.0 (114); 91 BedMart 79.0 (40); 105 City Mattress 58.0 (29); 110 Nest Bedding 52.5 (2).
- (b) **Wholesale brands that HNN cannot rank, because it ranks retailers.**
  - Tempur-Pedic, Sealy and Stearns & Foster are placed by Somnigroup's 2025 Tempur Sealy North America segment. The 10-K gives gross profit of $1,383.8M at a 51.2% margin, so net sales are about $2,703M. This is wholesale plus Tempur-Pedic's own stores, net of sales to Mattress Firm.
  - Brands with **no public sales figure** come last, grouped by parent: Ashley's Sierra Sleep, Nectar and DreamCloud; Serta Simmons Bedding's Serta, Beautyrest and Simmons; Somnigroup's Sleepy's (Mattress Firm private label); and Zinus. They are national wholesale or online brands, so they are ranked above the smaller regional HNN chains. **Their order is not a sales order.**
- **Within one company,** brands follow the order the company lists them.
- **Cutoff:** the list stops at 30 rows. Left out: City Mattress ($58.0M) and Nest Bedding ($52.5M) from HNN, and Corsicana, which moved to the "not brands" list (see below).
- **Not exhaustive.** Brands with no public sales figure that were not checked and may belong above the cutoff: Spring Air, Kingsdown, King Koil, Englander, Restonic, Therapedic, tulo (Mattress Firm), Intellibed (Purple), Awara and Siena (Resident/Ashley), GhostBed, Puffy, Amerisleep, WinkBeds, Layla, Lull, Allswell (Walmart private label) and Lady Americana (Mathis Home).
- **Caveat:** the figures mix retail sales (HNN) with one wholesale segment (10-K), and Mattress Firm resells Somnigroup's brands. The order is indicative only.

| # | Brand (2025 sales basis; stores) | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Mattress Firm (HNN $3,582.0M; 2,174 stores) | Somnigroup International Inc. | public company | none at 5%+ (FMR 14.11%, Vanguard 7.57%, BlackRock 6.94%) | 2025-02-05 | SGI | company-owned stores ("over 2,100") plus e-commerce | blocked (mattressfirm.com 403) | MT1 |
| 2 | Tempur-Pedic (Somnigroup TSNA ~$2,703M) | Somnigroup International Inc. | public company | none at 5%+ | not checked (brand native to parent) | SGI | Wholesale and Direct (company stores, e-commerce) | none found | MT2 |
| 3 | Sealy (same basis) | Somnigroup International Inc. | public company | none at 5%+ | not checked | SGI | Wholesale and Direct | none found | MT2 |
| 4 | Stearns & Foster (same basis) | Somnigroup International Inc. | public company | none at 5%+ | not checked | SGI | Wholesale and Direct | none found | MT2 |
| 5 | Sleep Number (HNN $1,270.0M; 600 stores) | SNBR, Inc., a wholly owned subsidiary of Sleep Country Canada Inc.; Sleep Country is owned by Fairfax Financial Holdings Limited | other: insurance holding company (Fairfax describes itself as a holding company engaged in property and casualty insurance) | none | 2026-07-31 (asset sale closed; Sleep Country to Fairfax 2024-10-01) | — (seller is now OTC: SNBRQ, deregistered) | company-operated stores and online ("exclusive direct- to-consumer selling in 600 stores and online") | none found | MT5 |
| 6 | Brooklyn Bedding (HNN 3Z Brands $519.0M; 12 showrooms) | 3Z Brands; an affiliate of Cerberus Capital Management acquired Brooklyn Bedding LLC (stake not stated) | PE-owned (no stated stake) | Cerberus Capital Management | 2021-10-13 | — | manufacturer, wholesaler, DTC; Arizona showrooms | **yes**: https://brooklynbedding.com/pages/ambassador-program (via Impact, 5%) | MT6 |
| 7 | Helix Sleep (same basis) | 3Z Brands; Cerberus affiliate acquired Helix Sleep, Inc. | PE-owned (no stated stake) | Cerberus Capital Management | 2021-10-13 | — | DTC | blocked (helixsleep.com 403) | MT6 |
| 8 | Birch (same basis) | 3Z Brands | PE-owned (no stated stake) | Cerberus Capital Management | 2021-10-13 (a Helix brand then; listed as 3Z brand 2022) | — | DTC | none found | MT6 |
| 9 | Bear Mattress (same basis) | 3Z Brands | PE-owned (no stated stake) | Cerberus Capital Management | 2022 | — | DTC | **yes**: https://www.bearmattress.com/pages/partnerships | MT6 |
| 10 | Nolah (same basis) | 3Z Brands | PE-owned (no stated stake) | Cerberus Capital Management | 2022–23 ("within the last year" before 2023-03-15) | — | DTC | network listings only (FlexOffers/Impact per directories) | MT6 |
| 11 | Leesa (same basis) | 3Z Brands | PE-owned (no stated stake) | Cerberus Capital Management | 2023-03-15 | — | DTC plus stores and West Elm partnership | **yes**: https://www.leesa.com/pages/affiliates (via Impact) | MT6 |
| 12 | Saatva (HNN $515.0M; 29 viewing rooms) | not found (site states founding in 2010, not an owner) | not found | none found | not found | — | online plus viewing rooms; made to order | **yes**: "Affiliate sign up" footer link to https://join.partnerize.com/saatva/en (Partnerize) | MT12 |
| 13 | Avocado Green Mattress (HNN Avocado Green Brands $410.0M; 14 stores) | not found | not found | none found | not found | — | online plus stores | **yes**: https://www.avocadogreenmattress.com/affiliate-program (via Impact) | MT13 |
| 14 | Brentwood Home (same basis) | not found (Avocado Green Brands per HNN) | not found | none found | not found | — | online | **yes**: https://www.brentwoodhome.com/pages/partner-with-us | MT13 |
| 15 | Mattress Warehouse (HNN $395.0M; 531 stores incl. Sleep Outfitters) | Mattress Warehouse, LLC; Wynnchurch Capital "growth investment" (stake not stated) | PE-owned (no stated stake) | Wynnchurch Capital | December 2021 (sponsor page; release dated 2022-01-18) | — | company stores (not sourced as company-owned vs franchised) | **yes**: https://mattresswarehouse.com/affiliate-program (via Rakuten) | MT15 |
| 16 | Sleep Outfitters (same basis; 103 stores bought) | MW SO Holdings Company, LLC ("Mattress Warehouse") | PE-owned (via Mattress Warehouse) | Wynnchurch Capital | 2025-05-01 | — | specialty mattress stores | yes (shared Mattress Warehouse program; sleepoutfitters.com shows no link) | MT15 |
| 17 | Casper (HNN $293.5M; 40 stores) | Carpenter Co. ("has become a subsidiary of Carpenter Co."); Carpenter's owner not stated | owner type not confirmed; formerly PE (Durational, 2022–2024) | none current (Durational Capital Management from 2022-01-25) | 2024-11-07 (release date) | — | online plus retail partners and stores | none found (directories describe a referral scheme) | MT17 |
| 18 | Purple (HNN $251.0M; 55 showrooms) | Purple Innovation, Inc.; Coliseum Capital Management holds 49.6% and "exercises substantial control" | public company; controlling holder Coliseum (type for Form ADV check) | Coliseum Capital Management (holder and lender; PE status not confirmed); Somnigroup 6.8% | n/a (IPO not checked) | PRPL | DTC (Purple.com, showrooms) plus wholesale | **yes**: https://purple.com/affiliate-program | MT18 |
| 19 | Tuft & Needle (HNN $154.5M) | Serta Simmons Bedding, LLC; SSB's owners after its 2023 Chapter 11 exit not stated | owner type not confirmed; formerly PE (Advent, trade press) | none confirmed | not found (2018, trade press) | — | online plus retail partners | none found (partners page is brand collaborations) | MT19 |
| 20 | America's Mattress (HNN $148.0M; 96 stores) | not found: stores "independently owned by local entrepreneurs"; owner of the network not stated (HNN calls them Serta Simmons Bedding showrooms) | not found | none found | not found | — | independently owned licensed stores | none found | MT20 |
| 21 | The Original Mattress Factory (HNN $118.0M; 114 showrooms) | The Original Mattress Factory, via its ESOP | other: employee-owned (ESOP) | none | not found (ESOP year not on the pages read) | — | factory-direct company showrooms (12 factories) | none found | MT21 |
| 22 | BedMart (HNN $79.0M; 40 stores) | not found (bedmart.com did not respond) | not found (trade press: family-owned) | none found | not found | — | mattress stores in Oregon, SW Washington, Hawaii (HNN) | not checked (site unreachable) | MT22 |
| 23 | Sierra Sleep (no public figure) | Ashley Furniture Industries ("a privately owned company") | other: private company, owner not stated (no PE evidence) | none | not found | — | mattress-in-a-box sold through Ashley stores and dealers | none found | MT23 |
| 24 | Nectar (no public figure) | Ashley Home, Inc., an affiliate of Ashley Global Retail, LLC (agreement to acquire Resident Home Inc., 2024-03-04) | other: private company, owner not stated | none current (Resident's 2021 investors were growth/VC funds per trade press) | 2024-03 (signing 2024-03-04; closing per trade press 2024-03-07) | — | online plus stores | **yes**: https://www.nectarsleep.com/p/affiliates | MT24 |
| 25 | DreamCloud (no public figure) | Ashley (via Resident Home Inc.), as row 24 | other: private company, owner not stated | none current | 2024-03 | — | online | **yes**: https://www.dreamcloudsleep.com/p/affiliates | MT24 |
| 26 | Serta (no public figure) | Serta Simmons Bedding, LLC; owners after 2023 Chapter 11 not stated | owner type not confirmed; formerly PE (Advent, trade press) | none confirmed | not found | — | wholesale manufacturer (plus licensed America's Mattress stores, per HNN) | none found | MT19 |
| 27 | Beautyrest (no public figure) | Serta Simmons Bedding, LLC | owner type not confirmed | none confirmed | not found | — | wholesale | none found | MT19 |
| 28 | Simmons (no public figure) | Serta Simmons Bedding, LLC | owner type not confirmed | none confirmed | not found | — | wholesale | none found | MT19 |
| 29 | Sleepy's (no public figure; Mattress Firm private label) | Somnigroup International Inc. | public company | none at 5%+ | 2025-02-05 (with Mattress Firm) | SGI | sold only at Mattress Firm and mattressfirm.com | blocked (mattressfirm.com 403) | MT1 |
| 30 | Zinus (no public figure) | "a member of the innovative Hyundai Department Store Group" | other: corporate group (Korean conglomerate) | none | not found | — (listing not sourced) | online and mass retail (not sourced) | none found (network listings only: FlexOffers) | MT30 |

### Evidence
- **MT1 Mattress Firm (and row 29, Sleepy's)**
  - Owner: "and the term "Mattress Firm Acquisition" refers to the acquisition of Mattress Firm which was completed on February 5, 2025." — [Somnigroup International Inc., Form 10-K FY2025, filed 2026-02-27](https://www.sec.gov/Archives/edgar/data/1206264/000120626426000015/sgi-20251231.htm)
  - Since: same sentence (2025-02-05). Name change: "In connection with the closing of the Mattress Firm Acquisition, we amended our Certificate of Incorporation to change our name to "Somnigroup International Inc." effective February 18, 2025." — same 10-K
  - Ticker: "On February 18, 2025, our common stock began trading on the NYSE under the symbol "SGI" in connection with our name change to Somnigroup International Inc." — same 10-K
  - Model: "As of December 31, 2025, Somnigroup operated 2,852 company-owned stores, including 2,174 Mattress Firm stores, Tempur Sealy owned stores, Dreams stores and joint venture stores." and "Our direct channel is led by over 2,100 Mattress Firm retail stores and e-commerce in the U.S." — same 10-K
  - Sleepy's: "• Sleepy's ® - The Sleepy's brand is our private label brand offering at our Mattress Firm stores and online at www.mattressfirm.com." — same 10-K
  - 5% holders: "FMR LLC 245 Summer Street Boston, MA 02210 29,677,438 (1) 14.11 %", "The Vanguard Group 100 Vanguard Blvd. Malvern, PA 19355 15,924,287 (2) 7.57 %" and "BlackRock, Inc. 55 East 52nd Street New York, NY 10055 14,588,476 (3) 6.94 %" — [Somnigroup, DEF 14A, filed 2026-03-31](https://www.sec.gov/Archives/edgar/data/1206264/000120626426000035/sgi-20260330.htm)
  - Affiliate: blocked. mattressfirm.com returned HTTP 403 to the homepage request (its robots.txt allows `*`).
  - BDC names: "Somnigroup International Inc.", "Tempur Sealy International, Inc.", "Mattress Firm, Inc.", "Mattress Firm Group Inc."
  - Notes: 2026 event: "On August 26, 2026, Somnigroup International Inc., a Delaware corporation (the "Company") and Sparrow Unity Corporation, a Missouri corporation and a direct, wholly owned subsidiary of the Company ("Merger Sub"), consummated the previously announced acquisition of Leggett & Platt, Incorporated" — [Somnigroup, Form 8-K, filed 2026-08-26](https://www.sec.gov/Archives/edgar/data/1206264/000120626426000121/sgi-20260826.htm). Leggett is a components supplier, so it goes in the "not brands" list.
- **MT2 Tempur-Pedic, Sealy, Stearns & Foster**
  - Owner: "Our portfolio of product brands includes many highly recognized brands, including Tempur-Pedic®, Sealy® and Stearns & Foster®, which are described below:" — [Somnigroup, Form 10-K FY2025, filed 2026-02-27](https://www.sec.gov/Archives/edgar/data/1206264/000120626426000015/sgi-20251231.htm)
  - Since: not checked (Tempur-Pedic is native to the parent; the Sealy acquisition date was not checked)
  - Model: "The Tempur Sealy North America and Tempur Sealy International segments sell products through two channels: Direct and Wholesale." and "Our Wholesale channel includes sales of product to third-party retailers, hospitality businesses and healthcare customers." — same 10-K
  - Ranking figure: "Tempur Sealy North America net sales decreased $1,087.7 million, or 28.7%." — same 10-K. The segment table lists Tempur Sealy North America gross profit 1,383.8 at 51.2%, which implies about $2,703M of 2025 net sales.
  - 5% holders: as MT1.
  - Affiliate: none found. The tempurpedic.com, sealy.com and stearnsandfoster.com homepages have no affiliate link.
  - BDC names: as MT1, plus "Sealy Corporation", "Tempur-Pedic International"
- **MT5 Sleep Number**
  - Owner (buyer): "on July 18, 2026, the Company entered into an Amended and Restated Asset Purchase Agreement (the “Amended and Restated Purchase Agreement”) with SNBR, Inc., a wholly-owned subsidiary of Sleep Country Canada Inc. (in such capacity, the “Purchaser”) and Sleep Country Canada Inc. pursuant to which the Purchaser agreed to purchase substantially all of the assets of the Company" — [Sleep Number Corporation, Form 8-K, filed 2026-08-03](https://www.sec.gov/Archives/edgar/data/827187/000095010326011603/dp251018_8k.htm)
  - Since: "On July 31, 2026, the parties consummated and closed the Asset Sale." — same 8-K
  - Bankruptcy: "on June 12, 2026, Sleep Number Corporation (“Sleep Number” or the “Company”) and its subsidiaries (together with Sleep Number, the “Debtors”) filed voluntary petitions for relief" — same 8-K. Price: "increase in the base purchase price payable in cash from $415,000,000 to $529,500,000" — [Form 8-K, filed 2026-07-23](https://www.sec.gov/Archives/edgar/data/827187/000095010326011104/dp250511_8k.htm)
  - Owner of Sleep Country: "pursuant to which 16133258 Canada Inc., a newly-formed and wholly-owned subsidiary of Fairfax Financial Holdings Limited ("Fairfax") acquired all of the issued and outstanding common shares of Sleep Country for C$35.00 in cash per common share." — [Torys LLP, transaction page "Fairfax acquires Sleep Country", October 1, 2024](https://www.torys.com/en/work/2024/07/e7973cfc-6a43-4dad-a818-e358b427c0fe) (law-firm page; the company's own release on newswire.ca returned 403 and sleepcountry.ca is robots-disallowed)
  - Owner kind: "Fairfax Financial Holdings Limited is a holding company which, through its subsidiaries, is primarily engaged in property and casualty insurance and reinsurance and the associated investment management." — [Fairfax, About page, accessed 2026-11-07](https://www.fairfax.ca/about-fairfax/). In the extracted page text the first letter is split from the rest ("F airfax"); the quote above joins it.
  - Model (before the sale): "including our exclusive direct- to-consumer selling in 600 stores and online" — [Sleep Number, Form 10-K FY2025, filed 2026-03-12](https://www.sec.gov/Archives/edgar/data/827187/000082718726000014/snbr-20260103.htm)
  - Affiliate: none found (no affiliate link on the sleepnumber.com homepage)
  - BDC names: "Sleep Number Corporation", "SNBR, Inc.", "Sleep Country Canada Inc.", "Sleep Country Canada Holdings Inc."
  - Notes:
    - The seller deregistered: Form 15-12G filed 2026-08-03; the 25-NSE was filed 2026-07-14.
    - Fairfax's own pages read do not name Sleep Country.
    - Whether the Sleep Number brand and stores continue under Sleep Country was not checked beyond "substantially all of the assets".
    - HNN's 2025-data entry still calls Sleep Number "Publicly held", which was stale by July 2026.
- **MT6 3Z Brands: Brooklyn Bedding, Helix Sleep, Birch, Bear Mattress, Nolah, Leesa**
  - Owner (2021): "(together with its affiliates, “Cerberus”) today announced that one of its affiliates has completed a previously announced series of related transactions through which it has acquired each of Brooklyn Bedding LLC (“Brooklyn Bedding”) and Helix Sleep, Inc." — [Cerberus, press release "Cerberus Completes Acquisition of Brooklyn Bedding and Helix Sleep", October 13, 2021](https://www.cerberus.com/media/cerberus-completes-acquisition-of-brooklyn-bedding-and-helix-sleep/)
  - Owner kind: "Founded in 1992, Cerberus is a global leader in alternative investing with over $55 billion in assets across complementary credit, private equity, and real estate strategies." — same release
  - Since: "October 13, 2021" (same release)
  - Brands (2022): "This new identity follows Brooklyn Bedding and Helix Sleep's 2021 merger in partnership with Cerberus Capital Management and the entity's recent acquisition of Bear Mattress in 2022." and "which includes Helix Sleep, Brooklyn Bedding, Birch, Bear Mattress, and the company's wholesale business." — [Brooklyn Bedding, PR Newswire release "New Corporate Name, 3Z Brands, Unites Portfolio of DTC Mattress Brands Under One Identity" (2022)](https://www.prnewswire.com/news-releases/brooklyn-helix-unveils-new-corporate-identity-3z-brands-301729705.html)
  - Leesa and Nolah: "3Z Brands ("3Z"), a vertically-integrated manufacturer, wholesaler, retailer and direct-to-consumer distributor of award-winning sleep products, today announced the acquisition of Leesa Sleep ("Leesa")." and "In 2021, Brooklyn Bedding and Helix Sleep combined in partnership with Cerberus Capital Management, and within the last year, the platform acquired Bear Mattress and Nolah Sleep" — [Brooklyn Bedding, PR Newswire release "3Z Brands Announces Acquisition of Leesa Sleep", March 15, 2023](https://www.prnewswire.com/news-releases/3z-brands-announces-acquisition-of-leesa-sleep-301772936.html)
  - Current brand list: "Nolah: A Sleep Technology Company Leesa: Meticulously designed, exceptionally comfortable" and "We continue to build a house of exceptional sleep brands backed by our world-class, vertically integrated manufacturing facility based in Arizona." — [3Z Brands, homepage, accessed 2026-11-07](https://www.3zbrands.com/) (the menu lists Helix Sleep, Brooklyn Bedding, Birch, Bear Mattress, Nolah and Leesa)
  - Model: "Each consumer-facing brand, like Helix, Bear, and Brooklyn Bedding, will continue to operate under its current identities, with the 3Z Brands serving as the unifying corporate entity." — 2022 release above
  - Affiliate:
    - Brooklyn Bedding: "Earn a 5% commission on every Brooklyn Bedding Mattress sale made through your referral link." and "A unique URL will be provided for you, via Impact, making earning commissions straightforward." — [Brooklyn Bedding Ambassador Program](https://brooklynbedding.com/pages/ambassador-program)
    - Bear: "Bear manages a select and growing number of exclusive online publishers to help drive traffic to our website." — [Bear Mattress, Partnerships page](https://www.bearmattress.com/pages/partnerships)
    - Leesa: "Sign up for our affiliate program is quick and easy through Impact with applications reviewed within 24 hours." — [Leesa, Affiliates page](https://www.leesa.com/pages/affiliates)
    - Helix: blocked (helixsleep.com returned 403 to robots.txt and the homepage).
    - Birch and Nolah: no affiliate link on their homepages. Nolah has network listings only (FlexOffers, Impact; not opened).
  - BDC names: "3Z Brands", "Brooklyn Bedding LLC", "Helix Sleep, Inc.", "Brooklyn-Helix", "Leesa Sleep", "Bear Mattress"
  - Notes:
    - The last primary statement naming Cerberus is the 2023-03-15 Leesa release, and no stake is stated anywhere. No later sale was found, but Cerberus publishes no fetchable portfolio page, so current status rests on the 2023 release.
    - HNN also names white-label lines Southerland and 40Winks under 3Z. Southerland's December 2024 acquisition is a directory lead only.
- **MT12 Saatva**
  - Owner: not found. "Since its founding in 2010, Saatva has championed sleep as a foundation of well-being." — [Saatva, About us / Our story, accessed 2026-11-07](https://www.saatva.com/about-us). No owner statement on the About page, the homepage or `llms.txt` / `llms-full.txt`.
  - Affiliate: footer link labelled "Affiliate sign up" points to `https://join.partnerize.com/saatva/en` — [saatva.com homepage HTML](https://www.saatva.com/) (Partnerize; the program page itself was not opened)
  - BDC names: "Saatva, Inc.", "Saatva"
  - Notes: search snippets (secondary profiles, not cited) say founder-held and bootstrapped. Four fetches.
- **MT13 Avocado Green Mattress, Brentwood Home**
  - Owner: not found. avocadogreenmattress.com/about-us returned 404. The homepage has no owner statement. Only secondary profiles (not cited) say "privately held".
  - Grouping: "Avocado Green Brands includes Avocado’s organic mattresses, bedding and American-made bed frames and furniture, and Brentwood Home’s mattresses, bedding and yoga products." — [HNN 125, Nos. 26–50](https://homenewsnow.com/blog/2026/06/14/home-news-now-125-furniture-bedding-retailers-2025-nos-26-50/) (trade press; grouping only, not an owner fact)
  - Affiliate (Avocado): "Does my site qualify for the Avocado Affiliate Program?" and "When you log in to your Impact control panel, you’ll have full access to all of your performance and financial metrics at a glance." — [Avocado, Become an Affiliate](https://www.avocadogreenmattress.com/affiliate-program)
  - Affiliate (Brentwood Home): "You want to earn commissions by referring your audiences to our eco-luxury products." and "Affiliates are often media partners, product reviewers, or brand ambassadors." — [Brentwood Home, Partner With Us](https://www.brentwoodhome.com/pages/partner-with-us)
  - BDC names: "Avocado Green Brands", "Avocado Mattress LLC", "Brentwood Home"
- **MT15 Mattress Warehouse, Sleep Outfitters**
  - Owner: "a leading middle market private equity firm, announced that it has made a strategic, growth investment in Mattress Warehouse, LLC" — [Wynnchurch Capital, news release "Wynnchurch Capital Makes Growth Investment in Mattress Warehouse", January 18, 2022](https://www.wynnchurch.com/news/wynnchurch-capital-makes-growth-investment-in-mattress-warehouse)
  - Current: "Wynnchurch invested in Mattress Warehouse in December 2021." and "Wynnchurch and management are driving growth at Mattress Warehouse by increasing store count, partnering with direct-to-consumer brands, and enhancing digital and omnichannel capabilities." — [Wynnchurch, portfolio page "Mattress Warehouse", accessed 2026-11-07](https://www.wynnchurch.com/portfolio/mattress-warehouse) (the page shows no realized or exited status; it sits in the current portfolio grid)
  - Company's own release: "Today, the company added another milestone with an investment from Wynnchurch Capital." — [Mattress Warehouse press center, "Wynnchurch Capital to Invest in Mattress Warehouse", January 18, 2022](https://mattresswarehouse.com/blogs/mattress-warehouse-press-center/wynnchurch-capital-to-invest-in-mattress-warehouse-growth-strategy)
  - Sleep Outfitters: "On May 1, 2025, we completed the previously announced divestiture of 73 Mattress Firm retail locations and our Sleep Outfitters subsidiary, which included 103 specialty mattress retail locations and seven distribution centers to MW SO Holdings Company, LLC ("Mattress Warehouse")." — [Somnigroup, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1206264/000120626426000015/sgi-20251231.htm)
  - Affiliate: "When a user clicks on one of those links, they will be brought to our website and their activity will be tracked by the Rakuten platform." — [Mattress Warehouse, Affiliate Program](https://mattresswarehouse.com/affiliate-program). The page header shows both banners ("Mattress Warehouse Sleep Outfitters").
  - BDC names: "Mattress Warehouse, LLC", "MW SO Holdings Company, LLC", "Sleep Outfitters USA"
  - Notes: date framing differs. The sponsor page says the investment was in December 2021, while the release is dated January 17 (page header) and January 18, 2022 (dateline).
- **MT17 Casper**
  - Owner: "Casper Sleep Inc., which has one of the best-known brands in the bedding category and is recognized as the leader in the bed-in-a-box e-commerce category, has become a subsidiary of Carpenter Co." — [Carpenter Co., news "Casper Sleep Inc. to operate as subsidiary of Carpenter Co.", Published: November 7, 2024](https://carpenter.com/2024/11/casper-sleep-inc-to-operate-as-subsidiary-of-carpenter-co/)
  - Owner kind: "Founded in 1950, Carpenter Co. is the world’s largest vertically integrated manufacturer of polyurethane foams." — same page. Carpenter's About and History pages name founder E. Rhodes Carpenter but state no current owner.
  - Former PE owner: "(“Casper” or the “Company”) today announced that its all-cash acquisition by Durational Capital Management, LP (“Durational”) has been completed." — [Casper Sleep Inc., Form 8-K, Exhibit 99.1, filed 2022-01-25](https://www.sec.gov/Archives/edgar/data/1598674/000114036122002541/brhc10033043_ex99-1.htm)
  - Affiliate: none found (no affiliate link on the casper.com homepage; directories describe a gift-card referral scheme)
  - BDC names: "Casper Sleep Inc.", "Marlin Parent, Inc.", "Carpenter Co."
  - Notes: whether Carpenter bought Casper from Durational, and on what terms, is not stated in the pages read.
- **MT18 Purple**
  - Owner: "Our Common Stock is listed on NASDAQ under the symbol “PRPL”." — [Purple Innovation, Inc., Form 10-K FY2025, filed 2026-03-31](https://www.sec.gov/Archives/edgar/data/1643953/000121390026036974/ea0274767-10k_purple.htm)
  - Controlling holder: "Coliseum Capital Management, LLC (“Coliseum”) is our largest stockholder and Lender, and exercises substantial control over our Board of Directors (“Board”) composition, management team members and strategies." — same 10-K
  - 5% holders: "Coliseum (2) 61,131,909 49.6 % Somnigroup International, Inc. (3) 8,000,000 6.8 %" — [Purple, DEF 14A, filed 2026-04-22](https://www.sec.gov/Archives/edgar/data/1643953/000121390026046358/ea0285773-01.htm) (Coliseum's count includes 14.2 million warrant shares, per the 10-K: "Coliseum beneficially owns 61.1 million shares of Common Stock (which includes 46.9 million shares of Common Stock currently owned and 14.2 million shares of Common Stock that could be acquired upon exercise of its warrants).")
  - Model: "We market and sell our products via our direct-to-consumer channel, which includes Purple.com (our direct-to-consumer e-commerce), Purple showrooms, our customer contact center and online marketplaces (collectively “DTC”), and our wholesale channel through retail brick-and-mortar and online wholesale partners." — same 10-K
  - Affiliate: "Nothing compares to Purple — or our affiliate program" and "For individual creators and influencers, earn a competitive commission for sales generated through your unique attribution link." — [Purple, Affiliate Program](https://purple.com/affiliate-program)
  - BDC names: "Purple Innovation, Inc.", "Purple Innovation, LLC", "Intellibed"
  - Notes:
    - Coliseum is also Purple's term lender: "with Coliseum Capital Partners (“CCP”) and other lenders" (same 10-K).
    - Purple filed several Item 3.01 (listing-standard) 8-Ks in 2025–26; not checked further.
    - **For the assembler:** Coliseum's Form ADV `Any PE Funds` decides whether this row is PE (controlled) or stays public.
- **MT19 Serta Simmons Bedding: Tuft & Needle, Serta, Beautyrest, Simmons**
  - Owner (brands): "We are one of North America’s largest bedding manufacturers, the company behind the Serta®, Beautyrest®, Simmons®, and Tuft & Needle® brands." — [Serta Simmons Bedding, Brands page, accessed 2026-11-07](https://www.sertasimmons.com/brands/)
  - SSB's own owners: not stated. "Serta Simmons Bedding, LLC (“SSB” or the “company”), a leading global sleep company, today announced that it has concluded its financial restructuring and emerged from Chapter 11, marking the completion of a critical step in the company’s turnaround effort." and "As SSB emerges from Chapter 11, a new Board of Directors has been appointed to oversee the company." — [SSB, release, June 29, 2023](https://www.sertasimmons.com/news/serta-simmons-bedding-completes-financial-restructuring-emerges-chapter-11/). The release names the chair, "Established private equity investor Mark Genender (Managing Partner, Bristol Growth Capital, LLC)", but not the shareholders.
  - Before the restructuring: "as well as a majority of SSB’s existing equity holders (the “consenting equity”)." and "Ropes and Gray LLP is serving as legal counsel to Advent International Corporation." — [SSB, release, Jan. 23, 2023](https://www.sertasimmons.com/news/serta-simmons-bedding-takes-decisive-actions-strengthen-financial-position-drive-long-term-growth/)
  - Since: not found (Tuft & Needle joined SSB in 2018 per trade press)
  - Affiliate: none found. The tuftandneedle.com "partners" page covers brand collaborations, not commissions. serta.com and beautyrest.com homepages have no affiliate link.
  - BDC names: "Serta Simmons Bedding, LLC", "Serta Simmons Bedding", "SSB", "Tuft & Needle, LLC", "Simmons Bedding Company", "National Bedding Company"
  - Notes:
    - The equity split after the plan is in the court record (Kroll site ssbrestructuring.com), which was not read: no PDF tool was available, and the per-row cap was reached at 6 fetches.
    - Trade press (not cited) says priority lenders took the equity and that Advent held a majority from 2012.
    - In July 2026, SSB bought Dormae Products' Serta licensee assets (trade press).
- **MT20 America's Mattress**
  - Owner: not found. "Every one of our stores is independently owned by local entrepreneurs and staffed by sleep experts who send their kids to the same schools, cheer for the same teams, and show up for the same community events as you." — [America's Mattress, About page](https://www.americasmattress.com/about-Americas-Mattress). The page does not say who owns the network or brand.
  - Lead (trade press, not cited): HNN calls the stores "Independently-owned and operated Serta Simmons Bedding showrooms".
  - Affiliate: none found
  - BDC names: "America's Mattress"
- **MT21 The Original Mattress Factory**
  - Owner: "Thanks to our employee stock ownership plan (ESOP), The Original Mattress Factory is an employee-owned operation." — [The Original Mattress Factory, "Why We Choose OMF"](https://www.originalmattress.com/why-we-choose-omf)
  - Model: "The Original Mattress Factory currently has 12 factories, over 100 showrooms and more than 400 employees." — [OMF, Timeline](https://www.originalmattress.com/time-line)
  - Affiliate: none found
  - BDC names: "The Original Mattress Factory, Inc."
- **MT22 BedMart**
  - Owner: not found. www.bedmart.com gave no response to robots.txt or the homepage. Trade press (not cited) says it is family-owned and that its parent "Sleep Smart NW" also runs America's Mattress stores.
  - Affiliate: not checked (site unreachable)
  - BDC names: "BedMart", "Sleep Smart NW"
- **MT23 Sierra Sleep (Ashley)**
  - Owner: "Ashley Furniture Industries is a privately owned company." — [Ashley Furniture Industries, FAQ](https://www.ashleyfurnitureindustriesllc.com/about-ashley/faq/)
  - Brand: "Sierra Sleep Mattress-in-a-Box Designs for Easy Delivery & Setup" — [Ashley, Our Products / Ashley Family of Brands](https://www.ashleyfurnitureindustriesllc.com/our-products/)
  - Model: "All Ashley stores are independently owned and operated." — FAQ above
  - Affiliate: none found (no affiliate link on the ashleyfurniture.com homepage)
  - BDC names: "Ashley Furniture Industries, LLC", "Ashley Global Retail, LLC"
- **MT24 Nectar, DreamCloud**
  - Owner: "Ashley Home, Inc. and Resident Home Inc. today announced the signing of an agreement, under which Ashley Home, Inc., an affiliate of Ashley Global Retail, LLC (collectively, “Ashley”), will acquire Resident Home Inc." — [Ashley, release "Ashley and Resident Announce Acquisition", March 4, 2024](https://www.ashleyfurnitureindustriesllc.com/?p=752)
  - Brands: "Through its award-winning Nectar®, DreamCloud®, Awara™, and Siena™ brands, Resident has established itself as a leading online seller of mattresses and bedding accessories." — same release
  - Owner kind: Ashley, "a privately owned company" (MT23)
  - Since: signing on 2024-03-04 (primary). Closing reported 2024-03-07 by HNN (trade press, not cited). No primary closing statement was read.
  - Affiliate: Nectar has [/p/affiliates](https://www.nectarsleep.com/p/affiliates), page title "Affiliates | Nectar Sleep". DreamCloud has [/p/affiliates](https://www.dreamcloudsleep.com/p/affiliates), page title "Become Our Affiliate - Join Our Team In $15 Billion Mattress Industry | DreamCloud". Both footers list "Affiliate Program". The body text is rendered by script, so the network was not read.
  - BDC names: "Resident Home Inc.", "Resident Home, LLC", "Ashley Home, Inc."
- **MT30 Zinus**
  - Owner: "Zinus is a member of the innovative Hyundai Department Store Group, known around the world for Hyundai Motors." and "Founded in 1971, the Hyundai Department Store Group offers a diverse range of products and services that enrich our lives." — [Zinus, About Us](https://www.zinus.com/pages/about-us)
  - Since / ticker: not found (Zinus's own Korean listing and the 2023 deal were not checked)
  - Affiliate: none found on the brand site; network listings only (FlexOffers, PostAffiliatePro; not opened)
  - BDC names: "Zinus, Inc.", "Zinus"

### Rollups and groups that are not brands
Not counted in the list. Each groups brands or locations under a name that consumers don't see on the product.
- **Somnigroup International Inc.** (formerly Tempur Sealy International): parent of Tempur-Pedic, Sealy, Stearns & Foster, Mattress Firm and Sleepy's. Public (NYSE: SGI), with no PE holder at 5%+ (MT1).
- **Leggett & Platt, Incorporated:** bedding-components supplier (springs, foam); a wholly owned Somnigroup subsidiary since 2026-08-26 (MT1).
- **Serta Simmons Bedding, LLC:** parent of Serta, Beautyrest, Simmons and Tuft & Needle. Owners after 2023 not stated (MT19).
- **3Z Brands** (formerly Brooklyn-Helix): parent of six DTC brands plus the white-label lines Southerland and 40Winks. Owner: Cerberus affiliate (MT6).
- **Avocado Green Brands:** parent of Avocado and Brentwood Home. Owner not found (MT13).
- **Resident Home Inc.:** parent of Nectar, DreamCloud, Awara and Siena. Owner: Ashley Home, Inc. (MT24).
- **Ashley Home, Inc. / Ashley Global Retail, LLC / Ashley Furniture Industries:** "a privately owned company" (MT23).
- **MW SO Holdings Company, LLC:** Mattress Warehouse's holding company for the 2025 Sleep Outfitters purchase. Owner: Wynnchurch Capital (MT15).
- **Sleep Country Canada Inc. / SNBR, Inc. / 16133258 Canada Inc.:** Sleep Number's buyer and its Fairfax holding chain (MT5).
- **Carpenter Co.:** foam manufacturer, parent of Casper. Owner not stated (MT17).
- **Corsicana Mattress Company** (moved here from the brand list): its site says "Corsicana offers a range of sleep brands created to support different consumers, price points, and retail strategies." and "Whether through established brands, private label programs, or custom solutions, we collaborate closely with our partners to bring smart, reliable sleep products to market." ([Corsicana, About Us](https://corsicanabedding.com/pages/about-us)). Owner not found. Trade-press leads, not cited: Blue Torch Finance bought it in a 2022 Chapter 11 sale; Fenway Partners (2014) and Long Point Capital (2016) owned it before.
- **Hyundai Department Store Group:** Zinus's group (MT30).
- **Sleep Smart NW:** BedMart's parent per trade press, which also runs America's Mattress stores (MT22).

### Category share
**Ranked rows (N = 30, composite):**
- **PE-owned (control, or no stated stake): 8 / 30 = 26.7%**
  - 3Z Brands / Cerberus (6): Brooklyn Bedding, Helix Sleep, Birch, Bear Mattress, Nolah, Leesa. No stake stated; the last primary statement naming Cerberus is from 2023.
  - Wynnchurch Capital (2): Mattress Warehouse and Sleep Outfitters. A "growth investment" with no stake stated; the sponsor page reads as current.
- **PE minority stake: 0.** PE-owned plus minority = **8 / 30 = 26.7%.**
- **Public company: 6 / 30 = 20.0%.**
  - Somnigroup (5): Mattress Firm, Tempur-Pedic, Sealy, Stearns & Foster, Sleepy's. Its 5%+ holders are FMR, Vanguard and BlackRock.
  - Purple (1): Coliseum holds 49.6% and "exercises substantial control".
- **Other: 6 / 30 = 20.0%**
  - insurance holding company: 1 (Sleep Number, via Sleep Country Canada and Fairfax)
  - private company, "privately owned", owner not stated: 3 (Ashley's Sierra Sleep, Nectar, DreamCloud)
  - employee-owned (ESOP): 1 (The Original Mattress Factory)
  - corporate group: 1 (Zinus, Hyundai Department Store Group)
- **Not found or owner type not confirmed: 10 / 30 = 33.3%**
  - parent known, its owners not stated: Serta, Beautyrest, Simmons, Tuft & Needle (SSB) and Casper (Carpenter Co.)
  - owner not found: Saatva, Avocado Green Mattress, Brentwood Home, America's Mattress, BedMart
- **Rows with owner kind settled:** 20 / 30 (67%).
- **Strict count:** 8 / 30 now. **9 / 30 (30.0%) if Coliseum Capital Management's Form ADV reports PE funds.** Because Coliseum's position is described as "substantial control", Purple would then count as PE-owned rather than as a minority stake. Somnigroup's holders (FMR LLC, The Vanguard Group, BlackRock, Inc.) are expected to be unflagged; that is for the assembler to confirm.
- **By parent company:** 14 parents. America's Mattress and BedMart count as their own parents because their owners are unknown. **PE-owned parents: 2 / 14 = 14.3%** (3Z Brands, Mattress Warehouse).
- **By sales:** PE rows' companies hold **$914M of $10,438M = 8.8%**.
  - The sum is each company counted once: Mattress Firm 3,582.0; Tempur Sealy North America ~2,703; Sleep Number 1,270.0; 3Z 519.0; Saatva 515.0; Avocado 410.0; Mattress Warehouse 395.0; Casper 293.5; Purple 251.0; Tuft & Needle 154.5; America's Mattress 148.0; OMF 118.0; BedMart 79.0.
  - Indicative only: the figures mix retail estimates with one wholesale segment, and leave out SSB, Ashley and Resident, and Zinus, which have no public figure.
- **By stores:** PE rows hold **543 of 3,705 stores = 14.7%** (Mattress Warehouse 531 plus Brooklyn Bedding's 12 showrooms; HNN counts).
- **Upper bound if leads were confirmed:**
  - Purple via Coliseum: **9 / 30 (30.0%)**.
  - The four SSB rows would move only if SSB's post-2023 owners include PE firms. Trade press says the priority lenders took the equity, and those lenders are not named in the sources read. All SSB rows plus America's Mattress would make it 14 / 30 at most; there is no evidence for that.
  - No other row has a PE lead. Saatva, Avocado and BedMart leads all say founder or family.
- **Sources disagree:** none on owners. Two framing or date differences:
  - Mattress Warehouse: the sponsor page says December 2021; the releases are dated 2022-01-17/18.
  - HNN's 2025-data list still calls Sleep Number "Publicly held"; the asset sale closed 2026-07-31.
- **Formerly PE among non-PE rows:**
  - Casper: Durational Capital Management, 2022-01-25 to 2024 (SEC 8-K).
  - Serta, Beautyrest, Simmons, Tuft & Needle: Advent International. Advent is named in SSB's 2023 release as a party with counsel; its majority from 2012 is from trade press only.
- **Lender or court-driven ownership changes in this category:**
  - Serta Simmons Bedding: Chapter 11, 2023.
  - Sleep Number: Chapter 11 asset sale, 2026.
  - Corsicana (not a brand row): Chapter 11 sale to Blue Torch, 2022, trade press only.

**Affiliate income:**
- **Brand-direct programs found (10):**
  - Saatva (Partnerize)
  - Leesa (Impact)
  - Bear
  - Brooklyn Bedding (Impact, 5%)
  - Purple
  - Nectar
  - DreamCloud
  - Avocado (Impact)
  - Brentwood Home
  - Mattress Warehouse (Rakuten)
- **Blocked:** Helix (403) and Mattress Firm (403).
- **Network listings only:** Nolah, Zinus, Casper (referral scheme).
- **None found:** Somnigroup's product brands, SSB's brands, Sleep Number, Ashley's Sierra Sleep, OMF, America's Mattress and Sleep Outfitters' own site. Each homepage was checked for an affiliate link, plus two category-wide searches.
- **Overlap with PE:** 4 of the 10 programs are on PE-owned rows (Leesa, Bear and Brooklyn Bedding under Cerberus's 3Z, and Mattress Warehouse under Wynnchurch). Helix, also PE, was blocked. Unlike eyewear, affiliate income and PE ownership overlap here, through the online and DTC tier.

## Firms named
Every investment firm named as an owner or 5%+ holder, as the sources name it (for the assembler's Form ADV check):
- **Cerberus Capital Management, L.P.** ("Cerberus"; "one of its affiliates" acquired Brooklyn Bedding and Helix): 3Z Brands
- **Wynnchurch Capital, L.P.** ("Wynnchurch"): Mattress Warehouse, Sleep Outfitters
- **Coliseum Capital Management, LLC** (49.6% of Purple) and **Coliseum Capital Partners** ("CCP", Purple's lender). Its Form ADV decides the strict count.
- **Fairfax Financial Holdings Limited** (via 16133258 Canada Inc. and Sleep Country Canada Inc.): Sleep Number. Fairfax is an insurance holding company; its investment arm was not checked.
- **Durational Capital Management, LP**: former owner of Casper (2022)
- **Advent International Corporation**: named in SSB's January 2023 release as a represented party (former SSB equity holder per trade press)
- 5%+ holders of public rows: **FMR LLC**, **The Vanguard Group**, **BlackRock, Inc.** (Somnigroup); **Somnigroup International, Inc.** (6.8% of Purple; an operating company, not an investment firm)
- Named but not owners: **Bristol Growth Capital, LLC** (SSB chairman Mark Genender's firm; no ownership stated)
- Leads only, from trade press or directories (not cited, not counted): Blue Torch Finance / Blue Torch Capital, Long Point Capital, Fenway Partners and KKR (Corsicana); Ares Management and Ontario Teachers' Pension Plan (Simmons/Serta, 2009–2012); Ion Crossover Partners, Nexus Capital Management and Baron Capital Group (Resident, 2021 round). SSB's post-2023 lenders and owners are not named in any source read.

## Worker log
- **Time:** start 2026-11-07T16:59:38Z, end about 2026-11-07T17:25Z: about 26 minutes wall-clock for 30 rows, including writing and the quote self-check.
- **Requests:**
  - WebSearch: 28.
  - WebFetch: 0. Every page was read with curl, so quotes come from raw page text, not a summarizer.
  - Direct HTTP (curl): **153 logged requests**, of which 47 were robots.txt reads, 6 were HNN ranking pages and 1 was a HEAD probe.
    - **16 went to SEC:** company tickers ×1, submissions JSON ×3, full-text search ×1, filing index ×1 and documents ×10. All were HTTP 200 under the contact-free user agent at under 2 requests per second.
    - Status mix: 141 × 200, 5 × 403 (beddingnewsnow.com, newswire.ca, helixsleep.com ×2, mattressfirm.com), 4 × 404 (sertasimmons.com robots.txt ×2 and one old URL, avocadogreenmattress.com/about-us), 2 × no response (bedmart.com) and 1 HEAD answered 405.
  - Agent tokens: not metered by this worker.
- **What was fast:**
  - Public parents. One Somnigroup 10-K plus one DEF 14A settled five rows (Mattress Firm, Tempur-Pedic, Sealy, Stearns & Foster, Sleepy's) and the Sleep Outfitters sale.
  - EDGAR settled Sleep Number's 2026 sale in two 8-Ks, and Casper's 2022 take-private in one full-text search plus one exhibit.
  - Sponsor pages rendered on the server: Cerberus's 2021 release settled six 3Z rows together with two 3Z/PR Newswire releases. Wynnchurch's portfolio page settled Mattress Warehouse and Sleep Outfitters.
  - Affiliate checks were cheap: one homepage request per brand, then a grep for affiliate links.
- **What made brands slow:**
  1. **No usable ranking.** Furniture Today's bedding-producer list is robots-disallowed (and its newest free edition is 2021). Bedding News Now returned 403. HNN ranks retailers, so wholesale brands had to be added from a 10-K or left without a figure. Building the composite took 8 searches and 9 requests.
  2. **Owners hidden by restructuring.** Serta Simmons Bedding's 2023 Chapter 11 releases name the new board but not the new shareholders; the plan sits in a court-records PDF. Sleep Number changed hands in July 2026, after the ranking's data year.
  3. **Founder-held DTC brands state their founding but never their owner:** Saatva and Avocado.
  4. **Parent chains that stop at a private company with no ownership statement:** Carpenter Co. (Casper) and Sleep Country Canada (robots-disallowed; reached only through a law-firm page).
  5. **Bot walls:** helixsleep.com, mattressfirm.com, newswire.ca and beddingnewsnow.com (403); bedmart.com gave no response.
- **Which kinds of brands had no primary source for the owner:**
  - founder-held direct-to-consumer brands (Saatva, Avocado Green Mattress, Brentwood Home);
  - brands whose parent left Chapter 11 owned by unnamed lenders (Serta, Beautyrest, Simmons, Tuft & Needle);
  - licensed store networks whose sites describe independently owned stores, not the brand owner (America's Mattress);
  - regional family chains with an unreachable site (BedMart);
  - brands owned by a private manufacturer with no ownership statement (Casper / Carpenter Co.).
- **Notes for the assembler:**
  - **Script-rendered pages:**
    - Nectar's and DreamCloud's /p/affiliates pages render their body by script. Only the `<title>` text ("Affiliates | Nectar Sleep"; "Become Our Affiliate - Join Our Team In $15 Billion Mattress Industry | DreamCloud") and the footer link "Affiliate Program" are in the HTML.
    - Saatva's affiliate evidence is a footer link (`data-selector="link-Affiliate sign up"`) in the HTML, not a page sentence.
  - **Table-cell quotes** (Somnigroup and Purple 5% rows, the HNN rank rows) are page text with whitespace collapsed. The Purple row reads "Coliseum (2) 61,131,909 49.6 %".
  - **Odd spacing in source text:**
    - the Sleep Number 10-K renders "direct- to-consumer" with a space after the hyphen;
    - Fairfax's About page splits the first letter ("F airfax Financial Holdings Limited");
    - the 2023 3Z/Leesa release has a space before the final period ("Nolah Sleep ."), so the quote stops before it.
  - **3zbrands.com robots:** ClaudeBot and anthropic-ai are listed in the same group as `*`, which disallows only paths such as /config and /search. The homepage is allowed.
  - **cerberus.com robots** sets `Crawl-delay: 10`. The release was fetched straight after robots.txt, without that 10-second wait. Only those 2 requests went to the site.
  - **Self-check:** a script string-matched 99 cited quotes and table cells against the saved page text (tags removed, whitespace collapsed, curly quotes and dashes normalized), and all 99 were found. A negative control of 6 deliberately altered quotes all failed.
  - **BDC leads:**
    - Serta Simmons Bedding (its pre-2023 term loans were widely held; check "Serta Simmons Bedding, LLC");
    - Purple (Coliseum term loan);
    - Sleep Number (DIP and prepetition lenders, 2026);
    - Mattress Firm / Somnigroup;
    - 3Z Brands and Mattress Warehouse (sponsor-backed, any credit facility not checked);
    - Corsicana (Blue Torch, a lender, per trade press).
