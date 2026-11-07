# Category audit: Pet stores

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (fetches logged 16:35–16:58 UTC) · Ownership facts come from primary sources only. Trade press and a location-data vendor supply the ranking only.

**Short answer**

| | Pet stores (26 ranked store chains) | Including 4 added online-first rows (N = 30) |
|---|---|---|
| PE-owned plus PE minority stake, by brand row | **5 / 26 (19.2%)**: PetSmart, Petco, Unleashed by Petco, Woof Gang Bakery & Grooming, Pet Food Express. All five are PE-owned (control, or no stated stake); none is a minority stake. | **6 / 30 (20.0%)**; adds Chewy (BC Partners, 88.4% of voting power) |
| Strict count (public company with a 5%+ holder whose Form ADV reports PE funds) | **No change found yet.** The only public non-PE ranked row is Petsense (Tractor Supply: Vanguard 12.2%, BlackRock 9.2%). The added PetMed rows have 5%+ holders Nina Capital Holdings Inc. (12.2%), SilverCape Investments Limited (12.1%) and Renaissance Technologies LLC (5.6%), types not confirmed; Form ADV is for the assembler. | same |
| Owner not found | **13 / 26 (50.0%)**, plus Hollywood Feed (private, owner not stated) and Mud Bay (ESOP stake >10%, rest not stated) | 13 / 30 |
| Share of stores in the ranked rows that sit on PE-owned rows | **61.0%** (3,271 of 5,358 US locations; counts from mixed dates and sources) | — |
| Brand-direct affiliate programs | **2 found**: Chewy (via Impact; a PE-controlled row) and 1-800-PetMeds. PetSmart and Petco: network listings only (brand pages returned 500 / 403). | |

- **Fewer than 30 national chains exist** in the sources found. The list below is every national or large regional US pet specialty chain found with about 12 or more locations, 26 rows, ranked by US location count. Online-first retailers are added as unranked rows A1–A4, as the pilot's eyewear section did.
- **Biggest finding:** the two largest store chains and the largest online pet retailer are all PE-controlled. BC Partners controls both PetSmart (private, since 2015) and Chewy (NYSE: CHWY, "controlled company"). CVC and CPP Investments control Petco (Nasdaq: WOOF, "controlled company", 64.4% of total voting power).
- **Lender-owned, not PE (as sources state):** Pet Supplies Plus (#3) and its sister Wag N' Wash went to Fusion Parent, LLC when Franchise Group emerged from Chapter 11 on 2025-06-06; the plan equitized "the first lien debt into 100% of the equity". The lenders are not named in the releases read. Who they are (credit funds of PE firms or not) is open.
- **Formerly PE among non-PE rows:** Feeders Pet Supply (PNC Riverarch majority 2016 until Houchens, an ESOP, bought 100%); Pet Supermarket (Roark lists it under "Previous Investments"; current owner not found).

## How this was sourced (read first)

- **Ranking:** composite, by US location count (see "Ranking" below). ScrapeHero location reports (a data vendor, pages dated 2024-02 to 2026-10) supply most counts; company releases, a 10-K and two trade items supply the rest. Used for the ranking only, never as evidence of ownership.
- **Ownership facts:** SEC filings (10-K, DEF 14A, 8-K, 424B4), company and sponsor press releases, sponsor portfolio pages and company sites. Two company releases were readable only as reprints (franchising.com for Pet Supplies Plus/Wag N' Wash 2022; the EarthWise 2022 item on shopassociation.org, used for the count and model only) and are flagged.
- **SEC access:** all 22 SEC requests (www.sec.gov, data.sec.gov, efts.sec.gov) used the user agent `EvidenceEngine ownership-research bot (category audit)` with no contact detail, at most 2 requests per second (0.6 s sleep per request). All returned HTTP 200.
- **Robots:** robots.txt was read before each new site fetched with curl. Sites whose robots.txt disallows ClaudeBot / anthropic-ai were not used: petland.com (see the note in PT9), earthwisepet.com and petsbarn.com. Sites that returned bot challenges (HTTP 403, Cloudflare or PerimeterX) were not retried: petsuppliesplus.com, hollywoodfeed.com, petsupermarket.com, petco.com, allivet.com, petcarerx.com.
- **Never fetched:** competitor sites, Reddit, WhoIsMyDentist, Private Equity Vet, PitchBook, CB Insights and Preqin results that came up in search. Deal directories (mergr, privateequityinfo, privsource) and affiliate-network listings were read as search snippets only and are never cited.
- **Owner kinds are research notes, not engine classifications.** "PE-owned" means control, or a PE owner with no stated stake. A public company that a PE fund controls (Petco, Chewy) counts as PE-owned. Counts are by brand row: Petco and Unleashed by Petco are 2 rows; Pet Supplies Plus and Wag N' Wash are 2 rows.
- **Quotes:** copied from the curl'd page text with whitespace collapsed and HTML entities decoded. No quote below came through a WebFetch summarizer (no WebFetch calls were made).

## Ranking

**No free, current top-30 ranking of US pet specialty retailers was found.**
- Pet Business magazine's annual "Top 25 Retailers" list is the trade ranking (by store count, North America). The newest free copy found is the 2019 edition (GlobalPETS reprint, 2019-03-04, https://globalpetindustry.com/news/top-25-pet-retailers-north-america/), which names chains but not the full list. The 2023 edition is only in a digital-magazine flipbook (linked from https://animalhealthdigest.com/2023s-top-25-pet-retailers, 2024-03-05). petbusiness.com did not respond to curl. Rejected.
- ScrapeHero's "10 Largest pet stores in the United States in 2026" (updated 2026-10-29, https://www.scrapehero.com/location-reports/10-largest-pet-stores-in-the-usa/) counts stockists of pet-food brands (Blue Buffalo, Freshpet) as "pet stores", so its top-10 is unusable as a ranking. xMap's 2025 list has the same problem. Rejected as rankings; ScrapeHero's per-brand location reports were used for counts.

**Composite used:** candidate set = chains named in the 2019 Pet Business article, the pet-store brands with a ScrapeHero US location report (found by scanning its location-report sitemap), and chains surfaced in owner searches. Each chain is placed by its US location count:
- (a) ScrapeHero per-brand report (`https://www.scrapehero.com/location-reports/<Brand>-USA/`, the "There are N ... in the United States as of DATE" sentence), marked SH with its as-of date;
- (b) the company's own filing or release where that is the only count, or where it is fresher (Petsense: Tractor Supply 10-K);
- (c) trade press where nothing else was found (marked "trade").

**Not exhaustive.** Excluded by scope: pet-food brands, boarding and daycare chains (Pet Paradise, Dogtopia, Best Friends Pet Care, Hounds Town, The Dog Stop), farm stores (Tractor Supply's own banner), and Pet Valu (its US stores closed in 2020; it now operates in Canada). Unchecked, possibly above the cutoff: Natural Pawz (Texas; about 16 stores were bought back by its founders in 2023 per trade press), Pet Depot (California; acquired by EarthWise in 2023 per trade press), Global Pet Foods (mostly Canada), Chow Hound Pet Supplies (a Feeders banner, counted inside Feeders' 58).

| # | Brand (US locations: source, as of) | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PetSmart (1,537; SH, 2026-10-16) | consortium led by funds advised by BC Partners; BC Partners Fund XI with Apollo since a 2023 recapitalization ("Unrealised") | PE-owned | BC Partners (with La Caisse, GIC, StepStone, Longview in 2015; Apollo in 2023) | 2015-03-11 | — (delisted 2015) | bricks-and-mortar stores; company vs franchise split not stated | network listings only (Impact, FlexOffers); brand page returned HTTP 500 | PT1 |
| 2 | Petco (1,355; SH, 2026-10-18; "approximately 1,400 pet care centers" in the U.S. and Puerto Rico (10-K)) | Petco Health and Wellness Company, Inc., "indirectly controlled" by CVC funds and CPP Investments through Scooby Aggregator, LP (64.4% of total voting power) | PE-owned (public, sponsor-controlled) | CVC Capital Partners; Canada Pension Plan Investment Board | 2016-01-26 (IPO 2021) | WOOF | company-operated (all pet care centers leased) | network listings only (Rakuten / Impact per directories); petco.com returned 403 | PT2 |
| 3 | Pet Supplies Plus (752; SH, 2026-10-16) | Fusion Parent, LLC (created when Franchise Group emerged from Chapter 11; first-lien debt equitized into 100% of equity) | other: lender-owned (lenders not named) | none confirmed (formerly Sentinel Capital, per trade press) | 2025-06-06 | — | franchisor with corporate stores | none found | PT3 |
| 4 | Woof Gang Bakery & Grooming (288; SH, 2025-02-28; "more than 450 franchisee locations open or under development" (company, 2026-06-23)) | investors Garnett Station Partners and Great Hill Partners; stakes not stated | PE-owned (no stated stake) | Garnett Station Partners (2022); Great Hill Partners (2026) | 2022 (Garnett); 2026-06-23 (Great Hill) | — | franchise | none found | PT4 |
| 5 | Petsense by Tractor Supply (207; Tractor Supply 10-K, 2025-12-27; SH 198) | Tractor Supply Company | public company | none at 5%+ (Vanguard 12.2%, BlackRock 9.2%) | 2016-09-29 | TSCO | company-operated | none found | PT5 |
| 6 | Pet Supermarket (200; SH, 2026-06-23) | not found (Roark Capital lists it under "Previous Investments") | not found; formerly PE (Roark) | none current confirmed | not found | — | not found | none found | PT6 |
| 7 | Hollywood Feed (177; SH, 2026-07-09; 168 (company, 2025-07-15)) | Hollywood Feed, LLC; owner not stated (Shawn McGhee is president and CEO) | private, owner not stated (no PE evidence found) | none found | not found | — | not found | none found | PT7 |
| 8 | EarthWise Pet ("over 170" (2022 release, reprint)) | not found | not found | none found | not found | — | franchise-led (~75% franchisee-owned, ~25% corporate, 2022) | none found (site robots-disallowed) | PT8 |
| 9 | Petland (89; SH, 2025-11-27) | not found (petland.com robots-disallowed; not used) | not found | none found | not found | — | not found (franchise, per sources not usable) | none found | PT9 |
| 10 | Pet Food Express (69; SH, 2026-09-30) | Rainier Partners (investment May 2022, status "Current"; stake not stated) | PE-owned (no stated stake) | Rainier Partners | 2022-05 | — | not found | none found | PT10 |
| 11 | Pet Wants (68 retail (company, year-end 2025)) | not found | not found | none found | not found | — | franchise | none found | PT11 |
| 12 | Mud Bay (65; SH, 2026-05-13) | Mud Bay; employees' ESOT stake "more than 10%"; holder of the rest not stated | other: partly employee-owned (ESOP); majority owner not stated | none found | ESOP since 2015 | — | not found | none found | PT12 |
| 13 | Chuck & Don's (63; SH, 2026-10-14) | not found (trade press: parent Independent Pet Partners went bankrupt in 2023 and lenders took the chain) | not found | none current confirmed (IPP was TPG Growth-backed per trade press) | not found | — | not found | none found | PT13 |
| 14 | Feeders Pet Supply (incl. Chow Hound Pet Supplies) (58; Houchens release) | Houchens Industries (100%) | other: employee-owned (Houchens is an S Corp ESOP) | none current (PNC Riverarch held the majority from 2016) | release dated 2024-10-10 (trade press says April 2023) | — | company-operated | none found | PT14 |
| 15 | Concord Pet Foods & Supplies (33; company) | Mutschler family | family | none | not applicable (founder family, 1981) | — | company stores | none found | PT15 |
| 16 | Bentley's Pet Stuff (31; SH, 2026-05-13) | not found | not found | none found | not found | — | not found | none found | PT16 |
| 17 | Kahoots Feed & Pet (26; SH, 2026-07-24) | Kahoots ("Family-owned") | family | none | not found | — | not found | none found | PT17 |
| 18 | Wag N' Wash (25; trade, 2023-10-03) | Pet Supplies Plus, so Fusion Parent, LLC | other: lender-owned (via Pet Supplies Plus) | none confirmed | PSP bought it 2022-02; Fusion Parent since 2025-06-06 | — | franchise | none found | PT18 |
| 19 | Pet's Barn (25; SH, 2026-08-07) | not found (petsbarn.com robots-disallowed) | not found | none found | not found | — | not found | none found | PT19 |
| 20 | Healthy Spot (23; trade, 2022-08-22) | not found | not found | none found (directory lead: Monogram Capital, not confirmed) | not found | — | not found | none found | PT20 |
| 21 | Unleashed by Petco (22; SH, 2026-10-18) | Petco Health and Wellness Company, Inc. (see #2) | PE-owned (public, sponsor-controlled) | CVC Capital Partners; CPP Investments | not checked (Petco concept) | WOOF | company-operated | as Petco | PT21 |
| 22 | Choice Pet (17; SH, 2026-10-23) | not found | not found | none found | not found | — | not found | none found | PT22 |
| 23 | Kriser's Natural Pet (16; SH, 2026-09-18) | not found (same 2023 IPP bankruptcy as Chuck & Don's, per trade press) | not found | none current confirmed | not found | — | not found | none found | PT23 |
| 24 | Pet Pros (16; SH, 2026-07-13) | not found | not found | none found | not found | — | not found | none found | PT24 |
| 25 | Premier Pet Supply (14; company store list; SH 13 (2024-10-24)) | not found | not found | none found | not found | — | not found | none found | PT25 |
| 26 | Pet Club (12; SH, 2024-02-09) | not found | not found | none found | not found | — | not found | none found | PT26 |
| A1 | Chewy (online-first; added, not ranked) (online; plus Chewy Vet Care clinics) | Chewy, Inc., controlled by BC Partners affiliates (88.4% of total voting power) | PE-owned (public, sponsor-controlled) | BC Partners (consortium with La Caisse, GIC, StepStone, Longview) | 2017-05 (via PetSmart; IPO 2019) | CHWY | online retailer | **yes, brand-direct**: https://www.chewy.com/app/content/affiliate (via Impact) | PT27 |
| A2 | 1-800-PetMeds / PetMeds (online-first; added) (online) | PetMed Express, Inc. | public company | none identified (5%+: Nina Capital Holdings Inc. 12.2%, SilverCape Investments Limited 12.1%, Renaissance Technologies LLC 5.6%; types not confirmed) | not applicable (founded 1996) | PETS | online pet pharmacy | **yes, brand-direct**: https://www.1800petmeds.com/affiliateprogram.html | PT28 |
| A3 | PetCareRx (online-first; added) (online) | PetMed Express, Inc. (wholly owned subsidiary) | public company | as A2 | 2023-04 | PETS | online pet pharmacy | blocked (403) | PT29 |
| A4 | Allivet (online-first; added) (online) | Tractor Supply Company | public company | none at 5%+ | 2024-12-30 | TSCO | online pet and animal pharmacy | blocked (PerimeterX) | PT30 |

### Evidence
- **PT1 PetSmart**
  - Owner (2015): "Parent is indirectly controlled by a consortium including funds advised by BC Partners, Inc., La Caisse de dépôt et placement du Québec, affiliates of GIC Special Investments Pte Ltd, affiliates of StepStone Group LP and Longview Asset Management, LLC." — [PetSmart, Inc., Form 8-K, filed 2015-03-11](https://www.sec.gov/Archives/edgar/data/863157/000119312515087596/d887827d8k.htm)
  - Since: "On March 11, 2015, PetSmart, Inc., a Delaware corporation" … "completed its previously announced merger" — [same 8-K](https://www.sec.gov/Archives/edgar/data/863157/000119312515087596/d887827d8k.htm) (merger with Argos Merger Sub Inc., a subsidiary of Argos Holdings Inc.)
  - Owner (sponsor page, 2015 fund): "PetSmart was acquired in March 2015 in a public to private (PtoP) transaction by a consortium led by funds advised by BC Partners along with a number of Limited Partners." — [BC Partners, portfolio page "PetSmart - Chewy", accessed 2026-11-07](https://www.bcpartners.com/portfolio/petsmart-chewy/). The same page shows "Investment status Partially Realised/Publicly Traded".
  - Current: "PetSmart, which BC Partners acquired alongside Apollo, is seen as a destination for pet parents and their pets, with the widest in-store variety of pet products, including food, treats, toys, and accessories." and "Acquired in 2023, PetSmart is the leading bricks and mortar specialty pet retailer in North America, with 1,600+ stores across the US and Canada." — [BC Partners, portfolio page "PetSmart" (Fund XI), accessed 2026-11-07](https://www.bcpartners.com/portfolio/petsmart-xi/). The page shows "Investment status Unrealised".
  - Model: "bricks and mortar specialty pet retailer" (same page). Franchise/company split not stated.
  - Affiliate: network listings only (Impact, FlexOffers directory pages in search; not opened). `https://www.petsmart.com/affiliate-program.html` returned HTTP 500. No brand-direct page found.
  - BDC names: "PetSmart, Inc.", "PetSmart LLC", "Argos Holdings Inc.", "Argos Merger Sub Inc."
  - Notes: in-store services named on the BC Partners page: grooming, training, boarding and veterinary care (Banfield Pet Hospital clinics inside PetSmart stores were not checked). The 2023 "XI" entry and the "Partially Realised/Publicly Traded" entry describe one company held by two BC Partners funds; Apollo's stake is not stated.
- **PT2 Petco**
  - Owner: "We are currently indirectly controlled by certain funds (the “CVC Funds”) that are advised and/or managed by CVC Capital Partners (“CVC”) and Canada Pension Plan Investment Board, a Canadian company (together with its affiliates, “CPP Investments” and, together with the CVC Funds, our “Sponsors”)." — [Petco Health and Wellness Company, Inc., Form 10-K FY2025, filed 2026-03-13](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm)
  - Control: "Our Sponsors primarily exercise their control through Scooby Aggregator, LP (our “Principal Stockholder”), who holds shares of our Class A and Class B-1 common stock." — [Petco, DEF 14A, filed 2026-05-14](https://www.sec.gov/Archives/edgar/data/1826470/000182647026000040/woof-20260514.htm). The ownership table lists Scooby Aggregator, LP at 59.0% of Class A, 100.0% of Class B-1, **64.4% of total voting power** and 51.2% of director-election power (as of 2026-04-27).
  - Controlled company: "We are a “controlled company” within the meaning of the Nasdaq rules and, as a result, qualify for, and rely on, exemptions from certain corporate governance requirements." — [Petco 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm)
  - Since: "On January 26, 2016, the Company completed a merger (the “Acquisition”) whereby Petco Holdings, Inc. converted from a Delaware corporation to a Delaware limited liability company and became a wholly owned subsidiary of the Company." — [Petco 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm) (the Company was formed in 2015 "as an acquisition entity controlled by Scooby LP", same filing)
  - Ticker: WOOF on The Nasdaq Stock Market LLC (cover table of [Form 8-K, filed 2026-09-02](https://www.sec.gov/Archives/edgar/data/1826470/000119312526380189/woof-20260902.htm))
  - Model: "We lease all of our distribution center locations and all of our approximately 1,400 pet care centers in the U.S. and Puerto Rico." — [Petco 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm)
  - Affiliate: network listings only (directory pages name Rakuten and Impact; not opened). petco.com returned HTTP 403 to robots.txt, so no page was fetched.
  - BDC names: "Petco Health and Wellness Company, Inc.", "Petco Animal Supplies Stores, Inc.", "PET Acquisition LLC", "Scooby Aggregator, LP"
  - Notes: in-store vet brand Vetco: "we had approximately 300 full service veterinary hospitals in our network and operated approximately 1,600 Vetco clinics on a weekly basis" (same 10-K). CPP Investments is a pension investor, not a PE firm; CVC alone makes the row PE-owned.
- **PT3 Pet Supplies Plus**
  - Owner: "Following the transaction, both the Pet Supplies Plus ("PSP") and Buddy's Home Furnishings ("Buddy's") entities will be owned by the newly-created Fusion Parent, LLC." — [Franchise Group, Inc., press release "Franchise Group Successfully Completes Financial Restructuring", PR Newswire, 2025-06-06](https://www.prnewswire.com/news-releases/franchise-group-successfully-completes-financial-restructuring-302475683.html)
  - Owner kind: "The RSA contemplates the proposed equitization of the first lien debt into 100% of the equity in the reorganized enterprise, which would substantially reduce the Company's debt, enhance liquidity, and strengthen the enterprise for the benefit of Pet Supplies Plus, The Vitamin Shoppe, and Buddy's Home Furnishings and their stakeholders." — [Franchise Group, press release, PR Newswire, 2024-11-03](https://www.prnewswire.com/news-releases/franchise-group-reaches-agreement-with-first-lien-lenders-to-substantially-reduce-debt-enhance-liquidity-and-best-position-profitable-operating-businesses-for-sustainable-growth-302294886.html)
  - Lenders: "The ad hoc group of debtor-in-possession and first lien term lenders was advised by Paul Hastings LLP as legal counsel and Lazard as investment banker." — [2025-06-06 release](https://www.prnewswire.com/news-releases/franchise-group-successfully-completes-financial-restructuring-302475683.html). The lenders are not named.
  - Since: "Jun 06, 2025" (release dateline, same page)
  - Model: "Franchised locations of FRG's brands are not part of the proceedings." — [2024-11-03 release](https://www.prnewswire.com/news-releases/franchise-group-reaches-agreement-with-first-lien-lenders-to-substantially-reduce-debt-enhance-liquidity-and-best-position-profitable-operating-businesses-for-sustainable-growth-302294886.html)
  - Affiliate: none found (petsuppliesplus.com returned a Cloudflare 403 to robots.txt).
  - BDC names: "Pet Supplies Plus", "PSP", "Fusion Parent, LLC", "Franchise Group, Inc.", "Franchise Group Newco PSP"
  - Notes: trade press (not cited) reports that PSP and Wag N' Wash "formally separated" from Franchise Group on 2025-12-08 with a securitization financing, under the name "Pet Retail Brands". No primary copy of that release was read, and it does not change the owner stated above. Sentinel Capital (PE) owned PSP before Franchise Group bought it in 2021 (trade press). Franchise Group was taken private in 2023 (not checked). Whether any first-lien lender is a PE firm's credit arm is not known.
- **PT4 Woof Gang Bakery & Grooming**
  - Owner: "Woof Gang Bakery & Grooming (“Woof Gang” or the “Company”), a leading pet grooming and specialty retail franchise concept, today announced a growth investment from Great Hill Partners (“Great Hill”), a Boston-based investment firm with a long track record of partnering with category-defining businesses to accelerate their growth." — [Great Hill Partners, news release, 2026-06-23](https://www.greathillpartners.com/media/woof-gang-bakery-grooming-secures-strategic-growth-investment-from-great-hill-partners)
  - Owner: "Great Hill joins existing investor Garnett Station Partners who remains a significant and committed partner to Woof Gang’s continued growth." — [same release](https://www.greathillpartners.com/media/woof-gang-bakery-grooming-secures-strategic-growth-investment-from-great-hill-partners)
  - Since: "Jun 23, 2026" (release date on the same page). Garnett Station's 2022 investment: Business Wire release `https://www.businesswire.com/news/home/20220616005349/en` surfaced in search and was not fetched (Business Wire returned 403 to curl in the pilot).
  - Model: "Woof Gang has more than doubled its footprint since 2022, expanding to more than 450 franchisee locations open or under development across the United States." — [same release](https://www.greathillpartners.com/media/woof-gang-bakery-grooming-secures-strategic-growth-investment-from-great-hill-partners)
  - Affiliate: none found
  - BDC names: "Woof Gang Bakery & Grooming", "Woof Gang Bakery"
  - Notes: neither stake is stated in the release, so the row is PE-owned by the "no stated stake" rule. Trade press calls Great Hill's investment a "minority" one; Garnett Station's portfolio page (garnettstation.com/portfolio) renders its list by JavaScript. Grooming is part of the concept, so the brand is on the list as a retail-plus-grooming franchise.
- **PT5 Petsense by Tractor Supply**
  - Owner: "We operate retail stores under the names Tractor Supply Company and Petsense by Tractor Supply." — [Tractor Supply Co, Form 10-K FY2025, filed 2026-02-19](https://www.sec.gov/Archives/edgar/data/916365/000091636526000014/tsco-20251227.htm)
  - Listing: "The Company’s common stock trades on the NASDAQ Global Select Market under the symbol" (TSCO) — [same 10-K](https://www.sec.gov/Archives/edgar/data/916365/000091636526000014/tsco-20251227.htm)
  - Count and model: "At December 27, 2025, we operated a total of 207 Petsense by Tractor Supply stores in 23 states" — [same 10-K](https://www.sec.gov/Archives/edgar/data/916365/000091636526000014/tsco-20251227.htm)
  - Since: "Petsense On September 29, 2016, we acquired Petsense, a small-box pet specialty supply retailer focused on meeting the needs of pet owners, primarily in small and mid-sized communities, and offering a variety of pet products and services." — [Tractor Supply, Form 10-K FY2016, filed 2017-02-23](https://www.sec.gov/Archives/edgar/data/916365/000091636517000031/a2016form10-k.htm)
  - 5% holders: DEF 14A filed 2026-03-26 lists The Vanguard Group 12.2% and BlackRock, Inc. 9.2% — [Tractor Supply, DEF 14A](https://www.sec.gov/Archives/edgar/data/916365/000119312526126620/d16327ddef14a.htm)
  - Affiliate: none found
  - BDC names: "Tractor Supply Company", "Petsense, LLC"
- **PT6 Pet Supermarket**
  - Owner: not found
  - Former owner: Roark Capital's portfolio page lists "Pet Supermarket is the largest specialty retailer of pet food and pet-related supplies based in the southeastern US." inside the section marked `portfolio-section--previous` ("Previous Investments") — [Roark Capital, Portfolio page, accessed 2026-11-07](https://www.roarkcapital.com/portfolio). Pet Valu and Bosley's are in the same "previous" section.
  - Since: not found (trade press: Roark bought it from its founder in May 2015 and combined it with Pet Valu under "Pet Retail Brands" in 2016)
  - Model: not found
  - Affiliate: none found
  - BDC names: "Pet Supermarket, Inc.", "Pet Retail Brands"
  - Notes: slow, 6 requests and 3 searches. petsupermarket.com robots.txt allows crawling but its about page returned "Access to this page has been denied" (HTTP 403). A deal directory names Golub Capital, Penfund and Roark (lead only, not cited). The current owner after Roark's exit was not found.
- **PT7 Hollywood Feed**
  - Owner: not stated. "Hollywood Feed, LLC (Hollywood Feed) announced this week that it has entered into an agreement to acquire PetPeople Holdings, LLC (PetPeople)." and "“We’re thrilled to welcome PetPeople’s team members and customers into our family,” says Shawn McGhee, president and CEO of Hollywood Feed." — [Hollywood Feed press release, posted by the Greater Memphis Chamber, 2022-02-28](https://members.memphischamber.com/news/details/hollywood-feed-announces-acquisition-of-petpeople-holdings-02-28-2022)
  - Count: "About Hollywood Feed: Hollywood Feed serves pets, their owners, caretakers and communities in 168 stores across 19 states." — [Hollywood Feed press release, Greater Memphis Chamber, 2025-07-15](https://members.memphischamber.com/news/details/expansions-continue-across-south-for-retailer-hollywood-feed-07-15-2025)
  - Since: not found (trade press: the McGhees bought the chain in 2006)
  - Model: not found
  - Affiliate: none found
  - BDC names: "Hollywood Feed, LLC", "PetPeople Holdings, LLC"
  - Notes: hollywoodfeed.com returned a Cloudflare 403. Trade press (not cited) reports a Fortress Investment Group-led $112 million senior secured credit facility in 2026: a lender lead for the BDC check, not equity. PetPeople (acquired 2022) is now part of Hollywood Feed, so it is not a separate row.
- **PT8 EarthWise Pet**
  - Owner: not found
  - Count and model: "With the acquisition, EarthWise Pet expands to over 170 locations, of which approximately 75% are franchisee-owned and 25% are corporate-owned." — [EarthWise Pet release as carried by Pets Plus, reprinted on shopassociation.org, 2022-11-17](https://shopassociation.org/earthwise-pet-acquires-42-franchise-locations-and-independently-branded-stores/) (trade reprint; used for count and model only)
  - Affiliate: none found
  - BDC names: "EarthWise Pet", "EarthWise Pet Supply"
  - Notes: earthwisepet.com robots.txt disallows ClaudeBot and anthropic-ai, so the company site was not fetched. The same release quotes "Mike Seitz, CEO"; no owner statement found. Trade press (not cited) says EarthWise also bought Pet Pros (2021, kept as franchisees), Loyal Biscuit and Pet Depot (2023).
- **PT9 Petland**
  - Owner: not found
  - Notes: petland.com's robots.txt disallows ClaudeBot. Its about page was fetched once before the full robots.txt had been read (only its first lines were printed), and nothing from that page is used here. A search found only secondary profiles ("privately held"; founder Ed Kunzelman as chairman), not cited. Count: SH reports 89 US stores; Petland also has stores abroad.
  - BDC names: "Petland, Inc."
- **PT10 Pet Food Express**
  - Owner: "Pet Food Express Investment Date: May 2022 Status: Current" — [Rainier Partners, Portfolio page, accessed 2026-11-07](https://www.rainierpartners.com/portfolio)
  - Owner detail: "California’s trusted independent pet retailer, dedicated to helping pets live longer, healthier lives." and "Founded by Michael Levy, Pet Food Express has reimagined pet care by focusing on the very best brands and products." — [Rainier Partners, Pet Food Express page](https://www.rainierpartners.com/portfolio/pet-food-express/)
  - Owner kind: "Rainier Partners - Private Equity Firm - We invest in and help build great businesses" — [Rainier Partners, home page (page title)](https://www.rainierpartners.com/)
  - Since: May 2022 (portfolio tile)
  - Model: not found
  - Affiliate: none found
  - BDC names: "Pet Food Express", "Pet Food Express, Ltd."
  - Notes: stake not stated, so PE-owned by the "no stated stake" rule. petfoodexpress.com redirects to petfood.express (a delivery storefront) and has no robots.txt of its own.
- **PT11 Pet Wants**
  - Owner: not found
  - Count: "“We continued to expand our physical retail footprint, reached 68 retail locations systemwide, and saw double-digit growth that far exceeded overall pet industry growth." — [Pet Wants brand page on 1851 Franchise (marked "SPONSORED"), year-end 2025](https://1851franchise.com/petwants/pet-wants-closes-out-2025-with-60-retail-stores-open-and-double-digit-growth-2731508) (franchisor-paid content; used for count and model only)
  - Model: franchise ("2025 franchise development", same page)
  - BDC names: "Pet Wants", "Strategic Franchising Systems, Inc." (umbrella named in a search snippet, not confirmed)
  - Notes: a 2017 release title mentions "Franchise Funding Group's Investment" (not opened).
- **PT12 Mud Bay**
  - Owner: "In 2015, Mud Bay launched an employee stock ownership program that enables every Muddy who works at least twenty hours per week to acquire and grow an ownership stake in Mud Bay." and "Annual investments in our Employee Stock Ownership Trust had grown employee’s ownership stake to more than 10%." — [Mud Bay, "Our History", accessed 2026-11-07](https://blog.mudbay.com/our-history/)
  - Since: ESOP launched 2015 (same page)
  - Model: not found
  - Affiliate: none found
  - BDC names: "Mud Bay, Inc."
  - Notes: the page does not say who holds the rest. Secondary sources say the founding Wulff family (not cited).
- **PT13 Chuck & Don's**
  - Owner: not found. chuckanddons.com/content/about-us (fetched, robots allows) names no owner.
  - Notes: trade press (not cited): Independent Pet Partners (IPP), backed by TPG Growth, bought the chain on 2019-02-15; IPP filed for Chapter 11 in February 2023 with a deal for lenders to buy the 66 Chuck & Don's and Kriser's stores. No primary source on the closing or the current owner was found.
  - BDC names: "Chuck & Don's", "Independent Pet Partners Holdings, LLC", "IPP"
- **PT14 Feeders Pet Supply**
  - Owner: "BOWLING GREEN, KY – Houchens Industries (“Houchens”), one of the largest and most diversified wholly owned S Corp ESOPs in the United States, announced today that it has acquired Feeders Pet Supply (“FSP” or the “Company”)." — [Houchens Industries, news post "Houchens Acquires Feeders Pet Supply", "Published on October 10, 2024"](https://www.houchens.com/post/houchens-acquires-feeders-pet-supply)
  - Stake: "Now, the Company has entered into an agreement to sell 100% of the company to Houchens as a pathway for their employees to share in not only the ownership and success of FSP, but the ownership and success of Houchens." — [same page](https://www.houchens.com/post/houchens-acquires-feeders-pet-supply)
  - Former PE: "That growth accelerated in 2016 when PNC Riverarch, based in Pittsburgh, Pennsylvania acquired the majority ownership." — [same page](https://www.houchens.com/post/houchens-acquires-feeders-pet-supply)
  - Count and banners: "The Company operates under the names of Feeders Pet Supply and Chow Hound Pet Supplies across six different states." and "in addition to its 58 brick and mortar locations spread across Michigan, Indiana, Ohio, Kentucky, Tennessee, and North Carolina" — [same page](https://www.houchens.com/post/houchens-acquires-feeders-pet-supply)
  - Affiliate: none found
  - BDC names: "Feeders Supply Company", "Feeders Pet Supply", "Houchens Industries, Inc."
  - Notes: date disagreement only. The Houchens page is dated 2024-10-10; trade press dates the deal to April 2023. Both say Houchens bought it.
- **PT15 Concord Pet Foods & Supplies**
  - Owner: "Concord Pet Foods & Supplies is proud to still be family-owned by Larry and his daughter and son - Lindsay and Larry Jr, serving local customers throughout Pennsylvania, Maryland, New Jersey, and Delaware." — [Concord Pet Foods & Supplies, About page, accessed 2026-11-07](https://concordpetfoods.com/pages/about)
  - Count: "The company grew to 9 locations by 1998, 20 by 2010, and presently Concord Pet Foods & Supplies is proud to have 33 locations." — [same page](https://concordpetfoods.com/pages/about)
  - Affiliate: none found
  - BDC names: "Concord Pet Foods & Supplies"
- **PT16 Bentley's Pet Stuff**
  - Owner: not found (bentleyspetstuff.com home page, fetched, lists stores and "Since 2008" but no owner; it has no robots.txt file)
  - Notes: trade press (not cited) says Bentley's merged with Dee-O-Gee in 2021 to form "Pet Stuff Franchising", and that some St. Louis and Kansas City stores passed to Treats Unleashed.
  - BDC names: "Bentley's Pet Stuff", "Pet Stuff Franchising"
- **PT17 Kahoots Feed & Pet**
  - Owner: "Family-owned & Family-focused" — [Kahoots, "Story" page, accessed 2026-11-07](https://www.kahootsfeedandpet.com/pages/story) (a heading; the family is not named on the page)
  - Since: not found (trade: founded 1987)
  - Affiliate: none found
  - BDC names: "Kahoots Feed & Pet"
- **PT18 Wag N' Wash**
  - Owner (2022): "Pet Supplies Plus, (“PSP” or the “Company”) announced today it has acquired Wag N’ Wash, an emerging natural pet food, self-wash, and grooming franchise with over 15 locations." — [Pet Supplies Plus press release, reprinted on franchising.com, 2022-02-24](https://www.franchising.com/amp/news/20220224_pet_supplies_plus_acquires_wag_n_wash_natural_pet_food__grooming.html) (company release; third-party reprint)
  - Owner (current): via Pet Supplies Plus, owned by Fusion Parent, LLC since 2025-06-06 (see PT3)
  - Count: "The emerging brand currently has 25 locations open and 40 more in various stages of development across the US." — [Pet Insight, 2023-10-03](https://pet-insight.com/?p=27973) (trade press; count only)
  - Model: franchise (2022 release sentence above)
  - Affiliate: none found
  - BDC names: "Wag N' Wash", "Pet Supplies Plus"
- **PT19 Pet's Barn**
  - Owner: not found. petsbarn.com robots.txt disallows ClaudeBot, Claude-Web and anthropic-ai, so the site was not fetched.
  - BDC names: "Pet's Barn"
- **PT20 Healthy Spot**
  - Owner: not found. healthyspot.com/pages/about-us (fetched) has no owner statement.
  - Count: "Two new company-owned Los Angeles locations will open in Hollywood and Culver City this Fall, bringing Healthy Spot’s total store count to 23." — [Pet Insight, 2022-08-22](https://pet-insight.com/?p=25779) (trade press; count only)
  - Notes: a startup directory lists Monogram Capital as an investor (lead only, not confirmed).
  - BDC names: "Healthy Spot"
- **PT21 Unleashed by Petco**
  - Owner: "We operate 59 locations in the United States under our Unleashed brand, our concept which caters to more urban areas, as well as 89 locations in Mexico through our joint venture with Grupo Gigante." — [Petco, Prospectus (424B4), filed 2021-01-15](https://www.sec.gov/Archives/edgar/data/1826470/000119312521009268/d62974d424b4.htm)
  - Current owner and control: as PT2. The FY2025 10-K does not mention Unleashed; ScrapeHero counts 22 US stores (2026-10-18).
  - BDC names: as PT2
- **PT22 Choice Pet**
  - Owner: not found. choicepet.com/pages/our-story (fetched) has no owner statement.
  - BDC names: "Choice Pet"
- **PT23 Kriser's Natural Pet**
  - Owner: not found. krisers.com/content/about-us (fetched) has no owner statement. The site runs on the same platform as chuckanddons.com.
  - Notes: trade press: Kriser's was an IPP banner, and its Texas stores went to NP Acquisition LLC (Natural Pawz founders) and its Midwest stores to lenders in the 2023 bankruptcy. Not confirmed.
  - BDC names: "Kriser's Natural Pet", "Independent Pet Partners Holdings, LLC"
- **PT24 Pet Pros**
  - Owner: not found (no fetch beyond search; trade press links it to EarthWise Pet in 2021 and to 16 IPP stores in 2023)
  - BDC names: "Pet Pros"
- **PT25 Premier Pet Supply**
  - Owner: not found. The about page (fetched after its 30-second crawl delay) lists 14 Michigan locations but no owner. TV station pages call it "family-owned" (not cited).
  - BDC names: "Premier Pet Supply"
- **PT26 Pet Club**
  - Owner: not found (one search; only directory listings, which call it family-owned)
  - BDC names: "Pet Club"
- **PT27 Chewy (added, online-first)**
  - Owner: "The Company is controlled by a consortium including private investment funds advised by BC Partners Advisors LP (“BC Partners”) and its affiliates, La Caisse de dépôt et placement du Québec, affiliates of GIC Special Investments Pte Ltd, affiliates of StepStone Group LP and funds advised by Longview Asset Management, LLC (collectively, the “Sponsors”)." — [Chewy, Inc., Form 10-K FY2025, filed 2026-03-25](https://www.sec.gov/Archives/edgar/data/1766502/000176650226000034/chwy-20260201.htm)
  - Control: "Affiliates of funds advised by BC Partners Advisers LP (together with its affiliates, “BC Partners”) currently beneficially own common stock with a majority of the voting power of all of our outstanding common stock and have the power to approve any action requiring a majority vote of the combined voting power of our outstanding Class A common stock and Class B common stock." — [Chewy, DEF 14A, filed 2026-05-22](https://www.sec.gov/Archives/edgar/data/1766502/000114036126022529/ny20064174x1_def14a.htm). The table lists "BC Partners Holdings Limited/Argos Holdings GP LLC" with 100.0% of Class B and **88.4% of total voting power**; other 5%+ holders: Vanguard Capital Management 5.2%, AQR Capital Management, LLC 7.0%, BlackRock, Inc. 8.3% (of Class A).
  - Listing: "Our Class A common stock, par value $0.01 per share, is listed on the New York Stock Exchange under the symbol “CHWY” and began trading on June 14, 2019." — [Chewy 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1766502/000176650226000034/chwy-20260201.htm)
  - Since: "In May 2017, PetSmart acquired Chewy.com, the leading online specialty pet retailer in the US., significantly expanding its presence in e-commerce." — [BC Partners, "PetSmart - Chewy" page](https://www.bcpartners.com/portfolio/petsmart-chewy/). Separation from PetSmart: "We entered into certain transactions (the “Transactions”) with affiliates of BC Partners pursuant to an Agreement and Plan of Merger (the “Merger Agreement”), which closed on October 30, 2023." — [Chewy 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1766502/000176650226000034/chwy-20260201.htm)
  - Model: "Overview We are the largest pet e-tailer in the United States, offering virtually every product a pet needs." — [Chewy 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1766502/000176650226000034/chwy-20260201.htm)
  - Affiliate: "Chewy runs its affiliate program through Impact, where partners can apply, access affiliate links, and earn commission on qualifying orders." — [Chewy, "Chewy Affiliates (USA)" page, accessed 2026-11-07](https://www.chewy.com/app/content/affiliate)
  - BDC names: "Chewy, Inc.", "Argos Holdings Inc.", "Buddy Chester Sub LLC", "Citrus Intermediate Topco LLC"
  - Notes: in-store/clinic brand: "In 2024, we opened and operated eight veterinary clinics under the brand name “Chewy Vet Care,” offering pet health services including routine appointments, urgent care and surgery." (same 10-K). The 10-K says "BC Partners Advisors LP" and the proxy "BC Partners Advisers LP"; the spelling difference is in the filings.
- **PT28 1-800-PetMeds / PetMeds (added, online-first)**
  - Owner: "Our common stock is traded on the NASDAQ Global Select Market (“NASDAQ”) under the symbol" (PETS) — [PetMed Express, Inc., Form 10-K FY2026, filed 2026-06-02](https://www.sec.gov/Archives/edgar/data/1040130/000104013026000019/pets-20260331.htm)
  - 5% holders: DEF 14A filed 2026-06-25 lists, under "Other 5% Shareholders", Nina Capital Holdings Inc. 12.2%, SilverCape Investments Limited 12.1%, Renaissance Technologies LLC 5.6% — [PetMed Express, DEF 14A](https://www.sec.gov/Archives/edgar/data/1040130/000104013026000023/pets-20260625.htm). Nina Capital and SilverCape have filed Schedule 13Ds (2025-12 to 2026-06); their types are not stated in the proxy.
  - Affiliate: "It’s FREE and easy to monetize your content with our competitive affiliate program." — [PetMeds, Affiliate Program page, accessed 2026-11-07](https://www.1800petmeds.com/affiliateprogram.html)
  - BDC names: "PetMed Express, Inc."
- **PT29 PetCareRx (added, online-first)**
  - Owner and since: "In April 2023, we acquired PetCareRx, Inc. (“PetCareRx”), an online supplier of pet medications, foods, and supplies based in New York." — [PetMed Express 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1040130/000104013026000019/pets-20260331.htm)
  - Affiliate: blocked (petcarerx.com/affiliate-program returned HTTP 403)
  - BDC names: "PetCareRx, Inc.", "PetMed Express, Inc."
- **PT30 Allivet (added, online-first)**
  - Owner and since: "On December 30, 2024, the Company completed its acquisition of Allivet, an online pet pharmacy." — [Tractor Supply 10-K FY2025](https://www.sec.gov/Archives/edgar/data/916365/000091636526000014/tsco-20251227.htm)
  - Affiliate: blocked (allivet.com returned a PerimeterX "Access to this page has been denied" page)
  - BDC names: "Allivet, Inc.", "Tractor Supply Company"

### Rollups and groups that are not brands
Not counted in the list. Each groups locations or brands under a name no consumer sees.
- **Argos Holdings Inc. / BC Partners Holdings Limited / Argos Holdings GP LLC; Buddy Chester Sub LLC, Citrus Intermediate Topco LLC**: BC Partners holding vehicles for PetSmart (8-K 2015) and Chewy's Class B shares (Chewy DEF 14A 2026). Owner: BC Partners-advised funds and co-investors (PT1, PT27).
- **Scooby Aggregator, LP / Scooby LP**: CVC and CPP Investments vehicle that controls Petco (PT2).
- **Fusion Parent, LLC** (also called "Pet Retail Brands" in trade reports of the 2025-12 separation): owns Pet Supplies Plus, Wag N' Wash and Buddy's Home Furnishings; former first-lien lenders of Franchise Group (PT3).
- **Franchise Group, Inc.**: former parent of Pet Supplies Plus; emerged from Chapter 11 on 2025-06-06 (PT3).
- **Independent Pet Partners Holdings, LLC (IPP)**: rollup of regional chains (Chuck & Don's, Kriser's, Natural Pawz, Loyal Companion and others) that kept their names. Owner: TPG Growth per trade press (not confirmed); filed Chapter 11 in February 2023 and sold its stores to lenders, Pet Supplies Plus, Pet Pros and NP Acquisition LLC (trade press).
- **Pet Retail Brands Ltd. (2016)**: Roark-era holding company for Pet Valu and Pet Supermarket (law-firm deal page in search; not cited). Owner then: Roark Capital affiliates. Roark now lists both as previous investments.
- **Houchens Industries, Inc.**: Kentucky ESOP conglomerate that owns Feeders Pet Supply and Chow Hound Pet Supplies (PT14).
- **Pet Stuff Franchising**: Bentley's Pet Stuff and Dee-O-Gee franchisor (trade press, 2021). Owner not found.
- **Strategic Franchising Systems, Inc.**: umbrella franchisor named for Pet Wants in a search snippet. Owner not found.

### Category share
**Ranked store chains (N = 26, composite by US location count):**
- **PE-owned (control, or no stated stake): 5 / 26 = 19.2%**
  - PetSmart (BC Partners; private).
  - Petco and Unleashed by Petco (CVC and CPP Investments via Scooby Aggregator, 64.4% of voting power; Nasdaq-listed "controlled company").
  - Woof Gang Bakery & Grooming (Garnett Station Partners and Great Hill Partners; no stake stated).
  - Pet Food Express (Rainier Partners; no stake stated).
- **PE minority stake: 0.** PE-owned plus minority = **5 / 26 = 19.2%.**
- **Public company: 1 / 26 = 3.8%**: Petsense (Tractor Supply). Its 5%+ holders are Vanguard and BlackRock; no PE holder.
- **Other: 7 / 26 = 26.9%**
  - lender-owned: 2 (Pet Supplies Plus and Wag N' Wash, via Fusion Parent)
  - family: 2 (Concord Pet Foods & Supplies; Kahoots)
  - employee-owned: 1 (Feeders Pet Supply, via Houchens' ESOP) plus 1 partial (Mud Bay: ESOP stake ">10%", rest not stated)
  - private, owner not stated: 1 (Hollywood Feed)
- **Not found: 13 / 26 = 50.0%**: Pet Supermarket, EarthWise Pet, Petland, Pet Wants, Chuck & Don's, Bentley's Pet Stuff, Pet's Barn, Healthy Spot, Choice Pet, Kriser's, Pet Pros, Premier Pet Supply, Pet Club. These rows hold 744 of 5,358 locations (13.9%).
- **Rows with owner kind settled:** 11 / 26 (42%): the 5 PE rows, Petsense, the 2 lender-owned rows, the 2 family rows and Feeders (ESOP). Mud Bay and Hollywood Feed are only partly settled.
- **Strict count:** unchanged at 5 / 26 pending the assembler's Form ADV check. The only public non-PE ranked row (Petsense) has no PE holder at 5%+.
- **By parent company:** 24 parents (Petco and Unleashed are one; Pet Supplies Plus and Wag N' Wash are one). PE-owned parents: 4 / 24 = 16.7% (BC Partners' PetSmart, Petco, Woof Gang, Pet Food Express).
- **By locations:** PE-owned rows hold 3,271 of 5,358 US locations (61.0%). The counts mix sources and dates (2022–2026), so this is indicative only. Woof Gang counts at 288 (ScrapeHero, 2025-02); the company's own "more than 450 … open or under development" would raise the share.
- **By sales:** not computed. PetSmart's sales are not public.
- **Upper bound if leads were confirmed:** adding Healthy Spot (Monogram Capital, directory lead) gives 6 / 26 (23.1%). If Pet Supermarket's unknown post-Roark owner is PE, 7 / 26 (26.9%).
- **Sources disagree:** none on owners. Two framing or date differences: Woof Gang (the company release states no stake; trade press calls Great Hill's investment "minority"), and Feeders (the Houchens page is dated 2024-10-10; trade press dates the deal April 2023).
- **Formerly PE among non-PE rows:** Feeders (PNC Riverarch, 2016 to the Houchens sale), Pet Supermarket (Roark, "Previous Investments"), Pet Supplies Plus (Sentinel to 2021, trade press only), and Chuck & Don's and Kriser's (IPP / TPG Growth to 2023, trade press only).

**Including added online-first rows (N = 30):** PE-owned 6 / 30 = 20.0% (adds Chewy). Public 4 / 30 (Petsense; PetMeds and PetCareRx via PetMed Express; Allivet via Tractor Supply). Other 7 / 30. Not found 13 / 30 (43.3%).

**Affiliate income:**
- **Brand-direct programs found:** Chewy (via Impact) and 1-800-PetMeds.
- **Network listings only:** PetSmart (Impact, FlexOffers) and Petco (Rakuten / Impact). Their own pages returned HTTP 500 and 403.
- **Blocked:** Allivet and PetCareRx.
- **None found:** every other row. Store-chain sites were checked during owner fetches, with one category-wide search.
- **Overlap with PE:** unlike eyewear, the category's largest affiliate program sits on a PE-controlled row (Chewy, BC Partners). PetSmart and Petco, both PE-owned, have network listings.

## Firms named
Every investment firm named as an owner or 5%+ holder, as the sources name it (for the assembler's Form ADV check):
- **BC Partners**: "BC Partners, Inc." (PetSmart 8-K 2015), "BC Partners Advisors LP" (Chewy 10-K), "BC Partners Advisers LP" (Chewy DEF 14A), "BC Partners Holdings Limited" (Chewy DEF 14A table)
- **Apollo**: "Apollo" (BC Partners PetSmart XI page; entity not named)
- **La Caisse de dépôt et placement du Québec**; **GIC Special Investments Pte Ltd**; **StepStone Group LP**; **Longview Asset Management, LLC** (PetSmart 2015 and Chewy consortium)
- **CVC Capital Partners** ("CVC Capital Partners VI Limited", "CVC Pet LP" in the Petco DEF 14A); **Canada Pension Plan Investment Board** (CPP Investments)
- **Garnett Station Partners**; **Great Hill Partners** (Woof Gang)
- **Rainier Partners** (Pet Food Express)
- **Roark Capital Group** (Pet Supermarket, previous investment)
- **PNC Riverarch** (former Feeders majority holder; the release says "PNC Riverarch")
- 5%+ holders of public rows: **The Vanguard Group**, **BlackRock, Inc.** (Tractor Supply); **Vanguard Capital Management**, **AQR Capital Management, LLC**, **BlackRock, Inc.** (Chewy Class A); **Nina Capital Holdings Inc.**, **SilverCape Investments Limited**, **Renaissance Technologies LLC** (PetMed Express)
- Leads only, from trade press or directories (not cited, not counted): TPG Growth (IPP), Sentinel Capital Partners (Pet Supplies Plus to 2021), Monogram Capital (Healthy Spot), Golub Capital and Penfund (Pet Supermarket), Fortress Investment Group (Hollywood Feed lender, 2026), Franchise Funding Group (Pet Wants, 2015).

## Worker log
- **Time:** start 2026-11-07T16:35:14Z, end about 2026-11-07T17:00Z: about 25 minutes wall-clock for 30 rows, including writing and the quote self-check.
- **Requests:**
  - WebSearch: 33.
  - WebFetch: 0. Every page was read with curl, so quotes come from raw page text, not a summarizer.
  - Direct HTTP (curl): 134 logged requests (41 of them robots.txt reads; 24 to ScrapeHero, of which 21 were per-brand location reports). 22 went to SEC (submissions JSON ×5, company tickers ×1, full-text search ×3, documents ×13), all HTTP 200 under the contact-free user agent at ≤2 req/s.
  - Status mix: 120 × 200, 6 × 403, 3 × 404, 1 × 500, 1 × 307 (PerimeterX), 3 × no response (petbusiness.com twice, concordpet.com).
  - Agent tokens: not metered by this worker.
- **What was fast:** public parents. Five 10-Ks and four DEF 14As settled Petco, Unleashed, Petsense, Chewy, PetMeds, PetCareRx and Allivet (7 rows) with mechanically checkable quotes. BC Partners' server-rendered portfolio pages settled PetSmart's current status in 2 requests. Rainier Partners' portfolio page settled Pet Food Express in 1 request (investment date and "Current" status on the tile). Roark's page HTML separates current from previous holdings by section class, which settled that Roark no longer holds Pet Supermarket.
- **What made brands slow:**
  1. **No usable ranking.** Pet Business's Top 25 is in a flipbook. ScrapeHero's and xMap's top-10s count pet-food stockists as stores. Building the composite took about 25 location-report requests and 3 searches.
  2. **Bot walls on company sites:** petsuppliesplus.com, hollywoodfeed.com, petsupermarket.com, petco.com, allivet.com and petcarerx.com (Cloudflare or PerimeterX, 403).
  3. **robots.txt disallowing ClaudeBot:** petland.com, earthwisepet.com and petsbarn.com. These are three sizable chains whose own sites were the likeliest owner source.
  4. **Ownership changes through bankruptcy:** Pet Supplies Plus (Franchise Group, 2024–25) and Chuck & Don's and Kriser's (IPP, 2023). Lenders end up owning the chain, and the releases do not name them.
  5. **Exits without a named buyer:** Roark lists Pet Supermarket as previous, and no buyer release was found.
- **Which kinds of brands had no primary source for the owner:**
  - private regional chains whose sites name founders or say "family" without an owner (Hollywood Feed, Bentley's, Choice Pet, Premier Pet Supply, Pet Club, Healthy Spot);
  - franchisors whose sites are robots-disallowed or name only a CEO (Petland, EarthWise Pet, Pet Wants);
  - chains that passed through a bankrupt PE rollup (Chuck & Don's, Kriser's, Pet Pros);
  - a PE exit with no buyer announcement (Pet Supermarket).
- **Notes for the assembler:**
  - **petland.com:** fetched once (about page) before its full robots.txt, which disallows ClaudeBot, had been read; nothing from it is used.
  - **Quotes from tables or tiles** (Petco and Chewy voting-power rows, TSCO and PetMed 5% rows, Rainier's "Investment Date: May 2022 Status: Current" tile) are page text with whitespace collapsed.
  - **BC Partners "Investment status" values** are field labels, not sentences.
  - **Kahoots' "Family-owned & Family-focused"** is a heading. It decodes from `&amp;` in the HTML.
  - **The Chewy affiliate page** is 1.4 MB but rendered on the server; the quoted sentence is in the HTML.
  - **No JavaScript-only pages are cited.**
  - **Self-check:** a script string-matched the cited quotes against the saved page text (whitespace collapsed, curly quotes and dashes normalized). All 55 extracted quotes plus 15 hand-picked ones (table cells, quotes with inner quote marks) were found; 5 deliberately altered quotes all failed.
  - **BDC leads:** Hollywood Feed's Fortress-led facility (trade, 2026), Pet Supermarket's 2015 Golub financing (trade), IPP (bankrupt 2023), and Fusion Parent / Pet Supplies Plus (securitization, 2025-12, trade).
