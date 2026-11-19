# Website pages and shareable cards

Type: grilling
Status: open
Blocked by: 60, 58, 108, engine/29, engine/40, engine/69  (Website stack and hosting; Card wording; The how-this-works page; Events and the public changelog; Search and the demand log; Graph endpoint and non-brand output shapes)
Map: [chains-and-brands](../map.md)

## Question

Which pages does version 1 have, what does each show, and what does a shareable deal card look like?

## Context

- Pivot proposal, **not decided**: brand or chain page, category page, a public feed of new PE deals built on `events`, name search, the how-this-works page; each new deal becomes a shareable card; creators get sourced data.
- Search (engine "Search and the demand log") and the changelog (engine "Events and the public changelog") supply the data.
- Accounts, follows and paid alerts are out of this map (later map), so v1 pages are public and anonymous.
- **From engine "Schema conventions"** (2026-11-05): a readable name in page URLs (`/b/x7k2.../dunkin`) is this ticket's; the stable key is `entities.public_id` (12 random Crockford base32 characters, never reused).
- **From "Brand and chain model"** (2026-11-06): launch has brand pages and no store pages; the store map is the first follow-up after launch (map "Not yet specified"). A rollup or other company appears only where it owns a brand; whether owners (companies, investment firms) get pages of their own is this ticket's.
- **From engine "Category storage and recompute"** (2026-11-07): category pages and their shares read the stored `entity_categories` rows; formerly-PE history comes from ended `entity_pe_owner_periods` rows.
- **From engine "Brand card, receipt and edge shapes"** (2026-11-07; formerly "Claim card and graph output shapes"): a brand page shows the brand card, each fact opening its receipt; archived copies are never served publicly.
- **From "Category brand lists and checked"** (2026-11-17): each industry page shows a one-line method ("The 30 largest US grocery banners by 2025 sales (NRF Top 100), each banner a brand"), the current top 30 first, then "also checked" (lists only grow), and a count of brands and how many are checked; each brand row shows its own checked date. An industry goes live only when every brand on its list is checked. Some seeded brands belong to no industry (PE-owned brands found outside launch industries) and have only brand pages.
- **From "Alternatives and affiliate links"** (2026-11-17): PE-owned and PE minority stake brand pages carry an alternatives block, grouped by industry, in each list's order, collapsed after 10, each alternative with its own verdict line and "Shop at {brand}" / "On Amazon" links where they exist (`rel="sponsored"`); industry pages get a "Show only brands with no PE found" filter. No paid placement.
- **From "Card wording"** (2026-11-18): the brand card's section order and every fixed line are in its Answer (verdict with owner name and explanation line; pending deal under the verdict; PE owners with chain count; private equity shareholders; other owners; products under this name; disputes with each reading's result; history; franchise note; alternatives; what we checked; receipts). The prototype's look (https://claude.ai/artifact/Gqhsabk2oDKkKhfk4Wtasu) is not a design decision; layout, type and styling are this ticket's.
- **From "What would change this"** (2026-11-18): a "What would change this" section of one to three generated lines sits after the verdict and the pending deal on every brand card.
- **From "The how-this-works page"** (2026-11-18): one public page of eleven question-headed sections with a contents list; each section has a stable link name (`#verified`, `#private-equity-test`) and every label or term on a card links to its section. v1 stays without accounts or sign-in (the developer reaffirmed it: "not having any sort of sign up or login is much better").

