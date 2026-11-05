# Research: Category audit pilot (restaurants, gyms, eyewear)

Ticket: [52-research-category-audit-pilot](../issues/52-research-category-audit-pilot.md) · Researched 2026-11-04 (US time; fetches logged as 2026-11-05 UTC) · Ownership facts come from primary sources only; trade press supplies the brand rankings only.

**Question:** For the top ~30 US brands in restaurants, gyms and eyewear: what share is owned by private equity today, which brands or parents borrow from public BDCs, which have brand-direct affiliate programs, and would the same method and cost work for ~12 more categories?

**Short answer**

| | Restaurants | Gyms | Eyewear (30 ranked rows) |
|---|---|---|---|
| PE-owned plus PE minority stake | **9 / 30 (30.0%)** | **9 / 30 (30.0%)** | **4 / 30 (13.3%)**; 20.5% of top-30 sales |
| Owner not found | 2 | 7 | 12 |
| Brands whose operating company or parent appears in a BDC schedule of investments (Q2 2026) | 5 | 12 | 4, plus 1 added row (1-800 Contacts) |
| Brand-direct affiliate programs | none found | none found | 4 found: Zenni, GlassesUSA, EyeBuyDirect (all added rows) and Walmart (store-wide). None is on a PE-owned row. |
| Cost per category (one agent) | 25 min, ~171 requests (167 by the worker, 4 by the parent) | 26 min, ~117 requests | 32 min, ~158 requests |

- **BDC overlap overall:** 21 of the 90 ranked brands, through 14 distinct borrowers held by 35 BDCs.
- **BDC overlap among PE brands:** 12 of the 22 brands that are PE-owned or have a PE minority stake appear. That is all 4 in eyewear, 4 of 9 in gyms and 4 of 9 in restaurants.
- **Quote check:** a script checked 162 cited quotes against their pages, and 160 were found verbatim. The other 2 sit behind a page that renders only in a browser.
- **Shared costs:** the BDC, Form ADV and quote-check work is a one-time setup of about 110 further requests. Later categories reuse it.
- **Glossary-strict count:** four public companies have a 5%+ holder whose Form ADV reports PE funds: Burger King, Popeyes, Wendy's and Life Time. Counted as PE minority stake, the shares become restaurants 12/30 (40.0%) and gyms 10/30 (33.3%); eyewear is unchanged. The table above counts them as public (§9, question 3).

## How this was sourced (read first)

**What sources were used**
- **Rankings:** trade press only, named with dates in each section: NRN/Technomic, Athletech News/Wefranch and Vision Monday. No ranking was used as evidence of ownership.
- **Ownership facts:** SEC filings, company and sponsor press releases, sponsor portfolio pages, and company sites. A few company releases were readable only as third-party reprints or law-firm releases, and each is flagged in its row's notes (Culver's, EyeCare Partners 2019, Barry's).
- **Never fetched:**
  - competitor sites (Buy'r, Worse on Purpose, Grass, ShopFair, Ethos), Reddit, WhoIsMyDentist and Private Equity Vet;
  - PitchBook, Preqin and CB Insights results that came up in searches.
- **Leads only, never cited:** deal directories (mergr, privateequityinfo) and affiliate-network listings (FlexOffers, Admitad, Awin).

**How the facts were checked**
- **Quote check:** after the workers finished, the parent downloaded every cited URL with curl and string-matched each quote against the page text. Whitespace, curly quotes, dashes and zero-width characters were normalized; matching was case-sensitive.
  - Scope: the 162 quotes that carry a URL or "same [source]".
  - Result: 160 found and 2 not reachable (EssilorLuxottica's press-release page is a JavaScript wrapper, row E2).
  - Negative control: 6 deliberately altered quotes all failed, so the checker can fail.
  - Not covered: page fields quoted without a sentence, such as portfolio-tile "Status Current" values.
- **Form ADV:** firm names were looked up in the SEC's Nov-2026 monthly adviser files ([`ia110226-registered.zip`, `ia11022026-exempt.zip`](https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers)). The field read is `Any PE Funds` (see §5).
- **BDC data:** DERA BDC data sets `2026_07`–`2026_10` ([page](https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets)). They cover 173 BDCs, and 172 of them have holdings for the period ended 2026-06-30 (147,678 holding rows) (see §6).

**Rules and labels used here**
- **SEC access:** every SEC request (www, efts, data.sec.gov) used the user agent `EvidenceEngine ownership-research bot (category audit pilot)`, which has no email or other contact detail. All were served HTTP 200, so no SEC step had to be skipped. Requests stayed at or under 2 per second.
- **Owner kinds are research notes, not engine classifications** (ADR 0001 governs the product).
  - "PE-owned" means control, or a PE hop with no stated stake (glossary: "A hop with no stated stake counts as control").
  - A public company that a PE fund controls (Jersey Mike's) counts as PE-owned.
  - Counts are by brand row, not by parent: Inspire Brands is 4 rows and Xponential is 5.
  - "Not found" means no primary source settled the current owner within the per-brand cap of about 5 fetches. It is never a guess.
- **Robots:** franchisetimes.com disallows ClaudeBot in robots.txt. One page was fetched before robots.txt was read, and the site was not used after that.

## 1. Results at a glance

| | Restaurants | Gyms | Eyewear (ranked) |
|---|---|---|---|
| Ranking | NRN "2026 Top 500" (Technomic), US systemwide sales 2025, published 2026-06-16 | Composite by location count: Athletech News/Wefranch top 9 (2026-03-19), the rest by each brand's own count | Vision Monday "2025 Top 50 U.S. Optical Retailers", US sales 2024, published 2025-06-18 |
| PE-owned (control) | 8 (26.7%) | 8 (26.7%) | 4 (13.3%) |
| PE minority stake | 1 (3.3%) | 1 (3.3%) | 0 |
| Public company | 16 (53.3%); 3 have a 5%+ holder whose Form ADV reports PE funds (3G for Burger King and Popeyes, Trian for Wendy's) | 7 (23.3%); 1 has 5%+ PE holders (Life Time: Leonard Green 11.2%, TPG 8.0%) | 8 (26.7%); 0 |
| Other | 2 family | 3 founder-led with owner not stated; 4 owner type not confirmed | 4 nonprofit (VSP Vision), 1 health system, 1 family |
| Investment-firm owner, current status not reconfirmed | 1 (Panera / JAB, last primary source 2017) | — | — |
| Not found | 2 (6.7%) | 7 (23.3%) | 12 (40.0%) |
| Upper bound if trade-press leads were confirmed | 10 (33.3%) | 11 (36.7%) | 7 (23.3%) |
| Sources disagree | 0 | 0 (Barry's differs on framing only; both sources put a PE firm in the chain) | 0 |

**Ticket leads, checked:**
- **Roark / Inspire Brands:** confirmed for Dunkin', Sonic, Arby's and Buffalo Wild Wings.
  - The chain rests on two sources. The 2020 Dunkin' tender-offer document says Inspire's parent is "an indirect, majority-owned subsidiary of affiliates of investment funds managed by Roark Capital Management LLC". Roark's portfolio page lists Inspire under "Current Investments" today.
  - Jimmy John's is named on Roark's page as an Inspire brand but is not in the NRN top 30, so it was not checked further.
- **Subway to Roark:** closed 2024-04-30 (Subway newsroom).
- **Jersey Mike's to Blackstone:** closed 2025-01-16, but the lead is out of date. Jersey Mike's listed on the NYSE as **JMKE on 2026-07-31**. At the IPO Blackstone funds held about 76.5% of voting power, and the company is a "controlled company" (424B4).
- **Pizza Hut to LongRange:** **closed 2026-09-01** (Yum! Brands 8-K).
- **Denny's to TriArtisan:** Denny's is outside the NRN top 30 and was not checked.
- **Ravenous list:** not needed. No fact in this file rests on it.
- **Whataburger:** the restaurants worker left it as not found. The parent settled it from the company's own site: BDT Capital Partners holds a majority (2019). BDT calls itself a merchant bank, and its Form ADV reports PE funds.

## 2. Restaurants

**Ranking:** Nation's Restaurant News (NRN staff), "2026 Top 500: The 50 biggest restaurant chains in America", published June 16, 2026, ranking Technomic's 2026 Top 500 by U.S. systemwide sales, data year 2025. https://www.nrn.com/top-500-restaurants/2026-top-500-the-50-biggest-restaurant-chains-in-america. The page says: "Every year, Nation's Restaurant News and sibling publication Restaurant Business provide analysis of Technomic's Top 500 restaurant chains report, which ranks companies by U.S. systemwide sales." The rank order comes from the slide titles ("1. McDonald's" … "50. Red Robin") in the page source. Per-chain sales figures sit in slide images and were not transcribed. Technomic's own press release (April 15, 2026) carries no per-chain list: https://www.technomic.com/press-top-500-report/. Trade press, used for the ranking only.

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | McDonald's | McDonald's Corporation | public company | none at 5%+ (DEF 14A: Vanguard, BlackRock, State Street) | not checked (brand native to parent) | MCD | ~95% franchised | none found | R1 |
| 2 | Starbucks | Starbucks Corporation | public company | none at 5%+ (Capital Research, Capital World, Vanguard) | not checked | SBUX | company-operated plus licensed stores | none found (network listings only, unverified) | R2 |
| 3 | Chick-fil-A | Chick-fil-A (Cathy family) | family | none | not applicable (founder family) | — | Owner-Operator model (franchise-like) | none found | R3 |
| 4 | Taco Bell | Yum! Brands, Inc. | public company | none at 5%+ (Vanguard, BlackRock, Capital International, JPMorgan, T. Rowe) | not checked | YUM | 97% of Yum units franchised/licensed (all concepts) | none found | R4 |
| 5 | Dunkin' | Inspire Brands, Inc. | PE-owned (via Inspire Brands) | Roark Capital | 2020-12-15 | — | franchisor (Inspire is "franchisor and operator") | none found | R5 |
| 6 | Wendy's | The Wendy's Company | public, PE holder? (see note: Trian, owner type not confirmed) | Trian Fund Management 7.9%; Peltz/May group ~16% voting | not checked | WEN | ~95% franchised | none found | R6 |
| 7 | Chipotle Mexican Grill | Chipotle Mexican Grill, Inc. | public company | none at 5%+ (Vanguard, Capital World) | not checked | CMG | company-operated (all U.S./Canada) | none found | R7 |
| 8 | Burger King | Restaurant Brands International Inc. | public, PE holder (3G Funds ~22% voting; 3G owner type not confirmed) | 3G Capital (holder, not controller) | not checked | QSR | >95% of RBI system franchised | none found | R8 |
| 9 | Domino's | Domino's Pizza, Inc. | public company | none (Vanguard, Berkshire Hathaway 9.96%, BlackRock, T. Rowe) | not checked | DPZ | mostly franchised (6,924 U.S. franchised stores) | network listing only (Awin), unverified | R9 |
| 10 | Subway | affiliates of Roark | PE-owned | Roark Capital | 2024-04-30 | — | franchised | none found | R10 |
| 11 | Panda Express | not found | not found | not found | not found | — | not found | none found | R11 |
| 12 | Panera Bread | JAB (indirect parent, per 2017 merger 8-K) | Owner type not confirmed (JAB: "partner-led investment firm") | JAB Holding (PE status not confirmed) | 2017-07-18 | — | not found | none found | R12 |
| 13 | Texas Roadhouse | Texas Roadhouse, Inc. | public company | none at 5%+ (Vanguard, BlackRock) | not checked | TXRH | mostly company-operated (714 company, 102 franchise) | none found | R13 |
| 14 | Popeyes | Restaurant Brands International Inc. | public, PE holder (3G Funds ~22% voting; owner type not confirmed) | 3G Capital (holder) | 2017-03-27 | QSR | >95% of RBI system franchised | none found | R14 |
| 15 | Chili's Grill & Bar | Brinker International, Inc. | public company | none at 5%+ (BlackRock, FMR, Vanguard) | not checked | EAT | mostly company-owned (1,163 company, 472 franchised, Brinker total) | none found | R15 |
| 16 | Raising Cane's | not found | not found | not found | not found | — | not found | none found | R16 |
| 17 | Olive Garden | Darden Restaurants, Inc. | public company | none at 5%+ (Capital World, BlackRock, Vanguard, Wellington) | not checked | DRI | company-operated (87 franchised U.S. units, all Darden) | none found | R17 |
| 18 | Sonic | Inspire Brands, Inc. | PE-owned (via Inspire Brands) | Roark Capital | 2018-12 (8-K filed 2018-12-07) | — | franchisor | none found | R18 |
| 19 | Pizza Hut | LongRange Capital (ex-China) | PE-owned | LongRange Capital | 2026-09-01 | — | franchised (Yum: 97% of units, 2025) | none found | R19 |
| 20 | Dairy Queen | International Dairy Queen Inc. (Berkshire Hathaway subsidiary) | public company (conglomerate parent) | none | not found | BRK.A / BRK.B | franchised (~7,800 franchised restaurants) | none found | R20 |
| 21 | Wingstop | Wingstop Inc. | public company (formerly PE-owned, Roark) | none at 5%+ (BlackRock, T. Rowe, Lone Pine, MFS) | not checked | WING | ~98% franchised | none found | R21 |
| 22 | KFC | Yum! Brands, Inc. | public company | none at 5%+ | not checked | YUM | 97% of Yum units franchised/licensed | none found | R22 |
| 23 | Little Caesars | Ilitch Companies (family) | family | none | not applicable | — | 86% franchise-owned | none found | R23 |
| 24 | Culver's | Culver family (majority); affiliates of Roark (minority) | PE minority stake | Roark Capital | 2017-10-16 (announced) | — | not found | none found | R24 |
| 25 | Whataburger | BDT Capital Partners (majority, via affiliated funds); Dobson family minority | PE-owned (BDT calls itself a merchant bank; its Form ADV reports PE funds) | BDT Capital Partners | 2019 | — | not found | none found | R25 |
| 26 | Arby's | Inspire Brands (buyer formed by Roark in 2011) | PE-owned (via Inspire Brands) | Roark Capital | 2011-07-04 | — | franchisor | none found | R26 |
| 27 | Jack in the Box | Jack in the Box Inc. | public company | none (BlackRock, Vanguard, Capital World, Biglari Capital 5.70%, Jan-2025 proxy) | not checked | JACK | 93% franchised | none found | R27 |
| 28 | Jersey Mike's Subs | Jersey Mike's Subs Inc., controlled by Blackstone funds (~76.5% voting at IPO) | PE-owned (public, Blackstone-controlled) | Blackstone | 2025-01-16 (IPO 2026-07-31) | JMKE | nearly all franchised | none found | R28 |
| 29 | Buffalo Wild Wings | Inspire Brands (affiliate of Arby's) | PE-owned (via Inspire Brands) | Roark Capital | 2018-02-05 | — | franchisor | none found | R29 |
| 30 | Applebee's | Dine Brands Global, Inc. | public company | none at 5%+ (AllianceBernstein, BlackRock, Vanguard, Morgan Stanley); activist 13Ds Nov 2026 | 2007-11-29 | DIN | franchised (1,520 franchised Applebee's) | none found | R30 |

### Evidence
- **R1 McDonald's**
  - Owner: "The Company franchises and operates McDonald’s restaurants in the global restaurant industry." — [McDonald's Corp, Form 10-K FY2025, filed 2026-02-24](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm)
  - Since: not checked (brand native to the listed parent)
  - Model: "Of the 45,356 McDonald's restaurants at year-end 2025, approximately 95% were franchised." — [McDonald's Corp, Form 10-K FY2025, filed 2026-02-24](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm)
  - 5% holders: "beneficial owners of more than 5% of our common stock outstanding as of December 31, 2025" — [McDonald's Corp, DEF 14A, filed 2026-04-07](https://www.sec.gov/Archives/edgar/data/63908/000119312526145548/mcd-20260407.htm) (table lists Vanguard 10.03%, BlackRock 7.3%, State Street 5.1%)
  - Affiliate: none found (checked: two web searches across top chains; only third-party aggregator pages surfaced)
  - BDC names: "McDonald's Corporation"
- **R2 Starbucks**
  - Owner: "Formed in 1985, Starbucks Corporation’s common stock trades on the Nasdaq Global Select Market (“Nasdaq”) under the symbol “SBUX.”" — [Starbucks Corp, Form 10-K FY2025, filed 2025-11-14](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm)
  - Since: not checked
  - Model: "optimizing the mix of company-operated and licensed stores around the world" — [Starbucks Corp, Form 10-K FY2025, filed 2025-11-14](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm)
  - 5% holders: DEF 14A filed 2026-01-26 lists Capital Research Global Investors 6.7%, Capital World Investors 6.6%, The Vanguard Group 10.0% — [Starbucks Corp, DEF 14A](https://www.sec.gov/Archives/edgar/data/829224/000121390026007780/ea0270973-01.htm)
  - Affiliate: none found on brand site; FlexOffers lists a "Starbucks Store Online" program (third-party network listing, not verified, not a brand-direct page): https://www.flexoffers.com/affiliate-programs/starbucks-store-online-affiliate-program
  - BDC names: "Starbucks Corporation"
- **R3 Chick-fil-A**
  - Owner: "Chick-fil-A is still a family business, with Truett's grandson, Andrew, serving as the CEO." — [Chick-fil-A, Who We Are page, accessed 2026-11-05](https://www.chick-fil-a.com/about/who-we-are)
  - Since: not applicable (founder family)
  - Model: "Most Owner-Operators own only one restaurant, meaning they're small business owners who are onsite and actively involved." — [Chick-fil-A, Who We Are page, accessed 2026-11-05](https://www.chick-fil-a.com/about/who-we-are)
  - Affiliate: none found
  - BDC names: "Chick-fil-A, Inc."
  - Notes: the page does not say "privately held"; "family business" is the company's own wording.
- **R4 Taco Bell**
  - Owner: "The Company’s Common Stock trades under the symbol YUM and is listed on the New York Stock Exchange (“NYSE”)." — [Yum! Brands, Form 10-K FY2025, filed 2026-02-20](https://www.sec.gov/Archives/edgar/data/1041061/000104106126000084/yum-20251231.htm)
  - Since: not checked
  - Model: "At December 31, 2025, 97% of our Concepts’ units are operated by independent franchisees or licensees under the terms of franchise or license agreements." — [Yum! Brands, Form 10-K FY2025, filed 2026-02-20](https://www.sec.gov/Archives/edgar/data/1041061/000104106126000084/yum-20251231.htm)
  - 5% holders: DEF 14A filed 2026-04-03 lists Vanguard 12.1%, BlackRock 9.7%, Capital International Investors 7.3%, JP Morgan Chase & Co. 7.3%, T. Rowe Price — [Yum! Brands, DEF 14A](https://www.sec.gov/Archives/edgar/data/1041061/000119312526142078/yum-20260402.htm)
  - Affiliate: none found (an Admitad "Taco Bell Affiliate Program" page surfaced in search; third-party network page, not verified, not brand-direct)
  - BDC names: "Yum! Brands, Inc.", "Taco Bell Corp."
- **R5 Dunkin'**
  - Owner: "Parent is an indirect, majority-owned subsidiary of affiliates of investment funds managed by Roark Capital Management LLC(“Roark”)." — [Vale Merger Sub / Inspire Brands, Offer to Purchase, Exhibit (a)(1)(A) to Schedule TO-T, filed 2020-11-16](https://www.sec.gov/Archives/edgar/data/1357204/000119312520293739/d12583dex99a1a.htm)
  - Owner (Parent = Inspire): "a wholly-owned indirect subsidiary of Inspire Brands, Inc." — [same Offer to Purchase](https://www.sec.gov/Archives/edgar/data/1357204/000119312520293739/d12583dex99a1a.htm)
  - Owner (current): "Inspire Brands is the franchisor and operator of the Arby’s, Buffalo Wild Wings, Jimmy John’s, SONIC, Dunkin’, and Baskin Robbins brands." — [Roark Capital, Portfolio page, "Current Investments" section, accessed 2026-11-05](https://www.roarkcapital.com/portfolio)
  - Since: "Accordingly, on December 15, 2020, Parent and Purchaser will consummate the Merger pursuant to Section 251(h) of the DGCL." — [Schedule TO-T/A, filed 2020-12-15](https://www.sec.gov/Archives/edgar/data/1357204/000119312520317428/d828546dsctota.htm)
  - Model: "Inspire Brands is the franchisor and operator of the Arby’s, Buffalo Wild Wings, Jimmy John’s, SONIC, Dunkin’, and Baskin Robbins brands." — [Roark Capital, Portfolio page, accessed 2026-11-05](https://www.roarkcapital.com/portfolio)
  - Affiliate: none found (FlexOffers "Dunkin Donuts Shop" listing says the program is not currently offered)
  - BDC names: "Inspire Brands, Inc.", "Dunkin' Brands Group, Inc.", "Vale Merger Sub, Inc."
  - Notes: the majority-owned wording is from 2020. Current status rests on Roark listing Inspire under "Current Investments". Trade reports (not cited) say Inspire filed confidentially for an IPO in May 2026; EDGAR full-text search found no public Inspire S-1 as of 2026-11-04.
- **R6 Wendy's**
  - Owner: "The Company’s common stock is traded on the Nasdaq Global Select Market (“Nasdaq”) under the symbol “WEN.”" — [The Wendy's Company, Form 10-K FY2025, filed 2026-02-23](https://www.sec.gov/Archives/edgar/data/30697/000003069726000009/wen-20251228.htm)
  - Holder: "Nelson Peltz, our former Chairman and Chairman Emeritus, Peter May, our Senior Vice Chairman and Matthew Peltz, our former Vice Chairman, beneficially own shares of our outstanding common stock that collectively constitute approximately 16% of the Company’s total voting power as of February 16, 2026." — [The Wendy's Company, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/30697/000003069726000009/wen-20251228.htm). The DEF 14A (filed 2026-04-02) table lists "Trian Fund Management, L.P." at 7.9%, within the Peltz/May holdings — [DEF 14A](https://www.sec.gov/Archives/edgar/data/30697/000119312526140220/d79835ddef14a.htm)
  - Since: not checked
  - Model: "approximately 95% of Wendy’s restaurants are operated by franchisees" — [The Wendy's Company, DEF 14A, filed 2026-04-02](https://www.sec.gov/Archives/edgar/data/30697/000119312526140220/d79835ddef14a.htm)
  - Affiliate: none found
  - BDC names: "The Wendy's Company"
  - Notes: Form ADV: Trian Fund Management, L.P. (CRD 154172) reports `Any PE Funds = Y` (6 PE funds) in the Nov-2026 file, although Trian is widely described as an activist investor. It is a holder, not a controller.
- **R7 Chipotle Mexican Grill**
  - Owner: "Our common stock trades on the New York Stock Exchange under the symbol “CMG.”" — [Chipotle, Form 10-K FY2025, filed 2026-02-04](https://www.sec.gov/Archives/edgar/data/1058090/000105809026000009/cmg-20251231.htm)
  - Since: not checked
  - Model: "as one of the largest restaurant companies that owns and operates all our restaurants in the U.S. and Canada" — [Chipotle, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1058090/000105809026000009/cmg-20251231.htm)
  - 5% holders: DEF 14A filed 2026-04-28 lists The Vanguard Group, Inc. 11.25% and Capital World Investors 7.92% — [Chipotle, DEF 14A](https://www.sec.gov/Archives/edgar/data/1058090/000114036126017294/ny20063214x1_def14a.htm)
  - Affiliate: none found (Admitad page surfaced, not verified)
  - BDC names: "Chipotle Mexican Grill, Inc."
- **R8 Burger King**
  - Owner: "Our common shares trade on the New York Stock Exchange (“NYSE”), our primary stock exchange, and the Toronto Stock Exchange (“TSX”) under the ticker symbol “QSR”." — [Restaurant Brands International, Form 10-K FY2025, filed 2026-02-20](https://www.sec.gov/Archives/edgar/data/1618756/000161875626000017/qsr-20251231.htm)
  - Holder: "The 3G Funds currently beneficially own Partnership exchangeable units representing approximately 22% of the combined voting interest in RBI." — [RBI, DEF 14A, filed 2026-04-23](https://www.sec.gov/Archives/edgar/data/1618756/000119312526171760/d22888ddef14a.htm)
  - Holder kind: "3G Capital Partners LP, a global investment firm" — [RBI, DEF 14A, filed 2026-04-23](https://www.sec.gov/Archives/edgar/data/1618756/000119312526171760/d22888ddef14a.htm)
  - Since: not checked
  - Model: "As of the date of this Annual Report on Form 10-K, over 95% of system-wide restaurants were franchised restaurants." — [RBI, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1618756/000161875626000017/qsr-20251231.htm)
  - Affiliate: none found
  - BDC names: "Restaurant Brands International Inc.", "Restaurant Brands International Limited Partnership", "Burger King Holdings, Inc."
  - Notes: Form ADV: 3G Capital Partners LP (CRD 156934) reports `Any PE Funds = Y` (2 PE funds) in the Nov-2026 file. So RBI has a PE-flagged holder at ~22% of voting interest, which is not control.
- **R9 Domino's**
  - Owner: "Domino’s Pizza, Inc.’s common stock is traded on The Nasdaq Stock Market LLC (“Nasdaq”) under the ticker symbol “DPZ.”" — [Domino's Pizza, Form 10-K FY2025, filed 2026-02-23](https://www.sec.gov/Archives/edgar/data/1286681/000119312526062321/dpz-20251228.htm)
  - Since: not checked
  - Model: "Our U.S. stores segment is comprised primarily of our franchise operations, which consisted of 6,924 franchised stores located in the U.S. as of December 28, 2025." — [Domino's Pizza, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1286681/000119312526062321/dpz-20251228.htm)
  - 5% holders: DEF 14A filed 2026-03-10 lists Vanguard 11.53%, Warren E. Buffett/Berkshire Hathaway Inc. 9.96%, BlackRock 6.74%, T. Rowe Price 6.24% — [Domino's, DEF 14A](https://www.sec.gov/Archives/edgar/data/1286681/000128668126000012/dpz-20260309.htm)
  - Affiliate: none found on brand site; an Awin merchant profile (https://ui.awin.com/merchant-profile/31075) surfaced in search. Region and brand-direct status not verified (search snippets tie Awin to Domino's UK).
  - BDC names: "Domino's Pizza, Inc.", "Domino's Pizza Master Issuer LLC"
- **R10 Subway**
  - Owner: "today completed its previously announced sale to affiliates of Roark." — [Subway newsroom, "Subway® Sale to Roark is Complete", 2024-04-30](https://newsroom.subway.com/2024-04-30-Subway-R-Sale-to-Roark-is-Complete)
  - Owner kind: "Roark is an Atlanta-based private equity firm with $38 billion in equity under management." — [same release](https://newsroom.subway.com/2024-04-30-Subway-R-Sale-to-Roark-is-Complete)
  - Since: "MIAMI, April 30, 2024 /PRNewswire/ -- Subway®, one of the world's largest restaurant brands," — [same release](https://newsroom.subway.com/2024-04-30-Subway-R-Sale-to-Roark-is-Complete)
  - Model: "Subway restaurants are owned and operated by Subway franchisees" — [same release](https://newsroom.subway.com/2024-04-30-Subway-R-Sale-to-Roark-is-Complete)
  - Current: Subway appears under "Current Investments" on [Roark Capital, Portfolio page, accessed 2026-11-05](https://www.roarkcapital.com/portfolio)
  - Affiliate: none found
  - BDC names: "Subway" (operating-company legal name not found in sources read)
- **R11 Panda Express**
  - Owner: not found
  - Since: not found
  - Model: not found
  - Affiliate: none found
  - BDC names: "Panda Restaurant Group, Inc."
  - Notes: slow, 4 fetches and 2 searches. pandarg.com pages are script-rendered, and the About page fetched has no ownership sentence. pandaexpress.com returned HTTP 403. A 2013 GlobeNewswire company release returned 403. Only secondary profiles say "family-owned" (not cited).
- **R12 Panera Bread**
  - Owner: "As a result of the Merger, the Company became a wholly owned subsidiary of Parent and an indirect subsidiary of JAB." — [Panera Bread Co, Form 8-K, filed 2017-07-18](https://www.sec.gov/Archives/edgar/data/724606/000119312517229854/d425559d8k.htm)
  - Owner kind: "JAB Holding Company is a partner-led investment firm with generational capital." — [JAB Holding Company, About page, accessed 2026-11-05](https://www.jabholco.com/about/)
  - Since: "Trading of Class A Common Stock on the NASDAQ was suspended as of approximately 9:00 am EST on July 18, 2017." — [Panera Bread Co, Form 8-K, filed 2017-07-18](https://www.sec.gov/Archives/edgar/data/724606/000119312517229854/d425559d8k.htm)
  - Model: not found (panerabread.com franchise page returned 404)
  - Affiliate: none found
  - BDC names: "Panera Bread Company", "Panera Brands", "JAB Holdings B.V.", "Rye Parent Corp."
  - Notes: no primary source after 2017 confirms that JAB still owns Panera; jabholco.com/investments is script-rendered with no listing in the HTML or WordPress API. EDGAR shows no Panera Brands S-1 (searched 2025-06 to 2026-11). Form ADV: JAB Consumer Fund Management SARL (ERA, CRD 299567) reports `Any PE Funds = Y` (10 PE funds), and JAB Capital Management, LLC (ERA, CRD 320809) reports `N`. Which JAB entity advises the fund that holds Panera is not stated in any source read.
- **R13 Texas Roadhouse**
  - Owner: "Our common stock is traded on the Nasdaq Global Select Market under the symbol TXRH." — [Texas Roadhouse, Form 10-K FY2025, filed 2026-02-27](https://www.sec.gov/Archives/edgar/data/1289460/000110465926021292/txrh-20251230x10k.htm)
  - Since: not applicable (founding company)
  - Model: "Of the 714 restaurants we owned and operated, we operated 648 as Texas Roadhouse restaurants, 56 as Bubba’s 33 restaurants, and ten as Jaggers restaurants." — [Texas Roadhouse, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1289460/000110465926021292/txrh-20251230x10k.htm)
  - 5% holders: DEF 14A filed 2026-04-10 lists Vanguard 9.6% and BlackRock 9.3% — [Texas Roadhouse, DEF 14A](https://www.sec.gov/Archives/edgar/data/1289460/000110465926041771/txrh-20260521xdef14a.htm)
  - Affiliate: none found
  - BDC names: "Texas Roadhouse, Inc."
- **R14 Popeyes**
  - Owner: "Our common shares trade on the New York Stock Exchange (“NYSE”), our primary stock exchange, and the Toronto Stock Exchange (“TSX”) under the ticker symbol “QSR”." — [RBI, Form 10-K FY2025, filed 2026-02-20](https://www.sec.gov/Archives/edgar/data/1618756/000161875626000017/qsr-20251231.htm)
  - Since: "Accordingly, following the consummation of the Offer, Parent and Sub effected the Merger pursuant to Section 302A.621 of the MBCA, with the Company continuing as the surviving corporation in the Merger and thereby becoming an indirect, wholly-owned subsidiary of Parent." — [Popeyes Louisiana Kitchen, Form 8-K, filed 2017-03-27](https://www.sec.gov/Archives/edgar/data/1041379/000119312517097222/d269346d8k.htm). In the same 8-K, Parent is "Restaurant Brands International Inc., a corporation existing under the laws of Canada"; the tender closed March 27, 2017.
  - Model: "As of the date of this Annual Report on Form 10-K, over 95% of system-wide restaurants were franchised restaurants." — [RBI, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1618756/000161875626000017/qsr-20251231.htm)
  - Affiliate: none found
  - BDC names: "Restaurant Brands International Inc.", "Popeyes Louisiana Kitchen, Inc."
  - Notes: 3G Funds hold ~22% of RBI voting interest (see R8).
- **R15 Chili's Grill & Bar**
  - Owner: "Our common stock is traded on the New York Stock Exchange (“NYSE”) under the symbol “EAT”, and as of August 11, 2026, there were 296 holders of record of our common stock." — [Brinker International, Form 10-K FY2026, filed 2026-08-19](https://www.sec.gov/Archives/edgar/data/703351/000070335126000029/eat-20260624.htm)
  - Since: not checked
  - Model: "As of June 24, 2026, we owned, operated or franchised 1,635 restaurants, consisting of 1,163 Company-owned restaurants and 472 franchised restaurants, located in the United States, 28 other countries and two United States territories." — [Brinker International, Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/703351/000070335126000029/eat-20260624.htm)
  - 5% holders: DEF 14A filed 2026-09-25 lists BlackRock 15.63%, FMR LLC 15.58%, Vanguard Portfolio Management 5.97%, Vanguard Capital Management 5.43% — [Brinker, DEF 14A](https://www.sec.gov/Archives/edgar/data/703351/000119312526402857/d86754ddef14a.htm)
  - Affiliate: none found
  - BDC names: "Brinker International, Inc."
- **R16 Raising Cane's**
  - Owner: not found
  - Since: not found
  - Model: not found
  - Affiliate: none found
  - BDC names: "Raising Cane's"
  - Notes: raisingcanes.com returned HTTP 403 to automated fetches (about and company pages), and I did not try to get around it. A search for a company press release found only press coverage ("founder and owner", "privately held"); not cited.
- **R17 Olive Garden**
  - Owner: "The principal United States market on which our common shares are traded is the New York Stock Exchange, where our shares are traded under the symbol DRI." — [Darden Restaurants, Form 10-K FY2026, filed 2026-07-24](https://www.sec.gov/Archives/edgar/data/940944/000094094426000025/dri-20260531.htm)
  - Since: not checked
  - Model: "Through subsidiaries, we own and operate all of our restaurants in the United States, except for four restaurants operating under contractual agreements, one restaurant that we jointly own with a third party and operate independently, and 87 franchised restaurants." — [Darden, Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/940944/000094094426000025/dri-20260531.htm)
  - 5% holders: DEF 14A filed 2026-08-10 lists Capital World Investors 12.87%, BlackRock 8.08%, Vanguard Capital Management 7.56%, Wellington 6.00% — [Darden, DEF 14A](https://www.sec.gov/Archives/edgar/data/940944/000119312526342023/dri-20260804.htm)
  - Affiliate: none found
  - BDC names: "Darden Restaurants, Inc."
- **R18 Sonic**
  - Owner: "a Delaware corporation and wholly owned subsidiary of Inspire Brands, Inc." — [Sonic Corp, Form 8-K (Items 2.01/3.01/5.01), filed 2018-12-07](https://www.sec.gov/Archives/edgar/data/868611/000094787118000950/ss117852_8k.htm)
  - Since: "As a result of the Merger, the Company became a wholly owned subsidiary of Parent." — [Sonic Corp, Form 8-K, filed 2018-12-07](https://www.sec.gov/Archives/edgar/data/868611/000094787118000950/ss117852_8k.htm)
  - Model: "Inspire Brands is the franchisor and operator of the Arby’s, Buffalo Wild Wings, Jimmy John’s, SONIC, Dunkin’, and Baskin Robbins brands." — [Roark Capital, Portfolio page, accessed 2026-11-05](https://www.roarkcapital.com/portfolio)
  - Affiliate: none found
  - BDC names: "Sonic Corp.", "Inspire Brands, Inc."
  - Notes: the Inspire to Roark link is as in R5 (2020 SEC filing plus Roark's current portfolio page).
- **R19 Pizza Hut**
  - Owner: "will be acquired by LongRange Capital (“LongRange”), a private equity firm with a customer-centric and operationally oriented approach" — [Yum! Brands, Form 8-K Ex. 99.1, filed 2026-06-16](https://www.sec.gov/Archives/edgar/data/1041061/000119312526271893/d158986dex991.htm)
  - Since: "Yum! Brands Completes Sale of Pizza Hut to LongRange Capital" — [Yum! Brands, Form 8-K Ex. 99.1, "LOUISVILLE, Ky., September 1, 2026", filed 2026-09-01](https://www.sec.gov/Archives/edgar/data/1041061/000104106126000187/a8kex991912026.htm)
  - Model: "At December 31, 2025, 97% of our Concepts’ units are operated by independent franchisees or licensees under the terms of franchise or license agreements." — [Yum! Brands, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1041061/000104106126000084/yum-20251231.htm) (pre-sale; Yum-wide figure)
  - Affiliate: none found
  - BDC names: "Pizza Hut", "LongRange Capital" (acquiring entity's legal name not read; it is in Yum 10-Q Ex. 2.1, filed 2026-08-05)
  - Notes: the lead ("reported in 2026, closing unconfirmed") is now resolved: closing confirmed by the Yum 8-K of 2026-09-01. Pizza Hut in mainland China went to Yum China Holdings (closed 2026-08-07, same release).
- **R20 Dairy Queen**
  - Owner: "International Dairy Queen Inc. develops and services a worldwide system of approximately 7,800 franchised restaurants" — [Berkshire Hathaway, Form 10-K FY2025, filed 2026-03-02](https://www.sec.gov/Archives/edgar/data/1067983/000119312526083899/brka-20251231.htm)
  - Parent kind: "is a holding company owning subsidiaries engaged in numerous diverse business activities." — [Berkshire Hathaway, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1067983/000119312526083899/brka-20251231.htm)
  - Since: not found (dairyqueen.com history page returned HTTP 403; the 10-K gives no acquisition year)
  - Model: same 10-K sentence ("approximately 7,800 franchised restaurants")
  - Affiliate: none found
  - BDC names: "International Dairy Queen Inc.", "Berkshire Hathaway Inc."
- **R21 Wingstop**
  - Owner: "Since 2015, Wingstop Inc.’s common stock has traded on the Nasdaq Global Select Market under the symbol “WING.”" — [Wingstop, Form 10-K FY2025, filed 2026-02-18](https://www.sec.gov/Archives/edgar/data/1636222/000163622226000008/wing-20251227.htm)
  - Since: not applicable
  - Model: "The Company is primarily a franchisor, with approximately 98% of Wingstop’s restaurants currently owned and operated by independent franchisees." — [Wingstop, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1636222/000163622226000008/wing-20251227.htm)
  - 5% holders: DEF 14A filed 2026-04-02 lists BlackRock 9.96%, T. Rowe Price 7.83%, Lone Pine Capital 5.43%, MFS 5.1% — [Wingstop, DEF 14A](https://www.sec.gov/Archives/edgar/data/1636222/000119312526140360/d49901ddef14a.htm)
  - History (Formerly PE-owned): "was previously the Chairman of the Board of Roark’s prior investment in Wingstop" — [Inspire Brands, About page (board bio of Neal Aronson), accessed 2026-11-05](https://www.inspirebrands.com/about/); Roark lists Wingstop under "Previous Investments" ([Roark portfolio](https://www.roarkcapital.com/portfolio)). Years not found.
  - Affiliate: none found
  - BDC names: "Wingstop Inc."
- **R22 KFC**
  - Owner: "The Company’s Common Stock trades under the symbol YUM and is listed on the New York Stock Exchange (“NYSE”)." — [Yum! Brands, Form 10-K FY2025, filed 2026-02-20](https://www.sec.gov/Archives/edgar/data/1041061/000104106126000084/yum-20251231.htm)
  - Since: not checked
  - Model: "At December 31, 2025, 97% of our Concepts’ units are operated by independent franchisees or licensees under the terms of franchise or license agreements." — [Yum! Brands, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1041061/000104106126000084/yum-20251231.htm)
  - Affiliate: none found
  - BDC names: "Yum! Brands, Inc.", "KFC Corporation"
- **R23 Little Caesars**
  - Owner: "a privately held, family-owned group of businesses" — [Ilitch Companies, About page, accessed 2026-11-05](https://www.ilitchcompanies.com/about)
  - Brand link: "1959, with a single Little Caesars restaurant in Garden City, Michigan" — [Ilitch Companies, About page](https://www.ilitchcompanies.com/about)
  - Since: not applicable (founder family)
  - Model: "86% of Little Caesars Restaurants are Franchise Owned" — [Little Caesars Franchising site, accessed 2026-11-05](https://franchise.littlecaesars.com/)
  - Affiliate: none found
  - BDC names: "Little Caesars", "Ilitch Companies"
- **R24 Culver's**
  - Owner: "The Culver family will maintain a majority ownership of the company." — [Culver Franchising System, Inc. press release (Business Wire), 2017-10-16, reprinted on franchising.com](https://www.franchising.com/amp/news/20171016_culverrsquos_sells_minority_interest_to_atlantabas.html)
  - PE stake: "The agreement involves individual Culver’s shareholders selling a minority of their shares to affiliates of Roark." — [same release](https://www.franchising.com/amp/news/20171016_culverrsquos_sells_minority_interest_to_atlantabas.html)
  - Current: "Culver's is a family-favorite restaurant known for their ButterBurgers, Fresh Frozen Custard & Wisconsin Cheese Curds." — [Roark Capital, Portfolio page, "Current Investments" section, accessed 2026-11-05](https://www.roarkcapital.com/portfolio)
  - Since: October 16, 2017 (announcement dateline "PRAIRIE DU SAC, Wis. - October 16, 2017" in the same release; closing date not found)
  - Model: not found (culvers.com franchise/about URLs returned 404)
  - Affiliate: none found
  - BDC names: "Culver Franchising System, Inc."
  - Notes: the release is a reprint on a third-party site. Roark's own copy (roarkcapital.com/files/Culvers%20Announcement%20final.pdf) now returns "Page Not Found". The stake size is not disclosed ("a minority"), so under the glossary this is a minority hop: PE minority stake.
- **R25 Whataburger**
  - Owner: "SAN ANTONIO – Whataburger announced today that BDT Capital Partners, LLC, a merchant bank that advises and invests in family and founder-led companies, has agreed to acquire through its affiliated funds a majority interest in Whataburger." — [Whataburger, "Whataburger Positions Itself for the Future", 2019-06-14](https://stories.whataburger.com/whataburger-positions-itself-for-the-future/)
  - Since / current: "2019 - BDT Capital Partners acquired a majority interest in Whataburger." — [Whataburger, Our History, accessed 2026-11-05](https://stories.whataburger.com/our-history/)
  - Model: not found
  - Affiliate: none found
  - BDC names: "Whataburger"
  - Notes: settled by the parent, not the worker: 2 searches and 2 page downloads. The release date (June 14, 2019) comes from the PR Newswire copy of the same release (https://www.prnewswire.com/news-releases/whataburger-positions-itself-for-the-future-300868057.html, not fetched). The company's history page still lists the 2019 deal and no later sale. That is the only current-status signal, so the "last confirmed" date is the fetch date. The Dobson-family minority is in press coverage of the release, not in the sentences quoted here. Form ADV: BDT Capital Partners, LLC (CRD 160914) reports `Any PE Funds = Y` (45 PE funds) in the Nov-2026 file. BDT's self-description is "merchant bank", so the owner kind is PE by the ADV test, not by the firm's own label.
- **R26 Arby's**
  - Owner: "(NYSE: WEN) today announced that it has completed the sale of Arby's Restaurant Group, Inc. on the terms previously announced to a buyer formed by Roark Capital Group, effective as of July 4, 2011." — [Wendy's/Arby's Group, Form 8-K Ex. 99.1, filed 2011-07-05](https://www.sec.gov/Archives/edgar/data/30697/000003069711000041/a991pressreleasedatedjuly5.htm)
  - Current: "Arby's, a brand within the Inspire Brands portfolio, is a bold, differentiated hot sandwich leader where premium proteins, iconic flavor, and unapologetic creativity redefine what fast food can be." — [Roark Capital, Portfolio page, "Current Investments", accessed 2026-11-05](https://www.roarkcapital.com/portfolio)
  - Since: "effective as of July 4, 2011" (same 2011 release)
  - Model: "Inspire Brands is the franchisor and operator of the Arby’s, Buffalo Wild Wings, Jimmy John’s, SONIC, Dunkin’, and Baskin Robbins brands." — [Roark Capital, Portfolio page](https://www.roarkcapital.com/portfolio)
  - Affiliate: none found
  - BDC names: "Arby's Restaurant Group, Inc.", "ARG Holding Corporation", "ARG IH Corporation", "Inspire Brands, Inc."
  - Notes: in 2011 Wendy's said it would "retain an 18.5% common stock interest in the Arby's business"; whether it still holds that stake was not checked.
- **R27 Jack in the Box**
  - Owner: "Our common stock is traded on the NASDAQ Global Select Market under the symbol “JACK.”" — [Jack in the Box, Form 10-K FY2025, filed 2025-11-19](https://www.sec.gov/Archives/edgar/data/807882/000080788225000072/jack-20250928.htm)
  - Since: not applicable
  - Model: "Of those total Jack in the Box restaurants at fiscal year-end, 1,986, or 93%, were franchised." — [Jack in the Box, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/807882/000080788225000072/jack-20250928.htm)
  - 5% holders: DEF 14A filed 2025-01-27 (the newest one found) lists BlackRock 15.95%, Vanguard 12.53%, Capital World Investors 8.52%, Biglari Capital Corp. 5.70% — [Jack in the Box, DEF 14A](https://www.sec.gov/Archives/edgar/data/807882/000080788225000004/jack-20250127.htm)
  - Affiliate: none found
  - BDC names: "Jack in the Box Inc.", "Jack in the Box Funding, LLC"
  - Notes: an 8-K filed 2026-09-21 amends a "Nomination and Cooperation Agreement" with GreenWood Investors, LLC (activist, not control).
- **R28 Jersey Mike's Subs**
  - Owner: "Upon the closing of this offering, our Sponsor will beneficially own approximately 76.5% of the combined voting power of our shares eligible to vote in the election of our directors (or 74.5% if the underwriters exercise in full their option to purchase additional shares of Class A common stock)." — [Jersey Mike's Subs Inc., Prospectus (424B4), filed 2026-07-31](https://www.sec.gov/Archives/edgar/data/2127043/000119312526326453/project_70_424b4.htm)
  - Sponsor = Blackstone: "“Blackstone” or “our Sponsor” refers to investment funds associated with Blackstone Inc." — [same prospectus](https://www.sec.gov/Archives/edgar/data/2127043/000119312526326453/project_70_424b4.htm)
  - Control: "As a result, we will be a “controlled company” within the meaning of the NYSE corporate governance standards." — [same prospectus](https://www.sec.gov/Archives/edgar/data/2127043/000119312526326453/project_70_424b4.htm)
  - Since: "On January 16, 2025, we were acquired by the Buyer (as defined herein) as a new portfolio investment for a purchase price of $6.3 billion." — [same prospectus](https://www.sec.gov/Archives/edgar/data/2127043/000119312526326453/project_70_424b4.htm)
  - IPO: "On July 31, 2026, we completed the offering of 43 million shares of Class A common stock, par value $0.0001 per share (the “Class A common stock”), 30 million of which were sold by certain of our pre-IPO owners consisting of entities associated with Blackstone Inc." — [Jersey Mike's Subs Inc., Form 10-Q, filed 2026-10-28](https://www.sec.gov/Archives/edgar/data/2127043/000212704326000018/jmke-20260927.htm)
  - Model: "with 3,300 stores across all 50 states and two countries – nearly all of which are franchised." — [same prospectus](https://www.sec.gov/Archives/edgar/data/2127043/000119312526326453/project_70_424b4.htm)
  - Affiliate: none found
  - BDC names: "Jersey Mike's Subs Inc.", "Jersey Mike's Holdings", "Jersey Mike's Franchise Systems, LLC", "Submarine Buyer LLC"
  - Notes: the lead ("Blackstone, closed January 2025") holds, but the brand is now also NYSE-listed (JMKE, since July 2026). The 76.5% voting figure is at IPO; the post-IPO percentage was not checked (see Form 4 / 13G filings Aug–Oct 2026). The Blackstone funds named include "Blackstone Capital Partners IX L.P. and Blackstone Private Equity Strategies Fund L.P." (prospectus, Services and Information Agreements).
- **R29 Buffalo Wild Wings**
  - Owner: "As a result of the Merger, a change in control of BWW occurred, and BWW is now a wholly owned subsidiary of an affiliate of Arby’s." — [Buffalo Wild Wings, Form 8-K, filed 2018-02-05](https://www.sec.gov/Archives/edgar/data/1062449/000106244918000022/bwld2018258k.htm)
  - Current: Buffalo Wild Wings is in Roark's "Current Investments" and named in "Inspire Brands is the franchisor and operator of the Arby’s, Buffalo Wild Wings, Jimmy John’s, SONIC, Dunkin’, and Baskin Robbins brands." — [Roark Capital, Portfolio page, accessed 2026-11-05](https://www.roarkcapital.com/portfolio)
  - Since: "prior to the open of trading on February 5, 2018" — [Buffalo Wild Wings, Form 8-K, filed 2018-02-05](https://www.sec.gov/Archives/edgar/data/1062449/000106244918000022/bwld2018258k.htm) (Closing Date February 5, 2018)
  - Model: Roark sentence above ("franchisor and operator")
  - Affiliate: none found
  - BDC names: "Buffalo Wild Wings, Inc.", "Arby's Restaurant Group, Inc.", "Inspire Brands, Inc."
- **R30 Applebee's**
  - Owner: "Our common stock is listed on the New York Stock Exchange (“NYSE”) and trades under the ticker symbol “DIN.”" — [Dine Brands Global, Form 10-K FY2025, filed 2026-02-25](https://www.sec.gov/Archives/edgar/data/49754/000162828026011393/din-20251228.htm)
  - Since: "On November 29, 2007, pursuant to the Agreement and Plan of Merger, dated as of July 15, 2007" — [Applebee's International, Form 8-K, filed 2007-12-05](https://www.sec.gov/Archives/edgar/data/853665/000110465907086923/a07-30368_18k.htm) (IHOP Corp. merger; IHOP Corp. is the former name of Dine Brands, CIK 49754)
  - Model: "1,520 Applebee’s franchised restaurants" — [Dine Brands, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/49754/000162828026011393/din-20251228.htm)
  - 5% holders: DEF 14A filed 2026-03-27 lists AllianceBernstein 10.37%, BlackRock 9.12%, Vanguard 7.49%, Morgan Stanley 5.91% — [Dine, DEF 14A](https://www.sec.gov/Archives/edgar/data/49754/000119312526127555/d93744ddef14a.htm)
  - Affiliate: none found
  - BDC names: "Dine Brands Global, Inc.", "Applebee's International, Inc."
  - Notes: live situation. On 2026-10-28 the board "adopted a stockholder rights agreement" ([8-K filed 2026-10-29](https://www.sec.gov/Archives/edgar/data/49754/000119312526438102/d181868d8k.htm)). Two Schedule 13Ds were filed 2026-11-02 with event date 10/26/2026: Arkhouse Management Co. LP group 4.3%, and a Cobblers Cove Capital LP group (Matthew Perkal 1.4%). These are activist positions, not a control change; recheck before publishing.

### Category share
N = 30. The worker's counts are updated here for Whataburger (R25, settled by the parent) and for the Form ADV results in §5.
- **PE-owned (control): 8 / 30 = 26.7%.**
  - Via Inspire Brands / Roark: Dunkin', Sonic, Arby's, Buffalo Wild Wings.
  - Subway (Roark).
  - Pizza Hut (LongRange, closed 2026-09-01).
  - Jersey Mike's: Blackstone held ~76.5% of voting power at its IPO and the company is NYSE-listed.
  - Whataburger (BDT Capital Partners, majority, 2019).
- **PE minority stake: 1 / 30 = 3.3%.** Culver's: Roark holds an undisclosed minority.
- **PE-owned plus PE minority stake: 9 / 30 = 30.0%.**
- **Public company: 16 / 30 = 53.3%.**
  - The brands: McDonald's, Starbucks, Taco Bell and KFC (Yum), Wendy's, Chipotle, Burger King and Popeyes (RBI), Domino's, Texas Roadhouse, Chili's (Brinker), Olive Garden (Darden), Dairy Queen (Berkshire Hathaway, a conglomerate), Wingstop, Jack in the Box, Applebee's (Dine).
  - 3 of the 16 have a 5%+ holder whose Form ADV reports `Any PE Funds = Y`:
    - Burger King and Popeyes: 3G Capital Partners LP, ~22% of RBI voting interest.
    - Wendy's: Trian Fund Management, 7.9%; the Peltz/May group holds ~16% of voting power.
  - None of the three holders has control.
- **Other: 2 / 30 = 6.7%.** Family: Chick-fil-A and Little Caesars. No founder or co-op owner confirmed.
- **Investment-firm owner, current status not reconfirmed: 1 / 30 = 3.3%.**
  - Panera: owned by JAB per the 2017 merger 8-K. No later primary source was found.
  - JAB Consumer Fund Management SARL reports `Any PE Funds = Y`.
- **Not found: 2 / 30 = 6.7%.** Panda Express and Raising Cane's. Both sites returned 403 to automated fetches.
- **Upper bound:** if Panera/JAB were reconfirmed, the PE-owned share would be 10 / 30 = 33.3%.
- **Sources disagree:** none.
- **Formerly PE-owned among public rows:** Wingstop. Roark lists it under "Previous Investments"; the years were not found.

## 3. Gyms

**Ranking:** No single public ranking covers 30 current US gym brands, so this list is a composite ordered by **location count**, and the scope (US vs worldwide) is as each source states it. (a) Ranks for Planet Fitness, Anytime Fitness, Orangetheory, F45, LA Fitness, Crunch, Snap Fitness, 24 Hour Fitness and Workout Anytime come from Athletech News, "America's Biggest Gym Brands by Location Count" (Ani Freedman, published 2026-03-19; Wefranch data, US locations as of February 2026), https://athletechnews.com/americas-biggest-gym-brands-by-location-count-wefranch/. Only ranks 1–9 are free; the rest is paywalled and was not used. (b) Every other brand was placed by the count its own filing, release or site states (cited in Evidence), or, where only trade press gave a count, by that count (marked "trade"). The candidate set is the Athletech top 9, the brands of the companies checked (Xponential, Purpose Brands, TSG, LGP, Extraordinary Brands), and brands surfaced in searches. It is **not exhaustive**: brands under ~90 units, or missed by search, may belong above the cutoff (unchecked: D1 Training, iLoveKickboxing, Youfit, Retro Fitness, Club Studio/Esporta, VASA, Chuze, Fitness Connection, PureGym US/ex-Blink). Excluded by rule: nonprofits (YMCA) and CrossFit (an affiliate-licence brand that Athletech's list also leaves out). Boutique franchisors are in because the main ranking includes them. Rejected rankings: Club Industry Top 100 (last edition 2021, 2020 revenue; americanspa.com returned 403); Franchise Times Top 400 2026 (robots.txt disallows ClaudeBot/anthropic-ai, so not used after two fetches); Orbital (page now redirects to another company); ScrapeHero and xMap (top 10 only, no methodology).

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Planet Fitness (2,896 clubs, system) | Planet Fitness, Inc. | public company | none (no PE 5%+ holder in 2026 proxy; TSG Consumer lists it as exited) | IPO not checked | PLNT | franchise-led: 2,604 franchisee-owned, 292 corporate-owned | network listing only (Admitad) | G1 |
| 2 | Anytime Fitness (2,298 US) | Purpose Brands | PE-owned (via Purpose Brands); stake size not stated | Roark Capital | Roark invested 2014 | — | franchise | none found | G2 |
| 3 | Club Pilates (1,414 global) | Xponential Fitness, Inc. | public company | none identified (5%+ holder H&W Investco, LP: type not confirmed) | acquired by Xponential 2017 | XPOF | franchise (no company-owned studios) | none found | G3 |
| 4 | Orangetheory Fitness (1,283 US) | Purpose Brands | PE-owned (via Purpose Brands); stake size not stated | Roark Capital | Roark invested 2016 | — | franchise | network listing only (FlexOffers) | G4 |
| 5 | HOTWORX (800+) | not stated; founder Stephen Smith is CEO | founder-led, owner not stated (no PE evidence found in sources checked) | none found | — | — | franchise | none found | G5 |
| 6 | F45 Training (724 US) | not found (current) | not found; deregistered from SEC 2023 | not found (Kennedy Lewis, an investment manager, filed 13D in 2023) | — | none (was FXLV) | franchise (trade) | none found | G6 |
| 7 | 9Round (700+, 17 countries) | not found | not found | not found | — | — | franchise | none found | G7 |
| 8 | Pure Barre (625 global) | Xponential Fitness, Inc. | public company | as G3 | acquired by Xponential 2018 | XPOF | franchise | none found | G8 |
| 9 | LA Fitness (607 US) | not found (operator Fitness International, LLC) | not found | not found (trade press names PE co-owners; no primary source) | — | — | not found | none found | G9 |
| 10 | Gold's Gym (~600 worldwide) | RSG Group | Owner type not confirmed (private German group; no PE evidence found) | none found | 2020 | — | franchise and company gyms | none found | G10 |
| 11 | Crunch Fitness (569 US) | Leonard Green & Partners (majority) | PE-owned | Leonard Green & Partners (bought from TPG Growth) | announced 2025-04-15 | — | franchise and corporate gyms | none found | G11 |
| 12 | StretchLab (531 global) | Xponential Fitness, Inc. | public company | as G3 | acquired by Xponential 2017 | XPOF | franchise | none found | G12 |
| 13 | Snap Fitness (473 US) | Lift Brands | PE-owned (via Lift Brands) | TZP Group | not found | — | franchise | none found | G13 |
| 14 | Burn Boot Camp (400+, trade) | not stated; founders Devan and Morgan Kline | founder-led, owner not stated (no PE evidence found in sources checked) | none found | — | — | franchise | none found | G14 |
| 15 | BFT (333 global) | Xponential Fitness, Inc. | public company | as G3 | acquired by Xponential 2021 | XPOF | franchise | none found | G15 |
| 16 | 24 Hour Fitness (240+) | not found | not found (secondary: owned by its lenders since the 2020 Chapter 11) | not found | — | — | not found | network listing only (FlexOffers) | G16 |
| 17 | CorePower Yoga (~225, trade) | TSG Consumer Partners | PE-owned | TSG Consumer Partners | 2019 | — | not found (trade: corporate-owned) | none found | G17 |
| 18 | CycleBar (204 at end-2024, trade) | Extraordinary Brands, LLC | Owner type not confirmed (no PE evidence found) | none found | 2025-07-28 | — | franchise | none found | G18 |
| 19 | The Exercise Coach (200+ US) | not stated; operator Exercise Coach USA, LLC; founders Brian and Gerianne | founder-led, owner not stated (no PE evidence found in sources checked) | none found | — | — | franchise | none found | G19 |
| 20 | Workout Anytime (~200) | Jerry Pugh (majority) | PE minority stake | Skyline Global Partners, Peninsula Capital Partners (minority) | 2025 (April) | — | franchise | none found | G20 |
| 21 | YogaSix (194 global) | Xponential Fitness, Inc. | public company | as G3 | acquired by Xponential 2018 | XPOF | franchise | none found | G21 |
| 22 | Fit Body Boot Camp (190+, trade) | not found | not found | not found | — | — | franchise (trade) | none found | G22 |
| 23 | Life Time (189 centers) | Life Time Group Holdings, Inc. | public, PE holder (LGP 11.2%, TPG 8.0%) | Leonard Green & Partners, TPG (minority holders) | IPO Oct 2021 | LTH | company-operated (owned or leased) | none found | G23 |
| 24 | EōS Fitness (175+ open or in development) | TSG Consumer Partners | PE-owned | TSG Consumer Partners (bought from BRS & Co.) | 2025-07-21 | — | not stated (BRS bought it as 16 formerly franchised gyms) | none found | G24 |
| 25 | UFC GYM (150+ in 37 countries, trade) | not found | not found | not found | — | — | not found | none found | G25 |
| 26 | TITLE Boxing Club (~130, trade) | not found (trade: BoxUnion since 2021) | not found | not found | — | — | franchise (trade) | none found | G26 |
| 27 | [solidcore] (~130) | L Catterton (majority) | PE-owned | L Catterton | 2025 (financing dated 2025-02-04) | — | company-operated | none found | G27 |
| 28 | Equinox (107 clubs global) | not found | Owner type not confirmed (PE firms among 2024 investors) | L Catterton among investors (stake not stated) | — | — | company-operated | aggregator listing only (Equinox+ app) | G28 |
| 29 | Rumble (103 at end-2024, trade) | Extraordinary Brands, LLC | Owner type not confirmed (no PE evidence found) | none found | 2025-07-28 | — | franchise | none found | G29 |
| 30 | Barry's (89 studios worldwide) | Princeton Equity Group | PE-owned (stake not stated) | Princeton Equity Group (bought from North Castle Partners) | 2025-01 | — | not found | none found | G30 |

### Evidence
- **G1 Planet Fitness**
  - Owner: "Class A common stock trades on the New York Stock Exchange under the symbol" — [SEC, Planet Fitness 10-K FY2025, filed 2026-02-25](https://www.sec.gov/Archives/edgar/data/1637207/000163720726000011/plnt-20251231.htm)
  - Since: not checked (public; IPO year not needed for the category count)
  - Model: "Of our 2,896 clubs, 2,604 were franchisee-owned and 292 were corporate-owned." — [SEC, Planet Fitness 10-K FY2025, filed 2026-02-25](https://www.sec.gov/Archives/edgar/data/1637207/000163720726000011/plnt-20251231.htm)
  - Affiliate: network listing only, https://www.admitad.com/store/offers/planet-fitness-affiliate-program/ (no brand-direct affiliate page found)
  - BDC names: "Planet Fitness, Inc."; "Pla-Fit Holdings, LLC" (the 10-K names the holdings LLC; not separately checked)
  - Notes: the 2026 proxy lists no PE firm among the 5%+ holders (T. Rowe Price, Vanguard, BlackRock, Steadfast, SRS, Amundi): [SEC, Planet Fitness DEF 14A, filed 2026-03-25](https://www.sec.gov/Archives/edgar/data/1637207/000163720726000019/plnt-20260325.htm). TSG Consumer's portfolio page lists Planet Fitness with "Investment Year: 2012" and status "Exited" (https://www.tsgconsumer.com/portfolio/).
- **G2 Anytime Fitness**
  - Owner: "Purpose Brands is the parent company of Anytime Fitness, Orangetheory Fitness, Basecamp Fitness" — [Roark Capital, portfolio page, read 2026-11-05](https://www.roarkcapital.com/portfolio)
  - Since: "Private equity firm Roark Capital, which invested in Self Esteem Brands and Orangetheory Fitness in 2014 and 2016" — [PR Newswire, Orangetheory Fitness and Self Esteem Brands complete merger, 2024-04-02](https://prnewswire.com/news-releases/orangetheory-fitness-and-self-esteem-brands-complete-merger-creating-the-worlds-largest-footprint-in-fitness-health-and-wellness-services-302105939.html)
  - Model: "Anytime Fitness is the largest fitness franchise in the world, with gym facilities open 24 hours a day, 365 days a year." — [Roark Capital, portfolio page](https://www.roarkcapital.com/portfolio)
  - Affiliate: none found (checked: one category-wide search; no brand-direct page)
  - BDC names: "Purpose Brands, LLC"; "Self Esteem Brands"; "Anytime Fitness, LLC"
  - Notes: no source states Roark's stake size. Counted as control by the glossary default ("A hop with no stated stake counts as control").
- **G3 Club Pilates**
  - Owner: "Club Pilates, our first acquisition in 2017" — [SEC, Xponential Fitness 10-K FY2025, filed 2026-03-04](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Since: "Club Pilates, our first acquisition in 2017" — [SEC, Xponential 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Model: "company-owned studios is not a component of our business model" — [SEC, Xponential 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Affiliate: none found
  - BDC names: "Xponential Fitness, Inc."; "Xponential Fitness LLC"
  - Notes: ticker: "Shares of our Class A common stock trade on the NYSE under the symbol" (same 10-K). Count: "As of December 31, 2025, there were 1,414 operational studios and 1,996 licenses sold globally." (same 10-K). 5%+ holders: "held by H&W Investco, LP, each of which Mr. Grabowski is the Managing Partner" — [SEC, Xponential DEF 14A, filed 2026-04-24](https://www.sec.gov/Archives/edgar/data/1802156/000114036126016695/ny20067080x1_def14a.htm). The proxy does not say whether H&W Investco is a PE fund (Owner type not confirmed). Other 5%+ holders: Anthony Geisler (former CEO), Voss Capital.
- **G4 Orangetheory Fitness**
  - Owner: "Purpose Brands is the parent company of Anytime Fitness, Orangetheory Fitness, Basecamp Fitness" — [Roark Capital, portfolio page](https://www.roarkcapital.com/portfolio)
  - Since: "Private equity firm Roark Capital, which invested in Self Esteem Brands and Orangetheory Fitness in 2014 and 2016" — [PR Newswire, merger completion, 2024-04-02](https://prnewswire.com/news-releases/orangetheory-fitness-and-self-esteem-brands-complete-merger-creating-the-worlds-largest-footprint-in-fitness-health-and-wellness-services-302105939.html)
  - Model: "Orangetheory Fitness is one of the largest and fastest growing franchisors in the studio-based fitness market." — [Roark Capital, portfolio page](https://www.roarkcapital.com/portfolio)
  - Affiliate: network listing only, https://www.flexoffers.com/affiliate-programs/orangetheory-fitness-affiliate-program/ (no brand-direct page found)
  - BDC names: "Purpose Brands, LLC"; "Ultimate Fitness Group, LLC" (Orangetheory's operating entity name as it appears in search results; not confirmed from a primary source)
  - Notes: stake size not stated; control by glossary default.
- **G5 HOTWORX**
  - Owner: "Stephen Smith, Founder and CEO of HOTWORX." — [IFA (franchise.org), HOTWORX achieves 800 studio milestone, 2025-12-02](https://www.franchise.org/2025/12/hotworx-achieves-800-studio-milestone-as-infrared-fitness-movement-accelerates-worldwide/)
  - Since: not applicable
  - Model: "the revolutionary 24-hour infrared fitness studio franchise" — [IFA, 2025-12-02](https://www.franchise.org/2025/12/hotworx-achieves-800-studio-milestone-as-infrared-fitness-movement-accelerates-worldwide/)
  - Affiliate: none found
  - BDC names: "HOTWORX"; "Hotworx Holdings"
  - Notes: count: "With over 800 studio locations and over 250,000 members" (same page). The release names no parent or investors, so the owner is not stated. Trade press reported 900+ in Sept 2026.
- **G6 F45 Training**
  - Owner: not found (current). Last SEC record: "CERTIFICATION AND NOTICE OF TERMINATION OF REGISTRATION UNDER SECTION 12(g)" — [SEC, F45 Training Holdings Form 15-12G, 2023-11-07](https://www.sec.gov/Archives/edgar/data/1788717/000119312523272551/d526935d1512g.htm)
  - Since: not found
  - Model: not found (primary); trade press describes a franchise
  - Affiliate: none found
  - BDC names: "F45 Training Holdings Inc."; "FIT House of Brands"
  - Notes: a 2023 Schedule 13D/A was filed by "Kennedy Lewis Investment Management" — [SEC, 13D/A, 2023-10-24](https://www.sec.gov/Archives/edgar/data/1788717/000119312523261765/d574980dsc13da.htm). Kennedy Lewis is an investment manager that was also a lender under F45's credit agreement; it is not confirmed as an owner today. Trade press (2025–26) says a new parent brand "FIT House of Brands" was created but gives no owner. Slow: 5 fetches, no current primary source.
- **G7 9Round**
  - Owner: not found
  - Since: not found
  - Model: "With more than 700 locations in 17 countries around the world, 9Round is the undisputed leader in kickbox-fitness." — [9Round, master franchise page](https://www.9round.com/fitness-franchises/master) (count; the page is the brand's franchise-sales page)
  - Affiliate: none found
  - BDC names: "9Round Holding Company"; "9Round Franchising, LLC"
  - Notes: FDD-based aggregators put US franchised units near 200, so the 700+ figure is worldwide.
- **G8 Pure Barre**
  - Owner: "Pure Barre, founded in 2001 and acquired in 2018" — [SEC, Xponential 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Since: "Pure Barre, founded in 2001 and acquired in 2018" — same
  - Model: "company-owned studios is not a component of our business model" — same
  - Affiliate: none found
  - BDC names: "Xponential Fitness, Inc."
  - Notes: count: "As of December 31, 2025, there were 625 operational studios and 806 licenses sold globally." (same 10-K)
- **G9 LA Fitness**
  - Owner: not found
  - Since: not found
  - Model: not found
  - Affiliate: none found
  - BDC names: "Fitness International, LLC"; "LA Fitness International"
  - Notes: trade press (Orange County Business Journal, undated) says CIVC Partners, Madison Dearborn Partners and Seidler Equity Partners are majority owners. No sponsor portfolio page confirms it: civc.com and mdcp.com render no entries, and sepfunds.com/portfolio returned 404. EDGAR full-text search for "LA Fitness" with "Madison Dearborn" (2023–2026) returned 0 hits. M&A databases that show a 2015 "Pure Gym acquires LA Fitness" deal confuse it with the UK LA Fitness. Slow: 6 fetches.
- **G10 Gold's Gym**
  - Owner: "2020 hat die RSG Group Gold’s Gym im Rahmen eines Bieterverfahrens übernommen und die Marke in ihren Konzern integriert." — [RSG Group, Gold's Gym brand page (German)](https://www.rsggroup.com/en/brands/golds-gym/)
  - Since: same quote (2020)
  - Model: "Gold's Gym offers franchising opportunities both domestically and around the world." — [Gold's Gym home page](https://www.goldsgym.com/)
  - Affiliate: none found
  - BDC names: "Gold's Gym International, Inc."; "RSG Group GmbH"
  - Notes: RSG Group's own page says "knapp 600 Standorte" (nearly 600 locations) worldwide, and goldsgym.com says "500+". Who owns RSG Group (the founder's estate or family) is not stated, so: Owner type not confirmed.
- **G11 Crunch Fitness**
  - Owner: "Under the terms of the agreement, LGP will acquire a majority interest in Crunch Fitness from TPG Growth" — [Leonard Green & Partners, press release, 2025-04-15](https://www.leonardgreen.com/crunch-fitness-announces-strategic-investment-from-leonard-green-partners/)
  - Since: same release, dated 2025-04-15. LGP's portfolio page lists Crunch as "Current", deal type "Buyout", which implies the deal closed: [LGP portfolio](https://www.leonardgreen.com/portfolio/)
  - Model: "Crunch is a leading global franchisor of High Value, Low Price" — [LGP portfolio](https://www.leonardgreen.com/portfolio/)
  - Affiliate: none found
  - BDC names: "Crunch Holdings, LLC"; "Crunch, LLC"
  - Notes: the closing date itself was not found; current status comes from the LGP portfolio page.
- **G12 StretchLab**
  - Owner: "StretchLab, founded in 2015 and acquired in 2017" — [SEC, Xponential 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Since: same
  - Model: "company-owned studios is not a component of our business model" — same
  - Affiliate: none found
  - BDC names: "Xponential Fitness, Inc."
  - Notes: count: "As of December 31, 2025, there were 531 operational studios and 1,012 licenses sold globally." (same 10-K)
- **G13 Snap Fitness**
  - Owner: "© Lift Brands 2026 | All Rights Reserved" — [Snap Fitness US home page](https://www.snapfitness.com/us/)
  - Since: not found (secondary says TZP invested in 2014)
  - Model: "Snap Fitness locations are locally owned" — [Snap Fitness US home page](https://www.snapfitness.com/us/)
  - Affiliate: none found
  - BDC names: "Lift Brands, Inc."; "Snap Fitness, Inc."
  - Notes: PE link: TZP Group's portfolio lists "Lift Brands", "Global franchisor of fitness brands", status Current — [TZP Group portfolio](https://www.tzpgroup.com/portfolio/). Trade press (May 2024) reported Lift Brands up for sale; no completed sale found.
- **G14 Burn Boot Camp**
  - Owner: "Founded in 2012 by husband-wife duo Devan and Morgan Kline" — [IFA (franchise.org), Burn Boot Camp ends 2025 with double-digit growth, 2026-01-21](https://www.franchise.org/2026/01/burn-boot-camp-ends-2025-with-double-digit-growth-and-strong-franchisee-profitability-while-expanding-national-footprint/)
  - Since: not applicable
  - Model: "signed 51 new agreements and opened 36 new gyms in 2025" — same
  - Affiliate: none found
  - BDC names: "Burn Boot Camp"; "Burn Franchising, LLC"
  - Notes: owner not stated. Celebrity "equity partners" (Kevin Hart, Marshmello) were reported in 2026. No PE firm named in any source found. Count from trade (400th-location milestone release).
- **G15 BFT**
  - Owner: "BFT, founded in 2017 and acquired in 2021" — [SEC, Xponential 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Since: same
  - Model: "company-owned studios is not a component of our business model" — same
  - Affiliate: none found
  - BDC names: "Xponential Fitness, Inc."
  - Notes: count: "As of December 31, 2025, there were 333 operational studios and 790 licenses sold globally." (same 10-K). Most studios are outside the US (Australian origin), so BFT may not belong in a US top 30.
- **G16 24 Hour Fitness**
  - Owner: not found
  - Since: not found
  - Model: not found. Count: "With over 240 clubs in 9 states nationwide," — [24 Hour Fitness, About Us](https://www.24hourfitness.com/company/about_us/)
  - Affiliate: network listing only, https://www.flexoffers.com/affiliate-programs/24-hour-fitness-affiliate-program
  - BDC names: "24 Hour Fitness Worldwide, Inc." (EDGAR full-text search finds this name in 2024–26 N-PORT fund holdings, e.g. Advisors' Inner Circle Fund III and Nuveen Investment Trust III; not checked further)
  - Notes: secondary sources (Bloomberg Law, S&P) say its lenders took the equity when it emerged from Chapter 11 on 2020-12-31. The company's emergence release returned 403 on Business Wire and 404 on its own domain, and the trade reprint has no ownership sentence. Slow: 5 fetches.
- **G17 CorePower Yoga**
  - Owner: TSG Consumer portfolio entry "Yoga studio operator", Investment Year 2019, Status Current — [TSG Consumer Partners, portfolio](https://www.tsgconsumer.com/portfolio/)
  - Since: same (Investment Year: 2019)
  - Model: not found (primary); trade press says all studios are corporate-owned
  - Affiliate: none found
  - BDC names: "CorePower Yoga, LLC"; "CorePower Yoga Holdings"
  - Notes: the TSG entry quote is the tile text "Yoga studio operator". The year and status are page fields, not sentences.
- **G18 CycleBar**
  - Owner: "today announced that it has completed the divestiture of CycleBar and Rumble to Extraordinary Brands, LLC." — [Xponential investor relations, 2025-07-28](https://investor.xponential.com/news/detail/153/xponential-fitness-inc-announces-divestiture-of-cyclebar)
  - Since: same (2025-07-28)
  - Model: "we entered into an agreement with a buyer to divest the CycleBar and Rumble brands, including the intellectual property, franchise rights and franchise agreements for open studios" — [SEC, Xponential 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Affiliate: none found
  - BDC names: "Extraordinary Brands, LLC"
  - Notes: who owns Extraordinary Brands is not found. Trade press says it was founded in 2022 by Paul Flick. Count (204 at end-2024) is from trade press.
- **G19 The Exercise Coach**
  - Owner: "The Exercise Coach was founded in 2000 by Brian and Gerianne, a husband-and-wife team who shared a vision" — [The Exercise Coach, Our Story](https://exercisecoach.com/our-story/)
  - Since: not applicable
  - Model: "Each Exercise Coach studio is locally owned and operated by independent business owners who are passionate" — same
  - Affiliate: none found
  - BDC names: "Exercise Coach USA, LLC"
  - Notes: count: "Visit one of our 200+ locations to see if The Exercise Coach is a good fit for you." (same page). The franchisor's owner is not stated.
- **G20 Workout Anytime**
  - Owner: "Pugh acquired a majority stake in 200-unit Workout Anytime from founders Steve Strickland and John Quattrocchi" — [Workout Anytime news, 2025-04-18](https://workoutanytime.com/news_story/workout-anytimes-largest-franchisee-buys-the-200-unit-brand)
  - Since: same (deal "announced in early April" 2025)
  - Model: "Workout Anytime’s Largest Franchisee Buys the 200-Unit Brand" (headline) — same
  - Affiliate: none found
  - BDC names: "Workout Anytime Franchising Systems, LLC"
  - Notes: PE minority: "He worked with private equity firms Skyline Global Partners and Peninsula Capital Partners" — same page. The text on workoutanytime.com appears to reproduce a Franchise Times article.
- **G21 YogaSix**
  - Owner: "YogaSix, founded in 2011 and acquired in 2018" — [SEC, Xponential 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Since: same
  - Model: "company-owned studios is not a component of our business model" — same
  - Affiliate: none found
  - BDC names: "Xponential Fitness, Inc."
  - Notes: count: "As of December 31, 2025, there were 194 operational studios and 637 licenses sold globally." (same 10-K)
- **G22 Fit Body Boot Camp**
  - Owner: not found
  - Since: not found
  - Model: not found (primary); trade guide says franchise, 190+ locations, founded 2009 by Bedros Keuilian
  - Affiliate: none found
  - BDC names: "Fit Body Boot Camp"
  - Notes: no primary source fetched (cost cap).
- **G23 Life Time**
  - Owner: "Life Time Group Holdings, Inc. completed its initial public offering" — [SEC, Life Time 10-K FY2025, filed 2026-02-24](https://www.sec.gov/Archives/edgar/data/1869198/000186919826000010/lth-20251231.htm)
  - Since: same (IPO October 2021)
  - Model: "we operated 189 centers in 31 states and one Canadian province, 55 of which were owned (including ground leases) and 134 of which were leased" — same 10-K
  - Affiliate: none found
  - BDC names: "Life Time Group Holdings, Inc."; "Life Time, Inc."
  - Notes: PE holders: "which collectively held approximately 19.3% of our common stock as of December 31, 2025" (refers to LGP and TPG, same 10-K). The 2026 proxy table lists LGP Investors 11.2% and TPG Investors 8.0% as 5% stockholders — [SEC, Life Time DEF 14A, filed 2026-03-11](https://www.sec.gov/Archives/edgar/data/1869198/000186919826000020/lth-20260310.htm). LGP's portfolio lists Life Time as Current, deal type "Take-Private" (the 2015 buyout).
- **G24 EōS Fitness**
  - Owner: "completed the sale of EōS Fitness" ... "to TSG Consumer Partners, LP" — [BRS & Co., press release, 2025-07-21](https://brs.com/?p=2221)
  - Since: same (2025-07-21). TSG's portfolio lists EōS Fitness, "Investment Year: 2025", Status Current (https://www.tsgconsumer.com/portfolio/)
  - Model: not stated. The same BRS release says "BRS acquired the business with 16 formerly franchised gyms".
  - Affiliate: none found
  - BDC names: "EōS Fitness"; "EOS Fitness Holdings"; "EOS Fitness OPCO Holdings, LLC" (names not confirmed from a primary source)
  - Notes: count: "more than 175 gym locations open or in development" (BRS release), which includes unopened sites. Lead for the parent's BDC check: Golub Capital press release "Golub Capital provides $120 million one loan debt facility to support the refinancing of EōS Fitness by Bruckmann, Rosser, Sherrill & Co." (2019; https://golubcapital.com/news-insights/golub-capital-provides-120-million-one-loan-debt-facility-to-support-the-refinancing-of-eos-fitness-by-bruckmann-rosser-sherrill-co/, not fetched).
- **G25 UFC GYM**
  - Owner: not found (the ufcgym.com About page names no owner)
  - Since: not found
  - Model: not found (primary)
  - Affiliate: none found
  - BDC names: "UFC Gym"; "New Evolution Ventures"
  - Notes: trade press says the brand was formed in 2009 by New Evolution Ventures with UFC's then-owners. Count (150+ in 37 countries) from trade.
- **G26 TITLE Boxing Club**
  - Owner: not found (primary)
  - Since: not found
  - Model: not found (primary)
  - Affiliate: none found
  - BDC names: "TITLE Boxing Club, LLC"; "BoxUnion"
  - Notes: trade press says BoxUnion acquired it in January 2021, with ~130–141 locations since. The titleboxingclub.com franchise page returned 404.
- **G27 [solidcore]**
  - Owner: "The financing supports the acquisition of a majority stake in Solidcore by private equity firm L Catterton." — [Comvest Partners, press release, 2025-02-04](https://comvest.com/comvest-credit-partners-serves-as-joint-lead-arranger-on-325-million-senior-credit-facility-for-solidcore/)
  - Since: same (2025-02-04; trade press dates the signing to 2024-09-25)
  - Model: "owns and operates a national network of fitness studios" — same
  - Affiliate: none found
  - BDC names: "Solidcore"; "[solidcore]"; "SLC Holdings" (name not confirmed)
  - Notes: count: "approximately 130 locations across 25 states and the District of Columbia" (same release). The release comes from a lender (Comvest Credit Partners), which is a lead for the parent's BDC check. The L Catterton portfolio page returned 404.
- **G28 Equinox**
  - Owner: not found. Investors: "It also included investments from Ares Management, HPS Investment Partners, L Catterton," ... "and the principals of the Related Companies." — [Sixth Street, investment announcement, 2024-03-08](https://sixthstreet.com/investment_announce/equinox-group-secures-strategic-investments-to-refinance-existing-loans-and-support-growth-as-the-global-leader-in-high-performance-living/)
  - Since: not found
  - Model: "Equinox currently operates 107 clubs globally and has a current pipeline of over 25 new locations" — same
  - Affiliate: aggregator listing only (Equinox+ app on linkclicky.com; no brand-direct page found)
  - BDC names: "Equinox Holdings, Inc."; "Equinox Group"
  - Notes: secondary sources say Related Companies (Stephen Ross) is the controlling owner; no primary source found. **BDC lead for the parent:** EDGAR full-text search for "Equinox Holdings" (2025–26) hits BDC 10-Qs of Sixth Street Lending Partners, Sixth Street Specialty Lending (TSLX, 10-Q filed 2026-11-03) and HPS Corporate Capital Solutions Fund. Slow: 5 fetches.
- **G29 Rumble**
  - Owner: "today announced that it has completed the divestiture of CycleBar and Rumble to Extraordinary Brands, LLC." — [Xponential investor relations, 2025-07-28](https://investor.xponential.com/news/detail/153/xponential-fitness-inc-announces-divestiture-of-cyclebar)
  - Since: same
  - Model: "we entered into an agreement with a buyer to divest the CycleBar and Rumble brands, including the intellectual property, franchise rights and franchise agreements for open studios" — [SEC, Xponential 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1802156/000180215626000016/xpof-20251231.htm)
  - Affiliate: none found
  - BDC names: "Extraordinary Brands, LLC"
  - Notes: count (103 at end-2024) from trade press.
- **G30 Barry's**
  - Owner: "in connection with North Castle’s sale of Barry’s to Princeton Equity Group." — [Greenberg Traurig (counsel to Barry's and North Castle), press release, 2025-01-16](https://www.gtlaw.com/en/news/2025/01/press-releases/greenberg-traurig-advises-on-the--sale-of-iconic-fitness-brand-barrys)
  - Since: same (January 2025)
  - Model: not found. Count: "Barry’s has become an iconic fitness brand with 89 studios worldwide." — same
  - Affiliate: none found
  - BDC names: "Barry's Bootcamp Holdings, LLC"; "Barry's"
  - Notes: framing differs. The counsel release says "sale", while Barry's own PR Newswire release (title "Barry's Announces New Strategic Investment Partner Princeton Equity Group", copy on finanzen.net returned 403) says strategic investment. Both put a PE firm in the chain. The source is a law-firm release, not the company's, so it is weaker than a sponsor page (princetonequitygroup.com/portfolio rendered empty).

### Category share
N = 30 (composite ranking above).
- **PE-owned (control, or no stake stated): 8 / 30 = 26.7%**: Anytime Fitness, Orangetheory, Crunch, Snap Fitness, CorePower Yoga, EōS Fitness, [solidcore], Barry's.
- **PE minority stake: 1 / 30 = 3.3%**: Workout Anytime. PE-owned + minority = 9 / 30 = 30.0%.
- **Public company: 7 / 30 = 23.3%**: Planet Fitness, Life Time, and the five Xponential brands (Club Pilates, Pure Barre, StretchLab, BFT, YogaSix). One of the seven (Life Time) has 5%+ PE holders (LGP 11.2%, TPG 8.0%). Xponential's largest holder (H&W Investco, LP) is of unconfirmed type. Counting by parent company instead of by brand, the five Xponential brands are one parent.
- **Other: 7 / 30 = 23.3%**
  - founder-led, owner not stated, no PE evidence found: 3 (HOTWORX, Burn Boot Camp, The Exercise Coach)
  - private group, owner type not confirmed: 4 (Gold's Gym/RSG Group; CycleBar and Rumble/Extraordinary Brands; Equinox, which has PE firms among its 2024 investors with no stated stake)
  - family, nonprofit, conglomerate, lender-owned (confirmed): 0
- **Not found: 7 / 30 = 23.3%**: F45, 9Round, LA Fitness, 24 Hour Fitness, Fit Body Boot Camp, UFC GYM, TITLE Boxing Club.
- **Sources disagree:** Barry's, on framing only (sale vs strategic investment; both PE). No brand had owners contradicting each other.
- **Upper bound if trade-press leads held:** adding LA Fitness (PE co-owners per trade press) and Equinox (PE investors) would make PE involvement 11 / 30 = 36.7%. These are not counted.

## 4. Eyewear

**Ranking:** Vision Monday (Jobson), *VM's 2025 Top 50 U.S. Optical Retailers*, ranked by 2024 US sales ($ millions; company figures plus VM estimates; includes product sales, professional services, managed-vision-benefit revenue and e-commerce). Data year: calendar 2024. Published June 18, 2025. Chart PDF: https://www.visionmonday.com/CMSDocuments/2025/06/vmtop50retailers_2025.pdf (article: https://www.visionmonday.com/vm-reports/top-50-retailers/article/vms-2025-top-50-us-optical-retailers/). Trade press, used for the ranking only. **Why not the 2026 edition:** VM published the 2026 report (calendar 2025 data) on June 9, 2026 (https://www.visionmonday.com/vm-reports/top-50-retailers/article/for-vms-2026-top-50-us-optical-retailers-year-closes-with-positive-gains-in-sales-store-counts-across-the-us/), but only as a JavaScript flipbook (qgdigitalpublishing.com, i=862923) that returned no readable text to curl or WebFetch. Rows below are the list's entries 1–30, one row per entry. One entry can hold several banners (e.g. "Luxottica Retail" = LensCrafters, Pearle Vision, Target Optical, For Eyes, per the VM comments column). **Added, not ranked** (A1–A4): online sellers the list leaves out, namely Zenni, GlassesUSA, EyeBuyDirect and 1-800 Contacts. Warby Parker is already ranked (#10).

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Vision Source | Essilor (agreed to acquire in 2015); current EssilorLuxottica statement not found | public company (via EssilorLuxottica); formerly PE (Brazos, to 2015) | none current (Brazos Private Equity Partners before 2015) | 2015 (agreement) | EL (Euronext Paris), via parent | franchisor; members are franchisees owning their practices (optometrist network) | not checked (no consumer store) | E1 |
| 2 | Luxottica Retail (LensCrafters, Pearle Vision, Target Optical, For Eyes) | EssilorLuxottica | public company | none | not found | EL (Euronext Paris) | mixed: Pearle is a franchise; the others are company-run (Target Optical is run under licence, per VM, not primary) | LensCrafters: network listings only (FlexOffers/CJ); no brand-direct page found | E2 |
| 3 | Walmart (Walmart Vision Centers, Sam's Club Optical) | Walmart Inc. | public company | none | n/a | WMT (Nasdaq) | company-operated departments | yes (store-wide): https://affiliates.walmart.com/ | E3 |
| 4 | National Vision (America's Best, Eyeglass World) | National Vision Holdings, Inc. | public company (no PE 5%+ holder) | none | n/a | EYE (Nasdaq) | company-owned brands plus "Host" Vista Optical sites | not checked | E4 |
| 5 | EyeCare Partners | Partners Group (2019 agreement); 2024 refinancing "no impact" on equity; sale of optometry business to MyEyeDr announced 2026-09-28 (primary blocked) | PE-owned (Partners Group) | Partners Group | Dec 2019 (agreement) | — | rollup (MD/OD practices and ASCs) | n/a (no consumer store) | E5 |
| 6 | Costco Optical | Costco Wholesale Corp. | public company | none | n/a | COST (Nasdaq) | company-operated warehouse ancillary | not checked | E6 |
| 7 | MyEyeDr. (Capital Vision Services) | Goldman Sachs Asset Management (control) with Charlesbank minority | PE-owned (Goldman Sachs Asset Management / Merchant Banking) | Goldman Sachs MBD (West Street Capital Partners VII); Charlesbank (minority) | 2019 (agreement June 3, 2019) | — | rollup (management services company to affiliated optometry practices) | not checked | E7 |
| 8 | Visionworks | VSP Vision | other: nonprofit (VSP calls itself "not-for-profit") | none | not found (VM says Oct 2019, not primary) | — | company-operated stores (not sourced) | blocked (403) | E8 |
| 9 | AEG Vision | Riata Capital Group ("Status Current") | PE-owned (Riata Capital Group) | Riata Capital Group | not found | — | rollup ("owns and operates over 500 optometry practices") | n/a | E9 |
| 10 | Warby Parker | Warby Parker Inc. (founders hold ~55.6% of voting power) | public company (no PE 5%+ holder) | none | n/a | WRBY (NYSE) | company-operated stores plus online | yes, per Awin listing (not fetched); site footer links /affiliates (404 to curl) | E10 |
| 11 | Keplr Vision | not found | Owner type not confirmed | not found (lead: Imperial Capital, directory sites only) | not found | — | rollup (not sourced) | n/a | E11 |
| 12 | Eyemart Express | VSP Vision (bought from FFL Partners and Leonard Green) | other: nonprofit; formerly PE-owned (FFL, LGP; to Jan 2025) | none current | Jan 23, 2025 | — | company stores ("nearly 250 stores in 42 states") | not checked | E12 |
| 13 | Now Optics (Stanton Optical) | Now Optics (parent, per Stanton site); the owner of Now Optics was not found | Owner type not confirmed (founder Daniel Stanton is CEO) | not found | not found | — | company-owned plus franchised (VM: 234 and 60; not primary) | not checked | E13 |
| 14 | Fielmann USA (SVS Vision, Shopko Optical, Befitting) | Fielmann Group AG | public company ("German family business") | none | 2023 (US entry, VM); Shopko July 1, 2024 | FIE (Frankfurt), per VM; listing quote not fetched | company-operated (not sourced) | not checked | E14 |
| 15 | VSP Ventures | VSP Vision | other: nonprofit | none | not found (VM: 2019) | — | rollup of practices (VM) | n/a | E15 |
| 16 | Cohen's Fashion Optical | not found | Owner type not confirmed | not found | not found | — | not found | not checked | E16 |
| 17 | New Look Vision Group (US) (Edward Beiner, Morgenthal Frederics, etc.) | FFL Partners, CDPQ and the Dr. H. Doug Barnes Family; FFL lists it as current | PE-owned (FFL Partners; CDPQ co-owner) | FFL Partners | May 26, 2021 | — (delisted from TSX: BCI) | company-operated banners (not sourced) | not checked | E17 |
| 18 | Total Vision | not found | Owner type not confirmed (lead: Bregal Partners) | not found | not found | — | rollup (MSO, per VM) | n/a | E18 |
| 19 | Texas State Optical | not found (founded by the Rogers family in 1936) | Owner type not confirmed | not found | not found | — | doctor network ("TSO Network Office") | not checked | E19 |
| 20 | BJ's Optical Centers | BJ's Wholesale Club Holdings, Inc. | public company | none | n/a | BJ (NYSE) | services "provided by outside operators under a license"; optical operator not named | not checked | E20 |
| 21 | Eye Doctors Optical Outlets | iCare Health Solutions, a VSP Vision company | other: nonprofit | none | 2023 (VSP blog, Sept 14, 2023) | — | company stores (not sourced) | not checked | E21 |
| 22 | Emerging Vision (Sterling Optical, Site for Sore Eyes) | Emerging Vision, Inc. (its owner was not found) | Owner type not confirmed | not found | not found | — | franchisor | not checked | E22 |
| 23 | Henry Ford OptimEyes | Henry Ford Health | other: health system (nonprofit status not sourced) | none | not found | — | health-system-operated | not checked | E23 |
| 24 | Vision Associates | not found (VM says EssilorLuxottica; site did not respond) | Owner type not confirmed | not found | not found | — | dispensaries inside ophthalmology practices (VM) | n/a | E24 |
| 25 | U.S. Vision | not found (lead: Lincoln Road Advisors since 2021; VM reports all centers closed June 2026) | Owner type not confirmed | not found | not found | — | licensed departments (JCPenney, Meijer, Boscov's; VM) | n/a | E25 |
| 26 | Marion Eye Centers & Optical | not found | Owner type not confirmed | not found | not found | — | ophthalmology/optometry practice | n/a | E26 |
| 27 | Dr. Tavel Family Eye Care (City Optical Co.) | family ("Family-owned and operated since 1940") | family | none | n/a | — | company-operated (20+ Indiana offices) | not checked | E27 |
| 28 | Today's Vision | Today's Vision Licensing Corporation (its owner was not found) | Owner type not confirmed | not found | not found | — | licensing network; "Each location is Independently Owned and Operated" | not checked | E28 |
| 29 | Lumina Vision Partners | not found (lead: acquired by MyEyeDr, VM Apr 22, 2026) | Owner type not confirmed | not found | not found | — | rollup (VM) | n/a | E29 |
| 30 | Wisconsin Vision | not found | Owner type not confirmed | not found | not found | — | not found | not checked | E30 |
| A1 | Zenni Optical (added, not ranked) | not found | Owner type not confirmed | not found | not found | — | online-only | yes: https://www.zennioptical.com/c/affiliate (Impact) | A1 |
| A2 | GlassesUSA (added, not ranked) | not found | Owner type not confirmed | not found | not found | — | online | yes: https://www.glassesusa.com/affiliates | A2 |
| A3 | EyeBuyDirect (added, not ranked) | EssilorLuxottica | public company (subsidiary) | none | not found (lead: 2013 Essilor majority stake) | EL (via parent) | online | yes: https://www.eyebuydirect.com/affiliate-program | A3 |
| A4 | 1-800 Contacts (added, not ranked) | not found (site 403; KKR release not found) | Owner type not confirmed (lead: KKR, 2020, from AEA Investors, per Bloomberg) | not found | not found | — | online | blocked (403) | A4 |

### Evidence
- **E1 Vision Source**
  - Owner: "North America’s largest, independent optometric service alliance Vision Source, a portfolio company of Brazos Private Equity Partners of Dallas, announced today that it has entered into a definitive agreement to be acquired by Essilor." — [Vision Source press release, "Essilor Agrees to Acquire Vision Source…", July 30, 2015](https://visionsource.com/about/news-media/press-releases/essilor-agrees-to-acquire-vision-source-to-further-support-independent-eye-care-professionals/)
  - Since: "KINGWOOD, TX  (July 30, 2015)" — same release
  - Model: "In accordance with franchise law, Vision Source is a franchisor, and its members are franchisees who own their respective practice." — [Vision Source, History & Facts (2026)](https://visionsource.com/about/history-facts/)
  - Affiliate: not checked (professional network, no consumer store)
  - BDC names: "Vision Source, L.P." (VM chart), "Vision Source, LP" (site footer); parents "Essilor of America, Inc.", "EssilorLuxottica"
  - Notes: no current EssilorLuxottica page naming Vision Source was found (essilorluxottica.com pages render by JavaScript and return empty text). Ownership since 2015 is inferred from the 2015 agreement plus VM's 2025 note ("is a part of Essilor of America"), which is trade press.
- **E2 Luxottica Retail (LensCrafters, Pearle Vision, Target Optical, For Eyes)**
  - Owner: "world-class retailers including Sunglass Hut, LensCrafters, Vision Express and Apollo." — [EssilorLuxottica press release, "2025 Universal Registration Document filed", 6 March 2026 (PDF)](https://www.essilorluxottica.com/cap/content/284372/)
  - Ticker: "EssilorLuxottica trades on the Euronext Paris market and is included in the Euro Stoxx 50 and CAC 40 indices." — same PDF (extra spaces in the PDF text between words)
  - Model: "Join a Top-Ranked Healthcare Franchise" — [Pearle Vision franchise site (2026)](https://www.ownapearlevision.com/)
  - Affiliate: LensCrafters is listed on FlexOffers as a CJ Affiliate program (https://www.flexoffers.com/affiliate-programs/lenscrafters-affiliate-program, network page, not fetched). No brand-direct page was found: lenscrafters.com returned 403. Sister brand Ray-Ban has https://www.ray-ban.com/usa/c/affiliates (search result, not fetched).
  - BDC names: "Luxottica of America Inc.", "Luxottica Retail", "EssilorLuxottica"
  - Quote check: the cited URL serves a JavaScript wrapper, so the parent's script couldn't reach the PDF text. The two quotes above are the only ones in this file it did not confirm.
  - Notes: the banner split and Target Optical's licence come from VM's comments column (trade press). Pearle, LensCrafters and Target Optical brand pages returned 404/403 or JavaScript-only content. Slow: 9 fetches for this row.
- **E3 Walmart**
  - Owner: "Common Stock, par value $0.10 per share WMT The Nasdaq Stock Market LLC" — [Walmart Inc. Form 10-K, FY ended Jan 31, 2026, filed 2026-03-13](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm)
  - Since: n/a
  - Model: "Health and wellness includes pharmacy, over-the-counter drugs and other medical products, and optical services." — same 10-K
  - Affiliate: "Become a Walmart Affiliate. Earn Commissions." — [Walmart Affiliate Program](https://affiliates.walmart.com/) (store-wide, not optical-specific)
  - BDC names: "Walmart Inc."
- **E4 National Vision (America's Best, Eyeglass World)**
  - Owner: "Common Stock, par value $0.01 per share EYE Nasdaq" — [National Vision Holdings, Inc. Form 10-K, FY2025, filed 2026-03-04](https://www.sec.gov/Archives/edgar/data/1710155/000162828026014379/eye-20260103.htm)
  - Since: n/a
  - Model: "our two owned brands, America’s Best Contacts and Eyeglasses (“America’s Best”) and Eyeglass World, as well as our Host brands, Vista Optical locations within select Fred Meyer stores and Vista Optical locations on select military bases." — same 10-K
  - Affiliate: not checked
  - BDC names: "National Vision Holdings, Inc.", "National Vision, Inc."
  - Notes: the 5%+ holders in the 2026 proxy are BlackRock 14.4%, Vanguard 13.0%, Wellington 7.3% and William Blair 6.2%, with no PE firm: "William Blair Investment Management, LLC (7) 150 North Riverside Plaza Chicago, IL 60606 4,896,516 6.2%" — [DEF 14A, filed 2026-05-04](https://www.sec.gov/Archives/edgar/data/1710155/000114036126018642/ny20063318x1_def14a.htm). Lead director D. Randolph Peeler is listed as "Senior Advisor, Berkshire Partners, LLC" (a former PE sponsor; he holds no 5% stake).
- **E5 EyeCare Partners**
  - Owner: "Partners Group, the global private markets investment manager, has agreed to make a significant equity investment on behalf of its clients in EyeCare Partners LLC" — [Partners Group press release, Dec 16, 2019, as republished on marktpuls.ch](https://www.marktpuls.ch/artikel/permalink/369426) (partnersgroup.com returned 403/404)
  - Since: "Denver, US; Baar-Zug, Switzerland; December 16, 2019" — same release
  - Owner (still current, 2024): "There is no impact on EyeCare Partners’ equity ownership." — [EyeCare Partners press release, April 2024 refinancing](https://eyecare-partners.com/press-release/eyecare-partners-announces-refinancing-transactions-secures-new-money-investment)
  - Owner (still held, 2026-06-30, added by the parent): `<name>EYECARE PARTNERS</name> <lei>254900ZAACWK09RJ8W93</lei> <title>ECP Parent, LLC</title>` — [Partners Group Private Equity Fund, LLC, Form N-PORT, period 2026-06-30, filed 2026-08-31](https://www.sec.gov/Archives/edgar/data/1447247/000141036826090305/primary_doc.xml). This is one Partners Group registered fund's position, not a statement of control. The same LEI links "ECP Parent, LLC" in Carlyle's BDC filings to EyeCare Partners (§6).
  - Model: "the largest vertically integrated medical vision services provider in the US" — Partners Group release above
  - Affiliate: n/a
  - BDC names: "EyeCare Partners, LLC" / "EyeCare Partners LLC"
  - Notes: on 2026-09-28 EyeCare Partners announced the sale of its optometry business (300+ offices) to MyEyeDr., with closing expected Q4 2026. Source: [Business Wire](https://secure.businesswire.com/news/home/20260928896885/en/EyeCare-Partners-Announces-Sale-of-Optometry-Business), which returned **403 to both curl and WebFetch**, so the deal is known only from trade-press leads (VM, Eyes On Eyecare). Closing is **not confirmed**. The same announcement reportedly includes a term-loan exchange backed by about 81% of second-out lenders, which is relevant to BDC exposure. Slow: 8 fetches.
- **E6 Costco Optical**
  - Owner: "Common Stock, $.005 Par Value COST The NASDAQ Global Select Market" — [Costco Wholesale Corp. Form 10-K, FY ended Aug 30, 2026, filed 2026-10-07](https://www.sec.gov/Archives/edgar/data/909832/000090983226000093/cost-20260830.htm)
  - Since: n/a
  - Model: "Warehouse Ancillary (includes gasoline, pharmacy, food court, optical, hearing aids, and tire installation)" — same 10-K
  - Affiliate: not checked
  - BDC names: "Costco Wholesale Corporation"
- **E7 MyEyeDr. (Capital Vision Services)**
  - Owner: "In 2019, Charlesbank acquired a minority interest in the company alongside Goldman Sachs Asset Management, management and other investors" — [Charlesbank Capital Partners, MyEyeDr. investment page ("Status Current"), 2026](https://www.charlesbank.com/investments/myeyedr/)
  - Since: "GS MBD will acquire Capital Vision Services, LP (“CVS”) from Altas and CDPQ" — [CDPQ (La Caisse) news release, June 3, 2019](https://www.lacaisse.com/en/node/6806)
  - Model: "CVS, which provides management services to MyEyeDr. O.D.’s (“MyEyeDr.” or the “Company”) optometry practices" — same CDPQ release
  - Affiliate: not checked
  - BDC names: "Capital Vision Services, LP", "Capital Vision Services, LLC", "MyEyeDr. O.D.", "MyEyeDr"
  - Notes: MyEyeDr is the reported buyer of EyeCare Partners' optometry division (E5, pending) and of Lumina Vision Partners (E29, trade press). If both close, rows 5, 7 and 29 partly merge under one PE owner. The MyEyeDr newsroom URLs tried returned 404.
- **E8 Visionworks**
  - Owner: "Marchon Eyewear, Inc., Visionworks" (from the boilerplate list "the people that power our complementary businesses—VSP Vision Care, Marchon Eyewear, Inc., Visionworks, Eyefinity, Eyeconic, VSP Optics, and VSP Ventures") — [VSP Vision press release, Jan 23, 2025, hosted by Leonard Green & Partners](https://www.leonardgreen.com/vsp-vision-completes-eyemart-express-acquisition/)
  - Owner kind: "As the first national not-for-profit vision benefits company, this is what drives everything we do." — same release
  - Since: not found (primary). VM: "VSP Vision, which acquired Visionworks in October 2019" (trade press)
  - Model: not sourced
  - Affiliate: blocked (visionworks.com returned 403 Access Denied)
  - BDC names: "Visionworks of America, Inc."; parent "VSP Vision", "Vision Service Plan"
  - Notes: the ® marks in the boilerplate are separate HTML elements, so quote matching may need markup stripped.
- **E9 AEG Vision**
  - Owner: "Transaction Type Buy & Build Status Current" — [Riata Capital Group, AEG Vision portfolio page, 2026](https://www.riatacapital.com/portfolio/aeg-vision)
  - Owner (2): "Riata intends to continue to expand the AEG vision through the acquisition of additional regional eyecare groups and independent optometry practices." — same page
  - Since: not found
  - Model: "AEG Vision owns and operates over 500 optometry practices throughout the U.S." — same page
  - Affiliate: n/a
  - BDC names: "AEG Vision", "AEG Vision Holdings" (holding-company name not confirmed)
- **E10 Warby Parker**
  - Owner: "Class A Common Stock, $0.0001 par value per share WRBY New York Stock Exchange" — [Warby Parker Inc. Form 10-K, FY2025, filed 2026-02-26](https://www.sec.gov/Archives/edgar/data/1504776/000150477626000006/wrby-20251231.htm)
  - Since: n/a
  - Model: "As of December 31, 2025, we operated 318 retail stores across the United States and five retail stores in Canada." — same 10-K
  - Affiliate: the Awin merchant profile https://ui.awin.com/merchant-profile/17226 (search result, not fetched). The site footer links https://www.warbyparker.com/affiliates, which returned 404 to curl.
  - BDC names: "Warby Parker Inc."
  - Notes: the 5%+ holders are FMR 14.8%, JPMorgan 9.0%, Durable Capital Partners 6.8% and BlackRock 6.2% of Class A, with no PE firm: "Durable Capital Partners LP (3) 7,310,605 6.8" — [DEF 14A, filed 2026-04-28](https://www.sec.gov/Archives/edgar/data/1504776/000110465926050432/tm261524-1_def14a.htm). Founders Blumenthal and Gilboa hold 29.6% and 26.0% of total voting power through Class B shares (same table).
- **E11 Keplr Vision**
  - Owner: not found. Checked keplrvision.com/about-us (404) and imperialcap.com/investments (no Keplr mention). The Imperial Capital link appears only on directory sites (mergr, privateequityinfo), which are leads, not sources.
  - Since: not found
  - Model: not found
  - Affiliate: n/a
  - BDC names: "Keplr Vision", "Keplr Vision, LLC" (unconfirmed), "Total ECP", "Visionary Eye Partners"
  - Notes: slow, 5 fetches without a primary source. This is a typical PE-rollup gap: the sponsor's portfolio page lacks it or renders by JavaScript.
- **E12 Eyemart Express**
  - Owner: "VSP Vision ™ announced today it has completed the acquisition of Eyemart Express from FFL Partners and Leonard Green & Partners." — [VSP Vision press release, Jan 23, 2025, on leonardgreen.com](https://www.leonardgreen.com/vsp-vision-completes-eyemart-express-acquisition/)
  - Since: "RANCHO CORDOVA, Calif . , Jan. 23, 2025 /PRNewswire/" — same release
  - Model: "Doctor-founded in 1990, Eyemart Express has nearly 250 stores in 42 states." — same release
  - Affiliate: not checked
  - BDC names: "Eyemart Express", "Eyemart Express, LLC" (unconfirmed)
  - Notes: formerly PE-owned (FFL Partners and Leonard Green, to Jan 2025). FFL's portfolio page lists "Eyemart Express exited".
- **E13 Now Optics (Stanton Optical)**
  - Owner: "For more information about our parent company, Now Optics, click here." — [Stanton Optical, About Us (2026)](https://www.stantonoptical.com/about-us/)
  - Owner (2): "Daniel Stanton Founder, CEO" — [Now Optics homepage (2026)](https://www.nowoptics.com/)
  - Since: not found
  - Model: not found (primary). VM counts 234 company-owned and 60 franchised; stantonoptical.com/franchise/ returned 404.
  - Affiliate: not checked
  - BDC names: "Now Optics Holdings, LLC", "Now Optics, LLC"
  - Notes: who owns Now Optics was not found. One aggregator lead names FFL Partners (equity) and Monroe Capital (debt). The FFL portfolio page shows no Now Optics. Monroe Capital runs a public BDC (MRCC), so check DERA.
- **E14 Fielmann USA**
  - Owner: "German family business forms leading optical retailer in the Upper Midwest of the United States" — [Fielmann Group AG press release, "Fielmann Group closes acquisition of Shopko Optical…", 1 July 2024](https://www.fielmann-group.com/en/newsroom/detail/fielmann-group-closes-acquisition-of-shopko-optical-and-increases-fy2024-outlook/)
  - Since: "Shopko Optical is consolidated as part of the Fielmann Group as of 1 July 2024" — same release
  - Model: not sourced
  - Affiliate: not checked
  - BDC names: "Fielmann USA, Inc.", "Fielmann Group AG", "Shopko Optical", "SVS Vision"
  - Notes: the ticker FIE comes from VM (trade press). The fielmann-group.com IR share page returned 404. Seller of Shopko Optical: Monarch Alternative Capital (search lead, not fetched).
- **E15 VSP Ventures**
  - Owner: "Ventures—work together to create a world where everyone can bring their best vision to life." (end of the VSP boilerplate business list, which includes "VSP Ventures") — [VSP Vision press release, Jan 23, 2025](https://www.leonardgreen.com/vsp-vision-completes-eyemart-express-acquisition/)
  - Since: not found (VM: "established by VSP Vision in 2019")
  - Model: not sourced (VM: centrally managed network of acquired practices)
  - Affiliate: n/a
  - BDC names: "VSP Ventures"
- **E16 Cohen's Fashion Optical**
  - Owner: not found. The about page only tells the founder's story: "Business boomed and the Cohen family outgrew the pushcart operation and established the original Cohen’s Optical retail store located on Orchard Street." — [Cohen's Fashion Optical, About Us](https://www.cohensfashionoptical.com/about-us/)
  - Since: not found
  - Model: not found
  - Affiliate: not checked
  - BDC names: "Cohen's Fashion Optical"
- **E17 New Look Vision Group (US)**
  - Owner: "FFL Partners, a San Francisco-based private equity firm, Caisse de dépôt et placement du Québec (CDPQ), a global investment group, and the Dr. H. Doug Barnes Family have acquired all of the outstanding Class A common shares of the Company" — [CDPQ (La Caisse) news release, May 26, 2021](https://www.lacaisse.com/en/news/pressreleases/ffl-partners-and-cdpq-complete-acquisition-of-new-look-vision-group)
  - Owner (current): "New Look Vision Group current" — [FFL Partners portfolio page (2026)](https://www.fflpartners.com/portfolio)
  - Since: "Montréal, May 26, 2021" — CDPQ release
  - Model: not sourced (US banners from VM: Edward Beiner, Morgenthal Frederics, Robert Marc NYC, etc.)
  - Affiliate: not checked
  - BDC names: "New Look Vision Group Inc.", "NL1 AcquireCo" (search lead)
- **E18 Total Vision**
  - Owner: not found. bregalpartners.com failed TLS (certificate for *.bluehost.com), bregal.com/portfolio does not mention it, and totalvision.com did not respond. Lead: VM, "backed by NYC-based Bregal Partners".
  - Since: not found
  - Model: not found (VM: MSO)
  - Affiliate: n/a
  - BDC names: "Total Vision LLC"
- **E19 Texas State Optical**
  - Owner: not found. History only: "Texas State Optical was established in 1936 when the Rogers family opened the first TSO office in Beaumont, Texas." — [TSO, Our History](https://www.tso.com/our-history.html)
  - Since: not found
  - Model: "© 2026 TSO Network Office. All rights Reserved" (network of doctors' offices) — same page
  - Affiliate: not checked
  - BDC names: "Texas State Optical", "TSO Network Office"
- **E20 BJ's Optical Centers**
  - Owner: "Common Stock, par value $0.01 BJ New York Stock Exchange" — [BJ's Wholesale Club Holdings, Inc. Form 10-K, FY2025, filed 2026-03-12](https://www.sec.gov/Archives/edgar/data/1531152/000153115226000007/bj-20260131.htm)
  - Since: n/a
  - Model: "Many of these services are provided by outside operators under a license arranged by BJ’s. Specialty services include full-service optical centers" — same 10-K
  - Affiliate: not checked
  - BDC names: "BJ's Wholesale Club Holdings, Inc."
  - Notes: the outside optical operator is not named, and could be a separately owned (possibly PE) company. Not pursued.
- **E21 Eye Doctors Optical Outlets**
  - Owner: "Optical Outlets will continue to operate as it does today, but now as a part of iCare Health Solutions" — [VSP Vision Care blog, "iCare Health Solutions Acquires Optical Outlets", Sept 14, 2023](https://visionpartners.vsp.com/blog/vision-benefits/icare-health-solutions-acquires-optical-outlets)
  - Owner (2): "a VSP Vision™ company, has acquired Optical Outlets" — same page
  - Since: "Posted: September 14, 2023" — same page
  - Model: not sourced
  - Affiliate: not checked
  - BDC names: "Optical Outlets", "iCare Health Solutions"
  - Notes: iCare was bought by VSP from Pine Tree Equity Partners in Nov 2021 (search lead, not fetched), so formerly PE-owned.
- **E22 Emerging Vision (Sterling Optical, Site for Sore Eyes)**
  - Owner: "Emerging Vision is the parent company of a diverse portfolio of trusted retail brands nationwide, including Sterling Optical, Site for Sore Eyes, The Eye Gallery, and OPTICA." — [Emerging Vision homepage (2026)](https://www.emergingvision.com/)
  - Since: not found
  - Model: "Take the first step in becoming a franchisee!" — same page
  - Affiliate: not checked
  - BDC names: "Emerging Vision, Inc."
  - Notes: who owns Emerging Vision, Inc. was not found.
- **E23 Henry Ford OptimEyes**
  - Owner: "Services | OptimEyes | Henry Ford Health" (page title) — [henryford.com, OptimEyes services](https://henryford.com/optimeyes/services)
  - Since: not found
  - Model: health-system-operated optical and optometry offices (location pages sit under henryford.com/optimeyes/locations/)
  - Affiliate: not checked
  - BDC names: "Henry Ford Health"
  - Notes: Henry Ford Health's nonprofit status was not separately sourced.
- **E24 Vision Associates**
  - Owner: not found. visionassociates.com did not respond (HTTP 000). Lead: VM, "a business unit of EssilorLuxottica".
  - Since / Model / Affiliate: not found / VM: dispensaries inside ophthalmology practices / n/a
  - BDC names: "Vision Associates"
- **E25 U.S. Vision**
  - Owner: not found (primary). Lead: a Business Wire release, "Refac Holdings Announces Acquisition by Lincoln Road Advisors" (Mar 3, 2021; businesswire.com blocks automated fetches). VM (June 2026, trade press) reports that Lincoln Road Advisors closed all U.S. Vision optical centers nationwide.
  - Since / Model / Affiliate: not found / licensed departments (VM) / n/a
  - BDC names: "U.S. Vision, Inc.", "Refac Holdings", "Refac Optical Group"
  - Notes: likely defunct since June 2026 (unconfirmed). Drop it from a 2026 list once that is confirmed.
- **E26 Marion Eye Centers & Optical**
  - Owner: not found (about page names no owner). [Marion Eye Centers, About Us](https://www.marioneyecenters.com/about-us/)
  - Since / Model / Affiliate: not found / not found / n/a
  - BDC names: "Marion Eye Centers"
- **E27 Dr. Tavel Family Eye Care (City Optical Co.)**
  - Owner: "Family-owned and operated since 1940, we have over 20 offices across Indiana." — [Dr. Tavel, About Us](https://www.drtavel.com/about-us)
  - Since: n/a
  - Model: company-operated offices (same quote)
  - Affiliate: not checked
  - BDC names: "City Optical Company"
- **E28 Today's Vision**
  - Owner: "© 2026 Today’s Vision Licensing Corporation." — [Today's Vision homepage](https://www.todaysvision.com/)
  - Model: "Each location is Independently Owned and Operated." — same page
  - Since: not found
  - Affiliate: not checked
  - BDC names: "Today's Vision Licensing Corporation"
  - Notes: who owns the licensing corporation was not found.
- **E29 Lumina Vision Partners**
  - Owner: not found (primary). luminavisionpartners.com returned 404, and the MyEyeDr newsroom returned 404. Lead: VM, Apr 22, 2026, "MyEyeDr. Acquires Lumina Vision Partners" (trade press).
  - Since / Model / Affiliate: not found / rollup (VM) / n/a
  - BDC names: "Lumina Vision Partners"
- **E30 Wisconsin Vision**
  - Owner: not found (homepage names no owner). [Wisconsin Vision](https://www.wisconsinvision.com/)
  - Since / Model / Affiliate: not found / not found / not checked
  - BDC names: "Wisconsin Vision, Inc."
- **A1 Zenni Optical (added, not ranked)**
  - Owner: not found (the about page has history only: "Making stylish, affordable vision care accessible to millions since 2003.") — [Zenni, About Us](https://www.zennioptical.com/c/about-us)
  - Since / Model: not found / online-only ("Launched the first online-only eyewear …", same page)
  - Affiliate: "We've partnered with Impact Radius to bring you a market-leading affiliate advertising program." — [Zenni Optical Affiliate Program](https://www.zennioptical.com/c/affiliate)
  - BDC names: "Zenni Optical, Inc."
- **A2 GlassesUSA (added, not ranked)**
  - Owner: not found (glassesusa.com/about-us and /about returned 404)
  - Since / Model: not found / online
  - Affiliate: "Earn up to 30% commission, the highest rate in the industry." — [GlassesUSA Affiliate Program](https://www.glassesusa.com/affiliates)
  - BDC names: "GlassesUSA.com"
- **A3 EyeBuyDirect (added, not ranked)**
  - Owner: "Eyebuydirect is a subsidiary of EssilorLuxottica, the world's largest provider of eyecare products and services." — [Eyebuydirect press release (PR Newswire), July 19, 2022](https://www.prnewswire.com/news-releases/eyebuydirect-rebrand-cements-new-positioning-that-empowers-individuality-301589180.html)
  - Since: not found (lead: Essilor majority stake 2013)
  - Model: online
  - Affiliate: "Affiliate Program | Become an EyeBuyDirect Affiliate" (page title) — [EyeBuyDirect Affiliate Program](https://www.eyebuydirect.com/affiliate-program)
  - BDC names: "EyeBuyDirect", "EssilorLuxottica"
- **A4 1-800 Contacts (added, not ranked)**
  - Owner: not found (primary). 1800contacts.com returned 403 to curl and WebFetch, and no KKR press-release URL was found (kkr.com URLs tried returned 404). Lead: Bloomberg, Sept 23, 2020, "KKR Buys 1-800 Contacts From AEA in $3 Billion-Plus Deal".
  - Since / Model: not found / online
  - Affiliate: blocked (403)
  - BDC names: "1-800 Contacts, Inc.", "1-800 Contacts"
  - Notes: a high-value gap. If the KKR lead is confirmed, this row is PE-owned.

### Category share
**Ranked rows only (N = 30, VM 2025 list, 2024 data):**
- PE-owned (control): **4 / 30 = 13.3%** (EyeCare Partners, MyEyeDr., AEG Vision, New Look Vision Group)
- PE minority stake: 0 (Charlesbank is a minority holder in MyEyeDr., but that row is counted as PE control through Goldman Sachs)
- Public company: **8 / 30 = 26.7%** (Vision Source and Luxottica Retail via EssilorLuxottica, Walmart, National Vision, Costco, Warby Parker, Fielmann USA, BJ's). Rows with a 5%+ PE holder: **0**.
- Other: **6 / 30 = 20.0%**. Nonprofit: 4 (VSP Vision's Visionworks, Eyemart Express, VSP Ventures, Eye Doctors Optical Outlets). Health system: 1 (Henry Ford OptimEyes). Family: 1 (Dr. Tavel).
- Not found / Owner type not confirmed: **12 / 30 = 40.0%** (Keplr, Now Optics, Cohen's, Total Vision, TSO, Emerging Vision, Vision Associates, U.S. Vision, Marion, Today's Vision, Lumina, Wisconsin Vision)
- Sources disagree: 0 found. EyeCare Partners' pending optometry sale is "not confirmed", not a disagreement.
- **Sensitivity:** if the trade-press and directory leads were confirmed from primary sources, the PE count would rise to 7 of 30 (23.3%) with Total Vision (Bregal), Lumina (MyEyeDr/Goldman) and Keplr (Imperial Capital). Vision Associates would move to public (EssilorLuxottica).
- **Sales-weighted:** the 4 confirmed PE-owned rows hold $4,232M of the top-30's $20,646M in 2024 US sales, or **20.5%** (VM figures; EyeCare Partners' figure includes ophthalmology). The 3 VSP-owned nonprofit rows that are former PE holdings (Eyemart Express, Eye Doctors Optical Outlets via iCare, and Visionworks, which had a Centerbridge minority before 2019 per a search lead) are not counted as PE.

**Including added rows (N = 34):** PE-owned 4 (11.8%), public 9 (26.5%; adds EyeBuyDirect), other 6 (17.6%), not found 15 (44.1%; adds Zenni, GlassesUSA, 1-800 Contacts). If the KKR lead for 1-800 Contacts were confirmed, PE would be 5 of 34 (14.7%).

**Affiliate income:** brand-direct programs were confirmed for Zenni (Impact), GlassesUSA and EyeBuyDirect, plus Walmart (store-wide). Warby Parker has one on Awin (the network page and the site's footer link were found, but the page was not fetched). LensCrafters appears on network listings only. 1-800 Contacts and Visionworks were blocked. Every confirmed affiliate brand is public-owned or of unknown ownership. **None of the four confirmed PE-owned rows sells online with an affiliate program** (they are practice rollups). For this category, affiliate income and PE share fall on different brands.

## 5. Form ADV check of the named firms

The source is the SEC monthly adviser files for Nov 2026: [registered advisers `ia110226-registered.zip` and exempt reporting advisers `ia11022026-exempt.zip`](https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers), downloaded 2026-11-05. The columns read are `Any PE Funds` and `Total number of PE funds`. Firms were matched by name against `Primary Business Name` and `Legal Name`. "Name match only" means the adviser's name resembles the firm in the lead, but no source tied that CRD to the brand.

| Firm (as sources name it) | Brand rows (role) | Adviser entity in the file | Type, CRD | `Any PE Funds` (PE funds) | Latest ADV |
|---|---|---|---|---|---|
| Roark Capital | Dunkin', Sonic, Arby's, BWW, Subway (control); Culver's (minority); Anytime Fitness, Orangetheory (control) | Roark Capital Management, LLC | RIA 160368 | Y (14) | 2026-03-31 |
| Blackstone | Jersey Mike's (control) | Blackstone Management Partners L.L.C. | RIA 136979 | Y (36) | 2026-03-30 |
| LongRange Capital | Pizza Hut (control) | LongRange Capital, L.P. | RIA 309379 | Y (1) | 2026-10-01 |
| BDT Capital Partners | Whataburger (majority) | BDT Capital Partners, LLC | RIA 160914 | Y (45) | 2026-10-23 |
| JAB | Panera (owner per 2017 8-K) | JAB Consumer Fund Management SARL; also JAB Capital Management, LLC | ERA 299567; ERA 320809 | Y (10); N | 2026-03-27 |
| 3G Capital | Burger King, Popeyes (~22% RBI voting, holder) | 3G Capital Partners LP | RIA 156934 | Y (2) | 2026-03-31 |
| Trian | Wendy's (7.9%, holder) | Trian Fund Management, L.P. | RIA 154172 | Y (6) | 2026-07-31 |
| Biglari Capital | Jack in the Box (5.70% in the Jan-2025 proxy, holder) | Biglari Capital LLC | RIA 115197 | N | 2026-03-28 |
| Leonard Green & Partners | Crunch (control); Life Time (11.2%, holder); Eyemart (seller, 2025) | Leonard Green & Partners, L.P. | RIA 158164 | Y (107) | 2026-03-31 |
| TPG | Life Time (8.0%, holder); Crunch (seller) | TPG Capital Advisors, LLC | RIA 159738 | Y (127) | 2026-07-24 |
| TZP Group | Snap Fitness / Lift Brands (control) | TZP Management Associates, LLC | RIA 160907 | Y (48) | 2026-03-31 |
| TSG Consumer Partners | CorePower Yoga, EōS Fitness (control) | TSG Consumer Partners LP | RIA 160826 | Y (18) | 2026-04-30 |
| L Catterton | [solidcore] (majority); Equinox (investor, no stated stake) | Catterton Management Company, L.L.C.; L Catterton Europe SAS; L Catterton Asia Advisors | RIA 157428; ERA 162124; ERA 162692 | **N**; Y (6); Y (3) | 2026-06-15; 2026-03-30; 2026-03-30 |
| Princeton Equity Group | Barry's (control) | Princeton Equity Advisors, LP | RIA 310405 | Y (8) | 2026-03-30 |
| Peninsula Capital Partners | Workout Anytime (minority) | Peninsula Capital Partners, L.L.C. | RIA 157354 | Y (4) | 2026-04-29 |
| Skyline Global Partners | Workout Anytime (minority) | not found in either file | — | — | — |
| BRS & Co. | EōS (seller, 2025) | Bruckmann, Rosser, Sherrill & Co., Management, L.P. | RIA 156881 | Y (4) | 2026-03-31 |
| North Castle Partners | Barry's (seller, 2025) | North Castle Partners, LLC | RIA 158213 | Y (11) | 2026-04-16 |
| Kennedy Lewis | F45 (13D filer and lender, 2023) | Kennedy Lewis Management LP | RIA 290399 | N | 2026-04-24 |
| H&W Investco | Xponential (5%+ holder) | not found | — | — | — |
| Related Companies | Equinox (named as controlling owner only by secondary sources) | Related Fund Management, LLC | RIA 156543 | N | 2026-03-31 |
| Partners Group | EyeCare Partners (control) | Partners Group AG; Partners Group (USA) Inc. | ERA 162791; RIA 145228 | Y (56); Y (2) | 2026-03-30; 2026-07-28 |
| Goldman Sachs Asset Management | MyEyeDr (control) | Goldman Sachs Asset Management, L.P. | RIA 107738 | Y (239) | 2026-09-25 |
| Charlesbank | MyEyeDr (minority) | Charlesbank Capital Partners, LLC | RIA 160256 | Y (31) | 2026-10-27 |
| Riata Capital Group | AEG Vision (control) | Riata Capital Group, LLC | RIA 289948 | Y (15) | 2026-03-16 |
| FFL Partners | New Look Vision Group (control, with CDPQ); Eyemart (seller) | FFL Partners, LLC | RIA 156980 | Y (30) | 2026-03-29 |
| KKR | 1-800 Contacts (lead only) | Kohlberg Kravis Roberts & Co. L.P. | RIA 144533 | Y (553) | 2026-09-25 |
| Bregal Partners | Total Vision (lead only) | name match only: Bregal Investments, Inc. | RIA 285006 | Y (44) | 2026-03-30 |
| Imperial Capital | Keplr Vision (lead only) | name match only: Imperial Capital Limited | ERA 316569 | Y (7) | 2026-03-05 |
| Lincoln Road Advisors | U.S. Vision (lead only) | name match only: Lincoln Road Global Management, LLC | ERA 328969 | Y (4) | 2026-05-22 |
| Brazos Private Equity Partners | Vision Source (owner until 2015) | name match only: Brazos Investment Partners I, L.P. | ERA 157120 | Y (1) | 2026-03-30 |
| Berkshire Partners | National Vision (former sponsor; the lead director's employer) | Berkshire Partners LLC | RIA 160675 | Y (26) | 2026-03-27 |
| Centerbridge | Visionworks (minority before 2019, lead only) | Centerbridge Partners, L.P. | RIA 157359 | Y (42) | 2026-06-24 |
| Durable Capital Partners | Warby Parker (6.8%, holder) | Durable Capital Partners LP | RIA 305221 | N | 2026-07-01 |
| Monarch Alternative Capital | Shopko Optical (seller, lead only) | Monarch Alternative Capital LP | RIA 159465 | N | 2026-07-31 |
| Pine Tree Equity, AEA Investors | iCare (former owner); 1-800 Contacts (former owner, lead) | not found | — | — | — |

What the check shows:
- **Control owners pass, with one exception.** Every control owner named in a PE-owned row has an adviser entity with `Any PE Funds = Y`, except L Catterton. L Catterton's main US adviser (Catterton Management Company, L.L.C., CRD 157428) reports **N**; only its Europe and Asia exempt reporting advisers report Y. A test keyed to that firm's main CRD would therefore miss L Catterton ([solidcore]).
- **The flag is also Y for firms that do not call themselves PE.** Trian (an activist investor), 3G Capital, BDT ("merchant bank") and a JAB fund manager all report PE funds. Under an ADV-only test, Burger King, Popeyes and Wendy's carry minority holders flagged as PE.
- **A name match does not prove identity.** Four leads match only by name. Confirming them needs a source that ties the CRD to the deal, such as the sponsor's site naming its adviser or the deal release naming the fund.
- **Four firms are not in either file:** Skyline Global Partners, H&W Investco, Pine Tree Equity and AEA Investors. Absence from Form ADV does not mean "not PE": a firm can file under another name, be a state-registered adviser or a family office, or file nothing.

## 6. BDC overlap

**Data.** The source is the SEC/DERA BDC data sets ([page](https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets); readme in [edgar-bdc.md](../../engine/research/edgar-bdc.md)): monthly files `2026_07`, `2026_08` (76 MB; the main Q2 10-Q month), `2026_09` and `2026_10`, downloaded 2026-11-05.
- `soi.tsv` across the four files: 173 BDCs.
- For the period ended 2026-06-30: 172 BDCs and 147,678 holding rows. A few BDCs carry other period ends (Saratoga 2026-05-31 and 2026-08-31; Ares Capital also 2026-09-30), and those are shown as filed.
- Searched columns: `Investment, Identifier Axis`, `Investment, Issuer Name Axis`, `InvestmentsIdentifier` and the Issuer Name enumeration.

**Method.**
- Regex search for each brand name, operating-company name and parent name the workers reported (about 130 patterns). Each hit was then read by hand.
- A brand counts as overlapping only when the filer's own text ties the borrower to the brand, in one of three ways:
  - **Filer's label:** e.g. "Fitness International, LLC (LA Fitness)" or "1-800 Contacts (CNT Holdings I Corp)".
  - **Exact legal name:** the borrower's name matches one the brand's own sources use, e.g. "Equinox Holdings, Inc." or "Xponential Fitness LLC".
  - **Another SEC filing:** "ECP Parent, LLC" is tied to EyeCare Partners through a shared LEI. Partners Group Private Equity Fund, LLC's N-PORT for the period ended 2026-06-30 lists `<name>EYECARE PARTNERS</name> <lei>254900ZAACWK09RJ8W93</lei> <title>ECP Parent, LLC</title>` ([N-PORT, filed 2026-08-31](https://www.sec.gov/Archives/edgar/data/1447247/000141036826090305/primary_doc.xml)).
- False positives removed:
  - "Bloomington Holdco, LLC (BW Fusion)", which matched "Bloomin".
  - "Equinox Buyer, LLC", a "Specialized Finance" borrower held by StepStone and two Stone Point BDCs, which is not the gym company.
  - "PennantPark-TSO Senior Loan Fund II", which matched "TSO".

**Result: 21 of 90 ranked brands, plus 1 added eyewear row.**

| Category | Brand row(s) | Borrower as filed | BDCs | Brand's owner kind (§2–4) |
|---|---|---|---|---|
| Restaurants | Dunkin', Sonic, Arby's, Buffalo Wild Wings | Inspire Brands, Inc. (filer's label "(Arbys & Buffalo Wild Wings)") | 1: Crescent Private Credit Income Corp | PE-owned |
| Restaurants | Raising Cane's | Raising Cane's Restaurants, LLC | 4: Ares Strategic Income Fund, Barings Private Credit Corp, Blackstone Private Credit Fund, Goldman Sachs Private Credit Corp | not found |
| Gyms | LA Fitness | Fitness International, LLC (filer's label "(LA Fitness)" at Saratoga) | 3: Antares Private Credit Fund, Franklin BSP Capital Corp, Saratoga Investment Corp | not found |
| Gyms | 24 Hour Fitness | ADAN-B LLC (filer's label "(24 Hour Fitness)") | 3: TCW Direct Lending VIII, TCW Specialty Lending, TCW Star Direct Lending | not found |
| Gyms | Equinox | Equinox Holdings, Inc. | 6: Ares Capital Corp, Ares Strategic Income Fund, Diameter Credit Co, HPS Corporate Capital Solutions Fund, Sixth Street Lending Partners, Sixth Street Specialty Lending | Owner type not confirmed |
| Gyms | Crunch Fitness | Crunch Holdings, LLC; "Crunch Fitness Merger Sub LLC" | 7: Apollo Debt Solutions BDC, Golub Capital BDC, Golub Capital BDC 4, Golub Capital Direct Lending Corp, Golub Capital Direct Lending Unlevered Corp, Golub Capital Private Credit Fund, HPS Corporate Lending Fund | PE-owned |
| Gyms | Club Pilates, Pure Barre, StretchLab, BFT, YogaSix | Xponential Fitness LLC | 2: Fortress Private Lending Fund, HPS Corporate Capital Solutions Fund | public company |
| Gyms | Snap Fitness | Lift Brands, Inc. (loan); Snap Fitness Holdings, Inc. (equity and warrants) | 3: Capital Southwest, CION Investment Corp, WhiteHorse Finance | PE-owned |
| Gyms | CorePower Yoga | CorePower Yoga, LLC | 2: Bain Capital Private Credit, Bain Capital Specialty Finance | PE-owned |
| Gyms | [solidcore] | Solidcore Topco, LLC | 2: Fortress Private Lending Fund, John Hancock Comvest Private Income Fund | PE-owned |
| Eyewear | EyeCare Partners | ECP Parent, LLC (**equity**, not a loan) | 2: Carlyle Secured Lending, Carlyle Credit Solutions | PE-owned |
| Eyewear | MyEyeDr. | "MyEyeDr" (term loan) | 1: CIFC Direct Lending Evergreen Fund | PE-owned |
| Eyewear | AEG Vision | "AEG Vision" | 2: Bain Capital Private Credit, Bain Capital Specialty Finance | PE-owned |
| Eyewear | New Look Vision Group | New Look Vision Group, Inc.; New Look Corporation | 5: Bain Capital Specialty Finance, Golub Capital BDC, Golub Capital Private Credit Fund, OHA Senior Private Lending Fund (U), T. Rowe Price OHA Select Private Credit Fund | PE-owned |
| Eyewear (added row) | 1-800 Contacts | CNT Holdings I Corp (filer's label "1-800 Contacts (CNT Holdings I Corp)" at Crescent) | 7: Ares Strategic Income Fund, BlackRock Private Credit Fund, Blackstone Private Credit Fund, Crescent Private Credit Income Corp, Franklin BSP Capital, Goldman Sachs Private Credit Corp, North Haven Private Income Fund | not found (KKR lead) |

- **By owner kind:** 12 of the 21 overlapping ranked brands are PE-owned. 12 of the 22 PE-owned or PE-minority brands overlap: 4 of 9 restaurants, 4 of 9 gyms and 4 of 4 eyewear.
- **Not only PE borrowers:** the overlap also includes a founder-held chain (Raising Cane's), a public company (Xponential) and chains whose owner was not found (LA Fitness, 24 Hour Fitness, Equinox).
- **Restaurants overlap least, and why was not investigated.** Two names the workers reported as financing entities had no hits: "Domino's Pizza Master Issuer LLC" and "Jack in the Box Funding, LLC". Nor did the names for Subway, Jersey Mike's ("Submarine Buyer LLC"), Pizza Hut/LongRange, Whataburger or Culver's.

**Evidence rows.** There is one row per BDC per period, and each link opens the filing in the SEC inline viewer. Identifier text is as DERA's `soi.tsv` stores it. The filer's `|` separators appear as `¦` so the table renders, and `…` marks a cut.

**Restaurants**

| Brand row(s) | BDC | Filing (form, period) | Identifier as filed (excerpt) |
|---|---|---|---|
| Inspire Brands (Dunkin', Sonic, Arby's, BWW) | Crescent Private Credit Income Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1954360/000119312526352548/ck0001954360-20260630.htm) | `…r Discretionary Distribution and Retail Inspire Brands, Inc. (Arbys & Buffalo Wild Wings) Investment Type Senior Secured First Lien Term Loan In…` |
| Raising Cane's | Ares Strategic Income Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1918712/000162828026054923/asif-20260630.htm) | `Raising Cane's Restaurants LLC , First lien senior secured loan` |
| Raising Cane's | Barings Private Credit Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1859919/000185991926000068/bdc-20260630.htm) | `Raising Canes Restaurants LLC ¦ First Lien Senior Secured Term Loan` |
| Raising Cane's | Blackstone Private Credit Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1803498/000180349826000048/bcred-20260630.htm) | `Raising Cane's Restaurants, LLC ¦ Emerald JV LP` |
| Raising Cane's | Goldman Sachs Private Credit Corp. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1920145/000119312526340582/ck0001920145-20260630.htm) | `…ted States 1st Lien/Senior Secured Debt Raising Cane's Restaurants, LLC Industry Hotels, Restaurants & Leisure Interest Rate 5.64% Reference R…` |

**Gyms**

| Brand row(s) | BDC | Filing (form, period) | Identifier as filed (excerpt) |
|---|---|---|---|
| 24 Hour Fitness (ADAN-B) | Tcw Direct Lending VIII LLC | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1825265/000119312526346657/ck0001825265-20260630.htm) | `…tels, Restaurants & Leisure ADAN-B LLC (24 Hour Fitness), Acquisition Date 04/30/25 Revolver - 9.48% (SOFR + 5.75%, 1.50% Floor) Net Assets 0.2% …` |
| 24 Hour Fitness (ADAN-B) | Tcw Specialty Lending LLC | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/2066811/000119312526346673/ck0002066811-20260630.htm) | `…tels, Restaurants & Leisure ADAN-B LLC (24 Hour Fitness), Acquisition Date 04/30/25 Revolver - 9.48% (SOFR + 5.75%, 1.50% Floor) Net Assets 0.2% …` |
| 24 Hour Fitness (ADAN-B) | Tcw Star Direct Lending LLC | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1916608/000119312526346666/ck0001916608-20260630.htm) | `…els, Restaurants & Leisure, ADAN-B LLC (24 Hour Fitness), Acquisition Date - 4/30/2025 Investment - Term Loan - 9.42% (SOFR + 5.75%, 1.50% Floor)…` |
| CorePower Yoga | Bain Capital Private Credit | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1899017/000119312526349812/ck0001899017-20260630.htm) | `Services: Consumer CorePower Yoga, LLC First Lien Senior Secured Loan SOFR Spread 5.25% Interest Rate 8.92% Maturity Date 4/30/2031` |
| CorePower Yoga | Bain Capital Specialty Finance, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1655050/000119312526342491/bcsf-20260630.htm) | `Services: Consumer CorePower Yoga, LLC First Lien Senior Secured Loan SOFR Spread 5.25% Interest Rate 8.92% Maturity Date 4/30/2031` |
| Crunch | Apollo Debt Solutions BDC | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1837532/000119312526341358/ck0001837532-20260630.htm) | `Crunch Fitness [Member]` |
| Crunch | Golub Capital BDC 4, Inc. | [10-K/A, 2025-09-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1901612/000190161226000024/gbdc4-20250930.htm) | `Crunch Holdings, LLC, One stop 1` |
| Crunch | Golub Capital BDC 4, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1901612/000190161226000031/gbdc4-20260630.htm) | `Crunch Holdings, LLC ¦ One stop 1` |
| Crunch | Golub Capital BDC, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1476765/000147676526000048/gbdc-20260630.htm) | `Crunch Holdings, LLC ¦ One stop 1 ¦ Non-Affiliated Issuer` |
| Crunch | Golub Capital Direct Lending Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1868878/000186887826000031/gdlc-20260630.htm) | `Crunch Holdings, LLC ¦ One stop 1` |
| Crunch | Golub Capital Direct Lending Unlevered Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1901606/000190160626000026/gdlcu-20260630.htm) | `Crunch Holdings, LLC ¦ One stop 1` |
| Crunch | Golub Capital Private Credit Fund | [10-K/A, 2025-09-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1930087/000193008726000078/gcred-20250930.htm) | `Crunch Holdings, LLC, One stop 1` |
| Crunch | Golub Capital Private Credit Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1930087/000193008726000099/gcred-20260630.htm) | `Crunch Holdings, LLC ¦ One stop 1` |
| Crunch | HPS Corporate Lending Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1838126/000162828026056772/hps-20260630.htm) | `Crunch Holdings LLC 1 ¦ Non-Affiliated Issuer` |
| Equinox (Equinox Holdings) | Ares Capital Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1287750/000162828026050307/arcc-20260630.htm) | `Equinox Holdings, Inc. [Member]` |
| Equinox (Equinox Holdings) | Ares Capital Corp | [10-Q, 2026-09-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1287750/000162828026067383/arcc-20260930.htm) | `Equinox Holdings, Inc. [Member]` |
| Equinox (Equinox Holdings) | Ares Strategic Income Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1918712/000162828026054923/asif-20260630.htm) | `Equinox Holdings, Inc. [Member]` |
| Equinox (Equinox Holdings) | Diameter Credit Co | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1916099/000119312526342470/ck0001916099-20260630.htm) | `…Lien Debt Hotels, Restaurants & Leisure Equinox Holdings, Inc Term Loan Interest Rate 10.98% Reference Rate SOFR Spread 7.25% Acquisition Date 3/2…` |
| Equinox (Equinox Holdings) | HPS Corporate Capital Solutions Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1989817/000162828026056793/hps-20260630.htm) | `Equinox Holdings, Inc. ¦ Non-Affiliated Issuer` |
| Equinox (Equinox Holdings) | Sixth Street Lending Partners | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1925309/000119312526335004/ck0001925309-20260630.htm) | `… Investments Hotel, Gaming, and Leisure Equinox Holdings, Inc. Second-lien loan ($10,983 par, due 6/2027) Initial Acquisition Date 3/13/2024 Refer…` |
| Equinox (Equinox Holdings) | Sixth Street Specialty Lending, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1508655/000119312526332725/tslx-20260630.htm) | `…t Investments Hotel, Gaming and Leisure Equinox Holdings, Inc. Investment Second-lien loan ($2,746 par, due 6/2027) Initial Acquisition Date 3/13/…` |
| LA Fitness (Fitness International) | Antares Private Credit Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1976336/000119312526349158/ck0001976336-20260630.htm) | `…ured Debt Diversified Consumer Services Fitness International LLC Asset Type First Lien Term Loan Reference Rate and Spread S + 4.50% Interest Rate 8.1…` |
| LA Fitness (Fitness International) | Franklin BSP Capital Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1825248/000182524826000024/fbcc-20260630.htm) | `Fitness International, LLC, Hotels, Restaurants & Leisure` |
| LA Fitness (Fitness International) | Saratoga Investment Corp. | [10-Q, 2026-05-31](https://www.sec.gov/ix?doc=/Archives/edgar/data/1377936/000121390026075931/ea0295366-10q_saratoga.htm) | `Fitness International, LLC (LA Fitness) - Services: Consumer - Term Loan B (1/24) - Loan` |
| LA Fitness (Fitness International) | Saratoga Investment Corp. | [10-Q, 2026-08-31](https://www.sec.gov/ix?doc=/Archives/edgar/data/1377936/000121390026107187/ea0306042-10q_saratoga.htm) | `Fitness International, LLC (LA Fitness) - Services: Consumer - Term Loan B (1/24) - Loan` |
| Snap Fitness (Lift Brands) | Capital Southwest Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/17313/000001731326000095/cswc-20260630.htm) | `LIFT BRANDS, INC [Member]` |
| Snap Fitness (Lift Brands) | CION Investment Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1534254/000153425426000010/cion-20260630.htm) | `Equity ¦ Snap Fitness Holdings, Inc., Warrants` |
| Snap Fitness (Lift Brands) | Whitehorse Finance, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1552198/000110465926093465/whf-20260630x10q.htm) | `Snap Fitness Holdings, Inc Warrants` |
| Solidcore | Fortress Private Lending Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/2012139/000119312526344953/ck0002012139-20260630.htm) | `…ents Debt Investments Consumer Services Solidcore Topco, LLC Investment First Lien - Term Loan Reference Rate and Spread SOFR+575 Interest …` |
| Solidcore | John Hancock Comvest Private Income Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1987221/000119312526349413/ck0001987221-20260630.htm) | `First Lien Senior Secured Solidcore Topco, LLC - Term Loan Industry Consumer Services Spread Above Index SOFR + 5.75% (1.50% …` |
| Xponential (Club Pilates, Pure Barre, StretchLab, BFT, YogaSix) | Fortress Private Lending Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/2012139/000119312526344953/ck0002012139-20260630.htm) | `…ents Debt Investments Consumer Services Xponential Fitness LLC Investment First Lien - Term Loan Reference Rate and Spread SOFR+675 Interest Rate 10…` |
| Xponential (Club Pilates, Pure Barre, StretchLab, BFT, YogaSix) | HPS Corporate Capital Solutions Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1989817/000162828026056793/hps-20260630.htm) | `Xponential Fitness LLC` |

**Eyewear**

| Brand row(s) | BDC | Filing (form, period) | Identifier as filed (excerpt) |
|---|---|---|---|
| 1-800 Contacts (CNT Holdings I Corp) | Ares Strategic Income Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1918712/000162828026054923/asif-20260630.htm) | `CNT Holdings I Corp ¦ First lien senior secured loan` |
| 1-800 Contacts (CNT Holdings I Corp) | Blackrock Private Credit Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1902649/000119312526338073/ck0001902649-20260630.htm) | `…ments Healthcare Providers and Services CNT Holdings I Corp. Instrument First Lien Term Loan Ref SOFR(Q) Floor 0.75% Spread 2.50% Total Coupon…` |
| 1-800 Contacts (CNT Holdings I Corp) | Blackstone Private Credit Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1803498/000180349826000048/bcred-20260630.htm) | `CNT Holdings I Corp. ¦ Emerald JV LP` |
| 1-800 Contacts (CNT Holdings I Corp) | Crescent Private Credit Income Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1954360/000119312526352548/ck0001954360-20260630.htm) | `… Investments Food, Beverage and Tobacco 1-800 Contacts (CNT Holdings I Corp) Investment Type Senior Secured First Lien Term Loan Interest Term S…` |
| 1-800 Contacts (CNT Holdings I Corp) | Franklin BSP Capital Corp | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1825248/000182524826000024/fbcc-20260630.htm) | `CNT Holdings I Corp., Personal Care Products` |
| 1-800 Contacts (CNT Holdings I Corp) | Goldman Sachs Private Credit Corp. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1920145/000119312526340582/ck0001920145-20260630.htm) | `…ted States 1st Lien/Senior Secured Debt CNT Holdings I Corp. Industry IT Services Interest Rate 6.09% Reference Rate and Spread S + 2.25% Matu…` |
| 1-800 Contacts (CNT Holdings I Corp) | North Haven Private Income Fund LLC | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1851322/000119312526342549/ck0001851322-20260630.htm) | `…tments Health Care Providers & Services CNT Holdings I Corp. Investment First Lien Debt Reference Rate & Spread S + 2.50% Interest Rate 6.16% …` |
| AEG Vision | Bain Capital Private Credit | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1899017/000119312526349812/ck0001899017-20260630.htm) | `Healthcare & Pharmaceuticals AEG Vision First Lien Senior Secured Loan SOFR Spread 5.90% Interest Rate 9.57% Maturity Date 3/27/2027` |
| AEG Vision | Bain Capital Specialty Finance, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1655050/000119312526342491/bcsf-20260630.htm) | `Healthcare & Pharmaceuticals AEG Vision First Lien Senior Secured Loan SOFR Spread 5.90% Interest Rate 9.57% Maturity Date 3/27/2027` |
| EyeCare Partners (ECP Parent, LLC) | Carlyle Credit Solutions, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1702510/000170251026000084/cars-20260630.htm) | `Investment ¦ Non-Affiliated Issuer ¦ Equity Investments ¦ ECP Parent, LLC ¦ Healthcare & Pharmaceuticals` |
| EyeCare Partners (ECP Parent, LLC) | Carlyle Secured Lending, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1544206/000154420626000055/csl-20260630.htm) | `Investment ¦ Non-Affiliated Issuer ¦ Equity Investments ¦ ECP Parent, LLC ¦ Healthcare & Pharmaceuticals` |
| MyEyeDr | CIFC Direct Lending Evergreen Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/2056516/000119312526350908/ck0002056516-20260630.htm) | `…ct Lns Health Care Providers & Services MyEyeDr Type Term Loan, Senior Secured Acquisition date 12/31/2025 Maturity date 4/15/2031 Curren…` |
| New Look Vision Group | Bain Capital Specialty Finance, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1655050/000119312526342491/bcsf-20260630.htm) | `Retail New Look Vision Group First Lien Senior Secured Loan - Delayed Draw CORRA Spread 5.25% Interest Rate 7.51% Maturity Date 5/26/2028` |
| New Look Vision Group | Golub Capital BDC, Inc. | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1476765/000147676526000048/gbdc-20260630.htm) | `New Look Corporation ¦ One stop 1 ¦ Non-Affiliated Issuer` |
| New Look Vision Group | Golub Capital Private Credit Fund | [10-K/A, 2025-09-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1930087/000193008726000078/gcred-20250930.htm) | `New Look Corporation and New Look Vision Group Inc, One stop` |
| New Look Vision Group | Golub Capital Private Credit Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1930087/000193008726000099/gcred-20260630.htm) | `New Look Corporation ¦ One stop` |
| New Look Vision Group | OHA Senior Private Lending Fund (U) LLC | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1955010/000195501026000014/brhc-20260630.htm) | `New Look Vision Group, Inc. ¦ CAD Revolver` |
| New Look Vision Group | T. Rowe Price OHA Select Private Credit Fund | [10-Q, 2026-06-30](https://www.sec.gov/ix?doc=/Archives/edgar/data/1901164/000190116426000022/oha-20260630.htm) | `New Look Vision Group, Inc. ¦ CAD Revolver` |

**What "no hit" means.**
- **Scope:** a name with no hit has no holding under that name in any BDC schedule of investments for Q2 2026. It does not mean the company has no private-credit debt. BDCs are only part of private credit, and this data does not show:
  - loans held by private funds, CLOs or banks;
  - whole-business securitizations;
  - debt raised under a holdco name that no source ties to the brand.
- **Not searched:** earlier periods (DERA goes back to Q4 2022), so overlap history is not shown.
- **Hidden borrower names:** several borrowers are holdcos whose names don't say the brand: "ECP Parent, LLC", "ADAN-B LLC", "CNT Holdings I Corp", "Submarine Buyer LLC". These link to a brand only when a filer adds a label or another filing ties them.

**BDC borrowers in these categories that are outside the top 30** (leads for the developer; their brand links were not checked):
- **Restaurants:**
  - Crumbl Enterprises, LLC: 9 BDCs across Blackstone, Golub and MidCap funds.
  - RL Investor Holdings LLC (fka Red Lobster Management, LLC): TCW Direct Lending VII, listed as a *controlled affiliate* investment.
  - Red Robin International, Inc.: TCW.
  - Flynn Restaurant Group LP, a large multi-brand franchisee: Oaktree Specialty Lending, Barings Private Credit Corp and others.
  - Others: Cooper's Hawk Intermediate, Barteca Restaurants, Ruby Tuesday Operations, Fertitta Entertainment, BCPE Grill Parent, Cafe Rio Holding, Taco Cabana (YTC Enterprises), Swensons Drive-In Restaurants, IFH Franchisee Holdings (Ares Capital), City BBQ, Angry Chickz, Philz Coffee.
- **Gyms:**
  - VASA Fitness Buyer, Inc. (Bain Capital BDCs) and Mountainside Fitness Acquisitions, LLC (Crestline).
  - Blink Holdings, Inc. (AB Private Credit Investors). It is still held at 2026-06-30, although PureGym bought Blink out of Chapter 11 on 2024-11-29 (PureGym's release, read by the gyms worker).
  - Fitness-named holdcos that could be franchisees of top-30 brands, unconfirmed: Excel Fitness Holdings / Excel Fitness Consolidator (Ares Capital), Bandon Fitness, Riser Fitness, One World Fitness PFF, Supreme Fitness Group NY Holdings, Renew Fitness Operations, Omega Midwest Buyer (dba Omega Fitness Holdings), CR Fitness Holdings, Camarillo Fitness Holdings, CDM Fitness Holdings, Fitness Ventures Holdings, US Fitness Holdings.
  - Not gym operators: equipment and software makers (Life Fitness, Titan Fitness, Core Health & Fitness, ABC Fitness).
- **Eyewear (mostly optometry and ophthalmology rollups):**
  - EyeSouth Eye Care Holdco / SCP Eye Care: 15 BDCs.
  - Acuity Eyecare Holdings, LLC: 5 Golub funds and PIMCO Capital Solutions BDC.
  - Others: CHA Vision Holdings (fka FR Vision Holdings), Chestnut Optical Midco, FYI Optical Acquisitions, Midwest Vision Partners Management, American Vision Partners, Center for Sight Management, Pair Eyewear (TriplePoint Venture Growth), ABB/Con-cise Optical Group (a contact-lens distributor).

## 7. Affiliate income

- **Restaurants: no brand-direct affiliate program found for any of the 30.** Network or aggregator listings surfaced but were not verified: Awin for Domino's (apparently UK), FlexOffers for "Starbucks Store Online", and Admitad pages for McDonald's, Taco Bell and Chipotle. The check was two category-wide searches plus brand-site browsing during the owner checks.
- **Gyms: no brand-direct affiliate program found.** Only network listings turned up: Orangetheory (FlexOffers), Planet Fitness (Admitad), 24 Hour Fitness (FlexOffers), and the Equinox+ app on an aggregator. The check was one category-wide search.
- **Eyewear: brand-direct programs confirmed on their own pages:**
  - [Zenni](https://www.zennioptical.com/c/affiliate) (via Impact): "We've partnered with Impact Radius to bring you a market-leading affiliate advertising program."
  - [GlassesUSA](https://www.glassesusa.com/affiliates): "Earn up to 30% commission, the highest rate in the industry."
  - [EyeBuyDirect](https://www.eyebuydirect.com/affiliate-program)
  - [Walmart](https://affiliates.walmart.com/), store-wide rather than optical-specific.
  - **Warby Parker:** probable. An Awin merchant profile was found but not opened, and the site's footer `/affiliates` link returned 404 to curl.
  - **LensCrafters:** network listings only. Ray-Ban (a sister brand) has an affiliates page that came up in search and was not fetched.
  - **1-800 Contacts and Visionworks:** blocked (403).
  - **Overlap with PE:** none of the 4 PE-owned eyewear rows is a consumer online seller. They are practice rollups (EyeCare Partners, MyEyeDr, AEG Vision) or a retail group (New Look). So in eyewear, affiliate income and PE ownership sit on different brands.

## 8. Method and cost

**Setup.** One parent agent and three worker agents, all the same model. Each worker covered one category, and the three ran in parallel.
- **Workers:** built the ranking and the per-brand table.
- **Parent:**
  - probed SEC access;
  - downloaded the DERA BDC and Form ADV files;
  - ran the BDC and ADV matching;
  - re-checked every quote;
  - settled Whataburger and the ECP Parent link;
  - assembled this file.
- **Per-brand cap:** about 5 fetches, then "not found".
- **Elapsed time:** 2026-11-05 01:15 to 02:09 UTC, about 54 minutes for all three categories.

| | Restaurants | Gyms | Eyewear | Parent (shared) |
|---|---|---|---|---|
| Wall-clock | 25 min | 26 min | 32 min | about 54 min, partly overlapping the workers |
| WebSearch | 15 (+2 by the parent) | 36 | 30 | 2 (the same Whataburger searches, not extra) |
| WebFetch | 19 | 50 | 13 (2 usable) | 0 |
| curl / direct HTTP | about 133 (about 115 to SEC) (+2 by the parent) | 31 (25 to SEC) | about 115 (17 to SEC) | about 110 (see below) |
| Agent tokens | about 261k | about 258k | about 282k | not metered |
| Tool calls | 111 | 120 | 161 | — |
| Rows with owner kind settled | 27 / 30 (90%), plus Panera settled only for 2017 | 16 / 30 (53%) | 18 / 30 (60%) | |

The parent's requests (about 110):
- 3 SEC probes;
- 1 BDC data-set page, 4 size checks and 4 monthly zips (80 MB);
- 1 Form ADV page and 2 zips (6 MB);
- 92 page downloads for the quote check;
- 4 for Whataburger;
- 3 for the ECP Parent link (2 full-text searches and the N-PORT).

Each BDC or ADV pass over the downloaded files takes seconds.

**What was cheap.**
- **Public parents** cost 2–5 EDGAR requests per brand: the latest 10-K for listing and model, and the DEF 14A for 5%+ holders. Their quotes can be checked mechanically.
- **Brands bought from a public company** were also cheap: EDGAR full-text search finds the completion 8-K or tender-offer filing, which names the buyer and the date (Dunkin', Sonic, BWW, Arby's, Popeyes, Panera, Applebee's, Pizza Hut).
- **Sponsor portfolio pages rendered on the server** (Roark, Leonard Green, TSG, TZP, FFL, Riata, Charlesbank) settled several brands per fetch and separate current holdings from previous ones.
- **BDC overlap and ADV flags** are one-time downloads followed by text matching. A new category needs only its list of name variants.

**What made brands slow** (5–9 fetches each, often still unsettled):
1. **Private founder or family chains with no SEC record.** Their own sites block automated fetches (403: Raising Cane's, Panda Express, Dairy Queen's history page, 1-800 Contacts, LensCrafters, Visionworks) or render only with JavaScript (Panda Restaurant Group, Whataburger's newsroom, EssilorLuxottica).
2. **Old PE deals with no current confirmation.** The sponsor's page renders only with JavaScript or is gone (404), as for LA Fitness (civc.com, mdcp.com, sepfunds.com), Keplr, Total Vision and Culver's (Roark's PDF). Deal releases on Business Wire return 403 to automated fetches.
3. **Ownership changes in 2025–26 that the rankings predate.** Jersey Mike's IPO, the Pizza Hut sale, Eyemart to VSP, Lumina to MyEyeDr (trade press), EyeCare Partners' pending optometry sale, and U.S. Vision's closures (trade press). The eyewear ranking uses 2024 data and is already stale in at least 4 rows.
4. **Rankings.**
   - Gyms has no free, current top-30 list. Athletech's list is free only for the top 9. Franchise Times is robots-disallowed. Club Industry's last edition was in 2021.
   - Eyewear's 2026 edition is a flipbook that couldn't be read.
   - NRN's sales figures sit in slide images.
   - The ranking step took about 8 of the gyms worker's 26 minutes and 13 requests for eyewear.
5. **Consortium financings.** A release can name investors without saying who controls (Equinox).
6. **BDC holdco names.** A borrower such as "ECP Parent, LLC" or "ADAN-B LLC" needs a second filing or the filer's own label to tie it to a brand.

**Which kinds of brands had no primary source for the owner:**
- **Founder or family-held private chains** whose only owner statement would be on their own site, and the site was unreadable: Panda Express, Raising Cane's.
- **Small franchisors whose pages name founders but never owners:** HOTWORX, Burn Boot Camp, The Exercise Coach, 9Round, Fit Body Boot Camp, UFC GYM, TITLE Boxing.
- **Long-held private chains with old PE deals:** LA Fitness, 24 Hour Fitness (lender-owned per secondary sources), F45 (after it deregistered with the SEC).
- **Regional or doctor-owned optical chains and licensing networks:** Cohen's, Texas State Optical, Marion, Wisconsin Vision, Today's Vision, Emerging Vision, Vision Associates.
- **PE rollups known only from trade press or directories:** Keplr, Total Vision, Lumina.
- **Online sellers whose owner wasn't found:** Zenni, GlassesUSA, 1-800 Contacts (KKR lead).

**Arithmetic for ~12 more categories** (numbers only; the decision is the developer's):
- **Per-category cost from this pilot:** one worker for 25–32 minutes, about 120–170 requests and about 260–280k agent tokens. For 12 categories that is about 1,400–2,000 requests and about 3.1–3.4M agent tokens.
- **Wall-clock:** with 3 workers at a time, that is 4 rounds of about 30 minutes, plus about 15 minutes of parent checks per round: roughly 3 hours.
- **Shared setup carries over:** the DERA and ADV files are reused (refresh monthly). Each new category adds a BDC name pass (seconds) and 30–40 quote-check downloads.
- **Unsettled share under the same ~5-fetch cap:**
  - about 10% where most brands have public or sponsor parents (restaurants);
  - 40–47% where private franchisors and regional chains dominate (gyms, eyewear).
  - Untested: a higher cap, or other sources (franchise disclosure documents, state SoS records), would change this.
- **Rankings are a per-category unknown.** So is each category's mix of public, sponsor-held and private brands, which is what drives the unsettled share. Neither was checked for the remaining categories.

### Per-category worker logs

#### Restaurants (worker log; the parent later settled Whataburger, see R25)
- **Time:** 2026-11-05T01:18:30Z to 2026-11-05T01:43Z, about 25 minutes wall-clock for 30 brands (including writing and a self-check).
- **Self-check:** all 57 evidence quotes citing sec.gov were string-matched against the curl'd filing text with a script (whitespace collapsed, curly quotes normalized), and 57 of 57 were found. Non-SEC quotes (about 15, from WebFetch) were not mechanically re-checked.
- **Calls:** 15 WebSearch, 19 WebFetch, about 133 curl/HTTP requests. About 115 of those went to SEC (submissions JSON, 10-K/10-Q/DEF 14A/8-K/424B4 documents and EDGAR full-text search), all served under the contact-free user agent "EvidenceEngine ownership-research bot (category audit pilot)" at ≤2 req/s. The rest went to roarkcapital.com, inspirebrands.com, jabholco.com, pandarg.com, whataburger.com, bdtmsd.com and similar sites.
- **What was fast:** public parents (16 brands). One script pulled each latest 10-K and DEF 14A from EDGAR (about 2 requests per filing) and regex search found the listing, franchise-model and 5%-holder sentences. That is roughly 5 requests and well under a minute per brand. Sponsor-owned brands acquired from public companies (Dunkin', Sonic, BWW, Arby's, Popeyes, Panera, Applebee's) were also fast: EDGAR full-text search finds the completion 8-K or tender-offer filing, which states the buyer and date. The Roark portfolio page HTML separates "current" from "previous" investments, which confirmed current status for six brands at once.
- **What was slow, and why:**
  - Panda Express, Raising Cane's, Whataburger: privately held with no SEC footprint. Their sites are script-rendered (pandarg.com, whataburger.com) or block automated fetches (raisingcanes.com 403, pandaexpress.com 403). Each took 5–7 calls and remained "not found".
  - Panera: settled for 2017 via SEC, but no primary source reconfirms current JAB ownership (the JAB investments page is script-rendered).
  - Culver's: the sponsor's own release PDF is gone (404), so it rests on a press-release reprint plus the sponsor's portfolio listing.
  - Dairy Queen since-date: dairyqueen.com 403.
  - Pizza Hut and Jersey Mike's needed fresh checks because the leads were stale (both changed in 2026); EDGAR settled both in about 6 requests each.
- **Gaps by kind:**
  - (1) Founder- or family-held private chains with no SEC filings and no sponsor (Panda, Raising Cane's): a primary owner source exists only on the company's own site, which was unreadable by script.
  - (2) Private chains owned by investment firms that don't publish portfolio pages in fetchable HTML (Whataburger/BDT, Panera/JAB): current status unconfirmed.
  - (3) Acquisition dates for brands native to public parents were not checked (marked "not checked"), because they are not ownership changes.
- **Affiliate programs:** checked with two web searches across the top chains plus brand-site browsing during owner checks. No brand-direct affiliate program found for any of the 30. Only third-party network or aggregator listings surfaced (Awin for Domino's, likely UK; FlexOffers for Starbucks Store; Admitad pages for McDonald's, Taco Bell and Chipotle), none verified. Practically, restaurants look like a near-zero affiliate category.
- **Blocked or unusable:** raisingcanes.com (403), pandaexpress.com (403), dairyqueen.com (403), globenewswire.com (403), businesswire.com (403 to curl). Old roarkcapital.com/files PDFs return 404. jabholco.com and whataburger.com are script-rendered. NRN's ranking slideshow carries sales figures only in images.
- **Quote caveat:** quotes from WebFetch pages (Chick-fil-A, Subway, Ilitch, Little Caesars franchise site, franchising.com) passed through a summarizer and may differ in apostrophes or quote marks. SEC quotes were taken from the curl'd text with whitespace collapsed; inline tags in the HTML may split some sentences.

#### Gyms (worker log)
- Time: start 2026-11-05T01:18:29Z, end 2026-11-05T01:44:33Z (about 26 minutes; the ranking search took ~8 of them).
- Calls: WebSearch 36, WebFetch 50, HTTP via curl/python 31. Of the 31, 25 went to SEC (submissions JSON, 10-K/DEF 14A/13D/15-12G documents, 6 full-text searches) and 6 elsewhere (franchisetimes.com robots and page, withorbital.com ×4). SEC documents downloaded: 9 (PLNT, LTH and XPOF 10-K and DEF 14A; F45 13D/A, 8-K and 15-12G). One PDF (PureGym's Blink release) was read locally with pypdf.
- Cheap brands: public companies. One 10-K plus one DEF 14A settled Planet Fitness, Life Time and all five Xponential brands (7 brands from 6 SEC documents), with mechanically checked quotes. Sponsor portfolio pages that render server-side (Roark, LGP, TSG, TZP) settled 2–3 brands per fetch.
- Slow brands and why:
  - LA Fitness, 24 Hour Fitness, F45, Equinox: 5–6 fetches each, still not settled. Private and long-held, no current press release, sponsor pages render with JavaScript (civc.com, mdcp.com) or 404 (sepfunds.com, lcatterton.com, mainpostpartners.com), Business Wire returns 403, and SEC deregistration (F45) ended the public record.
  - Barry's: 5 fetches; only a law-firm release, because the PR copy returned 403.
  - Gold's Gym: 4 fetches; the owner sentence is only on RSG's German page.
  - Chuze was researched (2016 Main Post Partners PR) and then dropped from the top 30 for having too few units, as was Blink/PureGym US (PureGym bought it out of Chapter 11 on 2024-11-29 for $121m per PureGym's release; about 56 gyms).
- Brands with no primary source for the owner:
  - long-held private chains with old PE deals (LA Fitness, 24 Hour Fitness)
  - ex-public companies after deregistration (F45)
  - small founder-led franchisors whose own pages name founders but never owners (9Round, Fit Body Boot Camp, UFC GYM, TITLE Boxing; HOTWORX, Burn and Exercise Coach only name founders)
  - companies financed by consortiums where the "investors" release does not say who controls (Equinox)
- Affiliate: checked with one category-wide search only. Gyms have no brand-direct affiliate pages. Network or aggregator listings exist for Orangetheory (FlexOffers), Planet Fitness (Admitad), 24 Hour Fitness (FlexOffers) and Equinox+ (aggregator). The category looks weak for affiliate income.
- Ranking gap: no free, current, robots-permitted ranking of US gym brands covers 30 brands. This is the largest method weakness for this category.
- Blocked or refused:
  - franchisetimes.com: robots.txt disallows ClaudeBot/anthropic-ai, so I stopped after 2 fetches.
  - 403: americanspa.com, businesswire.com, journaldespalaces.com, finanzen.net, withorbital.com (it now redirects to fairground.run).
  - 404: sepfunds.com/portfolio, mainpostpartners.com/portfolio, lcatterton.com/portfolio, goldsgym.com/about-us, corepoweryoga.com/about, titleboxingclub.com/franchise, the PureGym corporate release page.
  - JS-only (no entries): mdcp.com, civc.com, princetonequitygroup.com.
- Quote verification: every quote from an SEC document was string-checked against the downloaded text (20 of 20 matched). Quotes from WebFetch come through a summarizer, which cut several to under 125 characters. Some contain curly apostrophes (’) as the summarizer returned them, so they may fail a strict match if the page uses straight ones.
- Leads for the parent's BDC check: Equinox Holdings (Sixth Street Lending Partners, TSLX and HPS Corporate Capital Solutions 10-Qs, per EDGAR full-text search); EōS Fitness (Golub Capital 2019 one-loan release); Solidcore (Comvest Credit Partners 2025); Fitness Connection (Golub Capital release on Roark's 2019 acquisition, not in the top 30).

#### Eyewear (worker log)
- Start 2026-11-05T01:18:31Z, end about 01:50Z: **about 32 minutes** wall clock.
- Calls: **WebSearch 30**, **WebFetch 13** (2 returned usable text, 11 failed: 404 ×5, 403 ×3, empty JavaScript page ×3, TLS ×1). **curl about 115 requests** (103 logged lines, plus about 12 early or unlogged). SEC: 17 sec.gov requests (5 EDGAR full-text searches, 4 submissions JSON, 1 index, 7 documents). The contact-free user agent was accepted by www.sec.gov, efts.sec.gov and data.sec.gov.
- Status mix of logged curl requests: 54 × 200, 23 × 404 (guessed about-page URLs), 6 × 403 (Business Wire, LensCrafters, Visionworks, 1-800 Contacts, StreetInsider, Partners Group), 5 × no response/TLS (Bregal Partners, Total Vision, Today's Vision guess, Vision Associates), 1 × 429 (galvnews), 1 × 202-empty (Euronext).
- **Per-row cost:** public companies were cheapest, about 2 requests each through EDGAR (submissions JSON, then the 10-K cover page; the DEF 14A ownership table added 1–2). Ranking acquisition took 13 requests (the 2026 flipbook was unreadable, and the PDF needed a hand-written text extractor because no PDF library is installed). EssilorLuxottica brands took 9: its site renders by JavaScript, its retail brand sites return 403, and the usable source was a press-release PDF reached through an iframe URL. Each PE rollup took 3–8 (EyeCare Partners 8, MyEyeDr 6, AEG 3, New Look 3).
- **Slow to settle:** (1) PE rollups whose sponsor pages render by JavaScript or are missing (Keplr/Imperial Capital, Total Vision/Bregal). (2) Deals announced only on Business Wire, which returns 403 to automated fetches (EyeCare Partners' 2026 optometry sale, U.S. Vision 2021, MyEyeDr's Lumina deal). (3) Big consumer sites that block bots (1-800 Contacts, LensCrafters, Visionworks). (4) EssilorLuxottica's JavaScript site.
- **No primary source for the owner, by kind:** (a) small regional or doctor-owned chains (Cohen's, Marion, Wisconsin Vision, TSO, Today's Vision, Emerging Vision), whose sites tell founder history but never name the current owner. (b) PE rollups whose only evidence is trade press or directories (Keplr, Total Vision, Lumina). (c) privately held online sellers (Zenni, GlassesUSA). (d) KKR's 1-800 Contacts, where both the company site and the sponsor release could not be reached.
- **Data-currency caveat:** the 2024-data ranking is already stale in at least 4 rows: Eyemart (VSP, Jan 2025), Lumina (MyEyeDr, Apr 2026, trade press), U.S. Vision (closed June 2026, trade press) and EyeCare Partners' optometry arm (pending sale to MyEyeDr). Category-level PE share needs re-dating at each audit.
- Competitor sites appeared in search results (ledger.worseonpurpose.com for EyeBuyDirect, Glasses.com and LensCrafters) and were **not opened**. Preqin and CB Insights results were not opened. No Reddit, WhoIsMyDentist or Private Equity Vet fetches.
- **Quote-check caveats for the parent:** quotes from the EssilorLuxottica and VM PDFs come from my own PDF text extraction, so line breaks and extra spaces are normalized. VSP's boilerplate has ® marks as separate elements. SEC cover-page quotes are whitespace-normalized table cells.

## 9. Unconfirmed / open

**Facts not settled** (each is marked in its row):
- **Restaurants:**
  - Panera: whether JAB still owns it; the last primary source is 2017.
  - Panda Express and Raising Cane's: owner.
  - Culver's: closing date.
  - Jersey Mike's: Blackstone's stake after the IPO.
  - Dine Brands: activist positions are live (13Ds filed 2026-11-02).
- **Gyms:**
  - Owner not found for 7 rows: LA Fitness, 24 Hour Fitness, F45, 9Round, Fit Body Boot Camp, UFC GYM, TITLE Boxing.
  - Not confirmed: who controls Equinox, and who owns RSG Group and Extraordinary Brands.
  - The composite list is not exhaustive. VASA, Chuze, Youfit, Fitness Connection, Club Studio and PureGym US were not checked.
- **Eyewear:**
  - Owner not found or owner type not confirmed for 12 rows.
  - Pending: EyeCare Partners' sale of its optometry business to MyEyeDr (announced 2026-09-28; the Business Wire release returned 403).
  - Trade press only: Lumina to MyEyeDr, and U.S. Vision's closures.
  - Vision Source: no source after 2015 confirms the current owner.
  - 1-800 Contacts: KKR is a lead only, from Bloomberg.
  - The 2026 Vision Monday list could not be read.
- **Form ADV:** firm identity for the four name-only matches (§5).
- **BDC:** only Q2-2026 holdings were searched, and fitness-named holdcos were not linked to franchise brands.

**Questions this raises for the developer** (numbers only; nothing here is decided):
1. **What a share counts.** This file counts brand rows. The alternatives are counting by parent company (Inspire = 1, Xponential = 1) or by sales: eyewear is 13.3% by rows and 20.5% by sales.
2. **A public company that PE controls.** Jersey Mike's is counted as PE-owned here, which follows the glossary's chain definition. The alternative is to count it as public.
3. **Public companies whose 5%+ holder's Form ADV reports PE funds.** Under the glossary ("PE minority stake" = every chain to PE has a minority hop) and an ADV-based firm test (ADR 0001), four rows would move from public to PE minority stake:
   - Burger King and Popeyes (3G, ~22% of RBI voting).
   - Wendy's (Trian, 7.9%).
   - Life Time (Leonard Green 11.2%, TPG 8.0%).

   Strictly read, the shares become **restaurants 12/30 (40.0%)** and **gyms 10/30 (33.3%)**; eyewear is unchanged. The workers counted these rows as public.
4. **What "eyewear" means.** The only public ranking is of optical *retailers*, which includes practice rollups. The affiliate programs sit on online sellers and frame brands that the list mostly leaves out.
5. **The `Any PE Funds` test.** It flags Trian, 3G, BDT and JAB as PE, and misses L Catterton's main US adviser (§5). This touches ADR 0001's firm test, not just this audit.

## Sources

Rankings (trade press, used for ranking only):
- Nation's Restaurant News, "2026 Top 500: The 50 biggest restaurant chains in America", 2026-06-16: https://www.nrn.com/top-500-restaurants/2026-top-500-the-50-biggest-restaurant-chains-in-america
- Athletech News, "America's Biggest Gym Brands by Location Count" (Wefranch data), 2026-03-19: https://athletechnews.com/americas-biggest-gym-brands-by-location-count-wefranch/
- Vision Monday, "VM's 2025 Top 50 U.S. Optical Retailers", 2025-06-18: https://www.visionmonday.com/vm-reports/top-50-retailers/article/vms-2025-top-50-us-optical-retailers/ (chart PDF: https://www.visionmonday.com/CMSDocuments/2025/06/vmtop50retailers_2025.pdf)

Data sets:
- SEC/DERA, BDC Data Sets (files `2026_07_bdc.zip` to `2026_10_bdc.zip`): https://www.sec.gov/data-research/sec-markets-data/bdc-data-sets
- SEC, Information About Registered Investment Advisers and Exempt Reporting Advisers (Nov-2026 files): https://www.sec.gov/data-research/sec-markets-data/information-about-registered-investment-advisers-exempt-reporting-advisers
- SEC EDGAR full-text search (JSON endpoint `efts.sec.gov/LATEST/search-index`, undocumented; see [edgar-bdc.md](../../engine/research/edgar-bdc.md))
- Partners Group Private Equity Fund, LLC, Form N-PORT for period 2026-06-30: https://www.sec.gov/Archives/edgar/data/1447247/000141036826090305/primary_doc.xml

Every per-brand fact is cited inline in §2–4 to its own filing, release or page.
