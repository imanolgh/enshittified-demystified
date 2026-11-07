# Category audit: Vitamins and supplements

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (fetches logged 17:12–17:37 UTC) · Ownership facts come from primary sources only. Trade press supplies the candidate list only.

**Short answer**

| | Vitamins and supplements (30 composite rows) | Including 5 added rows (N = 35) |
|---|---|---|
| PE-owned plus PE minority stake, by brand row | **3 / 30 (10.0%)**: Thorne (L Catterton), Natrol (New Mountain Capital), The Vitamin Shoppe (Kingswood Capital Management and Performance Investment Partners). All three are control; none is a minority stake. | **5 / 35 (14.3%)**; adds Jarrow Formulas (New Mountain) and Swanson Health (Swander Pace Capital) |
| Pending PE deal | Nature's Bounty and Puritan's Pride: Nestlé agreed on 2026-09-01 to sell its mainstream VMS business to Yellow Wood Partners; closing expected "by the first half of 2027". At closing the share would be **5 / 30 (16.7%)**. | 7 / 35 (20.0%) |
| Strict count (public company with a 5%+ holder whose Form ADV reports PE funds) | **No change found yet.** The only public rows with a 5%+ holder that is not an index or mutual-fund giant are Herbalife (Nantahala Capital Management 8.40%, The Baupost Group 8.33%, Route One Investment Company 7.28%, Renaissance Technologies 5.43%) and Spring Valley (Walmart: Walton Enterprises 44.11%, a family vehicle). Form ADV is for the assembler. | same |
| Owner not found | **3 / 30 (10.0%)**: NOW, Nordic Naturals (both sites' robots.txt disallow ClaudeBot), Life Extension (site returns 403 "Access Denied" even for robots.txt). Plus 2 not reconfirmed: One A Day (Bayer, only a third-party SEC filing; bayer.com and oneaday.com block bots) and GNC (Harbin, 2020 SEC filing, nothing later). | 4 / 35 (adds AG1) |
| Brand-direct affiliate programs | **3 found on ranked rows**: Nature Made (via CJ), Thorne (Ambassador Program, a PE-owned row) and OLLY (TikTok Shop "Open Affiliate Program"). Piping Rock, vitafusion's new owner, runs a store-wide program. **3 more are leads only** (the program pages are blocked): The Vitamin Shoppe (a PE-owned row), GNC and AG1. | |

- **No free top-30 sales ranking exists for this category** in the sources found. The 30 rows are a composite candidate list, not a sales rank (see "Ranking"). So the shares here are softer than the pilot's restaurant and eyewear numbers.
- **Biggest finding:** the category is dominated by large public consumer-health and food groups. Nestlé (6 rows), Unilever (3), Haleon (2), P&G, Kimberly-Clark, Costco, Walmart and Herbalife account for 16 of the 30 rows. PE control shows up in three places: practitioner and natural-channel brands (Thorne, Natrol and, among added rows, Jarrow), a specialty retail chain (The Vitamin Shoppe) and, once the sale closes (expected by H1 2027), Nestlé's mainstream portfolio (Nature's Bounty and Puritan's Pride; USD 1.2 billion of 2025 sales across seven brands).
- **Ownership changed in 2025–26 for 3 rows, and 2 more are pending**, so any ranking from 2024 or earlier is already stale:
  - The Vitamin Shoppe: Franchise Group sold it to Kingswood and PIP on 2025-05-20.
  - vitafusion: Church & Dwight sold it to Piping Rock Health Products on 2025-12-31.
  - Zarbee's: Kimberly-Clark acquired Kenvue on 2026-11-02.
  - Pending: Nature's Bounty and Puritan's Pride, in Nestlé's sale to Yellow Wood.
- **Lenders worth a BDC check:** Thorne's 2023 buyout credit agreement names Churchill Agency Services LLC as administrative agent (see SU21).

## How this was sourced (read first)

- **Ranking:** composite candidate list built from free trade press and a consumer survey; see "Ranking". No ranking was used as evidence of ownership.
- **Ownership facts:** SEC filings (10-K, 20-F, DEF 14A, 8-K), company releases and annual-report PDFs, sponsor portfolio pages, and company sites. Three company documents were read as PDFs, not HTML: Nestlé's 2026-09-01 release, Nestlé's nine-month 2026 sales release and Nestlé's 2025 Financial Statements. Their quotes come from pypdf text with whitespace collapsed.
- **SEC access:** all SEC requests (www.sec.gov, data.sec.gov, efts.sec.gov) used the user agent `EvidenceEngine ownership-research bot (category audit)` with no contact detail, at most 2 requests per second (0.6 s sleep per request). All returned HTTP 200.
- **Robots:**
  - robots.txt was read before each new site fetched with curl.
  - Sites whose robots.txt disallows ClaudeBot / anthropic-ai were not used: newhope.com (publisher of Nutrition Business Journal), nowfoods.com and nordic.com.
  - pharmavite.com sets `Crawl-delay: 10`, and requests there were spaced 10+ seconds apart.
  - Sites whose robots.txt itself returned a bot block, which were not used: digitaledition.chaindrugreview.com (AWS WAF), drugstorenews.com (Cloudflare), oneaday.com and bayer.com (bot block page), lifeextension.com (Akamai 403), puritan.com and nestlehealthscience.us (Imperva 403), gardenoflife.com (403), vitaminshoppe.com (DataDome), drinkag1.com (429) and mastercorporate.nestlehealthscience.com (401, site locked).
  - nestle.com HTML pages returned 403, but its robots.txt allows crawling and its PDFs downloaded normally.
- **Never fetched:** competitor sites (one competitor "ledger" page came up twice in search and was not opened), Reddit, WhoIsMyDentist, Private Equity Vet, PitchBook, Preqin and CB Insights. Deal directories (mergr, privsource, mergerlinks) and affiliate-network listings (FlexOffers, UpPromote, Awin, LinkClicky) were read as search snippets only and are never cited.
- **Owner kinds are research notes, not engine classifications.**
  - "PE-owned" means control, or a PE owner with no stated stake.
  - Counts are by brand row. Nestlé is 6 rows and Unilever is 3.
  - "Not found" means no primary source settled the current owner within about 5 fetches. It is never a guess.
- **Quotes:** copied from the curl'd page text with HTML tags replaced by spaces, whitespace collapsed and entities decoded. No quote came through a WebFetch summarizer (no WebFetch calls were made). Where a ® sits in its own HTML span, the quote is split around it (noted in the row).

## Ranking

**No free, current top-30 ranking of US supplement brands by sales was found.**
- **Nutrition Business Journal** (the trade standard) ranks the "Top 50" supplement companies by US sales. That list sits only in its paid Supplement Business Report ($5,195 for the 2026 edition, per search snippets of store.newhope.com). Its publisher's site, newhope.com, disallows ClaudeBot. Rejected.
- **Chain Drug Review's Circana tables** (drug channel only): the digital edition sits behind an AWS WAF JavaScript challenge, including its robots.txt. Rejected.
- **Drug Store News:** Cloudflare challenge. Rejected.
- **Statista charts:** paywalled. Not used.
- **ASINSIGHT's Amazon "Vitamin Market Report"** (July 2026, https://www.asinsight.com/market-analysis/US/vitamin): covers only Amazon's top-10 listings. Rejected as a ranking.
- **ConsumerLab's 2026 survey** (8,850+ supplement users, https://cdn.consumerlab.com/reports/CLSurveyBrochure2026.pdf): rates satisfaction and lists its 188 brands alphabetically, so it gives no order. It was used as a popularity filter only.

**Composite used (a candidate list, not a sales rank; the # column is a row number):**
- **(a) Trade press:** brands named in Nutraceuticals World, "2025 Top Dietary Supplement Companies and Brands" (Rodman Media, free page; the 2024 issue URL redirects to https://www.nutraceuticalsworld.com/top-company-profile/2024-top-dietary-supplement-companies-and-brands/, which now carries the 2025 edition; fetched 2026-11-07).
  - The page says: "many large, multinational players have sizable market share, including, Nestlé Health Science (Vital Proteins, Garden of Life, Pure Encapsulations, Orgain); Haleon (Centrum, Emergen-C); Bayer (One A Day);". It then names Procter & Gamble's Align, New Chapter and MetaMucil and Unilever's "(Olly Nutrition, Liquid I.V., Smarty Pants, Onnit, Nutrafol)".
  - It names Amway and Herbalife "(about $5 billion in global revenue) remain among the top “direct-selling” companies".
  - It lists past profiles: NOW (2023) and Pharmavite, Nature's Way, Thorne and Nordic Naturals (2024).
  - The quote ends at "Bayer (One A Day);" because the P&G names that follow sit inside links.
- **(b) ConsumerLab filter:** brands in ConsumerLab's 2026 list of 188 brands, each rated by 90 or more respondents. This filter was used to add mass-market and natural-channel leaders.
- **(c) Owner disclosures:** brands whose owner's filing or release shows scale, for example Nestlé's mainstream VMS portfolio (USD 1.2 billion of 2025 sales) and Church & Dwight's former "power brand" vitafusion.
- **(d) Retail:** the two national specialty supplement retail chains (GNC, The Vitamin Shoppe) and the two largest retailer private labels (Kirkland Signature, Spring Valley).
- **Rows by basis:**
  - In ConsumerLab's list: 26 of the 30 rows.
  - Not in it: Airborne and Zarbee's (worker's pick of large mass-market immune and kids' brands; the owner's own page or filing names each brand) and Herbalife and Nutrilite (Nutraceuticals World's direct sellers).
- **Selection bias:** rows were not chosen for their ownership. Thorne is in on (a) and (b); Natrol on (b), as ConsumerLab's 2026 top-rated melatonin brand; The Vitamin Shoppe on (d).
- **Added rows A1–A5** sit outside the 30. They are brands that sources read for other rows showed to have notable owners (Jarrow, Orgain, MegaFood) or that are large online specialty sellers (Swanson, AG1). They are reported separately, as the pilot's eyewear section did.

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Nature Made | Pharmavite LLC, "a subsidiary of Otsuka Pharmaceutical Co., Ltd." | corporate group (Otsuka; listing not confirmed in sources read) | none found | not checked | — (Otsuka Holdings; not in sources read) | product brand (mass, drug, online) | **yes**: https://www.naturemade.com/pages/affiliates (via CJ) | SU1 |
| 2 | Nature's Bounty | Nestlé (Holistic Health portfolio); sale to Yellow Wood Partners agreed 2026-09-01, pending | public company (Nestlé S.A.); **pending sale to PE** | Yellow Wood Partners (buyer, pending) | Nestlé since 2021 (not in sources read); sale expected to close by H1 2027 | — (Nestlé trades on SIX) | product brand | none found | SU2 |
| 3 | Centrum | Haleon plc | public company | none at 5%+ except BlackRock, Inc. 5.22% | not checked | HLN (NYSE ADS; LSE) | product brand | none found | SU3 |
| 4 | One A Day | Bayer (third-party SEC filing, historical wording only) | public company (Bayer AG), **not reconfirmed** | none found | not found | — | product brand | none found (oneaday.com blocks bots) | SU4 |
| 5 | vitafusion | Piping Rock Health Products, Inc. (bought from Church & Dwight, completed 2025-12-31) | private company, owner not stated (site: "three generations") | none found | 2025-12-31 | — | product brand | none found for vitafusion; owner runs a store-wide program at https://www.pipingrock.com/pages/affiliate-program | SU5 |
| 6 | OLLY | Unilever PLC (a "Power Brand" in Beauty & Wellbeing) | public company | none at 5%+ except BlackRock, Inc. 8.5% and The Vanguard Group 5.4% | not checked | UL (NYSE ADS) | product brand | **yes**: "OLLY Open Affiliate Program" for TikTok Shop creators, https://www.olly.com/pages/terms-and-conditions-for-tiktok-shop-creators | SU6 |
| 7 | Emergen-C | Haleon plc | public company | as Centrum | not checked | HLN | product brand | none found | SU7 |
| 8 | Airborne | Reckitt (listed in Reckitt US "Our Brands") | public company (Reckitt; listing not confirmed in sources read) | none found | not checked | — | product brand | none found | SU8 |
| 9 | Culturelle | i-Health, Inc.; trademarks "of dsm-firmenich group" | corporate group (dsm-firmenich; listing not confirmed in sources read) | none found | not checked | — | product brand | none found | SU9 |
| 10 | Metamucil | The Procter & Gamble Company | public company | none at 5%+ (BlackRock 6.70%, Vanguard Capital Management 7.52%) | not checked | PG | product brand | none found | SU10 |
| 11 | Kirkland Signature | Costco Wholesale Corporation (private label) | public company | none at 5%+ (Vanguard 9.79%, BlackRock 7.83%) | not applicable (retailer's own label) | COST | retailer private label | none found | SU11 |
| 12 | Spring Valley | Walmart Inc. (private brand) | public company, family-controlled (Walton Enterprises, LLC 44.11%) | none | not applicable | WMT | retailer private label | Walmart's program is store-wide (pilot, not re-fetched) | SU12 |
| 13 | Nature's Way | Nature's Way; "Our parent company, Schwabe" | corporate parent (Schwabe, European plant-medicine maker); Schwabe's owners not checked | none found | not checked | — | product brand | none found (site has rewards and reseller programs only) | SU13 |
| 14 | Natrol | Vytalogy Wellness (New Mountain Capital, "Current Private Equity Flagship Control") | **PE-owned** | New Mountain Capital | 2020-11 (NMC: "Natrol Investment Date November 2020"); company release dated 2020-12-01 | — | product brand | none found | SU14 |
| 15 | Zarbee's | Kenvue LLC, a wholly owned subsidiary of Kimberly-Clark Corporation (merger closed 2026-11-02) | public company | none at 5%+ (pre-merger proxy: Vanguard 12.2%, BlackRock 7.6%, State Street 5.4%) | 2026-11-02 (Kimberly-Clark) | KMB | product brand | none found | SU15 |
| 16 | Garden of Life | Garden of Life LLC, 100% Nestlé | public company (Nestlé S.A.) | none found | not checked | — | product brand | none found (gardenoflife.com returns 403) | SU16 |
| 17 | Pure Encapsulations | Pure Encapsulations, LLC, 100% Nestlé (kept out of the Yellow Wood sale) | public company (Nestlé S.A.) | none found | not checked | — | product brand (practitioner channel) | none found | SU17 |
| 18 | Solgar | Nestlé (kept out of the Yellow Wood sale) | public company (Nestlé S.A.) | none found | not checked | — | product brand | none found | SU18 |
| 19 | Vital Proteins | Vital Proteins LLC, 100% Nestlé | public company (Nestlé S.A.) | none found | not checked (Nestlé took a majority in 2020; release not fetched) | — | product brand | ambassador program paid in product (search snippet only, page not fetched); no cash affiliate program found | SU19 |
| 20 | NOW | not found | not found | not found | not found | — | not found | not checked (robots disallow) | SU20 |
| 21 | Thorne | Thorne HealthTech, Inc., a wholly owned subsidiary of Healthspan Buyer, LLC ("affiliated funds of L Catterton"); L Catterton lists Thorne as "current" | **PE-owned** | L Catterton | 2023-10-16 | — (delisted 2023) | product brand (DTC and practitioner) | **yes**: Thorne Ambassador Program (commissions), https://www.thorne.com/faq/what-is-thornes-ambassador-program | SU21 |
| 22 | Nordic Naturals | not found | not found | not found | not found | — | not found | not checked (robots disallow) | SU22 |
| 23 | Liquid I.V. | Unilever PLC ("Power Brand") | public company | as OLLY | not checked | UL | product brand | none found | SU23 |
| 24 | Nutrafol | Unilever PLC (acquired 2022; a minority interest remains, holders not named) | public company (majority) | none found | 2022 (per Unilever 20-F) | UL | product brand (DTC, salons, Ulta) | none found (customer referral and stylist-partner programs only) | SU24 |
| 25 | Herbalife | Herbalife Ltd. | public company | 5%+ holders for ADV check: Nantahala Capital Management 8.40%, The Baupost Group 8.33%, Route One Investment Company 7.28%, Renaissance Technologies 5.43% (plus Vanguard 12.08%, BlackRock 7.16%) | not applicable | HLF | direct selling via independent members | none (direct-selling members, not affiliates) | SU25 |
| 26 | Nutrilite | Amway ("Family owned") | family | none | 1972 | — | direct selling via Amway Business Owners | none (direct-selling ABOs, not affiliates) | SU26 |
| 27 | Life Extension | not found | not found | not found | not found | — | not found | not checked (site blocks all requests) | SU27 |
| 28 | Puritan's Pride | Nestlé (Holistic Health portfolio); sale to Yellow Wood Partners pending | public company (Nestlé S.A.); **pending sale to PE** | Yellow Wood Partners (buyer, pending) | sale expected to close by H1 2027 | — | product brand and direct online seller | lead only (puritan.com page in search; site returns 403) | SU28 |
| 29 | GNC | GNC Holdings, LLC ("New GNC"), assets bought by Harbin Pharmaceutical Group Holding Co., Ltd. in 2020 | corporate (Chinese pharmaceutical group); **not reconfirmed** after 2020 | none found | 2020-10-07 | — | not found (franchise mix not in sources read) | lead only: https://www.gnc.com/affiliate.html (in search; page returns 403) | SU29 |
| 30 | The Vitamin Shoppe | Kingswood Capital Management, LP and Performance Investment Partners, LLC; Kingswood lists it as current | **PE-owned** | Kingswood Capital Management; Performance Investment Partners | 2025-05-20 | — | "over 635 company-operated retail stores" plus website | lead only: https://www.vitaminshoppe.com/lp/affiliate (in search; site blocks bots) | SU30 |

**Added rows (not counted in the 30):**

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| A1 | Jarrow Formulas | Vytalogy Wellness (New Mountain Capital, current) | **PE-owned** | New Mountain Capital | 2020-09 ("Jarrow Formulas Investment Date September 2020") | — | product brand | not checked | SU31 |
| A2 | Swanson Health | Swander Pace Capital (portfolio tile "Status Current") | **PE-owned** | Swander Pace Capital | 2016 (Business Wire release in search; not fetched) | — | online, catalog and marketplace seller | none found (partner FAQ has no affiliate program) | SU32 |
| A3 | Orgain | Orgain, LLC, 91.1% Nestlé | public company (Nestlé S.A., majority) | none found | not checked | — | product brand | not checked | SU33 |
| A4 | MegaFood | Pharmavite (Otsuka) | corporate group (Otsuka) | none found | not checked | — | product brand | not checked | SU34 |
| A5 | AG1 | not found | not found (a 2022 company release names minority investors led by Alpha Wave; not fetched) | not found | not found | — | DTC | lead only: drinkag1.com/affiliate-terms (in search; site returns 429) | SU35 |

### Evidence
- **SU1 Nature Made**
  - Owner: "Based in California, Pharmavite is a subsidiary of Otsuka Pharmaceutical Co., Ltd." — [Pharmavite, "Nature Made® Named Top Vitamin Brand in U.S. News & World Report's 2025 Survey", 2025-07, boilerplate](https://www.pharmavite.com/news/2025/07/nature-made-named-top-vitamin-brand-in-u-s-news-world-reports-2025-survey-with-eight-1-rankings/)
  - Brand link: "Through its Nature Made" — [same release](https://www.pharmavite.com/news/2025/07/nature-made-named-top-vitamin-brand-in-u-s-news-world-reports-2025-survey-with-eight-1-rankings/). The boilerplate continues with Bonafide, Equelle, MegaFood and Uqora; the ® marks sit in their own spans.
  - Group link: "Pharmavite LLC Manufacture and sales of nutritional products" — [Otsuka Holdings, Group Companies page, accessed 2026-11-07](https://www.otsuka.com/en/company/group/)
  - Affiliate: "Start profiting by joining our affiliate program and recommending Nature Made products." and "Affiliates earn a commission on all referred sales to NatureMade.com" — [Nature Made, Affiliates page, accessed 2026-11-07](https://www.naturemade.com/pages/affiliates). The sign-up links go to signup.cj.com (CJ, a network).
  - BDC names: "Pharmavite LLC", "Otsuka Pharmaceutical Co., Ltd."
  - Notes: the Otsuka Holdings overview page read has no listing sentence, so no ticker is given. The 5%+ holders of the Otsuka parent were not checked (not an SEC filer).
- **SU2 Nature's Bounty**
  - Owner and pending sale: "Nestlé has agreed to divest its mainstream Vitamins, Minerals and Supplements (VMS) business (the ‘Holistic Health portfolio’) to Yellow Wood Partners for USD 1.0 billion (CHF 0.8 billion)." — [Nestlé press release (PDF), Vevey, 1 September 2026](https://www.nestle.com/sites/default/files/2026-09/agreement-divest-mainstream-vitamins-minerals-supplements-en.pdf)
  - Brands in scope: "The scope of the transaction comprises seven established brands: Nature's Bounty, Osteo Bi-Flex, Ester-C, Gard, Nuun, Puritan's Pride and Sisu" — [same release](https://www.nestle.com/sites/default/files/2026-09/agreement-divest-mainstream-vitamins-minerals-supplements-en.pdf)
  - Timing: "The transaction is subject to applicable regulatory approvals and is expected to close by the first half of 2027." — [same release](https://www.nestle.com/sites/default/files/2026-09/agreement-divest-mainstream-vitamins-minerals-supplements-en.pdf)
  - Still pending in October: "The transaction is subject to regulatory approvals and is expected to close by the first half of 2027." — [Nestlé, nine-month 2026 sales release (PDF)](https://www.nestle.com/sites/default/files/2026-10/nine-month-sales-press-release-2026-en.pdf)
  - Scale: "In 2025, the business generated sales of USD 1.2 billion (CHF 1.0 billion)." — [Nestlé release, 2026-09-01](https://www.nestle.com/sites/default/files/2026-09/agreement-divest-mainstream-vitamins-minerals-supplements-en.pdf)
  - Nestlé listing: "They will be valued at the closing price of the share on the SIX Swiss Exchange on the ex-dividend date 2026." — [Nestlé, Financial Statements 2025 (PDF)](https://www.nestle.com/sites/default/files/2026-02/financial-statements-2025-en.pdf)
  - BDC names: "The Bountiful Company", "Nature's Bounty", "Yellow Wood Partners"
  - Notes: the release does not call Yellow Wood a PE firm. Trade press does (search snippets, not cited), so the firm is in "Firms named" for the Form ADV check. Nestlé's 2025 statements tie goodwill impairment to "The Bountiful Company (TBCo) business". The other brands in the deal (Osteo Bi-Flex, Ester-C, Gard, Nuun, Sisu) are not rows.
- **SU3 Centrum**
  - Owner: "VMS declined low-single digit with an improved performance from Centrum in the second half of the year and good growth in Emergen-C." — [Haleon plc, Annual Report and Form 20-F 2025, filed 2026-03-13](https://www.sec.gov/Archives/edgar/data/1900304/000110465926027443/hln-20251231x20f.htm)
  - Listing: "In addition to our shares being listed on the London Stock Exchange (LSE), Haleon is a foreign private issuer (FPI) with American Depositary Shares (ADSs) listed on the New York Stock Exchange (NYSE)." — [same 20-F](https://www.sec.gov/Archives/edgar/data/1900304/000110465926027443/hln-20251231x20f.htm)
  - Holders: "On 21 March 2025, Pfizer ceased to be a shareholder of the Company, having previously held 32% following demerger." In the same table, BlackRock, Inc. is at 5.22% and Wellington Management Group LLP at 4.98% — [same 20-F](https://www.sec.gov/Archives/edgar/data/1900304/000110465926027443/hln-20251231x20f.htm)
  - BDC names: "Haleon plc", "Haleon", "Centrum"
- **SU4 One A Day**
  - Owner: "Under his leadership, Bayer achieved significant growth of its $1 billion Nutritionals & Digestive Health portfolio, and the One A Day brand achieved the #1 position in the adult multivitamin category." — [Functional Brands Inc., Form 10-K, filed 2026-03-27 (director biography)](https://www.sec.gov/Archives/edgar/data/1837254/000121390026035675/ea0280451-10k_functional.htm)
  - Notes: this is a third party's filing describing past events, not an owner statement, so the row is "not reconfirmed". bayer.com and oneaday.com return a bot-block page to every request, including robots.txt, and were not retried. An EDGAR full-text search ("One A Day" "Bayer", 2023 onward) found only third-party filings.
  - BDC names: "Bayer", "One A Day"
- **SU5 vitafusion**
  - Owner: "On December 9, 2025, the Company announced a definitive agreement to sell the VitaFusion and L’il Critters brands to Piping Rock Health Products, Inc. The sale was completed on December 31, 2025, and included the VitaFusion and L’il Critters brands, relevant trademarks and licenses, and Church & Dwight's former manufacturing and distribution facilities in Vancouver and Ridgefield, Washington." — [Church & Dwight, Form 10-K FY2025, filed 2026-02-12](https://www.sec.gov/Archives/edgar/data/313927/000119312526048139/chd-20251231.htm)
  - Owner kind: "Our roots in the health and wellness industry run deep, spanning over 50 years and three generations." — [Piping Rock, About Us page, accessed 2026-11-07](https://www.pipingrock.com/pages/about-us)
  - Affiliate (owner, store-wide): "When you sign up to be a Piping Rock affiliate, you’ll receive a customized link that you can share in your newsletters, on your website, social media posts, and more." — [Piping Rock, Affiliate Program page](https://www.pipingrock.com/pages/affiliate-program)
  - BDC names: "Piping Rock Health Products, Inc.", "Piping Rock", "VitaFusion"
  - Notes: the page implies a family business but never names an owner, so the owner kind is "private, owner not stated". Search snippets of trade press say "family-owned" (not cited). Church & Dwight's December 2025 release (q4cdn PDF) adds nothing on Piping Rock's owners.
- **SU6 OLLY**
  - Owner: "Our Power Brands: Clear Dermalogica Dove Hourglass K18 Liquid I.V. Nexxus Nutrafol OLLY Paula’s Choice Pond’s Sunsilk TRESemmé Vaseline" — [Unilever PLC, Annual Report on Form 20-F 2025, filed 2026-03-12](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Owner: "Wellbeing grew double-digit, led by Nutrafol and Liquid I.V., while OLLY delivered high single-digit growth supported by premium gummy innovation." — [same 20-F](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Listing: "Unilever’s shares are also traded on the New York Stock Exchange (UL) in the form of American Depositary Shares, with one American Depositary Share representing one Unilever ordinary share." — [same 20-F](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Holders: "As far as Unilever is aware, the only holders of more than 3% of, or 3% of voting rights attributable to, Unilever’s ordinary share capital (‘Disclosable Interests’) on 31 December 2025, were BlackRock, Inc. with a shareholding of 8.5%, The Vanguard Group, Inc. with a shareholding of 5.4% and Wellington Management Company LLP with a shareholding of 3.1%." — [same 20-F](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Affiliate: "OLLY Open Affiliate Program (the “Program”)" — [OLLY, Terms and Conditions for TikTok Shop Creators](https://www.olly.com/pages/terms-and-conditions-for-tiktok-shop-creators). This is a brand-run creator program on TikTok Shop, not on olly.com.
  - BDC names: "Unilever PLC", "OLLY"
- **SU7 Emergen-C**
  - Owner: "Expanded the Emergen-C brand in the US." — [Haleon, Annual Report and Form 20-F 2025](https://www.sec.gov/Archives/edgar/data/1900304/000110465926027443/hln-20251231x20f.htm)
  - Listing and holders: as SU3.
  - BDC names: "Haleon plc"
- **SU8 Airborne**
  - Owner: "Our Brands Airborne Clearasil Durex K-Y Move Free Nutramigen Biofreeze Delsym Enfamil Lysol Mucinex Veet" — [Reckitt US site, navigation "Our Brands", accessed 2026-11-07](https://www.reckitt.com/us/)
  - Notes: menu text, not a sentence. Reckitt's global "Our Brands" page (https://www.reckitt.com/our-brands/) does not list Airborne. Search snippets tie Airborne to Reckitt's 2012 purchase of Schiff Nutrition (trade, not cited). The Reckitt listing and its 5%+ holders were not checked (not an SEC filer).
  - BDC names: "Reckitt", "Airborne"
- **SU9 Culturelle**
  - Owner: "Culturelle®, AZO®, and Estroven® are trademarks of dsm-firmenich group." — [Culturelle home page footer, accessed 2026-11-07](https://www.culturelle.com/)
  - Operating company: "Other i-Health, Inc. brands" — [same page](https://www.culturelle.com/)
  - BDC names: "i-Health, Inc.", "dsm-firmenich"
  - Notes: trademark ownership is stated; ownership of the operating company i-Health is implied. The dsm-firmenich listing was not checked.
- **SU10 Metamucil**
  - Owner: "In personal health care, we are a global market leader among the categories in which we compete, including respiratory treatments, digestive wellness, sleep aids, vitamins and analgesics behind our Vicks, Metamucil, Pepto-Bismol and Neurobion brands." — [Procter & Gamble, Form 10-K FY2026, filed 2026-08-04](https://www.sec.gov/Archives/edgar/data/80424/000008042426000103/pg-20260630.htm)
  - Listing: "P&G trades on the New York Stock Exchange under the stock symbol PG." — [same 10-K](https://www.sec.gov/Archives/edgar/data/80424/000008042426000103/pg-20260630.htm)
  - 5% holders: "The following table shows all entities that are the beneficial owners of more than 5% of any class of the Company’s voting securities:" The table lists BlackRock, Inc. 6.70% and Vanguard Capital Management 7.52% — [P&G, DEF 14A, filed 2026-08-28](https://www.sec.gov/Archives/edgar/data/80424/000119312526372211/pg-20260826.htm)
  - BDC names: "The Procter & Gamble Company"
  - Notes: Nutraceuticals World also names P&G's Align and New Chapter. The P&G 10-K names neither, so they are not rows.
- **SU11 Kirkland Signature**
  - Owner: "We have invested significantly in the development and protection of our well-recognized brands, including the Costco Wholesale trademarks and our private-label brand, Kirkland Signature." — [Costco, Form 10-K FY2026, filed 2026-10-07](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm)
  - Listing: "Our common stock trades on the NASDAQ Global Select Market, under the symbol “COST.”" — [same 10-K](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm)
  - 5% holders: "The following table sets forth information regarding ownership of the common stock by each person or group known to the Company to own more than 5% of the outstanding shares of the common stock on November 7, 2025." The table lists Vanguard Group, Inc. 9.79% and BlackRock, Inc. 7.83% — [Costco, DEF 14A, filed 2025-12-04](https://www.sec.gov/Archives/edgar/data/909832/000090983225000159/cost-20251204.htm)
  - BDC names: "Costco Wholesale Corporation"
- **SU12 Spring Valley**
  - Owner: "We also market lines of merchandise under our private brands, including brands such as:" … "Spring Valley," — [Walmart Inc., Form 10-K FY2026, filed 2026-03-13](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm)
  - Listing: "Our common stock trades on the Nasdaq Global Select Market under the symbol "WMT."" — [same 10-K](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm)
  - 5% holders: the table lists Walton Enterprises, LLC 44.11% and Walton Family Holdings Trust 6.44% — [Walmart, DEF 14A, filed 2026-04-23](https://www.sec.gov/Archives/edgar/data/104169/000119312526173673/wmt-20260423.htm)
  - Affiliate: Walmart's store-wide affiliate program was recorded in the pilot (eyewear, https://affiliates.walmart.com/). It was not re-fetched.
  - BDC names: "Walmart Inc."
- **SU13 Nature's Way**
  - Owner: "Our parent company, Schwabe, is one of the oldest plant-based pharmaceutical manufacturers in Europe." — [Nature's Way, About Us page, accessed 2026-11-07](https://www.naturesway.com/pages/about-us)
  - Notes: Schwabe's own ownership was not checked; schwabe.com is an unrelated US law firm, and the group's own site was not found within the cap. Nature's Way runs a rewards program and an authorized-reseller program (search snippets), with no affiliate program.
  - BDC names: "Nature's Way", "Schwabe"
- **SU14 Natrol**
  - Owner: "Vytalogy Wellness Status Current Private Equity Flagship Control Headquarters Los Angeles, CA Jarrow Formulas Investment Date September 2020 Natrol Investment Date November 2020" — [New Mountain Capital, Portfolio: Vytalogy Wellness, accessed 2026-11-07](https://www.newmountaincapital.com/portfolio/jarrow/)
  - Brand link: "Vytalogy Wellness and its family of brands, Natrol and Jarrow Formulas, is a modern wellness company that fuses science and quality ingredients to create highly-efficacious products that make a transformative impact on consumers’ lives." — [same page](https://www.newmountaincapital.com/portfolio/jarrow/)
  - Since: "Natrol LLC, U.S.-based manufacturer of vitamins, minerals and supplements, announced today that New Mountain Capital has acquired Natrol LLC in a partnership that will enable the decades-old company to continue to expand to its next level of success." — [Natrol, "New Mountain Capital Acquires Natrol" (Chatsworth, CA, December 1, 2020)](https://www.natrol.com/blogs/news/new-mountain-capital-acquires-natrol-llc)
  - Owner kind: "The firm currently manages private equity, public equity, and credit funds with $28 billion in assets under management." — [same release](https://www.natrol.com/blogs/news/new-mountain-capital-acquires-natrol-llc)
  - BDC names: "Vytalogy Wellness", "Natrol LLC", "Jarrow Formulas"
  - Notes: the portfolio grid on https://www.newmountaincapital.com/portfolio/ also carries `data-status="Current Private Equity\nFlagship Control"` for this tile (an HTML attribute). The release says New Mountain also manages "credit funds", so a New Mountain lending vehicle is worth checking in the BDC data.
- **SU15 Zarbee's**
  - Owner: "As a result of the First Merger, a change of control of the Company occurred on the Closing Date and the Initial Surviving Company became a direct wholly owned subsidiary of K-C." — [Kenvue Inc., Form 8-K (Items 2.01, 3.01, 5.01), filed 2026-11-02](https://www.sec.gov/Archives/edgar/data/1944048/000095015726001147/form8-k.htm). K-C is defined there as "Kimberly-Clark Corporation, a Delaware corporation".
  - Since: "On November 2, 2026 (the “ Closing Date ”), pursuant to the Merger Agreement, (i) First Merger Sub merged with and into the Company (the “ First Merger ”), with the Company surviving as a direct wholly owned subsidiary of K-C" — [same 8-K](https://www.sec.gov/Archives/edgar/data/1944048/000095015726001147/form8-k.htm). The spaces inside the curly quotes are in the page text.
  - Brand: "Some of our products, including those under the Lactaid" … "brands, that are marketed in the United States are considered dietary supplement products and are governed by the Dietary Supplement Health and Education Act of 1994" — [Kenvue, Form 10-K FY2025, filed 2026-02-20](https://www.sec.gov/Archives/edgar/data/1944048/000194404826000030/kvue-20251228.htm). The elided words are "® and Zarbee’s ®"; each ® sits in its own span.
  - Listing: "Kimberly-Clark common stock is listed on The Nasdaq Stock Market LLC under the ticker symbol "KMB"." — [Kimberly-Clark, Form 10-K FY2025, filed 2026-02-12](https://www.sec.gov/Archives/edgar/data/55785/000162828026007567/kmb-20251231.htm)
  - 5% holders (pre-merger): "regarding persons or groups known to us to be beneficial owners of more than five percent of our common stock." The table lists The Vanguard Group Inc. 12.2%, BlackRock, Inc. 7.6% and State Street Corporation 5.4% — [Kimberly-Clark, DEF 14A, filed 2026-03-23](https://www.sec.gov/Archives/edgar/data/55785/000162828026020404/kmb-20260323.htm)
  - BDC names: "Kenvue Inc.", "Kenvue LLC", "Kimberly-Clark Corporation"
  - Notes: the holder percentages predate the share issuance to Kenvue holders, so they need a post-merger recheck.
- **SU16 Garden of Life**
  - Owner: "Garden of Life LLC Wilmington (Delaware) 100%" — [Nestlé, Financial Statements 2025 (PDF), "Companies of the Nestlé Group, joint arrangements and associates", United States section](https://www.nestle.com/sites/default/files/2026-02/financial-statements-2025-en.pdf)
  - Not in the sale: the brand is not among the seven in SU2's scope sentence.
  - BDC names: "Garden of Life LLC"
- **SU17 Pure Encapsulations**
  - Owner: "Pure Encapsulations, LLC Wilmington (Delaware) 100%" — [Nestlé, Financial Statements 2025 (PDF)](https://www.nestle.com/sites/default/files/2026-02/financial-statements-2025-en.pdf)
  - Kept: "Pure Encapsulations continues to perform strongly, delivering consistent double-digit sales growth." — [Nestlé, nine-month 2026 sales release (PDF)](https://www.nestle.com/sites/default/files/2026-10/nine-month-sales-press-release-2026-en.pdf)
  - BDC names: "Pure Encapsulations, LLC"
- **SU18 Solgar**
  - Owner: "where brands such as Solgar and Pure Encapsulations continue to perform strongly." — [Nestlé press release (PDF), 2026-09-01](https://www.nestle.com/sites/default/files/2026-09/agreement-divest-mainstream-vitamins-minerals-supplements-en.pdf)
  - Notes: no Solgar entity appears in the 2025 subsidiary list (below the disclosure thresholds, or held through another entity). Ownership rests on Nestlé's CEO calling it one of "our" premium brands in the release. The quote begins mid-sentence; the PDF text has a stray space in "science -led" just before it.
  - BDC names: "Solgar"
- **SU19 Vital Proteins**
  - Owner: "Vital Proteins LLC Wilmington (Delaware) 100%" — [Nestlé, Financial Statements 2025 (PDF)](https://www.nestle.com/sites/default/files/2026-02/financial-statements-2025-en.pdf)
  - Notes: vitalproteins.com pages read (terms and an about URL that returned 404) name no owner. The 2020 majority-stake release is on mastercorporate.nestlehealthscience.com, which is locked (401). Nestlé's 100% figure suggests the founders' remaining stake was bought out; no release saying so was read.
  - BDC names: "Vital Proteins LLC"
- **SU20 NOW**
  - Owner: not found
  - Notes: nowfoods.com robots.txt has "User-agent: ClaudeBot Disallow: /" and the same for anthropic-ai, so the site was not fetched. One search found no primary source. Secondary sources call it family-owned (not cited).
  - BDC names: "NOW Foods"
- **SU21 Thorne**
  - Owner: "The Buyer Parties are affiliated funds of L Catterton." — [Thorne HealthTech, Form 8-K (Items 1.01, 2.01, 5.01 and others), filed 2023-10-16](https://www.sec.gov/Archives/edgar/data/1844280/000119312523256578/d406957d8k.htm)
  - Control: "Following the consummation of the Merger, Thorne became a wholly-owned subsidiary of Parent." — [same 8-K](https://www.sec.gov/Archives/edgar/data/1844280/000119312523256578/d406957d8k.htm). Parent is "Healthspan Buyer, LLC, a Delaware limited liability company" per the same filing.
  - Since: "In connection with the consummation of the Merger, on October 16, 2023, Thorne terminated and repaid in full all outstanding obligations due under its Credit Agreement, dated December 21, 2022, with Fifth Third Bank, National Association." — [same 8-K](https://www.sec.gov/Archives/edgar/data/1844280/000119312523256578/d406957d8k.htm)
  - Current: L Catterton's investments page lists Thorne in the "Flagship_Buyout current Consumer_Brands" tile class — [L Catterton, Investments, accessed 2026-11-07](https://www.lcatterton.com/Investments.html). The status is an HTML class attribute, not visible text.
  - Lender (BDC lead): "On October 16, 2023, Parent, as the borrower, entered into that certain Credit Agreement with Healthspan Intermediate, LLC as holdings, Churchill Agency Services LLC, as administrative agent and collateral agent, and the lenders from time to time party thereto" — [same 8-K](https://www.sec.gov/Archives/edgar/data/1844280/000119312523256578/d406957d8k.htm)
  - Affiliate: "Thorne’s Ambassador Program allows brand advocates to earn commissions by promoting Thorne products within their online community." — [Thorne, FAQ "What is Thorne's Ambassador Program?"](https://www.thorne.com/faq/what-is-thornes-ambassador-program)
  - BDC names: "Thorne HealthTech, Inc.", "Healthspan Buyer, LLC", "Healthspan Intermediate, LLC"
- **SU22 Nordic Naturals**
  - Owner: not found
  - Notes: nordic.com robots.txt disallows ClaudeBot, so the site was not fetched. One search found only secondary pages ("family-owned", "no plans to sell"; not cited). A Norwegian registry hit for "Nordic Naturals AS" (two 50% shareholders, unnamed in the snippet) could not be tied to the US company.
  - BDC names: "Nordic Naturals"
- **SU23 Liquid I.V.**
  - Owner: the Power Brands list and the "Wellbeing grew double-digit, led by Nutrafol and Liquid I.V." sentence in SU6 — [Unilever, Form 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Also: "We are building a segmented supply chain to accelerate our growth in premium products and unlock cost efficiencies, including completing the in-housing of around half of Liquid I.V.’s production." — [same 20-F](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - BDC names: "Liquid I.V."
- **SU24 Nutrafol**
  - Owner and since: "Nutrafol is a blueprint for category growth, with turnover tripling since its 2022 acquisition." — [Unilever, Form 20-F 2025](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm)
  - Minority: "relating to the revaluation of the minority interest liability of Nutrafol and OZiva" — [same 20-F](https://www.sec.gov/Archives/edgar/data/217410/000021741026000007/ul-20251231.htm). The same filing mentions "the step-up acquisitions of Nutrafol". The minority holders are not named.
  - Affiliate: none found; nutrafol.com shows a customer referral program and a "Become a Stylist Partner" page (search results).
  - BDC names: "Nutrafol"
  - Notes: whether any minority holder is an investment firm was not checked.
- **SU25 Herbalife**
  - Owner: "Our common shares are listed on the New York Stock Exchange, or NYSE, and trade under the symbol “HLF.”" — [Herbalife Ltd., Form 10-K FY2025, filed 2026-02-18](https://www.sec.gov/Archives/edgar/data/1180262/000119312526057113/hlf-20251231.htm)
  - Model: "using our science-backed products and the individual coaching provided by our network of independent members." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1180262/000119312526057113/hlf-20251231.htm)
  - 5% holders: "Greater than 5% beneficial owners The Vanguard Group (13) 12,495,374 12.08% Nantahala Capital Management, LLC (14) 8,681,857 8.40% The Baupost Group, L.L.C. (15) 8,609,420 8.33% Route One Investment Company, L.P. (16) 7,528,938 7.28% BlackRock, Inc. (17) 7,401,578 7.16% Renaissance Technologies LLC (18) 5,619,568 5.43%" — [Herbalife, DEF 14A, filed 2026-03-17](https://www.sec.gov/Archives/edgar/data/1180262/000121390026029131/ea0276754-01.htm) (table text, whitespace collapsed)
  - BDC names: "Herbalife Ltd.", "Herbalife"
  - Notes: none of the 5%+ holders controls Herbalife. Nantahala, Baupost and Route One are investment managers whose Form ADV PE-fund flag is for the assembler.
- **SU26 Nutrilite**
  - Owner: "Family owned." — [Amway, Our Story page, accessed 2026-11-07](https://www.amwayglobal.com/our-story/)
  - Brand link and since: "1972 Amway acquires Nutrilite Amway acquires the Nutrilite brand, rounding out our brand offerings to include home, beauty, and nutrition categories." — [same page](https://www.amwayglobal.com/our-story/)
  - Model: "Leveraging that model today, we’re empowering Amway Business Owners" — [same page](https://www.amwayglobal.com/our-story/)
  - BDC names: "Amway", "Nutrilite"
- **SU27 Life Extension**
  - Owner: not found
  - Notes: lifeextension.com returns "Access Denied" (Akamai) even for robots.txt, so it was not retried. ConsumerLab's 2026 release names Life Extension the top-rated catalog/internet brand (the reason for the row), but that is not an owner source.
  - BDC names: "Life Extension"
- **SU28 Puritan's Pride**
  - Owner and pending sale: the scope sentence in SU2 ("Nature's Bounty, Osteo Bi-Flex, Ester-C, Gard, Nuun, Puritan's Pride and Sisu") — [Nestlé press release (PDF), 2026-09-01](https://www.nestle.com/sites/default/files/2026-09/agreement-divest-mainstream-vitamins-minerals-supplements-en.pdf)
  - Affiliate: lead only. A puritan.com affiliate URL (https://puritan.com/house/affiliate_program.asp) surfaced in search, but puritan.com returns 403 (Imperva) to robots.txt.
  - BDC names: "Puritan's Pride", "The Bountiful Company"
- **SU29 GNC**
  - Owner: "Also as previously disclosed, on August 7, 2020, the Debtors entered into a Stalking Horse Agreement (as amended from time to time, the “Stalking Horse Agreement”) with Harbin Pharmaceutical Group Holding Co., Ltd. (“Harbin”), pursuant to which Harbin agreed to acquire substantially all of the Debtors’ assets at the closing of the transactions contemplated therein (the “Closing”)." — [GNC Holdings, Inc., Form 8-K (Items 1.01, 1.02, 2.01, 5.02), filed 2020-10-07](https://www.sec.gov/Archives/edgar/data/1502034/000119312520265653/d25873d8k.htm)
  - Since: "On October 7, 2020, the Debtors and Harbin consummated the Closing, thereby completing the disposition of substantially all of the Debtors’ assets in accordance with the Stalking Horse Agreement." — [same 8-K](https://www.sec.gov/Archives/edgar/data/1502034/000119312520265653/d25873d8k.htm)
  - New entity: "the Debtors (a) transferred substantially all of their assets (other than their Canadian assets) to GNC Holdings, LLC, a Delaware limited liability company formed as a wholly owned subsidiary of the Company (“New GNC”)" — [same 8-K](https://www.sec.gov/Archives/edgar/data/1502034/000119312520265653/d25873d8k.htm)
  - BDC names: "GNC Holdings, LLC", "GNC Holdings, Inc.", "Harbin Pharmaceutical Group Holding Co., Ltd."
  - Notes: there is no primary source after 2020. gnc.com's robots.txt allows crawling, but /affiliate.html returned 403. Harbin's own owners were not settled: its 2020 Schedule 13D/A on GNC lists "Harbin Pharmaceutical Group Co., Ltd." (PRC) as the reporting person without control-person detail, and EDGAR full-text search for "Harbin Pharmaceutical Group" with "CITIC" in 13D filings returned 0 hits.
- **SU30 The Vitamin Shoppe**
  - Owner and since: "LOS ANGELES, May 20, 2025 – Kingswood Capital Management, LP (together with its affiliates, “Kingswood”) and Performance Investment Partners, LLC (“PIP”) are pleased to announce they have completed their acquisition of The Vitamin Shoppe (“The Vitamin Shoppe” or the “Company”), a leading pure-play omnichannel retailer of vitamins and nutritional supplements, from Franchise Group, Inc." — [Kingswood Capital Management, release, 2025-05-20](https://www.kingswood-capital.com/kingswood-capital-management-and-performance-investment-partners-complete-acquisition-of-the-vitamin-shoppe/)
  - Model: "The Company conducts business through over 635 company-operated retail stores under The Vitamin Shoppe and Super Supplements™ banners and via its website." — [same release](https://www.kingswood-capital.com/kingswood-capital-management-and-performance-investment-partners-complete-acquisition-of-the-vitamin-shoppe/)
  - Owner kind: "About Kingswood Capital Management, LP Kingswood Capital Management, LP partners with leading companies in the middle market which stand to benefit from its capital and extensive operating resources." and "Mr. Genender has a long history of private equity investing in both middle market and growth companies" — [same release](https://www.kingswood-capital.com/kingswood-capital-management-and-performance-investment-partners-complete-acquisition-of-the-vitamin-shoppe/). 
  - Current: The Vitamin Shoppe tile carries the class `company-status-current` — [Kingswood, Portfolio, accessed 2026-11-07](https://www.kingswood-capital.com/portfolio/) (an HTML attribute; visible text lists "The Vitamin Shoppe" among portfolio names)
  - Affiliate: lead only (https://www.vitaminshoppe.com/lp/affiliate surfaced in search; vitaminshoppe.com serves a DataDome challenge, including on robots.txt).
  - BDC names: "The Vitamin Shoppe", "Vitamin Shoppe", "Franchise Group, Inc."
  - Notes: neither firm's text says "private equity firm" in the sentences quoted; Kingswood's Form ADV is for the assembler.
- **SU31 Jarrow Formulas (added row A1)**
  - Owner and since: the SU14 portfolio sentence ("Status Current Private Equity Flagship Control … Jarrow Formulas Investment Date September 2020") — [New Mountain Capital, Vytalogy Wellness](https://www.newmountaincapital.com/portfolio/jarrow/)
  - Brand: "Founded in 1977, Jarrow Formulas is a leading independent formulator, manufacturer, and marketer of high-quality and scientifically supported probiotics, vitamins, minerals and supplements (“VMS”)." — [same page](https://www.newmountaincapital.com/portfolio/jarrow/)
  - BDC names: "Jarrow Formulas", "Vytalogy Wellness"
- **SU32 Swanson Health (added row A2)**
  - Owner and current: "Status Current Headquarters Fargo, ND Company Website Swanson Health Products is a marketer and distributor of Swanson-branded and national-branded vitamins and supplements." — [Swander Pace Capital, Portfolio, accessed 2026-11-07](https://www.spcap.com/portfolio) (tile text, whitespace collapsed; the HTML puts this status block in the same carousel item as the Swanson bio)
  - Model: "The company operates a production facility in Fargo, ND, and sells through its website, catalog, online marketplaces, and international distributors." — [same page](https://www.spcap.com/portfolio)
  - Since: 2016, from the Business Wire release title "Swander Pace Capital Acquires Swanson Health Products" (search result only; Business Wire was not fetched)
  - Affiliate: none found (https://www.swansonvitamins.com/pages/faqs-partners has no affiliate program)
  - BDC names: "Swanson Health Products", "Swanson"
- **SU33 Orgain (added row A3)**
  - Owner: "Orgain, LLC Wilmington (Delaware) 91.1%" — [Nestlé, Financial Statements 2025 (PDF)](https://www.nestle.com/sites/default/files/2026-02/financial-statements-2025-en.pdf)
  - Also: "the Group increased its ownership interests in certain subsidiaries, primarily in Hsu Fu Chi (full acquisition of the non-controlling interests) and Orgain (partial acquisition of the non-controlling interests)" — [same PDF](https://www.nestle.com/sites/default/files/2026-02/financial-statements-2025-en.pdf)
  - BDC names: "Orgain, LLC"
  - Notes: the 8.9% minority holders are not named.
- **SU34 MegaFood (added row A4)**
  - Owner: the Pharmavite boilerplate in SU1 lists MegaFood among "its" brands; Otsuka's group page lists "FoodState, Inc. Production and sales of natural and whole food supplements" — [Otsuka Holdings, Group Companies](https://www.otsuka.com/en/company/group/)
  - BDC names: "FoodState, Inc."
- **SU35 AG1 (added row A5)**
  - Owner: not found
  - Notes: drinkag1.com returned HTTP 429 to robots.txt. A January 2022 company release on Business Wire ("Athletic Greens Raises $115M From Alpha Wave Ventures and Strategic Investors…") surfaced in search and was not fetched. It names minority investors, not a controller.
  - BDC names: "Athletic Greens", "AG1"

### Rollups and groups that are not brands
These names group brands, or were the owner's holding vehicle, and are not consumer-facing names in this category. Not counted in the 30.
- **Pharmavite LLC:** groups Nature Made, MegaFood, Bonafide, Equelle and Uqora. Owner: Otsuka Pharmaceutical Co., Ltd. (SU1).
- **Nestlé Health Science:** the Nestlé unit holding the six Nestlé rows. **"Holistic Health portfolio"** is Nestlé's name for the mainstream VMS business being sold to Yellow Wood Partners, which includes The Bountiful Company brands (SU2).
- **Vytalogy Wellness:** groups Natrol and Jarrow Formulas. Owner: New Mountain Capital (SU14).
- **Healthspan Buyer, LLC / Healthspan Intermediate, LLC:** L Catterton's holding vehicles for Thorne (SU21).
- **i-Health, Inc.:** groups Culturelle, AZO and Estroven. Owner: dsm-firmenich group (SU9).
- **Kenvue LLC:** Zarbee's operating parent, now a subsidiary of Kimberly-Clark (SU15).
- **Schwabe:** Nature's Way's parent (SU13).
- **GNC Holdings, LLC ("New GNC"):** GNC's operating entity after the 2020 sale. Owner: Harbin Pharmaceutical Group Holding Co., Ltd. (SU29).
- **Franchise Group, Inc.:** former owner of The Vitamin Shoppe, which sold it in May 2025 (SU30).
- **Amway:** company name; Nutrilite is its supplement brand. Owner: family (SU26).

## Category share

N = 30 composite rows (not a sales ranking).
- **PE-owned (control): 3 / 30 = 10.0%.**
  - Thorne (L Catterton, 2023).
  - Natrol (New Mountain Capital via Vytalogy, 2020).
  - The Vitamin Shoppe (Kingswood and PIP, 2025).
- **PE minority stake: 0 / 30.**
- **PE-owned plus PE minority stake: 3 / 30 = 10.0%.**
- **Pending PE: 2 / 30.** Nature's Bounty and Puritan's Pride go to Yellow Wood Partners if the sale closes (expected by H1 2027). The share would then be 5 / 30 = 16.7%.
- **Public company: 16 / 30 = 53.3%.**
  - Nestlé: Nature's Bounty, Garden of Life, Pure Encapsulations, Solgar, Vital Proteins, Puritan's Pride.
  - Unilever: OLLY, Liquid I.V., Nutrafol.
  - Haleon: Centrum, Emergen-C.
  - One row each: Metamucil (P&G), Kirkland Signature (Costco), Spring Valley (Walmart, family-controlled at 44.11%), Zarbee's (Kimberly-Clark), Herbalife.
- **Corporate-group owner, listing not confirmed in sources read: 3 / 30 = 10.0%.** Nature Made (Otsuka), Airborne (Reckitt), Culturelle (dsm-firmenich).
- **Owner not reconfirmed: 2 / 30 = 6.7%.**
  - One A Day: Bayer, via a third-party filing only.
  - GNC: Harbin Pharmaceutical Group Holding, last primary source 2020.
- **Family: 1 / 30 = 3.3%.** Nutrilite (Amway).
- **Private, ultimate owner not stated: 2 / 30 = 6.7%.**
  - vitafusion: Piping Rock; the site implies a multi-generation family.
  - Nature's Way: Schwabe; Schwabe's owners were not checked.
- **Not found: 3 / 30 = 10.0%.** NOW, Nordic Naturals, Life Extension.
- **Strict count:** no change found yet, so 3 / 30.
  - Form ADV candidates among 5%+ holders of public rows: Herbalife's Nantahala Capital Management, LLC; The Baupost Group, L.L.C.; Route One Investment Company, L.P.; and Renaissance Technologies LLC.
  - The other public rows' 5%+ holders are Vanguard, BlackRock and State Street, which the pilot did not count. Haleon discloses only BlackRock (5.22%) above 5%; Unilever discloses BlackRock (8.5%) and Vanguard (5.4%).
- **With added rows (N = 35):** PE-owned 5 / 35 = 14.3%, adding Jarrow and Swanson; 7 / 35 = 20.0% if the Yellow Wood sale closes. Not found: 4 / 35 (adds AG1).
- **By parent company:**
  - The 30 rows sit under 22 owners: Nestlé, Unilever, Haleon, P&G, Costco, Walmart, Kimberly-Clark, Herbalife, Otsuka/Pharmavite, Reckitt, dsm-firmenich, Bayer, Piping Rock, Schwabe, Amway, New Mountain/Vytalogy, L Catterton, Kingswood/PIP and Harbin, plus NOW, Nordic Naturals and Life Extension as their own (unknown) owners.
  - PE parents: 3 / 22 = 13.6%, or 3 / 19 = 15.8% of the owners that were identified.
  - If the Yellow Wood sale closes, the parent count becomes 23 (Yellow Wood added, Nestlé kept) and PE parents 4 / 23 = 17.4%.
- **By sales:** not computed. Only two rows carry a sales figure in the sources read:
  - Nestlé's mainstream VMS portfolio (Nature's Bounty, Puritan's Pride and five non-row brands): USD 1.2 billion in 2025.
  - vitafusion and L'il Critters: "The VMS brands represented less than 5% of our 2025 net sales." ([Church & Dwight 10-K FY2025](https://www.sec.gov/Archives/edgar/data/313927/000119312526048139/chd-20251231.htm))
- **Sources disagree:** none.
- **Formerly PE among non-PE rows:** not checked in this pass.

## Firms named

As the sources name them, for the assembler's Form ADV check:
- **L Catterton:** "affiliated funds of L Catterton" (Thorne 8-K). Vehicles: "Healthspan Buyer, LLC", "Healthspan Merger Sub, Inc.", "Healthspan Intermediate, LLC".
- **New Mountain Capital:** "New Mountain Capital" (Natrol release, NMC portfolio).
- **Kingswood Capital Management, LP** and **Performance Investment Partners, LLC** (The Vitamin Shoppe).
- **Yellow Wood Partners** (pending buyer of Nature's Bounty and Puritan's Pride; Nestlé release).
- **Swander Pace Capital** (Swanson, added row).
- **Alpha Wave Ventures / Alpha Wave Global** (AG1 2022 minority round; search snippet only, not cited).
- **Lender:** Churchill Agency Services LLC (administrative agent, Thorne 2023 credit agreement; for the BDC match).
- **5%+ holders of public rows:**
  - Herbalife: The Vanguard Group; Nantahala Capital Management, LLC; The Baupost Group, L.L.C.; Route One Investment Company, L.P.; BlackRock, Inc.; Renaissance Technologies LLC.
  - P&G: BlackRock, Inc.; Vanguard Capital Management.
  - Costco: Vanguard Group, Inc.; BlackRock, Inc.
  - Walmart: Walton Enterprises, LLC; Walton Family Holdings Trust.
  - Kimberly-Clark: The Vanguard Group Inc.; BlackRock, Inc.; State Street Corporation.
  - Haleon: BlackRock, Inc. (5.22%); Wellington Management Group LLP is at 4.98%, below 5%.
  - Unilever: BlackRock, Inc.; The Vanguard Group, Inc.; Wellington Management Company LLP is at 3.1%, below 5%.

## Worker log
- **Time:** start 2026-11-07T17:11:17Z, end about 2026-11-07T17:46Z: about 35 minutes wall-clock for 30 rows plus 5 added rows, including the ranking search, writing and the quote self-check.
- **Requests:**
  - WebSearch: 26 (9 on the ranking, 13 on owners, 4 on affiliate programs).
  - WebFetch: 0. Every page was read with curl, so quotes come from raw page text, not a summarizer.
  - Direct HTTP (curl): 112 logged requests, including 40 robots.txt reads and 1 HEAD.
    - 33 went to SEC (submissions JSON ×9, EDGAR full-text search ×4, documents ×20), all HTTP 200 under the contact-free user agent at ≤2 req/s.
    - Status mix: 89 × 200, 10 × 403, 8 × 404, 1 × 401, 1 × 429, 1 × 202 (AWS WAF challenge) and 1 × 301 with no body.
    - Not counted: 2 package downloads from PyPI (pypdf, cryptography) to read the PDFs.
  - Agent tokens: not metered by this worker.
- **Self-check:** a script string-matched the evidence quotes against the saved page text (HTML tags replaced by spaces, whitespace collapsed, curly quotes and dashes normalized; pypdf text for PDFs).
  - 116 extracted quotes were found, plus 16 checked by hand (quotes with inner quote marks, the ranking-section quotes and table-text quotes).
  - The script's 32 "not found" hits were all non-quotes: BDC name lists, note text between two quotes, and the two HTML-attribute statuses (L Catterton, Kingswood), which are not page text.
  - 6 deliberately altered quotes all failed.
- **What was fast:**
  - **SEC filers:** 10-K, 20-F and DEF 14A, about 2 requests each. They settled 13 rows: Haleon ×2, Unilever ×3, P&G, Costco, Walmart, Herbalife, Kimberly-Clark/Zarbee's, Church & Dwight/vitafusion, Thorne and GNC.
  - **One Nestlé PDF of the 2025 Financial Statements:** its subsidiary list gives percentage ownership and settled Garden of Life, Pure Encapsulations, Vital Proteins and Orgain at once. The 2026-09-01 release settled Nature's Bounty, Puritan's Pride and Solgar.
  - **Server-rendered sponsor portfolio pages:** New Mountain, L Catterton, Kingswood and Swander Pace each settled current status in one request.
- **What made brands slow:**
  1. **No usable ranking.** NBJ's Top 50 is paid, and newhope.com disallows ClaudeBot. Chain Drug Review's Circana tables and Drug Store News sit behind bot challenges. The ranking step took 9 searches and about 8 requests before falling back to a composite.
  2. **Robots.txt disallowing ClaudeBot on private brands' own sites:** nowfoods.com and nordic.com. These were the only likely owner sources for two large private brands.
  3. **Bot walls on brand and parent sites:** bayer.com and oneaday.com (block page), lifeextension.com (Akamai), nestle.com HTML and nestlehealthscience.us (Imperva), gardenoflife.com, puritan.com, vitaminshoppe.com (DataDome), gnc.com affiliate page, drinkag1.com (429).
  4. **Ownership changes in 2025–26:** The Vitamin Shoppe (2025-05-20), vitafusion (sold 2025-12-31) and Zarbee's (Kimberly-Clark, 2026-11-02) changed owner; Nature's Bounty and Puritan's Pride are pending. A pre-2025 list would misstate 3 of the 30 rows today, and 5 once the Nestlé sale closes.
  5. **Brand pages that name a parent but not the parent's owner:** Piping Rock ("three generations"), Nature's Way ("Our parent company, Schwabe").
- **Which kinds of brands had no primary source for the owner:**
  - private founder or family brands whose own sites disallow AI crawlers or block bots (NOW, Nordic Naturals, Life Extension);
  - a venture-funded DTC brand whose site rate-limits bots and whose funding release is on Business Wire (AG1);
  - a European parent whose brand sites all block bots (Bayer's One A Day).
- **Notes for the assembler:**
  - **PDF sources:** quotes from Nestlé (SU2, SU16–SU19, SU28, SU33) come from PDFs. The checker needs PDF text extraction. pypdf leaves stray spaces in some words ("science -led", "private -label", "Nestlé ."), and the quotes avoid those spots.
  - **Quotes on attributes or tiles:**
    - L Catterton's Thorne status is an HTML class (`Flagship_Buyout current Consumer_Brands`), and Kingswood's Vitamin Shoppe status is `company-status-current`. Neither is visible text.
    - New Mountain and Swander Pace status lines are tile text with whitespace collapsed.
    - The Reckitt US brand list is navigation text.
  - **Quotes split around ® spans:** SU1 (Nature Made boilerplate) and SU15 (Zarbee's). The Kenvue 8-K's curly quotes carry inner spaces ("“ Closing Date ”") in the page text.
  - **No JavaScript-only pages are cited.**
  - **Not checked:** Vitamin World (a smaller specialty chain) and the other brands in the Nestlé sale (Osteo Bi-Flex, Ester-C, Gard, Nuun, Sisu). Neither has a row.
  - **BDC leads:**
    - Thorne: Healthspan Buyer, LLC, Churchill Agency Services LLC as agent, 2023 credit agreement.
    - Vytalogy Wellness (Natrol, Jarrow): New Mountain also manages credit funds (SU14).
    - The Vitamin Shoppe: Kingswood/PIP 2025 buyout financing (not read).
    - Swanson Health Products.
    - GNC Holdings, LLC.
    - Yellow Wood's acquisition vehicle for the Nestlé portfolio (not yet formed in sources read).
