# PE consumer scan, worker 2: consumer-focused firms

Ticket: [82 Research: Where PE owns consumer brands](../../issues/82-research-where-pe-owns-consumer-brands.md) · Worker report, 2026-11-16, saved by the parent session as returned (subagents could not write files), with each firm's company lines grouped by industry. Raw downloads and scripts were kept in the session scratchpad (temporary).

Read 20 of 22 firms' own portfolio pages (Encore's robots.txt blocks all bots; NRD has no portfolio page): 302 consumer-facing firm-company rows, about 293 distinct companies once co-owned and split rows are merged. Status came from each site's own data (per-item `data-status` attributes or classes, tab sections, a Nuxt payload, the public WordPress REST API for Princeton and Palladium); Butterfly's `?type=active` filter needed one browser render. US consumer-facing only; B2B skipped. `L` = locations keep local names; `L (gk)` = from the worker's general knowledge, not the firm's page.

## 1. Per firm

**Roark Capital** | https://www.roarkcapital.com/portfolio | read ("Current Investments") | 56 entries (parents and brands listed separately, about 23 distinct companies) | 20 rows
- restaurants: Inspire Brands (Arby's, Baskin-Robbins, Buffalo Wild Wings, Dunkin', Jimmy John's, SONIC); GoTo Foods (Auntie Anne's, Carvel, Cinnabon, Jamba, McAlister's, Moe's, Schlotzsky's, Seattle's Best Coffee); CKE Restaurants (Carl's Jr., Hardee's); Culver's; Dave's Hot Chicken; Jim 'N Nick's Bar-B-Q; Miller's Ale House; Subway
- oil change and auto service: Driven Brands (Take 5 Oil Change, Meineke)
- collision repair: Driven Brands (Maaco, CARSTAR, ABRA)
- gyms: Purpose Brands (Anytime Fitness, Orangetheory, The Bar Method, Basecamp); Fitness Connection
- beauty and spa services: Waxing the City; Massage Envy
- home services: ServiceMaster Brands (Merry Maids, ServiceMaster Restore)
- moving: TWO MEN AND A TRUCK
- education and tutoring: Mathnasium
- child care: Primrose Schools
- youth activities: Youth Enrichment Brands (i9 Sports, US Sports Camps, School of Rock, SafeSplash, U.S. Baseball Academy); KE Camps

**Sycamore Partners** | https://www.sycamorepartners.com/investments | read after one browser retry (static HTML is a JavaScript shell) | 22 | 12
- pharmacies: Walgreens · primary care: VillageMD (Village Medical) · restaurants: Playa Bowls
- women's apparel: KnitWell Group (Ann Taylor, LOFT, Talbots, Chico's, etc.); Lane Bryant; Torrid
- child care: Goddard Systems (The Goddard School) · beverages: AtoZ Wineworks · travel: Azamara; Margaritaville at Sea
- sporting goods: Pure Fishing (Abu Garcia, Berkley, Penn) · office supply stores: Staples US Retail
- skipped as non-US: Boots Group, RONA, Staples Canada

**L Catterton** | https://www.lcatterton.com/Investments.html plus 17 `Investments-<slug>.html` detail pages | read | 168 current across all funds (about 65 non-US consumer, 10 real estate, about 20 B2B, tech or financial) | 72 rows
- restaurants: Barcelona Wine Bar; bartaco; Founders Table (Chopt, Dos Toros); Hopdoddy; Piada; Snap Kitchen; Urban Egg; Velvet Taco
- gyms: Equinox; [solidcore] · fitness equipment: iFIT / ICON (NordicTrack; listed as two entries); Hydrow; Tonal
- beauty and cosmetics: Elevate Beauty (Omnilux); DIBS Beauty; Eighth Day; Kopari; Merit; Oddity (IL MAKIAGE, SpoiledChild); ROZ; Stripes Beauty; YSE Beauty; REMEDY Science
- personal care products: Function of Beauty; Public Goods
- supplements: Thorne; HumanN; GHOST; Alice Mushrooms; Tally Health; Mars Men
- packaged food: Good Culture; Goodles; Kodiak; Smash Foods · beverages: Remedy Drinks; X2 Performance
- pet food: Ethos Pet Brands (Natural Balance, Canidae); I and love and you; JustFoodForDogs
- veterinary care: Alliance Animal Health (L (gk)); Sploot Veterinary Care
- specialty physician practices: US Fertility (L (gk)); Arizona Pain · primary care: SignatureMD
- home services: Master Trades Group (fka Len the Plumber; "under various brands") (L)
- women's apparel: Savage X Fenty; ThirdLove; BloomChic; Ganni · men's apparel: Mizzen+Main · children's apparel: Hanna Andersson · apparel: A.P.C.; Etro
- footwear: Birkenstock; Tod's · jewelry: John Hardy · home furnishings: Boll & Branch · grocery: Hungryroot
- travel: AmaWaterways; GetYourGuide · hotels and lodging: Postcard Cabins; Open Road Resorts (RV parks)
- golf equipment: L.A.B. Golf · auto parts and accessories: RealTruck · boating supplies: West Marine · RVs and campervans: Storyteller Overland
- private aviation: Flexjet · ignition interlocks: Mindr (Intoxalock) · online marketplaces: Artsy · DTC brand aggregator: Dragonfly · acupuncture and wellness: WTHN
- Ganni, A.P.C., Etro and Tod's are European with only a few US stores.

**TSG Consumer Partners** | https://www.tsgconsumer.com/investments/ | read | 21 | 17
- gyms: CorePower Yoga; EoS Fitness · restaurants: Crumbl; Los Tacos No. 1; Pura Vida Miami
- personal care products: DUDE Wipes; Hempz; Saltair · beauty and cosmetics: PHLUR; Summer Fridays
- oil change and auto service: Mavis · auto parts and accessories: PowerStop; Rough Country
- hair salons: Radiance Holdings (Sola Salon Studios, The NOW, Woodhouse) · car washes: Super Star Car Wash
- veterinary care: Thrive Pet Healthcare (L (gk)) · home services: Wrench Group (L (gk))
- skipped: ATI Restoration (mostly commercial), Cadogan Tate (UK), Revolut, Legacy.com

**Freeman Spogli** | https://www.freemanspogli.com/portfolio/ (status from `/portfolio/_payload.json`) | read | 20 | 13
- restaurants: Philz Coffee; Cafe Rio; City Barbeque · med spas: VIO Med Spa
- home services: Infinity Home Services (roofing and exteriors); NearU · veterinary care: EverVet (L)
- car washes: WhiteWater Express · home furnishings: Brooklinen
- pet care services: Propelled Brands (Camp Bow Wow) · hair salons: Propelled Brands (My Salon Suite)
- urgent care: CRH Healthcare (L; the page has a "Local Brands" section) · battery and phone repair stores: Batteries Plus

**Golden Gate Capital** | https://goldengatecap.com/portfolio/?_sft_status=active | read | 22 active | 7
- moving: All My Sons · home services: All U Need Pest Control; Virginia Green · oil change and auto service: Mavis Discount Tire
- apparel: PacSun · child care: The Learning Experience · car washes: Tidal Wave Auto Spa

**Levine Leichtman (LLCP)** | https://www.llcp.com/portfolio/ | read | 34 | 7
- golf equipment: Club Champion · home services: Five Star Franchising (8 home-service franchise brands)
- restaurants: Kilwins; Shipley Do-Nuts · med spas: SEV · veterinary care: Suveto (L (gk)) · home care: SYNERGY HomeCare

**Gryphon Investors** | https://www.gryphon-inv.com/companies/ | read | 35 | 15
- dermatology: AQUA Dermatology · supplements: Double Wood Supplements; Metagenics
- veterinary care: Heartland Veterinary Partners (L (gk)) · behavioral health: LEARN Behavioral (autism therapy)
- work gear: Mechanix Wear · beauty and cosmetics: Milani; Revision Skincare
- home services: NAEHS (Southern HVAC, a "house of brands") (L); Repipe Specialists
- physical therapy: Physical Rehabilitation Network (L (gk)) · dental care: Smile Brands (Bright Now! Dental, Monarch, etc.)
- beverages: Spindrift · pet food: Vetnique Labs · eye care: Vision Innovation Partners (L (gk))

**Brentwood Associates** | https://www.brentwood.com/our-portfolio/ | read | 23 | 18
- gyms: Afterburn Holdings (Orangetheory franchisee)
- restaurants: Blaze Pizza; Chicken Salad Chick; Far West Services (Wingstop franchisee, 100+ units); Hissho Sushi; Lazy Dog; Pacific Catch; Snooze; Upward Projects (Postino)
- women's apparel: Boston Proper · apparel: J.McLaughlin · dental care: Jefferson Dental & Orthodontics
- key duplication: KeyMe · supplements: L-Nutra (ProLon) · beauty and cosmetics: Pacifica
- home services: Perennial Services Group (lawn, pest, arbor) (L) · education and tutoring: The Great Courses · water and ice vending: Watermill Express

**Princeton Equity Group** | https://princetonequity.com/companies/ (WordPress REST API: tag "active" = 19, "realized" = 9) | read | 19 | 17
- home services: 1-800-Packouts; Bath Solutions; Bio-One; Five Star Franchising; Gotcha Covered; Mosquito Shield; Restoration 1; Stellar Brands (Restoration 1, bluefrog)
- gyms: AMPED Fitness; Barry's; D1 Training; Stretch Zone
- yard sign rentals: Card My Yard · behavioral health: Ellie Mental Health · youth activities: KidStrong
- med spas: Princeton Medspa Partners (L (gk)) · oil change and auto service: Strickland Brothers

**MidOcean Partners** | https://www.midoceanpartners.com/our-business/portfolio-companies | read | 20 | 9
- dental care: Affinity Dental Management · auto parts and accessories: Arnott; Holley
- packaged food: Casper's (FatBoy); Louisiana Fish Fry · home services: Empower Brands (Lawn Doctor, Mosquito Hunters, etc.)
- oil change and auto service: FullSpeed Automotive (Grease Monkey, SpeeDee) · beauty and cosmetics: Image Skincare · luggage: Travelpro Group
- skipped: PPLSI (LegalShield), close to insurance

**Butterfly Equity** | https://www.bfly.com/investments (butterflyequity.com redirects; `?type=active` render shows all 13) | read | 13 | 8
- beverages: The Duckhorn Portfolio; Generous Brands (Bolthouse Farms juices, Evolution Fresh, Health-Ade)
- packaged food: Chosen Foods; Pete & Gerry's; Bolthouse Fresh Foods · supplements: MaryRuth Organics; Orgain · restaurants: QDOBA

**Encore Consumer Capital** | encoreconsumercapital.com | unreadable: robots.txt `User-agent: *` `Disallow: /` (only named search engines allowed), and the HTTPS certificate doesn't match the domain

**VMG Partners** | https://www.vmgpartners.com/companies | read | 50 (25 consumer, 25 technology) | 28
- beauty and cosmetics: Miss A; Snif; Tone; Danessa Myricks; Melanin Haircare; Beautystat; Kosas; Shani Darden
- personal care products: Vacation; Cocolab; Proudly; Necessaire (filed under Technology)
- packaged food: Brami; Stars + Honey; Fruit Riot; Milton's; Little Freddie; Bobbie (filed under Technology); Redbud
- supplements: Ghost · pet care services: Scenthound · pet food: Maev · gyms: ETS Performance; Undefeated Tribe; Solidcore
- med spas: OVME · beauty and spa services: Rowan (ear piercing) · grocery: Weee! (filed under Technology)

**Swander Pace Capital** | https://spcap.com/portfolio/ | read | 11 | 5
- OTC health products: Mommy's Bliss · packaged food: Mighty Spark; Bragg; Oregon Ice Cream · supplements: Swanson Health Products
- skipped: Maple Donuts, Inovata, Café Valley and Captek (B2B), St-Méthode (Canada only), Max Solutions (unclear)

**Castanea Partners** | https://castaneapartners.com/brands/?status=current-investments | read | 12 | 12
- gyms: West Coast Fitness (Orangetheory franchisee) · beverages: Brew Dr. Kombucha; The Bruery; Essentia (possibly stale) · packaged food: Yasso
- restaurants: Jeni's · sporting goods: Simms Fishing · personal care products: Thymes · baby products: 4moms
- home furnishings: MacKenzie-Childs · hair salons: Drybar · fitness equipment: TRX

**Stripes** | https://www.stripes.co/investments | read | 63 | 21
- restaurants: Just Salad; La La Land Kind Cafe; Levain Bakery; Popup Bagels; 7th Street Burger; Snooze
- grocery: Erewhon · fitness equipment: Aviron · behavioral health: Boulder Care; Equip
- apparel: BRUNT; Vuori · women's apparel: KHAITE · men's apparel: The Black Tux · beauty and cosmetics: Kosas
- beverages: Califia Farms · packaged food: MìLà; Seven Sundays · pet food: Stella & Chewy's · sporting goods: Shibumi Shade · collectibles grading: Collectors (PSA)
- skipped: A24 (media), GoFundMe and other fintech

**Kohlberg & Company** | https://www.kohlberg.com/investments/ | read | 28 | 5
- sporting goods: Elevate Outdoor Collective · behavioral health: Meadows Behavioral Healthcare · packaged food: Sara Lee Frozen Bakery
- specialty physician practices: Spire Orthopedic Partners (L (gk)); United Digestive (L (gk))

**Charlesbank Capital Partners** | https://www.charlesbank.com/investments/ | read | 33 | 8
- urgent care: Access Medical Clinic · behavioral health: Action Behavior Centers · home services: American Residential Services
- OTC health products: Bridges Consumer Healthcare · dental care: MB2 Dental (L (gk)) · primary care: MDVIP · eyewear: MyEyeDr. · footwear: REEF

**Palladium Equity Partners** | https://www.palladiumequity.com/investments (`wp-json/wp/v2/company?company_status=12`, "unrealized") | read | 18 | 6
- packaged food: SpiceWorld; Del Real Foods · beverages: Jordan's Skinny Mixes · bowling and family entertainment: Sky Zone · jewelry: Daniel's Jewelers · behavioral health: Health Connect America

**Monomoy Capital Partners** | https://www.mcpfunds.com/portfolio | read | 17 active | 2
- oil change and auto service: Jiffy Lube (bought from Shell, July 2026) · hot tubs: Artesian Spas

**NRD Capital** | https://nrdcapital.com | unreadable: no portfolio page (nav is About, Viewpoint, Impact, Contact; /portfolio and /portfolio.php return 404)

## 2. Tally (firm-company rows; co-owned companies count once per firm)

- restaurants 41 (Roark alone about 21 restaurant brands); beauty and cosmetics 25; packaged food 25; home services 21; gyms 15; supplements 13; beverages 11; personal care products 10; women's apparel 9; behavioral health 7.
- 6 each: apparel, oil change and auto service, pet food, veterinary care. 5 each: auto parts and accessories, fitness equipment.
- 4 each: dental care, med spas, specialty physician practices, sporting goods, travel.
- 3 each: beauty and spa services, car washes, child care, footwear, grocery, hair salons, home furnishings, primary care, youth activities.
- 2 each: OTC health products, education and tutoring, golf equipment, hotels and lodging, jewelry, men's apparel, moving, pet care services, urgent care.
- 1 each: collision repair (Driven), pharmacies (Walgreens), office supply stores (Staples), dermatology, physical therapy, eye care, eyewear (MyEyeDr.), home care, children's apparel, bowling and family entertainment (Sky Zone), luggage, baby products, boating supplies, RVs and campervans, hot tubs, private aviation, ignition interlocks, online marketplaces, DTC brand aggregator, acupuncture and wellness, battery and phone repair stores, key duplication, water and ice vending, collectibles grading, work gear, yard sign rentals.
- 302 rows give about 293 distinct companies: co-owned and listed by two firms (Mavis, Snooze, Kosas, GHOST, solidcore, Five Star Franchising); split into two rows (Driven Brands, Propelled Brands); Princeton lists both Restoration 1 and its parent Stellar Brands.

## 3. Notes

- Unreadable: Encore (robots.txt blocks all bots), NRD (no portfolio page).
- Domains: swanderpace.com now redirects to a gambling spam site; the firm is at spcap.com. stripes.com is the Stars and Stripes newspaper; the firm is at stripes.co. Butterfly is at bfly.com, Gryphon at gryphon-inv.com.
- Status quirks: Golden Gate's `Crawl-delay: 10` honored; Castanea still lists Essentia as current (worker believes Nestlé bought it in 2021, unchecked), Drybar may also be stale; L Catterton lists ICON and iFIT separately (same company, old and new name); Princeton tags bluefrog "realized" but lists its parent Stellar Brands as active.
- Surprises: home services (21) nearly as large as gyms plus car washes, driven by franchisor platforms (Princeton, Empower, Five Star) and HVAC and plumbing rollups; behavioral health (7) across six firms (autism therapy chains, virtual treatment); other unmeasured clusters: med spas, specialty physician practices, consumer auto parts brands, fitness equipment, cruise lines (Azamara, Margaritaville at Sea); consumer packaged goods dominate VMG, Castanea, Butterfly and Swander Pace.
- Caveats: VMG and Stripes are growth investors and often hold minority stakes, so "PE-owned" overstates control for many of their 49 rows. Page-backed `L` flags: Master Trades, NAEHS, CRH, Perennial, EverVet; the rest are `L (gk)`.
- Cost: about 50 minutes; roughly 250k tokens; about 122 requests (32 robots.txt, about 85 page and data fetches, 5 one-time browser renders: Golden Gate, Sycamore ×2, Butterfly, Palladium; the Golden Gate render proved unnecessary).
