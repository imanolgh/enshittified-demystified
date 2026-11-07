# Research: Full category audit (ten categories, assembled)

Ticket: [66-research-full-category-audit](../issues/66-research-full-category-audit.md) · Assembled 2026-11-07, 18:04 to about 18:50 UTC · Method copied from [category-audit-pilot.md](category-audit-pilot.md) · Worker files: [category-audit/](category-audit/)

**Question:** in ten more candidate categories, what share of the top ~30 US brands is owned or backed by private equity today, which brands or parents borrow from public BDCs, and which have brand-direct affiliate programs, counted the same way as the pilot (restaurants, gyms, eyewear)?

**Sources and rules, in one paragraph.** Ownership facts come from the ten worker files, which cite SEC filings, company and sponsor releases, sponsor portfolio pages and company sites; trade press supplied rankings only. The assembler added two SEC data sets: the November 2026 monthly Form ADV adviser files and the DERA BDC data sets `2026_07` to `2026_10`. The assembler re-downloaded every cited URL with curl and string-matched the quotes. Every SEC request used the user agent `EvidenceEngine ownership-research bot (category audit)` with no contact detail, at 0.6 s or more between requests. No competitor site, WhoIsMyDentist, Private Equity Vet, Independent Vet, Reddit, PitchBook, Preqin or CB Insights page was fetched. Owner kinds are research notes for a human, not engine classifications (ADR 0001). Counts are by brand row, as the developer ruled until the counting question is settled. The worker files were not edited.

## Short answer

The first three rows are copied from the pilot's short answer and §1 to §4, unchanged. The other ten are this run, after the Form ADV and BDC passes.

| Category | Rows | Confirmed PE share (PE-owned plus PE minority) | Upper bound | Strict | By parent | By sales or stores | Owner not found | BDC overlap (brand rows) | Brand-direct affiliate programs (on PE rows) | Ranking quality |
|---|---|---|---|---|---|---|---|---|---|---|
| Restaurants (pilot) | 30 | 9 (30.0%) | 10 (33.3%) | 12 (40.0%) | not reported | not reported | 2 | 5 | 0 (0) | sales rank (NRN/Technomic, 2025 sales) |
| Gyms (pilot) | 30 | 9 (30.0%) | 11 (36.7%) | 10 (33.3%) | not reported | not reported | 7 | 12 | 0 (0) | composite (location counts) |
| Eyewear (pilot) | 30 | 4 (13.3%) | 7 (23.3%) | 4 (13.3%) | not reported | 20.5% of top-30 sales | 12 | 4, plus 1 added row | 4 (0) | sales rank (Vision Monday, 2024 sales) |
| Pharmacies | 30 | 1 (3.3%) | 1 (3.3%) | 2 (6.7%) | 1/29 (3.4%); strict 2/29 | 30.7% of the 8 ranked rows' Rx sales; strict 34.6% | 7 | 3 | 2 (1) | composite: 8 by Rx sales, 22 unranked |
| Dollar and discount | 25 (13 core, 12 off-price) | 2 (8.0%); core 1/13 (7.7%) | 2 (8.0%) | 4 (16.0%); core 2/13 (15.4%) | 2/17 (11.8%); core 1/10 | 14.5% of known core sales | 5 | 1 | 0 (0) | composite: 8 by NRF sales, the rest by own store counts |
| Car washes | 30 | 16 (53.3%) | 17 (56.7%) | 16 (53.3%) | 14/28 (50.0%) | 70.5% of sites | 1 | 11 | 0 (0) | unit count (one M&A adviser's list) |
| Pet stores | 26 ranked (+4 online) | 5 (19.2%) | 7 (26.9%) | 5 (19.2%) | 4/24 (16.7%) | 61.0% of locations | 13 | 6, plus Chewy | 2 (1) | composite (location counts) |
| Women's apparel | 32 | 12 (37.5%) | 14 (43.8%) | 12 (37.5%) | 6/22 (27.3%) | not computed | 5 | 8 | 5 (1) | composite (own store counts) |
| Mattresses | 30 | 8 (26.7%) | 9 (30.0%) | 9 (30.0%) | 2/14 (14.3%); strict 3/14 | 8.8% of sales, 14.7% of stores; strict 11.2% and 16.1% | 10 | 6 (11 with the 3Z group) | 10 (4; 5 with Purple) | composite (partly sales; 8 rows unordered) |
| Cookware | 30 (10 ranked) | 4 (13.3%); 3/10 ranked | 4 (13.3%) | 4 (13.3%) | 4/22 (18.2%) | 29.6% of the top 10's Amazon skillet share | 6 | 1 | 10 (1) | composite: 10 by Amazon skillet share, 20 unranked |
| Vitamins and supplements | 30 (+5 added) | 3 (10.0%) | 5 (16.7%) if the Yellow Wood sale closes | 3 (10.0%) | 3/22 (13.6%) | not computed | 3 | 2, plus 2 added rows | 3 (1) | candidate list (no sales rank) |
| Dental chains | 30 | 15 (50.0%) | 19 (63.3%) | 15 (50.0%) | 6/20 (30.0%) | 64.5% of offices | 8 | 22 | 0 (0) | composite (own office counts) |
| Veterinary chains | 21 | 11 (52.4%) | 16 (76.2%) | 11 (52.4%) | 9/16 (56.3%) | 26.3% of fixed-site hospitals | 1 | 6 | 0 (0) | composite (own site counts) |

- **Form ADV changed numbers in six categories.** Car washes rose from 10 to 16 of 30, dollar and discount from 0 to 2 of 25, and the strict counts for pharmacies (Albertsons) and mattresses (Purple) rose by one each. The vet upper bound rose from 14 to 16 of 21, and the women's apparel strict range of 12 to 15 narrowed to 12. Details in §2.
- **BDC overlap in the ten categories:** 66 of 284 brand rows (23.2%), through 43 borrower groups held by 88 BDCs at their latest reported period (mostly 2026-06-30). 45 of the 77 PE-owned or PE-minority rows overlap (58.4%). Dental is the extreme: 22 of 30 rows. Details in §3.
- **Quote check:** 1,022 quoted strings and HTML fields in the Evidence and rollup sections. 943 matched the re-downloaded page text, 25 matched raw HTML, 5 matched a worker's saved copy, 48 could not be checked, and 1 failed (car washes, CW10). A negative control of 29 altered quotes failed 29 of 29. Another 54 quoted strings are the workers' own labels or field names, not page quotes, and are left out. Details in §4.
- **Cost:** the ten workers used 3,419,427 agent tokens, about 342k per category against the pilot's 260k to 280k. The assembler took about 46 minutes and about 800 HTTP requests. Details in §6.

## How this was assembled (read first)

**Inputs**
- **Worker files:** the ten files in [category-audit/](category-audit/). A script pulled each row's Evidence lines (URL and quoted text), the "BDC names" lines (429 name variants) and the "Firms named" lists. The scripts and downloaded data are in the session scratchpad, not the repo.
- **Form ADV:** the SEC's monthly adviser files for November 2026, [`ia110226-registered.zip` and `ia11022026-exempt.zip`](https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers), downloaded 2026-11-07. They are the same month the pilot used; no later month was posted. The fields read are `Any PE Funds`, `Total number of PE funds`, `Any VC Funds`, `Firm Type`, `Organization CRD#`, `Latest ADV Filing Date` and `Website Address`.
- **DERA BDC data sets:** [`2026_07` to `2026_10`](https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets), downloaded 2026-11-07; `2026_10` is still the latest posted. Their `soi.tsv` files hold 175 BDCs, 174 of them with holdings dated 2026-06-30 (98,631 rows on that date). The pilot reported 173, 172 and 147,678 for the same four files; the difference was not investigated.

**How the Form ADV results were read**
- The project's ruling (engine "Owner kind", 2026-11-07): `Any PE Funds = Y` marks a PE firm even if it calls itself something else, and `N` proves nothing, because an affiliated adviser may report the funds.
- **Match** means the adviser's legal or business name is the firm's name as the worker's source states it, or the adviser's `Website Address` is the domain the worker cited for that firm.
- **Name match only** means the name resembles the firm but nothing ties that CRD to the deal.
- **Not found** means no adviser by that name is in either file. Absence does not mean "not PE": a firm can file under another name, be state-registered, be a family office or a pension, or file nothing.
- **Large index and asset managers are not counted in the strict rule**, as in the pilot. This matters because several of them have an adviser entity that reports PE funds (BlackRock, FMR, J.P. Morgan, State Street, T. Rowe Price). See question 4 in §7.

**How the BDC overlap was read** (pilot §6 rules)
- About 230 regex patterns were built from the workers' name variants and leads, plus broad category terms ("car wash", "dental", "veterinar" and so on). They were searched in every `soi.tsv` column that holds an identifier, issuer, investee or investment name.
- A brand counts only when the filer's text ties the borrower to it: the brand's own name in the borrower's name ("Club Car Wash Operating, LLC"), a filer's label ("Express Wash Acquisition Company, LLC (Whistle)"), or an exact legal name that the brand's sources use ("Blazing Star Parent, LLC").
- "Current" means the BDC still reports the holding at its latest period (2026-05-31 or later). Holdings that appear only in a prior-period column (2025-09-30 or 2025-12-31) are listed separately.

## 1. Results by category

Each paragraph gives the numbers after the Form ADV and BDC passes, then one line per change from the worker's number.

**Pharmacies** ([pharmacies.md](category-audit/pharmacies.md))
- **List:** 30 rows. 8 are the retail entries in Drug Channels Institute's 2025 prescription-revenue ranking. The other 22 are franchise networks and regional grocers in no ranked order, because fewer than 30 national drugstore chains exist.
- **PE share:** Walgreens is the only PE-owned row: Sycamore Partners took it private on 2025-08-28. That is 1 of 30 rows (3.3%) but 30.7% of the eight ranked rows' prescription revenue.
- **Strict count:** Cerberus Capital Management, L.P. reports PE funds. Albertsons (Cerberus 31.0%) therefore counts under the strict rule: 2 of 30 (6.7%), and 34.6% of ranked revenue.
- **Owner not found:** 7, mostly family grocers whose sites block bots.
- **BDC overlap:** Walgreens (Blazing Star Parent, LLC, 11 BDCs), and Tops and Price Chopper/Market 32 (Northeast Grocery Inc, Great Elm Capital Corp).
- **Affiliate programs:** Walgreens (CJ) and Walmart (store-wide).
- **Change:** the strict count is confirmed at 2/30 (Cerberus `Any PE Funds = Y`, 9 PE funds). The worker had left it pending.

**Dollar and discount** ([dollar-discount.md](category-audit/dollar-discount.md))
- **List:** 13 core dollar, variety and closeout brands plus 12 off-price rows, 25 in all.
- **Family Dollar:** Brigade Capital Management, LP reports PE funds (2). It is a named buyer of Family Dollar, with Macellum (not in the files), so Family Dollar counts as PE-owned since 2025-07-05. That is core 1/13 (7.7%), 14.5% of known core sales.
- **Gabe's:** majority-owned since 2025-08-25 by a lender group of Brigade, Arbour Lane (Y, 3 PE funds) and Anchorage (N). It counts as PE-owned too, which makes 2/25 (8.0%) for all rows. It is a lender takeover; question 6 in §7 asks how such rows should read.
- **Strict count:** Summit Trail Advisors, LLC (Ollie's, 5.62%, Y with 8 PE funds) and Pleasant Lake Partners LLC (the adviser behind Fund 1's 31.1% of Citi Trends, Y with 1) make two PE minority stakes. That is core 2/13 (15.4%) and all rows 4/25 (16.0%). Mantle Ridge (Dollar Tree) reports no PE funds.
- **BDC overlap:** Family Dollar only, as 1959 Holdings, LLC at three BDCs.
- **Affiliate programs:** none.
- **Change:** confirmed rose from 0/13 to 1/13 and from 0/25 to 2/25 (Brigade Y, Arbour Lane Y).
- **Change:** the strict upper bound fell from 3/13 to 2/13 and from 6/25 to 4/25 (Mantle Ridge N, Kayne Anderson Rudnick N, Divisadero N). Burlington's JPMorgan and Capital International holdings are not counted, as in the pilot.

**Car washes** ([car-washes.md](category-audit/car-washes.md))
- **List:** 30 brand rows, ranked by site count on Car Wash Advisory's list (an M&A adviser, May 2026 data). Rollups were replaced by their brands.
- **PE share:** 16 of 30 (53.3%), on 70.5% of the 4,472 sites.
- **Strict count:** the same, because no public company is left. Mister Car Wash went private on 2026-05-19.
- **Upper bound:** 17/30 (56.7%). It adds LUV, whose owner Susquehanna Private Capital is in neither adviser file.
- **Owner not found:** 1 (Sam's Xpress), plus 6 private chains whose owner is not stated.
- **BDC overlap:** 11 rows: Whistle, Mister, Quick Quack, Club Car Wash, GO, WhiteWater, Cobblestone, Flagship, LUV, Clean Express and BlueWave. A "Splash Car Wash, Inc." borrower that the filers don't tie to either Splash row is listed separately.
- **Affiliate programs:** none.
- **Change:** confirmed rose from 10/30 to 16/30. Four owners report PE funds:
  - Freeman Spogli Management Co., L.P. (Y, 7): WhiteWater.
  - Access Holdings Management Company LLC (Y, 27): Cobblestone and Flagship.
  - Point72 Asset Management, L.P. (Y, 4): Tsunami.
  - Wildcat Capital Management, LLC (Y, 3), a family office that reports PE funds: Club Car Wash and Clean Express.
- **Change:** by parent rose from 10/28 to 14/28 (50.0%), and by sites from 54.0% to 70.5%.

**Pet stores** ([pet-stores.md](category-audit/pet-stores.md))
- **List:** 26 ranked store chains (a composite by location count, because fewer than 30 were found), plus 4 online-first rows.
- **PE share:** 5 of 26 (19.2%), on 61.0% of ranked locations:
  - PetSmart (BC Partners);
  - Petco and Unleashed (CVC, CPP Investments);
  - Woof Gang (Garnett Station, Great Hill);
  - Pet Food Express (Rainier Partners). Rainier Capital Partners LP reports PE funds (3) and lists rainierpartners.com, the site the worker cited, as its website.
- **With Chewy (BC Partners):** 6/30 (20.0%).
- **Upper bound:** 7/26 (26.9%), if Healthy Spot's directory lead (Monogram Capital, Y) holds and Pet Supermarket's unknown post-Roark owner is PE.
- **Owner not found:** 13 (50.0%).
- **BDC overlap:**
  - PetSmart (5 BDCs);
  - Petco and Unleashed (2);
  - Pet Supplies Plus and Wag N' Wash: Fusion Parent, LLC common stock and membership units at BCP Investment Corp;
  - Hollywood Feed (Fortress Private Lending Fund);
  - Chewy (Blackstone Private Credit Fund).
- **Affiliate programs:** Chewy, a PE-controlled row, and 1-800-PetMeds.
- **Change:** none.

**Women's apparel** ([womens-apparel.md](category-audit/womens-apparel.md))
- **List:** 32 rows, a composite of brands' own store counts plus 6 online brands.
- **PE share:** 12 of 32 (37.5%). All five owners report PE funds:
  - Sycamore controls Torrid and seven KnitWell brands;
  - Summit Partners controls Princess Polly, and Permira controls Reformation;
  - TowerBrook (J.Jill, 49.2%) and H.I.G. (Lulus, 32.1%) hold minorities.
- **Strict count:** stays 12/32. Aldebaran Capital, LLC (Cato, 6.2%) reports no PE funds, and BBRC International (Victoria's Secret) is in neither file.
- **Upper bound:** 14/32 (43.8%). It adds maurices (OpCapita, 2019; not in the files) and Madewell (Anchorage Capital Group, which reports no PE funds; `N` proves nothing).
- **By parent:** 6/22 (27.3%).
- **Owner not found:** 5.
- **BDC overlap:** Torrid (Saratoga) and the seven KnitWell brands (Knitwell Borrower LLC at two HPS BDCs).
- **Affiliate programs:** 5. The one on a PE row is Reformation.
- **Change:** the strict range of 12 to 15 narrows to 12.

**Mattresses** ([mattresses.md](category-audit/mattresses.md))
- **List:** 30 rows, a composite ordered partly by sales: HNN's retail estimates plus one Somnigroup 10-K segment. 8 rows have no figure and are unordered.
- **PE share:** 8 of 30 (26.7%): six 3Z Brands names (Cerberus) plus Mattress Warehouse and Sleep Outfitters (Wynnchurch). Both owners report PE funds. These rows hold 8.8% of sales and 14.7% of stores.
- **Strict count:** Coliseum Capital Management, LLC reports PE funds (2). Its 49.6% of Purple "exercises substantial control", so the strict count is 9/30 (30.0%), 11.2% of sales and 16.1% of stores.
- **Not found or owner type not confirmed:** 10, including the four Serta Simmons Bedding rows.
- **BDC overlap:**
  - Helix Sleep, Inc. at three TCW BDCs. The other five 3Z brands belong to the same group.
  - Saatva, as Whitestone Home Furnishings, LLC (d/b/a Saatva, Inc.), at WhiteHorse Finance.
  - Serta Simmons Bedding LLC common stock at two Barings BDCs, so lenders hold the equity.
- **Affiliate programs:** 10, of which 4 are on PE rows (5 counting Purple).
- **Change:** the strict count, pending in the worker's file, is now 9/30.

**Cookware** ([cookware.md](category-audit/cookware.md))
- **List:** 30 rows: 10 ranked by Amazon US skillet share (from a vendor blog) and 20 unranked candidates.
- **PE share:** 4 of 30 (13.3%), and 3 of the 10 ranked rows: Cuisinart (American Securities), Martha Stewart (Marquee Brands, Neuberger Berman), Caraway (M-One Capital) and Made In (KarpReilly). All four owners report PE funds. The ranked PE rows hold 29.6% of the top 10's skillet share.
- **Strict count:** unchanged. RWWM, Pzena, Appaloosa and PRIMECAP report no PE funds.
- **Owner not found:** 6, plus 11 private makers whose owner is not stated.
- **BDC overlap:** Cuisinart only: Conair Holdings LLC loans and ASP Conair Holdings LP units at four BDCs.
- **Affiliate programs:** 10. The one on a PE row is Caraway.
- **Name-only lead:** a directory lists Misen's investor as "Vanterra Ventures". It matches Vanterra Capital LLC (Y) by name only, so Misen is not added to the upper bound.
- **Change:** none.

**Vitamins and supplements** ([supplements.md](category-audit/supplements.md))
- **List:** a 30-row candidate list, because no free sales ranking exists, plus 5 added rows.
- **PE share:** 3 of 30 (10.0%):
  - Thorne (L Catterton; only its Europe and Asia advisers report PE funds, as in the pilot);
  - Natrol (New Mountain);
  - The Vitamin Shoppe (Kingswood; Performance Investment Partners is in neither file).
- **Pending deal:** Yellow Wood Partners (Y, 10 PE funds) agreed to buy Nature's Bounty and Puritan's Pride. At closing the share would be 5/30 (16.7%).
- **Strict count:** unchanged. Herbalife's 5%+ holders (Nantahala, Baupost, Route One, Renaissance) report no PE funds.
- **Owner not found:** 3, plus 2 rows whose owner was not reconfirmed.
- **BDC overlap:** Thorne (Healthspan Buyer, LLC at five New Mountain BDCs and two Nuveen Churchill BDCs) and The Vitamin Shoppe (three TCW BDCs).
  - Added rows: Swanson (Antares) and AG1 (warrants at TriplePoint).
  - Vytalogy (Natrol, Jarrow) and Herbalife appear only in prior-period columns.
- **Affiliate programs:** 3 on ranked rows. The one on a PE row is Thorne.
- **Change:** none.

**Dental chains** ([dental.md](category-audit/dental.md))
- **List:** 30 brand rows ordered by their own office counts. The candidate DSOs came from Becker's mid-2026 list, read through search.
- **PE share:** 15 of 30 (50.0%) are PE-owned with a current primary source, on 64.5% of offices.
  - 17/30 if Ideal Dental (Blackstone Tactical Opportunities, Y) and Dental365 (TJC LP, Y) are added. Both statuses date from 2021.
  - 19/30 (63.3%) if the two Affordable Care rows, lender-owned since June 2026, are added as well.
- **Public rows:** none, so the strict count equals the confirmed count.
- **Owner not found:** 8.
- **BDC overlap:** 22 of 30 rows, including 14 of the 15 confirmed PE rows.
  - At 2026-06-30, FS KKR Capital Corp holds Affordable Care Class A and Class B common stock and preferred stock, plus Dental Care Alliance common stock.
  - Lenders also hold equity in InterDent (Gentle Dental: Prospect, common stock), Absolute Dental (Ares Capital, as an affiliated issuer with units) and Familia (Monroe, Class A units).
- **Affiliate programs:** none.
- **Change:** none. Every PE owner reports PE funds. FS KKR's adviser, FS/KKR Advisor, LLC, reports none, so the adviser file does not settle Affordable Care.

**Veterinary chains** ([veterinary.md](category-audit/veterinary.md))
- **List:** 21 brand rows, because fewer than 30 branded chains were found.
- **PE share:** 11 of 21 (52.4%): 10 PE-owned rows plus MedVet, where Leonard Green holds a minority. Every PE owner reports PE funds.
- **Mars:** Mars (family-owned) holds 64.3% of fixed-site hospitals through Banfield, VCA and BluePearl. PE rows hold 26.3%.
- **Upper bound:** 16/21 (76.2%). It adds:
  - Bond Vet and Small Door (pre-merger investors Warburg Pincus Y and Valspring Y);
  - Lovet (TAG, trade press);
  - Petfolk (Deerfield Management Company, Y with 1 PE fund);
  - VEG (D1 Capital Partners, Y with 24, named in a 2021 release title).
- **Owner not found:** 1, plus 4 rows whose owner type is not confirmed.
- **BDC overlap:** 6 rows: Vetco (via Petco), CityVet, Petfolk, MedVet, and Chewy Vet Care and Modern Animal (via Chewy). Six BDCs hold Pathway Vet Alliance, which the worker's own note calls Thrive's former name; no primary source read here says so.
- **Affiliate programs:** none.
- **Change:** the upper bound rose from 14/21 to 16/21 (Deerfield Y, D1 Capital Y).

## 2. Form ADV check of the named firms

**Source:** the SEC monthly adviser files for November 2026 (links in "How this was assembled"). Types: RIA = registered adviser; ERA = exempt reporting adviser. The PE column shows `Any PE Funds`, with `Total number of PE funds` in brackets.

**A. Owners, controllers and minority holders of brand rows**

| Firm (as sources name it) | Rows and role | Adviser entity in the file | Type, CRD | PE funds | Latest ADV | Note |
|---|---|---|---|---|---|---|
| Sycamore Partners | Walgreens (owner); Torrid, 7 KnitWell brands (control) | Sycamore Partners Management, L.P. | RIA 284346 | Y (33) | 2026-03-31 | match |
| Cerberus Capital Management | Albertsons (31.0%, holder); 6 3Z Brands rows (control) | Cerberus Capital Management, L.P. | RIA 152175 | Y (9) | 2026-08-26 | match; **decides the pharmacies strict count** |
| Brigade Capital Management | Family Dollar (co-buyer); Gabe's (lender group) | Brigade Capital Management, LP | RIA 144078 | Y (2) | 2026-10-15 | match; **decides Family Dollar and Gabe's** |
| Macellum Capital Management | Family Dollar (co-buyer) | not found | n/a | n/a | n/a | absence proves nothing |
| Arbour Lane Capital Management | Gabe's (lender group) | Arbour Lane Capital Management LP | RIA 298198 | Y (3) | 2026-03-31 | match |
| Anchorage Capital | Gabe's (lender group); Madewell via J.Crew Group (majority, 2020) | Anchorage Capital Group, L.L.C.; Anchorage Capital Advisors, L.P. | RIA 135657; RIA 328998 | N; N | 2026-03-30; 2026-08-27 | match; **leaves Madewell unconfirmed**. Anchorage Capital Partners (Sydney, ERA, Y) is a different firm by name only |
| Leonard Green & Partners | Mister (control); TAG: Aspen Dental, ClearChoice (co-owner); MedVet (minority) | Leonard Green & Partners, L.P. | RIA 158164 | Y (107) | 2026-03-31 | match (as pilot) |
| Oaktree Capital Management | Whistle (majority) | Oaktree Capital Management, L.P. | RIA 106793 | Y (7) | 2026-08-17 | match |
| A&M Capital (AMCO) | Whistle (minority) | A&M Capital Advisors, LP | RIA 163576 | Y (8) | 2026-06-25 | match |
| Golden Gate Capital | Tidal Wave | Golden Gate Private Equity Inc. (business name Golden Gate Capital) | RIA 157379 | Y (7) | 2026-04-28 | match (website goldengatecap.com) |
| TSG Consumer Partners | Super Star; Thrive | TSG Consumer Partners LP | RIA 160826 | Y (18) | 2026-04-30 | match (as pilot) |
| Imperial Capital (Toronto) | GO Car Wash | Imperial Capital Limited | ERA 316569 | Y (7) | 2026-03-05 | match: website imperialcap.com, the domain the worker cited |
| Freeman Spogli & Co. | WhiteWater | Freeman Spogli Management Co., L.P. | RIA 156819 | Y (7) | 2026-03-31 | match (website freemanspogli.com); **decides WhiteWater** |
| Access Holdings | Cobblestone, Flagship (Spotless Brands) | Access Holdings Management Company LLC | RIA 297197 | Y (27) | 2026-03-26 | match (website accessholdings.com); **decides 2 rows** |
| Susquehanna Private Capital | LUV | not found ("Susquehanna" matches nothing) | n/a | n/a | n/a | **LUV stays pending** |
| Point72 Private Investments | Tsunami ("an affiliate of") | Point72 Asset Management, L.P. | RIA 283077 | Y (4) | 2026-08-14 | firm's main adviser; the "Private Investments" unit has no separate filing. **Decides Tsunami** |
| Wildcat Capital Management | Club Car Wash, Clean Express (platform owner) | Wildcat Capital Management, LLC | RIA 162178 | Y (3) | 2026-05-12 | match; **decides 2 rows** although the worker's sources call it a single-family office |
| Sculptor | Wildcat platform (investor, stake not stated) | Sculptor Capital LP; Sculptor Advisors LLC | RIA 107913; RIA 319598 | N; N | 2026-10-09 | match; no effect (Wildcat decides) |
| Warburg Pincus | El Car Wash (control); Bond Vet (2021 investor); MB2 (rollup); Gabe's (former) | Warburg Pincus LLC | RIA 156945 | Y (213) | 2026-03-31 | match |
| AEA Investors | Splash Northeast (majority); AmeriVet (rollup) | AEA Enterprise Partners Management LP; AEA QP Advisers LLC | RIA 132753; RIA 124560 | Y (5); Y (25) | 2026-06-04 | match (website aeainvestors.com). The pilot reported AEA as not found; that was a search miss |
| Percheron Capital | Caliber | Percheron Investment Management LP | RIA 312004 | Y (14) | 2026-09-15 | match (website percheroncapital.com) |
| Eagle Merchant Partners | Caliber (minority, 2021) | EMP Management LLC | RIA 285104 | Y (17) | 2026-10-12 | match (business name) |
| TRP Capital Partners | Jax Kar Wash | TRP Capital Advisors, LLC; TRP Capital Advisors V and VI, LLC | RIA 281098; 306604; 329787 | Y (6; 11; 5) | 2026-03-26 to 2026-03-31 | match (website trpfund.com) |
| KKR | Quick Quack (minority); Heartland Dental (rollup); BrightSpring (left-out pharmacy row, 21.7%) | Kohlberg Kravis Roberts & Co. L.P.; KKR Credit Advisors (US) LLC | RIA 144533; RIA 146629 | Y (553); Y (38) | 2026-09-25 | match (as pilot) |
| Seidler Equity Partners | Quick Quack (minority) | Seidler Kutsenda Management Company, LLC | RIA 156909 | Y (32) | 2026-07-07 | match (website sepfunds.com) |
| BC Partners | PetSmart, Chewy (and Chewy Vet Care, Modern Animal) | BC Partners Advisors L.P.; BC Partners LLP | RIA 288495; ERA 284927 | Y (9); Y (80) | 2026-09-29; 2026-03-20 | match |
| CVC Capital Partners | Petco, Unleashed, Vetco | CVC Capital Partners Advisory Company Limited; CVC Advisers Jersey Limited | ERA 161620; ERA 296266 | Y (15); Y (52) | 2026-10-28 | match; CVC Advisors (U.S.) Inc. reports N |
| CPP Investments | Petco (co-controller); Lulus (17.5%) | not found | n/a | n/a | n/a | a pension plan; no ADV expected |
| Garnett Station Partners | Woof Gang | Garnett Station Partners, LLC | RIA 300033 | Y (27) | 2026-05-12 | match |
| Great Hill Partners | Woof Gang | Great Hill Partners, LP | RIA 158158 | Y (50) | 2026-03-30 | match |
| Rainier Partners | Pet Food Express | Rainier Capital Partners LP | RIA 315967 | Y (3) | 2026-03-31 | match: website rainierpartners.com, the domain the worker cited |
| Summit Partners | Princess Polly (a.k.a. Brands, 56.0%) | Summit Partners, L.P. | RIA 135271 | Y (87) | 2026-08-20 | match |
| Permira | Reformation | Permira Investment Advisers Limited | ERA 292536 | Y (32) | 2026-04-01 | match |
| OpCapita | maurices (2019) | not found | n/a | n/a | n/a | maurices stays in the upper bound |
| TowerBrook Capital Partners | J.Jill (49.2%) | TowerBrook Capital Partners L.P. | RIA 155730 | Y (40) | 2026-06-09 | match |
| H.I.G. Growth Partners | Lulus (32.1%) | H.I.G. Capital, LLC | RIA 160711 | Y (119) | 2026-03-31 | match at firm level; H.I.G. WhiteHorse Advisers (the lending arm) reports N |
| Institutional Venture Partners | Lulus (17.6%) | Institutional Venture Management XIV to XVIII, LLC | ERAs | N (VC funds only) | 2026-03-28 | match; VC adviser |
| Wynnchurch Capital | Mattress Warehouse, Sleep Outfitters | Wynnchurch Capital, L.P. | RIA 173227 | Y (5) | 2026-03-23 | match (website wynnchurch.com) |
| Coliseum Capital Management | Purple (49.6%, "substantial control") | Coliseum Capital Management, LLC | RIA 158120 | Y (2) | 2026-03-30 | match; **decides Purple (strict)** |
| Fairfax Financial Holdings | Sleep Number (via Sleep Country Canada) | not found (Hamblin Watsa not found either) | n/a | n/a | n/a | an insurance holding company |
| American Securities | Cuisinart (Conair); TAG | American Securities LLC | RIA 160648 | Y (22) | 2026-05-14 | match |
| McCarthy Capital / M-One Capital | Caraway | M-One Capital Management, LLC | RIA 158782 | Y (9) | 2026-05-26 | match: website m-onecapital.com, the domain the worker cited |
| KarpReilly | Made In | KarpReilly, LLC | RIA 161169 | Y (7) | 2026-05-04 | match |
| Neuberger Berman | Martha Stewart (lead investor in Marquee Brands) | NB Alternatives Advisers LLC; Neuberger Berman Investment Advisers LLC | RIA 149822; RIA 124687 | Y (154); Y (11) | 2026-09-29; 2026-09-24 | match at firm level; the adviser for the Marquee stake isn't named |
| L Catterton | Thorne | Catterton Management Company, L.L.C.; L Catterton Europe SAS; L Catterton Asia Advisors | RIA 157428; ERA 162124; ERA 162692 | N; Y (6); Y (3) | 2026-06-15; 2026-03-30 | as pilot: the main US adviser reports N |
| New Mountain Capital | Natrol, Jarrow (Vytalogy); 5 Sonrava rows; Summit Wash (rollup) | New Mountain Capital, L.L.C. | RIA 161394 | Y (14) | 2026-03-30 | match |
| Kingswood Capital Management | The Vitamin Shoppe | Kingswood Capital Management, L.P. | RIA 304649 | Y (15) | 2026-04-17 | match (website kingswood-capital.com) |
| Performance Investment Partners | The Vitamin Shoppe | not found | n/a | n/a | n/a | Kingswood decides |
| Yellow Wood Partners | Nature's Bounty, Puritan's Pride (pending buyer) | Yellow Wood Partners LLC | RIA 161062 | Y (10) | 2026-07-29 | match |
| Swander Pace Capital | Swanson (added row) | SPC Management Co., Inc. | RIA 157259 | Y (5) | 2026-03-23 | match (website spcap.com) |
| Ares Management | TAG | Ares Management LLC | RIA 130074 | Y (157) | 2026-08-26 | match |
| Gryphon Investors | 5 Smile Brands rows; Heartland Veterinary Partners (rollup) | Gryphon Advisors, LLC | RIA 160185 | Y (18) | 2026-10-21 | match (website gryphoninvestors.com) |
| Thomas H. Lee Partners | Smile Doctors | THL Managers VII, LLC | RIA 171042 | Y (26) | 2026-07-02 | match by business name "THL" |
| Linden Capital Partners | Smile Doctors; Sage Dental | Linden Manager LLC (business name Linden Capital Partners) | RIA 161059 | Y (28) | 2026-03-25 | match (website linden.com) |
| Brentwood Associates | Jefferson Dental | Brentwood Private Equity, LLC | RIA 156558 | Y (23) | 2026-04-28 | match |
| Blackstone Tactical Opportunities | Ideal Dental (DECA, 2021) | Blackstone Tactical Opportunities Advisors L.L.C. | RIA 160157 | Y (103) | 2026-07-21 | match; current status still not reconfirmed |
| The Jordan Company | Dental365 (2021) | TJC LP | RIA 160313 | Y (48) | 2026-05-15 | match; current status still not reconfirmed |
| FS KKR Capital Corp | Affordable Care, Dental Care Alliance (lender equity) | FS/KKR Advisor, LLC | RIA 292803 | N | 2026-06-01 | match; the BDC's adviser reports no PE funds |
| RiverGlade Capital | CityVet | RiverGlade Capital Management, L.P. | RIA 290557 | Y (5) | 2026-03-27 | match |
| Oak Hill Capital | UrgentVet (AVG) | Oak Hill Capital Management, LLC | RIA 136656 | Y (35) | 2026-03-30 | match; Oak Hill Advisors (the MedVet lender) reports N |
| General Atlantic | GoodVets, WellHaven | General Atlantic Service Company, L.P. | RIA 133536 | Y (323) | 2026-08-12 | match |
| SkyKnight Capital | GoodVets, WellHaven | SkyKnight Capital, L.P. | RIA 281570 | Y (15) | 2026-03-31 | match |
| Whistler Capital Partners | Heart + Paw | Whistler Capital Partners LLC | RIA 316528 | Y (5) | 2026-03-31 | match |
| Cortec Group | Lap of Love | Cortec Group Management Services, LLC | RIA 161429 | Y (12) | 2026-03-27 | match |
| Deerfield Management | Petfolk (Series C lead) | Deerfield Management Company, L.P. | RIA 157876 | Y (1) | 2026-07-31 | match; **adds Petfolk to the vet upper bound** |
| Valspring Capital | Small Door (2025 equity lead) | Valspring Capital Management, LP | RIA 318288 | Y (1) | 2026-03-26 | match |
| D1 Capital Partners | VEG (2021 round co-lead; lead only) | D1 Capital Partners L.P. | RIA 297298 | Y (24) | 2026-03-31 | match; **adds VEG to the vet upper bound** |
| Fidelity (FMR) | VEG (2021 co-lead); many 5%+ holdings | Fidelity Management & Research Company LLC | RIA 108281 | Y (1) | 2026-07-30 | asset manager, not counted (see §7) |
| Durable Capital Partners | VEG (2021) | Durable Capital Partners LP | RIA 305221 | N | 2026-07-01 | match |
| Sequoia Heritage; Talisman Capital; Movendo Capital; White Star Capital; Idea Farm Ventures | VEG; Bond Vet; Petfolk | not found | n/a | n/a | n/a | |
| Lerer Hippeau; Primary Venture Partners; Toba Capital; Cutting Horse | Small Door; Petfolk | VC-only exempt advisers | ERAs | N (VC funds) | 2026-03 | match |

**B. 5%+ holders of public rows (the strict count)**

| Holder | Row (stake) | Adviser entity | Type, CRD | PE funds | Effect |
|---|---|---|---|---|---|
| Mantle Ridge LP | Dollar Tree (7.0%) | Mantle Ridge LP | RIA 284653 | N | none |
| Summit Trail Advisors, LLC | Ollie's (5.62%) | same | RIA 220519 | Y (8) | Ollie's counts as PE minority (strict) |
| Kayne Anderson Rudnick | Ollie's (6.06%) | Kayne Anderson Rudnick Investment Management, LLC | RIA 104599 | N | none |
| Fund 1 Investments / Pleasant Lake Partners | Citi Trends (31.1%); Torrid (10.49%) | Pleasant Lake Partners LLC (Fund 1 Investments has no separate filing) | RIA 304281 | Y (1) | Citi Trends counts as PE minority (strict); Torrid is already PE-owned |
| Divisadero Street Capital | Citi Trends (5.7%) | Divisadero Street Capital Management, LP | RIA 317392 | N | none |
| Shay Capital | Citi Trends (5.1%) | not found | n/a | n/a | none |
| Aldebaran Capital, LLC | Cato (6.2%) | same (Carmel, IN) | RIA 122360 | N | none |
| BBRC International | Victoria's Secret, PINK (13.0%, then 9.8%) | not found | n/a | n/a | none |
| Royce & Associates; Paradigm Capital Management | J.Jill (8.1%; 6.2%) | Royce & Associates, LP; Paradigm Capital Management, Inc. | RIA 107689; RIA 107982 | N; N | none (J.Jill already counted through TowerBrook) |
| Nomura Holdings | Torrid (6.26%) | Nomura adviser entities | RIAs | N | none |
| RWWM, Inc. | Helen of Troy / OXO (5.04%) | RWWM, Inc. | RIA 148221 | N | none |
| Pzena Investment Management | Newell / Calphalon (11.6%) | Pzena Investment Management LLC | RIA 106847 | N | none |
| Appaloosa LP; PRIMECAP Management | Whirlpool / KitchenAid (6.92%; 6.75%) | Appaloosa LP; PRIMECAP Management Co | RIA 281909; RIA 105516 | N; N | none |
| Nantahala; Baupost; Route One; Renaissance Technologies | Herbalife (8.40%; 8.33%; 7.28%; 5.43%) | each under its own name | RIA 158081; 109530; 156398; 106661 | N (all four) | none |
| Nina Capital Holdings; SilverCape Investments | PetMed Express (12.2%; 12.1%) | not found | n/a | n/a | none |
| AQR Capital Management | Chewy Class A | AQR Capital Management, LLC | RIA 111883 | N | none |
| Gabelli; River Road; Dimensional | Ingles; AEO | GAMCO and Gabelli entities; River Road Asset Management; Dimensional Fund Advisors LP | RIAs | N | none |
| Capital International / Capital World Investors | Burlington (13.9%); CVS (5.50%) | Capital Research and Management Company | RIA 110885 | N | none |
| Centre Partners V, L.P. | Lifetime Brands (26.2%), Farberware tools licensee, not a row | Centre Partners Management LLC | RIA 109534 | Y (8) | none (not a row; see question 9 in §7) |
| Index and asset managers: Vanguard, BlackRock, State Street, FMR, T. Rowe Price, J.P. Morgan, Wellington, Charles Schwab IM, Dodge & Cox | many rows | Vanguard entities N; BlackRock Capital Investment Advisors Y (125), BlackRock Financial Management Y (73); SSGA Funds Management Y (1); FMR Y (1); T. Rowe Price Associates Y (3); J.P. Morgan Investment Management Y (27); Wellington N; Schwab IM N; Dodge & Cox N | RIAs | mixed | **not counted**, as in the pilot (see §7) |

**C. Former owners, lenders and leads** (no row's number depends on these)
- **Y (PE funds reported):**
  - Former owners: Roark Capital Management (Pet Supermarket, Great Expressions; RIA 160368), Berkshire Partners (Affordable Care; RIA 160675), Harvest Partners (Affordable Care, DCA; RIA 158284), Halifax Investment Management (Familia; RIA 152789, website thehalifaxgroup.com), Durational Capital Management (Casper; RIA 291371), Advent International (Serta Simmons Bedding; RIA 105673), Bansk Group (VIP Petcare; RIA 312320), Martis Capital (WellHaven; RIA 296437).
  - More former owners: Trive Capital and Latticework (AVG), Goldman Sachs Asset Management (MedVet 2019), Bain Capital Private Equity (Burlington), CCMP Capital Advisors (Ollie's director link), ACON Investments Management (Bargain Hunt; website aconinvestments.com), Palladin Consumer Partners (Splash Northeast seller), Wafra Inc. (El seller), Sun Capital Advisors (ClearChoice), FFL Partners, Tailwind Management and Littlejohn & Co. (Benevis), Sentinel Capital Partners (MB2, Pet Supplies Plus).
  - Rollup owners: Charlesbank (MB2), Quad-C Management (Specialized Dental, DCA), Shore Capital Partners Management (Mission Pet Health), Tyree & D'Angelo Partners (Heartland Veterinary Partners), CCMP Growth Advisors (MOJO/Mammoth).
  - Leads only: TPG Capital Advisors (IPP), Monogram Capital (Healthy Spot), Penfund (Pet Supermarket), FIG LLC (Fortress, Hollywood Feed lender), Blue Torch, Long Point and Fenway (Corsicana), ION Crossover Partners and Nexus Capital (Resident), Alpha Wave Global (AG1), Hillhouse Investment Management (Carote IPO), Silver Lake (Mission Pet Health), Cressey & Company (VetCor), Revelstoke (Vet's Best Friend), JAB Consumer Fund Management (NVA; as pilot), Apollo Capital Management (PetSmart 2023 recap), StepStone Group LP (PetSmart and Chewy consortium).
  - Lenders: HPS Investment Partners (KnitWell), Churchill Asset Management (Thorne), WhiteHawk Capital Partners (Family Dollar), Blackstone Alternative Credit Advisors (J.Crew 2020).
- **N:** Davidson Kempner (J.Crew lender), Baron Capital (Resident), Mill Road Capital (Lifetime), GC Advisors (Golub, Pet Supermarket lender).
- **Name match only:**
  - FSI Manager LLC "Fireside Investments" (El seller, ERA, Y 3);
  - Stonehenge Partners, Corp. (MedVet 2019 investor, ERA, Y 2, website stonehengepartners.com, so likely a match);
  - Vanterra Capital LLC (Misen lead "Vanterra Ventures", Y 8);
  - C&S Capital Partners, LLC (Small Door investor "C&S Family Capital", Y 7);
  - CDPQ Global Infrastructure (La Caisse, infrastructure only, Y 1);
  - Parkview entities (Petfolk, N);
  - JB Capital (Lifetime, N).
- **Not found:** Red Dog Equity, Audrose Partners, PNC Riverarch, Gordon Brothers, Second Avenue Capital, Black Canyon Capital, Bristol Growth Capital, Franchise Funding Group, Mubadala, Ontario Teachers', ADIA, GIC, Longview Asset Management, Shunwei, Gotham Gal, Pilot Growth, Lampros, Peugeot Invest, Studio Ramsay Global, RJJRP Holdings, Imperial Capital Group (the former AmeriVet owner by that name).

**What the check shows**
- **Every confirmed control owner reports PE funds through at least one adviser entity.** L Catterton reports them only through its Europe and Asia advisers; its main US adviser says N, as in the pilot.
- **Six owners the workers could not label now pass:** Brigade, Arbour Lane, Freeman Spogli, Access Holdings, Point72 and Wildcat.
- **Two decisive owners are absent:** Susquehanna Private Capital (LUV) and OpCapita (maurices). Absence proves nothing.
- **Two decisive owners report N:** Anchorage Capital Group (Madewell) and FS/KKR Advisor (the BDC that holds Affordable Care and DCA equity). `N` proves nothing.
- **The flag reaches past buyout firms.** Wealth managers (Summit Trail), activists (Pleasant Lake, Coliseum), VC and growth investors (Deerfield, Valspring, D1, Alpha Wave) and the big index managers all have advisers that report PE funds.

## 3. BDC overlap

**Result: 66 of 284 brand rows in the ten categories, through 43 borrower groups held by 88 BDCs.** All holdings below are current at each BDC's latest period: 2026-06-30 unless shown otherwise (Ares Capital and OFS 2026-09-30, Saratoga 2026-08-31).

| Category | Brand row(s) | Borrower as filed | BDCs holding it now | Owner kind |
|---|---|---|---|---|
| Pharmacies | Walgreens | Blazing Star Parent, LLC (first-lien term loan) | 11: Ares Capital Corp; Ares Strategic Income Fund; First Eagle Private Credit Fund; Oaktree Gardens OLP; Oaktree Specialty Lending; Oaktree Strategic Credit Fund; Sixth Street Lending Partners; Sixth Street Specialty Lending; SLR HC BDC; SLR Investment Corp.; SLR Private Credit BDC II | PE-owned |
| Pharmacies | Tops; Price Chopper/Market 32 | Northeast Grocery Inc | 1: Great Elm Capital Corp. | owner type not confirmed |
| Dollar and discount | Family Dollar | 1959 Holdings, LLC; "Family Dollar" (second lien) | 3: Crescent Capital BDC; Crescent Private Credit Income Corp; First Eagle Private Credit Fund | PE-owned (after ADV) |
| Car washes | Whistle Express | Express Wash Acquisition Company, LLC (filer's label "(Whistle)") | 3: BlackRock Direct Lending Corp.; BlackRock Private Credit Fund; BlackRock TCP Capital Corp. | PE-owned |
| Car washes | Mister Car Wash | Mister Car Wash Holdings, Inc. | 2: Blackstone Private Credit Fund; Golub Capital Private Credit Fund | PE-owned |
| Car washes | Quick Quack | Quick Quack Car Wash Holdings, LLC (also labeled "and KKR Game Changer Co-Invest Feeder II L.P.") | 10: 5C Lending Partners; Antares Private Credit Fund; Ares Capital Corp; Ares Strategic Income Fund; 5 Golub Capital BDCs; StepStone Private Credit Fund | PE minority |
| Car washes | Club Car Wash | Club Car Wash Operating, LLC; Club Car Wash Preferred, LLC; also Wildcat Car Wash Holdings, LLC | 3: HPS Corporate Lending Fund; MidCap Apollo Institutional Private Lending; MidCap Financial Investment Corp | PE-owned (after ADV) |
| Car washes | GO Car Wash | Go Car Wash Management Corp.; Go Car Wash Parent, Corp. | 6: Blackstone Private Credit Fund; Blackstone Secured Lending; Golub Capital BDC; Golub Capital Direct Lending Corp; 2 MidCap BDCs | PE-owned |
| Car washes | WhiteWater Express | "WhiteWater Express" (subordinated debt, 14% PIK) | 2: Bain Capital Private Credit; Bain Capital Specialty Finance | PE-owned (after ADV) |
| Car washes | Cobblestone; Flagship | Spotless Brands, LLC | 19: AGL Private Credit Income Fund; 2 Bain Capital BDCs; 2 Blue Owl BDCs; 2 Carlyle BDCs; FS KKR Capital Corp; KKR Enhanced US Direct Lending Fund-L; 2 KKR FS Income Trusts; 2 Goldman Sachs BDCs; HPS Corporate Lending Fund; Jefferies Credit Partners BDC; 2 Lord Abbett funds; Phillip Street BDC; Senior Credit Investments | PE-owned (after ADV) |
| Car washes | LUV Car Wash | "LUV Car Wash" (common equity, acquired 2022) | 3: Morgan Stanley Direct Lending Fund; North Haven Private Income Fund; T Series BDC | PE status pending |
| Car washes | Clean Express Auto Wash | Express Wash Concepts, LLC | 2: Blackstone Private Credit Fund; HPS Corporate Lending Fund | PE-owned (after ADV) |
| Car washes | BlueWave Express | Texas Express Wash, LLC (loans); Texas Wash Holdings, LLC (d/b/a ClearWater Express Wash) (warrants) | 1: WhiteHorse Finance | private, owner not stated |
| Pet stores | PetSmart | PetSmart LLC | 5: Apollo Debt Solutions BDC; Crescent Private Credit Income Corp; Franklin BSP Capital; HPS Corporate Capital Solutions Fund; HPS Corporate Lending Fund | PE-owned |
| Pet stores; vet | Petco; Unleashed; Vetco | Petco Health and Wellness Company Inc; Petco Animal Supplies | 2: OFS Capital (2026-09-30); Palmer Square Capital BDC | PE-owned |
| Pet stores | Pet Supplies Plus; Wag N' Wash | Fusion Parent, LLC (fka Franchise Group Inc.): common stock and membership units, listed as an affiliate portfolio company | 1: BCP Investment Corp | lender-owned |
| Pet stores | Hollywood Feed | Hollywood Feed, LLC | 1: Fortress Private Lending Fund | private, owner not stated |
| Pet stores (added); vet | Chewy; Chewy Vet Care; Modern Animal | Chewy, Inc. | 1: Blackstone Private Credit Fund | PE-owned |
| Women's apparel | Torrid | Torrid LLC (term loan) | 1: Saratoga Investment Corp. (2026-08-31) | PE-owned |
| Women's apparel | Ann Taylor, LOFT, Lane Bryant, Talbots, Chico's, White House Black Market, Soma | Knitwell Borrower LLC | 2: HPS Corporate Capital Solutions Fund; HPS Corporate Lending Fund | PE-owned |
| Mattresses | Helix Sleep (the 3Z group's other five brands share the parent) | Helix Sleep, Inc. (term loan, acquired 2025-11-07) | 3: TCW Direct Lending VIII; TCW Specialty Lending; TCW Star Direct Lending | PE-owned |
| Mattresses | Saatva | Whitestone Home Furnishings, LLC (d/b/a Saatva, Inc.) | 1: WhiteHorse Finance | not found |
| Mattresses | Serta, Beautyrest, Simmons, Tuft & Needle | Serta Simmons Bedding LLC (common stock) | 2: Barings BDC; Barings Capital Investment Corp | owner type not confirmed |
| Cookware | Cuisinart | Conair Holdings LLC (first and second lien); ASP Conair Holdings LP (Class A units) | 4: Blue Owl Capital Corp; Blue Owl Credit Income Corp.; North Haven Private Income Fund; Steele Creek Capital | PE-owned |
| Supplements | Thorne | Healthspan Buyer, LLC | 7: New Mountain Finance Corp; New Mountain Guardian IV BDC; New Mountain Guardian IV Income Fund; New Mountain Private Credit Fund; NMF SLF I; Nuveen Churchill Direct Lending; Nuveen Churchill Private Capital Income Fund | PE-owned |
| Supplements | The Vitamin Shoppe | The Vitamin Shoppe, LLC (acquired 2026-03-23) | 3: TCW Direct Lending VIII; TCW Specialty Lending; TCW Star Direct Lending | PE-owned |
| Supplements (added) | Swanson Health | Swanson Health Products, Incorporated | 1: Antares Private Credit Fund | PE-owned |
| Supplements (added) | AG1 | Athletic Greens International, Inc. (warrants) | 2: TriplePoint Private Venture Credit; TriplePoint Venture Growth BDC | not found |
| Dental | Aspen Dental; ClearChoice | ADMI Corp. (aka Aspen Dental); Aspen Dental Management Inc. | 3: Franklin BSP Capital; HPS Corporate Lending Fund; New Mountain Finance Corp | PE-owned |
| Dental | Smile Doctors | Smile Doctors LLC | 7: Antares Private Credit Fund; Antares Strategic Credit Fund; Blackstone Private Credit Fund; Blackstone Secured Lending; Crescent Capital BDC; New Mountain Guardian IV BDC; New Mountain Private Credit Fund | PE-owned |
| Dental | Affordable Dentures & Implants; DDS Dentures | Affordable Care Inc (loans; Class A and B common; preferred) | 6: Apollo Debt Solutions BDC; Crescent Capital BDC; FS KKR Capital Corp; KKR Enhanced US Direct Lending Fund-L; KKR FS Income Trust; KKR FS Income Trust Select | lender-owned |
| Dental | Western Dental, DentalWorks, Brident, Perfect Teeth, Vital Smiles | "Western Dental"; Sonrava Health Holdings, LLC; Western Dental Holdings, LLC (equity) | 3: Audax Credit BDC; Franklin BSP Capital; Steele Creek Capital | PE-owned |
| Dental | Great Expressions | Great Expressions Dental Center PC | 1: Bain Capital Specialty Finance | not found |
| Dental | Gentle Dental | InterDent, Inc. (term loans; common stock) | 1: Prospect Capital Corp | not found |
| Dental | Ideal Dental | DECA Dental Holdings LLC | 5: Goldman Sachs BDC; Goldman Sachs Private Middle Market Credit; New Mountain Finance Corp; New Mountain Private Credit Fund; NMF SLF I | investment-firm owner, not reconfirmed |
| Dental | Midwest Dental, Monarch, Bright Now!, Castle, Mint Dentistry | Smile Brands Inc.; Smile Brands Group Inc. | 6: AB Private Credit Investors; Apollo Debt Solutions BDC; Barings BDC; Franklin BSP Capital; Nuveen Churchill Direct Lending; PennantPark Floating Rate Capital | PE-owned |
| Dental | Sage Dental | Sage Dental Management, LLC (loans; LLC units) | 1: TPG Twin Brook Capital Income Fund | PE-owned |
| Dental | Dental365 | Dental365 LLC; Premier Care Dental Management, LLC (dba Dental365) | 5: 5C Lending Partners; Adams Street Credit Solutions Fund; FS KKR Capital Corp; KKR FS Income Trust; KKR FS Income Trust Select | investment-firm owner, not reconfirmed |
| Dental | Absolute Dental | Absolute Dental Group LLC and Absolute Dental Equity, LLC (affiliated issuer; loan, Class A common and preferred units) | 1: Ares Capital Corp (2026-09-30) | not found |
| Dental | Familia Dental | Familia Dental Group Holdings, LLC (Class A units) | 1: Monroe Capital Income Plus | not found |
| Vet | CityVet | CityVet, Inc. | 2: Capital Southwest; Crestline Lending Solutions | PE-owned |
| Vet | Petfolk | Petfolk Inc. (preferred stock, warrants) | 1: TriplePoint Private Venture Credit | owner type not confirmed |
| Vet | MedVet | Medvet Associates LLC | 2: OHA Senior Private Lending Fund (U); T. Rowe Price OHA Select Private Credit Fund | PE minority |

**Per category:**

| Category | Brand rows overlapping | PE or PE-minority rows overlapping |
|---|---|---|
| Pharmacies | 3 / 30 | 1 / 1 |
| Dollar and discount | 1 / 25 | 1 / 2 |
| Car washes | 11 / 30 | 9 / 16 |
| Pet stores | 6 / 26 ranked, plus Chewy | 3 / 5 |
| Women's apparel | 8 / 32 | 8 / 12 |
| Mattresses | 6 / 30 (11 with the 3Z group) | 1 / 8 (6 with the group) |
| Cookware | 1 / 30 | 1 / 4 |
| Supplements | 2 / 30, plus 2 added rows | 2 / 3 |
| Dental | 22 / 30 | 14 / 15 |
| Veterinary | 6 / 21 | 5 / 11 |
| **Total** | **66 / 284 (23.2%)** | **45 / 77 (58.4%)** |

**Not counted, with the reason:**
- **Not tied by the filer:**
  - "Splash Car Wash, Inc." at 2 Goldman Sachs BDCs, Phillip Street BDC and West Bay BDC. The maturities are 2031 and 2032; the name fits both Splash rows.
  - "Southeastern Grocers LLC" at 2 Silver Point BDCs. The pharmacy worker names Southeastern Grocers, Inc. as Winn-Dixie's former group; the suffix differs and the 2025 changes of ownership are not traced.
  - Pathway Vet Alliance LLC (with Jedi Group Holdings) at 6 BDCs: Ares Capital, Golub Capital Private Credit Fund and four New Mountain funds. It is tied to Thrive only by the worker's own note.
  - Independent Pet Partners Intermediate Holdings, LLC common equity at Main Street Capital and MSC Income Fund. This is IPP, the bankrupt former parent of Chuck & Don's and Kriser's; no primary source ties it to them today.
- **Different companies:**
  - "Blazing Star Shields Direct Parent, LLC (dba Shields Health Solutions)" at 5 BDCs is the Shields business, a separate company since the Walgreens deal.
  - "McKesson Medical-Surgical Top Holdings Inc." at 5 BDCs is a Medical-Surgical business, not the Health Mart franchisor.
  - Also excluded: West Coast Dental Services (not Coast Dental), Hamilton Thorne (a medical-device company), Stella & Chewy's (pet food), KabaFusion (infusion), and "Florida Veg Investments" (produce, matched by "VEG").
- **Prior periods only** (holdings in a 2025-09-30 or 2025-12-31 column, gone by 2026-06-30):
  - Vytalogy Wellness LLC (fka Jarrow Formulas), the Natrol and Jarrow parent, at FS KKR and three KKR funds;
  - Herbalife Ltd. at three Barings BDCs, and HLF Financing at Saratoga (last at 2026-02-28);
  - Modern Animal, Inc. at WTI Fund X;
  - Mister Car Wash at Ares Strategic Income Fund;
  - BrightSpring (a left-out pharmacy row) at Nuveen Churchill.
- **No hit:** Rows with no BDC hit include:
  - ZIPS, Super Star, Tidal Wave, El Car Wash, Tsunami, Summit Wash, Woof Gang, Pet Food Express, Princess Polly, Reformation, J.Jill, Lulus, Mattress Warehouse, Purple, Sleep Number, Somnigroup, Caraway, Made In, Marquee Brands, Natrol at 2026-06-30, GNC, Jefferson Dental, UrgentVet, GoodVets, Thrive, Heart + Paw, Lap of Love and NVA.
  - As in the pilot, "no hit" means no BDC holding under these names. It does not mean the company has no private-credit debt.

**The workers' BDC leads, checked:**

| Lead | Result |
|---|---|
| FS KKR's dental holdings (dental worker, from FSK's Q3 2026 10-Q) | Confirmed at 2026-06-30. FSK holds Affordable Care Inc loans, Class A and Class B common stock and preferred stock; Dental Care Alliance Inc loans and common stock; and Dental365 LLC loans. FSK's Q3 10-Q postdates the latest DERA file, so the DERA rows are Q2. |
| HPS and Knitwell | Confirmed: Knitwell Borrower LLC at HPS Corporate Lending Fund and HPS Corporate Capital Solutions Fund. |
| Churchill and Thorne | Confirmed: Healthspan Buyer, LLC at Nuveen Churchill Direct Lending and Nuveen Churchill Private Capital Income Fund, and at five New Mountain BDCs. |
| WhiteHorse and ClearWater | Confirmed: Texas Express Wash, LLC loans and Texas Wash Holdings, LLC (d/b/a ClearWater Express Wash) warrants at WhiteHorse Finance. |
| Oak Hill and MedVet | Confirmed: Medvet Associates LLC at OHA Senior Private Lending Fund (U) and T. Rowe Price OHA Select Private Credit Fund. |
| Car washes: EDGAR full-text leads | Confirmed: Quick Quack (Golub, StepStone), GO (MidCap, Golub, BXSL, BCRED), Club Car Wash (HPS, MidCap), WhiteWater (Bain ×2), Mammoth (First Eagle, OHA, Monroe), Spotless (KKR funds, Carlyle, Phillip Street). Not in the Q2 BDC data: ZIPS (PennantPark, HPS, Capital Southwest, Onex, MSC Income), Super Star (Carlyle), Summit Wash (New Mountain Private Credit Fund); Spotless at Golub and T Series; EWC at Cliffwater, 5C, SLR and FS KKR. Cliffwater's fund is not a BDC in DERA. |
| Dental: BCSF and Great Expressions | Confirmed. |
| Dental: Affordable Care at KKR funds and Crescent | Confirmed. |
| Pet: Hollywood Feed (Fortress) | Confirmed. |
| Pet: Fusion Parent | Confirmed (equity at BCP Investment Corp). |
| Pet: IPP | Found (equity at two Main Street BDCs), but not tied to a current brand. |
| Pet: Pet Supermarket (Golub) | No hit. |
| Mattresses: Serta Simmons Bedding | Confirmed (common stock at Barings). |
| Mattresses: 3Z | Confirmed through Helix Sleep, Inc. |
| Mattresses: Purple, Sleep Number, Somnigroup, Mattress Warehouse, Corsicana | No hit. "Sleep OpCo LLC" at WhiteHorse Finance is untied. |
| Supplements: Vitamin Shoppe and Swanson | Confirmed. |
| Supplements: Vytalogy | Prior period only. |
| Supplements: GNC and the Yellow Wood vehicle | No hit. |

**BDC borrowers in these categories that are not rows** (leads for the developer; brand links not checked):
- **Dental rollups:** MB2 Dental Solutions (16 BDCs), Dental Care Alliance and DCA Investment Holdings (8 now; 11 more held it only at 2025-12-31, before the June 2026 restructuring), Heartland Dental (5), Specialized Dental Holdings II (5), Pacific Dental Services, the PDS Health company (3), New Benevis Topco and Holdco (1, New Mountain Finance).
- **Vet rollups:** PetVet Care Centers (25 BDCs), Southern Veterinary Partners, of Mission Pet Health (11), Heartland Veterinary Partners (11), AmeriVet Partners Management (10), VetCor Professional Practices and PPV Intermediate Holdings (6).
- **Car washes:** Mammoth Holdings, the MOJO rollup (5 BDCs), Wildcat Car Wash Holdings (HPS), Team Car Wash (TCW Midco), Rapid Express Car Wash, Sun Day Carwash.
- **Other:** New Spanx, LLC and New Spanx Topco LP, held as an affiliated issuer at HPS Corporate Lending Fund and Oaktree Specialty Lending (Spanx was left out of the women's list); Lifetime Brands (Saratoga); Win Brands Group (housewares); Nellson Nutraceutical, Vital Bidco (Vitamin Well), Beacon Wellness Brands and Integrative Nutrition (supplement makers).

## 4. Quote check

**Method**
- **Downloads:** every URL cited in the Evidence, rollup and Ranking sections was re-downloaded with curl: 475 pages.
- **Etiquette:** robots.txt was read first for each host, and crawl delays were honored, with at least 1 s between requests and at least 1 s after robots.txt. Redirects were followed only within a host. A redirect to a new host got its own robots.txt check in a later pass.
- **Robots refusals:** a robots.txt that answered 401 or 403 was treated as a refusal, which is stricter than RFC 9309. 6 hosts were skipped that way: spotlessbrands.com, mortensondentalpartners.com, marsveterinary.com, summitwashholdings.com, businesswire.com and s21.q4cdn.com (the Aritzia PDF). One more host's robots.txt disallows Claude agents: petstuff.com, where bentleyspetstuff.com now redirects.
- **Text extraction:** script and style blocks were stripped and entities decoded. PDFs were read with pypdf, in a venv in the scratchpad.
- **Normalization:** NFKC (which also folds non-breaking spaces), curly quotes and dashes, zero-width characters, and the ®, ™ and ℠ marks. Matching was case-sensitive.
- **Spacing:** a second, space-insensitive pass catches text split by tags ("Caraway , the iconic"). Only 1 quote needed it.
- **Ellipses:** quotes with "…" were matched part by part.
- **Which page:** a quote was matched against the page on its own line first. "Same 10-K" lines use the row's other cited pages. A quote restating another row's quote was matched only when the line names that row.

**Fallbacks, each labelled in the table**
- **(a) Raw HTML:** for fields and attributes (portfolio-tile classes, `data-category`, embedded JSON, meta descriptions), with JSON escapes decoded.
- **(b) Worker copy:** used where the site blocked curl and a worker had saved the page: the Aritzia PDF (women's apparel) and the Smile Doctors 2026 release (dental, which returned HTTP 500 to the assembler). These are labelled "worker copy, not independently re-fetched".
- **(c) Not checkable:** WebFetch-summarizer quotes, JavaScript-only pages, a table image, blocked pages with no saved copy, pages named without a URL, and quotes the worker marked as search snippets or trade press "not cited".

**Scope.** All 1,076 double-quoted strings and backtick HTML fields on Evidence and rollup lines.
- **Left out of the totals:** 54 strings that are not page quotes: Form ADV field names (`Any PE Funds`), robots directives, HTML entity notes, the workers' own labels ("no stated stake", "owner today"), section names, search strings, URL slugs, and absence claims.
- **Absence claims checked:** each says a phrase is missing from a page. Those checked are missing: "Benevis", "LT Smile" and "Kool Smiles" on New Mountain's portfolio page; "private equity" on the FS&Co and Susquehanna pages.
- **Ranking-section quotes are not in the totals:** they are trade press used only for the ranking. Spot result: the DCI, NRF, HNN, SmartScout, Similarweb and Nutraceuticals World quotes matched, and 3 of 4 Car Wash Advisory quotes did (its page-title quote did not). The VetValue, Veterinary Integration Solutions and ScrapeHero pages were named without a link and not fetched.

| Category | Quotes and fields | Matched (page text) | Matched in raw HTML | Matched in worker copy | Not checkable | Failed |
|---|---|---|---|---|---|---|
| Pharmacies | 88 | 83 | 2 | 0 | 3 | 0 |
| Dollar and discount | 88 | 84 | 2 | 0 | 2 | 0 |
| Car washes | 119 | 107 | 2 | 0 | 9 | 1 |
| Pet stores | 86 | 74 | 2 | 0 | 10 | 0 |
| Women's apparel | 110 | 102 | 3 | 3 | 2 | 0 |
| Mattresses | 91 | 89 | 0 | 0 | 2 | 0 |
| Cookware | 116 | 113 | 1 | 0 | 2 | 0 |
| Supplements | 109 | 99 | 3 | 0 | 7 | 0 |
| Dental | 102 | 89 | 5 | 2 | 6 | 0 |
| Veterinary | 113 | 103 | 5 | 0 | 5 | 0 |
| **Total** | **1,022** | **943** | **25** | **5** | **48** | **1** |

- **Matched by hand (6, inside "Matched"):**
  - Discount Drug Mart's and NOW Foods' robots.txt lines (`User-agent: ClaudeBot` / `Disallow: /`). Both files were re-fetched and say exactly that.
  - HNN's "Independently-owned and operated Serta Simmons Bedding showrooms". It sits on the HNN 51 to 75 ranking page, which the mattresses file cites in its Ranking section, not on the row.
  - Quad-C's tile text "Realized | Dental Care Alliance" and "Current | Specialized Dental". The page text reads "Realized Dental Care Alliance" and "Current Specialized Dental"; the "|" is the worker's separator.
- **Matched on another page cited in the same row:** 9, for example Autobell's quotes on its page-data JSON (as the worker said) and Sleep Number's "same 8-K" quotes.
- **Not checkable, by reason (48):**
  - 23 search snippets or trade press the worker marked "not cited";
  - 11 WebFetch-only quotes (Spotless Brands ×6, Mortenson ×2, Mars Veterinary Health ×3);
  - 5 blocked pages: Business Wire titles ×3, H-E-B, and Bentley's site now behind petstuff.com's robots.txt;
  - 5 pages named without a URL (Madewell footer, nutrafol.com, gentledental.com, a Walmart news title, a CA Transparency Act PDF);
  - 3 JavaScript-only pages (KKR's Quick Quack release ×2, Modern Animal's locations page);
  - 1 text in a table image (DCI).
- **The one failure:**
  - **CW10 (car washes, WhiteWater), Notes line:** "We partner with exceptional founders and management teams in the consumer and distribution sectors to build enduring businesses." The worker gives it as FS&Co's meta description. The cited page (freemanspogli.com/portfolio/whitewater-express/) has no meta description and no such sentence. It is probably on another FS&Co page that the row does not link.
  - The row's ownership facts don't depend on it.
- **Negative control:** 29 matched quotes, about three per category, were altered by one change each (a digit shifted, a word reversed, a letter's case flipped, or a word dropped). They were re-run against the same page with the same matcher.
  - The originals came from SEC filings, raw-HTML fields, a PDF and a worker copy.
  - All 29 originals matched and all 29 altered versions failed.

## 5. Firms that appear in several categories

| Firm | Rows in the ten categories (role) | Pilot categories |
|---|---|---|
| Sycamore Partners | Walgreens (pharmacies); Torrid and 7 KnitWell brands (women's apparel): 9 rows, control | none |
| Leonard Green & Partners | Mister Car Wash (control); Aspen Dental and ClearChoice via TAG (co-owner); MedVet (minority) | Crunch (control); Life Time (11.2% holder); Eyemart (seller) |
| Roark Capital | Pet Supermarket and Great Expressions, both listed as previous investments | Dunkin', Sonic, Arby's, Buffalo Wild Wings, Subway, Anytime Fitness, Orangetheory (control); Culver's (minority) |
| KKR | Quick Quack (minority); Heartland Dental (rollup, majority since 2018); BrightSpring (21.7%, left-out pharmacy row); Dollar General (exited 2013). Its credit side lends to Spotless, Dental365, MB2, VetCor and AmeriVet, and holds Affordable Care and DCA equity through FS KKR and KKR FS funds | 1-800 Contacts (lead) |
| Cerberus Capital Management | six 3Z Brands mattress rows (control); Albertsons (31.0%, strict) | none |
| L Catterton | Thorne (control) | [solidcore] (majority); Equinox (investor) |
| BC Partners | PetSmart, Chewy (pet stores); Chewy Vet Care, Modern Animal (vet) | none |
| CVC and CPP Investments | Petco, Unleashed (pet stores); Vetco (vet) | none |
| TSG Consumer Partners | Super Star Car Wash; Thrive Pet Healthcare | CorePower Yoga, EōS Fitness |
| New Mountain Capital | Natrol, Jarrow (supplements); 5 Sonrava dental rows; Summit Wash (car-wash rollup). Its BDCs also lend to Thorne, Ideal Dental, Smile Doctors, TAG, Heartland Dental, Pathway, PetVet, AmeriVet and Benevis | none |
| American Securities | Cuisinart (cookware); TAG (dental) | none |
| Warburg Pincus | El Car Wash (control); Bond Vet (2021 investor); MB2 (dental rollup); Gabe's (former) | none |
| Brigade Capital Management | Family Dollar; Gabe's | none |
| Gryphon Investors | 5 Smile Brands rows (dental); Heartland Veterinary Partners (vet rollup) | none |
| AEA Investors | Splash Car Wash Northeast; AmeriVet (vet rollup) | 1-800 Contacts (former owner, lead) |
| H.I.G. Capital | Lulus (32.1%); InterDent (realized); its WhiteHorse arm lends to ClearWater/BlueWave and Saatva | none |
| Oak Hill | UrgentVet/AVG (Oak Hill Capital); VetCor (realized); Oak Hill Advisors lends to MedVet and Mammoth | none |
| Fund 1 / Pleasant Lake | Citi Trends (31.1%); Torrid (10.49%) | none |
| Imperial Capital (Toronto) | GO Car Wash | Keplr Vision (lead; the pilot marked it name match only, but the adviser's website, imperialcap.com, is the sponsor's own site) |
| Linden; Quad-C; Harvest Partners; Charlesbank | dental: Smile Doctors, Sage (Linden); Specialized Dental, DCA (Quad-C); Affordable Care, DCA (Harvest, former); MB2 (Charlesbank) | Charlesbank: MyEyeDr (minority) |

**Lenders across categories** (current BDC holders of brand-row borrowers):
- HPS Corporate Lending Fund holds 6 of the 43 borrower groups: Club Car Wash, Spotless, EWC, PetSmart, KnitWell and TAG.
- Blackstone Private Credit Fund holds 5: Mister, GO, EWC, Chewy and Smile Doctors.
- Franklin BSP Capital holds 4: PetSmart, TAG, Sonrava and Smile Brands.

## 6. Method and cost

**Setup.** There were ten worker agents, one per category, at most four at a time, and one assembler (this file). The workers built the rankings and the per-brand tables. The assembler ran the Form ADV and BDC passes, re-downloaded and checked every quote, and wrote this file.

| | Agent tokens | Tool calls | Wall-clock | Requests from the worker log (WebSearch + WebFetch + curl; SEC part of curl) |
|---|---|---|---|---|
| Pharmacies | 321,402 | 147 | 23.7 min | 15 + 1 + 135 (52 SEC) |
| Dollar and discount | 308,067 | 150 | 23.8 min | 19 + 1 + 119 (38 SEC) |
| Car washes | 372,987 | 251 | 35.8 min | 32 + 8 + 203 (19 SEC) |
| Pet stores | 343,841 | 158 | 23.7 min | 33 + 0 + 134 (22 SEC) |
| Women's apparel | 347,916 | 158 | 24.9 min | 21 + 7 + 170 (50 SEC) |
| Mattresses | 327,669 | 150 | 23.8 min | 28 + 0 + 153 (16 SEC) |
| Cookware | 330,957 | 174 | 27.5 min | 24 + 4 + 152 (20 SEC) |
| Supplements | 347,003 | 198 | 33.0 min | 26 + 0 + 112 (33 SEC) |
| Dental | 362,109 | 201 | 34.4 min | 39 + 7 + 126 (6 SEC) |
| Veterinary | 357,476 | 222 | 36.6 min | 35 + 2 + 131 (16 SEC) |
| **Workers, total** | **3,419,427** | **1,809** | 287 min of agent time | 272 + 30 + 1,435 (272 SEC) |
| Assembler | not metered | about 90 | about 46 min (18:04 to 18:50 UTC) | 0 + 0 + about 800 (148 SEC) |

- **Pilot comparison:** about 260k to 280k tokens per category in the pilot, against 308k to 373k here (mean 342k). The heavier categories (car washes, dental, vet) had no usable ranking and many sponsor pages to read.
- **The assembler's requests:**
  - About 790 by the fetcher, including 264 robots.txt reads and 82 same-host redirect hops, of which 140 went to SEC.
  - 8 SEC data requests (2 pages, 2 Form ADV zips, 4 DERA zips, 89 MB).
  - 2 robots.txt re-checks.
  - PyPI installs of pypdf and cryptography into the scratchpad venv.
  - Every SEC request returned HTTP 200, except data.sec.gov/robots.txt (404).
- **Cheap, reusable steps:** each Form ADV or BDC pass over the downloaded files takes seconds. The quote re-check took about 5 minutes of downloads and 3 minutes of matching.

**What made brands slow** (from the worker logs):
- **Rankings:** no free ranking was usable in 8 of 10 categories, against 1 of 3 in the pilot.
- **Bot walls and robots.txt refusals on the brands' own sites:** H-E-B, Wegmans, Petland, EarthWise, NOW, Nordic Naturals, Life Extension, Great Expressions and others.
- **2025 to 2026 ownership changes,** which the rankings predate (question 10 in §7).
- **Business Wire,** which returns 403 to automated fetches; several deal releases sit only there.
- **Ownership through bankruptcy or debt-for-equity deals,** where releases don't name the new owners.

**Etiquette lapses the workers reported:**
- **Car washes:** on modwash.com and nouria.com, two page requests came 1 to 2 s apart inside a `Crawl-delay: 10`. On several sites the first page request came within a second of robots.txt.
- **Mattresses:** cerberus.com was fetched straight after robots.txt, without its 10-second wait.
- **Dental:** one greatexpressions.com page (about-us) was fetched in the same command as robots.txt, before the file was read; the site disallows ClaudeBot and was not used. harvestpartners.com was fetched 1.5 s after robots.txt, inside its 10-second delay.
- **Vet:** heartandpaw.com was fetched in the same command as its robots.txt, which disallows ClaudeBot; the page is not cited. petiq.com's homepage was fetched 1.5 s after a 10-second delay was set. veg.com was read after checking only veg.vet's robots.txt.
- **Pet stores:** petland.com's about page was fetched once before its robots.txt, which disallows ClaudeBot, had been read; nothing from it is used.

**The assembler's own lapses:**
- **Two hostnames of one site were queued separately:** accessholdings.com and www.accessholdings.com, and leonardgreen.com and www.leonardgreen.com. Each site sets a site-wide `Crawl-delay: 10`, and each got two requests about 1 s apart. That was 2 lapses in about 790 requests; no other host's crawl delay applied to our agents.
- **One worker copy stood in for a fetch:** the women's apparel worker's copy of the Aritzia PDF (s21.q4cdn.com) was used, because that CDN's robots.txt answers 403.

## 7. Open questions for the developer

Numbers only; nothing here is decided.

1. **Brand row vs parent vs sales.** The shares move a lot with the unit:
   - car washes: 53.3% by row, 50.0% by parent, 70.5% by sites;
   - pharmacies: 3.3% by row, 30.7% of ranked Rx sales;
   - vet: 52.4% by row, 26.3% of hospitals;
   - dental: 50.0% by row, 30.0% by parent, 64.5% by offices;
   - women's apparel: 37.5% by row, 27.3% by parent;
   - mattresses: 26.7% by row, 14.3% by parent, 8.8% by sales.

   Sycamore alone accounts for 9 rows through 2 parents, and Cerberus for 6 rows through one parent (3Z Brands), plus Albertsons in the strict count.
2. **Categories with fewer than 30 brands.**
   - Dollar and discount has 13 core brands; the off-price block takes it to 25.
   - Vet has 21 branded chains.
   - Pharmacies has 8 ranked retail entries; 22 more rows are franchise networks and regional grocers.
   - Pet stores has 26 store chains.
3. **Composite rankings.**
   - Only restaurants and eyewear (pilot) have a trade-press sales ranking for all 30 rows.
   - Pharmacies (8 of 30), dollar (8 of 25), mattresses (22 of 30, mixing retail and wholesale) and cookware (10 of 30, Amazon skillets only) are partly ranked by sales.
   - Car washes is ranked by site count from one M&A adviser.
   - Pet stores, women's apparel, dental and vet are ordered by each brand's own count.
   - Supplements is an unordered candidate list.
4. **Strict rule and asset managers.**
   - Read literally, `Any PE Funds = Y` on a 5%+ holder catches index and asset managers too: BlackRock's advisers (Y, up to 125 PE funds), J.P. Morgan Investment Management (Y, 27), FMR (Y, 1), State Street (Y, 1) and T. Rowe Price (Y, 3). That would put nearly every public row in the strict count.
   - This file follows the pilot and leaves them out. It does count Summit Trail Advisors (a wealth adviser with 8 PE funds, Ollie's) and Pleasant Lake (an activist with 1 PE fund, Citi Trends).
5. **Single-family offices.** Wildcat Capital Management, which its own sources call a single-family office, reports 3 PE funds. That decides 2 car-wash rows (Club Car Wash, Clean Express) and 341 sites.
6. **Lender-owned companies.**
   - **Serta Simmons Bedding:** 4 mattress rows. Barings BDC and Barings Capital Investment hold its common stock.
   - **Pet Supplies Plus and Wag N' Wash:** 2 rows. BCP Investment Corp holds Fusion Parent's common stock and membership units.
   - **Gabe's:** 1 row. The lender group is Brigade (Y), Arbour Lane (Y) and Anchorage (N); it is counted here as PE-owned by the ADV rule.
   - **ZIPS:** 1 row, owned by "a group of its existing institutional investors". No BDC hit.
   - **Affordable Care:** 2 rows. FS KKR, three KKR funds, Apollo Debt Solutions and Crescent Capital BDC hold it; FSK holds Class A and Class B common and preferred stock.
   - **Dental Care Alliance:** a rollup, not a row. FSK holds common stock, and 8 BDCs hold its debt.
   - **BDC equity in brands whose owner is "not found":** InterDent/Gentle Dental (Prospect, common stock), Absolute Dental (Ares Capital, affiliated issuer), Familia (Monroe, Class A units), Saatva (WhiteHorse, loans only). Spanx, not a row, is held as an affiliated issuer by HPS and Oaktree.
   - **Counts:** these are 10 brand rows across 5 categories (mattresses, pet stores, dollar and discount, car washes, dental).
   - **The lenders' advisers:** Barings LLC (RIA 106006), the adviser of the two Barings BDCs that hold Serta Simmons Bedding stock, reports PE funds (13). FS/KKR Advisor reports none. KKR Credit Advisors (US) reports PE funds (38).
   - **If lender-held equity were read through the lenders' Form ADV,** the 4 Serta Simmons Bedding rows would take mattresses from 8 to 12 of 30. Gabe's is already in, and Affordable Care's 2 rows are already in dental's upper bound. No source states who holds the majority in these companies.
7. **Pending deals.**
   - Nature's Bounty and Puritan's Pride to Yellow Wood Partners (Y, 10 PE funds), expected by the first half of 2027: supplements would go from 3/30 to 5/30.
   - EyeCare Partners' optometry business to MyEyeDr (pilot eyewear, trade press): both rows are already PE-owned (Partners Group; Goldman Sachs AM), so eyewear stays at 4/30 by row.
   - Also pending, with no effect on PE counts: Giant Eagle to Kroger (family to public); CVS Pharmacy's separation (public to public, H1 2028); GoodVets buying WellHaven (PE to PE).
8. **VC and growth investors whose type depends on Form ADV.**
   - Deerfield Management Company (Y, 1; Petfolk), Valspring Capital Management (Y, 1; Small Door), Warburg Pincus (Y, 213; Bond Vet, El Car Wash, MB2) and D1 Capital Partners (Y, 24; VEG) all report PE funds.
   - Counting their rounds as PE would take vet from 11/21 to 15/21. The other upper-bound row, Lovet, rests on trade press.
   - Alpha Wave Global (Y, 12; AG1) would add 1 supplements added row.
   - Institutional Venture Partners (Lulus 17.6%) reports VC funds only.
9. **Dental and vet rollups that aren't brands.**
   - **Dental:** 7 rollups listed separately. 3 are PE-owned (Heartland, MB2, Specialized Dental Partners), 1 is lender-owned (DCA), 1 is doctor/ESOP-owned (Mortenson) and 2 are not found (PDS, Benevis). 6 of the 7 are BDC borrowers.
   - **Vet:** 30 rollups listed, 8 checked, 5 of those 8 PE-backed. 6 rollup names are BDC borrowers: PetVet (25 BDCs), Mission/SVP (11), Heartland Veterinary Partners (11), AmeriVet (10), VetCor (6), Pathway (6).
   - Counting rollups as rows would change the denominators.
10. **Licensing cases.** Five cookware rows are licensed names: Farberware, KitchenAid, Martha Stewart, Rachael Ray and Pioneer Woman.
    - **Farberware:** Meyer runs the cookware (private, owner not stated). Lifetime Brands licenses the name for tools and cutlery; Lifetime's 26.2% holder, Centre Partners Management, reports PE funds (8). Assigning the row to Lifetime would make it a strict-count PE minority.
    - **KitchenAid:** Whirlpool owns the brand, and Meyer makes the cookware. Whirlpool's non-index holders report no PE funds.
    - **Martha Stewart:** the one licensed row counted as PE (Marquee Brands, Neuberger Berman).
11. **2025 and 2026 changes that make public rankings stale.**

| Category | Rows whose owner changed or is changing |
|---|---|
| Pharmacies | 2: Walgreens private 2025-08-28; Giant Eagle pending. Rite Aid liquidated and is not a row. |
| Dollar and discount | 4: Family Dollar 2025-07-05; Gabe's 2025-08-25; Big Lots! to Variety 2025-01; Nordstrom Rack take-private 2025-05-20. 5 chains closed in 2023 to 2025, 3 of them once PE-owned. |
| Car washes | 4: Mister take-private 2026-05-19; ZIPS out of Chapter 11 2025-04-30; Splash Northeast to AEA 2025-04-25; BlueWave to ClearWater 2025-11-26. Take 5 was absorbed by Whistle. |
| Pet stores | 3: Pet Supplies Plus and Wag N' Wash to lenders 2025-06-06; Great Hill joined Woof Gang 2026-06-23. |
| Women's apparel | Francesca's is liquidating (about 400 to 475 stores), so it is not a row. |
| Mattresses | 2 in 2026: Sleep Number sold 2026-07-31; Somnigroup bought Leggett 2026-08-26. 2 in 2025: Mattress Firm 2025-02-05; Sleep Outfitters 2025-05-01. |
| Supplements | 3: The Vitamin Shoppe 2025-05-20; vitafusion 2025-12-31; Zarbee's 2026-11-02. 2 pending. |
| Dental | 2 rows (Affordable Care, 2026-06-29) and 1 rollup (DCA, 2026). |
| Vet | 5: Modern Animal to Chewy 2026-05-21; VIP Petcare to Tractor Supply 2026-05-28; Bond Vet and Small Door merged 2026-07-09; WellHaven to GoodVets, announced 2026-09-24. |
| Pilot | At least 4 eyewear rows were stale; Jersey Mike's IPO and Pizza Hut's sale for restaurants. |

## Sources

- SEC, Form ADV data, ["Information About Registered Investment Advisers and Exempt Reporting Advisers"](https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers): `ia110226-registered.zip`, `ia11022026-exempt.zip`, downloaded 2026-11-07.
- SEC/DERA, ["BDC Data Sets"](https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets): `2026_07_bdc.zip` to `2026_10_bdc.zip`, downloaded 2026-11-07. Example filings behind the table in §3, in the SEC inline viewer:
  - [Ares Capital 10-Q, 2026-09-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1287750/000162828026067383/arcc-20260930.htm): Blazing Star Parent; Absolute Dental; Pathway.
  - [Great Elm 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1675033/000119312526335023/gecc-20260630.htm): Northeast Grocery.
  - [Crescent Capital BDC 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1633336/000119312526342351/ccap-20260630.htm): 1959 Holdings.
  - [BlackRock Direct Lending 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1834543/000119312526337958/ck0001834543-20260630.htm): Express Wash Acquisition Company (Whistle).
  - [Blackstone Private Credit Fund 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1803498/000180349826000048/bcred-20260630.htm): Mister, GO, EWC, Chewy.
  - [HPS Corporate Lending Fund 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1838126/000162828026056772/hps-20260630.htm): Club Car Wash, Wildcat Car Wash Holdings.
  - [HPS Corporate Capital Solutions Fund 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1989817/000162828026056793/hps-20260630.htm): Knitwell Borrower.
  - [WhiteHorse Finance 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1552198/000110465926093465/whf-20260630x10q.htm): Texas Express Wash, Whitestone (Saatva).
  - [BCP Investment Corp 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1372807/000119312526337959/bcic-20260630.htm): Fusion Parent.
  - [Barings BDC 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1379785/000137978526000030/bbdc-20260630.htm): Serta Simmons Bedding common stock.
  - [TCW Direct Lending VIII 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1825265/000119312526346657/ck0001825265-20260630.htm): Helix Sleep, The Vitamin Shoppe.
  - [New Mountain Finance 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1496099/000149609926000029/nmfc-20260630.htm): Healthspan Buyer.
  - [Blue Owl Capital Corp 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1655888/000165588826000056/obdc-20260630.htm): Conair.
  - [FS KKR Capital Corp 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1422183/000162828026053783/fsk-20260630.htm): Affordable Care, DCA, Dental365.
  - [Prospect Capital 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1287032/000128703226000269/psec-20260630.htm): InterDent.
  - [Monroe Capital Income Plus 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1742313/000174231326000046/mcip-20260630.htm): Familia.
  - [Capital Southwest 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/17313/000001731326000095/cswc-20260630.htm): CityVet.
  - [OHA Senior Private Lending Fund (U) 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1955010/000195501026000014/brhc-20260630.htm): Medvet Associates.
  - [TriplePoint Private Venture Credit 10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1792509/000179250926000024/tpvc-20260630.htm): Petfolk, Athletic Greens.
  - [Saratoga 10-Q, 2026-08-31](https://www.sec.gov/ix?doc=/Archives/edgar/data/1377936/000121390026107187/ea0306042-10q_saratoga.htm): Torrid.
- The ten worker files and the pilot, linked above, for every ownership fact and quote.
