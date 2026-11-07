# Research: Category audit, dental chains

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (17:23–17:58 UTC) · Ownership facts come from primary sources only; trade press (Becker's Dental + DSO Review) supplies the candidate DSO ranking only.

**Question:** For the top ~30 US dental brands (consumer-facing chain names on dental offices), who owns each today, what share is PE-owned or PE-backed, and which have brand-direct affiliate programs? DSOs whose offices keep local practice names are listed separately as rollups.

**Short answer**

| | Dental chains (30 brand rows) |
|---|---|
| PE-owned plus PE minority stake, current status confirmed by a primary source | **15 / 30 (50.0%)**; 64.5% of offices in the 27 rows with a count |
| The same, adding 2 rows whose investment-firm owner is confirmed only for 2021 (Ideal Dental / Blackstone Tactical Opportunities; Dental365 / The Jordan Company) | 17 / 30 (56.7%) |
| Upper bound, also counting the 2 Affordable Care rows, whose equity passed to lenders in June 2026 | 19 / 30 (63.3%) |
| Strict count (public company with a 5%+ PE-flagged holder counts as minority) | **same as above: no public company is among the 30**. No dental brand found has a listed parent |
| Owner not found | **8** (Great Expressions, Gentle Dental, Dental Dreams, Absolute Dental, Nuvia, Familia Dental, Tend, Risas). 3 more name a founder or "doctor-owned" practices but no owner of the support company (Comfort Dental, Coast Dental, Dental Depot) |
| Brand-direct affiliate programs | **none found**. Aspen Dental appears on affiliate-network listings (FlexOffers, LinkClicky/Impact), which are leads, not brand-direct pages |
| Rollups (not brands), listed separately | 7; **3 / 7 PE-owned** (Heartland, MB2, Specialized Dental Partners); 1 lender-owned since 2026 (Dental Care Alliance) |

- **Category character:** dental brands sit on top of a DSO structure. The brand-named office is legally a dentist-owned practice ("independently owned and operated by licensed dentists"); the PE owner holds the support company (DSO/MSO) that runs everything else. Every "PE-owned" row here is PE-owned at the DSO level.
- **Concentration:** 10 of the 15 PE rows are banners of just two DSOs: Sonrava Health (New Mountain Capital: Western Dental, DentalWorks, Brident, Perfect Teeth, Vital Smiles) and Smile Brands (Gryphon Investors: Midwest Dental, Monarch, Bright Now!, Castle, Mint Dentistry). TAG (Ares, Leonard Green, American Securities) adds Aspen Dental and ClearChoice.
- **2026 credit events:** two of the ten largest DSOs went through lender-led restructurings in 2026. Affordable Care (Affordable Dentures & Implants, DDS Dentures) and Dental Care Alliance both show lender-held common stock acquired in June 2026 in FS KKR Capital Corp's Q3 10-Q. The PE sponsor (Harvest Partners) no longer lists Affordable Care.
- **Ranking caveat:** no free top-30 ranking of dental brands exists, and the trade-press DSO rankings (Becker's, DrBicuspid) return 403 to automated fetches. The list below is a composite ordered by each brand's own office count (see Ranking), and it is not exhaustive below about 50 offices.

## How this was sourced (read first)

- **Ranking:** Becker's Dental + DSO Review, "Where the largest DSOs stand halfway through 2026", read only through search-engine summaries because the page returns 403 to curl and WebFetch. It supplied the candidate set of large DSOs; it is trade press and was used for nothing else. Brand rows were then ordered by each brand's own office count from its site or its owner's page (see Ranking).
- **Ownership facts:** sponsor portfolio pages (Leonard Green, New Mountain, Gryphon, Linden, Brentwood, Berkshire, Roark, H.I.G., Halifax, Quad-C), company press releases and company sites, two SEC filings (FS KKR Capital Corp 10-Q for Q3 2026; Bain Capital Specialty Finance 10-Q for Q2 2026), and law-firm deal announcements where no company release was reachable (Kirkland for Dental365 and Jefferson; Troutman/Locke Lord for DECA; Milbank and Kirkland for DCA). Law-firm sources are flagged in their rows. One company release was read as a wire reprint (Smile Doctors 2026, FinancialContent reprint of GlobeNewswire), and one as a partner's release (DECA/Ideal Dental on nhl.com, by Dallas Stars Communications).
- **Leads only, never cited:** Becker's, DrBicuspid, Dental Economics, Dentaltown, Group Dentistry Now, LevinPro, Bloomberg (Affordable Care restructuring), PitchBook, Mergr, PrivSource, privateequityinfo, CB Insights, ZoomInfo, Built In, GoTu, Simplify, FlexOffers and LinkClicky results that came up in searches. None was opened except where noted as a failed fetch.
- **Never fetched:** WhoIsMyDentist, Private Equity Vet, Reddit and the competitor sites (Buy'r, Worse on Purpose, Grass, ShopFair, Ethos). PESP (pestakeholder.org) results appeared in searches and were not opened.
- **Robots and access** (details in the worker log):
  - greatexpressions.com disallows ClaudeBot, anthropic-ai and Claude-Web. One page (about-us) was fetched in the same command as robots.txt, before the file was read. It is not cited, and the site was not used after that.
  - harvestpartners.com sets `Crawl-delay: 10`. Its portfolio page was fetched 1.5 s after robots.txt, before the delay was noticed. That was the only request to the site.
  - Every other site's crawl-delay was honored (leonardgreen.com, hig.com, coastdental.com, brentwood.com, midwest-dental.com and risasdental.com 10 s; dental365.com and troutman.com 5 s).
- **Quote self-check:** all 83 quotes and fields taken from curl'd pages were string-matched against the downloaded text (HTML stripped, whitespace collapsed, curly quotes and dashes normalized). 83 of 83 were found. 6 of them are raw-HTML fields (portfolio-tile status classes and URL paths), marked "HTML field" below. Negative control: 3 deliberately altered quotes all failed. Not mechanically checked: the one WebFetch-only quote (Mortenson, DN37).
- **Owner kinds are research notes, not engine classifications** (ADR 0001 governs the product). "PE-owned" means control, or a PE owner with no stated stake. Counts are by brand row.

## Dental chains

**Ranking (candidate set):** Becker's Dental + DSO Review, "Where the largest DSOs stand halfway through 2026", https://www.beckersdental.com/dso-dpms/where-the-largest-dsos-stand-halfway-through-2026/. It ranks DSOs by supported practices/offices as of June 2026. The publication date was not obtained, because the page returns 403 to curl and WebFetch, so the list was read only through search-engine summaries:
1. Heartland Dental (more than 1,900)
2. The Aspen Group (more than 1,300)
3. PDS Health (about 1,000)
4. MB2 Dental (more than 800)
5. Smile Brands (more than 600)
6. Sonrava Health (nearly 600)
7. Smile Doctors (more than 550)
8. Affordable Care (about 425)
9. Dental Care Alliance (about 400)
10. Specialized Dental Partners (more than 275)

Trade press, used for the candidate set only.

**Why not a trade-press brand ranking:** none exists for free. Becker's and DrBicuspid publish only top-10 DSO lists (companies, not brands), and both block automated fetches (Becker's: "Please enable JS"; DrBicuspid: Cloudflare challenge, even on robots.txt). Group Dentistry Now publishes no ranking. Orbital's "US dental groups and DSOs, mapped" returned 403.

**How the 30 brand rows were built (composite, by office count):**
- **Brand DSOs:** each top-10 DSO whose offices carry one consumer-facing name became one row per banner. That is TAG (Aspen Dental, ClearChoice), Sonrava (Western Dental, DentalWorks, Brident, Perfect Teeth, Vital Smiles; Western Dental Kids is folded into Western Dental), Smile Brands (Midwest Dental, Monarch, Bright Now!, Castle, Mint Dentistry), Smile Doctors, and Affordable Care (Affordable Dentures & Implants, DDS Dentures + Implant Solutions).
- **Other branded chains:** added from searches (Great Expressions, which was No. 10 in Becker's mid-2025 list; Ideal Dental; Gentle Dental; Comfort Dental; Coast Dental; and others).
- **Office counts:** each row is placed by the count its own site, release or owner's page states (cited in Evidence). Where only trade press or a directory gave a count, the row is marked "trade" or "directory". Counts mix dates (2016–2026), and several are "more than" floors.
- **Rows 28–30** have no count found and are unordered.
- **Rollups:** DSOs whose practices keep local names went to "Rollups and groups that are not brands".
- **Not exhaustive:** checked but not placed for lack of a count or owner: Lovett Dental (Houston), 1st Family Dental, Bright Direction Dental, Gentle Dental of New England (a different group from InterDent's Gentle Dental, at gentledental.com), Pearl Street Dental Partners, and banners of Benevis.

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Aspen Dental (nearly 1,100 offices) | The Aspen Group (TAG); Leonard Green lists TAG as "Status: Current" | PE-owned (via TAG); stakes not stated | Ares Management, Leonard Green & Partners, American Securities | by 2015 (American Securities recap 2015-03-23, Ares and LGP already holders; Ares/LGP increase 2017-06-13) | — | DSO: brand-named practices "independently owned and operated by licensed dentists" | network listings only (FlexOffers, LinkClicky/Impact), unverified | DN1 |
| 2 | Smile Doctors (591, orthodontics) | Smile Doctors LLC, "With the long-term and continued backing of THL Partners and Linden Capital Partners" | PE-owned (THL and Linden "in an equal partnership"; orthodontists keep "a significant ownership stake"; no controlling stake stated) | Thomas H. Lee Partners, Linden Capital Partners | Linden 2017; THL 2022-01-05 | — | ortho support organization; affiliated orthodontists via joint-venture and de novo models | none found | DN2 |
| 3 | Affordable Dentures & Implants (about 425, trade; 340 on the former sponsor's page) | Affordable Care; lenders hold its equity after a June 2026 restructuring (FS KKR Capital Corp holds Class A and B common stock as an "affiliated person", 5–25%) | Owner type not confirmed: lender-owned after a debt-for-equity exchange (trade press names Blackstone and KKR credit funds as lead lenders) | none current confirmed (former: Berkshire Partners, now "former" on its page; Harvest Partners 2021 per trade, no longer on its page) | 2026-06-29 (FSK's acquisition date for the common stock) | — | DSO: each practice "individually owned and operated by a licensed dentist" | none found | DN3 |
| 4 | Western Dental & Orthodontics (more than 350; includes Western Dental Kids) | Sonrava Health (f.k.a. Western Dental); New Mountain Capital portfolio "Status Current" | PE-owned (via Sonrava) | New Mountain Capital | 2012 ("Investment Date November 2012") | — | DSO with affiliated offices | none found | DN4 |
| 5 | Great Expressions Dental Centers (269 in 2016, via search; site not used) | not found. Roark lists it under "Previous Investments" | not found (formerly PE: Audax, OMERS PE, Roark) | none current found | — | — | DSO ("branded dental practice network") | none found | DN5 |
| 6 | Gentle Dental (InterDent; about 175 practices, trade) | not found. H.I.G. Capital lists InterDent as "Status Realized" | not found (formerly PE: H.I.G. 2012) | none current found | — | — | DSO | none found | DN6 |
| 7 | Ideal Dental (more than 150) | DECA Dental Group ("a flagship brand of DECA Dental"); strategic investment from "funds managed by Blackstone Tactical Opportunities" (2021) | Investment-firm owner, current status not reconfirmed (stake not stated) | Blackstone Tactical Opportunities | 2021-08 | — | DSO; JV program lets dentists "set up, own, operate" practices | none found | DN7 |
| 8 | Comfort Dental (150+) | not stated; franchise founded by Dr. Rick A. Kushner | founder-led franchisor, owner not stated; practices "Dentist-owned" (no PE evidence found in sources checked) | none found | — | — | franchise; dentist-owned independent practices | none found | DN8 |
| 9 | Midwest Dental (141 offices listed on its site; worker count) | Smile Brands (listed among its brands) | PE-owned (via Smile Brands) | Gryphon Investors | Gryphon in Smile Brands 2016; brand's own date not found | — | DSO affiliates | none found | DN9 |
| 10 | DentalWorks (more than 110, including "DentalWorks Affiliated Practices") | Sonrava Health | PE-owned (via Sonrava) | New Mountain Capital | not found for the brand (Sonrava: 2012) | — | DSO; branded and affiliated practices | none found | DN10 |
| 11 | Monarch Dental (more than 100) | Smile Brands | PE-owned (via Smile Brands) | Gryphon Investors | 2016 (Gryphon) | — | DSO affiliates | none found | DN11 |
| 12 | Coast Dental (more than 100) | not stated. Support company Coast Dental Services, LLC; practices are P.A./P.C. entities of Adam Diasti, DDS | founder-led, owner not stated (no PE evidence found in sources checked) | none found | — | — | DSO; dentist-owned professional entities | none found | DN12 |
| 13 | ClearChoice Dental Implant Centers (about 100, trade) | The Aspen Group (TAG) | PE-owned (via TAG) | Ares Management, Leonard Green & Partners, American Securities | 2020 (trade; not confirmed) | — | each center "owned and operated by a licensed and experienced dentist" | none found | DN13 |
| 14 | Bright Now! Dental (more than 90) | Smile Brands | PE-owned (via Smile Brands) | Gryphon Investors | 2016 (Gryphon) | — | DSO affiliates | none found | DN14 |
| 15 | Sage Dental (90+, trade) | Sage Dental Management; Linden lists it under current investments | PE-owned (stake not stated) | Linden Capital Partners | not found | — | DSO | none found | DN15 |
| 16 | Brident Dental & Orthodontics (more than 80) | Sonrava Health (a "supported affiliate" of Western Dental) | PE-owned (via Sonrava) | New Mountain Capital | not found | — | DSO | none found | DN16 |
| 17 | Dental365 (about 70 in 2021, trade; current count not found) | The Jordan Company, through an affiliate of The Resolute Fund V, L.P. (2021) | Investment-firm owner, current status not reconfirmed | The Jordan Company | 2021 (close expected August 2021) | — | not found | none found | DN17 |
| 18 | Castle Dental (more than 60) | Smile Brands | PE-owned (via Smile Brands) | Gryphon Investors | 2016 (Gryphon) | — | DSO affiliates | none found | DN18 |
| 19 | Jefferson Dental & Orthodontics (53 in 2017, via search) | Brentwood Associates (tile marked current investment) | PE-owned (stake not stated) | Brentwood Associates (bought from Black Canyon Capital) | 2017-04 | — | DSO, "affiliated clinics" | none found | DN19 |
| 20 | Dental Dreams (51, directory) | not found | not found | not found | — | — | not found | none found | DN20 |
| 21 | Absolute Dental (50+) | not found (Absolute Dental Group, LLC) | not found | not found | — | — | DSO ("branded Dental Service Organization") | none found | DN21 |
| 22 | Dental Depot (about 50: 25 in Oklahoma and "just as many" elsewhere) | not stated; "Every Dental Depot is doctor-owned" | doctor-owned per its site (no PE evidence found in sources checked) | none found | — | — | doctor-owned practices | none found | DN22 |
| 23 | Nuvia Dental Implant Center (40+ markets, via search) | not found | not found | not found | — | — | not found (site 403) | none found | DN23 |
| 24 | Familia Dental (35) | not found. Halifax lists it as "former" | not found (formerly PE: Halifax 2016) | none current found | — | — | DSO | none found | DN24 |
| 25 | Tend (33 studios) | not found | not found (venture investors named only in secondary sources) | not found | — | — | not stated | none found | DN25 |
| 26 | Perfect Teeth (30+) | Sonrava Health | PE-owned (via Sonrava) | New Mountain Capital | not found | — | DSO | none found | DN26 |
| 27 | Vital Smiles (7 communities, pediatric) | Sonrava Health | PE-owned (via Sonrava) | New Mountain Capital | not found | — | DSO | none found | DN27 |
| 28 | Mint Dentistry (count not found) | Smile Brands (listed among its brands) | PE-owned (via Smile Brands) | Gryphon Investors | not found | — | DSO affiliates | none found | DN28 |
| 29 | DDS Dentures + Implant Solutions (count not found) | Affordable Care | as row 3: lender-owned after 2026 restructuring | as row 3 | joined Affordable Care 2019; lenders 2026-06-29 | — | DSO | none found | DN29 |
| 30 | Risas Dental and Braces (count not found) | not found | not found | not found | — | — | not found | none found | DN30 |

### Evidence
- **DN1 Aspen Dental**
  - Owner (TAG, current): "TAG offers a full range of essential business support services to consumer healthcare brands under the Aspen Dental, Chapter Aesthetic Studio, ClearChoice Dental Implant Centers and WellNow Urgent Care trade names." and the tile field "Deal Type: Buyout Status: Current" — [Leonard Green & Partners, Portfolio page, accessed 2026-11-07](https://www.leonardgreen.com/portfolio/)
  - Owner (sponsors): "Ares Management, L.P. (NYSE:ARES) and Leonard Green & Partners, L.P. today announced that private equity funds managed by each firm have entered into a definitive agreement to increase their equity ownership in Aspen Dental Management Inc. (ADMI)." and "The transaction is in partnership with ADMI’s leadership team and funds affiliated with American Securities, LLC." — [American Securities, press release, 06.13.17](https://www.american-securities.com/news/press-release/ares-management-leonard-green-increase-ownership-in-aspen-dental-management-inc/)
  - Since: "American Securities LLC, Ares Management, L.P., and Leonard Green & Partners, L.P. today announced that an affiliate of American Securities has entered into a definitive agreement to recapitalize Aspen Dental Management Inc." — [Leonard Green & Partners, news, March 23, 2015](https://leonardgreen.com/american-securities-leads-recapitalization-of-aspen-dental/). The same release says the recap was "in partnership with the management team and funds affiliated with Ares and Leonard Green", so they were holders before 2015. The first PE entry date was not checked.
  - Brand to TAG, and count: "Aspen Dental, part of The Aspen Group (TAG), is committed to breaking down barriers to oral healthcare and helping patients put themselves first, starting with a healthy mouth." and "With nearly 1,100 Aspen Dental-branded offices across the United States" — [TAG mediaroom, Missoula opening, 2026-10-15](https://aspendental.mediaroom.com/2026-10-15-Aspen-Dental-Opens-in-Missoula-with-Same-Day-Emergency-Visits,-Giving-Patients-with-Dental-Pain-an-Option-Outside-the-ER)
  - Model: "Aspen Dental-branded dental practices are independently owned and operated by licensed dentists." — [TAG mediaroom, 2025-08-25](https://aspendental.mediaroom.com/2025-08-25-Aspen-Dental-and-ClearChoice-Anchor-Strong-Growth,-Innovation-Across-The-Aspen-Groups-Multi-Brand-Healthcare-Portfolio). The same release's boilerplate: "TAG supports independent healthcare practices operating more than 1,400 locations in 46 states through five consumer healthcare brands"
  - Affiliate: network listings only, not brand-direct: FlexOffers (https://www.flexoffers.com/affiliate-programs/aspen-dental-affiliate-program) and LinkClicky (https://linkclicky.com/affiliate-program/aspen-dental/, which says the program runs on Impact). The two disagree on payout. Neither was opened.
  - BDC names: "The Aspen Group", "Aspen Dental Management, Inc.", "ADMI Corp." (not checked)
  - Notes: no stake split from a primary source. The 80/20 split in search results comes from an advocacy group (not cited).
- **DN2 Smile Doctors**
  - Owner: "THL is investing alongside existing financial sponsor Linden Capital Partners (“Linden”) in an equal partnership." and "Affiliated orthodontists will retain a significant ownership stake in the organization." — [Smile Doctors, "Smile Doctors Receives Strategic Investment from Thomas H. Lee Partners", Jan. 5, 2022](https://smiledoctors.com/smile-files/smile-doctors-investment-thl-partners/)
  - Current: "With the long-term and continued backing of THL Partners and Linden Capital Partners, Smile Doctors continues to welcome new affiliation conversations through its joint venture and de novo models." — [Smile Doctors release, GlobeNewswire, July 14, 2026 (FinancialContent reprint)](https://www.financialcontent.com/article/gnwcq-2026-7-14-smile-doctors-outpaces-first-half-growth-plan-nears-600-locations-nationwide)
  - Current (sponsor): HTML field, the URL path https://www.linden.com/portfolio/investments/current/smile-doctors/ on [Linden Capital Partners, Portfolio page](https://www.linden.com/portfolio/)
  - Since: "since our initial investment in 2017" (Linden's Tony Davis, in the 2022 release above)
  - Count: "The company now supports 591 locations in 36 states and expects to exceed 600 locations before year-end." (2026 release above)
  - Affiliate: none found
  - BDC names: "Smile Doctors LLC" (not checked)
- **DN3 Affordable Dentures & Implants**
  - Brand to company: "Affordable Care is the DSO for two top dental brands: Affordable Dentures & Implants and DDS Dentures + Implant Solutions." — [Berkshire Partners, Affordable Care page, accessed 2026-11-07](https://berkshirepartners.com/portfolio-companies/affordable-care/)
  - Former sponsor: "Year Invested 2015 Investment Type Management Recapitalization" (same page). The tile on [Berkshire's portfolio page](https://berkshirepartners.com/portfolio/) has the HTML class `investments-item former management-recapitalization healthcare`, so Berkshire lists it as former.
  - Lender equity (2026): FS KKR Capital Corp's schedule of investments lists "Affordable Care Inc, Class A Common Stock 69,504 33.2 31.6 6/29/2026" (shares, cost $m, fair value $m, acquisition date). Footnote (ac) applies: "As of September 30, 2026, the Company held investments in portfolio companies of which it may be deemed to be an “affiliated person” but is not deemed to “control”." The (ac) definition sets affiliated person at 5% or more of voting securities and control at more than 25%. FSK also lists Class B common stock, and a preferred stock position whose fair value went to zero in 2026 — [FS KKR Capital Corp, Form 10-Q for Q3 2026, filed 2026-11-05](https://www.sec.gov/Archives/edgar/data/1422183/000162828026070499/fsk-20260930.htm)
  - Model: "Each practice is individually owned and operated by a licensed dentist" (Berkshire page above)
  - Count: "Affordable Care was founded in 1975 and today is America’s largest dental support organization focused on tooth replacement services with 340 affiliated practices in nearly 40 states." (Berkshire page, undated). Becker's (trade) says about 425.
  - Affiliate: none found
  - BDC names: "Affordable Care Inc" (FSK: first-lien, subordinated, Class A/B common)
  - Notes: trade press (Bloomberg, May 2026; Becker's; Private Equity Wire; not cited) reports that lenders led by Blackstone and KKR took 100% of the equity and that existing equity was wiped out. Harvest Partners, the 2021 sponsor per trade, no longer lists Affordable Care on [its portfolio page](https://www.harvestpartners.com/portfolio/) (checked 2026-11-07; an absence, not a statement). The current controlling holder was not found. affordablecare.com was not fetched.
- **DN4 Western Dental & Orthodontics**
  - Owner: "Sonrava Health (f.k.a Western Dental) is one of the most experienced dental service organizations (DSOs) in the U.S., with a large-scale footprint of over 580 offices across 20 states." and fields "Status Current", "Investment Date November 2012" — [New Mountain Capital, Sonrava Health portfolio page, accessed 2026-11-07](https://www.newmountaincapital.com/portfolio/sonrava-health/)
  - Since: "New Mountain reinstated its dialogue with Sonrava Health in early 2012 and acquired the company later that year." (same page)
  - Count: "Operating the most integrated system of oral healthcare in the nation, Western Dental serves 3 million patient visits annually across more than 350 offices in California, Arizona, and Nevada." — [Sonrava Health, Our Brands page, accessed 2026-11-07](https://www.sonrava.com/brands)
  - Sonrava total: "Sonrava Health provides high quality care in over 400 affiliated offices in 20 states coast to coast from California to Florida, and border to border from Michigan to Texas." — [Sonrava Health, home page](https://www.sonrava.com/). This disagrees with New Mountain's "over 580 offices" (counts only).
  - Affiliate: none found
  - BDC names: "Sonrava Health", "Western Dental Services, Inc." (not checked)
  - Notes: Sonrava's home page lists "Western Dental & Orthodontics Kids" as a separate brand. It is folded into this row because it carries the same name.
- **DN5 Great Expressions Dental Centers**
  - Owner: not found
  - Former owner: "Great Expressions is a leading branded dental practice network that provides comprehensive affordable dental services distinguished by convenience, value, and a broad acceptance of insurance plans." This tile sits inside the HTML section `portfolio-section portfolio-section--previous` ("Previous Investments") — [Roark Capital, Portfolio page, accessed 2026-11-07](https://www.roarkcapital.com/portfolio)
  - Lender: "Great Expressions Dental Center PC (4) First Lien Senior Secured Loan" (maturity 9/30/2026, part PIK) — [Bain Capital Specialty Finance, Form 10-Q for Q2 2026, filed 2026-08-10](https://www.sec.gov/Archives/edgar/data/1655050/000119312526342491/bcsf-20260630.htm)
  - Count: 269 affiliated practice locations in 2016, per the OMERS/Roark release on GlobeNewswire as seen through search (not fetched).
  - Affiliate: none found
  - BDC names: "Great Expressions Dental Center PC" (BCSF)
  - Notes: slow, 5 requests and 2 searches. greatexpressions.com disallows ClaudeBot and anthropic-ai in robots.txt. One page was fetched before the file was read, and nothing from it is used. No 2024–26 ownership change was found.
- **DN6 Gentle Dental (InterDent)**
  - Owner: not found
  - Former owner: "Invested 2012 Status Realized Fund Private Equity - US" and "InterDent, based in Inglewood, California, is a leading dental practice support organization in the United States." — [H.I.G. Capital, InterDent portfolio page, accessed 2026-11-07](https://hig.com/portfolio/interdent/)
  - Count: about 175 practices (InterDent job posting seen through search; not cited)
  - Affiliate: none found
  - BDC names: "InterDent, Inc.", "InterDent Service Corporation" (not checked)
  - Notes: gentledental.com is "Gentle Dental of New England", a different group that was not researched. InterDent's brand site was not found.
- **DN7 Ideal Dental**
  - Brand to company: "Ideal Dental, a flagship brand of DECA Dental, was founded in Dallas, and has been delivering high quality, affordable dental care to patients since 2008." — [Dallas Stars Communications, "Ideal Dental becomes official dentist partner of the Dallas Stars", October 02, 2024 (DECA announcement)](https://www.nhl.com/stars/news/ideal-dental-becomes-official-dentist-partner-of-the-dallas-stars-100224)
  - Count: "making it a trusted choice for families and individuals across nine states with over 150 locations." (same)
  - Owner: "A Locke Lord team represented DECA Dental CEO and founder Dr. Sulman Ahmed in a strategic investment in DECA Dental from funds managed by Blackstone Tactical Opportunities." — [Troutman Pepper Locke, achievement note, August 30, 2021](https://www.troutman.com/experience/locke-lord-represents-deca-dental-ceo-and-founder-in-strategic-investment-from-blackstone-tactical-opportunities/) (law-firm release; Blackstone's own release returned 403)
  - Since: 2021-08 (same)
  - Affiliate: none found
  - BDC names: "DECA Dental Group", "DECA Dental Holdings" (not checked)
  - Notes: no stake is stated, and no source after 2021 confirms that Blackstone still holds it. decadental.com does not name an investor. idealdental.com belongs to an unrelated dental lab (TLS certificate mismatch); the consumer site is myidealdental.com (not fetched).
- **DN8 Comfort Dental**
  - Owner: not stated. "Founded by experienced dentist Dr. Rick A. Kushner, Comfort Dental is the largest and most successful dental franchise in the world." — [Comfort Dental, About Us, accessed 2026-11-07](https://comfortdental.com/about-us/)
  - Model: "Dentist-owned independent local practices" (same)
  - Count: "150+ locations" (same)
  - Affiliate: none found
- **DN9 Midwest Dental**
  - Owner: [Smile Brands, Locations page](https://www.smilebrands.com/locations/) lists "Midwest Dental" and "Mint Dentistry" (adjacent in the list: "Midwest Dental Mint Dentistry") among "Smile Brands Regional Brands and Groups". It also says "Our growing portfolio of brands and practice models range from large regional brands to uniquely branded local practices." and "Smile Brands supports over 600 offices across 29 states."
  - Smile Brands' owner: see DN14 (Gryphon)
  - Count: 141 distinct office phone numbers on the office list of the [Midwest Dental home page](https://www.midwest-dental.com/), counted by the worker. The site states no total.
  - Affiliate: none found
  - Notes: the brand site does not name Smile Brands. The link rests on Smile Brands' own list.
- **DN10 DentalWorks**
  - Owner and count: "Today, there are more than 110 DentalWorks and DentalWorks Affiliated Practices across 13 states" — [Sonrava Health, Our Brands page](https://www.sonrava.com/brands). Sonrava's owner: DN4.
  - Affiliate: none found
- **DN11 Monarch Dental**
  - Owner: "Leading provider of support services to over 600 dental offices nationwide, including Bright Now!® Dental, Monarch Dental®, and Castle Dental®, offering comprehensive business support services through exclusive long-term agreements with affiliate dental groups." — [Gryphon Investors, Smile Brands Inc. page](https://www.gryphon-inv.com/companies/smile-brands-inc/)
  - Count: "With more than 100 affiliates throughout Arkansas, Indiana, New Mexico, Ohio, Texas, and Utah, there is a Monarch Dental office near you." — [Monarch Dental, home page, accessed 2026-11-07](https://www.monarchdental.com/)
  - Affiliate: none found
- **DN12 Coast Dental**
  - Owner: not stated. "The dentists and hygienists are employees or independent contractors of Coast Florida, P.A., (Adam Diasti, DDS, DN12490), Coast Dental of Georgia, P.C., (Adam Diasti, DDS, DN11634) or Coast Dental of Texas, PC (Adam Diasti, DDS, Lic. 32327)." — [Coast Dental, home page footer, accessed 2026-11-07](https://www.coastdental.com/)
  - Count: "Coast Dental, along with its professional affiliations, have more than 100 locations in Florida, Georgia and Texas." (same)
  - Affiliate: none found
  - Notes: directories say it is privately held by the founding Diasti brothers (not cited). A January 2026 vendor release (Planet DDS on Business Wire, seen through search) says 88 locations. Coast Dental Services was SEC-registered until a 2003 going-private transaction (not checked).
- **DN13 ClearChoice Dental Implant Centers**
  - Owner: "ClearChoice Dental Implant Centers, part of The Aspen Group (TAG), have helped restore hope and confidence in more than 250,000 patients across the United States" — [TAG mediaroom, Rochester opening, 2026-11-04](https://aspendental.mediaroom.com/2026-11-04-CLEARCHOICE-DENTAL-IMPLANT-CENTER-OPENS-IN-ROCHESTER,-BRINGING-FULL-ARCH-DENTAL-IMPLANT-CARE-TO-MONROE-COUNTY). TAG's owners: DN1.
  - Model: "each ClearChoice Dental Implant Center is owned and operated by a licensed and experienced dentist" (same)
  - Count: no primary count found. "Additionally, the brand added three new centers in the first half of 2025, including its first Hawaii location." ([TAG mediaroom, 2025-08-25](https://aspendental.mediaroom.com/2025-08-25-Aspen-Dental-and-ClearChoice-Anchor-Strong-Growth,-Innovation-Across-The-Aspen-Groups-Multi-Brand-Healthcare-Portfolio)). Becker's (trade) says it reached 100 practices.
  - Since: 2020. Aspen Dental Management announced the purchase of ClearChoice from Sun Capital Partners in November 2020 (Business Wire, seen through search; not fetched).
  - Affiliate: none found
- **DN14 Bright Now! Dental**
  - Owner: the Gryphon sentence in DN11, plus fields "Year Invested 2016" — [Gryphon Investors, Smile Brands Inc. page](https://www.gryphon-inv.com/companies/smile-brands-inc/). The Smile Brands tile on [Gryphon's portfolio page](https://www.gryphon-inv.com/portfolio/) carries the HTML field `href="https://www.gryphon-inv.com/companies/smile-brands-inc/" data-status="current"`.
  - Smile Brands model: "Smile Brands provides comprehensive business support services through exclusive long-term agreements with affiliate dental groups." and "75+ Affiliated Brands Nationwide" — [Smile Brands, About](https://www.smilebrands.com/about/)
  - Count: "Bright Now! Dental has more than 90 affiliated locations throughout Arizona, California, Colorado, Florida, Indiana, Maryland, Ohio, Oregon, Pennsylvania, Virginia, and Washington" — [Bright Now! Dental, home page, accessed 2026-11-07](https://www.brightnow.com/)
  - Affiliate: none found
  - BDC names: "Smile Brands Inc.", "Smile Brands Group Inc." (not checked)
- **DN15 Sage Dental**
  - Owner: HTML field, the URL path https://www.linden.com/portfolio/investments/current/sage-dental-management/ on [Linden Capital Partners, Portfolio page](https://www.linden.com/portfolio/), where "Sage Dental" is listed with the description "Dental services organization"
  - Count: 90+ practices (Becker's, trade). mysagedental.com returned 403, and sagedental.com is an unrelated Canadian practice.
  - Since: not found
  - Affiliate: none found
  - BDC names: "Sage Dental Management, LLC" (not checked)
- **DN16 Brident Dental & Orthodontics**
  - Owner and count: "Western Dental (with its supported affiliates Brident Dental & Orthodontics and Vital Smiles)" and "Brident Dental & Orthodontics, with more than 80 offices throughout Texas" — [Sonrava Health, Our Brands page](https://www.sonrava.com/brands)
  - Affiliate: none found
- **DN17 Dental365**
  - Owner: "Kirkland advised The Jordan Company, L.P., a middle-market private equity firm, on its acquisition through an affiliate of The Resolute Fund V, L.P. (“Resolute V”) of Dental365, a full-service dental practice, from the founding shareholders and current investor Regal Healthcare Capital Partners, L.P.." — [Kirkland & Ellis, press release, 26 July 2021](https://www.kirkland.com/news/press-release/2021/07/kirkland-represents-tjc-on-dental365) (law-firm release)
  - Founder: "Resolute V is completing the acquisition in partnership with Dental365’s founder and CEO, Dr. Scott Asnis, who will continue to lead the company." (same)
  - Count: about 70 in 2021 (trade). dental365.com returned 404 to the bot, and jordanco.com serves only a script redirect.
  - Affiliate: none found
  - BDC names: "Dental365 LLC" (FSK Q3 2026 10-Q, first-lien loans)
  - Notes: no source after 2021 confirms The Jordan Company still owns it.
- **DN18 Castle Dental**
  - Owner: the Gryphon sentence in DN11
  - Count: "With more than 60 affiliated locations across Tennessee and Texas, there is a Castle Dental location near you." — [Castle Dental, home page, accessed 2026-11-07](https://www.castledental.com/)
  - Affiliate: none found
- **DN19 Jefferson Dental & Orthodontics**
  - Owner (current): the tile linking to https://www.brentwood.com/our-portfolio/jefferson-dental-care/ carries the HTML class `portfolio-item stage-current-investment sector-health-wellness` — [Brentwood Associates, Our Portfolio](https://www.brentwood.com/our-portfolio/)
  - Description: "Headquartered in Dallas, TX, Jefferson provides best-in-class marketing and non-clinical support services to its affiliated clinics" — [Brentwood Associates, Jefferson Dental & Orthodontics page](https://www.brentwood.com/our-portfolio/jefferson-dental-care/)
  - Since: "Kirkland & Ellis LLP advised Brentwood Associates, a leading consumer-focused private equity investment firm, on its decision to acquire Jefferson Dental Care from Black Canyon Capital." — [Kirkland & Ellis, press release, 10 April 2017](https://www.kirkland.com/news/press-release/2017/04/kirkland-counsels-brentwood-associates-on-purchase) (law-firm release)
  - Count: 53 affiliated clinics in 2017 (Business Wire, seen through search). jeffersondental.com fails TLS for www and apex.
  - Affiliate: none found
  - BDC names: "JDC Healthcare Management, LLC", "Jefferson Dental Care" (not checked)
- **DN20 Dental Dreams**
  - Owner: not found (2 searches, home page fetched; the site names no owner)
  - Count: 51 offices (Built In directory, seen through search; not cited)
  - Affiliate: none found
- **DN21 Absolute Dental**
  - Owner: not found. "Absolute Dental is Nevada's largest branded Dental Service Organization (DSO) with 40 affiliated dental practices throughout northern and southern Nevada" — [Absolute Dental, PR Newswire, July 6, 2022](https://www.prnewswire.com/news-releases/absolute-dental-reaches-40-practice-milestone-with-completion-of-two-practice-acquisitions-in-southern-nevada-301581425.html)
  - Count: "50+ Locations & Growing" — [Absolute Dental, home page, accessed 2026-11-07](https://www.absolutedental.com/)
  - Affiliate: none found
  - Notes: an aggregator says "BPOC" acquired it in 2016 (lead only, not confirmed).
- **DN22 Dental Depot**
  - Owner: not stated. "Every Dental Depot is doctor-owned, which means our providers have the freedom and flexibility to provide you and your family with the care you truly need" — [Dental Depot, home page, accessed 2026-11-07](https://dentaldepot.net/)
  - Count: "we’re proud to have just as many locations throughout Texas, Arizona, Missouri, and Oklahoma, with 25 here in the Sooner State alone!" (same)
  - Affiliate: none found
- **DN23 Nuvia Dental Implant Center**
  - Owner: not found. nuviasmiles.com returned 403, including robots.txt. A careers listing (secondary) says the centers are locally owned by dentists with a business affiliation to "Nuvia MSO, LLC".
  - Count: "more than 40 markets" (April 2026 release, seen through search; not fetched)
  - Affiliate: none found
- **DN24 Familia Dental**
  - Owner: not found
  - Former owner: "Familia Dental Investment Date: April 2016" and "Familia operates 37 clinics across six states". The tile has the HTML class `... health-wellness former` — [The Halifax Group, Portfolio page, accessed 2026-11-07](https://www.thehalifaxgroup.com/portfolio/)
  - Count: "35 Locations in IL, IN, NM, TX, & WI" — [Familia Dental, home page](https://www.familiadental.com/). This disagrees with Halifax's 37 (counts only).
  - Affiliate: none found
- **DN25 Tend**
  - Owner: not found. Secondary sources name venture investors (GV and others), not cited.
  - Count: "New York City 16 Studios Washington DC Metro 8 Studios Boston 4 Studios Atlanta 3 Studios Westport 1 Studio Nashville 1 Studio" (33 in total) — [Tend, home page, accessed 2026-11-07](https://www.hellotend.com/)
  - Affiliate: none found
- **DN26 Perfect Teeth**
  - Owner and count: "Founded in 1995, Perfect Teeth is the perfect choice for families needing quality dental care throughout the 30+ locations in Colorado, New Mexico, and Arizona." — [Sonrava Health, Our Brands page](https://www.sonrava.com/brands). Sonrava's owner: DN4.
  - Affiliate: none found
- **DN27 Vital Smiles**
  - Owner and count: "Vital Smiles can be found in seven communities in the state of Alabama." — [Sonrava Health, Our Brands page](https://www.sonrava.com/brands)
  - Affiliate: none found
- **DN28 Mint Dentistry**
  - Owner: listed on the [Smile Brands, Locations page](https://www.smilebrands.com/locations/) (see DN9)
  - Count: not found (mintdentistry.com returned 403, including robots.txt)
  - Affiliate: none found
- **DN29 DDS Dentures + Implant Solutions**
  - Owner: the Berkshire sentence in DN3 ("Affordable Care is the DSO for two top dental brands: Affordable Dentures & Implants and DDS Dentures + Implant Solutions."). Berkshire's page links a "Related News March 1, 2019" item on Affordable Care and DDS.
  - Count: not found
  - Affiliate: none found
- **DN30 Risas Dental and Braces**
  - Owner: not found (1 search; the home page names no owner). An aggregator lists only a 2020 PPP loan.
  - Count: not found. The home page has no total, and its office links are rendered by script.
  - Affiliate: none found

### Rollups and groups that are not brands
These DSOs support practices that keep their own local names, so they are companies, not list entries (ticket "Brand and chain model"). The not-brand call is the worker's research note under that rule. No source sentence about practice naming was quoted, except Mortenson (mixed) and Smile Brands ("uniquely branded local practices").

| Rollup (count, source) | Owner (as source states) | Owner kind (research note) | Ev. |
|---|---|---|---|
| Heartland Dental (more than 1,900, Becker's) | KKR majority since 2018; Ontario Teachers' "will retain sizeable ownership" | PE-owned; current status not reconfirmed after 2018 | DN31 |
| PDS Health (about 1,000, Becker's) | not stated; founder and CEO Stephen E. Thorne IV (secondary) | not found (no primary owner statement; no PE evidence found) | DN32 |
| MB2 Dental (more than 800, Becker's) | Charlesbank Capital Partners (since 2021) and Warburg Pincus ($525 million investment, 2024) | PE-owned (stakes not stated) | DN33 |
| Dental Care Alliance (about 400, Becker's) | first-lien lenders after an out-of-court restructuring (2026); FSK holds common stock acquired 2026-06-01 (5–25%) | lender-owned (owner type not confirmed); formerly PE (Quad-C "Realized"; Harvest lists it as past; Mubadala per secondary) | DN34 |
| Specialized Dental Partners (more than 275, Becker's; specialty practices) | Quad-C Management (tile "Current") | PE-owned (stake not stated) | DN35 |
| Benevis (nearly 120, Becker's; the Kool Smiles name was retired) | not found (trade: New Mountain bought LT Smile in a 2020 bankruptcy sale; not on New Mountain's portfolio page) | not found | DN36 |
| Mortenson Dental Partners (156 practices; mixed naming, with Mortenson Family Dental offices plus affiliates under their own names, e.g. Nikodem Dental) | "doctor and employee-owned", with an ESOP | doctor- and employee-owned (no PE evidence found) | DN37 |

Smile Brands also supports "uniquely branded local practices" besides its regional banners. Its banners are rows 9, 11, 14, 18 and 28. Its locally named practices are not a separate entry; owner Gryphon (DN14).

**PE share among the 7 rollups:** 3 / 7 (42.9%) PE-owned (Heartland, MB2, Specialized Dental Partners). Adding Dental Care Alliance as lender-owned gives 4 / 7 with an investment firm or lender in control. 1 is doctor/ESOP-owned, and 2 are not found (PDS, Benevis).

- **DN31 Heartland Dental:** "With the agreement, KKR acquires a majority interest in Heartland Dental from Ontario Teachers' Pension Plan and other existing shareholders." and "Under the terms, Ontario Teachers' will retain sizeable ownership and will continue as a significant partner to the company." — [Ontario Teachers', "Heartland Dental and KKR Finalize Majority Interest Deal", April 30, 2018](https://otpp.com/en-ca/about-us/news-and-insights/2018/heartland-dental-and-kkr-finalize-majority-interest-deal/). kkr.com was not checked for current status.
- **DN32 PDS Health:** no primary owner statement found (1 search). pdshealth.com lists Stephen E. Thorne IV as founder and CEO (seen through search; not fetched).
- **DN33 MB2 Dental:** "today announced a strategic investment from Warburg Pincus", "Charlesbank Capital Partners will continue its longstanding partnership with the company and is excited to support MB2’s next growth phase" and "Since Charlesbank’s initial investment in 2021, MB2 has added over 450 new partnerships" — [Charlesbank, MB2 Dental release, November 12, 2024](https://www.charlesbank.com/news/mb2-dental-announces-recapitalization-event-with-new-investor-warburg-pincus-solidifying-company-growth-milestone/). The 2021 majority acquisition from Sentinel Capital Partners is per a GlobeNewswire release seen through search.
- **DN34 Dental Care Alliance:** "Milbank LLP acted as counsel to an ad hoc group of term loan lenders in an out-of-court restructuring of Dental Care Alliance (DCA), a large US dental support organization." — [Milbank, July 13, 2026](https://www.milbank.com/en/news/milbank-advises-ad-hoc-group-of-lenders-on-dental-care-alliance-restructuring-transaction.html). "The transaction will reduce the company’s debt by more than $1.1 billion, provide DCA with $95 million of new capital" — [Kirkland & Ellis, 27 April 2026](https://www.kirkland.com/news/press-release/2026/04/kirkland-advises-dental-care-alliance-on-strategic-transaction). Lender equity: "Dental Care Alliance Inc, Common Stock 3,744,469 $ 33.1 $ 32.4 6/1/2026", under footnote (ac) (affiliated person, not control) — [FS KKR Capital Corp 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/1422183/000162828026070499/fsk-20260930.htm). On [Quad-C's portfolio page](https://www.quadcmanagement.com/portfolio/), the tile text reads "Realized | Dental Care Alliance". Trade press says the lenders became majority owners (not cited).
- **DN35 Specialized Dental Partners:** the tile text on [Quad-C, Portfolio page](https://www.quadcmanagement.com/portfolio/) reads "Current | Specialized Dental" (HTML field; status precedes name in each tile). The 2021 investment date is per trade (not cited).
- **DN36 Benevis:** owner not found. The [New Mountain Capital portfolio page](https://www.newmountaincapital.com/portfolio/) has no "Benevis", "LT Smile" or "Kool Smiles" entry (checked 2026-11-07). FFL Partners' page (seen through search) still lists Benevis; trade press says FFL sold it to Tailwind and Littlejohn in 2018.
- **DN37 Mortenson Dental Partners:** WebFetch summary of [Mortenson Dental Partners, "Mortenson Dental Partners and Nikodem Dental affiliate", December 16, 2025](https://mortensondentalpartners.com/2025/12/mortenson-dental-partners-and-nikodem-dental-affiliate/) quotes "one of the largest groups of doctor and employee-owned dental support organizations in the United States" and "MDP has grown to 156 practices across ten states." The site returns 403 to curl (including robots.txt), so this quote passed through a summarizer and was not mechanically checked.

### Category share
N = 30 brand rows.
- **PE-owned (control, or a PE owner with no stated stake), current status confirmed: 15 / 30 = 50.0%.**
  - Via Sonrava Health / New Mountain Capital: Western Dental, DentalWorks, Brident, Perfect Teeth, Vital Smiles.
  - Via Smile Brands / Gryphon Investors: Midwest Dental, Monarch, Bright Now!, Castle, Mint Dentistry.
  - Via TAG / Ares, Leonard Green, American Securities: Aspen Dental, ClearChoice.
  - Smile Doctors (THL and Linden), Sage Dental (Linden), Jefferson Dental (Brentwood).
- **PE minority stake: 0.**
- **Investment-firm owner, current status not reconfirmed: 2 / 30 = 6.7%.** Ideal Dental (Blackstone Tactical Opportunities, 2021) and Dental365 (The Jordan Company, 2021). Counted, the PE share becomes 17 / 30 = 56.7%.
- **Lender-owned after 2026 restructuring: 2 / 30 = 6.7%.** Affordable Dentures & Implants and DDS Dentures (Affordable Care). Owner type not confirmed; trade press names Blackstone and KKR credit funds. Counted as well, the share becomes 19 / 30 = 63.3%.
- **Founder-led or doctor-owned, support company's owner not stated: 3 / 30 = 10.0%.** Comfort Dental, Coast Dental, Dental Depot.
- **Not found: 8 / 30 = 26.7%.** Great Expressions, Gentle Dental, Dental Dreams, Absolute Dental, Nuvia, Familia Dental, Tend, Risas. Three of them were PE-owned in the past (Great Expressions: Roark "Previous"; Gentle Dental/InterDent: H.I.G. "Realized"; Familia: Halifax "former").
- **Public company: 0.** So the glossary-strict count equals the counts above.
- **By parent company:** the 30 rows have 20 distinct parents.
  - PE-owned, confirmed: 6 / 20 = 30.0% (TAG, Smile Doctors, Sonrava, Smile Brands, Sage, Jefferson).
  - Adding DECA and Dental365: 8 / 20 = 40.0%.
  - Adding Affordable Care: 9 / 20 = 45.0%.
- **By office count** (27 rows with a count; counts mix dates from 2016 to 2026, and most are "more than" floors; 4,500 offices in all):
  - PE-owned, confirmed: 2,902 = 64.5%.
  - Adding the 2 unreconfirmed rows: 3,122 = 69.4%.
  - Adding Affordable Dentures & Implants: 3,547 = 78.8%.
- **Sources disagree:**
  - No ownership conflict between primary sources.
  - Counts conflict for Sonrava's total (over 400 on its own site vs over 580 on New Mountain's page), Affordable Care (340 on Berkshire's page vs about 425 trade), Familia (35 vs 37) and Coast Dental (more than 100 on its site vs 88 in a vendor release).
  - Midwest Dental's 141 is the worker's count of listed offices, not a stated figure.

### Firms named
As sources name them, for the Form ADV check:
- **Owners or holders of brand rows:** Ares Management, L.P.; Leonard Green & Partners, L.P.; American Securities LLC; New Mountain Capital; Gryphon Investors; Thomas H. Lee Partners, L.P. ("THL Partners"); Linden Capital Partners; Blackstone Tactical Opportunities (funds managed by; parent Blackstone Inc.); The Jordan Company, L.P. (via The Resolute Fund V, L.P.); Brentwood Associates.
- **Lenders holding equity:** FS KKR Capital Corp (Affordable Care Inc and Dental Care Alliance Inc common stock; its adviser was not checked). Blackstone and KKR credit funds are named by trade press only.
- **Former owners named in primary sources:** Berkshire Partners (Affordable Care, "former"); Roark Capital (Great Expressions, "Previous"); H.I.G. Capital (InterDent, "Realized"); The Halifax Group (Familia, "former"); Black Canyon Capital (Jefferson's seller, 2017); Regal Healthcare Capital Partners, L.P. (Dental365's seller, 2021).
- **Former owners named only through search:** Harvest Partners (Affordable Care 2021); OMERS Private Equity and Audax Group (Great Expressions); Sun Capital Partners (ClearChoice); FFL Partners, Tailwind Capital and Littlejohn & Co. (Benevis); Sentinel Capital Partners (MB2).
- **Rollups:** KKR and Ontario Teachers' Pension Plan (Heartland); Charlesbank Capital Partners and Warburg Pincus (MB2); Quad-C Management (Specialized Dental Partners; also former DCA investor); Mubadala (DCA, secondary only).
- **Lender, no equity found:** Bain Capital Specialty Finance (Great Expressions loan).

### BDC leads for the assembler
- **FS KKR Capital Corp 10-Q, Q3 2026** (https://www.sec.gov/Archives/edgar/data/1422183/000162828026070499/fsk-20260930.htm):
  - "Affordable Care Inc": first lien and subordinated debt, plus Class A and Class B common, both acquired 6/29/2026, under footnote (ac).
  - "Dental Care Alliance Inc": first lien, plus common stock acquired 6/1/2026, under footnote (ac).
  - "Dental365 LLC": first-lien loans.
- **Bain Capital Specialty Finance 10-Q, Q2 2026:** "Great Expressions Dental Center PC", first-lien loan maturing 9/30/2026, with 3.00% PIK.
- **EDGAR full-text search** for "Affordable Care" in 2026 10-Qs also hit KKR Enhanced US Direct Lending Fund-L, KKR FS Income Trust, KKR FS Income Trust Select and Crescent Capital BDC. Those filings were not opened.
- **Name variants to match:** "The Aspen Group", "Aspen Dental Management", "ADMI Corp", "ClearChoice", "Sonrava Health", "Western Dental Services", "Smile Brands", "Smile Doctors", "Sage Dental Management", "DECA Dental", "JDC Healthcare Management", "Jefferson Dental", "Heartland Dental", "MB2 Dental", "Specialized Dental Partners", "Benevis", "LT Smile", "InterDent", "Coast Dental", "Familia Dental", "Dental Care Alliance", "DCA Investment Holdings", "DCA Acquisition Holdings" and "Affordable Care".
- **Search lead, not checked:** Charlesbank's news page has the title "MB2 Dental Raises US$2.344bn Unitranche Debt Facility With KKR".

### Worker log (dental)
- **Time:** start 2026-11-07T17:23:52Z, end about 17:58Z, about 34 minutes wall-clock, including writing and the quote self-check.
- **Calls:** WebSearch 39 (1 in extended mode); WebFetch 7, of which 1 was usable (Mortenson) and 6 failed (403 ×5: Becker's ×2, DrBicuspid, Orbital, Blackstone; TLS mismatch ×1: idealdental.com); curl about 126 requests (125 logged GETs plus 1 HEAD).
  - **SEC:** 6 requests (4 EDGAR full-text searches; FSK and BCSF 10-Q documents). All were served HTTP 200 under the contact-free user agent `EvidenceEngine ownership-research bot (category audit)`, at 2 per second or less.
  - **Other curl requests:** 55 robots.txt fetches and the pages cited above.
  - **Status mix:** 108 × 200, 7 × 403 (Becker's, DrBicuspid, Blackstone, Mortenson, Mint, Nuvia, Sage), 7 × 404 (Aspen mediaroom and FinancialContent robots, Aspen mediaroom news index, Coast about-us, Brentwood /portfolio/, Dental365 ×2), 3 × TLS failure (Ideal Dental ×2, Jefferson Dental).
- **What was fast:**
  - Sponsor portfolio pages rendered on the server: Leonard Green, New Mountain, Gryphon, Linden, Brentwood, Berkshire, Roark, Quad-C and Halifax.
  - DSO brand pages that list every banner: Sonrava's brands page settled 5 rows with counts in one fetch, and Smile Brands' locations page tied 5 banners to Smile Brands.
  - TAG's mediaroom releases carry per-brand boilerplate with counts.
  - Each settled brand took 1–3 requests.
- **What was slow, and why:**
  - **Rankings.** The only DSO rankings (Becker's, DrBicuspid) are top-10 company lists behind JavaScript or Cloudflare challenges, and no brand ranking exists. Building the composite took about 8 minutes and 6 searches.
  - **Ownership changes in 2026 that the rankings predate.** Affordable Care's and DCA's lender takeovers were found through the BDC 10-Q, not through any company or sponsor statement. That took 4 searches and 5 requests.
  - **PE exits with no named buyer.** Great Expressions (Roark "Previous"), InterDent/Gentle Dental (H.I.G. "Realized") and Familia (Halifax "former") each took 4–6 requests and stayed unsettled.
  - **Brand-to-company links.** Ideal Dental needed 6 requests before a partner release named it "a flagship brand of DECA Dental".
  - **Blocked or unusable sites:**
    - script redirect: jordanco.com;
    - 403: blackstone.com, mortensondentalpartners.com, mintdentistry.com, nuviasmiles.com, mysagedental.com;
    - 404 to the bot: dental365.com;
    - TLS mismatch: idealdental.com, jeffersondental.com;
    - robots-disallowed: greatexpressions.com.
- **Which kinds of brands had no primary source for the owner:**
  - (a) Chains whose PE owner exited without a public buyer: Great Expressions, Gentle Dental (InterDent), Familia Dental.
  - (b) Founder- or doctor-led regional chains whose sites name founders or "doctor-owned" practices but never the support company's owner: Comfort Dental, Coast Dental, Dental Depot, Dental Dreams, Absolute Dental, Risas.
  - (c) Venture-backed chains with no ownership statement: Tend.
  - (d) Implant chains whose sites block bots: Nuvia.
  - (e) Lender-controlled DSOs after 2026 restructurings, where no source names the controlling holder: Affordable Care.
- **Affiliate programs:** checked with one category-wide search plus brand-site browsing during owner checks. No brand-direct program was found. Aspen Dental appears on FlexOffers and LinkClicky/Impact network listings, which were not opened or verified. Dental looks like a near-zero affiliate category, like restaurants and gyms in the pilot.
- **Quote caveats for the assembler:**
  - All curl'd quotes were checked as described above (83/83; negative control 3/3 failed).
  - Raw-HTML fields need the raw page, not stripped text: the Berkshire, Gryphon, Brentwood, Halifax and Roark tile classes, and the Linden URL paths.
  - FSK and BCSF quotes are whitespace-normalized table cells from 12–40 MB inline-XBRL files.
  - Mortenson (DN37) is the only WebFetch-summarized quote.
  - The Becker's ranking figures came only through search summaries and have no checkable page text.
