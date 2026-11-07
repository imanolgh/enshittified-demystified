# Category audit: Cookware

Ticket: [66-research-full-category-audit](../../issues/66-research-full-category-audit.md) · Researched 2026-11-07 (fetches logged 16:59–17:26 UTC) · Ownership facts come from primary sources only. A data vendor's blog and a data vendor's free table supply the ranking only.

**Short answer**

| | Cookware (N = 30 brand rows: 10 ranked, 20 unranked) |
|---|---|
| PE-owned plus PE minority stake, by brand row | **4 / 30 (13.3%)**: Cuisinart (American Securities, control), Martha Stewart (Marquee Brands, backed by Neuberger Berman), Caraway (M-One Capital, formerly McCarthy Capital) and Made In (KarpReilly). All four count as PE-owned. Caraway and Made In count under the "no stated stake" rule, but each PE firm entered by leading a funding round, so each may hold a minority. Either way the combined count stays 4. |
| Top 10 by Amazon skillet revenue (the only ranked rows) | **3 / 10 PE (30%)**: Cuisinart (#2), Caraway (#5) and Made In (#8). Together they hold 17.6% of Amazon skillet share, out of 59.5% held by the top 10. |
| Strict count (a public company whose 5%+ holder's Form ADV reports PE funds) | **Still 4 / 30 until the assembler's Form ADV check.** There are 7 public rows (All-Clad, T-fal, OXO, Calphalon, KitchenAid, Ninja, Carote). The 5%+ holders whose type isn't confirmed are RWWM, Inc. (Helen of Troy, 5.04%), Pzena Investment Management (Newell, 11.6%), Appaloosa LP (Whirlpool, 6.92%) and PRIMECAP Management Company (Whirlpool, 6.75%). Groupe SEB's and Carote's holders were not read. |
| Owner not found | **6 / 30 (20.0%)**: HexClad, Blue Diamond, Le Creuset, Misen, Our Place, Pioneer Woman. Another 11 rows name a private company or founder but no owner (Meyer's 6 brands, Lodge, Tramontina, GreenPan, GreenLife, Gotham Steel). |
| Brand-direct affiliate programs | **10 found, each on a page the brand runs**: HexClad, GreenPan, Caraway, All-Clad, T-fal, Le Creuset, Great Jones, Hestan, Ninja (SharkNinja) and Zwilling (a group program that also covers Staub). **Probable: 2.** OXO's page exists, per search, but returned 403. Cuisinart's footer links to an affiliate page that returned 404. **Network listings only: 2** (Calphalon, Made In). **One PE row has a brand-direct program**: Caraway. |

- **No free ranking of US cookware brands by sales or share was found.** The list is a composite (see "Ranking"). Rows 1–10 are SmartScout's top 10 skillet brands on Amazon US, ranked by Amazon revenue share. Rows 11–30 are a stated candidate set, unranked and listed alphabetically.
- **Biggest finding:** in cookware, PE ownership sits on direct-to-consumer and licensed names: Caraway, Made In and Martha Stewart, plus Cuisinart through Conair. The heritage makers sit outside it: they are family-held or founder-held (Zwilling and Staub under the Werhahn family; Meyer's six brands; Lodge; Tramontina) or public (Groupe SEB, Newell, Helen of Troy, SharkNinja).
- **Affiliate income is common in this category.** 10 brand-direct programs were found, against 4 across all three pilot categories and 2 in pet stores. Most sit on non-PE rows: Groupe SEB (2), Meyer (2), Zwilling, SharkNinja, HexClad, GreenPan and Le Creuset.
- **Marquee Brands (Neuberger Berman) also owns the Emeril Lagasse and Sur La Table names** (CK22). Neither is a row here: Emeril was not in the candidate set, and Sur La Table is a retail chain that the ranking leaves out.

## How this was sourced (read first)

- **Ranking:** composite (see "Ranking" below). It uses SmartScout's blog post on the top 10 skillet brands on Amazon US (2025-07-17) and, for one added row, Similarweb's free Kitchen & Dining table (October 2026). Both were used for the ranking only, never as evidence of ownership.
- **Ownership facts** come from SEC filings (10-K, DEF 14A, 8-K), sponsor press releases and portfolio pages, a listed PE fund's case-study page (Neuberger's NBPE), and company sites (about pages, terms of sale, footers). No company release was read as a reprint.
- **SEC access:** 20 SEC requests (www.sec.gov, data.sec.gov, efts.sec.gov). All used the user agent `EvidenceEngine ownership-research bot (category audit)`, with no contact detail, at no more than 2 requests per second (0.6 s sleep per request). All returned HTTP 200.
- **Robots:**
  - robots.txt was read before each new site was fetched with curl.
  - No site used here disallows ClaudeBot or anthropic-ai.
  - lecreuset.com sets `Crawl-delay: 25`, and its two pages were fetched 26 s apart.
  - nbprivateequitypartners.com disallows GPTBot only.
  - tramontina.com and mycarote.com (Shopify) have robots.txt comments addressed to AI agents. Those comments were treated as page content, not instructions.
  - meyerus.com has a content-signal preamble with no signal set.
- **Blocked or failed:**
  - oxo.com and calphalon.com returned 403 to curl.
  - businesswire.com returned 403 to robots.txt and to the page.
  - bluediamondpan.com returned 404 for every subpage, though its homepage loaded.
  - Two of the four WebFetch calls hit 403 or 404. The HKEX PDF could not be text-extracted: there is no PDF library in the environment, and WebFetch could not read the compressed streams.
- **Never fetched:**
  - competitor sites (worseonpurpose.com ledger pages came up in 3 searches);
  - Reddit, WhoIsMyDentist and Private Equity Vet;
  - PitchBook, CB Insights and Preqin results that came up in searches.
- **Leads only, never cited:** Wikipedia, trade press on deals (Bloomberg, Retail Dive, mediaincanada), deal directories (mergerlinks, privsource) and affiliate-network listings (FlexOffers, LinkClicky).
- **Owner kinds are research notes, not engine classifications.**
  - "PE-owned" means control, or a PE owner with no stated stake.
  - "Private, owner not stated" means a primary source names the company and often its founder, but not who owns it, and no PE evidence was found.
  - Counts are by brand row: Meyer is 6 rows, Groupe SEB 2, Zwilling 2 and The Cookware Company 2.
- **Licensed names** (Farberware, KitchenAid, Rachael Ray, Martha Stewart, Pioneer Woman): the row reports who runs the US cookware business under the name, as the source states it, and notes the trademark owner where a source gives it.
- **Quotes:** copied from curl'd page text, with tags stripped, whitespace collapsed and HTML entities decoded. No quote below came through a WebFetch summarizer; the 4 WebFetch calls all failed or returned nothing usable.

## Ranking

**No free, current ranking of US cookware brands by sales, units or share was found.** Sources checked and rejected:
- Market-research report teasers (Expert Market Research, Orion, Mordor/GII, Spherical Insights, Market Research Future, Mintel, Statista): paywalled, and they list key players without ranks.
- Circana and the IHA: the 2026 State of the Industry report and the Home Industry Performance Awards give category trends and share-gain awards, not a brand ranking.
- HomeWorld Business: no cookware brand ranking turned up in search.
- Similarweb, "Best Selling Kitchen & Dining Brands on Amazon" (updated 2026-10-01, https://www.similarweb.com/top-amazon-brands/usa/home-kitchen/kitchen-dining/): only the top 5 are free, and they are mostly appliances. There is no cookware subcategory page (`…/kitchen-dining/cookware/` returned 404).
- YouGov Ratings: the cookware-brands page returned 404.
- Parse.gl: ranks AI-chatbot share of voice, not sales.

**Composite used.**

(a) **Rows 1–10:** SmartScout (a seller-analytics vendor), "Top 10 Skillets Brands on Amazon", blog post dated 2025-07-17, https://www.smartscout.com/blog/top-10-skillets-brands-on-amazon.
- It ranks brands by share of Amazon US skillet revenue (annual). The page says: "According to recent Amazon market data, Hexclad now leads the skillet category in both revenue and share, outpacing brands that have been around for decades." and "Hexclad leads the category with a 14.6% market share and $34.3 million in annual revenue."
- Order and figures as stated:

| Rank | Brand | Share | Annual revenue |
|---|---|---|---|
| 1 | HexClad | 14.6% | $34.3M |
| 2 | Cuisinart | 10.4% | $22.6M |
| 3 | Lodge | 8.9% | $22.0M |
| 4 | GreenPan | 6.6% | $12.4M |
| 5 | Caraway | 4.4% | $8.7M |
| 6 | Tramontina | 3.5% | $5.4M |
| 7 | All-Clad | 3.2% | $8.4M |
| 8 | Made In | 2.8% | $8.8M |
| 9 | OXO | 2.6% | $4.1M |
| 10 | Blue Diamond | 2.5% | $6.2M |

- The share and revenue columns don't put the brands in the same order (All-Clad, Made In and Blue Diamond have more revenue than Tramontina but lower shares). The order above follows share, as the article does.
- Limits: one channel (Amazon), one product type (skillets), and the methodology is not published.

(b) **Rows 11–30, unranked, listed alphabetically.** The row number is an id, not a rank. The candidate set is:
- other cookware brands of the companies behind ranked rows: T-fal (Groupe SEB, with All-Clad) and GreenLife (The Cookware Company, with GreenPan);
- the cookware brands of the large makers that market-research summaries name as US competitors: Newell (Calphalon); Meyer (Anolon, Circulon, Farberware, Rachael Ray, KitchenAid cookware, Hestan, Great Jones, all on Meyer's own brand list); Zwilling (Zwilling, Staub); Le Creuset;
- DTC brands outside the Amazon top 10: Our Place, Misen;
- mass-channel lines: Ninja (SharkNinja lists cookware in its 10-K); CAROTE, which Similarweb's free table shows among the top 5 Kitchen & Dining brands on Amazon US in October 2026 ("CAROTE 0.64% 0.11pp", revenue share); Gotham Steel (TV and mass retail);
- licensed celebrity lines sold through Walmart and department stores: Martha Stewart, Pioneer Woman.

**Not exhaustive.**
- Unchecked, possibly above the cutoff:
  - store brands (Walmart's Mainstays and Thyme & Table, Target's Goodful and Figmint, Costco's Kirkland Signature);
  - Amazon-native brands (SENSARTE and others);
  - Ayesha Curry (also on Meyer's list) and Emeril Lagasse (Marquee Brands);
  - Viking, Mauviel, Smithey, Field Company, Scanpan, Ballarini (Zwilling) and Demeyere (Zwilling).
- Excluded by scope: knife-only brands (the ranking does not group knives with cookware), bakeware-led brands (Nordic Ware, Pyrex and CorningWare under Corelle Brands), and kitchen retail chains (Williams-Sonoma, Sur La Table), because the ranking does not include retailers.

| # | Brand | Owner today (as source states) | Owner kind (research note) | PE firm(s) in chain | Since | Ticker | Operating model | Affiliate program | Ev. |
|---|---|---|---|---|---|---|---|---|---|
| 1 | HexClad (14.6% Amazon skillet share) | not found (site footer: "HexClad Cookware") | not found (trade press: founders, with a 2024 minority investment by Studio Ramsay Global, a Fox and Gordon Ramsay venture; not cited) | none found | not found | — | DTC plus Amazon and retail | **yes, brand-direct**: https://hexclad.com/pages/affiliate (up to 15%) | CK1 |
| 2 | Cuisinart (10.4%) | Conair (Conair Corporation), acquired by affiliates of American Securities; Rizzuto family retains a minority | PE-owned | American Securities | 2021-05-17 | — | brand of a manufacturer; sells through retail | probable: footer links to /support/affiliate.html, which returned 404 to curl; network listings (CJ, FlexOffers) not opened | CK2 |
| 3 | Lodge (8.9%) | Lodge Manufacturing Company; owner not stated | private, owner not stated (company founded by Joseph Lodge, 1896; history names Lodge descendants as past leaders; no PE evidence) | none found | not applicable (founded 1896) | — | manufacturer (two foundries in South Pittsburg, TN), plus factory stores | none found | CK3 |
| 4 | GreenPan (6.6%) | The Cookware Company (HQ in Belgium), created by Jan Helskens and Wim De Veirman; owner not stated | private, owner not stated (founders named; no PE evidence) | none found | not applicable (founded 2007) | — | brand of a manufacturer; DTC plus retail | **yes, brand-direct**: https://www.greenpan.us/pages/affiliate | CK4 |
| 5 | Caraway (4.4%) | Caraway; M-One Capital (formerly McCarthy Capital) lists it under Current Investments, investment type "Recapitalization & Growth"; stake not stated | PE-owned (no stated stake; the 2022 release calls it a $35M investment "led by" McCarthy) | M-One Capital / McCarthy Capital (McCarthy Partners Management, LLC) | 2022-09-28 | — | DTC plus Amazon and retail (Target, Crate & Barrel, Nordstrom) | **yes, brand-direct**: https://www.carawayhome.com/pages/affiliate | CK5 |
| 6 | Tramontina (3.5%) | Tramontina group, founded by Valentin and Elisa Tramontina in 1911 (Brazil); owner not stated | private, owner not stated (founder-family company per its history; no PE evidence) | none found | not applicable (founded 1911) | — | vertically integrated manufacturer | none found | CK6 |
| 7 | All-Clad (3.2%) | Groupe SEB ("All-Clad a company of GROUPE SEB USA") | public company (foreign-listed: Euronext Paris) | not checked (5%+ holders not read) | not checked | SK (Euronext Paris) | brand of a manufacturer; DTC plus retail | **yes, brand-direct**: https://www.all-clad.com/all-clad-affiliate-program (via CJ) | CK7 |
| 8 | Made In (2.8%) | Made In; KarpReilly lists it under Current Investments; stake not stated | PE-owned (no stated stake; KarpReilly led a $1.33M Series A in 2017) | KarpReilly | 2017-10-30 | — | DTC plus Amazon | network listing only (Impact per directories; not opened); no brand page found | CK8 |
| 9 | OXO (2.6%) | Helen of Troy Limited (owned trademark) | public company | none confirmed at 5%+ (BlackRock 6.90%, JPMorgan Chase 5.06%, RWWM, Inc. 5.04%, Vanguard Capital Management 5.00%; RWWM's type not confirmed) | not checked | HELE | brand of a consumer-products company | probable: brand page oxo.com/oxo-affiliate-program found in search; returned 403 | CK9 |
| 10 | Blue Diamond (2.5%) | not found (site footer: "© Blue Diamond"; subpages 404) | not found | none found | not found | — | not found | none found | CK10 |
| 11 | Anolon | Meyer Corporation, U.S. (on Meyer's brand list); Meyer founded and led by Stanley Cheng; owner not stated | private, owner not stated (founder-led; no PE evidence) | none found | not checked | — | brand of a manufacturer | none found | CK11 |
| 12 | Calphalon | Newell Brands Inc. | public company | none confirmed at 5%+ (BlackRock 13.5%, Pzena Investment Management 11.6%, Vanguard 10.6%; Pzena's type not confirmed) | not checked | NWL | brand of a consumer-products company | network listing only (FlexOffers "Newell Brands"); calphalon.com returned 403 | CK12 |
| 13 | CAROTE | Carote Ltd (HKEX-listed); a "controlling shareholder" is referred to but not named in pages read | public company (foreign-listed: HKEX); controlling shareholder not named | none found (trade press: Hillhouse and Shunwei joined the 2024 IPO; stakes unknown; not cited) | IPO 2024-10 (allotment results 2024-09-30) | 2549 (HKEX; from filings index, PDF not machine-read) | Amazon-native brand | none found | CK13 |
| 14 | Circulon | Meyer Corporation, U.S. (see CK11) | private, owner not stated (founder-led) | none found | not checked | — | brand of a manufacturer | none found | CK14 |
| 15 | Farberware | Meyer Corporation, U.S. (cookware; on Meyer's brand list). Lifetime Brands holds a royalty-free license for Farberware kitchen tools and cutlery (not cookware) | private, owner not stated (founder-led) | none found for the cookware business (Lifetime Brands, the tools licensee, has Centre Partners V, L.P. at 26.2%) | not checked | — (licensee Lifetime: LCUT) | brand of a manufacturer | none found | CK15 |
| 16 | Gotham Steel | Emson, Inc. (site footer); owner not stated | private, owner not stated (no PE evidence) | none found | not found | — | TV and mass-retail brand | none found | CK16 |
| 17 | Great Jones | Meyer Corporation, U.S. (on Meyer's brand list; Great Jones launched in 2018) | private, owner not stated (founder-led parent) | none found | not found (trade press: Hestan acquired it in June 2023) | — | DTC brand within Meyer | **yes, brand-direct**: https://greatjonesgoods.com/pages/affiliates | CK17 |
| 18 | GreenLife | The Cookware Company (USA), LLC (seller on the site's terms) | private, owner not stated (see CK4) | none found | not checked | — | brand of a manufacturer | none found | CK18 |
| 19 | Hestan | Meyer Corporation, U.S. (on Meyer's brand list; Hestan founded 1996) | private, owner not stated (founder-led parent) | none found | not checked | — | brand of a manufacturer (cookware made in Italy) | **yes, brand-direct**: https://hestanculinary.com/pages/affiliate-program | CK19 |
| 20 | KitchenAid (cookware) | brand: Whirlpool Corporation (licenses the name to third parties); cookware line on Meyer Corporation, U.S.'s brand list | public company (brand owner); cookware run by a private licensee | none confirmed at 5%+ for Whirlpool (BlackRock 11.01%, Vanguard 9.73%, Appaloosa LP 6.92%, PRIMECAP 6.75%, FMR 5.66%; Appaloosa's and PRIMECAP's types not confirmed) | not checked | WHR | licensed name (Whirlpool licensor) | not checked (kitchenaid.com not fetched) | CK20 |
| 21 | Le Creuset | not found (US entity: "Le Creuset of America, Inc.") | not found (trade press: privately held by Paul van Zuydam since 1988; not cited) | none found | not found | — | brand of a manufacturer; DTC plus own stores and retail | **yes, brand-direct**: https://www.lecreuset.com/affiliates.html (up to 10%) | CK21 |
| 22 | Martha Stewart | Marquee Brands LLC (bought Martha Stewart Living Omnimedia in 2019), a brand licensor whose lead investor is Neuberger Berman (since 2014); stake not stated | PE-owned (no stated stake) | Neuberger Berman (Marquee Brands) | 2019-06-10 (Marquee); Neuberger since 2014-12 | — | licensed name (royalties from third-party licensees; cookware licensee not identified) | not checked | CK22 |
| 23 | Misen | not found | not found (trade directories: venture-backed; not cited) | none found | not found | — | DTC | none found (homepage; /pages/partnerships not opened) | CK23 |
| 24 | Ninja (cookware) | SharkNinja, Inc. | public company (founder CJ Xuning Wang ~38.6%) | none at 5%+ other than FMR LLC 14.7% | not applicable | SN | brand of a consumer-products company | **yes, brand-direct**: https://www.sharkninja.com/affiliate.html (via Impact, up to 20%) | CK24 |
| 25 | Our Place | not found | not found (trade press: founder-led, venture-backed; not cited) | none found | not found | — | DTC plus retail | none found (site links only a refer-a-friend page) | CK25 |
| 26 | Pioneer Woman | not found (trade press: Ree Drummond licenses the name; Gibson Overseas is the licensee; Walmart exclusive; not cited) | not found | none found | not found | — | licensed name, Walmart-exclusive (trade press) | not checked | CK26 |
| 27 | Rachael Ray (cookware) | Meyer Corporation, U.S. (on Meyer's brand list) | private, owner not stated (founder-led) | none found | not checked | — | licensed celebrity name (license terms not stated) | not checked | CK27 |
| 28 | Staub | ZWILLING J.A. Henckels (acquired Staub 2008), wholly owned by Wilh. Werhahn KG since 1970 | family (Werhahn: "a family company") | none | 2008 | — | brand of a manufacturer | **yes (group program)**: https://www.zwilling.com/us/magazine/affiliate-program.html | CK28 |
| 29 | T-fal | Groupe SEB (seller: GROUPE SEB USA) | public company (foreign-listed: Euronext Paris) | not checked | not checked | SK (Euronext Paris) | brand of a manufacturer; DTC plus retail | **yes, brand-direct**: https://www.t-fal.com/affiliate-program (via CJ) | CK29 |
| 30 | Zwilling (incl. Henckels cookware) | ZWILLING J.A. Henckels, wholly owned by Wilh. Werhahn KG since 1970 | family | none | 1970 (Werhahn sole shareholder) | — | brand of a manufacturer | **yes, brand-direct**: https://www.zwilling.com/us/magazine/affiliate-program.html | CK30 |

### Evidence
- **CK1 HexClad**
  - Owner: not found. The site footer says "© HexClad Cookware. All rights reserved." — [HexClad, About page, accessed 2026-11-07](https://hexclad.com/pages/about-us)
  - Since: not found
  - Model: DTC site plus Amazon (ranking source) and retail (not checked)
  - Affiliate: "start earning up to 15% commission for every sale that you refer" — [HexClad, Affiliate page, accessed 2026-11-07](https://hexclad.com/pages/affiliate)
  - BDC names: "HexClad Cookware", "HexClad, Inc."
  - Notes: 2 searches, 6 fetches.
    - The only primary-source candidate, HexClad's Business Wire release of 2024-07-16 ("HexClad Announces Strategic Investment From Studio Ramsay Global", https://www.businesswire.com/news/home/20240716139872/en/), returned 403 to curl and to WebFetch.
    - Trade press (not cited) describes a $100M minority investment by Studio Ramsay Global, a joint venture of Fox Entertainment and Gordon Ramsay. That is not a PE firm.
    - The About and Press pages name chef partners, not owners.
- **CK2 Cuisinart**
  - Owner: "a leading U.S. private equity firm, announced today that Conair has been acquired by affiliates of American Securities." — [American Securities, press release "Conair Corporation Acquired By American Securities", 05.17.21](https://www.american-securities.com/news/press-release/conair-corporation-acquired-by-american-securities/)
  - Minority: "Certain members of the Rizzuto family have retained a minority ownership stake in Conair." — [same release](https://www.american-securities.com/news/press-release/conair-corporation-acquired-by-american-securities/)
  - Brand: "Based in Stamford, CT, Conair's iconic brands include Cuisinart®, Conair®, Babyliss®, Scunci® and Waring®." — [same release](https://www.american-securities.com/news/press-release/conair-corporation-acquired-by-american-securities/)
  - Since: "Conair Corporation Acquired By American Securities 05.17.21 // Press Release" — [same release](https://www.american-securities.com/news/press-release/conair-corporation-acquired-by-american-securities/). The page metadata gives 2021-05-17.
  - Current: "Conair Global leader in premium kitchen electric appliances, non-electric kitchenware, personal care, grooming, health, and beauty products" — [American Securities, Companies page, accessed 2026-11-07](https://www.american-securities.com/companies/). The listing sits under the page's "Status: Current" filter.
  - Model: brand of a manufacturer, sold through retail. Company vs franchise does not apply.
  - Affiliate: the cuisinart.com footer links to `https://www.cuisinart.com/support/affiliate.html`, which returned HTTP 404 to curl. A search found CJ and FlexOffers listings (not opened). Probable, not confirmed.
  - BDC names: "Conair Corporation", "Conair LLC", "Conair Holdings", "Cuisinart"
  - Notes: control is stated ("acquired by affiliates of American Securities"), with a named family minority.
- **CK3 Lodge**
  - Owner: not stated. Company: "Lodge Manufacturing Company is proud to be actively associated with domestic and international trade, business, and culinary organizations." — [Lodge, Affiliations page, accessed 2026-11-07](https://www.lodgecastiron.com/pages/affiliations)
  - History: "Lodge Cast Iron has been making heirloom-quality cookware and accessories since 1896." and "During tough economic times in the 1970s, William Leslie Kellermann, Joseph Lodge's grandson, drafted a plan to reconstruct the foundry." — [Lodge, About page, accessed 2026-11-07](https://www.lodgecastiron.com/pages/about-lodge)
  - Since: not applicable (founded 1896)
  - Model: "We currently operate two foundries in South Pittsburg, Tennessee, our home since the very beginning." — [Lodge, About page](https://www.lodgecastiron.com/pages/about-lodge)
  - Affiliate: none found. The site's "Affiliations" page lists trade associations and is not an affiliate program.
  - BDC names: "Lodge Manufacturing Company", "Lodge Cast Iron"
  - Notes: the About page calls Lodge's values "family values" but never says who owns the company today.
- **CK4 GreenPan**
  - Owner: "Like a lot of childhood friends, Jan Helskens and Wim De Veirman wanted to transform the world together." … "So, they created The Cookware Company and showed the world it’s possible to cook PFAS-free." — [GreenPan US, "A Greener Pan" page, accessed 2026-11-07](https://www.greenpan.us/pages/a-greener-pan)
  - HQ: "The Cookware Company has headquarters in Belgium with offices in New York, Hong Kong, Holland, Germany, and the UK." — [same page](https://www.greenpan.us/pages/a-greener-pan)
  - Since: "We changed the way people cook when we pioneered healthy ceramic nonstick in 2007." — [same page](https://www.greenpan.us/pages/a-greener-pan)
  - Model: brand of a manufacturer, sold DTC and through retail
  - Affiliate: "We’d love for you to join our affiliate community and share your experience with GreenPan and educate your readers and followers about our brand." — [GreenPan US, Affiliate page, accessed 2026-11-07](https://www.greenpan.us/pages/affiliate)
  - BDC names: "The Cookware Company", "The Cookware Company (USA), LLC", "GreenPan"
  - Notes: the site's brand menu lists "Bobby Flay by GreenPan", "Tucci by GreenPan", "Merten & Storck" and "GreenLife". The page names the founders but not the current owners.
- **CK5 Caraway**
  - Owner: "today announced that it has raised a $35M investment led by McCarthy Capital." — [McCarthy Capital (now M-One Capital), release "Caraway Closes $35M Investment to Introduce New Product Offerings and Expand Retail Footprint", NEW YORK, September 28, 2022](https://www.mccarthycapital.com/caraway-closes-35m-investment-to-introduce-new-product-offerings-and-expand-retail-footprint/)
  - Owner kind: "McCarthy Partners Management, LLC is a registered investment advisor that conducts business as McCarthy Capital." and "The firm rebranded to M-One Capital in 2025 (formerly McCarthy Capital)." — [same release](https://www.mccarthycapital.com/caraway-closes-35m-investment-to-introduce-new-product-offerings-and-expand-retail-footprint/)
  - Current: "Caraway Investment Type Recapitalization & Growth Leadership Jordan Nathan Founder & CEO" — [M-One Capital, Portfolio page, accessed 2026-11-07](https://www.m-onecapital.com/portfolio/). The Caraway tile sits inside the page's "Current Investments" section; that section div comes before the "Realized" section in the HTML.
  - Since: "NEW YORK, September 28, 2022" (release dateline) — [McCarthy Capital release](https://www.mccarthycapital.com/caraway-closes-35m-investment-to-introduce-new-product-offerings-and-expand-retail-footprint/)
  - Model: "Caraway is a digitally native, omnichannel provider of ceramic, non-toxic and nonstick cookware and bakeware." — [M-One Capital, Portfolio page](https://www.m-onecapital.com/portfolio/)
  - Affiliate: "We pay a commission on every sale from our website." — [Caraway, Affiliate page, accessed 2026-11-07](https://www.carawayhome.com/pages/affiliate)
  - BDC names: "Caraway Home, Inc.", "Caraway"
  - Notes:
    - Counted as PE-owned under the "no stated stake" rule. The release describes a funding round "led by" McCarthy, so the stake may be a minority; "Recapitalization" on the tile could mean more. Neither source states a percentage.
    - Whether McCarthy or M-One reports PE funds on Form ADV is for the assembler.
- **CK6 Tramontina**
  - Owner: "The small blacksmith’s shop founded by Valentin and Elisa Tramontina in 1911, in the south of Brazil, was the origin of a group that upholds the century-old vocation of delighting with simple gestures." — [Tramontina Global, About page, accessed 2026-11-07](https://global.tramontina.com/en/about)
  - Since: not applicable (founded 1911)
  - Model: "As a vertically integrated manufacturer founded in 1911, it produces these lines in its own factories, from stainless steel pans to forged knives." — [Tramontina US store, /about-us, accessed 2026-11-07](https://www.tramontina.com/about-us)
  - Affiliate: none found (US store homepage and about page checked)
  - BDC names: "Tramontina USA, Inc.", "Tramontina S.A."
  - Notes: no page read says "family-owned"; Wikipedia (not cited) does.
- **CK7 All-Clad**
  - Owner: "Groupe SEB Brands All-Clad Harnessing its heritage as a metalworking artisan founded in Canonsburg, USA, All-Clad innovates continuously to meet the broad range of needs of the most demanding cooks through top-quality products." — [Groupe SEB, All-Clad brand page, accessed 2026-11-07](https://www.groupeseb.com/en/all-clad)
  - US entity: "are made between All-Clad a company of GROUPE SEB USA" — [All-Clad, Terms of Sale, accessed 2026-11-07](https://www.all-clad.com/terms-of-sale)
  - Listing: "Listing Euronext Paris, Compartment A Introduction date 27 May 1975" and "Bloomberg : SK.FP" — [Groupe SEB, SEB Share page, accessed 2026-11-07](https://www.groupeseb.com/en/seb-share). The same page lists the index "Euronext Family Business".
  - Since: not checked (trade sources say 2004)
  - Model: brand of a manufacturer, sold DTC and through retail
  - 5% holders: not checked. They would be in the 2025 Universal Registration Document, which was not fetched.
  - Affiliate: "Through our partnership with CJ Affiliate, we offer competitive commissions, proven conversion rates, and dedicated support to help you succeed." — [All-Clad, Affiliate Program page, accessed 2026-11-07](https://www.all-clad.com/all-clad-affiliate-program)
  - BDC names: "Groupe SEB", "SEB S.A.", "Groupe SEB USA", "All-Clad Metalcrafters"
- **CK8 Made In**
  - Owner: "KarpReilly, a consumer-focused private equity firm who focuses on growing new brands, lead the round." — [KarpReilly, news "Made in announces closing of series A funding", 2017 / Oct / 30](https://www.karpreilly.com/made-in-announces-closing-of-series-a-funding/)
  - Since: "New York, New York (October 30, 2017) – Made In, the direct-to-consumer cookware brand that launched in September 2017, announced the closing of a $1.33M Series A funding." — [same release](https://www.karpreilly.com/made-in-announces-closing-of-series-a-funding/)
  - Current: the "Made In" tile on [KarpReilly, Portfolio page, accessed 2026-11-07](https://www.karpreilly.com/portfolio/) carries `data-category="current-investments branded-products digitally-native-brands"`. That is an HTML attribute, not page text. The page footer says "The portfolio listed herein is a sample of investments made by the founders of KarpReilly, LLC."
  - Model: DTC plus Amazon (ranking source)
  - Affiliate: none found on the brand site (`/pages/affiliate`, `/pages/affiliates` and `/pages/affiliate-program` returned 404). Directory listings (FlexOffers, LinkClicky) say the program runs on Impact; not opened.
  - BDC names: "Made In Cookware", "Made In"
  - Notes:
    - PE-owned under the "no stated stake" rule. The 2017 round was $1.33M and "also included various private investors", so KarpReilly may hold a minority.
    - A 2019 seed round led by Bonobos founder Brian Spaly is reported in search results (not cited).
- **CK9 OXO**
  - Owner: "Our portfolio of brands includes OXO, Hydro Flask, Osprey, Vicks, Braun, Honeywell, PUR, Hot Tools, Drybar, Curlsmith, Revlon and Olive & June, among others." — [Helen of Troy Limited, Form 10-K FY2026 (FYE 2026-02-28), filed 2026-04-23](https://www.sec.gov/Archives/edgar/data/916789/000091678926000048/hele-20260228.htm). In the same filing's trademark table, OXO appears under "Owned".
  - Listing: "Our common stock is listed on the NASDAQ Global Select Market under symbol: HELE." — [same 10-K](https://www.sec.gov/Archives/edgar/data/916789/000091678926000048/hele-20260228.htm)
  - Since: not checked
  - Model: "Our innovative products for home activities include food preparation and storage, cooking, cleaning, organization and beverage service." — [same 10-K](https://www.sec.gov/Archives/edgar/data/916789/000091678926000048/hele-20260228.htm)
  - 5% holders: "each person known to the Company to be the beneficial owner of more than five percent of the Common Stock" — [Helen of Troy, DEF 14A, filed 2026-06-24](https://www.sec.gov/Archives/edgar/data/916789/000091678926000088/hele-20260623.htm). The table lists BlackRock, Inc. 6.90%, JPMorgan Chase & Co. 5.06%, RWWM, Inc. 5.04% and Vanguard Capital Management LLC 5.00%.
  - Affiliate: probable. A search returned the brand page https://www.oxo.com/oxo-affiliate-program, whose snippet says the program runs through Impact. oxo.com returned 403 to curl and WebFetch, so the page was not read.
  - BDC names: "Helen of Troy Limited", "Helen of Troy L.P.", "OXO International"
  - Notes: RWWM, Inc. (Rocklin, CA): type not confirmed; Form ADV is for the assembler.
- **CK10 Blue Diamond**
  - Owner: not found. The homepage footer says "© Blue Diamond" — [Blue Diamond, homepage, accessed 2026-11-07](https://www.bluediamondpan.com/). Curl got 404 for /pages/terms-of-sale (with and without www) and /pages/warranty, and WebFetch got 404 for the terms page.
  - Since: not found
  - Model: not found
  - Affiliate: none found (homepage)
  - BDC names: "Blue Diamond", "The Cookware Company (USA), LLC" (lead only)
  - Notes: 5 fetches. Blue Diamond is widely reported as a Cookware Company brand (trade press, not cited), but the GreenPan site's brand menu does not list it, and no page read ties it to The Cookware Company.
- **CK11 Anolon**
  - Owner: Meyer's brand list: "Our Brands Hestan Ruffoni Anolon Circulon Meyer Great Jones Farberware Ayesha Curry Rachael Ray KitchenAid Anyday LockNLock Bonjour" (menu text) under "A portfolio of kitchenware brands for every chef and any kitchen" — [Meyer Corporation, U.S., Brands page, accessed 2026-11-07](https://meyerus.com/brands/)
  - Owner kind: "Inspired by our founder Stanley Cheng’s passion for engineering and good food, we’ve been reinventing and reimagining cookware so that you can focus on the joys of cooking great meals." — [Meyer, About page, accessed 2026-11-07](https://meyerus.com/about/). The homepage shows "Stanley Cheng CEO" and the address "Meyer Corporation U.S. 1 Meyer Plaza Vallejo, CA 94590" — [Meyer, homepage](https://meyerus.com/)
  - Trademark: "Meyer Is A Registered Trademark of Meyer Manufacturing Company Limited" — [Meyer, About page](https://meyerus.com/about/)
  - Since: not checked
  - Model: "Since 1972, Meyer has manufactured all types of cookware, controlling the entire process from raw materials to finished products." — [Meyer, About page](https://meyerus.com/about/)
  - Affiliate: none found (anolon.com homepage)
  - BDC names: "Meyer Corporation, U.S.", "Meyer Manufacturing Company Limited"
  - Notes: no page read says who owns Meyer. It is founder-led.
- **CK12 Calphalon**
  - Owner: "Gourmet cookware, bakeware and cutlery are sold under the Calphalon brand." — [Newell Brands Inc., Form 10-K FY2025, filed 2026-02-13](https://www.sec.gov/Archives/edgar/data/814453/000081445326000008/nwl-20251231.htm). The same filing lists Calphalon among the "Key Brands" of the Home and Commercial Solutions segment.
  - Listing: "Common Stock, $1 par value per share NWL Nasdaq Stock Market LLC" — [same 10-K, cover table](https://www.sec.gov/Archives/edgar/data/814453/000081445326000008/nwl-20251231.htm)
  - Since: not checked
  - Model: brand of a consumer-products company
  - 5% holders: "the only persons or groups that are known to the Company to be beneficial owners of more than 5% of the outstanding common stock are:" — [Newell Brands, DEF 14A, filed 2026-03-26](https://www.sec.gov/Archives/edgar/data/814453/000119312526126289/d52719ddef14a.htm). The table lists BlackRock, Inc. 13.5%, Pzena Investment Management, LLC 11.6% and The Vanguard Group, Inc. 10.6%.
  - Affiliate: network listing only. FlexOffers' Newell Brands and Calphalon program pages surfaced in search and were not opened; calphalon.com returned 403.
  - BDC names: "Newell Brands Inc.", "Calphalon Corporation"
- **CK13 CAROTE**
  - Owner: the company's investor page lists the entry "VOLUNTARY ANNOUNCEMENT PROPOSED INCREASE IN SHAREHOLDING BY CONTROLLING SHAREHOLDER" (2025/09/29) and "Announcement of Final Offer Price and Allotment Results" (2024/09/30) — [CAROTE, Announcements and Circulars page, accessed 2026-11-07](https://www.mycarote.com/pages/announcements-and-circulars)
  - Ticker: 2549 (HKEX). This comes from the HKEXnews filing index; the PDF (https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0926/2025092602730.pdf, 2025 interim report) was downloaded, but its text could not be extracted here.
  - Since: IPO 2024-10 (allotment results 2024-09-30, as listed above)
  - Model: Amazon-native brand (Similarweb, ranking only)
  - Affiliate: none found (homepage)
  - BDC names: "Carote Ltd", "Carote USA LLC", "Zhejiang Carote"
  - Notes: 5 fetches plus 2 searches. Search results (not cited) name Zhang Guodong as chairman. Bloomberg (not cited) reported that Hillhouse and Shunwei joined the IPO. Neither stake is known, and the controlling shareholder's name was not read from a primary page.
- **CK14 Circulon**
  - Owner: on Meyer's brand list — [Meyer, Brands page](https://meyerus.com/brands/) (see CK11)
  - Since: not checked
  - Model: brand of a manufacturer
  - Affiliate: none found (circulon.com homepage)
  - BDC names: "Meyer Corporation, U.S."
- **CK15 Farberware**
  - Owner (cookware): on Meyer's brand list — [Meyer, Brands page](https://meyerus.com/brands/) (see CK11). Meyer's Farberware page says: "We make trusted, well-loved and well-used cookware for everyone who takes care of their families through food." — [Meyer, Farberware brand page, accessed 2026-11-07](https://meyerus.com/brands/farberware/)
  - Other licensee: "The Company holds certain rights to use the Farberware brand for kitchen tools, cutlery, cutting boards, shears and certain other products which together represent a material portion of its sales, through a fully-paid, royalty-free license for a term that expires in 2195" — [Lifetime Brands, Inc., Form 10-K FY2025, filed 2026-03-12](https://www.sec.gov/Archives/edgar/data/874396/000087439626000008/lcut-20251231.htm)
  - Since: not checked
  - Model: licensed name across product lines. Meyer makes the cookware; Lifetime makes tools and cutlery. The trademark owner is not named in the pages read.
  - Affiliate: none found (farberwarecookware.com homepage)
  - BDC names: "Meyer Corporation, U.S.", "Lifetime Brands, Inc.", "Farberware Licensing Company"
  - Notes:
    - Lifetime Brands (LCUT) is not a row: its Farberware products are tools and cutlery, not cookware. Its DEF 14A ([filed 2026-04-24](https://www.sec.gov/Archives/edgar/data/874396/000119312526177145/d27361ddef14a.htm)) lists "Centre Partners V, L.P." at 26.2%, "JB Capital Partners L.P." at 7.1% and "Mill Road Capital II, L.P." at 5.3%.
    - If the developer counts the tools licensee, Farberware would have a PE minority holder via Centre Partners. It is not counted here.
- **CK16 Gotham Steel**
  - Owner: "© 2026 Emson, Inc." (site footer) — [Gotham Steel, homepage, accessed 2026-11-07](https://www.gothamsteel.com/)
  - Since: not found
  - Model: TV and mass-retail brand (product site)
  - Affiliate: none found (homepage)
  - BDC names: "Emson, Inc.", "E. Mishan & Sons, Inc."
  - Notes: search results (retail listings, a 2019 class action; not cited) name E. Mishan & Sons, Inc. as the company behind Emson. Emson's owner is not stated.
- **CK17 Great Jones**
  - Owner: on Meyer's brand list — [Meyer, Brands page](https://meyerus.com/brands/). Meyer's Great Jones page says: "In November 2018, Great Jones launched with a small team in an even smaller office in Greenwich Village." — [Meyer, Great Jones brand page, accessed 2026-11-07](https://meyerus.com/brands/great-jones/)
  - Since: not found. A search snippet (not cited) says "In June 2023, Great Jones was acquired by Hestan".
  - Model: DTC brand within Meyer
  - Affiliate: "We're always excited to welcome new members to our affiliate network." — [Great Jones, Affiliates page, accessed 2026-11-07](https://greatjonesgoods.com/pages/affiliates)
  - BDC names: "Meyer Corporation, U.S.", "Great Jones Goods"
- **CK18 GreenLife**
  - Owner: "purchasing the products and The Cookware Company (USA), LLC" (the Terms of Sale on the homepage name it as Seller) — [GreenLife, homepage, accessed 2026-11-07](https://www.greenlife-cookware.com/)
  - Also listed in GreenPan's brand menu ("GreenLife") — [GreenPan US](https://www.greenpan.us/pages/a-greener-pan)
  - Since: not checked
  - Model: brand of a manufacturer
  - Affiliate: none found (homepage)
  - BDC names: "The Cookware Company (USA), LLC"
- **CK19 Hestan**
  - Owner: on Meyer's brand list — [Meyer, Brands page](https://meyerus.com/brands/). Meyer's Hestan page says: "Hestan Culinary now proudly presents three product lines handcrafted in Italy that deliver this unparalleled performance excellence- without forsaking beauty." — [Meyer, Hestan brand page, accessed 2026-11-07](https://meyerus.com/brands/hestan/)
  - Since: not checked. The same page shows "Founded In 1996".
  - Model: brand of a manufacturer. The homepage lists "Hestan Commercial Corporation" among Meyer's US locations — [Meyer, homepage](https://meyerus.com/).
  - Affiliate: "We are forging new culinary ground in the cookware space and would like to invite you to be a part of it by joining our affiliate program." — [Hestan Culinary, Affiliate Program page, accessed 2026-11-07](https://hestanculinary.com/pages/affiliate-program)
  - BDC names: "Hestan Culinary", "Hestan Commercial Corporation", "Meyer Corporation, U.S."
- **CK20 KitchenAid (cookware)**
  - Brand owner: "Whirlpool is the owner of a number of trademarks in the United States and foreign countries." and "We receive royalties from licensing our trademarks to third parties who manufacture, sell and service certain products bearing the Whirlpool, Maytag, KitchenAid and Amana brand names." — [Whirlpool Corp, Form 10-K FY2025, filed 2026-02-11](https://www.sec.gov/Archives/edgar/data/106640/000010664026000009/whr-20251231.htm)
  - Cookware line: "From sets to individual pieces, KitchenAid cookware features bases designed to fuel creativity with better temperature control." — [Meyer, KitchenAid brand page, accessed 2026-11-07](https://meyerus.com/brands/kitchenaid/) (on Meyer's brand list)
  - Listing: "Common stock, par value $1 per share WHR New York Stock Exchange and NYSE Texas" — [Whirlpool 10-K, cover table](https://www.sec.gov/Archives/edgar/data/106640/000010664026000009/whr-20251231.htm)
  - 5% holders: "the only persons known by us as of February 20, 2026 to beneficially own more than 5% of our common stock" — [Whirlpool, DEF 14A, filed 2026-03-10](https://www.sec.gov/Archives/edgar/data/106640/000119312526100387/d41071ddef14a.htm). The table lists BlackRock 11.01%, The Vanguard Group 9.73%, Appaloosa LP 6.92%, PRIMECAP Management Company 6.75% and FMR LLC 5.66%.
  - Since: not checked
  - Model: licensed name. Lifetime Brands also licenses KitchenAid for "kitchen tools, cutlery and bakeware" (license expires December 2026) — [Lifetime Brands 10-K FY2025](https://www.sec.gov/Archives/edgar/data/874396/000087439626000008/lcut-20251231.htm).
  - Affiliate: not checked
  - BDC names: "Whirlpool Corporation", "Meyer Corporation, U.S."
  - Notes: counted as a public row (brand owner). The cookware business itself is run by a private licensee, Meyer, so neither side is PE.
- **CK21 Le Creuset**
  - Owner: not found. The site footer reads "© 1977- Le Creuset of America, Inc. All Rights Reserved." — [Le Creuset, About page, accessed 2026-11-07](https://www.lecreuset.com/about-le-creuset.html). The About page is brand history with no ownership sentence.
  - Since: not found
  - Model: brand of a manufacturer, sold DTC, in its own stores and through retail
  - Affiliate: "Earn referral fees of up to 10% on hundreds of classic, durable and innovative kitchen products." — [Le Creuset, Affiliates page, accessed 2026-11-07](https://www.lecreuset.com/affiliates.html)
  - BDC names: "Le Creuset of America, Inc.", "Le Creuset"
  - Notes: 1 search, 3 fetches (robots.txt, a 404, About) plus Affiliates. Trade press and Wikipedia (not cited) say Paul van Zuydam bought the company in 1988 and that it is privately held.
- **CK22 Martha Stewart**
  - Owner: "On June 10, 2019, Sequential Brands Group, Inc. (“Sequential” or the “Company”) completed its previously announced sale of 100% of the issued and outstanding equity interests of Martha Stewart Living Omnimedia, Inc." … "to Marquee Brands LLC (the “Buyer”)." — [Sequential Brands Group, Form 8-K, filed 2019-06-13](https://www.sec.gov/Archives/edgar/data/1648428/000155837019005681/sqbg-20190610x8k.htm)
  - Current: "Marquee Brands is a consumer-centric brand licensing platform that owns the Intellectual Property of well-recognised global brands, including Martha Stewart, Emeril Lagasse, Sur La Table, Motherhood Maternity, A Pea in the Pod, Dakine, Body Glove, BCBG Max Azria, BCBGeneration, Ben Sherman and Bruno Magli." — [Neuberger Private Equity Partners (NBPE), "Marquee Brands Case Study", accessed 2026-11-07](https://nbprivateequitypartners.com/en/case-studies/marquee-brands-case-study)
  - PE in chain: "Investment Date December 2014 Lead Investor Neuberger Berman" (overview fields, same page). The page shows NBPE's own holding as "Percent of Fair Value 3%" and "$35.5m Value of Investment". Neuberger's total stake in Marquee is not stated.
  - Since: 2019-06-10 (Marquee); Neuberger since December 2014
  - Model: "The Company generates revenue through royalty payments from third-party licensor partners who manufacture and distribute the products branded under the owned Intellectual Property as well as from internally managed e-commerce DTC platforms." — [NBPE case study](https://nbprivateequitypartners.com/en/case-studies/marquee-brands-case-study)
  - Affiliate: not checked
  - BDC names: "Marquee Brands LLC", "Marquee Brands Holdings", "Martha Stewart Living Omnimedia, Inc."
  - Notes:
    - The licensee that makes Martha Stewart cookware was not identified.
    - NBPE is a listed PE fund managed by Neuberger.
    - Counted as PE-owned (no stated stake) via Marquee.
- **CK23 Misen**
  - Owner: not found
  - Since: not found
  - Model: DTC
  - Affiliate: none found (homepage; a /pages/partnerships link was not opened)
  - BDC names: "Misen Inc.", "Misen"
  - Notes: 1 search plus 2 EDGAR full-text searches (`"Misen" cookware` in Forms C/D, and `"Misen" "knife"` since 2024-06), both 0 hits. Directory pages (not cited) report venture funding and a 2025 crowdfunding round.
- **CK24 Ninja (cookware)**
  - Owner: "Cooking and Beverage Appliances, which includes air fryers, multi-cookers, outdoor and countertop grills and ovens, propane grills, fire pits, coffee systems, carbonation, cookware, cutlery, kettles, toasters and bakeware" — [SharkNinja, Inc., Form 10-K FY2025, filed 2026-03-02](https://www.sec.gov/Archives/edgar/data/1957132/000195713226000015/sharkninja-20251231.htm)
  - Listing: "Our ordinary shares have been listed on the New York Stock Exchange under the symbol “SN” since July 31, 2023." — [same 10-K](https://www.sec.gov/Archives/edgar/data/1957132/000195713226000015/sharkninja-20251231.htm)
  - 5% holders: "each person or group known to us to beneficially own more than 5% of our Ordinary Shares" — [SharkNinja, DEF 14A, filed 2026-04-27](https://www.sec.gov/Archives/edgar/data/1957132/000195713226000022/sharkninja-20260427.htm). The table lists CJ Xuning Wang 38.6% (mostly through JS&W Group Holdings Limited Partnership) and FMR LLC 14.7%.
  - Since: not applicable
  - Model: brand of a consumer-products company
  - Affiliate: "Powered by Impact, our program makes it easy for you start promoting our products on your site." and "Up to 20% commission on sales" — [SharkNinja, Affiliate page, accessed 2026-11-07](https://www.sharkninja.com/affiliate.html) (linked from ninjakitchen.com)
  - BDC names: "SharkNinja, Inc.", "SharkNinja Operating LLC"
- **CK25 Our Place**
  - Owner: not found
  - Since: not found
  - Model: DTC plus retail (the site has a /pages/retail page; not opened)
  - Affiliate: none found. The homepage links /pages/refer-a-friend, a customer referral scheme and not an affiliate program.
  - BDC names: "Our Place", "From Our Place"
  - Notes: 1 search, 2 fetches. Trade press (not cited) names co-founders Shiza Shahid and Amir Tehrani and venture investors (Dreamers VC, FabFitFun's venture arm). No primary page stating ownership was found.
- **CK26 Pioneer Woman**
  - Owner: not found
  - Since: not found
  - Model: per trade press (not cited), a licensed line made by Gibson Overseas and sold exclusively at Walmart since 2015
  - Affiliate: not checked
  - BDC names: "Gibson Overseas, Inc.", "Gibson Homewares"
  - Notes: 1 search, no fetch. Walmart's 2015 release came up in search only as reprints.
- **CK27 Rachael Ray (cookware)**
  - Owner: on Meyer's brand list — [Meyer, Brands page](https://meyerus.com/brands/). Meyer's page says: "Rachael Ray brings an easy, no-fuss approach to cooking that has inspired people to get in the kitchen." — [Meyer, Rachael Ray brand page, accessed 2026-11-07](https://meyerus.com/brands/rachael-ray/)
  - Since: not checked
  - Model: celebrity-named line made by Meyer. The license terms are not stated.
  - Affiliate: not checked
  - BDC names: "Meyer Corporation, U.S."
- **CK28 Staub**
  - Owner: "2008 Acquisition of the French cookware manufacturer STAUB." and "Since 1970 ZWILLING has belonged to the Werhahn Group" — [ZWILLING, About the group page (US site), accessed 2026-11-07](https://www.zwilling.com/us/about-us/article-about-the-group-zwilling-group.html)
  - Owner kind: "Like ZWILLING, Werhahn is a family company with a long tradition that shares our values and innovative thinking." — [same page](https://www.zwilling.com/us/about-us/article-about-the-group-zwilling-group.html)
  - Since: 2008 (same page)
  - Model: brand of a manufacturer
  - Affiliate: "Our affiliate programs give culinary enthusiasts the opportunity to promote our brands and products while earning commissions." — [ZWILLING US, Affiliate Program page, accessed 2026-11-07](https://www.zwilling.com/us/magazine/affiliate-program.html). It is a ZWILLING Group program ("promote our brands"). The page does not name Staub in the text read, so the row is marked as a group program.
  - BDC names: "ZWILLING J.A. Henckels", "Staub USA", "Wilh. Werhahn KG"
- **CK29 T-fal**
  - Owner: "T-fal, part of Cook Groupe SEB brands, is a French pioneer in cookware and small appliances with a strong presence in the U.S. market." — [T-fal, Affiliate Program page, accessed 2026-11-07](https://www.t-fal.com/affiliate-program)
  - US entity: "ALL WARRANTIES ONLY APPLY TO PRODUCTS WHICH ARE MANUFACTURED AND SOLD AS T-FAL PRODUCTS BY GROUPE SEB USA OR AN AUTHORIZED RESELLER." — [T-fal, Terms of Sale, accessed 2026-11-07](https://www.t-fal.com/terms-of-sale)
  - Listing: see CK7 (Euronext Paris, SK)
  - Since: not checked
  - Model: brand of a manufacturer, sold DTC and through retail
  - Affiliate: "Through our partnership with CJ Affiliate, we provide competitive commissions, high-demand products, and dedicated support to help you maximize performance and revenue." — [T-fal, Affiliate Program page](https://www.t-fal.com/affiliate-program)
  - BDC names: "Groupe SEB USA", "SEB S.A."
- **CK30 Zwilling (incl. Henckels cookware)**
  - Owner: "1970 Wilh. Werhahn KG becomes the sole shareholder." and "Like ZWILLING, Werhahn is a family company with a long tradition that shares our values and innovative thinking." — [ZWILLING, About the group page (US site), accessed 2026-11-07](https://www.zwilling.com/us/about-us/article-about-the-group-zwilling-group.html)
  - Since: 1970 (same page)
  - Model: brand of a manufacturer
  - Affiliate: "Our affiliate programs give culinary enthusiasts the opportunity to promote our brands and products while earning commissions." — [ZWILLING US, Affiliate Program page](https://www.zwilling.com/us/magazine/affiliate-program.html)
  - BDC names: "ZWILLING J.A. Henckels", "Zwilling J.A. Henckels, LLC", "Wilh. Werhahn KG"

### Rollups and groups that are not brands
Not counted in the 30. Each one groups brands under a name that no consumer sees on cookware.
- **Meyer Corporation, U.S. / Meyer Manufacturing Company Limited (Hong Kong):** groups Anolon, Circulon, Farberware (cookware), Rachael Ray, KitchenAid (cookware), Hestan, Great Jones, Ayesha Curry, Ruffoni and others (CK11). Owner: not stated; the founder, Stanley Cheng, is CEO.
- **Groupe SEB / Groupe SEB USA:** groups All-Clad, T-fal (Tefal), Krups, Rowenta and others. Owner: public on Euronext Paris (SK); 5%+ holders not read (CK7, CK29).
- **ZWILLING J.A. Henckels AG / Werhahn Group:** groups Zwilling, Henckels, Staub, Ballarini, Demeyere and Miyabi. Owner: Wilh. Werhahn KG, a family company, sole shareholder since 1970 (CK28, CK30).
- **The Cookware Company / The Cookware Company (USA), LLC:** groups GreenPan, GreenLife and Merten & Storck (and, per trade press, Blue Diamond). Owner: not stated; the founders are named (CK4, CK18).
- **Conair (Conair Corporation / Conair LLC):** groups Cuisinart, Conair, BaByliss, Scunci and Waring. Owner: affiliates of American Securities, with a Rizzuto family minority (CK2).
- **Newell Brands Inc.:** Calphalon's parent. Public (NWL) (CK12).
- **Helen of Troy Limited:** OXO's parent. Public (HELE) (CK9).
- **Marquee Brands LLC:** brand licensor that owns the Martha Stewart, Emeril Lagasse and Sur La Table IP. Owner: Neuberger Berman is lead investor (CK22).
- **Emson, Inc.** (E. Mishan & Sons per search, not confirmed): Gotham Steel's seller. Owner not stated (CK16).
- **Lifetime Brands, Inc.:** licensee of Farberware and KitchenAid for tools, cutlery and bakeware, not cookware. Public (LCUT); Centre Partners V, L.P. holds 26.2% (CK15).

### Category share
**All rows (N = 30; 10 ranked, 20 unranked).**
- **PE-owned (control, or no stated stake): 4 / 30 = 13.3%**
  - Cuisinart: American Securities via Conair, control stated (2021).
  - Martha Stewart: Marquee Brands, with Neuberger Berman as lead investor; stake not stated.
  - Caraway: M-One Capital / McCarthy Capital, "Current Investments"; stake not stated (2022 round "led by").
  - Made In: KarpReilly, "current-investments"; stake not stated (2017 Series A lead).
- **PE minority stake: 0.** PE-owned plus minority = **4 / 30 = 13.3%.**
  - **Sensitivity:** if the two round-led investments (Caraway, Made In) are read as minority stakes, the split becomes 2 PE-owned and 2 PE minority. The combined 4 / 30 does not change.
- **Public company: 7 / 30 = 23.3%.**
  - The rows: All-Clad and T-fal (Groupe SEB), OXO (Helen of Troy), Calphalon (Newell), KitchenAid (Whirlpool as brand owner), Ninja (SharkNinja) and CAROTE (Carote Ltd, HKEX).
  - No 5%+ holder is a confirmed PE firm yet.
- **Other: 13 / 30 = 43.3%.**
  - **family: 2** (Zwilling, Staub: Werhahn)
  - **private, owner not stated: 11**:
    - Meyer's Anolon, Circulon, Farberware, Great Jones, Hestan and Rachael Ray;
    - Lodge, Tramontina, GreenPan, GreenLife and Gotham Steel.
    - Each names a company or founder, and none shows PE evidence.
- **Not found: 6 / 30 = 20.0%**: HexClad, Blue Diamond, Le Creuset, Misen, Our Place, Pioneer Woman. HexClad and Blue Diamond are ranked rows; together they hold 17.1% of Amazon skillet share.
- **Rows with owner kind settled:** 13 / 30 (43%): the 4 PE rows, the 7 public rows and the 2 family rows.
- **Ranked rows only (N = 10):**
  - PE-owned 3 / 10 (Cuisinart, Caraway, Made In).
  - Public 2 (All-Clad, OXO); private, owner not stated 3 (Lodge, GreenPan, Tramontina); not found 2 (HexClad, Blue Diamond).
- **Strict count:**
  - It stays 4 / 30 until the assembler's Form ADV check.
  - Holders to check: RWWM, Inc. (HELE 5.04%), Pzena Investment Management, LLC (NWL 11.6%), Appaloosa LP (WHR 6.92%) and PRIMECAP Management Company (WHR 6.75%).
  - If any reports PE funds, its row (OXO, Calphalon or KitchenAid) becomes a PE minority stake.
  - Groupe SEB's and Carote's holders were not read.
- **By parent company:** 22 parents.
  - Meyer has 6 rows; Groupe SEB, Zwilling/Werhahn and The Cookware Company have 2 each; the other 16 rows are each their own parent, and each not-found row is counted as its own parent.
  - PE-held parents: 4 / 22 = 18.2% (Conair, Marquee Brands, Caraway, Made In).
- **By sales:** only the ranked rows have a sales figure (Amazon skillets, SmartScout, 2025-07).
  - PE rows hold 17.6 of the top 10's 59.5 share points (29.6%).
  - By the stated annual revenue, they hold $40.1M of $132.9M (30.2%). The source's share and revenue columns don't line up exactly.
  - No all-channel sales figure was found for any private row.
- **Upper bound if leads were confirmed:** no PE lead was found for any not-found row. HexClad's reported investor (Studio Ramsay Global) is a media joint venture. Le Creuset's reported owner is an individual. Our Place and Misen are reported as venture-backed. The upper bound is therefore 4 / 30, unless a venture investor turns out to report PE funds on Form ADV.
- **Sources disagree:** none on owners. There are two framing notes:
  - Caraway: the release says "investment led by"; the portfolio tile says "Recapitalization & Growth".
  - Farberware: two licensees make different products under one name.

**Affiliate income:**
- **Brand-direct programs found (10):**
  - HexClad (up to 15%)
  - GreenPan
  - Caraway
  - All-Clad (CJ)
  - T-fal (CJ)
  - Le Creuset (up to 10%)
  - Great Jones
  - Hestan
  - Ninja (SharkNinja, via Impact, up to 20%)
  - Zwilling (group program, also counted for Staub)
- **Probable (2):** OXO (brand page found in search; 403) and Cuisinart (footer link; 404).
- **Network listings only (2):** Calphalon, Made In.
- **Not checked (4):** KitchenAid, Martha Stewart, Pioneer Woman, Rachael Ray.
- **Overlap with PE:** one PE row (Caraway) has a confirmed brand-direct program. Cuisinart (probable) and Made In (network listing) may add two more, and Martha Stewart was not checked. So in cookware, unlike eyewear, affiliate programs and PE ownership do overlap on DTC brands.

## Firms named
Every investment firm named as an owner or 5%+ holder, as the sources name it (for the assembler's Form ADV check):
- **American Securities**: "American Securities LLC" (Conair release)
- **McCarthy Capital / M-One Capital**: "McCarthy Partners Management, LLC", which "conducts business as McCarthy Capital"; rebranded "M-One Capital" in 2025 (Caraway)
- **KarpReilly**: "KarpReilly", "KarpReilly, LLC" (Made In)
- **Neuberger Berman**: "Neuberger Berman" (lead investor in Marquee Brands); "Neuberger Private Equity Partners Limited" (NBPE, the case-study publisher)
- 5%+ holders of public rows:
  - **Helen of Troy:** BlackRock, Inc.; JPMorgan Chase & Co.; RWWM, Inc.; Vanguard Capital Management LLC.
  - **Newell Brands:** BlackRock, Inc.; Pzena Investment Management, LLC; The Vanguard Group, Inc.
  - **Whirlpool:** BlackRock, Inc.; The Vanguard Group Inc.; Appaloosa LP; PRIMECAP Management Company; FMR LLC.
  - **SharkNinja:** FMR LLC (plus founder CJ Xuning Wang via JS&W Group Holdings Limited Partnership).
- Holders of the tools licensee (not a row, CK15): **Centre Partners V, L.P.** (26.2% of Lifetime Brands; the footnote also names "Taylor Parent" and "Centre Partners LP"); **JB Capital Partners L.P.**; **Mill Road Capital II, L.P.**
- Leads only, from trade press or directories (not cited, not counted):
  - Studio Ramsay Global, Fox Entertainment (HexClad, 2024);
  - Hillhouse and Shunwei (Carote IPO, 2024);
  - Starting Line Ventures and Brian Spaly (Made In seed, 2019);
  - Dreamers VC and FabFitFun (Our Place);
  - Gotham Gal Ventures, Vanterra Ventures, Pilot Growth Equity Partners and Lampros Capital Partners (Misen, per directories);
  - Peugeot Invest (a reported Groupe SEB holder, not confirmed).

## Worker log
- **Time:** start 2026-11-07T16:59:39Z, end 2026-11-07T17:27Z. That is about 28 minutes wall-clock for 30 rows, including the ranking search, writing and the quote self-check.
- **Requests:**
  - WebSearch: 24 (9 for the ranking, 15 for owners and affiliates).
  - WebFetch: 4, none usable. Business Wire returned 403, OXO 403 and Blue Diamond's terms page 404, and the HKEX PDF came back as unreadable compressed streams.
  - Direct HTTP (curl): 151 logged requests plus 1 redirect check, 41 of them robots.txt reads. 20 went to SEC: company tickers ×1, submissions JSON ×5, full-text search ×3, and documents ×11 (5 × 10-K, 5 × DEF 14A, 1 × 8-K). All were HTTP 200 under the contact-free user agent at ≤2 req/s.
  - Status mix (non-SEC, 131 requests): 101 × 200; 4 × 403 (oxo.com, calphalon.com, businesswire.com ×2); 24 × 404 (guessed paths, missing robots.txt files and Blue Diamond subpages); 2 × no response (a wrong Marquee Brands domain).
  - Agent tokens: not metered by this worker.
- **What was fast:**
  - Public parents: four 10-Ks and four DEF 14As settled OXO, Calphalon, Ninja and KitchenAid (brand side) with checkable quotes.
  - Sponsor pages rendered on the server: American Securities, M-One and KarpReilly each settled current status in 1–2 requests. On M-One and KarpReilly, the current-vs-realized split sits in the HTML structure, not the visible text.
  - Meyer's server-rendered brand list settled 6 rows' parent in one request.
  - Groupe SEB's own brand page plus each brand's terms-of-sale page settled All-Clad and T-fal.
  - Affiliate pages on Shopify and Magento brand sites load without JavaScript and are linked from footers.
- **What made brands slow:**
  1. **No usable ranking.** Market-research rankings are paywalled teasers. Circana publishes trends, not brand ranks. Similarweb's free table is the top 5 of a category mixed with appliances. The ranking took 9 searches and about 12 requests, and the only brand-level sales source found is one Amazon-only, skillet-only vendor blog.
  2. **Private founder-led makers that never state an owner:** Meyer, Lodge, Tramontina and The Cookware Company. Their sites name founders and history but not shareholders. Under the ~5-fetch cap they stay "owner not stated", not "not found".
  3. **Deal releases on Business Wire** (HexClad 2024) return 403, and no copy on the company's own site was found.
  4. **Foreign-listed parents:** the holder data for Groupe SEB (Euronext) and Carote (HKEX) sits in PDF registration documents and reports. The HKEX PDF could not be text-extracted here (no PDF library or pdftotext in the environment).
  5. **Licensed names:** Farberware, KitchenAid, Rachael Ray, Martha Stewart and Pioneer Woman split the brand owner from the cookware maker, which takes two sources per row.
  6. **Bot walls:** oxo.com and calphalon.com (403); bluediamondpan.com (404 on every subpage to curl and WebFetch).
- **Which kinds of brands had no primary source for the owner:**
  - VC-backed DTC brands with no sponsor page and no SEC filing: HexClad (its release is behind Business Wire's 403), Our Place, Misen;
  - private heritage makers whose sites never state an owner: Le Creuset (individual owner per trade press);
  - licensed celebrity lines whose licensor is an individual: Pioneer Woman;
  - mass-market brands whose sites show only a copyright line: Blue Diamond.
- **Notes for the assembler:**
  - **No JavaScript-only pages are cited.** Every quoted page was read from curl'd HTML.
  - **HTML-structure facts, not text:**
    - KarpReilly's Made In tile carries `data-category="current-investments …"`.
    - On M-One's portfolio page, the Caraway tile sits inside the "Current Investments" section div, which comes before the "Realized" section.
    - American Securities' Companies page shows "Status: Current" as a filter label.
  - **Field-label quotes:** NBPE's "Investment Date December 2014 Lead Investor Neuberger Berman" and Meyer's brand-menu list are field or menu text with whitespace collapsed. So are the SEC cover-table rows (NWL, WHR).
  - **Tag-boundary spaces:** the text extraction put spaces where tags meet (for example "Caraway , the iconic"). The quotes above avoid those spots. Where a quote can't avoid one, the checker should collapse whitespace before punctuation.
  - **The Le Creuset footer** begins "© 1977-" and is matched from "Le Creuset of America, Inc."
  - **Robots:** mycarote.com and tramontina.com carry robots.txt comments with instructions addressed to AI agents. They were ignored as content.
  - **The HKEX PDF** (Carote 2025 interim report) is the place to read Carote's controlling shareholder, and Groupe SEB's 2025 Universal Registration Document is the place for SEB's holders. Neither was read.
  - **Self-check:** a script string-matched every double-quoted string on the Ranking and Evidence lines against the saved curl text of the page cited on that line. Before matching, it collapsed whitespace, normalized curly quotes and dashes, and dropped spaces before punctuation; text on either side of "…" was matched separately. BDC-name lists and Notes were skipped.
    - Result: 110 of 112 were found. The 2 misses are by design: KarpReilly's `data-category` HTML attribute, and a search snippet marked "not cited" (Great Jones/Hestan, 2023).
    - Negative control: 8 deliberately altered quotes all failed.
    - Pages to check: all are on server-rendered HTML. The pages with the heaviest scripts (hexclad.com, carawayhome.com, greenpan.us) still carry the quoted text in their HTML.
