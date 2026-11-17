# PE consumer scan, worker 1: large diversified firms

Ticket: [82 Research: Where PE owns consumer brands](../../issues/82-research-where-pe-owns-consumer-brands.md) · Worker report, 2026-11-16, saved by the parent session as returned (subagents could not write files), with each firm's company lines grouped by industry. Per-firm notes, a TSV and raw downloads were kept in the session scratchpad (temporary). "Current" counts are what each page shows. `L` = locations keep local names, judged from how the firm's page describes the company, not verified location by location; `?` = likely but less clear.

Read all 22 firms' own sites; 15 have a usable portfolio list, 7 have none readable (Apollo, Blackstone, Bain, Brookfield, Ares, Goldman Sachs, Partners Group). **147 distinct US consumer-facing companies** (167 firm listings).

## 1. Per firm

**KKR** | https://www.kkr.com/invest/portfolio | read: the list loads only by JavaScript, so it was rendered in the browser using the page's own URL filters (`?industry=industry:consumer-discretionary&country=location:americas`), no clicks | 300 listed, current "as of August 24, 2026" (PE, growth, impact, infrastructure); 56 PE in the Americas | 9
- eyewear: 1-800 Contacts · gyms: Bay Club · home services: Groundworks (L); Neighborly (Mr. Rooter, Molly Maid etc.)
- restaurants: Nothing Bundt Cakes · school and cheer products: Varsity Brands · home health and hospice: BrightSpring Health Services
- dental care: Heartland Dental (L) · veterinary care: PetVet (L)

**Apollo** | https://www.apollo.com/strategies/asset-management/equity/private-equity | no list ("190+ Portfolio Companies, as of September 30, 2026", 3 case studies) | 1 featured: The Venetian Resort Las Vegas (casinos and resorts)

**Blackstone (private equity)** | https://www.blackstone.com/our-businesses/private-equity/ | no list (no portfolio page in the sitemap; 7 featured) | 2 featured: Jersey Mike's (restaurants); Ancestry (consumer apps)

**Carlyle** | https://www.carlyle.com/portfolio | read (plain fetch got a Cloudflare challenge; cleared by itself in one browser render, no clicks) | 245 listed: 150 Current, 95 Exited | 6
- packaged food: Arctic Glacier (packaged ice) · pet products: Compana Pet Brands · personal care products: Every Man Jack
- footwear: Golden Goose (Italian, US stores) · sporting goods: Dainese (Italian, US stores) · home furnishings: Flos B&B Italia (US showrooms)

**TPG** | https://www.tpg.com/portfolio | read (embedded data, "Select Investments") | 273 listed: 170 Active + 4 Partially Realized = 174 current, 97 Realized | 23
- gyms: Crunch Fitness (TPG still lists it Active; LGP lists it Current too); Life Time (LGP too)
- restaurants: Mendocino Farms; Philz Coffee · urgent care: GoHealth Urgent Care · behavioral health: LifeStance Health; Banyan Treatment Centers
- dental care: Blue Cloud Pediatric Surgery Centers · golf: Troon (L; LGP too) · travel: Viking Cruises; Airbnb
- beauty and cosmetics: Ipsy (BFA Industries) · packaged food: SmartSweets; LiveKindly; Little Leaf Farms · sporting goods: Rad Power Bikes
- senior living: Enlivant · home health and hospice: Kindred Healthcare · consumer apps: Calm
- education and tutoring: Age of Learning (ABCmouse); Prodigy Education · pay TV: DirecTV · home services: Palmetto (residential solar)

**Warburg Pincus** | https://warburgpincus.com/investments/ | read in a browser after a Cloudflare challenge that cleared by itself; names from each logo card's link | 185 cards, "active investments as of September 2026" (the firm says 225+ active) | 6
- veterinary care: Bond Vet · oil change and auto service: Big Brand Tire & Service · car washes: El Car Wash
- dental care: MB2 Dental (L); Paradigm Oral Health (L) · consumer apps: OfferUp

**General Atlantic** | https://www.generalatlantic.com/investments/?status=Current | read (10 pages via `pg=`) | 237 Current | 28
- restaurants: Blank Street; Torchy's Tacos; Joe & The Juice · beverages: Athletic Brewing
- apparel brand licensing: Authentic Brands Group (Reebok, Brooks Brothers, Forever 21 etc.)
- personal care products: Buff City Soap; Grove Collaborative · beauty services: European Wax Center · beauty and cosmetics: FORMA Brands; OSEA; Kayali
- home services: Flint Group (L?) · veterinary care: GoodVets · pet care services: Village Pet Care (L?) · pet food: Open Farm
- wellness studios: Restore Hyper Wellness · athletic apparel: Vuori; Gymshark · children's apparel: PatPat · women's apparel: SHEIN; Sézane
- behavioral health: ACES (autism therapy) · physical therapy: PT Solutions · urology: U.S. Urology Partners (L) · primary care: Suvida Healthcare
- consumer apps: Chess.com; Flo Health · education and tutoring: Quizlet

**Bain Capital (private equity)** | baincapital.com/portfolio | unreadable: 404, and neither the menu nor the sitemap has a portfolio or private equity page

**Advent International** | https://www.adventinternational.com/investments/ | read (crawl-delay 10 respected), but an all-time directory with no current/exited marker (only Sovos links an exit release, "Campbell to acquire Sovos Brands") | 455 all-time | 8 US consumer companies invested 2016–2026, status not shown
- personal care products: Salt & Stone · packaged food: Sauer Brands · beauty and cosmetics: Orveon (bareMinerals, BUXOM, Laura Mercier); Olaplex
- restaurants: First Watch · physical therapy: ATI Physical Therapy · home health and hospice: AccentCare · travel retail: Avolta (Hudson airport stores)
- non-US brands with US stores, not counted: ZIMMERMANN, Parfums de Marly/INITIO, Vestacy (Air Wick and other Reckitt home brands)

**Platinum Equity** | https://www.platinumequity.com/our-companies/ | partly read: the grid loads by JavaScript over 3 pages and the render showed only page 1; the page says "current portfolio of ~60 companies" and `our_companies-sitemap.xml` lists 59 company pages, used as the list (status not marked) | about 59 | 7
- packaged food: Horizon Organic · school and cheer products: Jostens · sporting goods: GSM Outdoors · sewing machines: SVP Worldwide (Singer, Pfaff, Husqvarna Viking)
- golf: Club Car · sports teams: Pistons Sports & Entertainment · video games: WorldWinner (a "Winc" page exists, unclear, not counted)

**H.I.G. Capital** | https://hig.com/portfolio/ | read (status classes) | 382 listed: 167 Active, 215 Realized | 14
- dental care: Advanced Dental Brands (L) · eye care: American Vision Partners (Barnet Dulaney Perkins, Southwestern Eye) (L) · physical therapy: CORA Physical Therapy
- women's apparel: Cuyana; Lulus · jewelry: GLD · consumer apps: Classmates · bowling and family entertainment: Family Entertainment Group
- online health retail: Health-E Commerce (FSA Store, HSA Store) · home improvement products: Homewerks · gastroenterology: Pinnacle GI Partners (Center for Digestive Health) (L)
- home warranty: Rely Home · travel: Shore Excursions Group · home services: Windows USA

**Leonard Green & Partners** | https://www.leonardgreen.com/portfolio/ | read ("Status: Current/Past") | 108 listed: 71 Current, 37 Past | 24
- eyewear: 1-800 Contacts (KKR too) · dental care: The Aspen Group (Aspen Dental, ClearChoice, WellNow Urgent Care, Chapter Aesthetic Studio)
- apparel brand licensing: Authentic Brands Group · collision repair: Caliber Collision · gyms: Crunch; Life Time · dermatology: Epiphany Dermatology
- crafts retail: JOANN (page says Current; the worker believes JOANN closed its stores in 2025, unverified) · toys: Lakeshore Learning · veterinary care: MedVet
- beauty services: Milan Laser Hair Removal · behavioral health: Mindpath Health · car washes: Mister Car Wash · personal care products: PDC Brands
- home furnishings: The Shade Store; Visual Comfort & Co. · oil change and auto service: Sun Auto Tire & Service · golf: Topgolf; Troon (L)
- restaurants: Union Square Hospitality Group; Velvet Taco; Zaxby's · home services: West Shore Home; The Wrench Group (L)

**Hellman & Friedman** | https://hf.com/our-portfolio/ | read | 80 unique: 29 Current, 51 Past | 2
- collision repair: Caliber Collision · auto glass repair: Belron (Safelite AutoGlass in the US; minority stake)

**Clayton, Dubilier & Rice** | https://www.cdr.com/portfolio | read (current-only list, no status field) | 42 | 7
- greeting cards: American Greetings · pet products: PetSafe Brands · packaged food: Shearer's Foods · auto glass repair: Belron (Safelite)
- home health and hospice: Gentiva · primary care: Mosaic Health (MPG, CareMore) · OTC health products: Opella (Sanofi's consumer health products)

**Brookfield (private equity)** | https://www.brookfield.com/our-businesses/private-equity | no full list ("Portfolio highlights", about 11 companies, all B2B or industrial; GEMS schools are in the Middle East; a podcast title mentions Spring Education Group, not counted) | 0

**Ares (private equity)** | https://www.aresmgmt.com/our-business/private-equity | read in a browser after a challenge that cleared by itself; no list ("~100 Global portfolio company investments") | 0

**Goldman Sachs Asset Management (private equity / West Street)** | unreadable: goldmansachs.com returned "Access Denied" (Akamai) to the bot, not retried; the am.gs.com sitemap has only product and insight pages | 0

**EQT** | https://eqtgroup.com/about/current-portfolio | partly read: 271 current entries embedded (no exit dates), the rest load by JavaScript; the sitemap's 642 company pages include divested companies; most of the 271 are venture and life-science funds | 271 shown | 2
- private schools: IMG Academy; Nord Anglia Education (has US schools)

**CVC** | https://www.cvc.com/portfolio/our-portfolio/ | read (9 pages via `?page=N`; "invested in over 150 companies") | 156 | 9
- pet stores: Petco · personal care products: Arthēa (formerly PDC Brands; LGP lists it as PDC Brands) · apparel brand licensing: Authentic Brands Group
- beverages: Lipton Teas & Infusions (Lipton, TAZO, Pukka) · consumer apps: Chess.com (GA too) · jewelry: Breitling (watches)
- consumer electronics: Razer · men's apparel: A Bathing Ape (BAPE) · video games: Dream Games and Jagex

**Partners Group** | unreadable: Cloudflare "Sorry, you have been blocked" (a block, not a challenge; no retry)

**BC Partners** | https://www.bcpartners.com/portfolio/?strategy=private-equity&investment_status=unrealised (plus region filters) | partly read (Europe page 2 not delivered without JavaScript) | 23+ current (6 unrealised in North America, 12+ in Europe, 5 partially realised or public) | 4
- pet stores: PetSmart; Chewy (partially realised / public) · women's health: Women's Care Enterprises (L?) · pet products: PetLab Co (UK, sells direct in the US)

**Apax** | https://www.apax.com/partnerships/ | partly read: the status filter works only by JavaScript (`?status=current` ignored) and the full alphabetical list (~200) has no status, so "Deal status" was read on 17 detail pages | current count not readable | 15 Current (FullBeauty and ClassPass show Realised)
- home services: Authority Brands; SavATree · child care: Cadence Education (L) · footwear: Cole Haan · weight loss: Ideal Protein
- senior living: InnovAge (PACE senior care) · pet food: Nulo · behavioral health: Eating Recovery Center · home warranty: Oncourse Home Solutions
- beverages: Far Niente; Ole Smoky · education and tutoring: Revolution Prep · packaged food: Bazooka Candy Brands (Ring Pop, Push Pop)
- home furnishings: At Home · women's apparel: Moda Operandi

## 2. Tally (distinct companies per label)

- restaurants 11; home services 9; packaged food 8; dental care 6; beauty and cosmetics 6; consumer apps 6; personal care products 5; behavioral health 5; women's apparel 5; beverages 4; education and tutoring 4; home furnishings 4; home health and hospice 4; veterinary care 4.
- 3 each: gyms (Bay Club; Crunch and Life Time each on TPG and LGP), golf (Troon, Topgolf, Club Car), pet stores (Petco, PetSmart, Chewy), pet products, physical therapy (PT Solutions, ATI, CORA), sporting goods, travel.
- 2 each: athletic apparel, beauty services (European Wax Center, Milan Laser), car washes (El Car Wash, Mister Car Wash), footwear, home warranty, jewelry, oil change and auto service (Big Brand Tire, Sun Auto), pet food, primary care, private schools, school and cheer products, senior living, video games.
- one company held by several firms: Authentic Brands (GA, LGP, CVC), Caliber (LGP, H&F), Belron/Safelite (H&F, CD&R), 1-800 Contacts (KKR, LGP).
- 1 each: urgent care, dermatology, eye care, gastroenterology, urology, women's health, weight loss, wellness studios, child care, bowling and family entertainment, casinos and resorts, toys, crafts retail, greeting cards, OTC health products, consumer electronics, sewing machines, sports teams, travel retail, pay TV, online health retail, home improvement products, children's apparel, men's apparel, pet care services.
- Rollups marked L: Groundworks, Heartland, PetVet, Troon, MB2, Paradigm, Advanced Dental Brands, American Vision Partners, Pinnacle GI, Wrench Group, U.S. Urology Partners, Cadence Education; less certain: Flint Group, Village Pet Care, Women's Care.

## 3. Notes

- Not fully read: no list at all (Bain 404; Apollo, Blackstone, Brookfield, Ares featured companies or a count only); blocked, not retried (Partners Group Cloudflare block; Goldman Sachs Akamai "Access Denied"); partial (Advent all-time list without status; Platinum sitemap as list; EQT 271 embedded entries; BC Partners Europe page 2 missing; Apax current count unknown). Carlyle, Warburg and Ares sent a Cloudflare challenge to the plain fetcher; each cleared by itself in one browser render, no clicks.
- Rules: robots.txt checked on every host for `EvidenceEngine` and `*`; crawl-delay 10 honoured (Advent, H.I.G., LGP); every other host under 1 request per second. The session's auto-mode safety check refused a direct fetch of the JSON feed KKR's portfolio page itself calls; the worker didn't try to get around that and used the page's own URL filters in the browser instead.
- Surprises: consumer packaged goods are a big unmeasured group (packaged food, beverages, personal care, beauty); other unmeasured clusters: behavioral health, home health and hospice, specialty physician-practice rollups (dermatology, eye care, gastroenterology, urology, women's health), consumer subscription apps, home furnishings, education and tutoring, home warranty, private schools. Several companies sit on more than one firm's page (Authentic Brands, Caliber, Safelite, Troon, Life Time, Crunch, 1-800 Contacts, Chess.com, PDC Brands/Arthēa): co-owners, or listings one firm never took down. Possibly stale: LGP's JOANN, TPG's Crunch (LGP also lists it), Apax's At Home.
- Cost: about 70 minutes; about 165 HTTP requests (132 page and sitemap fetches plus 25 robots.txt) and 10 browser renders; roughly 0.4M tokens.
