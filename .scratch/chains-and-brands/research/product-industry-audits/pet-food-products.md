# Product industry audit: Pet food and products

Ticket: [91-research-product-industry-audits](../../issues/91-research-product-industry-audits.md) · Worker report, researched 2026-11-17 (fetches logged 22:58–23:21 UTC) · Ownership facts come from primary sources only: SEC filings, company sites, a sponsor's release and Form ADV. Trade press supplies the ranking only. Pet store chains are left out (separate industry).

**Short answer**

| | Pet food and products (N = 30 brand rows: 13 ranked, 17 unranked) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **2 / 30 (6.7%)**: Wellness and Old Mother Hubbard, both Wellness Pet Company brands. Clearlake Capital agreed to buy the company in 2020, and the release names both brands. Both count as PE-owned (a buyout, no stated stake). Clearlake's portfolio page was blocked, so current status rests on the 2020 release (see open questions). PE minority stake: 0. |
| Ranked rows only (1–13, Jefferies survey) | **0 / 13.** Every ranked brand belongs to Nestlé Purina, Mars, General Mills, Costco, Colgate (Hill's), Post or Diamond Pet Foods. |
| Owner not found | **5 / 30 (16.7%)** strict: Taste of the Wild, plus Purina's Beneful, Dog Chow, Purina ONE and Pro Plan. No Nestlé domain could be read (purina.com, nestle.com, nestleusa.com and purina.ca all blocked), and no other primary source names these four brands' owner. Read leniently (the four carry the Purina masterbrand, and Smucker's 10-K names Nestlé Purina PetCare Company as the maker of Purina's cat and snack brands), the count is **1 / 30**. |
| Brand-direct affiliate programs | **1 found, non-PE**: Best Bully Sticks (Central Garden & Pet). **PE rows: 0.** Wellness's site (which also covers Old Mother Hubbard) links no affiliate program. Only 4 rows were checked: Best Bully Sticks, Wellness/Old Mother Hubbard and Tiki Pets. The big CPG brands sell through retailers and were not checked. |
| BDC overlap | **1 row: Wellness.** BlackRock Private Credit Fund holds "Wellness Pet LLC (Woof)" first-lien, first-out term loan (Q2 2026 data set). Old Mother Hubbard is not named in the BDC text, so it doesn't count. |

- **No free brand-level sales ranking of US pet food or products was found.** The list is a composite (see "Ranking"). Rows 1–13 come from a 2021 Jefferies survey of 1,450 US pet owners, reported by Petfood Industry. Rows 14–30 come from walking Petfood Industry's 2024 revenue table of US pet food companies, with at most two new brands per company.
- **Biggest finding:** the top of pet food is held by public companies and Mars. Of the 30 rows, 17 are public companies (Nestlé, General Mills, Colgate, Smucker, Post, Spectrum, Central, Freshpet, Costco) and 6 are family-owned (Mars ×5, Diamond). PE shows up only where the walk reaches mid-size companies: Wellness Pet Company is #11 by revenue in the table.
- **The result depends on the per-company cap** (numbers in "Open questions"). With 3 new brands per company, Wellness falls below the cut-off and the share is 0 / 30. With 1 per company, the walk reaches Compana, Nulo and other mid-size companies that weren't researched here.
- **No PE holder of the public parents counts.** Spectrum's 9.0% holder Callodine has affiliated advisers that report PE funds on Form ADV, but its latest Schedule 13G/A (7.56%) is filed under Rule 13d-1(b) as an investment adviser, so it is passive.

## How this was sourced (read first)

- **Ranking:** composite (see "Ranking"). It uses two Petfood Industry articles, read for the ranking only and never as evidence of ownership.
- **Ownership facts** come from SEC filings (10-K, DEF 14A, Schedules 13D and 13G), company sites (about pages, footers, trademark pages, press releases), Clearlake's release and Form ADV (November 2026 files, read locally).
- **SEC access:** 31 SEC requests (www.sec.gov, data.sec.gov, efts.sec.gov), all HTTP 200, all with the user agent `EvidenceEngine ownership-research bot (product industry audit)` and no contact detail, about 1.1 s apart (1 request per second or less).
- **Robots:**
  - robots.txt was read before the first request to each host.
  - mars.com sets `Crawl-delay: 10`; its three requests were 32 s and 16 s apart.
  - nestle.com's robots.txt carries a content-signal line (`ai-train=no, search=yes, ai-input=yes`); its brand page was challenged and never read.
  - rankings.newsweek.com disallows ClaudeBot and anthropic-ai, so Newsweek's "Most Loved Pet Brands 2026" was never fetched.
  - amazon.com disallows ClaudeBot, Claude-User and Claude-SearchBot. Only its robots.txt was read.
- **Slipped (rule broken once):** tasteofthewildpetfood.com's robots.txt disallows `anthropic-ai` and sets `Crawl-delay: 10`. Its homepage (page 071) was fetched in the same command as the robots.txt, before the rules were read. That breaks both rules. The page is excluded from evidence, nothing from it is quoted, and Taste of the Wild is counted as owner not found.
- **Blocked or failed:**
  - Imperva block pages ("This site is temporarily unavailable"), which are not challenges, so none was retried: purina.com, nestleusa.com and purina.ca, each on robots.txt.
  - Cloudflare challenges, retried once in the Playwright browser with the bot's user agent and no clicks:
    - cleared: petfoodindustry.com robots.txt and four of its articles; clearlake.com robots.txt and its 2020 release (the release was loaded straight in the browser after robots.txt cleared);
    - did not clear: Petfood Industry's 2025 top-10 article, nestle.com/brands/petcare and clearlake.com/portfolio/.
  - packworld.com challenged its robots.txt and was not pursued.
  - YipitData's monthly pet recaps are gated behind a form.
  - wellnesspetcompany.com gave a TLS name mismatch (it is not the company's site; wellnesspet.com is).
  - Four EDGAR full-text searches for Purina brand names returned 0 hits.
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist and Private Equity Vet; PitchBook, CB Insights and Preqin results that came up in searches. None of them came up as a lead except CB Insights in one search.
- **Leads only, never cited:**
  - Bloomberg Law and trade-press copies of Wellness's May 2025 refinancing release;
  - affiliate-network directories (FlexOffers, LinkClicky, Cuelinks) for Best Bully Sticks;
  - the Yummypets survey in Global Pet Industry (only category leaders).
- **Owner kinds are research notes, not engine classifications.** Counts are by brand row: Nestlé Purina is 6 rows, Mars 5, General Mills 3, and 2 each for Colgate, Post, Smucker, Spectrum, Central and Wellness Pet.
- **Quotes:** copied from saved page text (curl'd HTML with tags stripped, or the Playwright page's innerText). A script matched all 59 quoted strings against the saved page text, after collapsing whitespace, normalizing curly quotes and dashes, and dropping zero-width spaces. Result: 59 / 59 found. 4 deliberately altered controls all failed. Page cache: `$SCR/pages/pet-food/NNN.txt`, indexed in `index.tsv`. The quote file is `$SCR/scripts/pet-food/quotes.tsv`, and the checker is `check.py` in the same folder.

## Ranking

**No free, current ranking of US pet food or pet product brands by sales was found.** Sources checked and rejected:
- **YipitData:** monthly pet recaps that rank the top 50 brands, gated behind a form. A Petfood Industry write-up (2026-10-22) gives only rank movements.
- **Similarweb, "Best Selling Pet Supplies Brands on Amazon"** (updated 2026-11-01): the free table shows 5 brands ordered by year-on-year change in revenue share, not by share. They are Fancy Feast, Hill's Science Diet, Royal Canin, Sheba and Purina Pro Plan, with shares of 1.64%, 2.24%, 1.10%, 0.74% and 1.81%. That makes it a list of gainers, not a top list.
- **Newsweek, "Most Loved Pet Brands 2026":** robots.txt disallows Claude's agents.
- **Amazon Best Sellers:** robots.txt disallows Claude's agents.
- **YouGov Ratings:** has no pet brand category; its sitemap lists only dog and cat breeds.
- **Yummypets/Loop survey (Global Pet Industry):** names only the category leaders.
- **Reviews.ai via Petfood Industry:** sorts 19 dog food brands into four segments, without ranks.
- **Petfood Industry's 2025 top-10 company article:** challenge did not clear.

**Composite used.**

(a) **Rows 1–13, ranked: Jefferies survey.** Petfood Industry, "Top 15 favorite dog, cat food brands in US from survey", Tim Wall, October 13, 2021, https://www.petfoodindustry.com/pet-food-market/article/15468290/top-15-favorite-dog-cat-food-brands-in-us-from-survey.
- The article says: "Purina brands and Blue Buffalo topped pet owners’ favorite brands in a survey of 1,450 pet owners in the United States."
- The list has 15 lines. Two are not brands and are dropped: "Purina (unspecified sub-brand) - Nestle-Purina - 13%" (a masterbrand line) and "Other (Top: Fromm #27 at 1%)". The 13 brands keep the article's order.
- The article's company column is from 2021 and is not used. Today's owners come from primary sources: Nutrish and Kibbles 'n Bits moved from Smucker to Post in 2023.
- Limits:
  - it measures preference, not sales;
  - it is five years old;
  - it covers dog and cat food only, with no litter or supplies.

(b) **Rows 14–30, unranked: walk of Petfood Industry's company table.** Petfood Industry, "45 US pet food companies' revenues in 2024", Tim Wall, August 8, 2025, https://www.petfoodindustry.com/regions/us-and-canada/article/15752596/46-us-pet-food-companies-revenues-in-2024.
- It covers 45 companies, which "appear in Petfood Industry's Top Pet Food Companies database with headquarters in the United States."
- The rule:
  - Walk the table in revenue order: Nestlé Purina $22,457M, Mars $22,000M, Hill's $4,483M, General Mills $2,375.8M, J.M. Smucker $1,719.6M, Diamond $1,500M, Simmons $1,300M, Spectrum/United Pet Group $1,151.5M, Alphia $1,000M, Freshpet $975.2M, Wellness Pet Company $700M, Central Garden & Pet $547M, Sunshine Mills $525M, and so on.
  - Each company adds **at most two brands not already listed**.
  - Contract makers with no consumer brand of their own (Simmons, Alphia) are skipped.
  - Brands not sold in the US are skipped (Edgard & Cooper, Prime100, Spectrum's Europe-only IAMS and Eukanuba), and so are sub-lines of a listed brand (Blue Buffalo Wilderness and True Solutions, Pedigree Dentastix, Wellness CORE).
  - Stop at 30.
- Within a company, brands follow the order of the company's own primary source:
  - **Nestlé Purina and Mars** have no 10-K, and Nestlé's sites were blocked. They follow the order in which J.M. Smucker's FY2026 10-K competitor table names them:
    - Purina: Cat Chow (marked "(A)", the category leader), then Friskies.
    - Mars: Iams (already listed), Sheba, Dentastix (a Pedigree sub-line, skipped), then Greenies.
  - **Hill's:** Colgate's 10-K: Science Diet, Prescription Diet.
  - **General Mills:** 10-K trademark list, which is alphabetical: Blue Buffalo, Nudges, Tiki Pets.
  - **Smucker:** 10-K segment line: Meow Mix, Milk-Bone.
  - **Diamond:** its brand page lists only Diamond-named lines (Diamond, Diamond CARE, Diamond Naturals, Diamond Pro89). That counts as one row, "Diamond".
  - **Spectrum:** 10-K, "Companion Animal: Good’n’Fun®, DreamBone®, …".
  - **Freshpet:** one brand.
  - **Wellness:** its site menu: Wellness, then Old Mother Hubbard.
  - **Central:** 10-K alphabetical brand list: Aqueon, Best Bully Sticks.
- What the walk added: Purina +2, Mars +2, Hill's +1, General Mills +2, Smucker +2, Diamond +1, Spectrum +2, Freshpet +1, Wellness +2, Central +2. That makes 17 rows, 30 in all. The cut-off falls after Central; Sunshine Mills is next.
- **Known gaps:**
  - Post Holdings is absent from the table, though its brands enter through the survey.
  - Store brands other than Kirkland are absent (Walmart's Ol' Roy, Chewy's American Journey and Frisco, PetSmart's and Petco's labels).
  - DTC fresh brands are absent (The Farmer's Dog).
  - Litter brands are absent (Tidy Cats, Fresh Step, Arm & Hammer), because the table ranks pet food.
  - Pet-health brands are absent (Seresto, Frontline).
  - Supplies enter only through Spectrum and Central.

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Blue Buffalo (survey 7%) | General Mills, Inc. (10-K trademark list) | public company | none (5%+: BlackRock 10.5%, Vanguard Capital Mgmt 7.5%, State Street 5.9%, Vanguard Portfolio Mgmt 5.2%) | not checked | GIS | brand of a manufacturer | not checked | PF1 |
| 2 | Beneful (7%) | not found (no Nestlé page readable) | not found | none found | not found | — | brand of a manufacturer | not checked | PF2 |
| 3 | Pedigree (6%) | Mars, Incorporated (on Mars's petcare brand page; "a global, family-owned business") | family | none | not checked | — | brand of a manufacturer | not checked | PF3 |
| 4 | Dog Chow (5%) | not found (Purina masterbrand; no Nestlé page readable) | not found | none found | not found | — | brand of a manufacturer | not checked | PF2 |
| 5 | Kirkland Signature (4%) | Costco Wholesale Corporation ("our private-label brand") | public company | none (Vanguard 9.79%, BlackRock 7.83%) | not checked | COST | store brand | not applicable (store brand) | PF5 |
| 6 | Purina ONE (4%) | not found (as Dog Chow) | not found | none found | not found | — | brand of a manufacturer | not checked | PF2 |
| 7 | Pro Plan (4%) | not found (as Dog Chow) | not found | none found | not found | — | brand of a manufacturer | not checked | PF2 |
| 8 | Hill's Science Diet (3%) | Colgate-Palmolive Company (Hill's Pet Nutrition) | public company | none (Vanguard 10.26%, BlackRock 8.18%, State Street 5.95%) | not checked | CL | brand of a manufacturer | not checked | PF8 |
| 9 | Taste of the Wild (3%) | not found (only page read was fetched against robots.txt; excluded) | not found | none found | not found | — | brand of a manufacturer | not checked | PF9 |
| 10 | IAMS (3%) | Mars, Incorporated (US). Spectrum Brands holds IAMS "(Europe only)" | family | none | not checked | — | brand of a manufacturer | not checked | PF3 |
| 11 | Rachael Ray Nutrish (3%) | Post Holdings owns Nutrish (acquired from Smucker 2023-04-28); the "Rachael Ray" name is licensed from a third party | public company (licensed name element) | none (Vanguard 10.7%, BlackRock 8.1%, Clarkston 6.8%, Route One 6.5%; William P. Stiritz files a 13D as an individual) | 2023-04-28 | POST | brand of a manufacturer | not checked | PF11 |
| 12 | Royal Canin (3%) | Mars, Incorporated | family | none | not checked | — | brand of a manufacturer | not checked | PF3 |
| 13 | Kibbles 'n Bits (3%) | Post Holdings | public company | none (as row 11) | 2023-04-28 | POST | brand of a manufacturer | not checked | PF11 |
| 14 | Cat Chow | Nestlé Purina PetCare Company (named in Smucker's 10-K competitor table) | public company (Nestlé S.A., SIX Swiss Exchange; holders not read) | none found | not checked | — (NESN, SIX) | brand of a manufacturer | not checked | PF14 |
| 15 | Friskies | Nestlé Purina PetCare Company (same source) | public company | none found | not checked | — (NESN) | brand of a manufacturer | not checked | PF14 |
| 16 | Sheba | Mars, Incorporated | family | none | not checked | — | brand of a manufacturer | not checked | PF3 |
| 17 | Greenies | Mars, Incorporated | family | none | not checked | — | brand of a manufacturer | not checked | PF3 |
| 18 | Hill's Prescription Diet | Colgate-Palmolive Company | public company | none (as row 8) | not checked | CL | therapeutic diet, vet channel | not checked | PF8 |
| 19 | Nudges | General Mills, Inc. | public company | none (as row 1) | not checked | GIS | brand of a manufacturer | not checked | PF1 |
| 20 | Tiki Pets | General Mills, Inc. (10-K trademark list; site footer "© 2026 Copyright Tiki Pets") | public company | none (as row 1) | not checked | GIS | brand of a manufacturer | none found (homepage) | PF1 |
| 21 | Meow Mix | The J. M. Smucker Company | public company | none (Vanguard Capital Mgmt 7.2%, State Street 6.6%, BlackRock 5.9%) | not checked | SJM | brand of a manufacturer | not checked | PF21 |
| 22 | Milk-Bone | The J. M. Smucker Company | public company | none (as row 21) | not checked | SJM | brand of a manufacturer | not checked | PF21 |
| 23 | Diamond (incl. Diamond Naturals, CARE, Pro89) | Diamond Pet Foods; footer "© 2026 SCHELL & KAMPETER, INC."; "a family-owned company" | family (self-described; family not named) | none | not applicable | — | brand of a manufacturer | not checked | PF23 |
| 24 | Good'n'Fun | Spectrum Brands Holdings, Inc. (Global Pet Care) | public company | none counted (Pzena 10.7%, ADV N; Callodine 9.0% in proxy, 7.56% in latest 13G/A, filed under 13d-1(b)) | not checked | SPB | brand of a consumer-products company | not checked | PF24 |
| 25 | DreamBone | Spectrum Brands Holdings, Inc. | public company | none counted (as row 24) | not checked | SPB | brand of a consumer-products company | not checked | PF24 |
| 26 | Freshpet | Freshpet, Inc. | public company | none (BlackRock 11.4%, Wellington 8.1% by 13d-1(b) 13G/A, Wasatch 7.8%, BMO 5.2%) | not applicable | FRPT | refrigerated fresh food, own fridges in retail | not checked | PF26 |
| 27 | Wellness | Wellness Pet, LLC (footer); Clearlake signed an agreement to acquire The Wellness Pet Food Holdings Company, Inc. (WellPet) from affiliates of Berwind Corporation | PE-owned (no stated stake) | Clearlake Capital Group, L.P. (ADV Y, 75 PE funds) | 2020-11-18 (agreement) | — | DTC site plus retail | none found (homepage and media center) | PF27 |
| 28 | Old Mother Hubbard | Wellness Pet Company (site menu; named in Clearlake's release) | PE-owned (no stated stake) | Clearlake Capital Group, L.P. | 2020-11-18 (agreement) | — | brand of a manufacturer | none found (same site as Wellness) | PF27 |
| 29 | Aqueon | Central Garden & Pet Company | public company (founder William E. Brown holds 56.3% of voting power) | none (BlackRock 7.9% of votes, Vanguard 5.8%, Dimensional 4.1%) | not checked | CENT, CENTA | brand of a consumer-products company (aquarium) | not checked | PF29 |
| 30 | Best Bully Sticks | Central Garden & Pet Company | public company (as row 29) | none | not checked | CENT, CENTA | DTC site plus retail | **yes, brand-direct**: https://www.bestbullysticks.com/pages/affiliates | PF29 |

### Evidence

- **Ranking sources**
  - Company table: "The 45 dog, cat and other pet food companies in the list below contributed to that growth." and "appear in Petfood Industry's Top Pet Food Companies database with headquarters in the United States." — [Petfood Industry, "45 US pet food companies' revenues in 2024", August 8, 2025](https://www.petfoodindustry.com/regions/us-and-canada/article/15752596/46-us-pet-food-companies-revenues-in-2024)
  - Survey: "Purina brands and Blue Buffalo topped pet owners’ favorite brands in a survey of 1,450 pet owners in the United States." Rows quoted include "Purina (unspecified sub-brand) - Nestle-Purina - 13%", "Blue Buffalo - General Mills - 7%" and "Kibbles ‘n ‘Bits - J.M. Smucker - 3%". Date: "October 13, 2021". — [Petfood Industry, "Top 15 favorite dog, cat food brands in US from survey"](https://www.petfoodindustry.com/pet-food-market/article/15468290/top-15-favorite-dog-cat-food-brands-in-us-from-survey)
- **PF1 Blue Buffalo, Nudges, Tiki Pets (General Mills)**
  - Owner: "Some of the more important trademarks used in our global operations (set forth in italics in this report) include Annie’s, Betty Crocker, Bisquick, Blue Buffalo". The same list continues "… Nudges, Oatmeal Crisp …" and "… Tiki Pets, Total …". — [General Mills 10-K, FY ended 2026-05-31](https://www.sec.gov/Archives/edgar/data/40704/000162828026046466/gis-20260531.htm)
  - Second source for Nudges: Smucker's competitor table, "Blue Buffalo and Nudges General Mills, Inc." (see PF14).
  - Tiki Pets site footer: "© 2026 Copyright Tiki Pets" — [tikipets.com](https://tikipets.com/). No affiliate link on the homepage.
  - 5% holders: "BlackRock, Inc. 55,943,321 (7) — 10.5 Vanguard Capital Management 40,147,406 (8) — 7.5 State Street Corporation 31,552,421 (9) — 5.9" — [General Mills DEF 14A, filed 2026-08-13](https://www.sec.gov/Archives/edgar/data/40704/000162828026056619/gis-20260810.htm). All are index or asset managers filing 13Gs.
  - Since: not checked.
  - BDC names: "General Mills", "Blue Buffalo Pet Products", "Tiki Pets"
- **PF2 Beneful, Dog Chow, Purina ONE, Pro Plan (owner not found)**
  - Owner: not found from a primary source.
    - purina.com, nestleusa.com and purina.ca returned Imperva block pages on robots.txt.
    - nestle.com/brands/petcare stayed on a Cloudflare challenge after one browser retry.
    - EDGAR full-text searches for "Beneful", "Purina Pro Plan", "Purina ONE" and "Dog Chow" (2024 to date) returned 0 hits.
  - Leads only: the survey line "Purina (unspecified sub-brand) - Nestle-Purina" and the Purina masterbrand in three of the names. Smucker's 10-K names Nestlé Purina PetCare Company for Purina's other brands (PF14).
  - BDC names: "Nestlé Purina PetCare Company", "Purina"
- **PF3 Pedigree, IAMS, Royal Canin, Sheba, Greenies (Mars)**
  - Owner: "We are a global, family-owned business with a focus on becoming Sustainable in a Generation." — [Mars, Petcare brands page, accessed 2026-11-17](https://www.mars.com/our-brands/petcare)
  - The same page has a brand entry for each of "Pedigree", "Iams", "Royal Canin" and "Sheba", and says "GREENIES make all GREENIES™ Dental Treats".
  - Second source (Smucker 10-K, PF14): "Iams and Sheba Mars, Incorporated" and "Dentastix, Greenies and Temptations Mars, Incorporated".
  - IAMS outside the US: "Dog and Cat Food: Eukanuba® (Europe only), IAMS® (Europe only)." — [Spectrum Brands 10-K, FY ended 2025-09-30](https://www.sec.gov/Archives/edgar/data/109177/000010917725000043/spb-20250930.htm). So the US IAMS name is Mars's, and Spectrum holds it in Europe.
  - BDC names: "Mars, Incorporated", "Mars Petcare", "Royal Canin"
- **PF5 Kirkland Signature (Costco)**
  - Owner: "our private-label brand, Kirkland Signature" — [Costco 10-K, FY ended 2026-08-30](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm)
  - 5% holders: "Vanguard Group, Inc. 43,455,368(2) 9.79%" — [Costco DEF 14A, filed 2025-12-04](https://www.sec.gov/Archives/edgar/data/909832/000090983225000159/cost-20251204.htm). BlackRock holds 7.83%. Both figures come from 13F filings.
  - Model: store brand. The pet-food maker is not named in the sources read.
  - BDC names: "Costco Wholesale"
- **PF8 Hill's Science Diet, Hill's Prescription Diet (Colgate)**
  - Owner: "Hill’s markets pet foods primarily under three brands. Hill’s Science Diet, which is called Hill’s Science Plan in Europe, is a range of products for everyday nutritional needs. Hill’s Prescription Diet is a range of therapeutic pet foods" — [Colgate-Palmolive 10-K, FY2025](https://www.sec.gov/Archives/edgar/data/21665/000002166526000006/cl-20251231.htm)
  - 5% holders: "The Vanguard Group 100 Vanguard Blvd. Malvern, PA 19355 82,189,533(1) 10.26%" — [Colgate DEF 14A, filed 2026-03-25](https://www.sec.gov/Archives/edgar/data/21665/000130817926000136/cl015164-def14a.htm). BlackRock holds 8.18% and State Street 5.95%.
  - BDC names: "Hill's Pet Nutrition", "Colgate-Palmolive"
- **PF9 Taste of the Wild (owner not found)**
  - Owner: not found.
  - Diamond Pet Foods' trademark page lists only Diamond-named marks: "(i) Diamond, (ii) Diamond Naturals, (iii) Diamond CARE, (iv) Diamond Pro89" — [Diamond Pet Foods, Copyright/Trademark page](https://www.diamondpet.com/copyright-trademark/).
  - The brand's own site disallows anthropic-ai in robots.txt. Its homepage was fetched by mistake (see "Slipped") and is not used.
  - BDC names: "Taste of the Wild", "Schell & Kampeter, Inc."
- **PF11 Rachael Ray Nutrish, Kibbles 'n Bits (Post)**
  - Owner: "the Nutrish, 9Lives and Kibbles ’n Bits pet food brands" (Post Consumer Brands' core brands) — [Post Holdings 10-K, FY ended 2025-09-30](https://www.sec.gov/Archives/edgar/data/1530950/000153095025000260/post-20250930.htm)
  - Since: "including brands such as Rachael Ray Nutrish, Nature’s Recipe, 9Lives, Kibbles ’n Bits and Gravy Train" (acquisition from Smucker completed April 28, 2023) — [same 10-K](https://www.sec.gov/Archives/edgar/data/1530950/000153095025000260/post-20250930.htm)
  - Licence: Post lists "several trademarks that we license from third parties for use in the U.S., Canada and several other international markets, such as Pebbles, Oreo O’s, Rachael Ray and Premier Protein" — [same 10-K](https://www.sec.gov/Archives/edgar/data/1530950/000153095025000260/post-20250930.htm). Nutrish is in Post's own trademark list. The licensor of "Rachael Ray" is not named.
  - 5% holders: "The Vanguard Group (1) 100 Vanguard Blvd., Malvern, PA 19355 5,597,831 10.7 %", "Clarkston Capital Partners, LLC (3) 91 West Long Lake Road, Bloomfield Hills, MI 48304 3,562,796 6.8 %" and "Route One Investment Company, L.P. (4)" — [Post DEF 14A, filed 2025-12-15](https://www.sec.gov/Archives/edgar/data/1530950/000153095025000284/post-20251210.htm)
  - Form ADV: Clarkston N and Route One N.
  - 13D: "Name of reporting person William P. Stiritz" — [Schedule 13D/A on Post, filed 2026-03-05](https://www.sec.gov/Archives/edgar/data/1530950/000105205826000003/xslSCHEDULE_13D_X01/primary_doc.xml). He is an individual, not a PE firm.
  - BDC names: "Post Holdings", "Post Consumer Brands", "Nutrish"
- **PF14 Cat Chow, Friskies (Nestlé Purina); competitor table also used for the Mars order**
  - Owner: "Mainstream cat food Meow Mix Cat Chow (A), Friskies, Kit & Kaboodle, and Fancy Feast Nestlé Purina PetCare Company Iams and Sheba Mars, Incorporated" and "Beggin’ Strips Nestlé Purina PetCare Company Blue Buffalo and Nudges General Mills, Inc. Dentastix, Greenies and Temptations Mars, Incorporated" — [J.M. Smucker 10-K, FY ended 2026-04-30](https://www.sec.gov/Archives/edgar/data/91419/000009141926000050/sjm-20260430.htm)
  - Footnote: "(A) Identifies the current market leader within the product category." — [same 10-K](https://www.sec.gov/Archives/edgar/data/91419/000009141926000050/sjm-20260430.htm)
  - Notes: this is a competitor's filing (rank 1 source type, but not the owner's own words). Nestlé's 5% holders were not read, since Nestlé files no proxy with the SEC.
  - BDC names: "Nestlé Purina PetCare Company"
- **PF21 Meow Mix, Milk-Bone (Smucker)**
  - Owner: "U.S. Retail Pet Foods Meow Mix®, Milk-Bone®, Pup-Peroni®, and Canine Carry Outs®" — [J.M. Smucker 10-K, FY ended 2026-04-30](https://www.sec.gov/Archives/edgar/data/91419/000009141926000050/sjm-20260430.htm)
  - 5% holders: "Vanguard Capital Management LLC 7,677,331 (5) 7.2% State Street Corporation 6,932,086 (6) 6.6% BlackRock, Inc. 6,247,310 (7) 5.9%" — [Smucker DEF 14A, filed 2026-06-26](https://www.sec.gov/Archives/edgar/data/91419/000119312526283858/d227901ddef14a.htm)
  - BDC names: "The J. M. Smucker Company", "Milk-Bone", "Meow Mix"
- **PF23 Diamond (Diamond Pet Foods)**
  - Owner: "At Diamond Pet Foods, we're a family-owned company" and "© 2026 SCHELL & KAMPETER, INC. ALL RIGHTS RESERVED." — [Diamond Pet Foods homepage, accessed 2026-11-17](https://www.diamondpet.com/)
  - Brands: the brand list starts "Diamond® …" and includes "Diamond Naturals® Dry and canned formulas …" — [same page](https://www.diamondpet.com/). The trademark page is under PF9.
  - Notes: the family is not named.
  - BDC names: "Diamond Pet Foods", "Schell & Kampeter, Inc."
- **PF24 Good'n'Fun, DreamBone (Spectrum Brands)**
  - Owner: "Companion Animal: Good’n’Fun®, DreamBone®, Good Boy®, Nature's Miracle®" — [Spectrum Brands 10-K, FY ended 2025-09-30](https://www.sec.gov/Archives/edgar/data/109177/000010917725000043/spb-20250930.htm). The FY2026 10-K was not yet filed.
  - 5% holders: "Pzena Investment Management LLC1 2,459,485 10.7 % Callodine Capital Management, LP2 2,065,216 9.0 %" — [Spectrum DEF 14A, filed 2026-06-26](https://www.sec.gov/Archives/edgar/data/109177/000010917726000030/spb-20260626.htm). BlackRock holds 8.3%, American Century 7.3% and the two Vanguard entities 6.4% and 5.2%.
  - Callodine's latest filing: "Names of Reporting Persons Callodine Capital Management, LP", "Percent of class represented by amount in row (9) 7.56 %", with Item 3 box (e) checked: "An investment adviser in accordance with § 240.13d-1(b)(1)(ii)(E)" — [Schedule 13G/A on Spectrum, filed 2026-08-14](https://www.sec.gov/Archives/edgar/data/109177/000092963826003068/xslSCHEDULE_13G_X02/primary_doc.xml). The cover's "Rule 13d-1(b)" box is checked; that is an HTML image attribute, not text.
  - Notes: passive 13d-1(b), so it doesn't count even though two affiliated Callodine advisers report PE funds (Form ADV results).
  - BDC names: "Spectrum Brands", "United Pet Group"
- **PF26 Freshpet**
  - Owner: Freshpet, Inc. is the brand ("We position our brand to benefit from mainstream trends of growing pet humanization") — [Freshpet 10-K, FY2025](https://www.sec.gov/Archives/edgar/data/1611647/000161164726000006/frpt-20251231.htm)
  - 5% holders: "Blackrock, Inc.(3)" 11.4%, "Wasatch Advisors LP(2)" 7.8% and Bank of Montreal entities 5.2% — [Freshpet DEF 14A, filed 2026-04-27](https://www.sec.gov/Archives/edgar/data/1611647/000114036126017084/ny20064241x771_def14a.htm)
  - Newest 13G/A: "Names of Reporting Persons Wellington Management Group LLP", 8.1%, Rule 13d-1(b) box checked — [Schedule 13G/A on Freshpet, filed 2026-11-16](https://www.sec.gov/Archives/edgar/data/1611647/000090221926000369/xslSCHEDULE_13G_X02/primary_doc.xml)
  - Form ADV: Wasatch Advisors N.
  - BDC names: "Freshpet, Inc."
- **PF27 Wellness, Old Mother Hubbard (Wellness Pet Company; Clearlake)**
  - Owner: "today announced it has signed a definitive agreement to acquire The Wellness Pet Food Holdings Company, Inc. (“WellPet” or the “Company”) from affiliates of Berwind Corporation." — [Clearlake, release "Clearlake to Acquire WellPet, A Branded Leader in Premium Natural Pet Food and Treats", November 18, 2020](https://clearlake.com/news/clearlake-to-acquire-wellpet-a-branded-leader-in-premium-natural-pet-food-and-treats/)
  - Brands: "with brands including Wellness®, Old Mother Hubbard®, WHIMZEES®, Eagle Pack®, Holistic Select®, and Sojos®." — [same release](https://clearlake.com/news/clearlake-to-acquire-wellpet-a-branded-leader-in-premium-natural-pet-food-and-treats/)
  - Since: "November 18, 2020" (release dateline). That is the agreement date; no closing statement was read.
  - Brand site: "© Wellness Pet, LLC 2026. All Rights Reserved", and its dog-brand menu lists "… Old Mother Hubbard Protein Bowls …" — [wellnesspetfood.com, accessed 2026-11-17](https://www.wellnesspetfood.com/)
  - Company release boilerplate: "Wellness Pet Company, with 100 years of heritage …", which names no owner — [Wellness Pet Company release, 2026-05-14](https://www.wellnesspet.com/2026/05/14/wellness-pet-company-names-allyson-borozan-chief-marketing-officer/)
  - Current: not confirmed. clearlake.com/portfolio/ stayed on a challenge page in the browser.
  - Affiliate: none found. Neither the homepage footer nor the media center links a program.
  - BDC names: "Wellness Pet LLC", "Wellness Pet Company", "WellPet", "The Wellness Pet Food Holdings Company, Inc.", "Woof"
  - Notes:
    - Counted as PE-owned: a buyout agreement, with no minority stated.
    - Trade-press leads (not cited) describe a May 2025 lender-supported refinancing with $100M of new capital. Whether lenders took equity was not found. A change of control there would change this row.
- **PF29 Aqueon, Best Bully Sticks (Central Garden & Pet)**
  - Owner: "Products are sold under well-recognized brands including Aqueon®, Best Bully Sticks®, Cadet®" — [Central Garden & Pet 10-K, FY ended 2025-09-27](https://www.sec.gov/Archives/edgar/data/887733/000088773325000041/cent-20250927.htm)
  - Control: "William E. Brown 1,600,459 1,386,792(4) 1,432,565(5) 7.1 56.3". The last figure is "Percent of Total Voting Power". — [Central DEF 14A, filed 2025-12-22](https://www.sec.gov/Archives/edgar/data/887733/000114036125046376/ny20057494x771_def14a.htm). The same table lists BlackRock (7.9% of votes), Vanguard (5.8%) and Dimensional (4.1%).
  - Best Bully Sticks site: "© 2026 Best Bully Sticks." — [bestbullysticks.com](https://www.bestbullysticks.com/)
  - Affiliate: "Join the Best Bully Pack Affiliate Program" — [Best Bully Sticks, Affiliates page](https://www.bestbullysticks.com/pages/affiliates). It is linked from the footer ("AMBASSADORS & AFFILIATES"). Directories (not opened) list it on ShareASale or FlexOffers.
  - BDC names: "Central Garden & Pet", "Best Bully Sticks", "Aqueon"

### Rollups and groups that are not brands

Not counted in the 30.
- **Nestlé Purina PetCare Company / Nestlé S.A.:** Beneful, Dog Chow, Purina ONE, Pro Plan (owner not found), plus Cat Chow and Friskies (Smucker's 10-K).
- **Mars, Incorporated / Mars Petcare:** Pedigree, IAMS (US), Royal Canin, Sheba and Greenies. Family-owned.
- **General Mills:** Blue Buffalo, Nudges and Tiki Pets.
- **Colgate-Palmolive / Hill's Pet Nutrition:** Science Diet and Prescription Diet.
- **Post Holdings / Post Consumer Brands:** Nutrish and Kibbles 'n Bits (plus 9Lives, Nature's Recipe and Gravy Train, which are not rows).
- **J.M. Smucker:** Meow Mix and Milk-Bone.
- **Spectrum Brands / Global Pet Care (United Pet Group):** Good'n'Fun and DreamBone.
- **Central Garden & Pet:** Aqueon and Best Bully Sticks.
- **Wellness Pet Company (WellPet):** Wellness and Old Mother Hubbard. Owned by Clearlake per its 2020 release.
- **Diamond Pet Foods / Schell & Kampeter, Inc.:** Diamond. Family-owned per its site.
- **Costco:** Kirkland Signature.

### Category share

**All rows (N = 30; 13 ranked, 17 unranked).**
- **PE-owned: 2 / 30 = 6.7%** (Wellness, Old Mother Hubbard; Clearlake, buyout agreement 2020-11-18). **PE minority stake: 0.** Combined: **2 / 30 = 6.7%**, below the 10% bar.
- **Public company: 17 / 30 = 56.7%.**
  - Nestlé ×2, General Mills ×3, Colgate ×2, Post ×2, Smucker ×2, Spectrum ×2, Central ×2, Freshpet and Costco.
  - No 5%+ holder of any public parent counts: every 13G read is passive (13d-1(b)) or comes from an adviser whose ADV says N, and the one 13D is an individual's.
- **Family: 6 / 30 = 20.0%** (Mars ×5, Diamond).
- **Owner not found: 5 / 30 = 16.7% strict** (Taste of the Wild and four Purina rows); **1 / 30 lenient**.
- **Ranked rows only (N = 13):** PE 0. Public 5 (Blue Buffalo, Kirkland Signature, Hill's Science Diet, Rachael Ray Nutrish, Kibbles 'n Bits). Family 3 (Pedigree, IAMS, Royal Canin). Not found 5 (Beneful, Dog Chow, Purina ONE, Pro Plan, Taste of the Wild).
- **By parent:** 13 parents, counting Taste of the Wild as its own. PE-held parents: 1 / 13 (Wellness Pet Company).
- **By sales:** no brand-level sales figure was found. By the table's company revenue, Wellness Pet Company's $700M is 1.2% of the $57.9B combined revenue of the 10 row parents the table lists. That figure leaves out Post, Costco and Taste of the Wild's owner, and its Nestlé and Mars figures look company-wide rather than US-only.
- **Upper bound if leads were confirmed:** 2 / 30.
  - The four Purina rows and Taste of the Wild have no PE lead.
  - If the Wellness refinancing moved control to lenders, the share could be 0 / 30.
- **Sources disagree:** none. Framing note: IAMS belongs to Mars in the US and to Spectrum in Europe (geographic split, not a conflict).

**Affiliate income:**
- **Brand-direct programs found: 1** (Best Bully Sticks, non-PE).
- **Checked, none found: 3** (Wellness, Old Mother Hubbard, Tiki Pets).
- **Not checked: 26.** These are mainly mass CPG brands sold through retailers. Nestlé's sites were blocked anyway.
- **Overlap with PE:** none found.

## Firms named

Every investment firm named as an owner or 5%+ holder, as the sources name it:
- **Clearlake:** "Clearlake Capital Group, L.P. (together with certain of its affiliates, “Clearlake”)" (Wellness Pet Company). The seller was "affiliates of Berwind Corporation" (not looked up).
- **Holders of public parents:**
  - **Spectrum:** Pzena Investment Management, LLC; Callodine Capital Management, LP; BlackRock, Inc.; American Century Investment Management, Inc.; Vanguard Portfolio Management LLC; Vanguard Capital Management LLC.
  - **Post:** The Vanguard Group; BlackRock, Inc.; Clarkston Capital Partners, LLC; Route One Investment Company, L.P.; Dimensional Fund Advisors LP. Plus William P. Stiritz (13D, individual).
  - **Freshpet:** BlackRock, Inc.; Wasatch Advisors LP; Bank of Montreal entities; Wellington Management Group LLP.
  - **Central:** BlackRock, Inc.; The Vanguard Group; Dimensional Fund Advisors LP; Allspring Global Investments Holdings, LLC. Plus William E. Brown (founder).
  - **General Mills, Smucker, Colgate and Costco:** BlackRock, Vanguard and State Street only.

## Form ADV results (November 2026 files, read locally)

| Firm | CRD | Registered/exempt | Any PE Funds | PE funds | Role |
|---|---|---|---|---|---|
| Clearlake Capital Group, L.P. | 157920 | registered | **Y** | 75 | owner, Wellness Pet Company |
| Clearlake Capital RIC Management, LLC | 342281 | registered | N | – | affiliate |
| Callodine Capital Management, LP | 297115 | registered | N | – | Spectrum 9.0% (13G/A under 13d-1(b), 7.56%) |
| Callodine Credit Management, LLC | 313165 | registered | **Y** | 1 | affiliate of the above |
| Callodine BDC Advisor, LLC | 342427 | registered | **Y** | 2 | affiliate of the above |
| Pzena Investment Management LLC | 106847 | registered | N | – | Spectrum 10.7% |
| American Century Investment Management Inc | 105778 | registered | N | – | Spectrum 7.3% |
| Clarkston Capital Partners, LLC | 143456 | registered | N | – | Post 6.8% |
| Route One Investment Company, L.P. | 156398 | registered | N | – | Post 6.5% |
| Dimensional Fund Advisors LP | 106482 | registered | N | – | Post, Central |
| Wasatch Advisors LP | 106081 | registered | N | – | Freshpet 7.8% |
| JANA Partners Management, LP | 292832 | registered | N | – | none (checked because of JANA's 2022 Freshpet campaign; it is not a current 5% holder in the proxy) |

- Under the rule, Callodine is a PE firm, because two of its registrations report PE funds. Its Spectrum holding still doesn't count: the 13G is filed under Rule 13d-1(b).
- "Wasatch Health Partners" (Med Venture Management, LLC, CRD 335443) reports PE funds, but its website differs from Wasatch Advisors' and it appears to be a separate firm. Not counted.
- BlackRock, Vanguard, State Street, Wellington and Allspring were not looked up. Each files 13Gs under 13d-1(b), so none can count.

## BDC names

- **Matched:** only Wellness.
  - Row: "Debt Investments Food Products Wellness Pet LLC (Woof) Instrument First Lien First Out Term Loan Ref SOFR(Q) Spread 3.95% Total Coupon 7.62% Maturity 12/1/2029".
  - Filer: BlackRock Private Credit Fund, 10-Q for 2026-06-30, in `2026_08_bdc`.
  - No equity row was found.
- **How the match was made:** a word-bounded search of the "Investment, Identifier Axis" column of `2026_07` to `2026_10` `soi.tsv`, for every brand and parent name in the BDC lists above.
- **Not matched:** Mars, Nestlé, Purina, Post, Smucker, General Mills, Colgate, Costco, Spectrum, Central, Freshpet, Diamond and Schell & Kampeter. The first loose grep's hits (Schellman, Williams Industrial) were false positives.

## Affiliate programs

- **Brand-direct:** Best Bully Sticks (https://www.bestbullysticks.com/pages/affiliates), non-PE (Central Garden & Pet).
- **None found:** Wellness and Old Mother Hubbard (wellnesspetfood.com homepage and media center); Tiki Pets (homepage).
- **Not checked:** the other 26 rows.

## Licensed rows

- **Rachael Ray Nutrish (row 11):** Post owns the Nutrish mark. The "Rachael Ray" name is licensed from a third party that Post's 10-K doesn't name. Row owner: Post.
- **IAMS (row 10):** not a licence but a geographic split. Mars holds IAMS in the US, and Spectrum's 10-K lists IAMS and Eukanuba "(Europe only)".
- **Kirkland Signature (row 5):** Costco's own private-label mark. The pet-food maker was not identified in the sources read.

## Surprises

- **The PE presence in this industry is mid-size.** Wellness Pet Company is the only PE-held company above the walk's cut-off. The earlier scan's other PE names (Compana, Nulo, Redbarn, Primal, Ethos, Stella & Chewy's) sit at $50M to $300M in Petfood Industry's table, far below the cut-off.
- **Wellness's own 2026 materials don't name its owner, and Clearlake's portfolio page was blocked**, so the only PE evidence is a 2020 agreement release. Under the engine's 18-month rule, this hop would read "last confirmed 2020-11-18" unless a newer source is found.
- **Spectrum's holder Callodine is a PE firm under the "any registration" rule**, but its holding is passive (13d-1(b)). The engine's 13G rule matters here.
- **Nestlé Purina blocks every domain tried** (Imperva on purina.com, nestleusa.com and purina.ca; Cloudflare on nestle.com). The single largest pet company can't be read by the bot.
- **Tiki Pets and Nudges are General Mills brands** (10-K trademark list), not independent brands.

## Open questions for the developer (numbers only; nothing decided)

1. **Composite cap sensitivity** (PE share by brand row):
   - cap 2 new brands per company (used): **2 / 30 (6.7%)**;
   - cap 3: Wellness falls below the cut-off, **0 / 30**;
   - cap 1: the walk adds one row each for Sunshine Mills, ADM Animal Nutrition, Tuffy's, Whitebridge Pet Brands, Compana, Nulo and Instinct. These weren't researched here; the earlier scan reported Compana and Nulo as PE-held, unverified in this run. Counting those two and Wellness would give up to **3 / 30 (10.0%)**, and more if Instinct, Whitebridge or Sunshine Mills turn out PE-held.
2. **Post Holdings** is missing from the company table. Placed in the walk with up to 2 more rows (Nature's Recipe, 9Lives), it would push Central's 2 rows out. The PE count stays 2 / 30.
3. **Wellness current status:** 2 / 30 if the 2020 release stands. 0 / 30 if the hop is treated as unconfirmed (no source since 2020-11-18), or if the May 2025 refinancing moved control.
4. **Owner not found:** 5 / 30 strict and 1 / 30 lenient, a difference of 4 Purina rows.
5. **Coverage:**
   - 0 litter rows. Tidy Cats, Fresh Step and Arm & Hammer are outside a food-revenue table.
   - Supplies rows: 4 (Spectrum and Central).
   - Store brands: 1 (Kirkland).

## Cost

- **Requests:** 91 logged fetches (81 curl, 10 Playwright), including 28 robots.txt reads.
  - Status mix: 69 × 200, 3 × 301, 15 × 403, 2 × 404 and 2 TLS errors.
  - The 403s break down as 9 Cloudflare challenges to curl (6 of them on petfoodindustry.com), 3 Imperva blocks on Nestlé domains, and 3 challenges that didn't clear in the browser.
- **SEC:** 31 requests, all HTTP 200, about 1 per second.
  - 8 submissions JSON;
  - 4 full-text searches (0 hits);
  - 16 filings (8 × 10-K, 8 × DEF 14A);
  - 3 Schedule 13D/13G documents.
- **WebSearch:** 11 (8 for the ranking, 3 for Wellness's status and affiliate programs). WebFetch: 0.
- **Local data:** Form ADV November 2026 files; BDC `soi.tsv` for 2026_07 to 2026_10. Nothing was re-downloaded.
- **Time:** about 25 minutes of logged fetching (22:58–23:21 UTC), plus writing.
- **Tokens:** not metered by this worker, roughly 320k.
- **Slips:** 1, the tasteofthewildpetfood.com homepage fetch (see "How this was sourced"). It is excluded from evidence.
