# Research: Press-release and news feed sources

Ticket: [10-research-press-feeds](../issues/10-research-press-feeds.md) · Researched 2026-10-26 · Primary sources only: the wire services' own feed pages, feeds, robots.txt files and terms pages, plus Google's Terms of Service, robots.txt documentation and the copyright notice inside the Google News RSS feed itself.

**Bottom line:** PR Newswire and GlobeNewswire publish public RSS feeds, including subject-level **M&A** feeds and (PR Newswire) a **Dentistry** feed. Each feed shows only the **last 20 releases**, and neither publishes a rate limit. Business Wire's RSS host disallows `/rss/` for generic crawlers in its robots.txt, and its general terms forbid storing or aggregating content. **Google News RSS is blocked three ways**: (a) Google's robots.txt disallows `/rss` for all crawlers, and names `ClaudeBot` and `anthropic-ai` specifically; (b) Google's Terms of Service forbid automated access that ignores robots.txt; (c) every feed carries a notice limiting it to "personal, non-commercial use". The terms of **every** wire whose terms I could read restrict robots, scraping and database storage. Those terms are a legal question the developer has to weigh. This document cannot settle it.

Fetch method note: pages were fetched on 2026-10-26 with WebFetch and plain `curl` (default user agent, no spoofing). Several hosts (`www.globenewswire.com`, `www.businesswire.com`, `www.accessnewswire.com`) answered **HTTP 403** to every request, including their robots.txt and terms pages. I did not try to get around those blocks. Facts about those hosts are marked as unconfirmed, or taken from a reachable sibling host, and the text says which.

Sources:
- [PRN-RSS] PR Newswire RSS index: https://www.prnewswire.com/rss/
- [PRN-ALL] PR Newswire all-releases feed: https://www.prnewswire.com/rss/news-releases-list.rss
- [PRN-MA] PR Newswire M&A feed: https://www.prnewswire.com/rss/financial-services-latest-news/acquisitions-mergers-and-takeovers-list.rss
- [PRN-DENT] PR Newswire Dentistry feed: https://www.prnewswire.com/rss/health-latest-news/dentistry-list.rss
- [PRN-HC] PR Newswire Health Care & Hospitals feed: https://www.prnewswire.com/rss/health-latest-news/health-care-hospitals-list.rss
- [PRN-LIST] PR Newswire M&A listing page (holds the full category nav): https://www.prnewswire.com/news-releases/financial-services-latest-news/acquisitions-mergers-and-takeovers-list/
- [PRN-ROBOTS] https://www.prnewswire.com/robots.txt
- [PRN-TOU] PR Newswire Terms of Use (dated Sept 1, 2023): https://www.prnewswire.com/terms-of-use/
- [GNW-ALL] GlobeNewswire feed: https://rss.globenewswire.com/rssfeed/
- [GNW-MA] GlobeNewswire M&A subject feed: https://rss.globenewswire.com/RssFeed/subjectcode/27-Mergers%20and%20Acquisitions/feedTitle/GlobeNewswire%20-%20Mergers%20and%20Acquisitions
- [GNW-ROBOTS] https://rss.globenewswire.com/robots.txt
- [GNW-LIST] GlobeNewswire RSS directory (403 to me; known only from search-result snippets): https://www.globenewswire.com/rss/list
- [GNW-TC] GlobeNewswire / Intrado (Notified) Terms and Conditions: https://portal.notified.com/terms-conditions/en
- [BW-FEED] Business Wire sample feed (Technology: Networks): https://feed.businesswire.com/rss/home/?rss=G1QFDERJXkJeGVtRWA==
- [BW-ROBOTS] https://feed.businesswire.com/robots.txt
- [BW-TOU] Business Wire Terms of Use (403 to me; contents known only from search-result snippets): https://www.businesswire.com/terms-of-use
- [AXW-ROBOTS] https://www.accessnewswire.com/robots.txt
- [EIN-ROBOTS] https://www.einpresswire.com/robots.txt · [PRWEB-ROBOTS] https://www.prweb.com/robots.txt · [NWCA-ROBOTS] https://www.newswire.ca/robots.txt
- [GN-FEED] Google News RSS search feed (one observation request, see §2): `https://news.google.com/rss/search?q=%22dental%22+acquired&hl=en-US&gl=US&ceid=US:en`
- [GN-ROBOTS] https://news.google.com/robots.txt · [G-ROBOTS] https://www.google.com/robots.txt
- [G-TOS] Google Terms of Service (effective July 30, 2026): https://policies.google.com/terms
- [G-RTXT] Google, *How Google interprets the robots.txt specification*: https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt
- [G-PUB] Google News Publisher Center, feed sections: https://support.google.com/news/publisher-center/answer/9545414
- [G-THREAD] Google News Help community thread (2018) on custom-search RSS: https://support.google.com/googlenews/thread/740233/

---

## 1. Wire services' public RSS/Atom feeds

### PR Newswire (Cision)

**URLs.** The RSS index [PRN-RSS] lists an all-releases feed, `/rss/news-releases-list.rss`, plus 16 top-level industry feeds with the pattern `/rss/<group>-latest-news/<group>-latest-news-list.rss`. The groups are Auto & Transportation, Business Technology, Consumer Products & Retail, Consumer Technology, Energy, Entertainment & Media, Environment, Financial Services & Investing, General Business, Health, Heavy Industry & Manufacturing, People & Culture (`multicultural`), Policy & Public Interest, Sports, Telecommunications and Travel.

**Subject feeds the index does not list.** Each listing page `/news-releases/<group>-latest-news/<sub>-list/` [PRN-LIST] has a matching feed at `/rss/<group>-latest-news/<sub>-list.rss`. I confirmed three of them (HTTP 200, valid RSS):
- `financial-services-latest-news/acquisitions-mergers-and-takeovers-list.rss` [PRN-MA]
- `health-latest-news/dentistry-list.rss` [PRN-DENT]
- `health-latest-news/health-care-hospitals-list.rss` [PRN-HC]

Other subcategory slugs that look relevant, read from the nav on [PRN-LIST]: `financial-services-latest-news/` {`private-placement`, `venture-capital`, `joint-ventures`, `restructuring-recapitalization`, `financing-agreements`}; `health-latest-news/` {`mental-health`, `fitness-wellness`}; `general-business-latest-news/small-business-services`; `consumer-products-retail-latest-news/` {`animals-pets`, `restaurants`}. Because the RSS index does not list these feeds, they are an undocumented URL pattern.

**Format and fields.** The feeds are RSS 2.0 with `prn:`, `dc:` and `media:` namespaces. Each item carries `title`, `link`, `guid` (same as link), `pubDate`, `description` (a **truncated HTML summary**, not full text), `prn:industry`, `prn:subject` (on some items), `dc:subject` (short codes, e.g. `TNM` appears alongside the "Acquisitions, Mergers and Takeovers" subject in the M&A feed), `dc:contributor` (**the issuing organization**), `dc:language`, and `dc:publisher` ("PR Newswire Association LLC."). [PRN-ALL][PRN-MA]

**Item cap and freshness.** **20 items** per feed, observed on all-releases and M&A [PRN-ALL][PRN-MA]. The response header was `cache-control: public, max-age=60` (Cloudflare, `cf-cache-status: HIT`). The M&A feed also contains releases that are not M&A (one was "Graybar Reports Record Third Quarter Performance"), so a subject feed narrows the stream but does not filter it perfectly [PRN-MA].

**Rate limits.** None published on [PRN-RSS] or [PRN-TOU].

**Terms.** [PRN-TOU] has **no RSS-specific terms**. Its general clauses bar using "any robot, spider, site search/retrieval application, or other manual or automatic device or process to access" the site, or to "index or 'data mine'" its content. They also forbid to "reproduce, distribute, 'frame,' 'mirror,' 'scrape,' republish or retransmit", and forbid "database storage and retrieval" of PR Newswire Materials. Personal use is limited to "a single copy … solely for your personal, noncommercial use". Using content for "training a machine learning or artificial intelligence (AI) system" is also barred.

**Robots.** [PRN-ROBOTS] blocks only `/search/`, `/multivu/` and a few template paths. **`/rss/` and `/news-releases/` are not disallowed.** It also advertises Google News sitemaps (`/sitemap-news.xml`, paged `?page=1..N`) for every regional edition.

### GlobeNewswire (Notified, formerly Intrado)

**URLs.** `www.globenewswire.com` returned 403 to every request, including [GNW-LIST] and its robots.txt. The **`rss.globenewswire.com`** host was reachable:
- `https://rss.globenewswire.com/rssfeed/`: description "Contains the last 20 releases" [GNW-ALL]
- Subject feed `…/RssFeed/subjectcode/27-Mergers%20and%20Acquisitions/feedTitle/GlobeNewswire%20-%20Mergers%20and%20Acquisitions`: channel title "GlobeNewswire - Mergers and Acquisitions", 20 items, all M&A-type [GNW-MA]

Search-result snippets for [GNW-LIST] describe feeds by **Subject, Industry and Location**, each in RSS and ATOM, with URL shapes like `/atomfeed/industry/<id>-<name>` and `/atomfeed/subjectcode/<id>-<name>`. **I could not open that page to confirm it.** The subject ID `27` was confirmed only because the feed returned M&A releases.

**Format and fields.** RSS 2.0. `description` is an **HTML lead paragraph** (the dateline plus the first paragraph). `dc:identifier` holds a numeric release ID, `dc:contributor` is **the issuing organization**, `dc:publisher` is "GlobeNewswire Inc.", and `category` elements carry **tickers and ISINs** (e.g. `Nasdaq:RDNT`, `US0231351076`), plus `dc:keyword`. [GNW-ALL][GNW-MA]

**Rate limits.** None found.

**Terms.** [GNW-TC] is "the" agreement that governs "access to and use of GlobeNewswire". It is written for the *Customer*, meaning the issuer account holder. Section 3(6) bars using "any agent, engine, software, or other mechanism (including without limitation 'spiders' or 'bots') … to navigate or search the Service or to gather or extract data from the Service". It does not mention RSS. **I found no separate terms for readers or RSS users.**

**Robots.** [GNW-ROBOTS] (for the `rss.` host) contains `Allow: /news-release/` and disallows `/newsroom/rss/`, `/search`, `/api/`, `/JsonData/`, widget paths and non-English language prefixes. It lists news sitemaps at `sitemaps.globenewswire.com/news-en.xml` and others. **The robots.txt for `www.globenewswire.com`, where release pages actually live, could not be read (403).**

### Business Wire (Berkshire Hathaway)

**URLs.** The feed host `feed.businesswire.com` was reachable. A sample feed, `/rss/home/?rss=<opaque token>` [BW-FEED], is RSS 2.0, held **37 items**, and carries `<copyright>Copyright 2026, Business Wire.</copyright>` and `managingEditor RSSfeeds@BusinessWire.com`. Its item `link`s point to `http://www.businesswire.com/news/home/<id>/<lang>/?feedref=…`, its `guid` is the release ID, and `description` is a lead excerpt. Feed tokens are opaque base64-like strings. The official feed directory (`businesswire.com/portal/site/home/news/rss/`) and the "Feed Options for Media Partners" help page (`businesswire.com/help/feed-options`) both returned **403**, so **I could not confirm the token for an M&A or health feed from a primary source.**

**Robots: a blocker for generic crawlers.** [BW-ROBOTS] grants `Allow: /rss/` only to named partners (`NewsNow`, `Tiingo News`). Under `User-agent: *` it lists **`Disallow: /rss/`**, plus `/rss.php`, `/rss2/`, `/atom10/` and the portal news paths.

**Terms.** [BW-TOU] returned 403 to me. Search-result snippets of that page (effective Jan 1, 2024) say site use is licensed for submitting releases, "retrieving RSS feeds", and reading. They also say the terms prohibit using the site to "store, aggregate, reproduce, or distribute" its information and bar commercial use without written consent. **This is unconfirmed: I could not read the page itself.**

### ACCESS Newswire (formerly Accesswire / Issuer Direct)

[AXW-ROBOTS] has **`Disallow: /rss`**, **`Disallow: /rss2`**, `Disallow: /api`, and `Crawl-delay: 5`. The newsroom, `/rss` and the terms page all returned **403**. I found no feed URL or terms text from a primary source.

### Other wires (robots only)

- **EIN Presswire** [EIN-ROBOTS]: `Crawl-delay: 30` for `*`. It does not disallow RSS (only `/rss_expired`) and advertises news sitemaps. EIN Presswire showed up as a source in Google News results [GN-FEED].
- **PRWeb** (Cision) [PRWEB-ROBOTS]: RSS is not disallowed; it has news sitemaps.
- **Newswire.ca** (Cision) [NWCA-ROBOTS]: only `/search/` is disallowed; it has news sitemaps.

---

## 2. Google News RSS

**Official documentation: none found.** Google's help pages document only the **publisher** side, where a publisher submits its own RSS feed as a section in Publisher Center [G-PUB]. In a 2018 Google News Help community thread, a volunteer expert said custom-search RSS was no longer offered [G-THREAD]. That thread is a community answer, not Google documentation. **So the query syntax, item caps and redirect behavior below are observations, not documented facts.**

**Observed (one request, 2026-10-26)** [GN-FEED]:
- URL shape: `https://news.google.com/rss/search?q=<query>&hl=en-US&gl=US&ceid=US:en`. Quoted phrases work inside `q`.
- **100 items** were returned, with dates back to about 2026-10-02.
- Each item has `title` ("headline - Publisher"), `link` = **`https://news.google.com/rss/articles/<opaque id>?oc=5`** (not the publisher URL), `guid` = the opaque id, `pubDate`, `description` (an HTML anchor plus the publisher name), and **`<source url="https://publisher-home-domain">Publisher</source>`**. The `<source>` element gives the publisher's **home domain only**, not the article URL.
- The response header was `cache-control: no-cache, no-store`.
- **The copyright element, verbatim:** "This XML feed is made available solely for the purpose of rendering Google News results within a personal feed reader for personal, non-commercial use. Any other use of the feed is expressly prohibited. By accessing this feed or using these results in any manner whatsoever, you agree to be bound by the foregoing restrictions."

**Robots** [GN-ROBOTS]: `User-agent: *` has `Disallow: /` and allows only `/`, `/home…`, `/topics/`, `/publications/`, `/stories/`, `/swg/` and `/about…`. **`/rss/…` is therefore disallowed**: under Google's own precedence rule the most specific matching rule wins, and no Allow rule matches `/rss` [G-RTXT]. A separate group sets **`Disallow: /`** for `CCBot`, `GPTBot`, `ChatGPT-User`, `PerplexityBot`, **`anthropic-ai`, `ClaudeBot`, `Claude-Web`**.

**Terms** [G-TOS]: Google's Terms of Service prohibit "using automated means to access content from any of our services in violation of the machine-readable instructions on our web pages (for example, robots.txt files that disallow crawling, training, or other activities)".

**Resolving redirect links to the publisher URL: not established.** No Google documentation describes the `/rss/articles/<id>` format or how it resolves. The path sits under the disallowed `/rss/` prefix, so I did **not** request it to observe the redirect. The only publisher information available without following the link is the `<source url>` home domain and the "- Publisher" suffix in the title.

**Google Alerts RSS** (a common substitute): [G-ROBOTS] has `Disallow: /alerts/`. Only `/alerts/$`, `/alerts/manage` and `/alerts/remove` are allowed, so alert feed paths under `/alerts/feeds/` are disallowed too.

Disclosure: one GET of [GN-FEED] was made while gathering facts, before I had read [GN-ROBOTS]. No further Google News feed or article URLs were requested.

---

## 3. Robots and terms for fetching full article text from wire sites

| Wire | Release page path | Robots for release pages | Terms on automated access and storage |
|---|---|---|---|
| PR Newswire | `/news-releases/<slug>-<id>.html` | **Allowed** (not disallowed) [PRN-ROBOTS] | Bans robots/spiders, scraping, "database storage and retrieval", and commercial use [PRN-TOU] |
| GlobeNewswire | `www.globenewswire.com/news-release/YYYY/MM/DD/<id>/0/<lang>/<slug>.html` [GNW-ALL] | `Allow: /news-release/` on the `rss.` host [GNW-ROBOTS]; **the `www` host could not be read (403)** | Bans "spiders or bots … to gather or extract data" (customer agreement) [GNW-TC] |
| Business Wire | `www.businesswire.com/news/home/<id>/<lang>/` [BW-FEED] | `www` robots could not be read (403); the feed host disallows `/rss/` for `*` [BW-ROBOTS] | Per snippets only: no storing, aggregating or reproducing; no commercial use [BW-TOU] |
| ACCESS Newswire | not determined | `/rss` disallowed; `Crawl-delay: 5` [AXW-ROBOTS] | Not read (403) |
| EIN Presswire | not determined | `Crawl-delay: 30` [EIN-ROBOTS] | Not read |

Practical observation: GlobeNewswire, Business Wire and ACCESS Newswire returned **HTTP 403 from bot protection** (Akamai's `errors.edgesuite.net` reference on GlobeNewswire) to plain non-browser clients on their `www` hosts, even for robots.txt. A fetch that identifies itself honestly, as CLAUDE.md requires, may be refused there whatever robots.txt says.

---

## 4. Classifying a domain as `press_release` vs `news` (ADR 0003)

Signals available from primary sources:

1. **Wire domain list.** These domains publish issuer-written releases: `prnewswire.com`, `prweb.com`, `newswire.ca` (Cision), `globenewswire.com`, `businesswire.com`, `accessnewswire.com` / `accesswire.com`, `einpresswire.com`. Each wire feed names itself as publisher: `dc:publisher` "PR Newswire Association LLC." [PRN-ALL], "GlobeNewswire Inc." [GNW-ALL], and "Copyright … Business Wire" [BW-FEED].
2. **The issuer is named in the feed.** `dc:contributor` holds the organization that issued the release on PR Newswire [PRN-ALL] and GlobeNewswire [GNW-MA]. That gives the issuer without parsing HTML.
3. **Dateline markers in the text.** `/PRNewswire/`, `(GLOBE NEWSWIRE)` and `(BUSINESS WIRE)` appear in the description lead of every item observed (17 of 20 PRN items; all GNW and BW items) [PRN-ALL][GNW-ALL][BW-FEED]. The marker stays in the text when a news site **syndicates** a release, so it can identify a wire copy republished on a news domain.
4. **Mirrors exist.** Google News results list `finance.yahoo.com` and `einpresswire.com` side by side as sources [GN-FEED]. Yahoo Finance is known to republish wire releases, but **that is not confirmed here from a Yahoo primary source**. A domain-only rule would label such copies `news`.
5. ADR 0003 already says an SEC 8-K EX-99 is stored as `press_release`, and that "the same release on a wire must count once". So a classification rule also feeds independence: the same release on two domains is still one source.

---

## Implications for the design (facts and consequences, no decisions)

- **Polling cadence vs. the 20-item cap.** PR Newswire and GlobeNewswire feeds hold only the newest 20 items, and PR Newswire's all-releases feed turns over within minutes (CDN `max-age=60`). If the poll interval is longer than the time a feed takes to turn over 20 items, releases are missed with no error. The narrower subject feeds (M&A, Dentistry, Health Care) turn over more slowly than the all-releases feeds.
- **News sitemaps as a backfill.** PR Newswire and GlobeNewswire both advertise Google News sitemaps in robots.txt. That is a documented channel, offered to crawlers, which lists more URLs than a 20-item feed. The terms clauses on robots still apply to it.
- **The terms conflict with the pipeline.** The pipeline stores document text so `verify_citations` can string-match quotes. That is "database storage and retrieval" in PR Newswire's words, and "store, aggregate" in Business Wire's (per snippets). None of the terms I read grant an RSS or archive exception. Whether these clauses apply is a legal question for the developer, not something this research can resolve.
- **Google News RSS cannot be used as-is.** robots.txt disallows the path and names Anthropic's crawlers, the Google ToS ties automated access to robots.txt, and the feed's own notice limits it to personal, non-commercial readers. Its item links are opaque Google URLs, and the publisher URL is not in the feed (only the home domain).
- **Business Wire RSS is disallowed for generic user agents** on its feed host, and the 403s mean even release pages may be out of reach without a partner arrangement. An M&A-only Business Wire feed token could not be found from a primary source.
- **Feed metadata gives the issuer and identifiers for free.** `dc:contributor` names the issuer, and GlobeNewswire `category` elements carry tickers and ISINs. Both could help entity resolution, which is the developer's call.
- **Domain lists alone mislabel syndicated copies.** Dateline markers in the text are a second, mechanical signal, and they matter for the "count once" rule in ADR 0003.
- **Scrape-etiquette numbers are given only in robots.txt** (`Crawl-delay: 5` ACCESS Newswire, `30` EIN Presswire). No wire publishes an RSS rate limit.

## Unconfirmed / open

- GlobeNewswire's full RSS directory (subject, industry and location IDs) and any reader or RSS terms: `www.globenewswire.com` returned 403.
- GlobeNewswire `www` robots.txt, which governs the release pages themselves.
- Business Wire's terms text (snippets only), its official feed directory, the tokens for M&A or health feeds, and its `www` robots.txt.
- ACCESS Newswire feed URLs and terms (403).
- Google News RSS query operators beyond quoted phrases (e.g. `when:`, `site:`), the true item cap (100 seen once), and how `/rss/articles/<id>` resolves. None of this is documented by Google, and checking it would mean requesting disallowed paths.
- Whether any wire offers a licensed or partner feed for commercial aggregation (Business Wire's "Feed Options for Media Partners" page exists but returned 403), and at what cost.
- Whether PR Newswire's undocumented subject-feed URL pattern is stable.
- Whether Yahoo Finance and similar sites republish wire releases verbatim (not checked against a Yahoo primary source).
