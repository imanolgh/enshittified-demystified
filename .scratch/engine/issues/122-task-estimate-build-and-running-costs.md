# Task: Estimate build, seeding and monthly running costs

Type: task
Status: resolved
Blocked by: none
Map: [engine](../map.md)

## Question

What will the product cost to build, to seed once before launch, and to run each month after launch? Give a low and high figure for each, with every number traced to a measured figure from a resolved ticket or a dated vendor price.

## Context

- Opened 2026-11-20 at the developer's request ("how much this thing is going to cost to build"). No ticket had added the costs up. AFK: Claude does the work and writes the findings; the developer reads them. Tickets 42 and 43 wait on it, because both need the numbers.
- **Output:** `.scratch/engine/research/cost-estimate.md`, with three tables (build, one seeding pass, a typical month at launch), each row giving its figure, its derivation and its source, plus a list of assumptions still open.
- **Build cost.** Claude writes all of the code from the spec (CLAUDE.md role contract), so the build cost is Claude Code usage plus the developer's review and commit time. Estimate it from:
  - the build's pieces as the docs describe them today: connectors and producers (engine tickets 30, 32, 34, 36, 70, 74), the claims door and core (17, 18, 21, 23), schema and migrations (`docs/evidence_layer_plan.md` §4), Celery chains (38), the read API (41), the website (chains 60, 61), and the test suites with real fixtures (CLAUDE.md definition of done);
  - this project's measured session sizes: research tickets record their token counts (for example chains 66 about 4.1M tokens, chains 82 about 2.72M), and grilling sessions can be sized from their transcripts if available;
  - current Anthropic prices from Anthropic's own pricing documentation, looked up at the time, never from memory. Show both API pricing and the subscription plans, since the developer may be on either. Give developer time as hours, not dollars.
  - The spec doesn't exist yet, so say plainly how rough the build figure is and what would sharpen it.
- **Seeding pass.** Count documents from what's decided:
  - brands: 37 launch industries at 30 brands per list where 30 exist, lists that only grow, plus the extra batch of PE brands outside the launch industries (chains 55, 81, 91, 92, 93; `docs/pre-launch-seeding.md`); list-building itself about 1.2M to 1.6M Claude tokens (chains 55);
  - per brand: EDGAR full-text search, first run since 2001, up to 100 hits per name, each read whole (70); DeepSeek Search for past coverage (73, 118); registry pages (30);
  - shared: newsroom first crawls (about 45,000 LLM reads, 30 via 42); Form ADV monthly files and IAPD PDFs (34; parser, no LLM); about 2,400 BDC filings (36; parser, plus one LLM read of each 10-K's Item 1); 13D and 13G filings (70; parser);
  - price per read: about $0.0044 per document, $45 to $54 per 10,000, on DeepSeek's own API (22); the OpenRouter fallback only during outages (77).
- **Monthly running.** Re-reads on real text changes (20), new filings and releases, re-read cadences (37; 119 still open, so use ranges), recompute and the nightly drift check (68), a re-read of everything when a new prompt or model version ships (22: about $45 to $54 per 10,000 documents), search traffic (40), Google Places only on demand, hosting, storage, backups and monitoring (43 open: price two or three realistic options), Cloudflare Pages for the website (60), and the domain (117).
- **Stale figures to replace:** ticket 42's spend figures (2026-11-04) assume Claude batch pricing for extraction (about $120 to $240 per seeding pass of about 1,000 brands, $20 to $120 a month). Extraction has since moved to DeepSeek.
- **Rules:** no new paid API calls; use measured figures and published prices. Vendor pricing pages are sources, each cited with the date read. Bot rules as in CLAUDE.md, and stop and report on any permission refusal. No paywalled market data, no OpenAI models. Mark every figure that rests on an open ticket (94, 119, 43, 117) so the estimate can be re-run when they settle.

## Answer

Resolved 2026-11-20 by a background agent (about 256k tokens, no paid API calls). Findings: `.scratch/engine/research/cost-estimate.md`, every figure traced to a ticket or a vendor page read that day.

- **Build:** about $2,100 to $9,200 of Claude Code usage at Opus 5.5 API list prices (about $1,050 to $4,600 at Sonnet 5.5), or $500 to $900 in Max plan fees ($100 a month) or $1,000 to $1,800 on Ultra ($200 a month) over the 5 to 9 months the build would take at the measured pace; 130 to 370 developer hours. Rough to a factor of two either way, since no spec exists: 83 to 152 active days at $25 to $60 a day, against a measured $39 per planning day.
- **Planning so far (measured):** $746 at Opus 5.5 list prices over 19 active days (2026-10-17 to 2026-11-20; 12 sessions, 70 subagent runs, 1.92 billion tokens, nearly all cache reads). A floor: Claude Code deletes transcripts after 30 days. Research tickets' recorded token counts are worth $28 to $35 per million.
- **One seeding pass:** about $1,200 to $9,500, of which DeepSeek reads are $850 to $7,700 and Claude list-building and registry research $360 to $1,760.
- **A typical month at launch:** about $110 to $1,730 (model and API $23 to $1,074; hosting $65 to $450; Claude Code upkeep $20 to $200). Each new prompt or model version re-reads the corpus for another $850 to $7,700.
- **Biggest drivers:** EDGAR full-text search with every hit read whole (seeding $600 to $5,625, 60,000 to 225,000 filings; a long filing costs about $0.019, not the $0.0044 average); version re-reads; the build; registry research ($325 to $1,700, unmeasured); hosting ($65 Hetzner to about $450 Fly.io, with Backblaze B2 Object Lock at no extra cost).
- **Prices confirmed:** DeepSeek Flash $0.15 in and $0.60 out per million off-peak, double at peak (21% of the week); DeepSeek Search $0.75 per 1,000; Cloudflare Pages Free covers the site; Places IDs-only Text Search free. Not read: Cloudflare's domain search (403; the .com price came from trade press), AWS RDS and Render (no figures in the page text).
- **What sharpens it:** a free count-only EDGAR full-text search dry run over all names; timing one connector build from its transcripts; a registry-research pilot of about 20 entries.

Handed on:
- "Operational identity, budgets and guardrail values": replacement spend figures for the caps; full-text search noise is the single largest swing.
- "Hosting, storage and deployment": three priced options and Backblaze B2 for storage with Object Lock.
- "Task: Draft prompt p10 and run the approval check": a version shipped after seeding re-reads everything for $850 to $7,700.
