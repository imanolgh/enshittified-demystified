# Website stack and hosting

Type: grilling
Status: resolved
Map: [chains-and-brands](../map.md)

## Question

What is the website built with, how is it served (server-rendered or static pages over the API), and where is it hosted relative to the engine?

## Context

- ADR 0004: version 1 is a website; a native app comes later.
- CLAUDE.md's stack is backend-only (FastAPI and friends); no frontend stack is recorded. marketgaps.md:214 mentions "FastAPI (Python) + Vue" in passing. Adding a stack is the developer's decision.
- Distribution is the biggest gap (handoff §5): brand pages that can rank in search and shareable deal cards argue for server-rendered or pre-rendered HTML.
- Engine hosting is open in engine "Hosting, storage and deployment".

## Comments

### Round 1 (2026-11-18)

- **How pages are built** (Q1, revised): Claude first recommended server-rendered Jinja templates (one language, no build step) and flagged that `docs/stack_fastapi.md` named Vue 3 from the local-businesses era. The developer, who has built many Astro sites, asked what Jinja offers over Astro for search engines, link previews, SEO, a PWA and app stores. Facts given: both send complete HTML, so search and link previews are equal (static pages from a CDN are slightly faster); Jinja keeps one language, no rebuild and instant freshness; Astro brings the developer's familiarity, a site that stays up when the engine is down, ready-made sitemap, image, share-image and PWA plugins, and a static build that can be bundled into a Capacitor app. Neither has a barcode scanner: in a browser, scanning is client-side JavaScript either way (the browser's own detector in Chrome on Android, a library such as ZXing on iPhone); in a store app it is a native plugin, and Astro's static files can be bundled inside the app, so the app works offline in stores with poor signal, which the developer called "a huge point for astro". **Ruled: Astro, static pages over the FastAPI JSON API, React islands only where needed; search and the "Report a mistake" form call FastAPI from the browser.**

### Round 2 (2026-11-18)

- **Folder** (Q2): `web/` at the repo root with its own `package.json`, beside `app/` (CLAUDE.md layout updated).
- **Hosting and builds** (Q3, revised twice: the developer turned down rebuilding "at most every 15 minutes" and then proposed three builds a day): Cloudflare Pages serves the site and handles the domain and TLS; the engine and its API run where engine "Hosting, storage and deployment" decides. Builds: after the overnight run, only if every job in it finished without crashing (single-source failures, already handled per brand, don't count; a skipped build alerts the developer); at 2 pm and 8 pm in the developer's time zone (set in configuration), only if something published since the last build; and on a "rebuild the site" operator command. The engine calls a Cloudflare Pages deploy hook; Cloudflare builds from the engine's public read API; a failed build leaves the last good version live. About 90 scheduled builds a month, under Cloudflare's free build cap as Claude remembered it (to confirm against current docs). Single new documents are still read as they arrive ("Extraction execution"), so a daytime change shows at the next scheduled build.
- **Share images** (Q4, after the developer asked what satori offers): PNGs made during the build from a simple card template with satori (directly or through an Astro plugin built on it): it runs inside the build with no browser to install, takes milliseconds per image, uses the same markup, CSS and fonts as the site, and publishes plain files the CDN caches. Limits: a CSS subset (flexbox, no grid), fonts supplied as files (no WOFF2), no JavaScript, emoji need handling.
- **Types** (Q5): `openapi-typescript` generates the site's TypeScript types from FastAPI's OpenAPI schema before each build, so a renamed or removed field fails the build.
- **PWA and apps** (Q6, revised twice: offline scanning, then both stores): v1 ships a web app manifest and icons (add to home screen). Later, a Capacitor app for the Apple App Store and Google Play built from the Astro output, with a native barcode scanner that works offline in stores, an on-device data file (verdicts plus a barcode-to-brand index) refreshed when online, the barcode data source open (USDA branded foods first, ADR 0004), and iOS build access (a Mac or a cloud Mac build) plus both store accounts (Apple $99 a year, Google Play $25 once, from memory).
- **Name and domain** (Q7): a new ticket, "Site name and domain".

## Answer

Resolved 2026-11-18 in a grilling session (two rounds, recorded under Comments).

- **Astro, static output,** in `web/`, React islands only where needed, over the engine's public read API; search and the report form call FastAPI from the browser.
- **Cloudflare Pages** hosting; builds after a clean overnight run, at 2 pm and 8 pm when something changed, and on command; a failed build keeps the last good site live.
- **Share images** at build time with satori; **types** from OpenAPI with `openapi-typescript`.
- **v1 PWA:** a manifest and icons. **Store apps later** (Capacitor, both stores, offline scanning with on-device data).
- Docs: CLAUDE.md (stack line, `web/` in the layout); `docs/stack_fastapi.md` (Vue 3 replaced by Astro). No ADR, no glossary change.

Handed on:
- "Site name and domain" (new): blocks "Website pages and shareable cards".
- "Website pages and shareable cards": Astro components, the share image's content, the manifest.
- engine "Hosting, storage and deployment": the public read API on the engine host; Cloudflare in front of the site; the deploy hook.
- engine "Celery topology": the build triggers (after a clean overnight run; 2 pm and 8 pm when something published; the gate and the alert).
- engine "API conventions, internal auth and operator surface": the "rebuild the site" command and the skipped-build alert; public read endpoints the build uses, with a stable OpenAPI schema; browser calls to search and the report form from the site's origin.
- engine "Graph endpoint and non-brand output shapes": the JSON shapes the build reads.
- chains map Out of scope ("Barcode scanning and a native app"): the store-app notes above.
