# Bot protection workarounds: tools, costs and Cloudflare's verified bot program

Gathered 2026-11-11 after the portfolio page survey (portfolio-page-survey.md) found Blackstone and Warburg Pincus behind Cloudflare challenge pages. Reading only: no tool was installed or run and no target site fetched. Two supplied posts answered the fetcher with HTTP 403 and were not read: the python.plainenglish.io CAPTCHA post and the Medium post "Why stealth plugins are no longer the solution". Vendor pages are reported as claims.

## 1. How the blocks work

- **Detection engines.** Cloudflare runs heuristics that match requests against "a growing database of malicious fingerprints"; optional JavaScript detections that identify headless browsers; and a machine learning model fed "request features, including headers, session characteristics, and browser signals", which "accounts for the majority of all bot detections" ([cf-engines]). The output is a bot score from 1 (automated) to 99 (human) ([cf-score]).
- **TLS and HTTP fingerprints.** JA3 and JA4 "identify TLS clients based on how they initiate connections"; only Enterprise Bot Management customers can write rules on them ([cf-ja]). A September 2025 post adds HTTP/2 fingerprints, request sequences, data from challenge solves and "known residential and commercial proxy IP addresses", for Super Bot Fight Mode too ([cf-percustomer]). Model v8 (Q2 2024) added "better detection of residential proxies"; v9 (Q2 2025) targets "randomization attack techniques" ([cf-ml]).
- **Challenge types.** A Managed Challenge lets Cloudflare choose the check; a Non-Interactive (JavaScript) Challenge decides from injected JavaScript, usually in under five seconds; an Interactive Challenge asks for a click ([cf-pages]). Every challenge page carries `cf-mitigated: challenge` ([cf-detect]), as the survey saw; a Block action is a separate "hard block with no bypass option" ([bstack]).
- **Turnstile** runs proof-of-work, proof-of-space, web API probing and checks for "browser-quirks and human behavior" ([cf-turnstile]).
- **Clearance.** A passed challenge sets `cf_clearance`, 30 minutes by default ([cf-passage]). The cookie "is securely tied to the specific visitor and device it was issued to, preventing reuse across machines", and in Armed mode a component called Precursor "continuously re-evaluates clearance throughout a visitor's session" ([cf-clearance]).
- **Plans.** Bot Fight Mode (Free) issues CPU-heavy challenges and "cannot" be skipped with WAF rules ([cf-bfm]). Super Bot Fight Mode (Pro and up) sets an action per group; "definitely automated" accepts allow, block or managed challenge ([cf-sbfm], [cf-api]).

## 2. Tools and services

| Tool | Kind | Claims against Cloudflare or CAPTCHAs | How | License or price | Latest activity | Python and Playwright | Residential IPs or solver needed for Cloudflare |
|---|---|---|---|---|---|---|---|
| puppeteer-extra-plugin-stealth | JavaScript evasion plugin | No Cloudflare claim; "probably impossible to prevent all ways to detect headless chromium" ([pes]) | Patches `navigator.webdriver`, `chrome.runtime`, WebGL vendor and more | MIT, free | Last stealth commit 2023-03-01; repo push 2024-07-18 ([pes-commits], [pe-repo]); npm 2.11.2 has no deprecation flag ([pes-npm]) | Node only | Decodo: stealth alone "usually only works on the lowest security settings" ([decodo-blog]) |
| playwright-stealth | Python port of the above | "Don't expect this to bypass anything but the simplest of bot detection methods" ([pws]) | JavaScript init scripts | MIT, free | 2.0.3, 2026-04-04 ([pws-pypi]) | Native; Chromium only ([decodo-blog]) | Same as above |
| CloakBrowser | Patched Chromium binary plus wrapper | Self-reported: Turnstile pass, reCAPTCHA v3 score 0.9; "doesn't solve CAPTCHAs" ([cloak], [cloak-site]) | 87 C++ source patches | Wrapper MIT; binary proprietary. Free key: 1 session. Solo $19 (5 sessions) to Scale $499; operator not named ([cloak-site]) | Weekly Pro builds, latest 2026-11-03 (Chromium 156) ([cloak-rel]); 32.8k stars ([cloak-api]) | `launch()` returns a Playwright browser | No proxy included; README recommends residential for anti-bot sites ([cloak]) |
| invisible_playwright | Patched Firefox with Playwright API | Says it passes reCAPTCHA, hCaptcha, Turnstile scoring; "5/5 detection suites" banner, no published results ([invis]) | C++ Firefox patches, seeded fingerprints, Bezier mouse paths | MIT package, MPL-2.0 binary; "for educational purposes only" | Created 2026-05-13, pushed 2026-11-11 ([invis-api]) | Python 3.11+; Linux and Windows x86_64; ~550 MB engine | Proxy optional |
| Camoufox, Patchright, nodriver | Anti-detect Firefox; patched Playwright; CDP-free Chrome driver | Named as alternatives ([invis]) and tested ([paterson]) | Engine or protocol patches | MPL-2.0; Apache-2.0; AGPL-3.0 | Pushed 2026-11-11, 2026-11-10, 2026-10-26 ([camoufox], [patchright], [nodriver]) | nodriver is not a Playwright drop-in ([paterson]) | Tested only on a residential IP ([paterson]) |
| Skyvern | AI browser agent | "Solves CAPTCHAs natively", "No third-party solving services are needed" ([skyvern]) | LLM-driven Playwright; anti-bot measures only "in our managed cloud offering" ([skyvern-gh]) | AGPL-3.0; cloud Hobby $29 (basic solver, datacenter proxy), Pro $149 (advanced solver, residential) ([skyvern-price]) | Pushed 2026-11-11 ([skyvern-api]) | Python SDK on Playwright | Cloud tiers bundle both |
| Browserless | Hosted browser | `/stealth` hides automation signals; solver covers Turnstile; "handle any Cloudflare challenges automatically" ([bl-docs]) | Fingerprint spoofing, solver, optional residential proxy | Repo "Free for non-commercial uses" ([bl-api]); cloud $25 to $350 a month, 1 unit = 30 s, residential 6 units/MB, 10 units per solve ([bl-price]) | Pushed 2026-11-11 | CDP endpoint | Residential is an add-on |
| Bright Data Browser API | Hosted browser plus proxy network | "Built-in CAPTCHA solving" with a "CF Challenge" toggle; cites a third-party benchmark at 95%, no method shown ([bd]) | Residential pool ("400M+ monthly proxy IPs"), fingerprint emulation | $8/GB; Scale $499 for 71 GB; free 1 GB ([bd-price]) | Service | `connect_over_cdp` | Included |
| Decodo | Proxy network; Site Unblocker | Unblocker: "100% success rate" in one place, "99.99%" in another ([decodo-unb]) | Residential IPs; Unblocker as proxy endpoint with rendering | Residential $2.00 to $4/GB ([decodo-price]); Unblocker $5.50 to $10/GB ([decodo-unb]) | Service | Proxy endpoint | Is the proxy |
| ScrapingAnt | Scraping API | Avoids risk-based CAPTCHAs; "does not solve mandatory, always-on CAPTCHAs" ([sant-blog]) | Headless Chrome plus rotating proxies | Free 10k credits; $19 for 100k to $599 for 8M; default request 10 credits, range 1 to 25 ([sant]) | Service | HTTP API returning HTML, no Playwright control | Included |
| humanbrowser.cloud (Virix Ltd) | Hosted browser plus AI agent | Own May 2026 test: "~95–97% on standard Cloudflare, ~75–78% on Enterprise" ([hb-blog]) | Residential IP, iPhone profile, human-paced input | $0.10/h, $0.02/agent step, $8/GB residential, $0.005/CAPTCHA; Starter $20/month ([hb-price]) | Service | Not checked | Says residential is required ([hb-blog]) |
| HandsOn | Claude Code desktop-control plugin | None; no anti-bot content ([handson]) | Accessibility tree, OCR, screenshots; defers to Playwright inside browsers | MIT | Two releases on 2026-03-03, last activity 2026-03-07, 0 stars ([handson-api], [handson-rel]) | Windows and macOS only | Not applicable |
| 2Captcha | Solving service | Turnstile $1.45 per 1,000 ([2c-price]) | AI first, humans for low-confidence tasks ([2c]) | Per solve | Service | API | Is the solver |
| Anti-Captcha | Solving service | Turnstile $2 per 1,000 ([ac]) | "100% of captchas are solved by human workers" ([ac]) | Per solve | Service | API | Is the solver |
| CapSolver | Solving service | Turnstile and Cloudflare Challenge $1.20 per 1,000 ([cs]) | "AI-based" ([cs]); challenge task requires a static or sticky proxy and Chrome on Windows or Mac ([cs-docs]) | Per solve | Service | API | Needs your proxy |

## 3. What seems to work in 2026

**Stealth plugins alone.** No source read claims they pass Cloudflare; their own READMEs disclaim it ([pes], [pws]). Decodo, a proxy seller, says stealth "only fixes browser-level signals", not IP reputation, TLS or behavior ([decodo-blog]). humanbrowser's test put playwright-extra with stealth on a VPS at about 5% on Cloudflare Pro and 0% on Enterprise, and about 70% and 25% on a residential IP ([hb-blog]); that is a vendor test of 8 sites with about 500 requests per variant, with raw JSON linked but no outside check.

**Residential IPs.** BrowserStack says "Datacenter IPs are flagged by Cloudflare" ([bstack]); humanbrowser says data-center IPs get a high bot score before any JavaScript runs ([hb-blog]); CloakBrowser recommends residential proxies ([cloak]). Cloudflare's own docs and blog list known residential proxy IPs as a detection signal, so residential pools are themselves a target ([cf-percustomer], [cf-ml]). No source read tests a patched browser from a datacenter IP.

**The one non-vendor test.** Ian Paterson's May 2026 benchmark ran seven browsers against 31 targets from one residential home IP in one night ([paterson]). On the four Cloudflare sites in its table, vanilla Playwright passed two (crunchbase, nowsecure) and was blocked on two; CloakBrowser, Camoufox and Patchright passed the same two and were blocked or gated on the others; only nodriver passed all four. A Linux VPS behind a residential proxy was blocked "harder than the unproxied Mac Studio". His reading: "The matrix driver is automation-protocol fingerprinting, not cipher lists." He calls it "a snapshot, not a permanent fact".

**Solving services.** ScrapingAnt paid 2Captcha and Anti-Captcha for 1,200 solves: reCAPTCHA was accepted 99 or 100 times in 100, but Turnstile was "100/100 tokens, unverified", meaning no site confirmed the tokens ([sant-blog]). Cloudflare challenge solving needs a sticky proxy, and the resulting cookie is device-bound ([cs-docs], [cf-clearance]).

## 4. Costs

My assumptions, not vendor figures: 150 sites × 4 pages × 30 days = 18,000 page loads a month; walled only, 5 to 20 sites = 600 to 2,400. The 2025 median home page weighs 2.6 MB (mobile) to 2.9 MB (desktop), with images about 0.9 MB of the mobile figure ([almanac]). At 2.5 MB a page: about 45 GB a month for the full crawl, 1.5 to 6 GB for walled sites. Blocking images cuts roughly a third.

| Option | Full crawl (18,000 pages) | Walled only (600 to 2,400 pages) |
|---|---|---|
| Open-source stealth or patched browser + Decodo residential | 50 GB plan $150 | 3 GB $11.25 to 10 GB $35 |
| CloakBrowser + Decodo residential | $150 + $19 Solo | $11 to $35 with the free key; $19 more for Solo |
| Bright Data Browser API | $360 at $8/GB, or $499 Scale | $12 to $48 (a free tier gives 1 GB a month) |
| Browserless (about 16 units a page: time plus residential) | about $324 (Starter + overage) or $350 Scale | $25 to $62; $25 to $110 if every page needs a solve |
| humanbrowser.cloud | about $370; up to $460 if every page needs a solve | about $12 to $61 |
| Decodo Site Unblocker | 50 GB $375 | 5 GB $45 to 10 GB $85 |
| ScrapingAnt (10 to 25 credits a page) | $49 | free to $19 |
| Skyvern cloud | Not estimable: credits per action not stated ([skyvern-price]) | Same |
| Solving service only (worst case, every page) | $22 to $36 | $1 to $5, plus proxy and browser |

Prices come from the pages cited in section 2 ([decodo-price], [cloak-site], [bd-price], [bl-price], [hb-price], [decodo-unb], [sant], [2c-price], [cs]). Browserless prices are annual billing. ScrapingAnt makes no Cloudflare-challenge claim ([sant-blog]).

## 5. Third parties involved

**Proxy IP sourcing, as vendors state it.** Bright Data: "Every residential IP opts in. Verified customers only. Independently audited"; app owners embed an SDK and get "monthly remuneration based on the number of users who opt-in", and users get an ad-free app ([bd-res]). Decodo partners with "verified providers who run peer-to-peer networks" whose users "explicitly opt in and are fairly compensated"; it describes no audit and blocks banking and government sites ([decodo-sec]). humanbrowser, Browserless, Skyvern and ScrapingAnt do not say where their IPs come from ([hb-price], [bl-docs], [skyvern-price], [sant-blog]).

**Documented abuse.**
- 911 S5: over 19 million IPs, enrolled through backdoored free VPN apps bundled with pirated games ([fbi-911]).
- BADBOX 2.0: "millions of infected devices" feeding residential proxy services ([fbi-badbox]).
- IPIDEA (January 2026): Google found app SDKs paid "usually on a per-download basis", over 600 Android apps and 13 brands; "many of the malicious applications ... did not disclose that they enrolled devices", and operators "share pools of devices using reseller agreements" ([g-ipidea]).
- NetNut (July 2026): at least 2 million devices; "Google has high confidence that many popular residential proxy brands are in fact whitelabeling the NetNut botnet" ([g-netnut]).
- The FBI's March 2026 PSA names SDK deals, free VPNs, infected IoT devices, malware and bandwidth-sharing apps as enrollment routes, and advises businesses to block residential proxy IPs ([fbi-2026]).

No source read says whether any vendor in the table resells these pools.

**Who solves CAPTCHAs.** Anti-Captcha: human workers, "An average worker earns about $100 per month" ([ac]). 2Captcha: AI first, then "verified human workers" ([2c]). CapSolver: "AI-based", silent on humans ([cs]). Browserless, Bright Data, Skyvern and humanbrowser do not say ([bl-docs], [bd], [skyvern], [hb-price]).

## 6. Cloudflare's verified bot program

**Status.** Signed agents were merged into Verified; a Direct or Intermediary label now records who operates the bot ([cf-signed]).

**Requirements** ([cf-vb], [cf-policy]):
- Honest self-identification: a Web Bot Auth signature, a published IP list with a stable user agent, or reverse DNS. Submission requires Web Bot Auth or IP validation.
- Non-abusive behavior: "obeys robots.txt and crawl directives", "maintains reasonable request rates", and is never seen evading site owner preferences.
- The disclosed purpose must match the traffic.
- No traffic minimum is stated.

**How to apply.** Submit the BotBase form in a Cloudflare dashboard. Rejections give no reason; you ask Support.

**Web Bot Auth setup** ([cf-wba]):
- An Ed25519 key, published as a JWKS at `/.well-known/http-message-signatures-directory` with signed responses.
- `Signature-Input`, `Signature` and `Signature-Agent` headers on every request.

**Accountability and removal.** Since October 2026 Cloudflare scores verified bots continuously on honoring robots.txt and HTTP 429 ([cf-acct]). Breaches remove a bot from the allowlist, and Cloudflare "may revoke Verified status for all bots and agents owned or operated by an organization" ([cf-policy]).

**Would it pass a site set to challenge bots?** It depends on the control the site uses:
- Verified bots "have been excluded in default bot configurations across all plans" ([cf-vb]).
- In Super Bot Fight Mode, verified bots accept only allow or block; there is no challenge option ([cf-api]).
- WAF custom rules run before bot settings. A custom challenge rule catches verified bots unless its expression excludes them; Cloudflare's examples add `not cf.bot_management.verified_bot` or a skip rule ([cf-waf-bots], [cf-sbfm]).
- The Bot Fight Mode and Under Attack docs do not mention verified bots ([cf-bfm], [cf-uam]).
- Customers can set AI Crawler and Agent access policies to block ([cf-vb]).
- Owners need not opt in; they can ask Support to disable verification on their zone ([cf-wba]). humanbrowser's claim that Web Bot Auth needs sites to opt in ([hb-blog]) does not match Cloudflare's docs.

From outside, nothing shows which control Blackstone or Warburg Pincus use.

## 7. Facts that would matter for a decision

**Maintenance burden.**
- CloakBrowser shipped five Pro builds between 2026-10-06 and 2026-11-03, following Chromium ([cloak-rel]).
- Paterson saw a target switch anti-bot vendors mid-study, and the macOS CloakBrowser build lagging at Chromium 145 ([paterson]).
- humanbrowser: "variance by target is real" ([hb-blog]).
- The stealth plugin calls detection "a cat and mouse game" ([pes]).

**Detection and escalation.**
- Cloudflare caught Perplexity's undeclared crawler despite rotated IPs, other ASNs and a generic Chrome user agent: "We were able to fingerprint this crawler using a combination of machine learning and network signals." Cloudflare de-listed Perplexity and added signatures to a managed rule "available to all customers, including free plans" ([cf-perplexity]).
- AI Labyrinth, opt-in on every plan, leads bots that ignore no-crawl rules into AI-generated pages that are "not actually the content of the site", and feeds those visits into its bad-actor list and models ([cf-labyrinth]).

**Supply risk.** Google's takedowns cut proxy pools "by millions", and operators then buy capacity from competitors ([g-ipidea], [g-netnut]).

**Licenses.** AGPL-3.0 (Skyvern, nodriver), a proprietary binary (CloakBrowser), "for educational purposes only" (invisible_playwright) and non-commercial free use (Browserless self-hosted); see the table.

**Verified status and evasion together.** The policy bars a bot "observed evading site owner preferences" and allows revocation across an organization's bots ([cf-policy]).

## 8. Two sources the developer pasted

Added 2026-11-11. The developer pasted both texts; neither was fetched (Reddit stays unfetched under the project rule).

**Reddit thread, r/ClaudeCode, "Has anyone successfully deployed AI browser agents in production?"** (about eight months old). It is where HandsOn came from.
- HandsOn's author (3spky5u-oss) says desktop automation (screenshots, cursor input, accessibility settings) combined with Playwright "can defeat this", that a Playwright-spawned browser "loudly broadcasts 'IM A BOT'", and that the plugin was removed from GitHub after two account bans with no reason given, so it moved to GitLab. No test results are offered.
- Other replies say CAPTCHAs and bot defenses are "basically the hard stop unless you can switch to official APIs or you own the surface", that successful enterprise cases reverse-engineer a platform's network calls instead of driving a browser, and that "the scraping-random-websites use case is genuinely fragile".
- One reply reports CloakBrowser with residential proxies on VPS Docker hosts, with "human mimicking behaviors".
- At least three replies are product pitches (CapMonster Cloud, Linefox, Twin.so).

**Medium, Antonello Zanini, "Playwright at Scale in 2026: Why 'Stealth Plugins' Are No Longer the Solution"** (2026-08-18).
- It confirms the stealth plugin's last commit was more than three years ago, and says open-source evasions give anti-bot vendors "a blueprint".
- It lists six signal groups that detectors cross-check: user agent, client hints, WebGL, navigation trails (a too-clean session), CDP side effects, and behavior; and says consistency across all of them matters most.
- It is a Bright Data piece: it recommends Bright Data's Browser API, repeats the "~95% success" figure, and shows its own benchmark only as an image, with no method or raw data. It adds one price: about $8/GB pay as you go, falling to $5/GB on a $1,999 monthly plan.

[cf-engines]: https://developers.cloudflare.com/bots/concepts/bot-detection-engines/
[cf-score]: https://developers.cloudflare.com/bots/concepts/bot-score/
[cf-ja]: https://developers.cloudflare.com/bots/additional-configurations/ja3-ja4-fingerprint/
[cf-percustomer]: https://blog.cloudflare.com/per-customer-bot-defenses/
[cf-ml]: https://developers.cloudflare.com/bots/reference/machine-learning-models/
[cf-pages]: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/
[cf-detect]: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response/
[cf-turnstile]: https://developers.cloudflare.com/turnstile/
[cf-passage]: https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/
[cf-clearance]: https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/
[cf-bfm]: https://developers.cloudflare.com/bots/get-started/bot-fight-mode/
[cf-sbfm]: https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/
[cf-api]: https://developers.cloudflare.com/api/resources/bot_management/methods/update/
[cf-waf-bots]: https://developers.cloudflare.com/waf/custom-rules/use-cases/challenge-bad-bots/
[cf-uam]: https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/
[cf-vb]: https://developers.cloudflare.com/bots/concepts/bot/verified-bots/
[cf-policy]: https://developers.cloudflare.com/bots/concepts/bot/verified-bots/policy/
[cf-signed]: https://developers.cloudflare.com/bots/concepts/bot/signed-agents/
[cf-wba]: https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/
[cf-acct]: https://blog.cloudflare.com/verified-bots-accountability/
[cf-perplexity]: https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives
[cf-labyrinth]: https://blog.cloudflare.com/ai-labyrinth/
[bstack]: https://www.browserstack.com/guide/playwright-cloudflare
[pes]: https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth
[pes-commits]: https://api.github.com/repos/berstend/puppeteer-extra/commits?path=packages/puppeteer-extra-plugin-stealth
[pe-repo]: https://api.github.com/repos/berstend/puppeteer-extra
[pes-npm]: https://registry.npmjs.org/puppeteer-extra-plugin-stealth/latest
[pws]: https://github.com/Mattwmaster58/playwright_stealth
[pws-pypi]: https://pypi.org/pypi/playwright-stealth/json
[decodo-blog]: https://decodo.com/blog/playwright-stealth
[cloak]: https://github.com/CloakHQ/CloakBrowser
[cloak-site]: https://cloakbrowser.dev/
[cloak-rel]: https://api.github.com/repos/CloakHQ/CloakBrowser/releases
[cloak-api]: https://api.github.com/repos/CloakHQ/CloakBrowser
[invis]: https://github.com/feder-cr/invisible_playwright
[invis-api]: https://api.github.com/repos/feder-cr/invisible_playwright
[camoufox]: https://api.github.com/repos/daijro/camoufox
[patchright]: https://api.github.com/repos/Kaliiiiiiiiii-Vinyzu/patchright-python
[nodriver]: https://api.github.com/repos/ultrafunkamsterdam/nodriver
[paterson]: https://dev.to/ianlpaterson/anti-detect-browser-benchmark-2026-7-stealth-tools-31-cloudflare-targets-651-verdicts-4361
[skyvern]: https://www.skyvern.com/
[skyvern-gh]: https://github.com/Skyvern-AI/skyvern
[skyvern-api]: https://api.github.com/repos/Skyvern-AI/skyvern
[skyvern-price]: https://www.skyvern.com/pricing
[bl-docs]: https://docs.browserless.io/ai-integrations/claude-code-playwright-mcp
[bl-api]: https://api.github.com/repos/browserless/browserless
[bl-price]: https://www.browserless.io/pricing
[bd]: https://brightdata.com/products/scraping-browser
[bd-price]: https://brightdata.com/pricing/scraping-browser
[bd-res]: https://brightdata.com/proxy-types/residential-proxies
[decodo-price]: https://decodo.com/proxies/residential-proxies/pricing
[decodo-unb]: https://decodo.com/proxies/site-unblocker
[decodo-sec]: https://decodo.com/security-compliance
[sant]: https://scrapingant.com/
[sant-blog]: https://scrapingant.com/blog/bypass-captcha-playwright
[hb-blog]: https://humanbrowser.cloud/blog/bypass-cloudflare-playwright-2026
[hb-price]: https://humanbrowser.cloud/pricing
[handson]: https://gitlab.com/3spky5u/HandsOn/-/raw/main/README.md
[handson-api]: https://gitlab.com/api/v4/projects/79947522
[handson-rel]: https://gitlab.com/api/v4/projects/79947522/releases
[2c]: https://2captcha.com/
[2c-price]: https://2captcha.com/pricing
[ac]: https://anti-captcha.com/
[cs]: https://www.capsolver.com/
[cs-docs]: https://docs.capsolver.com/en/guide/captcha/cloudflare_challenge/
[almanac]: https://almanac.httparchive.org/en/2025/page-weight
[fbi-911]: https://www.ic3.gov/PSA/2024/PSA240529
[fbi-badbox]: https://www.ic3.gov/PSA/2025/PSA250605
[fbi-2026]: https://www.ic3.gov/PSA/2026/PSA260312
[g-ipidea]: https://cloud.google.com/blog/topics/threat-intelligence/disrupting-largest-residential-proxy-network
[g-netnut]: https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks
