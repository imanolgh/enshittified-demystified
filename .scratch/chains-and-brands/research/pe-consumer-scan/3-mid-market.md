# PE consumer scan, worker 3: mid-market generalists

Ticket: [82 Research: Where PE owns consumer brands](../../issues/82-research-where-pe-owns-consumer-brands.md) · Worker report, 2026-11-16, saved by the parent session as returned (subagents could not write files), with each firm's company lines grouped by industry. Raw downloads and parsing scripts were kept in the session scratchpad (temporary). `L` = the company's own page says its locations keep local names; `L?` = looks like a rollup but the page doesn't say.

Read 17 of 22 sites in full; two partly readable, three unreadable, and BDT & MSD has no portfolio page. **101 consumer-facing current listings, 100 unique companies** (Sevita on both MDP and Centerbridge). Biggest groups: home services 10, broadband internet 6, packaged food 6, behavioral health 5, home care 5.

## 1. Per firm

**The Riverside Company** | https://www.riversidecompany.com/investment-portfolios | read (records embedded in the page's JS, status "current" or "exited") | 136 current | 7
- home care: Best Life Brands (franchisor: in-home care, senior care placement, estate sales); Evive Brands (non-medical home care franchisor)
- hair salons: Head to Toe Brands (Bishops salons)
- home services: Threshold Brands (home service franchise); T3 Services Group (support to residential HVAC, plumbing, electrical) (L?)
- athletic apparel: Elite Sportswear (gymnastics and cheer apparel) · packaged food: NuStef Baking (pizzelle cookies, crackers)
- skipped: Western Botanicals (supplement contract manufacturer), Wondr Health (employer-paid), Wall Street Prep

**Summit Partners** | https://www.summitpartners.com/portfolio | read (sorted by date, 100 per page; pages 1–4 read, stopped when page 3 had 1 current and page 4 none) | 114 current | 15
- collision repair: CollisionRight · dialysis: U.S. Renal Care (330+ facilities) · primary care (senior): Leon Medical Centers (Medicare Advantage centers, Miami)
- allergy clinics: AllerVie Health (L?) · cardiology: US Health Partners (L?) · behavioral health: LifeStance Health; Blended Health (Connections Wellness Group)
- golf: Club Champion (60+ fitting studios) · restaurants: Philz Coffee
- women's apparel: a.k.a. Brands (Culture Kings, Princess Polly, Petal & Pup, Rebdolls) · eyewear: Quay Australia
- home furnishings: Brooklinen; Fracture (photo prints on glass) · personal care products: Hairstory (New Wash) · home security: Vivint Smart Home (page still says "Current")
- consumer software, not counted: onX, MUBI, Output. Skipped: Snap Finance (financial); Lingoda, Veepee, DERMANOVIS, Deine Urologie (not US)

**Clearlake Capital** | https://clearlake.com/portfolio/ | unreadable: a plain fetch gets a Cloudflare "Just a moment..." challenge (robots.txt allows everything); one browser retry cleared the challenge by itself, but the body read "403 Error / Something went wrong", so no portfolio content was served.

**Searchlight Capital** | https://searchlightcap.com/portfolio/ | read (status in each card's data-slug) | 25 current | 5
- apparel: Roots (Canada-based, sells online in the US) · home care: Care Advantage · postsecondary education: Arizona College of Nursing
- broadband internet: Fidium; All Points Broadband
- skipped: Netspend (prepaid cards), TelevisaUnivision (ad-supported media), Cengage

**Madison Dearborn Partners** | https://www.mdcp.com/portfolio (/filter/portfolio?status=current) | read | 27 current | 3
- home care: CareRing Health · disability services: Sevita Health (home and community services) · broadband internet: Fastwyre Broadband
- skipped: Asurion (insurance), MoneyGram (financial), Performance Health (sells mainly to clinicians)

**GTCR** | https://www.gtcr.com/investments/ | read (plain fetch hit a Sucuri JS challenge; one browser visit cleared by itself) | 54 current | 10
- dermatology: AQUA Dermatology (Florida, Georgia) · autism therapy: Caravel Autism Health · home security: SimpliSafe
- home services: Senske Services (lawn and pest) · wireless phone service: Consumer Cellular
- broadband internet: Point Broadband; Mega Broadband Investments; Visionary Broadband
- outdoor gear: Tactacam · event tickets: Vivid Seats
- not checked: Avryo Healthcare, Harpula, Equiti, Regatta Medical (descriptions load only on a tab click). Skipped: Dentalcorp (Canada only)

**Kelso & Company** | https://www.kelso.com/investments | read | 21 current | 2
- packaged food: Eagle Foods (Hamburger Helper, Suddenly Salad, Eagle, Magnolia, G.H. Cretors, Popcorn Indiana)
- OTC health products: Foundation Consumer Brands (seven OTC brands: nasal strips, children's cough and cold, oral pain relievers)

**The Jordan Company (TJC)** | https://tjclp.com/our-portfolio/ | read | 54 current | 6
- restaurants: Bojangles · dental care: Dental365
- home services: Heartland (HVAC, plumbing, electrical) (L?); Ned Stevens (gutter cleaning)
- outdoor gear: Camco (outdoor and RV products) · wedding venues: Wedgewood Weddings
- skipped: Parts Authority (mostly trade), Sunny Sky (foodservice), Allure Beauty Concepts (contract manufacturer), Bruin, Legion Sports

**TowerBrook Capital Partners** | https://www.towerbrook.com/investments/ | read (data-status active or prior) | 61 active | 10
- women's apparel: J.Jill · gyms: Ignite Fitness (Planet Fitness franchisee, 140+ gyms) · home health and hospice: Compassus
- physical therapy: PT Solutions · medical imaging: Solis Mammography · surgery centers: Regent Surgical Health (L?)
- packaged food: Amylu Foods; Demakes Enterprises · personal care products: Rael (feminine care, skincare) · water vending: FreshPure (filtered-water vending in grocery stores)
- skipped (not US): AA, Azzurri (Zizzi, ASK Italian), IZIPIZI, La Maison Bleue

**Centerbridge Partners** | https://www.centerbridge.com/private-equity | read, but status unclear ("Select Private Equity Investments" with no current/exited marker; includes BFF Banking, which IPO'd in 2017) | 29 listed | 7, status unknown
- hotels and resorts: Great Wolf Resorts · water treatment: Culligan · home care: Help at Home · behavioral health: Mindpath Health
- disability services: Sevita (also MDP) · dental care: Specialty1 Partners (endodontics, oral surgery, periodontics) (L?) · household products: KIK (pool and spa chemicals, household products)
- skipped: GoHealth, Versant Health, auxmoney, Fairstone, First National Bank of America, American Bath Group

**JLL Partners** | https://www.jllpartners.com/our-companies/ | read (filter tag "active-investments") | 21 active | 3
- behavioral health: Hightop Health (outpatient mental health) (L?); Odyssey Behavioral Healthcare · postsecondary education: Ross Education (allied-health career schools)

**BDT & MSD Partners** | https://bdtmsd.com/ | no portfolio page (the sitemap has 5 URLs: home, solutions, two bios, one news item)

**Investcorp (US private equity)** | https://www.investcorp.com/assest-class/north-america/ (2 pages) | read, no status marker | 15 listed | 0 (Health Plus Management manages physical-medicine practices, B2B; BCTS does commercial HVAC)

**Bregal Partners** | www.bregalpartners.com | unreadable: over HTTPS the site serves a `*.bluehost.com` certificate that doesn't match; over HTTP robots.txt says "User-agent: * / Disallow: /". bregal.com describes it as "consumer and multi-unit, food and beverage, and business services" but lists no companies. Likely the firm that matters most for this ticket.

**Bregal Sagemount** | https://www.sagemount.com/portfolio/ | partly readable: a JS search app; a browser render shows only the first 15 entries (A–C) with no status, and the status filter and paging need clicks. Visible, status unknown: Bite Squad, Allen Media Group. None counted.

**Triton** | https://www.triton-partners.com/portfolio (3 pages) | read | 50 current | 0 (only US companies: Acre Security, ProDriven (Werner ladders, sold to professionals), Wavelynx)

**Bridgepoint** | https://www.bridgepointgroup.com/our-portfolio | unreadable: a plain fetch gets a "Challenge Validation" page; in the browser, robots.txt returned a hard "Access Denied", so the site was left.

**American Securities** | https://www.american-securities.com/companies/ (default filter "Status: Current") | read | 22 current | 4
- dental care (also urgent care, veterinary care, aesthetics): The Aspen Group (Aspen Dental, ClearChoice Dental Implant Centers, WellNow Urgent Care, AZPetVet, Chapter Aesthetic Studio)
- child care: Learning Care (11 brands incl. La Petite Academy, Childtime, Tutor Time, Everbrook Academy, The Children's Courtyard, Montessori Unlimited)
- kitchen appliances and personal care: Conair (Cuisinart, Conair, Babyliss, Scunci, Waring) · medical imaging: SimonMed
- skipped: FullBloom (serves school districts), BELFOR, RealManage, ViaPath, NAPA

**Harvest Partners** | https://harvestpartners.com/portfolio-investments/ | read ("SELECT INVESTMENTS", data-status) | 38 current | 7
- massage and spas: Hand & Stone · child care: The Learning Experience · veterinary care: VetCor (L?)
- restaurants: Tacala (Taco Bell franchisee); OTG (airport restaurants) · home services: Power Home (remodeling) · outdoor apparel: KUIU
- skipped: Integrity Marketing Group, Mercer Advisors, Best Trash

**Audax Private Equity** | https://audaxprivateequity.com/portfolio | partly readable: only the 20 most recent investments (2023–2026) render; the rest sit behind "Load More", which needs a click | 20 shown, all Active | 2
- oil change and auto service: Strickland Brothers (Audax Strategic Capital, minority; controlled by Princeton Equity Group)
- child care: The Gardner School (Strategic Capital, minority; controlled by Quad Partners and Vistria)

**New Mountain Capital** | https://www.newmountaincapital.com/our-strategies/private-equity/portfolio/ | read (data-status) | 47 current (35 flagship control, 6 non-control, 6 continuation vehicles) | 7
- home services: Horizon Services ("supports strong, local brands") (L); HomeX (GEM Plumbing and Heating, Haller Enterprises; non-control) (L)
- car washes: Summit Wash Holdings · dental care: Sonrava Health (continuation vehicle) · sporting goods: Rawlings · supplements: Jarrow · beauty and cosmetics: Topix Brands (DermaE, ClarityRx)

**Trilantic North America** | https://www.trilanticnorthamerica.com/portfolio | read (Unrealized or Realized) | 24 unrealized | 7
- gyms: Taymax Group (Planet Fitness franchisee) · veterinary care: Rarebreed Veterinary Partners (L?) · home services: Strada Services (residential HVAC and electrical) (L?)
- grills: Traeger · beauty and cosmetics: Dime Beauty · household products: Gorilla Commerce (Gorilla Grip, Hills Point Industries) · residential solar: ION Solar
- not counted: Sunrise Strategic Partners ("consumer brand accelerator", no brands named), Orva

**Wind Point Partners** | https://www.wppartners.com/companies/ | read (active or realized) | 30 active | 6
- outdoor gear: RTIC (coolers, drinkware) · beverages: good2grow (kids' drinks)
- packaged food: Monarca Food Solutions (Hispanic snacks); Tropicale Foods (Hispanic frozen treats)
- pet products: Targeted PetCare (litter, treats, dental chews) · home services: Turf Masters Brands (residential lawn care)
- skipped: Assisi Pet Care (UK), Voyant Beauty and Stir Foods (contract manufacturers), FreshEdge (distributor)

## 2. Tally (100 unique companies)

| Industry | Count | Companies |
|---|---|---|
| home services | 10 | Threshold Brands, T3 Services Group, Senske, Heartland, Ned Stevens, Power Home, Horizon Services, HomeX, Strada Services, Turf Masters |
| broadband internet | 6 | Fidium, All Points Broadband, Fastwyre, Point Broadband, Mega Broadband, Visionary Broadband |
| packaged food | 6 | NuStef, Eagle Foods, Amylu, Demakes, Monarca, Tropicale |
| behavioral health | 5 | LifeStance, Blended Health, Mindpath, Hightop, Odyssey |
| home care | 5 | Best Life Brands, Evive Brands, Care Advantage, CareRing, Help at Home |
| dental care | 4 | Aspen Group, Dental365, Specialty1, Sonrava |
| restaurants | 4 | Philz Coffee, Bojangles, Tacala, OTG |
| child care | 3 | Learning Care, The Learning Experience, The Gardner School |
| outdoor gear | 3 | Tactacam, Camco, RTIC |
| apparel, other | 3 | Roots, Elite Sportswear, KUIU |
| 2 each | | medical imaging (SimonMed, Solis); veterinary care (VetCor, Rarebreed; plus AZPetVet inside Aspen Group); gyms (Ignite Fitness, Taymax, both Planet Fitness franchisees); home security (Vivint, SimpliSafe); home furnishings (Brooklinen, Fracture); personal care products (Hairstory, Rael); beauty and cosmetics (Topix, Dime); women's apparel (a.k.a. Brands, J.Jill); household products (KIK, Gorilla Commerce); postsecondary education (Arizona College of Nursing, Ross Education) |

One each (31): disability services (Sevita), collision repair, dialysis, primary care (senior), allergy clinics, cardiology, golf, eyewear, hair salons, physical therapy, surgery centers, home health and hospice, dermatology, autism therapy, water vending, wireless phone service, event tickets, OTC health products, wedding venues, hotels and resorts, water treatment, kitchen appliances and personal care, massage and spas, car washes, sporting goods, supplements, grills, residential solar, beverages, pet products, oil change and auto service.

## 3. Notes

- Unreadable or partly readable: Clearlake, Bridgepoint and Bregal Partners unreadable (Bregal Partners is the consumer and multi-unit specialist); Bregal Sagemount, Audax and Centerbridge partly readable or without status; BDT & MSD publishes no portfolio.
- Surprises: healthcare providers are the largest cluster overall (about 30 companies); rural broadband (6 consumer ISPs bought by buyout firms); packaged food, behavioral health and home care all large; Planet Fitness franchisees twice (TowerBrook, Trilantic); Taco Bell and airport food operators (Harvest); dental (Aspen Group, Sonrava, Specialty1) and child care keep coming up.
- Judgment calls: consumer ISPs, residential solar and water vending counted as consumer-facing; consumer apps (onX, MUBI, Output) and consumer finance or insurance (Snap Finance, Netspend, Asurion, GoHealth) left out; most `L?` marks are guesses the page doesn't confirm (only HomeX and Horizon stated).
- **Process incidents** (reported by the worker): Bregal Partners, one HTTP request to the homepage went out in the same command as the robots.txt read, before the worker saw "Disallow: /"; the response was deleted unread and nothing from it was used. Audax, a POST to the site's own search API was denied by the permission system and never sent, so the Audax list stays partial.
- Cost: about 51 minutes; about 105 requests (63 page fetches, 28 robots.txt reads, about 4 curl checks, 11 browser visits), at least 1.1 seconds apart per site; roughly 250k tokens.
