# Category audit: Veterinary chains

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (fetches logged 17:24–18:00 UTC) · Ownership facts come from primary sources only. Trade press and consultancy lists supply the candidate set and ranking only.

**Short answer**

| | Veterinary chains (21 brand rows: 19 fixed-site, 2 pop-up or in-home) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **11 / 21 (52.4%)**: 10 PE-owned (control, or a PE owner with no stated stake) plus 1 PE minority stake (MedVet, Leonard Green). |
| Strict count (public company with a 5%+ holder whose Form ADV reports PE funds) | **No change found: 11 / 21.** The two public non-PE rows have no investment-firm holder that could qualify: Tractor Supply (Vanguard 12.2%, BlackRock 9.2%) and Walmart (Walton Enterprises 44.11%, Walton Family Holdings Trust 6.44%). Petco and Chewy are already counted as PE-owned. Form ADV is for the assembler. |
| Owner not found | **1** (VEG ER for Pets), plus **4** where the owner type is not confirmed (Petfolk, Bond Vet, Small Door, Lovet) |
| Share of fixed-site hospitals on PE rows | **26.3%** (764 of 2,901 sites on the 19 fixed-site rows, PE-owned plus minority); Mars's three brands hold 64.3% |
| Brand-direct affiliate programs | **None found** for any vet-care brand. Two parents run store-wide programs that do not cover clinics: Chewy (Chewy Vet Care and Modern Animal rows; see the pet-stores audit) and Walmart (pilot). |
| Rollups and groups that are not brands | 30 listed. Of the 8 largest that were checked, **5 are PE-backed per a primary or law-firm source** (62.5%). The other 3 (NVA, PetVet Care Centers, VetCor) have only trade-press leads, and the rest were not checked. |

- **Fewer than 30 branded chains exist** in the sources found. Most large US vet groups are rollups whose hospitals keep their local names, so by the "Brand and chain model" rule they are companies, not brands. The table lists every consumer-facing vet banner found with about 15 or more sites, plus Walmart Pet Services (6), 21 rows in all.
- **Biggest finding:** the branded side is split in two. **Mars**, a family-owned company, holds the two largest banners (Banfield, VCA) plus BluePearl (#7): 64% of branded fixed-site hospitals. Nearly every other banner of any size is held by PE:
  - Petco's Vetco (CVC and CPP Investments);
  - Chewy's two clinic brands (BC Partners);
  - CityVet (RiverGlade);
  - UrgentVet (Oak Hill);
  - GoodVets and WellHaven (General Atlantic and SkyKnight);
  - Thrive (TSG);
  - Heart + Paw (Whistler);
  - Lap of Love (Cortec).
- **2026 ownership changes the rankings predate:**
  - Chewy bought Modern Animal (closed 2026-05-21).
  - Tractor Supply bought VIP Petcare from Bansk Group's PetIQ (2026-05-28).
  - Bond Vet and Small Door merged (2026-07-09); both brands continue.
  - GoodVets bought WellHaven from Martis Capital (announced 2026-09-24).
- **Formerly PE among non-PE rows:** VIP Petcare (Bansk Group via PetIQ, 2024-10-25 to 2026-05-28).

## How this was sourced (read first)

- **Ranking:** a composite by site count; see "Ranking" below.
- **Ownership facts:**
  - SEC filings: Petco, Chewy, Tractor Supply and Walmart 10-K, 10-Q and DEF 14A, and the PetIQ 8-K.
  - Company and sponsor pages: Mars, Banfield, VCA, BluePearl, TSG, Leonard Green, Oak Hill, RiverGlade, General Atlantic, Cortec, Shore, Gryphon and TAG.
  - Company releases on PR Newswire: Bond Vet, Petfolk, and Bond Vet with Small Door.
- **Law-firm releases:** four facts rest on these, and each is flagged in its row.
  - Bass, Berry & Sims for Heart + Paw. The company's own release sits on heartandpaw.com, whose robots.txt disallows ClaudeBot.
  - Holland & Knight for GoodVets / WellHaven, and Goodwin for Small Door. The company releases are on Business Wire, which returns 403.
  - Torys for AmeriVet (rollup list).
- **SEC access:** 16 requests (data.sec.gov submissions ×5, www.sec.gov documents ×11), all HTTP 200 except one mistyped URL (404, corrected). All used the user agent `EvidenceEngine ownership-research bot (category audit)` with no contact detail, with a 0.6 s sleep per request (under 2/s).
- **Robots:**
  - robots.txt was read before each new site was fetched with curl.
  - Not used:
    - heartandpaw.com and fairground.run (formerly withorbital.com, the data vendor the pilot tried) disallow ClaudeBot and anthropic-ai. heartandpaw.com was fetched once in the same command as its robots.txt, before the result was read, and is not cited. fairground.run was not fetched.
    - warburgpincus.com returned a Cloudflare challenge (403) and was not retried.
    - marsveterinary.com returned 403 to curl. It was read once through WebFetch, and those quotes are flagged.
  - Crawl-delay honored at mars.com (10 s), leonardgreen.com (10 s) and cityvet.com (10 s).
  - One slip: petiq.com's robots.txt sets `Crawl-delay: 10` outside any user-agent group, and its homepage was fetched 1.5 s after the robots.txt read. No other petiq.com page was fetched.
- **Never fetched:**
  - Private Equity Vet, Independent Vet (and the hn.jakechampion.name reader proxy of privateequityvet.org that appeared in a search), WhoIsMyDentist, Reddit and competitor sites;
  - PitchBook, Preqin, CB Insights and Crunchbase results.
  - Ethos Veterinary Health (ethosvet.com) was not fetched either, so its name never gets confused with the competitor Ethos. Its facts below come from nva.com.
- **Leads only, never cited:** deal directories (mergr, privsource, privateequityinfo, mergerlinks) and consultancy pages (transitionselite.com, vetvalue.pet, ctacquisitions.com) were used for leads only. So were trade items seen only as search snippets (dvm360, AVMA, pets.care, Today's Veterinary Business).
- **Owner kinds are research notes, not engine classifications.**
  - "PE-owned" means control, or a PE owner with no stated stake.
  - A public company that a PE fund controls (Petco, Chewy) counts as PE-owned, and so do brands it owns (Vetco, Chewy Vet Care, Modern Animal).
  - Counts are by brand row: Mars is 3 rows, Chewy 2, GoodVets 2 (GoodVets, WellHaven), and the merged Bond Vet / Small Door company 2.
- **Quotes:** copied from the curl'd page text with whitespace collapsed and HTML entities decoded. Exceptions are flagged:
  - VT2 and VT7 cite marsveterinary.com through the WebFetch summarizer.
  - VT14 cites a meta description.
  - Several items are page fields, sitemap counts or table cells, not sentences.
  - Some SEC and PR Newswire sentences have a stray space before punctuation where the HTML splits a tag (for example "Petfolk ," and "100 %"). They are quoted as the text renders.

## Ranking

**No free, current top-30 ranking of US veterinary chains was found**, and none ranks consumer-facing brands rather than owner groups.
- **Veterinary Integration Solutions, "Roll Call: North America's Biggest Veterinary Consolidators and Groups"** (Dr. Ivan Zak, updated 2022-12-07), https://vetintegrations.com/insights/veterinary-consolidators/.
  - It is a consultancy list of about 48 groups with "Number of Hospitals / Partner Locations", and it is nearly four years old.
  - It was used as the candidate set only. Its counts were not used.
- **Rejected:**
  - VetValue "Overview of Veterinary Practice Consolidators" (dated "Last Updated October 14, 2026", but its counts are old, for example "NVA (approx. 700…)").
  - Fairground / Orbital "Largest veterinary chains in the US" (robots.txt disallows ClaudeBot).
  - dvm360 "The state of veterinary corporatization" (undated, older counts).
  - Transitions Elite, PE Reveal and Fulkerson Advisors (consultancy or newsletter pages; leads only).
  - Private Equity Vet (never fetched).

**Composite used:**
- **Candidate set:**
  - the VIS roll call;
  - the Mars Veterinary Health family (Banfield, VCA, BluePearl);
  - in-store and retailer clinic networks named in filings (Petco, Chewy, Tractor Supply, Walmart);
  - single-brand chains surfaced in owner searches.
- **Placement:** each brand is placed by its own US site count as of 2026-11-07, from:
  - (a) the company's or sponsor's own statement;
  - (b) a count of location pages in the brand's own sitemap or location directory (marked "sitemap" or "directory");
  - (c) a filing.
- Fixed-site hospitals and clinics are ranked 1–19. Two networks without fixed hospitals are listed after them, unranked by hospitals: VIP Petcare (pop-up clinics in retail stores) and Lap of Love (in-home).
- **Not exhaustive:**
  - Brands under about 15 sites were not searched for systematically. Seen but left out: SAGE Veterinary Centers (an NVA specialty banner, single digits per the VIS list), Village Vets, PetWellClinic, Vetique.
  - Mobile and telehealth brands (The Vets, BetterVet, Vetster) were not researched.
  - Pet Paradise (boarding resorts with some clinics) and NVA Pet Resorts were left out as boarding, not vet, chains.
- **Banner rule applied:**
  - Thrive Pet Healthcare is a mixed group. About 29 of the 363 location pages in its sitemap have neighborhood or street slugs, and one checked page is named "Thrive Pet Healthcare – Eldridge". The rest carry practice names (for example `/animal-care-clinic`, `/elgin-veterinary-hospital`). So the Thrive-named clinics are one brand row, and the locally named practices are in the rollup list.
  - Ethos Veterinary Health (NVA) is in the rollup list because its hospitals' names were not checked.
  - WellHaven is a row because its site markets one consumer brand. Its per-location names were not checked; see VT11.

| # | Brand (US sites, source) | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Banfield Pet Hospital (1,000+ incl. Puerto Rico, company) | Mars, Incorporated ("an Affiliate of Mars, Incorporated") | family | none | 2007 | — | not checked | none found | VT1 |
| 2 | VCA Animal Hospitals (774, directory) | Mars ("Affiliate of Mars Inc.") | family | none | 2017 | — | company network of acquired hospitals, all VCA-named (not checked further) | none found | VT2 |
| 3 | Vetco / Petco veterinary hospitals (~300 hospitals plus ~1,600 weekly Vetco clinics, 10-K) | Petco Health & Wellness Company, Inc., controlled by CVC Funds and CPP Investments via Scooby Aggregator, LP (64.4% of total voting power) | PE-owned (public, PE-controlled) | CVC Capital Partners; Canada Pension Plan Investment Board | 2016-01-26 (Sponsors' acquisition of Petco) | WOOF | in Petco stores, company network | none brand-direct (Petco store-wide network listings, see pet-stores audit) | VT3 |
| 4 | VEG ER for Pets (130+, US and Canada, company) | not found (founder-led; owner not stated) | not found | not found (investors named only in a 2021 release that returned 403) | — | — | company-operated (not checked) | none found | VT4 |
| 5 | CityVet (103, sitemap) | RiverGlade Capital (current investment) | PE-owned (stake not stated) | RiverGlade Capital | not found | — | "single-branded veterinary practices" | none found | VT5 |
| 6 | UrgentVet (101 incl. coming soon, company) | American Veterinary Group (AVG), backed by Oak Hill Capital (current portfolio); management retains a stake | PE-owned (via AVG; stake not stated) | Oak Hill Capital (bought from Trive Capital and Latticework) | 2021-02-22 | — | urgent-care clinics, de novo | none found | VT6 |
| 7 | BluePearl Pet Hospital (92, sitemap) | Mars ("our parent company, Mars Petcare") | family | none | 2015 | — | emergency and specialty | none found | VT7 |
| 8 | GoodVets (75 before WellHaven, law-firm release; 88 clinic pages in sitemap) | GoodVets Group LLC; investors General Atlantic and SkyKnight Capital, L.P. | PE-owned (stake not stated) | General Atlantic; SkyKnight Capital | 2021 (SkyKnight, release not read); 2023-09-13 (General Atlantic) | — | "partners with entrepreneurial veterinarians" | none found | VT8 |
| 9 | Petfolk (51, sitemap) | not stated; Series C led by Deerfield Management | Owner type not confirmed (VC and growth investors) | none confirmed (Deerfield, Movendo, White Star: type not confirmed) | — | — | urgent and primary care clinics | none found | VT9 |
| 10 | Bond Vet (45, sitemap) | merged company of Bond Vet and Small Door (2026-07-09; owners not stated); pre-merger investors Warburg Pincus and Talisman Capital | Owner type not confirmed (PE firm Warburg Pincus among pre-merger investors) | Warburg Pincus (2021 investment, stake not stated) | merger 2026-07-09 | — | company clinics | none found | VT10 |
| 11 | WellHaven Pet Health (40+, company) | GoodVets Group LLC (bought from Martis Capital) | PE-owned (via GoodVets) | General Atlantic; SkyKnight Capital; formerly Martis Capital | announced 2026-09-24 | — | general practices; banner status see VT11 | none found | VT11 |
| 12 | MedVet (40, sitemap) | MedVet LLC: "veterinarian owned and led"; 95% of owners are current or retired doctors and employees; Leonard Green minority | PE minority stake | Leonard Green & Partners (minority, 2024); formerly Goldman Sachs Merchant Banking (2019) | 2024-06-25 | — | emergency and specialty; employee-owned | none found | VT12 |
| 13 | Modern Animal (30, sitemap) | Chewy, Inc. (wholly-owned subsidiary), controlled by BC Partners-led consortium | PE-owned (via Chewy, public, PE-controlled) | BC Partners | 2026-05-21 | CHWY | company clinics | none brand-direct (Chewy store-wide program, not clinic-specific) | VT13 |
| 14 | Thrive Pet Healthcare, Thrive-named clinics (~29 of 363 locations, sitemap heuristic) | TSG Consumer Partners (Thrive Pet Healthcare, current investment) | PE-owned (stake not stated) | TSG Consumer Partners | 2020 | — | mixed group; locally named practices listed under rollups | none found | VT14 |
| 15 | Heart + Paw (28, law-firm release, 2024) | Whistler Capital Partners (strategic growth investment) | PE-owned (stake not stated) | Whistler Capital Partners | 2024-01 | — | vet co-ownership model (not read in a usable source) | none found | VT15 |
| 16 | Lovet Pet Health Care, formerly AZPetVet (22 at acquisition, company) | TAG – The Aspen Group (ADMI Corp.) | Owner type not confirmed (TAG's owners not found in a primary source) | not found | 2022 (agreement 2022-08-16) | — | TAG "supports independent healthcare practices" | none found | VT16 |
| 17 | Chewy Vet Care (18, 10-K) | Chewy, Inc., controlled by BC Partners-led consortium ("BCP Stockholder Parties control a majority of the voting power") | PE-owned (public, PE-controlled) | BC Partners | 2024 (brand launched) | CHWY | company clinics | none brand-direct (Chewy store-wide program) | VT17 |
| 18 | Small Door Veterinary (17, sitemap) | merged company of Bond Vet and Small Door; pre-merger equity led by Valspring Capital | Owner type not confirmed (VC and growth investors) | none confirmed (Valspring Capital: type not confirmed) | merger 2026-07-09 | — | membership-based clinics | none found | VT18 |
| 19 | Walmart Pet Services (6, company, 2024) | Walmart Inc. | public company (family-controlled: Walton Enterprises 44.11%) | none | 2023 (first center) | WMT | Walmart centers; "services provided … in collaboration with PetIQ" | none brand-direct (Walmart store-wide program, pilot) | VT19 |
| — | VIP Petcare (2,900+ pop-up locations in retail stores, company; not ranked by hospitals) | Tractor Supply Company (100% of equity) | public company | none at 5%+ (Vanguard, BlackRock); formerly Bansk Group via PetIQ | 2026-05-28 | TSCO | pop-up community clinics in retailers | none found | VT20 |
| — | Lap of Love Veterinary Hospice (in-home; "more than 135 veterinarians" in 2020; not ranked by hospitals) | Cortec Group (portfolio tile: "Owned"), in partnership with the co-founders | PE-owned (stake not stated; trade press says minority) | Cortec Group (Fund VI in 2020; tile now reads Fund VIII) | 2020-01-24 | — | in-home only, "does not operate clinics" | none found | VT21 |

### Evidence
- **VT1 Banfield Pet Hospital**
  - Owner: "In 2007, Banfield joined the Mars, Incorporated family of businesses, uniting our team of passionate professionals under a shared purpose: A BETTER WORLD FOR PETS." — [Banfield, About page, accessed 2026-11-07](https://www.banfield.com/about-banfield)
  - Owner (footer): "Banfield Pet Hospital, an Affiliate of Mars, Incorporated" — [same page](https://www.banfield.com/about-banfield)
  - Count: "Banfield is now the leading provider of preventive veterinary care in the U.S. with more than 1,000 hospitals in neighborhoods across the country and Puerto Rico." — [same page](https://www.banfield.com/about-banfield)
  - Parent kind: "Mars has been a family-owned business for over a century." — [Mars, All About Mars, accessed 2026-11-07](https://www.mars.com/about)
  - Affiliate: none found
- **VT2 VCA Animal Hospitals**
  - Owner: "VCA joined the Mars family in 2017." — [VCA, About VCA, accessed 2026-11-07](https://vcahospitals.com/about-vca)
  - Owner (footer): "Affiliate of Mars Inc." — [same page](https://vcahospitals.com/about-vca)
  - Model: "As a national network of hometown hospitals, we provide world-class veterinary medicine by activating our shared expertise and pairing cutting-edge technology, procedures and best practices with deeply compassionate care." — [same page](https://vcahospitals.com/about-vca)
  - Count: 774 distinct hospital links whose names start with "VCA" (for example "VCA 12-Mile Animal Hospital") — [VCA Location Directory, accessed 2026-11-07](https://vcahospitals.com/find-a-hospital/location-directory). Every hospital name carries the VCA brand.
  - Other count: Mars Veterinary Health says VCA has "...more than 1,000 small animal general, specialty and emergency veterinary hospitals..." — [Mars Veterinary Health, Our Companies](https://marsveterinary.com/who-we-are/our-companies/). Read through the WebFetch summarizer because curl got 403. The quote is truncated by the summarizer and may not match the page exactly.
  - Affiliate: none found
- **VT3 Vetco / Petco veterinary hospitals**
  - Count: "As of January 31, 2026, we had approximately 300 full service veterinary hospitals in our network and operated approximately 1,600 Vetco clinics on a weekly basis." — [Petco, Form 10-K FY2025, filed 2026-03-13](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm)
  - Brand: "Petco Love, Petco Park, Reddy, Ruff & Mews, So Phresh, Vetco, Well & Good" (trademark list) — [same 10-K](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm)
  - Owner: "certain funds (the “CVC Funds”) that are advised and/or managed by CVC Capital Partners (“CVC”) and Canada Pension Plan Investment Board" — [same 10-K](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm)
  - Control: "Our Sponsors primarily exercise their control through Scooby Aggregator, LP (our “Principal Stockholder”)." and "We are a “controlled company” within the meaning of the Nasdaq rules" — [same 10-K](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm)
  - Voting: the table row for Scooby Aggregator, LP reads "64.4 %" of total voting power and "51.2 %" of director election power. "The general partner of Scooby LP is Scooby GP LLC, a member-managed limited liability company whose sole members are CVC Pet LP and CPP Investments." — [Petco, DEF 14A, filed 2026-05-14](https://www.sec.gov/Archives/edgar/data/1826470/000182647026000040/woof-20260514.htm)
  - Since: "On January 26, 2016, the Company completed a merger (the “Acquisition”) whereby Petco Holdings, Inc. converted from a Delaware corporation to a Delaware limited liability company and became a wholly owned subsidiary of the Company." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1826470/000119312526106114/woof-20260131.htm)
  - Affiliate: none brand-direct. Petco's store-wide network listings are covered in the pet-stores audit (PT2).
  - Notes: Petco's rows in the pet-stores audit carry the same owner facts.
- **VT4 VEG ER for Pets (Veterinary Emergency Group)**
  - Count: "With over 130 hospitals across the United States and Canada, VEG ER for Pets provides 24/7 expert emergency vet care for pets." — [VEG, home page (www.veg.vet, served as www.veg.com), accessed 2026-11-07](https://www.veg.vet/)
  - Founder: "After years of working in emergency vet med, Dr. David Bessler had a radical idea to fix the way things had always been done." — [VEG, Our Story](https://www.veg.com/our-story)
  - Owner: not found. The site names founders but no owner. The company's 2021 funding release names D1 Capital Partners, Fidelity Management & Research Company LLC and Durable Capital Partners LP, but it is on Business Wire and returned 403 to WebFetch, so it was seen only in its title and in search snippets ([URL](https://www.businesswire.com/news/home/20210922005550/en/Veterinary-Emergency-Group-Announces-Its-Third-Round-of-Funding-With-%24100-Million-in-Financing-Co-Led-by-D1-Capital-Partners-and-Fidelity-Management-Research-Company-LLC-and-Supported-by-Durable-Capital-Partners-LP)). Snippets also name Sequoia Heritage as an earlier investor. No later round was found.
  - Affiliate: none found
  - Notes: 6 requests (robots, home, sitemap, pages sitemap, news, story), then stopped. robots.txt was read on veg.vet. The site serves from veg.com (its sitemap points there), and veg.com's robots.txt was not read separately.
- **VT5 CityVet**
  - Owner: "Network of single-branded veterinary practices offering comprehensive pet care services including medical, surgical, retail, pharmacy, boarding, grooming and wellness." — [RiverGlade Capital, Investments, accessed 2026-11-07](https://riverglade.com/investments/). This is the CityVet tile.
  - Current: the CityVet tile carries filter class `awsm-40`, which the page's filter buttons label "Current" (`data-rel="awsm-40"` … "Current"; "Realized" is `awsm-41`). This is a page field, not a sentence.
  - Count: 103 location URLs in [CityVet's store-locator sitemap](https://www.cityvet.com/wpsl_stores-sitemap.xml) (accessed 2026-11-07). The home page lists 17 markets.
  - Since: not found
  - Affiliate: none found
- **VT6 UrgentVet**
  - Brand to parent: "In partnership with Trive and Latticework, the management team executed on an integrated market strategy to build a highly synergistic ecosystem of general veterinary practices and UrgentVet clinics." — [Trive Capital, "Trive Capital Announces Sale of American Veterinary Group" (2021)](https://www.trivecapital.com/trive-capital-announces-sale-of-american-veterinary-group/)
  - Owner: "Oak Hill Capital (“Oak Hill”), a New York-based middle-market private equity firm, announced its investment and partnership with American Veterinary Group (“AVG” or “the Company”)." — [Oak Hill, release dated 2021-02-22](https://oakhill.com/2021/02/22/oak-hill-capital-to-partner-with-american-veterinary-group/)
  - Stake: "Terms of the transaction were not disclosed." and "The management team of AVG, led by Chief Executive Officer Craig Niebur, Chief Operating Officer Dr. Christopher Smith, and Chief Development Officer Jim Herring will continue to lead the Company and retain an ownership stake" — [same release](https://oakhill.com/2021/02/22/oak-hill-capital-to-partner-with-american-veterinary-group/)
  - Current: "Current Portfolio American Veterinary Group Veterinary group based in the South that partners with relationship-focused hospitals throughout the region." — [Oak Hill, Investments, accessed 2026-11-07](https://oakhill.com/investments/)
  - Count: "Showing 1 - 10 of 101 locations" — [UrgentVet, Locations, accessed 2026-11-07](https://urgentvet.com/locations/). The list includes locations marked "Coming Soon".
  - Affiliate: none found
  - Notes: urgentvet.com names no owner (about page checked).
- **VT7 BluePearl Pet Hospital**
  - Owner: "BluePearl is proud to be a part of the Mars Veterinary Health family of veterinary practices and labs." and "We follow the five guiding principles created by our parent company, Mars Petcare" — [BluePearl, About Us, accessed 2026-11-07](https://bluepearlvet.com/about-us/)
  - Since: "In 2015, BluePearl joined the Mars Veterinary Health family..." — [Mars Veterinary Health, Our Companies](https://marsveterinary.com/who-we-are/our-companies/). Read through WebFetch (curl got 403); the summarizer truncated it.
  - Count: 92 top-level hospital pages in [BluePearl's hospital sitemap](https://bluepearlvet.com/hospital-sitemap.xml) (accessed 2026-11-07). Mars Veterinary Health says "over 100" (WebFetch).
  - Affiliate: none found
- **VT8 GoodVets**
  - Owner: "GoodVets Group LLC (“GoodVets”), a leading modern, single-brand veterinary care platform purpose-built to better serve pet owners and vets through premier medicine, customer service, technology, and design, today announced it has received a strategic growth investment from General Atlantic, a leading global growth equity firm." — [General Atlantic, press release dated 2023-09-13](https://www.generalatlantic.com/media-article/goodvets-announces-strategic-growth-investment-from-general-atlantic-to-fuel-continued-expansion-of-leading-veterinary-care-platform/)
  - Co-investor: "General Atlantic joins existing investor SkyKnight Capital, L.P. (“SkyKnight”)." — [same release](https://www.generalatlantic.com/media-article/goodvets-announces-strategic-growth-investment-from-general-atlantic-to-fuel-continued-expansion-of-leading-veterinary-care-platform/)
  - Model: "Founded in 2016, GoodVets partners with entrepreneurial veterinarians to build and operate state-of-the-art care facilities in fast-growing markets" — [same release](https://www.generalatlantic.com/media-article/goodvets-announces-strategic-growth-investment-from-general-atlantic-to-fuel-continued-expansion-of-leading-veterinary-care-platform/)
  - Count: "The transaction expands GoodVets' network from 75 to 116 hospitals and meaningfully extends its presence across key regions in the U.S., including the Pacific Northwest and Midwest." — [Holland & Knight, press release dated 2026-09-28 (law-firm release)](https://www.hklaw.com/en/news/pressreleases/2026/09/holland-and-knight-advises-goodvets-in-acquisition-of-wellhaven). GoodVets' own sitemap has 88 clinic pages under 26 cities ([sitemap](https://www.goodvets.com/sitemap.xml)), likely including openings.
  - Affiliate: none found
  - Notes: SkyKnight's 2021 entry is known only from search snippets of a Business Wire release (2021-07-12), which was not read.
- **VT9 Petfolk**
  - Investors: "has received a $36 million Series C investment led by Deerfield Management" and "Existing investors Movendo Capital, White Star Capital, Cutting Horse VC, Idea Farm Ventures, and Parkview International participated in the round." — [Petfolk, PR Newswire release dated 2024-10-29](https://www.prnewswire.com/news-releases/petfolk-receives-series-c-investment-led-by-deerfield-management-to-advance-the-evolution-of-veterinary-care-302289240.html)
  - Owner: not stated (a Series C lead is not stated to control)
  - Count: 51 clinic pages in 17 markets in [Petfolk's sitemap](https://petfolk.com/sitemap.xml) (accessed 2026-11-07)
  - Affiliate: none found
- **VT10 Bond Vet**
  - Investor (2021): "today announced a $170 million investment from Warburg Pincus, a leading global growth investor." — [Bond Vet, PR Newswire release dated 2021-10-11](https://www.prnewswire.com/news-releases/bond-vet-announces-growth-investment-from-warburg-pincus-301397215.html)
  - Co-investor: "The new partnership with Warburg Pincus and the continuing support of our initial capital provider Talisman Capital, will help accelerate our growth" — [same release](https://www.prnewswire.com/news-releases/bond-vet-announces-growth-investment-from-warburg-pincus-301397215.html)
  - Merger: "Bond Vet and Small Door Veterinary announced today that they have finalized their merger, forming one of the largest premium veterinary networks in the country." — [Bond Vet and Small Door Veterinary, PR Newswire release dated 2026-07-09](https://www.prnewswire.com/news-releases/bond-vet-and-small-door-veterinary-merge-to-expand-access-to-trusted-veterinary-care-302821175.html)
  - Brands kept: "In the near term, Small Door and Bond Vet will continue to operate under their own brands across all existing locations, with the same care teams pet families know today." — [same release](https://www.prnewswire.com/news-releases/bond-vet-and-small-door-veterinary-merge-to-expand-access-to-trusted-veterinary-care-302821175.html)
  - Terms: "Financial terms of the transaction were not disclosed." — [same release](https://www.prnewswire.com/news-releases/bond-vet-and-small-door-veterinary-merge-to-expand-access-to-trusted-veterinary-care-302821175.html)
  - Count: 45 clinic booking pages in [Bond Vet's sitemap](https://bondvet.com/sitemap-0.xml) (accessed 2026-11-07). The merger release says the combined company has "more than 55 clinics".
  - Affiliate: none found
  - Notes: the merger release names no owners of the combined company. Warburg Pincus's portfolio page returned a Cloudflare challenge.
- **VT11 WellHaven Pet Health**
  - Owner: "Holland & Knight represented GoodVets Group LLC, a full-service veterinary care company, in its acquisition of WellHaven Pet Health, a network of more than 40 veterinary hospitals operating across seven states, from Martis Capital." — [Holland & Knight, press release dated 2026-09-28 (law-firm release)](https://www.hklaw.com/en/news/pressreleases/2026/09/holland-and-knight-advises-goodvets-in-acquisition-of-wellhaven)
  - Count: "With more than 40 locations across five states, we’d love for you to join our family!" — [WellHaven Pet Health, home page, accessed 2026-11-07](https://www.wellhavenpethealth.com/)
  - Since: "The transaction was announced on September 24." (same Holland & Knight release)
  - Banner status: the site title is "Your CareCompanion™ Veterinarians | WellHaven Pet Health" and it runs one phone line, "(833) WELL-PET". Per-location names were not checked (the locations page returned 404). Trade snippets say WellHaven hospitals will move to the GoodVets brand.
  - Affiliate: none found
  - Notes: the GoodVets release itself is on Business Wire (403) and was not read. The two sources differ on states (seven vs five).
- **VT12 MedVet**
  - Owner (2024): "MedVet LLC, a leading provider of emergency and specialty veterinary care, today announced that it has received a minority capital investment from Leonard Green & Partners, L.P. (LGP) and a senior term loan from Oak Hill Advisors (OHA)." — [Leonard Green, release dated 2024-06-25 (posted 2024-06-28)](https://www.leonardgreen.com/medvet-receives-financing-to-support-continued-growth-in-specialty-healthcare-for-pets)
  - Exit of 2019 investors: "provide minority shareholders a successful exit from their 2019 investment, and provide partial liquidity for some of MedVet’s employee owners." — [same release](https://www.leonardgreen.com/medvet-receives-financing-to-support-continued-growth-in-specialty-healthcare-for-pets)
  - Owners: "continuing to provide a liquid investment to our owners, 95% of whom are current or retired doctors and employees" — [same release](https://www.leonardgreen.com/medvet-receives-financing-to-support-continued-growth-in-specialty-healthcare-for-pets)
  - Current: "MedVet is a leading veterinarian-owned and led network of specialty and emergency hospitals across the U.S. Sector: Healthcare Deal Type: Recapitalization Status: Current" — [Leonard Green, Portfolio, accessed 2026-11-07](https://www.leonardgreen.com/portfolio/)
  - 2019: "MedVet, a growing nationwide network of specialty and emergency veterinary hospitals, has secured an investment from entities affiliated with the Goldman Sachs Merchant Banking Division" — [MedVet, News release dated 2019-07-15](https://www.medvet.com/?p=17237)
  - Count: 40 location pages in [MedVet's location sitemap](https://www.medvet.com/location-sitemap.xml) (accessed 2026-11-07)
  - Affiliate: none found
  - Notes: the 2019 release calls Goldman Sachs, SkyKnight Capital and Stonehenge Partners investors. The 2024 release says the 2019 "minority shareholders" exited. Whether Goldman Sachs still holds a stake was not checked.
- **VT13 Modern Animal**
  - Owner: "On April 1, 2026, the Company entered into a definitive agreement to acquire Modern Animal, Inc. (“Modern Animal”)." and "and Modern Animal became a wholly-owned subsidiary of the Company." — [Chewy, Form 10-Q for the quarter ended 2026-08-02, filed 2026-09-09](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)
  - Since: "on May 21, 2026, the Company completed the acquisition of 100 % of the issued and outstanding stock in Modern Animal" — [same 10-Q](https://www.sec.gov/Archives/edgar/data/1766502/000162828026061018/chwy-20260802.htm)
  - Parent control: see VT17
  - Count: 30 clinic pages in [Modern Animal's sitemap](https://www.modernanimal.com/sitemap.xml) (accessed 2026-11-07). Some are marked "Opening" on the locations page.
  - Affiliate: none brand-direct (Chewy's store-wide program)
- **VT14 Thrive Pet Healthcare (Thrive-named clinics)**
  - Owner: the Thrive Pet Healthcare tile reads "Veterinary hospitals and specialty pet healthcare services Investment Details Investment Year 2020 Status Current" — [TSG Consumer Partners, Portfolio, accessed 2026-11-07](https://www.tsgconsumer.com/portfolio/). These are page fields.
  - Banner: "Thrive Pet Healthcare - Eldridge is a veterinary clinic serving clients in Houston and the surrounding areas." — [Thrive, Eldridge location page](https://www.thrivepetcare.com/locations/texas/houston/eldridge). This is the page's meta description; the visible page renders by JavaScript.
  - Count: [Thrive's sitemap](https://www.thrivepetcare.com/sitemap.xml) has 363 location pages. 29 have slugs that are not practice names (for example `eldridge`, `the-heights`, `183a-toll-road`, `thrive-east-austin`), so they are likely Thrive-named. Only Eldridge was confirmed.
  - Affiliate: none found
  - Notes: the remaining ~334 Thrive locations carry local practice names and are in the rollup list.
- **VT15 Heart + Paw**
  - Owner: "We represented Whistler Capital, a leading healthcare-focused private equity firm, in its strategic growth investment in Heart & Paw, a veterinary and multi-service pet care company operating in 28 locations across 10 states." — [Bass, Berry & Sims, "Whistler Capital Partners Acquires Heart + Paw" (law-firm page)](https://www.bassberry.com/experience/whistler-capital-partners-acquires-heart-paw/)
  - Terms: "Terms of the transaction were not disclosed." (same page)
  - Since: January 2024 per the company release (not used)
  - Affiliate: none found
  - Notes: the company's own release is at heartandpaw.com/press/…, but that site's robots.txt disallows ClaudeBot and anthropic-ai. It was fetched once before the robots result was read, and it is not cited. The law-firm page title says "Acquires", while its text says "strategic growth investment": a framing difference.
- **VT16 Lovet Pet Health Care (formerly AZPetVet)**
  - Owner: "TAG - The Aspen Group℠ announced today that it has reached an agreement to acquire AZPetVet, subject to governmental approvals and other customary closing conditions." — [TAG, newsroom, dated 2022-08-16](https://www.teamtag.com/newsroom/the-aspen-group-to-acquire-azpetvet/)
  - Count: "AZPetVet is a market leader in veterinary care with a network of 22 animal hospitals in the greater Phoenix area." — [same page](https://www.teamtag.com/newsroom/the-aspen-group-to-acquire-azpetvet/)
  - Current brand: "TAG supports independent healthcare practices operating more than 1,400 locations in 46 states through five consumer healthcare brands: Aspen Dental®, ClearChoice Dental Implant Center®, WellNow Urgent Care®, Chapter Aesthetic Studio℠ and Lovet Pet Health Care (formerly AZPetVet)." — [same page, footer](https://www.teamtag.com/newsroom/the-aspen-group-to-acquire-azpetvet/)
  - Entity: "© 2026 ADMI Corp. d/b/a TAG - The Aspen Group." (same footer)
  - TAG's owners: not found. A trade item (pets.care, search snippet) names Ares Management, Leonard Green & Partners and American Securities. Leonard Green's own portfolio page does not list TAG or Aspen Dental.
  - Affiliate: none found
  - Notes: Aspen Dental is in the dental-chains audit; check that file for TAG's owners.
- **VT17 Chewy Vet Care**
  - Count: "In 2024, we opened and operated eight veterinary clinics under the brand name “Chewy Vet Care,” offering pet health services including routine appointments, urgent care and surgery." and "In 2025, we continued to expand our Chewy Vet Care practices, bringing the total number of clinics to 18." — [Chewy, Form 10-K FY2025, filed 2026-03-25](https://www.sec.gov/Archives/edgar/data/1766502/000176650226000034/chwy-20260201.htm)
  - Owner: "The Company is controlled by a consortium including private investment funds advised by BC Partners Advisors LP (“BC Partners”) and its affiliates, La Caisse de dépôt et placement du Québec, affiliates of GIC Special Investments Pte Ltd, affiliates of StepStone Group LP and funds advised by Longview Asset Management, LLC (collectively, the “Sponsors”)." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1766502/000176650226000034/chwy-20260201.htm)
  - Control: "As of March 18, 2026, the BCP Stockholder Parties control a majority of the voting power of our outstanding common stock." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1766502/000176650226000034/chwy-20260201.htm)
  - Affiliate: none brand-direct for clinics. Chewy's store-wide program (via Impact) is in the pet-stores audit (PT27).
  - Notes: trade snippets say the Modern Animal deal takes Chewy's combined clinic count to 47 (18 + 29).
- **VT18 Small Door Veterinary**
  - Investors (2025): "The raise includes a $35 million equity financing led by Valspring Capital, with participation from existing investors, Primary Venture Partners, C&S Family Capital, Lerer Hippeau, and Toba Capital, as well as a new $20 million debt facility from Bridge Bank, a division of Western Alliance Bank." — [Goodwin, press release dated 2025-08-01 (law-firm release)](https://www.goodwinlaw.com/en/news-and-events/news/2025/08/announcements-technology-goodwin-advises-small-door-veterinary-in-raising-55-million)
  - Merger: see VT10. "Florent Peyre, co-founder and CEO of Small Door, will lead the new company as CEO" — [merger release](https://www.prnewswire.com/news-releases/bond-vet-and-small-door-veterinary-merge-to-expand-access-to-trusted-veterinary-care-302821175.html)
  - Count: 17 clinic pages in [Small Door's sitemap](https://www.smalldoorvet.com/sitemap.xml) (accessed 2026-11-07). The merger release says "Small Door operates 13 clinics" per snippets; that line was not checked on the page.
  - Owner: not stated (about page checked)
  - Affiliate: none found
- **VT19 Walmart Pet Services**
  - Brand: "Walmart today announced the expansion of its Walmart Pet Services centers, planned to open over the next month in the following cities: Cumming, Georgia Alpharetta, Georgia Glendale, Arizona Chandler, Arizona Mesa, Arizona" — [Walmart, corporate news dated 2024-10-08](https://corporate.walmart.com/news/2024/10/08/pet-care-unleashed-were-announcing-new-service-locations-online-vet-access-and-prescription-delivery). Count: these 5 plus the Dallas, Georgia pilot = 6.
  - Model: "with services provided by experienced veterinary and grooming professionals in collaboration with PetIQ" — [same page](https://corporate.walmart.com/news/2024/10/08/pet-care-unleashed-were-announcing-new-service-locations-online-vet-access-and-prescription-delivery)
  - 5% holders: the table lists "Walton Enterprises, LLC" 44.11% and "Walton Family Holdings Trust" 6.44% — [Walmart, DEF 14A, filed 2026-04-23](https://www.sec.gov/Archives/edgar/data/104169/000119312526173673/wmt-20260423.htm)
  - Since: first center 2023 (the corporate news title "Walmart Opens First-Ever Pet Services Center in Dallas, Georgia", 2023-09-20, seen in search only)
  - Affiliate: none brand-direct. Walmart's store-wide program is noted in the pilot (eyewear).
  - Notes: whether PetIQ's role passed to VIP Petcare / Tractor Supply in 2026 was not checked. The current count was not rechecked.
- **VT20 VIP Petcare**
  - Owner: "On May 28, 2026, the Company completed its acquisition of VIP Petcare, the veterinary services business of PetIQ." — [Tractor Supply, Form 10-Q for the quarter ended 2026-09-26, filed 2026-11-05](https://www.sec.gov/Archives/edgar/data/916365/000091636526000079/tsco-20260926.htm)
  - Stake: "Pursuant to the agreement governing the transaction, the Company acquired 100 % of the equity interest in VIP Petcare for a purchase price of $ 133.8 million" — [same 10-Q](https://www.sec.gov/Archives/edgar/data/916365/000091636526000079/tsco-20260926.htm)
  - Model: "and VIP Petcare, the largest provider of mobile veterinary care in the U.S." — [same 10-Q](https://www.sec.gov/Archives/edgar/data/916365/000091636526000079/tsco-20260926.htm)
  - Count: "Over 2,900 locations at stores like Tractor Supply, Pet Supplies Plus, Pet Food Express and more." — [VIP Petcare, home page, accessed 2026-11-07](https://www.vippetcare.com/)
  - 5% holders: "The Vanguard Group (2) 64,022,615 12.2 % BlackRock, Inc. (3) 48,193,100 9.2 %" (table) — [Tractor Supply, DEF 14A, filed 2026-03-26](https://www.sec.gov/Archives/edgar/data/916365/000119312526126620/d16327ddef14a.htm)
  - Former owner: "Parent and Merger Sub are affiliates of Bansk Group" and "with the Company surviving the Merger as a wholly owned subsidiary of Parent." — [PetIQ, Form 8-K, filed 2024-10-25](https://www.sec.gov/Archives/edgar/data/1668673/000110465924111319/tm2426836d1_8k.htm). The closing date is 2024-10-25.
  - Earlier count: "The Company's national veterinarian service platform operates at over 2,600 community clinic locations and wellness centers hosted at retailers across 39 states providing cost effective and convenient veterinary wellness services." — [PetIQ, Form 10-Q for the quarter ended 2024-06-30](https://www.sec.gov/Archives/edgar/data/1668673/000162828024035782/petq-20240630.htm)
  - Affiliate: none found
- **VT21 Lap of Love Veterinary Hospice**
  - Owner: "a group led by its affiliate, Cortec Group Fund VI, L.P. (“Cortec Fund VI”), in partnership with Co-Founders Dr. Dani McVety and Dr. Mary Gardner, completed the growth recapitalization of Lap of Love Veterinary Hospice (“Lap of Love” or the “Company”)." — [Cortec Group, release (closing date 2020-01-24)](https://cortecgroup.com/cortec-group-announces-partnership-with-lap-of-love-veterinary-hospice/)
  - Model: "The Company does not operate clinics or medical facilities and exclusively provides these services in customers’ homes, where they and their pets tend to be most comfortable." — [same release](https://cortecgroup.com/cortec-group-announces-partnership-with-lap-of-love-veterinary-hospice/)
  - Size: "Lap of Love manages a network of more than 135 veterinarians" (2020) — [same release](https://cortecgroup.com/cortec-group-announces-partnership-with-lap-of-love-veterinary-hospice/)
  - Current: the tile after the "Lap of Love logo" image reads "Fund VIII Owned Healthcare Services" — [Cortec Group, Companies, accessed 2026-11-07](https://cortecgroup.com/companies/). These are page fields.
  - Affiliate: none found
  - Notes: trade press calls Cortec's stake a minority. Cortec's release states no stake, and its tile says "Owned". This framing difference is listed under "Sources disagree".

### Rollups and groups that are not brands
Not counted in the 21 rows. Their hospitals keep local names, or they are parents of rows above. Owner given where a primary or law-firm source was read; otherwise the lead is marked as one.

**Checked (8 large rollups):**
- **National Veterinary Associates (NVA)**: "Our network of 1,000 community hospitals works with pet parents to provide high-quality medicine and an individualized approach to each pet’s care—every day, at every life stage." ([nva.com](https://www.nva.com/)). Owner: not found. nva.com and its About page name no owner. Trade press (Bloomberg Law snippet, 2019) says JAB agreed to buy a majority from Ares and OMERS, with the JAB Consumer Fund supplying most of the equity.
  - **Ethos Veterinary Health** is NVA's specialty and ER network: "Our 140+ hospitals are here for pets and the people who love them—providing evidence-based, compassionate care in life’s most critical moments." ([nva.com](https://www.nva.com/)). Hospital names were not checked. The name is unrelated to the competitor Ethos.
  - **NVA Pet Resorts** (boarding) and **SAGE Veterinary Centers** (NVA per the VIS list) are also NVA's.
- **Mission Pet Health** (Southern Veterinary Partners + Mission Veterinary Partners): "Mission Pet Health is one of the leading veterinary care organizations in the U.S., formed by the merger of Southern Veterinary Partners and Mission Veterinary Partners." ([Shore Capital Partners, portfolio page](https://www.shorecp.com/companies/mission-pet-health)). Owner: Shore Capital Partners (PE). Silver Lake co-investor per Bloomberg (lead). Stake not stated.
- **PetVet Care Centers**: owner not found in a primary source. Trade press says KKR bought it in 2017 and recapitalized it in 2023 (lead).
- **VetCor**: "Realized Portfolio VetCor A veterinary care platform in the U.S." ([Oak Hill, Investments](https://oakhill.com/investments/)). Oak Hill has exited. Current owner not found; trade leads name Harvest Partners and Cressey & Company.
- **Thrive Pet Healthcare (locally named practices, ~334 of 363 locations)**: TSG Consumer Partners, current (VT14). PE.
- **AmeriVet Veterinary Partners**: "On March 7, 2022, AmeriVet Veterinary Partners ("AmeriVet") announced the closing of a US$1.6 billion recapitalization in which funds managed by AEA Investors LP (“AEA”) and a wholly owned subsidiary of the Abu Dhabi Investment Authority (“ADIA”) acquired AmeriVet from Imperial Capital Group (“Imperial Capital”)." ([Torys LLP, transaction page (law-firm page)](https://www.torys.com/work/2022/03/b042f5a9-44c7-40ad-9fba-bff64c4e6a53)). PE (AEA). Current status not reconfirmed.
- **American Veterinary Group (AVG), general practices**: Oak Hill Capital, current (VT6). PE. AVG also runs the UrgentVet banner.
- **Heartland Veterinary Partners**: "Gryphon Investors (“Gryphon”), a San Francisco-based middle-market private equity firm, announced today that it has made a majority investment in Heartland Veterinary Partners (“Heartland” or “the Company”), a leading veterinary support organization in the Mid-American and Southern U.S. markets." and "Tyree & D’Angelo Partners (“TDP”) and management will retain minority stakes alongside Gryphon." ([Gryphon Investors, release dated 2019-12-12](https://www.gryphon-inv.com/news/gryphon-investors-invests-in-heartland-veterinary-partners/)). PE (majority). Current status not reconfirmed.

**Parents of brand rows (not separate list entries):**
- Mars Veterinary Health / Mars, Incorporated (family): Banfield, VCA, BluePearl.
- Petco Health & Wellness Company (CVC, CPP Investments): Vetco.
- Chewy, Inc. (BC Partners consortium): Chewy Vet Care, Modern Animal.
- GoodVets Group LLC (General Atlantic, SkyKnight): GoodVets, WellHaven.
- The merged Bond Vet / Small Door company (owners not stated).
- TAG – The Aspen Group / ADMI Corp. (owners not found): Lovet.
- Tractor Supply Company (public): VIP Petcare.
- PetIQ, Inc. (Bansk Group): former parent of VIP Petcare, now a pet-products company.

**Not checked (named in the VIS 2022 roll call or in searches; owner not researched within the cap):** Veterinary Practice Partners, Community Veterinary Partners, Encore Vet Group, Alliance Animal Health, United Veterinary Care, Rarebreed Veterinary Partners, Lakefield Veterinary Group, CareVet, Innovetive Petcare, BlueRiver Pet Care, Western Veterinary Partners, Veritas Veterinary Partners, Destination Pet, VetEvolve, EverVet Partners, Galaxy Vets, Curo Pet Care, O'Brien Veterinary Group, Valley Veterinary Care, Inspire Veterinary Partners, PetWell Partners, Pathway Vet Alliance (now Thrive). Leads from search snippets only: Revelstoke Capital (Vet's Best Friend, now Rarebreed per VIS).

**PE share among rollups:**
- Of the 8 checked, **5 / 8 (62.5%) are PE-backed per a primary or law-firm source**: Mission Pet Health, Thrive, AmeriVet, AVG and Heartland.
- The other 3 (NVA, PetVet, VetCor) have investment-firm owners in trade-press leads only. That would make it 8 / 8 if confirmed. JAB Consumer Fund Management SARL reported `Any PE Funds = Y` in the pilot's Form ADV check.
- The 22 unchecked rollups are not counted.

### Category share
**Brand rows (N = 21; 19 fixed-site plus VIP Petcare and Lap of Love):**
- **PE-owned (control, or PE owner with no stated stake): 10 / 21 = 47.6%**
  - Vetco (Petco: CVC, CPP Investments; Nasdaq-listed controlled company).
  - Chewy Vet Care and Modern Animal (Chewy: BC Partners consortium; NYSE-listed controlled company).
  - CityVet (RiverGlade Capital).
  - UrgentVet (AVG / Oak Hill Capital).
  - GoodVets and WellHaven (General Atlantic, SkyKnight Capital).
  - Thrive-named clinics (TSG Consumer Partners).
  - Heart + Paw (Whistler Capital Partners).
  - Lap of Love (Cortec Group).
- **PE minority stake: 1 / 21 = 4.8%.** MedVet: Leonard Green minority; 95% of owners are current or retired doctors and employees.
- **PE-owned plus PE minority stake: 11 / 21 = 52.4%.**
- **Family: 3 / 21 = 14.3%.** Banfield, VCA and BluePearl (Mars).
- **Public company: 2 / 21 = 9.5%.** VIP Petcare (Tractor Supply) and Walmart Pet Services (Walmart, Walton family 50.55% combined).
- **Owner type not confirmed: 4 / 21 = 19.0%.**
  - Bond Vet and Small Door: merged 2026-07-09, owners not stated. Warburg Pincus (PE) invested in Bond Vet in 2021, and Valspring Capital led Small Door's 2025 equity.
  - Petfolk: Deerfield-led Series C.
  - Lovet: TAG's owners not found.
- **Not found: 1 / 21 = 4.8%.** VEG ER for Pets.
- **Rows with owner kind settled:** 16 / 21 (76%).
- **Strict count:** 11 / 21 (unchanged). Neither public non-PE row has a 5%+ holder that is an investment firm other than Vanguard and BlackRock (Tractor Supply). Walmart's 5%+ holders are Walton family vehicles.
- **Upper bound if leads were confirmed:**
  - 14 / 21 (66.7%) with Bond Vet, Small Door (Warburg Pincus in the pre-merger chain) and Lovet (TAG: Ares, Leonard Green and American Securities per trade press).
  - 15 / 21 (71.4%) if Petfolk's lead investor Deerfield Management reports PE funds.
  - VEG's named investors (D1 Capital Partners, Fidelity, Durable Capital, Sequoia Heritage) are an open question for Form ADV.
- **Fixed-site rows only (N = 19):** PE-owned plus minority 10 / 19 = 52.6% (Lap of Love drops out).
- **By parent company (16 parents):**
  - PE-owned 8: Petco, Chewy, CityVet, AVG, GoodVets, Thrive, Heart + Paw, Lap of Love.
  - PE minority 1: MedVet.
  - That makes **9 / 16 = 56.3%**.
  - The rest: family 1 (Mars), public 2 (Walmart, Tractor Supply), owner type not confirmed 3 (Petfolk, the merged Bond Vet / Small Door company, TAG), not found 1 (VEG).
- **By fixed-site hospitals (19 rows, 2,901 sites):**
  - PE-owned 724 (25.0%); with MedVet's 40, 764 (26.3%).
  - Mars 1,866 (64.3%).
  - Owner type not confirmed 135 (4.7%); not found 130 (4.5%; VEG's count includes Canada); public 6 (0.2%).
  - The counts mix dates and methods (company statements, sitemap counts, a 2022 count for Lovet, and openings included for UrgentVet and GoodVets), so this is indicative only.
- **By sales:** not computed. Only Petco, Chewy and Tractor Supply report numbers, and they don't break out clinics by brand.
- **Sources disagree (owners):** none.
- **Framing and count differences:**
  - Lap of Love: trade press says "minority"; Cortec's release states no stake and its tile says "Owned".
  - Heart + Paw: the law-firm page title says "Acquires"; its text says "strategic growth investment".
  - WellHaven: seven states (Holland & Knight) vs five (WellHaven site).
  - Counts:
    - BluePearl: 92 (sitemap) vs "over 100" (Mars Veterinary Health);
    - VCA: 774 US (directory) vs "more than 1,000" (Mars Veterinary Health, likely including Canada);
    - GoodVets: 75 (law-firm release) vs 88 clinic pages (sitemap).
- **Formerly PE among non-PE rows:** VIP Petcare (Bansk Group via PetIQ, 2024-10-25 to 2026-05-28).

**Affiliate income:**
- No vet-care brand has a brand-direct affiliate program found (checked with one category-wide search and during owner fetches).
- Parent store-wide programs exist for Chewy and Walmart but are not clinic-specific.
- A network listing exists for The Vets, a mobile vet service that is not a row (FlexOffers/Impact listing seen in search, not verified).
- Telehealth services (Vetster) run affiliate programs, but they are not clinic chains.
- Practically, vet clinics look like a near-zero affiliate category.

## Firms named
Every investment firm named as an owner or 5%+ holder, as the sources name it (for the assembler's Form ADV check):
- **CVC Capital Partners** ("CVC Capital Partners", "CVC Funds", "CVC Pet LP", "CVC B-2 SPV, LLC"); **Canada Pension Plan Investment Board** ("CPP Investments"); vehicles "Scooby Aggregator, LP", "Scooby LP", "9314601 B-2 SPV, LLC" (Vetco)
- **BC Partners** ("BC Partners Advisors LP"; "BCP Stockholder Parties"); **La Caisse de dépôt et placement du Québec**; **GIC Special Investments Pte Ltd**; **StepStone Group LP**; **Longview Asset Management, LLC** (Chewy Vet Care, Modern Animal)
- **RiverGlade Capital** (CityVet)
- **Oak Hill Capital** (AVG / UrgentVet; former VetCor holder); **Oak Hill Advisors (OHA)** is a lender to MedVet, not an owner
- **Trive Capital**; **Latticework Capital Management** (former AVG owners)
- **General Atlantic**; **SkyKnight Capital, L.P.** (GoodVets, WellHaven; SkyKnight also an earlier MedVet investor)
- **Martis Capital** (former WellHaven owner)
- **Leonard Green & Partners, L.P.** (MedVet minority)
- **Goldman Sachs Merchant Banking Division** ("entities affiliated with"); **Stonehenge Partners** (MedVet 2019 investors)
- **TSG Consumer Partners** (Thrive)
- **Whistler Capital Partners** ("Whistler Capital") (Heart + Paw)
- **Cortec Group** ("Cortec Group Fund VI, L.P."; tile now reads "Fund VIII") (Lap of Love)
- **Warburg Pincus**; **Talisman Capital** (Bond Vet, pre-merger)
- **Valspring Capital**; **Primary Venture Partners**; **C&S Family Capital**; **Lerer Hippeau**; **Toba Capital** (Small Door, pre-merger)
- **Deerfield Management**; **Movendo Capital**; **White Star Capital**; **Cutting Horse VC**; **Idea Farm Ventures**; **Parkview International** (Petfolk)
- **Bansk Group** (former PetIQ / VIP Petcare owner)
- **Shore Capital Partners** (Mission Pet Health)
- **Gryphon Investors**; **Tyree & D’Angelo Partners** (Heartland)
- **AEA Investors LP**; **Abu Dhabi Investment Authority** (AmeriVet); **Imperial Capital Group** (former AmeriVet owner)
- 5%+ holders of public rows: **The Vanguard Group**, **BlackRock, Inc.** (Tractor Supply); **Walton Enterprises, LLC**, **Walton Family Holdings Trust** (Walmart; family vehicles)
- Leads only (search snippets or trade press, not cited, not counted): JAB Holding / JAB Consumer Fund, Ares Management and OMERS Private Equity (NVA 2019); KKR and Blue Owl (lender) (PetVet); Silver Lake (Mission Pet Health); Harvest Partners and Cressey & Company (VetCor); Ares Management, Leonard Green & Partners and American Securities (TAG); D1 Capital Partners, Fidelity Management & Research Company LLC, Durable Capital Partners LP and Sequoia Heritage (VEG); Revelstoke Capital (Vet's Best Friend).

## Worker log
- **Time:** start 2026-11-07T17:24:25Z, end about 2026-11-07T18:01Z: about 37 minutes wall-clock for 21 rows plus the rollup pass, including writing and a quote self-check.
- **Requests:**
  - WebSearch: 35.
  - WebFetch: 2. One read marsveterinary.com, which returned 403 to curl. The other tried VEG's 2021 Business Wire release and got 403.
  - Direct HTTP (curl): 131 logged requests (42 of them robots.txt reads). 16 went to SEC (submissions JSON ×5, documents ×11), all HTTP 200 except one mistyped URL (404, then corrected), under the contact-free user agent at ≤2 req/s.
  - Status mix: 121 × 200, 3 × 403 (marsveterinary.com robots.txt and page; warburgpincus.com Cloudflare), 6 × 404 (four guessed pages, wellhavenpethealth.com's missing robots.txt, one SEC typo), 1 × no response (oakhillcapital.com, a wrong host; the firm is at oakhill.com).
  - Agent tokens: not metered by this worker.
- **What was fast:**
  - Public parents. Seven SEC documents settled Vetco, Chewy Vet Care, Modern Animal, VIP Petcare and Walmart Pet Services (5 rows), with mechanically checkable quotes.
  - Server-rendered sponsor pages: TSG, Leonard Green, Oak Hill (current vs realized), RiverGlade (filter classes), Cortec (tile status), Shore and Gryphon. Each settled a row in 1–2 requests.
  - Brand sitemaps and location directories (VCA, BluePearl, MedVet, Bond Vet, GoodVets, Petfolk, Modern Animal, Small Door, CityVet) gave site counts in 1–2 requests each where no ranking exists.
- **What made brands slow:**
  1. **No ranking, and the brand rule.** No free, current list ranks vet brands. The available lists rank owner groups, and most groups are rollups with local names. The candidate set had to be rebuilt brand by brand, and Thrive had to be split by sitemap slugs.
  2. **Venture and growth rounds instead of buyouts.** Bond Vet, Small Door, Petfolk and VEG raised rounds with named leads but no stated owner. A merger (Bond Vet / Small Door) then erased even the investor picture.
  3. **2026 deals:** Modern Animal to Chewy, VIP Petcare to Tractor Supply, Bond Vet with Small Door, and WellHaven to GoodVets. Each made a lead or ranking stale and needed a fresh primary source.
  4. **Releases on Business Wire (403)** (VEG, Small Door, GoodVets / WellHaven, SkyKnight / GoodVets 2021) forced law-firm pages or left the fact unsettled.
  5. **Blocked or robots-disallowed sites:** marsveterinary.com (403), warburgpincus.com (Cloudflare), heartandpaw.com (disallows ClaudeBot), fairground.run (disallows ClaudeBot). JavaScript-only pages: thrivepetcare.com locations, medvet.com locations, modernanimal.com location list.
- **Which kinds of brands had no primary source for the owner:**
  - founder-led emergency chains funded by growth rounds whose only release is on Business Wire (VEG);
  - venture-backed de novo brands whose releases name round leads but never an owner (Petfolk, Small Door, and Bond Vet after its merger);
  - brands of a private parent whose own owners are stated only in trade press (Lovet under TAG);
  - among rollups, the biggest private owner-groups whose sponsor pages render by JavaScript or don't name them (NVA / JAB, PetVet / KKR, VetCor after Oak Hill's exit).
- **Quote self-check:** a script re-extracted the text of every saved page (tags stripped, entities decoded, whitespace collapsed, curly quotes and dashes normalized, case-sensitive) and matched 80 cited quotes from curl'd pages. **80 of 80 were found.** Two altered quotes were added as a negative control (Chewy "…clinics to 19." and Oak Hill "a Boston-based…"), and both failed, so the check can fail. Not covered: the two WebFetch quotes (VT2, VT7), the meta description (VT14), page fields and sitemap counts.
- **Quote caveats for the assembler:**
  - VT2 and VT7 quote marsveterinary.com through the WebFetch summarizer (truncated with "..."), so they will fail a strict match.
  - VT14 quotes a meta description.
  - Several items are counts of sitemap or directory entries, or page fields (TSG and Cortec tiles, the RiverGlade filter class), not sentences.
  - SEC table cells are whitespace-normalized ("64.4 %", "12.2 %").
  - A few PR Newswire and SEC sentences contain a stray space where tags split the HTML (for example "100 %", "$ 133.8 million"). They are quoted as rendered.
