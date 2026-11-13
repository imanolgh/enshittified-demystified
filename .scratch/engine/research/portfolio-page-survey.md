# Portfolio page survey: how ten PE firms build their portfolio pages

Gathered 2026-11-08 for engine "Rosters, portfolio pages and the registry". A subagent fetched each site with the user agent `portfolio-structure-survey/0.1` (no contact detail), at most 10 requests per site, with 10 seconds between requests where robots.txt asks for a crawl delay. It stopped at any block. Raw files were kept only in the session scratchpad.

## Per firm

| Firm | Portfolio URL | robots.txt for `*` | Names in raw HTML? | Names as visible text? | Detail pages | Former holdings | Count shown |
|---|---|---|---|---|---|---|---|
| Roark Capital | https://www.roarkcapital.com/portfolio | nothing blocked | yes | no: logo `alt`, and an `<h2>` inside a closed `<dialog>` | none; the sitemap's 86 `/home/<slug>` URLs return 404 (tested /home/subway, /home/arbys) | same HTML, hidden by CSS until "Previous Investments" is clicked | 86 (56 current, 30 previous) |
| Blackstone | (not reached) | robots.txt itself answered 403 with a Cloudflare challenge (`cf-mitigated: challenge`) | | | | | |
| L Catterton | https://www.lcatterton.com/Investments.html | robots.txt 404 (no rules) | no: tiles carry only a slug and an image filename; content loads by JavaScript | no | fragments such as https://www.lcatterton.com/Investments-equinox.html: "Year of Investment 2017 / Investment Status Current / Strategy Flagship Buyout"; P.F. Chang's: "Investment Status IPO: December 1998" | same HTML, CSS classes `current` and `historical`; majority or minority only as a class (`nag_major`, `nag_minor`) | 168 current, 155 historical; also a plain-text "List of L Catterton Transactions" fragment with about 375 names |
| TSG Consumer Partners | https://www.tsgconsumer.com/investments/ | portfolio allowed | yes | no: `alt`, link `title`, `aria-label` | none real: 82 `/investment/<slug>/` URLs redirect (301) to a modal on the listing; modals are hidden by CSS: "Investment Year 2003 / Status Exited / Subsector Food & Beverage" | all shown; `?status=exited` filters on the server | 82 (21 current, 61 exited); the page says the list is "a selection ... not a complete list" |
| Leonard Green & Partners | https://www.leonardgreen.com/portfolio/ | portfolio allowed, `Crawl-delay: 10` | yes | yes, card `<h2>` (the one listing that shows names as text) | sitemap lists 108 `/investments/<slug>/` URLs that return 200 with only a `<title>` | same HTML, all shown, status as text ("Status: Past") | 108 (71 current, 37 past); the site says "over 160 investments" |
| Sycamore Partners | https://www.sycamorepartners.com/investments | robots.txt 404 (no rules) | yes | no: `alt` and `title`; visible text per card is only "Current Investment" or "Exited" | `/investment-info/<slug>` returns the listing; a JavaScript POST fills a modal (content not determined) | two headed sections, both in the raw HTML | 38 (22 current, 16 exited) |
| Warburg Pincus | (not reached) | robots.txt allows `*`; the homepage answered 403 with a Cloudflare challenge | | | | | |
| Bain Capital Private Equity | https://www.baincapitalprivateequity.com/portfolio and .../portfolio/current-and-former-portfolio-companies | portfolio allowed, `Crawl-delay: 10` | yes | /portfolio: logos with `alt`; the full list: a plain-text `<ul>` | none; inline panels hidden by CSS: "Name: 1440 Foods / REGIONS: Americas / INDUSTRY: Consumer / YEAR: 2023" | separate pages; the full list has no status, so former = full list minus current | 111 current; 307 on the full list; the site says "more than 940 primary and add-on investments" |
| Levine Leichtman Capital Partners | https://www.llcp.com/portfolio/ | portfolio allowed | yes | no: `alt` and `aria-label` | yes, `/portfolio/<slug>/`: "Fund: LMM III / Status: Current / ... Date Invested: September 2022 / Date Realized: N/A"; Bertucci's: "Status: Realized ... Date Invested: July 2012 / Date Realized: April 2018" | same HTML, `data-status="current|realized"` | 83 on the listing (33 current, 50 realized); 86 in the sitemap, 3 not on the listing |
| Golden Gate Capital | https://goldengatecap.com/portfolio/ | nothing blocked (its `Crawl-delay: 10` sits outside any group) | first 24 only; the rest by infinite scroll, which a plain GET of `?sf_paged=2` also serves | no: logos with `alt=""` | yes, `/company/<slug>/`: California Pizza Kitchen, "Status: Exited / Year Invested: 2011" | `?_sft_status=active|exited` filters on the server | 105 (22 active, 83 exited); the sitemap lists all 105 company pages |

Newsrooms found: TSG https://www.tsgconsumer.com/news/, Leonard Green https://www.leonardgreen.com/news/, Sycamore https://www.sycamorepartners.com/news, Bain https://www.baincapital.com/news, LLCP https://www.llcp.com/media/, Golden Gate https://goldengatecap.com/news/, L Catterton https://www.lcatterton.com/Press.html (filled by JavaScript from press.json). Roark showed none.

## Across the eight reachable sites

- **Names as visible text on the listing:** 1 of 8 (Leonard Green), plus Bain's separate full-list page. Five put names only in `alt`, `title` or `aria-label` (Roark, TSG, Sycamore, LLCP, Bain /portfolio). Two show no name anywhere on the listing but the URL slug and image filename (Golden Gate, L Catterton).
- **Facts in hidden containers:** Roark (a closed `<dialog>`, and the whole former section hidden by `display:none`), TSG (modals hidden by `visibility:hidden`), Bain (panels hidden by `display:none`).
- **Status only in markup:** L Catterton, TSG, LLCP and Roark mark current or former with a class or data attribute.
- **Detail pages with their own URL and real content:** 2 (LLCP, Golden Gate), plus L Catterton's fragments. Elsewhere, per-company URLs 404, redirect, are empty or repeat the listing.
- **Sitemaps:** useful only at LLCP and Golden Gate. Roark's lists dead URLs; TSG's redirect; Leonard Green's are empty pages.
- **Needs JavaScript for names:** 1 (L Catterton). Golden Gate needs paging through `?sf_paged=N`, which works without JavaScript.
- **Incomplete by the firms' own words:** TSG ("not a complete list"), Leonard Green ("over 160", shows 108), Bain ("940+", lists 307).
- **Blocked for a plain user agent:** 2 of 10 (Blackstone, Warburg Pincus), both by Cloudflare challenge pages.
- **Other traps:** Sycamore's `/` is a splash page that redirects by a JavaScript timer; Bain's PE portfolio sits on its own domain, not baincapital.com; Golden Gate redirects https to http to https; L Catterton's live page deletes 4 tiles that are in its raw HTML.

## What this means for the text rule

"Document storage, fetch log and last-confirmed" keeps a page's visible text and drops scripts, styles and hidden elements. Under that rule, six of the eight reachable listings yield no company names, and Roark's 30 former holdings vanish.

## Unrelated fact found the same day

A separate check of the SEC's monthly Form ADV page with the user agent `adv-field-check/0.1` got HTTP 403 ("Request Rate Threshold Exceeded") on its first request. The category audit's user agent, `EvidenceEngine ownership-research bot (category audit)`, also without contact detail, was accepted on 2026-11-07. The monthly adviser files have a `Website Address` column (category-audit-full.md, Form ADV method note).
