# Research: Press-release and news feed sources

Type: research
Status: resolved
Map: [api-spec](../map.md)

## Question

Which press-release and news feeds can the press connector poll, and how do they behave?

## Find out

- Wire services' public RSS/Atom feeds (PR Newswire, Business Wire, GlobeNewswire, Accesswire…): URLs, coverage, terms, rate limits.
- Google News RSS: query syntax, result caps, terms; its links are redirect URLs — how to resolve to the publisher URL.
- Robots/terms for fetching full article text from wire sites.
- A way to classify a domain as `press_release` (wire/issuer) vs `news` (ADR 0003 source types).


## How to resolve

AFK. A subagent invokes the `research` skill and writes findings, every claim cited to its primary source, to `.scratch/api-spec/research/press-feeds.md`. No branches, commits or pushes (map scope ruling 2026-10-26). Then append `## Answer` here: a short summary + link to the findings file.

## Answer

- **PR Newswire** offers public RSS 2.0 feeds: one for all releases, 16 for industries, and undocumented subject feeds that work, including **M&A**, **Dentistry** and **Health Care & Hospitals**. Each feed holds only the newest **20 items** (summaries, not full text), and the CDN caches it for 60 seconds. Its robots.txt allows `/rss/` and `/news-releases/`.
- **GlobeNewswire** serves feeds from `rss.globenewswire.com`, including an M&A subject feed (subject code 27). Each holds 20 items and carries the issuer (`dc:contributor`) plus tickers and ISINs. The `www` host returned 403 to every request, so its feed directory, reader terms and `www` robots.txt could not be read.
- **Business Wire**: the feed host's robots.txt has `Disallow: /rss/` for all crawlers except named partners (NewsNow, Tiingo). Its terms, seen only in search snippets, forbid storing or aggregating content. **ACCESS Newswire's** robots.txt disallows `/rss` and `/rss2`.
- **Google News RSS is blocked three ways:** robots.txt disallows `/rss` (and blocks ClaudeBot and anthropic-ai outright), Google's Terms of Service forbid automated access that ignores robots.txt, and each feed's notice limits it to "personal, non-commercial use". Google documents none of the query syntax, the item cap (100 seen once) or how links resolve. Item links are opaque `news.google.com/rss/articles/…` URLs, and the feed gives only the publisher's home domain. Google Alerts feeds are disallowed too.
- **Terms of every wire I could read** (PR Newswire, and GlobeNewswire's customer agreement) prohibit robots and spiders, scraping and "database storage and retrieval". Storing release text for citation verification conflicts with that wording, which is a legal call for the developer.
- **Classifying `press_release` vs `news`:** a list of wire domains, the feed's `dc:publisher` and `dc:contributor` (issuer), and dateline markers (`/PRNewswire/`, `(GLOBE NEWSWIRE)`, `(BUSINESS WIRE)`). The dateline survives syndication, so it can flag a wire copy republished on a news domain.

[findings](../research/press-feeds.md)
