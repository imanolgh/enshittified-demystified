# Portfolio page types: how PE firm portfolio pages show former holdings

Gathered 2026-11-12 for engine "Rosters, portfolio pages and the registry", to measure how often a portfolio page shows current holdings only. It reuses the 88 open sites of the [portfolio wall survey](portfolio-wall-survey.md) of 2026-11-11 and extends the eight-site [portfolio page survey](portfolio-page-survey.md) of 2026-11-08. Every fact below comes from the page named in its row, fetched on 2026-11-12.

## Method

- **Sites.** The 88 sites whose homepage served in the wall survey (3G Capital included; Kennedy Lewis, Wildcat Capital and Durational Capital left out as wrong domains). The wall survey's raw `survey.json` was no longer in the session scratchpad, so the firm and domain list was rebuilt from that session's own record (its `domains.py` and printed outcomes). Portfolio URLs were found afresh from each homepage's links, not from the wall survey's crude link match.
- **Requests.** httpx 0.28.1, plain HTTP/1.1, user agent `EvidenceEngineBot/0.1 (portfolio survey)` with no contact detail, no JavaScript, no retries. Per site: robots.txt, the homepage, then the portfolio page picked by hand from the homepage's links. Four sites got a fourth fetch: a separate full-list page (BC Partners, Bain), the script file that holds the brand list (Bansk), and the data endpoint behind the list (Garnett Station, which answered 404). robots.txt was parsed with `*` and `$` wildcards, and a URL was fetched only if both the `EvidenceEngineBot` group (none exists on any site) and the `*` group allowed it. The pause between a site's requests was its `Crawl-delay` (capped at 15 s), else 3 s. Redirects were followed one hop at a time, each hop checked against robots.txt and the firm's domain (39 hops, all within the firm's domain).
- **Moved domains.** Gryphon (gryphoninvestors.com to gryphon-inv.com), Percheron (percheroncapital.com to percheron.com), RiverGlade (rivergladecapital.com to riverglade.com) and The Jordan Company (thejordancompany.com to tjclp.com) redirect to new domains of the same firm, and Point72's "Private Investments" page redirects to p72.vc (Point72 Ventures). Each new domain counted as its own site, with robots.txt read first: robots.txt, homepage and portfolio page, three requests (two for Percheron, whose portfolio sits on its homepage). Summit Trail Advisors redirects to corient.com, its acquirer and a different firm, which this survey did not fetch.
- **Totals.** 264 requests to 93 hosts, at most 4 per host. No site served a challenge, 403, 429 or robots refusal.
- **Reading a page.** Text built the way the project will: every text node including hidden elements (script and style bodies dropped), plus each image's `alt`, each link's `title` and each `aria-label`, in place. Separately, every `class`, `id` and `data-*` value holding a status word (current, active, exited, realized, former, past, prior, previous, historical) was counted. Types rest on the HTML as served, since that is what the engine will fetch.
- **Rules applied.** A status filter whose options name former holdings ("Status: All / Active / Exited") counts as the page saying its list mixes current and former; it does not count as marking each item. A heading in the text ("Past Investments", "Former") counts as marking the items under it. Where the items load only by JavaScript, the type rests on what the served HTML says, and the row is marked "inferred". Investments a firm's team made at earlier firms (Whistler, RiverGlade) are not the firm's former holdings.
- Raw pages stayed in the session scratchpad.

## Counts by type

| Type | Sites | Share of 88 | Share of the 73 with a portfolio page |
|---|---|---|---|
| 1. Current only, said in text | 5 | 6% | 7% |
| 2. Current only, not said | 8 | 9% | 11% |
| 3. Current and former, status in text | 26 | 30% | 36% |
| 4. Current and former, status only in markup | 22 | 25% | 30% |
| 5. Mixed, no status | 10 | 11% | 14% |
| 6. Former on a separate page | 2 | 2% | 3% |
| 7. No portfolio page found | 15 | 17% | |
| 8. Blocked | 0 | 0% | |

Five rows rest partly on inference because their items load only by JavaScript: General Atlantic (type 3), Garnett Station and THL (type 5), Percheron and Bansk (type 2). KKR's type rests on its text, though its names also load by JavaScript.

**Pages with no former holdings on them (types 1, 2 and 6): 15 of 73.** Rainier's filter offers "Prior", but its default view serves no prior holding. American Securities' status picker shows "Current", and its other options are not in the HTML. Both type 6 pages link a separate list.

**Portfolio pages that say they show a selection or an incomplete list: 23 of 73**, either in words ("a selection", "not a complete list", "Select Investments") or by stating a larger total than they show ("over 160 investments" over 107 cards): Deerfield, KKR, Blackstone, Centerbridge, Wafra, Wynnchurch, A&M Capital, Cortec, FFL, Leonard Green, M-One, Swander Pace, TRP, TSG, AEA, H.I.G., Harvest, KarpReilly, Sun, BC Partners, Riata, Yellow Wood and Bain. Pages whose stated total matches what they hold across all pages (Peninsula, Point72, CVC, Shore) are not counted.

## Per site

Counts in brackets are current / former. "Served" means the number in the HTML before any JavaScript, paging or "load more". In quotes, " / " marks a break between separate page elements, such as filter options.

### Type 1: current only, said in text

| Firm | Portfolio URL | Deciding quote or markup | Items | Selection statement | Paging or JavaScript |
|---|---|---|---|---|---|
| American Securities | https://www.american-securities.com/companies/ | Filter label "Status:" with the selected value "Current"; no former names in the HTML or the inline page data | 22 | none | other status options load by JavaScript |
| Deerfield Management | https://deerfield.com/what-we-do/investment/portfolio | Every item reads "Current"; the only filter options are "All / Current"; "Exclusions include historical investments" | 15 | "not representative of all of the portfolio companies purchased, sold, or recommended for Deerfield funds" | no |
| KKR | https://www.kkr.com/invest/portfolio | "Learn more about our current portfolio below." | 0 served | "represent a significant portion of KKR's ... portfolio as of August 24, 2026. Certain investments have been excluded" | company directory loads by JavaScript |
| LongRange Capital | https://www.longrangecapital.com/companies | Heading "Current Portfolio" | 5 | none | no |
| Rainier Partners | https://www.rainierpartners.com/portfolio/ | "Our current portfolio represents some of the best middle-market businesses"; each item "Status: Current"; a "STATUS: Current / Prior" filter exists, but no prior item is served | 7 | none | prior items only through the filter |

### Type 2: current only, not said

| Firm | Portfolio URL | Deciding quote or markup | Items | Selection statement | Paging or JavaScript |
|---|---|---|---|---|---|
| Bansk Group | https://www.banskgroup.com/brands.html | Inferred. The served page lists no brands; `js/brandlist.js` holds 11 entries, each `group: 'brand'`, none with a status | 11 | none | names only in a script file |
| Blackstone | https://www.blackstone.com/our-businesses/private-equity/ | "OUR PORTFOLIO" over 7 featured companies, no status | 7 | the page states "Portfolio Companies 105" | no |
| Centerbridge | https://www.centerbridge.com/private-equity | Heading "Select Private Equity Investments", no status | 28 | "Select" | no |
| Percheron Capital | https://percheron.com/ (homepage section) | Inferred. A "Portfolio Companies" table with a header row and no rows in the served HTML | 0 served | none | rows load by JavaScript |
| RiverGlade Capital | https://riverglade.com/investments/ | The firm's own holdings carry no status; a separate section "Prior to RiverGlade" lists the team's earlier deals | 13, plus the prior-firm list | none | no |
| Wafra | https://www.wafra.com/our-strategies/strategic-partnerships/ | Heading "Select Investments" over 29 logos with empty `alt`; no names in the text | 29 | "Select Investments" | no |
| Whistler Capital Partners | https://www.whistlercapital.com/portfolio | 4 "Platform investments" and 9 "Strategic positions", no status; a separate "Prior firm investments" section that "are not investments of Whistler Capital Partners" | 13, plus the prior-firm list | "This is not a complete list of such investments" (of the prior-firm list) | no |
| Wynnchurch Capital | https://www.wynnchurch.com/portfolio | "Our Portfolio", no status | 24 | "do not represent all of the types of investments Wynnchurch has made"; "A comprehensive list of all investments ... is available to qualified prospective investors" | no |

### Type 3: current and former, status in text

| Firm | Portfolio URL | Deciding quote or markup | Items | Selection statement | Paging or JavaScript |
|---|---|---|---|---|---|
| A&M Capital | https://www.a-mcapital.com/ (homepage section) | Labels such as "CURRENT AMCP II" and "REALIZED" on most items; a few (BrightPet Nutrition, Classic Brands) carry none | 57 | "we have invested in over 170 companies" (one strategy) | no |
| Access Holdings | https://accessholdings.com/portfolio/investments/ | Headings "CURRENT PORTFOLIO" and "PREVIOUS PORTFOLIO" | 12 (9 / 3) | none | no |
| Berkshire Partners | https://berkshirepartners.com/private-equity/portfolio/ | Heading "Former" before the former list | 116 (39 / 77) | none | no |
| Centre Partners | https://www.centrepartners.com/our-portfolio | Headings "Current Investments" and "Past Investments" | 89 (16 / 73) | none | no |
| Charlesbank | https://www.charlesbank.com/investments/ | Each card "Current" or "Realized" | 74 (33 / 41) | none | no |
| Cortec Group | https://cortecgroup.com/companies/ | Each card "Exited" or "Owned", e.g. "Fund V / Exited" | 27 served | "Cortec Group has acquired ~60 middle-market platforms" | "load more" by JavaScript |
| Eagle Merchant Partners | https://www.eaglemerchantpartners.com/portfolio | Each item "Current" or "Exited" | 16 (12 / 4) | none | no |
| FFL Partners | https://www.fflpartners.com/portfolio | Each item "current" or "exited" | 28 (18 / 10) | "selected in order to provide examples ... do not purport to be a complete list thereof" | no |
| General Atlantic | https://www.generalatlantic.com/investments/ | Inferred. A "Year Exited" column and a "Current / Past" filter; all 24 served rows show the exit year "1970" | 24 served | none | "Load More" by JavaScript; no former row served |
| Great Hill Partners | https://www.greathillpartners.com/companies | Realized tiles state the exit, e.g. "Acquired by TA Associates", "IPO / Public Stock Sale" | 12 served | none | `?page=N` paging |
| Halifax Group | https://thehalifaxgroup.com/our-portfolio/ | Hidden modals give "Exit Date:" on 25 of the 28 former items; classes `current` and `former` mark all | 44 (16 / 28) | none | no |
| Imperial Capital | https://www.imperialcap.com/investments | Headings "Active investments" and "Realized investments"; items are logos whose names appear only in link slugs | 33 (11 / 22) | none | no |
| Leonard Green & Partners | https://www.leonardgreen.com/portfolio/ | "Status: Current" or "Status: Past" on each card | 107 (68 / 39) | "Since inception, we have made over 160 investments" | no |
| Littlejohn & Co. | https://littlejohnllc.com/investments/ | "Status: Current" or "Status: Realized" on each card | 69 (19 / 50) | none | no |
| M-One Capital | https://www.m-onecapital.com/portfolio/ | Former items "Investment Status: Realized 2026" (54) or "Distributed" (2); current items carry no status field; tabs "Select Current Investments / Select Realized Investments" | about 66 | "Select"; "represent the most recent 10 years, plus relevant prior investments" | tabs by JavaScript, all items in the HTML |
| Peninsula Capital Partners | https://www.peninsulafunds.com/portfolio/ | "Investment Status: Active" or "Inactive" on each item | 154 (28 / 126) | "Over 150 Platform Investments" | no |
| Shore Capital Partners | https://www.shorecp.com/companies | Names suffixed "(Realized)" or "(Merged)", e.g. "BrightView (Realized)" | 23 served; page counts "current 64", "realized 23" | "tested in 60+ platform companies" | the rest by JavaScript |
| SkyKnight Capital | https://www.skyknightcapital.com/investments/ | "CURRENT" or "FORMER" on each card | 23 (17 / 6) | none | no |
| Summit Partners | https://www.summitpartners.com/portfolio | A Status column per row: "Current", "Merger", "IPO", "Exited" | 100 served | none | "load more" by JavaScript |
| Swander Pace Capital | https://spcap.com/portfolio/ | Hidden modals "Status Current" or "Status Realized" | 63 (11 / 52) | "We have partnered with over 100 companies" | no |
| Sycamore Partners | https://www.sycamorepartners.com/investments | Headings "Current Investments" and "Exited Investments"; each item "Current Investment" or "Exited" | 38 (22 / 16) | none | no |
| The Jordan Company | https://tjclp.com/our-portfolio/ | Modals "Status: Current" or "Status: Exited" | 99 (55 / 44) | none | no |
| Trive Capital | https://www.trivecapital.com/portfolio/ | Former items show "Realized Date", e.g. "March 18, 2020" | 68 (40 / 28) | none | no |
| TRP Capital Partners | https://www.trpfund.com/portfolio | Headings "Select Current Portfolio Companies (a)" and "Select Realized Investments (a)" | 28 shown (8 / 20) | "(a) Certain companies excluded for confidentiality reasons. Information for all companies available upon request." | "Show More" by JavaScript |
| TSG Consumer Partners | https://www.tsgconsumer.com/investments/ | Hidden modals "Status Current" or "Status Exited" | 82 (21 / 61) | "a selection of current and former portfolio companies and are not a complete list of TSG investments" | no |
| TZP Group | https://www.tzpgroup.com/portfolio/ | "Current" or "Exited" on each card | 58 (38 / 20) | none | no |

### Type 4: current and former, status only in markup

| Firm | Portfolio URL | Deciding quote or markup | Items | Selection statement | Paging or JavaScript |
|---|---|---|---|---|---|
| ACON Investments | https://aconinvestments.com/portfolio/ | `data-status` "active" or "realized"; one name reads "Waldo's (exited in 2023)" | 69 (33 / 36) | none | no |
| AEA Investors | https://www.aeainvestors.com/portfolio/ | `data-status` ".current." or ".realized." | 118 (59 / 59) | "may not represent a complete list of investments made by AEA" | no |
| Brentwood Associates | https://www.brentwood.com/our-portfolio/ | Classes `stage-current-investment` and `stage-realized-investment` | 56 (23 / 33) | none | no |
| BRS & Co. | https://brs.com/portfolio/ | `data-status` "current" or "exited" | 40 (6 / 34) | none | no |
| Gryphon Investors | https://www.gryphon-inv.com/companies/ | `data-status` "current" or "realized" | 72 (35 / 37) | none on the portfolio page; the homepage says "Gryphon has made 75 platform investments" | no |
| H.I.G. Capital | https://hig.com/portfolio/ | Classes `active` and `realized` | 381 | "H.I.G. Capital has invested in over 400 companies" | no |
| Harvest Partners | https://harvestpartners.com/portfolio-investments/ | `data-status` "current" or "realized" | 72 | "SELECT INVESTMENTS*"; the footnote links a PDF of all investments | no |
| KarpReilly | https://www.karpreilly.com/portfolio/ | `data-category` "current-investments ..." or "realized-investments ..." | 56 (33 / 23) | "a sample of investments ... For a complete list of current and prior investments, please contact" | no |
| Kingswood Capital | https://www.kingswood-capital.com/portfolio/ | Classes `company-status-current` and `company-status-exited` | 24 (21 / 3) | none | no |
| L Catterton | https://www.lcatterton.com/Investments.html | Classes `current` and `historical` | about 326 tiles (169 / 157) | none | names load by JavaScript |
| Linden Capital Partners | https://www.linden.com/portfolio/investments/ | Classes `current` and `past`; detail URLs under `/portfolio/investments/current/` and `/past/` | 47 (28 / 19) | none | no |
| Martis Capital | https://www.martiscapital.com/our-companies/ | Classes `portfolio_category-current`, `-exited` and `-hidden` | 29 (11 / 17, 1 hidden) | none | no |
| New Mountain Capital | https://www.newmountaincapital.com/our-strategies/private-equity/portfolio/ | `data-status` "Fully Realized" or "Current Private Equity ..." | 93 (47 / 46) | none | no |
| North Castle Partners | https://northcastlepartners.com/portfolio/ | Classes `type-current` and `type-historical`; the text says "Our current and historical brand partnerships" | 50 (20 / 30) | none | no |
| Pine Tree Equity | https://www.pinetreeequity.com/equity-partnership-portfolio | Classes `current` and `previous` | 30 (7 / 23) | none | no |
| Point72 | https://p72.vc/portfolio/ (Point72 Ventures) | `data-active` "1" or "0" | 162 (119 / 43) | "Since 2016 we've made more than 130 investments" | no |
| Roark Capital | https://www.roarkcapital.com/portfolio | Sections `portfolio-section--current` and `portfolio-section--previous`; the previous section is hidden by CSS | 86 (56 / 30) | none | no |
| Seidler Equity Partners | https://sepfunds.com/partnerships/ | Classes `company_status-active` and `company_status-exited` | 47 (19 / 28) | none | no |
| Sentinel Capital Partners | https://www.sentinelpartners.com/companies/ | `data-status` ".active." or ".exited." | 99 (28 / 71) | none | no |
| Sun Capital Partners | https://suncappart.com/portfolio/ | `data-strategy` "active" or "prior" | 105 (28 / 77) | "invested in more than 570 companies"; "Our current portfolio of ~30 companies" | no |
| TowerBrook | https://www.towerbrook.com/investments/ | `data-status` "active" or "prior" | 118 (61 / 57) | none | no |
| Valspring Capital | https://www.valspring.com/ (homepage section) | Three galleries (All 27, Current 7, Past 20) that a script switches by section id; names appear only as image file names ("ability.png") | 27 | none | tabs by JavaScript, all items in the HTML |

### Type 5: mixed, no status

| Firm | Portfolio URL | Deciding quote or markup | Items | Selection statement | Paging or JavaScript |
|---|---|---|---|---|---|
| Advent International | https://www.adventinternational.com/investments/ | Filter "All Exit Strategies"; cards carry no status; the name list includes long-exited holdings | 10 per page, 46 pages | none | `?sf_paged=N` |
| BC Partners | https://www.bcpartners.com/portfolio/ | Filter "Investment status / All investment statuses / Partially Realised/Publicly Traded / Realised / Unrealised"; cards carry only sector, strategy and region | 12 per page, 4 pages | "represent a selection of investments made by the last three flagship private equity funds"; a full list at https://www.bcpartners.com/all-investments/ (128 rows, no status) | `page/N` paging |
| Freeman Spogli | https://www.freemanspogli.com/portfolio/ | "Filterd by sector: all and theme: all and status: all. Total posts: 72"; names only in hidden `sr-only` spans | 72 | none | filters by JavaScript |
| Garnett Station Partners | https://garnettstation.com/partnerships/ | Inferred. Filter "Status / All / Active / Exited"; no items in the served HTML | 0 served | none | items load by JavaScript |
| Golden Gate Capital | https://goldengatecap.com/portfolio/ | Filter "Status / All / Active / Exited"; tiles carry no status | 24 served (105 in the 2026-11-08 survey) | none | infinite scroll; `?sf_paged=N` |
| Permira | https://www.permira.com/portfolio/our-portfolio | Filter "Status / All Status / Current / Realised"; item data has no status field | 20 of "111 PORTFOLIO COMPANIES" | none | "load more" by JavaScript |
| Princeton Equity Group | https://princetonequity.com/companies/ | "Filter BY: All / All / Active / Realized"; tiles carry no status | 24 served | none | "load more" |
| Riata Capital Group | https://www.riatacapital.com/portfolio | "Highlighted below are some of the current and former portfolio companies that Riata's principals have sponsored or managed." | 33 | "some of"; "sponsored 47 platform acquisitions" | no |
| Thomas H. Lee Partners | https://thl.com/portfolio/ | Inferred. Filter "Investment Status / Current / Exited"; no items in the served HTML | 0 served | none | items load by JavaScript |
| Yellow Wood Partners | https://www.yellowwoodpartners.com/brands | "Represents current and past brands in the Yellow Wood portfolio that achieved $10 million or more in sales"; all 29 tiles carry class `current` | 29 | "Certain brands have been excluded due to size." | no |

### Type 6: former on a separate page

| Firm | Portfolio URL | Deciding quote or markup | Items | Selection statement | Paging or JavaScript |
|---|---|---|---|---|---|
| Bain Capital Private Equity | https://www.baincapitalprivateequity.com/portfolio | Heading "Current Investments"; separate page https://www.baincapitalprivateequity.com/portfolio/current-and-former-portfolio-companies: "The below list includes all current and former portfolio companies", with no status | 111 current; about 310 names on the full list | "Since 1984, we have completed more than 940 primary and add-on investments" | no |
| CVC Capital Partners | https://www.cvc.com/portfolio/our-portfolio/ | "CVC's PE strategies are invested in over 150 companies worldwide. Our Case Studies page contains information about some of the companies we've partnered with in the past." | about 18 per page, 9 pages | "over 150 companies" | `?page=N` |

### Type 7: no portfolio page found

| Firm | Site | What the site has |
|---|---|---|
| 3G Capital | https://www.3g-capital.com/ | A one-page site with no portfolio |
| BDT & MSD Partners | https://bdtmsd.com/ | "Our solutions" and disclosures only |
| Brigade Capital | https://www.brigadecapital.com/ | Credit manager: strategies, values, team, news |
| Cerberus | https://www.cerberus.com/investment-platforms/private-equity/ | The private equity page cites "75 portfolio companies" but names none |
| Durable Capital Partners | https://durablecapital.com/ | The whole text: "Durable Capital Contact us" |
| Goldman Sachs Asset Management | https://am.gs.com/en-us/advisors | Fund products for advisors |
| JAB | https://www.jabconsumerpartners.com/ | The Luxembourg fund manager's site, no holdings |
| Monarch Alternative Capital | https://www.monarchlp.com/ | Credit and real estate pages |
| Oaktree Capital | https://www.oaktreecapital.com/ | Strategy pages, no company list |
| Pleasant Lake Partners | https://plpfunds.com/ | An investor portal link only |
| Related Companies | https://www.related.com/our-company/businesses | "Our Businesses" lists Related's own divisions and subsidiaries |
| Sculptor | https://www.sculptor.com/ | Credit, real estate and multi-strategy pages |
| Summit Trail Advisors | https://www.summittrail.com/ | Redirects to corient.com, its acquirer; not fetched |
| TPG | https://www.tpg.com/platforms/capital | No portfolio link in the navigation; the capital platform page names no companies |
| Trian | https://trianpartners.com/ | Home, about, press releases, contact |

## Surprises

- **No walls at this step.** All 88 sites, and the 5 moved domains, served robots.txt, homepage and portfolio page to a plain identified request.
- **On type 5 pages, status lives only on the server.** Golden Gate, BC Partners, Permira, Princeton and Freeman Spogli each offer a status filter, but their served items carry no status at all. Golden Gate's own homepage link to "Portfolio" points at `?_sft_status=active`, so a crawler that follows the navigation gets an active-only list.
- **A "current only" page can be a filter default.** Rainier's default view serves only its 7 current holdings, though its filter offers "Prior". American Securities' status picker shows "Current", and its other options are not in the HTML.
- **General Atlantic shows "1970" as the exit year of every current holding**, which looks like an empty date printed as the Unix epoch.
- **Yellow Wood's markup and text disagree.** All 29 tiles carry class `current`, while the note says the list "Represents current and past brands". Its "Past Brands" filter would show nothing.
- **Status as an exit event rather than a status word:** Great Hill ("Acquired by TA Associates", "IPO / Public Stock Sale"), Summit ("Merger", "IPO"), M-One ("Distributed"), Peninsula ("Inactive"), Halifax and Trive (an exit or realized date).
- **Some pages carry no company names in their text.** Imperial puts names only in link slugs, Wafra uses logos with empty `alt`, and Valspring uses image file names as `alt`. L Catterton loads names by JavaScript, and Bansk keeps them in a script file.
- **Team track records sit on two current portfolio pages.** Whistler ("Prior firm investments") and RiverGlade ("Prior to RiverGlade") list deals their people made at earlier firms, labeled in text.
- **Full lists kept off the page:** Harvest (a PDF), Wynnchurch ("available to qualified prospective investors"), KarpReilly ("please contact") and TRP ("available upon request"). BC Partners and Bain publish full lists on separate pages without status.
- **Five firms' domains moved:** Gryphon, Percheron, RiverGlade and The Jordan Company now redirect to new domains, and Summit Trail redirects to its acquirer. Point72's private investments sit on p72.vc.
