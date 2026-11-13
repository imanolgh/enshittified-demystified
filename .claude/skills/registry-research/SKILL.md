---
name: registry-research
description: Research and write registry entries: the investment firms, companies and brands whose own portfolio pages, newsrooms and about pages the engine reads. Use when asked to add a firm or brand to the registry, find an owner's portfolio page or newsroom, work through the registry gap report, or check a registry entry's pages and crawl fields.
---

# Registry research

The registry tells the crawler where to look. It is never evidence (GLOSSARY "Registry"), so nothing in an entry reaches extraction, sets an owner kind or appears on a card. The rules come from engine "Rosters, portfolio pages and the registry" (2026-11-12); the crawler is described in docs/evidence_layer_plan.md "Registry crawler".

## Who gets an entry

For the chains-and-brands launch:
- every company or investment firm on a listed brand's ownership chain that has a portfolio page, a newsroom or an about page naming its owner;
- each listed brand itself, for its own newsroom and about page.

Work from the operator gap report: owners on a listed brand's chain with no entry, and listed brands with no newsroom or about page. The launch target is a rule, not counts: every owner on a listed brand's chain that publishes a portfolio page or newsroom has an entry. DSO and rollup location rosters are parked with local businesses.

## One YAML file per organization

Write `registry/<slug>.yaml`, one organization per file (a firm can span categories: KKR is in car washes, dental and pharmacies). The developer approves an entry by committing it; never commit yourself.

```yaml
name: Roark Capital
identifiers:            # lookup only; never written as identifier rows
  crd: "160368"
domains:                # every domain the organization's own pages sit on
  - roarkcapital.com
pages:
  - url: https://www.roarkcapital.com/portfolio
    role: portfolio     # portfolio | newsroom | about
    render: http        # http | browser (only when names appear after JavaScript)
    paging_param: null  # e.g. sf_paged (Golden Gate)
    detail_links: null  # URL pattern for per-company pages or releases, e.g. /portfolio/*/
    required: true      # false only when the page is walled while you research it
    status_selector: roark-previous   # only when status lives in markup or a filter
research:               # code never reads this block
  kind: private equity firm
  parent: null
  evidence_urls:
    - https://www.roarkcapital.com/portfolio
  confidence: documented   # documented | reported | inferred
  notes: former holdings sit in a CSS-hidden "Previous Investments" section
```

## How to research an entry

1. **Find the organization's own domains.** Form ADV's `Website Address` holds only the first of several sites and is often LinkedIn or Facebook; confirm the real domain by the page title. Check for moved domains (Ares now serves from ares.com) and separate business-line domains (Bain's PE portfolio is on baincapitalprivateequity.com).
2. **Find each page.** The portfolio page (current and former holdings; a company's "our brands" page counts), the newsroom (the press-release index), and an about page that names the owner ("a portfolio company of Roark Capital").
3. **Read each page the way the engine will.** The text keeps hidden elements and writes image `alt`, link `title` and `aria-label` in place. Then set the crawl fields:
   - `render: browser` if the names appear only after JavaScript (L Catterton);
   - `paging_param` if the server pages the list (Golden Gate's `?sf_paged=N`);
   - `detail_links` if per-company pages state status or dates in text (LLCP, Golden Gate), and for a newsroom's release links;
   - `status_selector` if former holdings are marked only by a class, data attribute or section (Roark, LLCP's listing, L Catterton), or only by a server-side status filter: list the filter view (TSG's `?status=exited`) as its own page. The selector configs themselves belong to "Selector producers: store locators and rosters".
4. **Check access with the bot's rules.** Identified user agent, robots.txt first and obeyed, crawl delay honored. A page that returns a challenge gets one honest browser retry (no stealth, no clicks). If it is walled while you research it, write it with `required: false` and say so in `notes`. A hard block or a robots refusal means no pages from that site.
5. **Fill `research`** with the evidence for the organization's kind and parent, and an honest confidence. An inferred parent with no citation is a lead, not an entry.

## Rules

- Public primary sources only; never PitchBook, Preqin, CB Insights or any paywalled source; never WhoIsMyDentist, Private Equity Vet or Reddit.
- Never get around a block (CLAUDE.md scrape etiquette).
- Family-owned and public-company owners get entries too when they have the pages; the registry's `kind` never sets an owner kind.
- Batch entries as files for review; report what the gap report still lists and when a gap can't be filled ("no newsroom found").
