# Website pages and shareable cards

Type: grilling
Status: open
Blocked by: 60, 58, engine/29, engine/40  (Website stack and hosting; Card wording and the how-this-works page; Events and the public changelog; Search and the demand log)
Map: [chains-and-brands](../map.md)

## Question

Which pages does version 1 have, what does each show, and what does a shareable deal card look like?

## Context

- Pivot proposal, **not decided**: brand or chain page, category page, a public feed of new PE deals built on `events`, name search, the how-this-works page; each new deal becomes a shareable card; creators get sourced data.
- Search (engine "Search and the demand log") and the changelog (engine "Events and the public changelog") supply the data.
- Accounts, follows and paid alerts are out of this map (later map), so v1 pages are public and anonymous.
- **From engine "Schema conventions"** (2026-11-05): a readable name in page URLs (`/b/x7k2.../dunkin`) is this ticket's; the stable key is `entities.public_id` (12 random Crockford base32 characters, never reused).
- **From "Brand and chain model"** (2026-11-06): launch has brand pages and no store pages; the store map is the first follow-up after launch (map "Not yet specified"). A rollup or other company appears only where it owns a brand; whether owners (companies, investment firms) get pages of their own is this ticket's.
