# Portfolio wall survey: how many PE firm sites refuse a plain identified request

Gathered 2026-11-11 for engine "Rosters, portfolio pages and the registry" (Q11), after the developer predicted that most or all PE firm sites have bot blockers. It follows the ten-firm [portfolio page survey](portfolio-page-survey.md) of 2026-11-08.

## Method

- **Firms.** Every firm in the category audits' Form ADV tables that owns, controls or holds a stake in an audited brand ([category-audit-full.md](../../chains-and-brands/research/category-audit-full.md) §2.A, [category-audit-pilot.md](../../chains-and-brands/research/category-audit-pilot.md) §5), plus former and rollup owners from §2.C. Left out: firms named only as deal leads or lenders, index and asset managers, Biglari (no website on file) and the FS KKR BDC adviser. 103 firm websites in all.
- **Domains.** The SEC monthly adviser files for November 2026 (`ia110226-registered.zip`, `ia11022026-exempt.zip`) give each adviser's `Website Address`, but only the first of several, and for about 40 firms that first entry is LinkedIn, Facebook, YouTube or Wikipedia. Those domains were filled in by hand, and every fetched page's title was checked against the firm. Five hand-filled domains turned out wrong (two don't resolve, two are parked pages, one is probably another company) and are not counted.
- **Requests.** One plain HTTP client (httpx 0.28.1, HTTP/1.1, no JavaScript), user agent `EvidenceEngineBot/0.1 (portfolio survey)` with no contact detail, no retries. Per site, in order: robots.txt, then the homepage if robots.txt allows it, then one linked page whose path or label says portfolio, investments, companies or partnerships, if robots.txt allows it. The pause between a site's requests was its `Crawl-delay` (capped at 15 s), else 3 s. A challenge, block or robots refusal at any step stopped that site.
- **Where from.** The developer's home connection (a residential IP), the same as the 2026-11-08 survey. The engine will run from a hosting company's IPs, which bot services score worse, so production may meet more walls than this.
- **Raw results** stayed in the session scratchpad.

## Results

| Outcome | Sites |
|---|---|
| Open: robots.txt and homepage served normally | 88 |
| Challenged | 3 |
| Hard blocked | 1 |
| robots.txt disallows the homepage | 1 |
| Unreachable: TLS certificate or connection errors, not a bot response | 5 |
| Domain not confirmed (not counted) | 5 |

**Of the 93 sites reached, 88 (95%) served a plain identified request.** On 69 of the 88, a second page (usually the portfolio page) was fetched too and also served. On the other 19, no portfolio link was found on the homepage; most are hedge funds and lenders without a portfolio page. Sycamore's portfolio page (`/investments`), which the 2026-11-08 survey read, was missed by the link check.

**Bot services in front of open sites.** 46 of the 88 open sites sit behind Cloudflare (by `cf-ray` or `server: cloudflare`), and others behind Sucuri (2), Akamai (1, Goldman Sachs Asset Management), Vercel (1), CloudFront (2), Fastly (4) or Netlify (7). Running a bot service did not mean refusing an identified bot: Cloudflare sites were open 46 times and walled 3 times.

**The walled sites:**

| Firm | What happened | Brands it touches in the audits |
|---|---|---|
| Warburg Pincus | Homepage: HTTP 403, `cf-mitigated: challenge`, "Just a moment..." (robots.txt served) | El Car Wash (control); Bond Vet (2021 investor); MB2 (rollup); Gabe's (former) |
| Ares Management | Homepage: HTTP 403, `cf-mitigated: challenge` (robots.txt served) | The Aspen Group: Aspen Dental, ClearChoice (co-owner) |
| Neuberger Berman | robots.txt: HTTP 429, "Vercel Security Checkpoint" | Martha Stewart (lead investor in Marquee Brands) |
| Partners Group | robots.txt: HTTP 403, Cloudflare "Sorry, you have been blocked" | EyeCare Partners (control) |
| Anchorage Capital | robots.txt served and disallows the homepage for `*` | Madewell via J.Crew Group (majority, 2020); Gabe's (lender group) |

**Blackstone changed.** On 2026-11-08 even its robots.txt answered with a Cloudflare challenge. Today robots.txt, the homepage and the private equity page (`/our-businesses/private-equity/`, about 383 KB) all served with HTTP 200. The two runs differed in user agent (`portfolio-structure-survey/0.1` then, `EvidenceEngineBot/0.1 (portfolio survey)` now) and date; which one mattered isn't known. Walls can change from day to day.

**Unreachable sites.** Arbour Lane, Bregal Partners and Oak Hill Capital failed certificate checks, Brazos's handshake failed, and Quad-C refused the connection. These are broken or stale domains, not bot responses.

## Honest-browser test, 2026-11-12

The Q11 retry rule, run once against the three challenged sites (Partners Group was left out: a hard block means stop). Playwright 1.65.1 with its bundled Chromium headless shell 158.0.8127.18, launched with defaults: user agent `EvidenceEngineBot/0.1 (challenge test)`, no stealth settings, no proxies, no solving services, no clicks or typing, up to 30 s for a challenge to clear. robots.txt was read first, by plain request, and in the browser only when the plain request was challenged. 10 s between page visits. Same home connection as the survey. Each plain request was repeated right after for comparison.

| Site | Plain request | Honest browser |
|---|---|---|
| Warburg Pincus | robots.txt 200; homepage 403 challenge (`cf-mitigated: challenge`), same as 2026-11-11 | Homepage 200 and `/investments/` 200 ("Select Investments", 168 KB), first response, no challenge shown |
| Ares Management | aresmgmt.com 403 challenge; **ares.com 200** | aresmgmt.com redirected (301) to ares.com, 200 |
| Neuberger Berman | robots.txt 429, "Vercel Security Checkpoint" | robots.txt 429, checkpoint did not clear in 30 s; stopped (robots.txt unreadable) |

- **Warburg Pincus** challenges a plain HTTP client but serves a real browser that names itself as a bot. The difference is the client, not the name.
- **Ares** moved to ares.com, which serves a plain request. The old domain challenges plain clients and redirects browsers. The registry entry should hold ares.com.
- **Neuberger Berman** stays blocked to the honest rule.

**Standing count after the test,** of the 93 sites reached: 90 readable (88 by plain request, Warburg through the honest browser, Ares on its new domain); Neuberger Berman blocked; Partners Group hard-blocked; Anchorage refused by robots.txt.

The test environment is kept outside `/tmp`: `~/.local/share/playwright-tools/` (Playwright venv, a `python` launcher, and the browser libraries libnss3, libnspr4 and libasound2t64 unpacked from Ubuntu's own packages, because `sudo` can't prompt from inside the session). The script is `challenge-test/run.py` there.
