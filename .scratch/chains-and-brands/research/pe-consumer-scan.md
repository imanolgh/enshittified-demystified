# Research: Where PE owns consumer brands (bottom-up scan)

Ticket: [82 Research: Where PE owns consumer brands](../issues/82-research-where-pe-owns-consumer-brands.md) · Step 1 run 2026-11-16 by four background workers, assembled by the parent session. Worker reports with every firm's list: [1 large diversified](pe-consumer-scan/1-large-diversified.md), [2 consumer-focused](pe-consumer-scan/2-consumer-focused.md), [3 mid-market](pe-consumer-scan/3-mid-market.md), [4 services and healthcare](pe-consumer-scan/4-services-healthcare.md). Step 3 screened twelve new industries (the developer chose all twelve); results below.

## Method

- **Firms (88):** the buyout firms from the SEC's November 2026 adviser files ranked by PE fund count (SPV platforms, fund-of-funds, wealth managers, venture, software and infrastructure managers removed), plus consumer-focused firms and the firms the audits and the screen found owning consumer brands. The selection is partly judgment; see the ticket's Comments.
- **Pages:** each firm's own current portfolio page, read with the project's bot rules (robots.txt first, one honest browser retry on a challenge, no clicks, never around a block). A portfolio listing marked current is the evidence; no ownership quotes were collected.
- **Consumer-facing:** sells mainly to individuals or households under a name consumers see; US only; B2B, software, insurance and financial services left out.
- **Step 2 dropped:** the SEC BDC data set's per-holding industry field is filled on 3% of holdings.

## Coverage

- 73 of 88 firms gave a usable current list. No usable list: Apollo, Blackstone, Bain, Brookfield, Ares and BDT & MSD (no list on the site), NRD (no portfolio page), Valor and Centerbridge (no current/exited marker), Encore (robots.txt blocks all bots), Sentinel, Partners Group, Goldman Sachs, Bridgepoint and Clearlake (blocked or refused), Bregal Partners (robots.txt blocks all bots, certificate mismatch). Partly read: Advent, Platinum, EQT, BC Partners, Apax, Audax, Bregal Sagemount.
- About 775 consumer-facing company listings (147, 293, 100 and 235 by worker), roughly 735 distinct companies after cross-worker duplicates (Philz Coffee and Mavis on three firms' pages; Authentic Brands on three; Caliber, Troon, Life Time, Crunch, Wrench Group, The Learning Experience, PT Solutions, Rarebreed, Mindpath, LifeStance and others on two).
- Gaps in the evidence: one bot slip (worker 3 sent one homepage request to Bregal Partners in the same command as its robots.txt read, before seeing "Disallow: /"; the response was deleted unread); several possibly stale listings (LGP's JOANN, Castanea's Essentia, Apax's At Home).

## Results by industry (firm listings, not deduplicated across workers)

Already measured by the category audits or the industry screen; the scan confirms where the PE is:

| Industry | Listings | Examples |
|---|---|---|
| Restaurants | 70 | Roark (Inspire, GoTo Foods, Subway, CKE, Culver's), Garnett Station (11), Brentwood (8), L Catterton (8) |
| Home services | 57 | Neighborly, Authority Brands, Wrench, Apex, Groundworks, Five Star; mostly local-name rollups |
| Gyms | 24 | Purpose Brands (Anytime, Orangetheory), Crunch, Life Time, Equinox, LA Fitness, Planet Fitness franchisees |
| Dental care | 22 | Aspen Group, Heartland, MB2, Smile Brands, Dental365 |
| Women's apparel | 18 | KnitWell (Ann Taylor, LOFT, Talbots, Chico's), Torrid, Lane Bryant, J.Jill, Lulus |
| Supplements | 17 | Thorne, GHOST, Orgain, Metagenics, Jarrow |
| Veterinary care | 16 | PetVet, Thrive, MedVet, Bond Vet, Heartland Veterinary |
| Oil change and auto service | 12 | Mavis, Jiffy Lube, Driven (Take 5, Meineke), Sun Auto |
| Urgent care | 10 | AFC, GoHealth, Fast Pace, WellStreet |
| Car washes | 9 | Mister, El Car Wash, Quick Quack, Tidal Wave, WhiteWater |
| Physical therapy, child care | 8 each | PT Solutions, ATI, Ivy; Learning Care, Primrose, Goddard, The Learning Experience |
| Golf, collision repair, pet stores, ski resorts, eyewear, hair salons, bowling and family entertainment | 3 to 6 each | Topgolf, Troon; Caliber, Safelite; Petco, PetSmart; Alterra; 1-800 Contacts, MyEyeDr.; Sola; Sky Zone |

**Not yet measured:**

| Cluster | Listings | Examples | Note |
|---|---|---|---|
| Specialty physician practices (dermatology, eye care, orthopedics, GI, urology, ENT, fertility, women's health, cardiology, pain) | about 40 | Epiphany, QualDerm, American Vision Partners, U.S. Urology Partners, US Fertility | almost all local-name rollups |
| Packaged food | 40 | Horizon Organic, Eagle Foods (Hamburger Helper), Sara Lee Frozen Bakery, Bazooka, Kodiak | product brands |
| Beauty and cosmetics | 37 | Olaplex, Orveon (bareMinerals), IL MAKIAGE, Milani, Kosas | product brands; many growth or minority stakes |
| Hotels | 36 | 32 KSL properties | mostly run under franchisor brands (Ritz-Carlton, Westin) |
| Behavioral health (incl. autism therapy) | about 28 | LifeStance, Mindpath, Monte Nido, ACES, LEARN | mixed brands and local names |
| Apparel, other (general, athletic, men's, children's, licensing) | about 23 | Vuori, Authentic Brands, PacSun, The Black Tux | |
| Sporting goods, outdoor, fitness equipment | about 23 | Rawlings, iFIT (NordicTrack), Traeger, RTIC, Pure Fishing | product brands |
| Home care, home health and hospice | about 20 | BrightSpring, Gentiva, Kindred, SYNERGY HomeCare, Honor (Webster; a regional Medicaid personal care provider, not Home Instead's parent, corrected by step 3) | |
| Personal care products | 17 | DUDE Wipes, Every Man Jack, PDC Brands, Grove | product brands |
| Pet food, products and services | 17 | Ethos (Natural Balance), Open Farm, Stella & Chewy's, Camp Bow Wow | |
| Beverages | 16 | Lipton Teas, Athletic Brewing, Spindrift, Duckhorn | product brands |
| Primary care | 16 | VillageMD, MDVIP, Suvida, Mosaic Health | |
| Med spas and beauty services | about 16 | European Wax Center, Milan Laser, Massage Envy, Hand & Stone, LaserAway, Waxing the City | storefront chains |
| Home furnishings | 11 | At Home, The Shade Store, Visual Comfort, Brooklinen | |
| Education, tutoring and schools | about 10 | Mathnasium, ABCmouse, Revolution Prep, Nord Anglia | |
| Auto parts and accessories, youth activities, travel and cruises, infusion therapy, consumer apps, rural broadband | 6 to 9 each | RealTruck; i9 Sports, School of Rock; Viking; Calm; Fidium | |

## Step 3: screens of twelve new industries

Run 2026-11-16 by four background workers with the industry screen's method (top ~10 brands, primary sources, Form ADV, the strict public-company rule). Worker reports: [s3-a beauty and personal care](pe-consumer-scan/s3-a-beauty-personal-care.md), [s3-b health services](pe-consumer-scan/s3-b-health-services.md), [s3-c food, beverages and pet](pe-consumer-scan/s3-c-food-beverages-pet.md), [s3-d education, apparel and sporting goods](pe-consumer-scan/s3-d-education-apparel-sporting.md). 269 of 269 quotes matched their saved page text; every negative control failed.

| Industry | PE share by brand row | Verdict | Main owners and notes |
|---|---|---|---|
| Med spas and beauty services | 10 of 10 (100%) | full audit | Massage Envy and Waxing the City (Roark), European Wax Center (General Atlantic, private since 2026-05-08), Hand & Stone (Harvest), Milan Laser (LGP), LaserAway (Seidler), Drybar, Elements and Amazing Lash (Transom, 2026), The Lash Lounge (Riverside) |
| Behavioral health | 10 of 13 (77%) | full audit | autism therapy (Action Behavior Centers, Hopebridge, BlueSprig), opioid treatment (BHG, BayMark), Eating Recovery Center (Apax), Mindpath (LGP), Thriveworks; LifeStance a PE minority (TPG 11.2%); Acadia and UHS public |
| Education and youth activities | 7 of 12 (58%; 42% strict) | full audit | Roark's Youth Enrichment Brands (School of Rock, SafeSplash) and Mathnasium; Seidler's Unleashed (Sylvan, The Little Gym); Goldfish family-owned; Kumon and Huntington not found (evidence from two 403 retries dropped, Q14) |
| Home care and hospice | 6 of 14 (43%) | full audit, with a rollup list | Comfort Keepers (Halifax), Interim (Revelar), BrightStar (Peak Rock), Gentiva (CD&R), Enhabit (Kinderhook), AccentCare (Advent); insurers own CenterWell and Amedisys; Home Instead's parent is venture-backed |
| Primary care | 2 of 8 (25%) | no | CVS, Humana, Amazon and the Chen family own the big brands; PE holds MDVIP and local-name rollups |
| Pet food and products | 2 of 10 company rows (1 of 8 consumer-brand rows) | no | Mars, Nestlé and Hill's take about 85% of top-10 revenue; Wellness (Clearlake); 14 PE challenger brands outside |
| Sporting goods and outdoor | 1 of 10 (Amer Sports, PE minority) | no | Weber (BDT) and Traeger (AEA, Trilantic) PE-controlled; a grills, coolers and fitness slice is the only audit candidate |
| Apparel other than women's | 1 of 15 (Skechers, 3G) | no | 23 PE brands outside, led by Authentic Brands Group |
| Beauty and cosmetics | 0 of 10 | no top-10 audit | public conglomerates on top; 36 PE brands outside (Olaplex, Orveon, Oddity, Milani) |
| Personal care | 0 of 10 | no | 17 PE challenger brands outside |
| Packaged food | 0 of 10 (0 of 20) | no | 40 PE brands outside (Duke's, Hamburger Helper, Horizon Organic) |
| Beverages | 0 of 9 sourced (Heineken blocked) | no | top 30: Primo (One Rock 26.5%, PE minority); Tropicana (PAI) at #33 |

Product industries rank companies by sales, so their top 10 are large public or family companies and PE sits in the long tail; counting them would need an aisle-level or long-tail measure (a question for "Launch industries").

New counting questions from step 3 (for "Launch industries"): a PE partner at clinic level (146 Humana CenterWell clinics in a WCAS partnership); creditor groups whose advisers report mostly hedge funds (Cano Health); BayMark's lender takeover reported only in trade press; PE founders holding personally (3G Capital's founders in AB InBev's control group); owners whose Form ADV reports no PE funds (Strategic Value Partners for Revelyst, joining Atairos and Meritage); a self-described PE firm in neither adviser file (Susquehanna Private Capital, Soccer Shots); preferred equity from PE firms under a founder majority (Bass Pro).

Bot slips reported in step 3: worker A followed four cross-host redirects before reading the new host's robots.txt (all four allow the bot) and fetched twice inside a 10-second crawl-delay; worker B followed one redirect to a disallowed path (response deleted unread) and one cross-host redirect before reading robots.txt (no restrictions); worker D retried two 403 responses (Kumon, Huntington) in the browser without checking whether they were challenges; the developer ruled to drop both rows' evidence (Q14), which changes no PE share. Each fetcher was patched to stop following redirects to unread hosts or disallowed paths.

## Caveats

- Counts are firm listings, not brands or market share; a cluster with many listings can still be a small share of its industry (packaged food's top brands belong to large public companies).
- The firm set leans toward healthcare (worker 4) and consumer specialists (worker 2), so those clusters are inflated relative to a random sample.
- Growth investors (VMG, Stripes, General Atlantic, Summit) often hold minority stakes, so "PE-owned" overstates control for many beauty, food and apparel rows.
- `L` marks (local-name rollups) are often the workers' judgment, not the firm's statement.

## Cost

Step 1: about 1.0M agent tokens (harness counts 280k, 234k, 246k and 239k), 50 to 70 minutes per worker, roughly 520 HTTP requests and 25 browser renders. Step 3: about 1.19M agent tokens (274k, 313k, 299k and 307k), 30 to 50 minutes per worker. Total so far about 2.2M (estimate approved with option (b): about 2.1M).
