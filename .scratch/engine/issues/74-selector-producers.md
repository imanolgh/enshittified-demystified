# Selector producers: store locators and rosters

Type: grilling
Status: open
Blocked by: none
Map: [engine](../map.md)

## Question

How do `selector` producers work: the config schema and its revision number, the shape check, what one document is for a roster page, store-locator responses and their records, item-set diffs and the closing rule; and, needed for the chains-and-brands launch, the status-only selector that reads former holdings from markup or a server-side status filter on portfolio pages?

## Context

- Split from "Rosters, portfolio pages and the registry" on 2026-11-12 (Q0, developer ruling). That ticket keeps the registry, portfolio pages and newsrooms; selectors moved here because the general selector work isn't needed at launch.
- **Needed for launch: the status-only selector** (Q9 option e, kept after the scale check; Q16 revised). Every portfolio page is read by the LLM; a status-only selector runs alongside it only where status isn't in the text, writing name and status records (never deal wording). The page-type survey of 73 portfolio pages ([portfolio-page-types](../research/portfolio-page-types.md)) found 22 with status only in markup (Roark's CSS-hidden "previous" section, LLCP's `data-status`, L Catterton's `historical` class) and 5 with status only in a server-side filter (Golden Gate `?_sft_status=exited`, BC Partners, Permira, Princeton, Freeman Spogli; TSG has `?status=exited` too). For filter views, the registry lists the filtered URL as its own page and the selector marks every item on the exited view as former; the receipt links that filtered URL. Expect about 27 configs in 73 pages, about 50 at a full registry. A selector's `former` claims win the same-date tie over the LLM's default `current` reading ("Conflict, succession and co-investors"). A broken selector misses only companies exited during the break: an undated listing never restarts ownership a dated claim ended. The registry page field is `status_selector` (evidence_layer_plan.md §4 `registry_pages`).
- **Moved from "Rosters, portfolio pages and the registry"** (Q0): the selector config schema and its revision number (the selector's `producer_version`); the shape check (expected fields, roughly the usual item count, run before anything is written; failures alert); whether an HTML roster page is one document or one per item (the item's text must appear in the page's text either way); store-locator responses as parents with each store record a recurring child (endpoint plus store id); the item-set diff; how "closed after two complete crawls in a row miss it" works for stores and roster locations ("Edge lifecycle").
- **From "Claim producers and the claims door"** (2026-11-05): `selector` producers only read long uniform lists (store locators, location rosters) and now status markup; store-locator JSON endpoints are allowed when robots.txt permits them and they feed the public locator page; a JSON record is one code-rendered document.
- **From "Predicate semantics"** (2026-11-05): a roster or store-locator item yields `operated_by` (location → company) when the page states the operator, and `location_brands` rows from the brand names in its identity record.
- **From chains-and-brands "Brand and chain model"** (2026-11-06): store-locator selectors are for the store-map follow-up after launch; DSO and rollup location rosters are parked with local businesses. Only the status-only selector is on the launch path.
