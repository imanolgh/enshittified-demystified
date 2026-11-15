# Extraction model comparison on audit documents

Run 2026-11-13 for engine "Task: Compare extraction models on audit documents". Candidates and prices: [extraction-models](extraction-models.md).

## Method

- **Documents:** 50 fetched under the bot rules (identified user agent, robots.txt obeyed, no wire-service pages): 45 ordinary pages from all ten audit categories (company and sponsor pages, issuer releases, news; median about 1,600 tokens) and 5 SEC filings: the Dollar General, Petco and Burlington 10-Ks (about 80,000 to 110,000 tokens each), Mister Car Wash's merger 8-K and Driven Brands' Take 5 release. Text built the way the engine will: hidden elements kept, image `alt`, link `title` and `aria-label` written in place. A document was used only if the audit's verified quote appears in that text.
- **Known facts:** 70 ownership quotes the category audit had already checked against the source pages (15 of them in the filings).
- **Same instructions for every model:** a system prompt written from the rules recorded on "Extraction execution" (subject → object predicates `acquired_by`, `owned_by`, `managed_by`, `renamed_from`; names as written; fund and firm both claimed; sellers and exits as `holding: former`; deal status; stakes only when stated; listed means current; exact quotes; owner descriptions) and a strict JSON schema. One document per request, whole filings in one request, the brand named. Each model ran with its default thinking settings, one attempt per document (rate-limited requests were resent).
- **Routes:** OpenRouter with zero data retention and only hosts honoring every parameter (Claude ran on Google's endpoint; DeepSeek on FP8 hosts, spread by OpenRouter over nine of them); DeepSeek's own API (`deepseek-flash`, JSON mode, no search tools). Qwen3.8-Max was left out: OpenRouter had no zero-retention host for it.
- **Scoring:** valid = parses and matches the schema; quote match = the quote appears in the stored text exactly after collapsing whitespace and straightening quote marks (dashes not normalized); fact found = a passing ownership claim shares a run of at least 40 characters (or half the audit quote) with a known fact's quote.
- **Spend:** $13.81 on OpenRouter, $0.09 on DeepSeek's own API.

## Results

| Model (route) | Valid answers | Known facts found | In filings | Claims made | Quotes matching | Cost, 50 docs | Median seconds |
|---|---|---|---|---|---|---|---|
| Qwen3.8-27B (OpenRouter) | 49 of 50 | 40 of 70 | 11 of 15 | 94 | 99% | $1.30 | 76 |
| Mistral Large 4 (Mistral) | 50 | 38 | 7 | 98 | 90% | $1.04 | 73 |
| Kimi K3.1 Pro (OpenRouter) | 49 | 38 | 6 | 112 | 100% | $3.09 | 27 |
| Claude Opus 5.5 (OpenRouter) | 50 | 37 | 10 | 112 | 100% | $3.80 | 9 |
| GLM-5.3 (OpenRouter) | 43 | 37 | 5 | 131 | 94% | $2.42 | 90 |
| DeepSeek V4.1 Flash (DeepSeek's own API) | 50 | 35 | 7 | 93 | 100% | $0.09 | 7 |
| DeepSeek V4.1 Flash 1017 (OpenRouter) | 50 | 34 | 6 | 90 | 92% | $0.21 | 10 |
| Claude Sonnet 5.5 (OpenRouter) | 50 | 33 | 6 | 82 | 100% | $1.87 | 6 |
| Claude Haiku 5.5 (OpenRouter) | 50 | 31 | 6 | 67 | 100% | $0.29 | 5 |

Owner-description quotes matched at 96 to 100 percent for every model.

*Correction (2026-11-14): most quote failures in this table came from the test's own text extraction, not the models; see "Extraction artifacts" below. With those set aside: Mistral 96.9%, GLM 99.2%, DeepSeek through OpenRouter 96.7%, Qwen3.8-27B 98.9%; Claude, Kimi and DeepSeek's own API stay at 100%.*

## What the numbers show

- **Facts found are close.** Every model found 31 to 40 of the 70 known facts. At this sample size a gap of a few facts is noise. "Found" means quoting the audit's sentence; a model can also find true facts the audit didn't record, and more claims don't mean more correct claims (precision was not measured).
- **Long filings separate two models:** Qwen3.8-27B found 11 of 15 facts in the filings and Opus 10; the rest 5 to 7.
- **Quote matching separates the routes.** Claude, Kimi and DeepSeek's own API matched every quote. Mistral lost 10 percent, DeepSeek through OpenRouter 8 percent, GLM 6 percent: evidence the engine would discard.
- **The host matters as much as the model.** DeepSeek's OpenRouter failures came from two hosts (Parasail 0 of 4 quotes, StepFun 11 of 14); its other seven hosts matched every quote. GLM's came mostly from Fireworks (0 of 6). DeepSeek's own API matched all 93.
- **Some failures are near misses.** A failed GLM quote contains an en dash ("– operating under the brands of"); how `verify_citations` normalizes dashes is still open ("Citation verification rules").
- **Overthinking costs validity.** GLM's 7 invalid answers all ran out of output room (32,000 tokens) while reasoning; Kimi and Qwen3.8-27B each had one.
- **Cost and speed spread widely:** DeepSeek's own API cost $0.0018 a document and Claude Haiku $0.0057; Opus $0.076. Haiku, Sonnet and DeepSeek's own API answered in 5 to 7 seconds; Mistral, Qwen3.8-27B and GLM took 73 to 90.

## Precision check (2026-11-14)

Twenty claims drawn at random from each route's claims whose quotes passed (180 in all), shuffled together with the model names hidden, each judged on whether its quote supports it as stated: correct; partly right (the relationship is right but a detail is wrong); wrong (the quote doesn't support it). Every verdict was written down before the key was opened. Claude judged, so the developer may want to recheck; the items, verdicts and key are kept at `~/.local/share/extraction-eval/out/` (`precision-items.txt`, `precision-judgments.tsv`, `precision-key.json`).

| Route | Correct | Partly right | Wrong |
|---|---|---|---|
| Claude Sonnet 5.5 | 20 | 0 | 0 |
| Kimi K3.1 Pro | 20 | 0 | 0 |
| Claude Opus 5.5 | 19 | 0 | 1 |
| Qwen3.8-27B | 18 | 2 | 0 |
| Mistral Large 4 | 18 | 2 | 0 |
| DeepSeek V4.1 Flash 1017 (OpenRouter) | 18 | 2 | 0 |
| GLM-5.3 | 18 | 2 | 0 |
| Claude Haiku 5.5 | 17 | 3 | 0 |
| DeepSeek V4.1 Flash (DeepSeek's own API) | 15 | 0 | 5 |

- **No model invented a relationship.** Every wrong or partly right claim described a real relationship on the page; the errors were in details or in the quote chosen.
- **DeepSeek's own API: one pattern, five times.** All five wrong claims came from Ahold Delhaize's brands page, where it quoted the heading "our family of great local brands" for Food Lion, Stop & Shop, Gall & Gall, Delhaize and Super Indo instead of each brand's own line. The facts are true, but the quote doesn't name the brand, so it proves nothing. Opus's one wrong claim was similar: it credited Anchorage alone with the majority stake that the quote gives to a whole lender group, without naming Anchorage.
- **Details that would change what publishes:** Haiku read "reinvested 100% of their interests" as the Pessina family owning 100% of Walgreens (a stake that would contradict Sycamore's); GLM marked Scooby LP, Petco's current controlling parent, as a former owner (which would end a real ownership); DeepSeek through OpenRouter marked a completed growth investment as announced (it would sit as a pending deal and not count). Mistral claimed an exit the quote doesn't state.
- **Harmless details:** dates more precise than the text ("later that year" given as November 2012; a 2023 date the page doesn't give), and two renames whose quote lacks the former name (the engine's rename check would reject those).
- **Sample size:** 20 claims per route, many from the same few pages (the Ahold Delhaize brands page alone supplied about 30 of the 180), so differences of one or two claims are noise.
- **For "Citation verification rules":** a check that a claim's names appear in its quote (allowing the page's own owner as the unnamed object of a portfolio listing) would have caught all six wrong claims.

## DeepSeek prompt iteration (2026-11-14)

At the developer's request (budget: the DeepSeek balance, up to $4.85), DeepSeek V4.1 Flash on DeepSeek's own API was tested in rounds: run a chunk, find error patterns, fix the prompt, run again. 158 documents in all: the original 50, chunk 2 (53 new: 40 pages, 13 filings) and chunk 3 (55 new: 41 pages, 14 filings), with 223 known facts. Spent: $2.05 by the balance (DeepSeek billed about twice the off-peak rate assumed). Raw outputs and scripts: `~/.local/share/extraction-eval/`. The version 5 prompt and schema: [extraction-test-prompt-v5](extraction-test-prompt-v5.md).

**What each version changed**
- v2 (the developer's two fixes): the quote must name the claim's subject (and the owner, unless the page is the owner's own holdings list), never a heading; never derive a stake percentage from other numbers.
- v3: prefer a sentence over a bare list entry; owners described but not named ("family-owned", "employee-owned") still get a claim with that phrase as the name; "decision to acquire", "will acquire" and "definitive agreement" are announced; dates no more precise than the text; expected closing copied from the claim's own quote; never combine two owners in one name; "joined the Mars family" is figurative.
- v4: one unbroken stretch, never reworded; status words in the quote where the page gives them; trademark notices ("X is a trademark of Y") give owned_by; read the whole document and report every ownership fact (brand lists, acquisitions, subsidiaries, holders).
- v5: short quotes (one clause or sentence, about 250 characters, copied not retyped); real organization names, never a bare defined term ("Parent", "Merger Sub"); "former" only when the quote states the sale or exit; skip merger vehicles.

**Results on the original 50 documents**

| Version | Claims | Quotes matching (as scored) | Quotes naming no subject | Known facts found (of 70) |
|---|---|---|---|---|
| v1 | 93 | 100% | 22 | 35 |
| v2 | 96 | 100% | 1 | 33 |
| v3 | 98 | 97% | 1 | 38 |
| v4 | 139 | 94% | 1 | 37 |
| v5 | 151 | 99% | 5* | 41 |

*Mostly filings where the quote uses a defined term ("the Company") and the claim gives the real name, which the automatic check can't link.

On the new chunks, v5 found 45 of 78 (chunk 2) and 47 of 75 (chunk 3) known facts, against v3's 39 of 78 on chunk 2.

**Blind precision checks** (claims mixed across versions, version hidden until every verdict was written):

| Version | Fully correct | Partly right | Wrong |
|---|---|---|---|
| v1 | 13 of 20 (65%) | 1 | 6 (all: quote names neither side) |
| v4 | 54 of 60 (90%), over two samples | 6 | 0 |
| v5 | 39 of 40 (98%) | 1 (an ambiguous "announced the recapitalization") | 0 |

Remaining non-prompt issue: a company in Roark's CSS-hidden "Previous Investments" section reads as current, the markup-only status the planned status selector covers.

**Extraction artifacts.** Most failed quotes were the test's fault, not the model's. The test's HTML-to-text step put a space wherever HTML splits text into separate elements, so the stored text read "100 %", "$ 1.473 billion" and "Werhahn Group .", and SEC page footers ("76 Table of Contents") sat mid-sentence. The models quoted the document as it reads ("100%"). With spacing, dash style, ® marks and page footers set aside, v4's quotes match 99.2% and v5's 99.3%; the only real v5 failure is one sentence quoted for three brands. A repair test (send the passage around the best match and ask for an exact copy) fixed 12 of 15 failed v5 quotes, by copying the artifacts. Two engine consequences: the HTML text extractor must not insert separators between inline elements and must handle filing page footers ("Document storage" implementation, raised on "Citation verification rules"), and quote verification may need to ignore spacing around numbers and punctuation.

**Confirmed with clean text (2026-11-14).** All 158 documents were re-fetched (157 still served) and extracted with block-aware spacing: line breaks only around block elements (paragraphs, headings, list items, table rows), nothing between inline pieces, attribute text written in place as before. v5 then read that clean text: **615 of 615 quotes matched it exactly** (156 of 157 answers parsed; $0.73). Known facts found: 126 of 217 (58%) whose audit quote is still on the page. Checking the earlier answers against the clean text is not a fair test: models given the artifact-laden text reproduce its quirks (Qwen3.8-27B fell from 98.9% to 91.5% that way, while GLM rose from 93.9% to 98.5%). The design point: the model and the quote check must see the same cleanly extracted text.

**Real recall (2026-11-14).** The "known facts found" figure undercounts. All 92 misses of the clean-text run were sorted by hand: 38 audit lines are not ownership facts (stock-ticker lines, founding stories, datelines, copyright footers); 36 relationships were found through a different quote; 2 were lost to one invalid answer; 16 were real misses. So the model found 162 of 179 actual ownership facts, **about 90%**. Real misses: three facts other runs caught (Golden Gate behind Tidal Wave, a 2017 Aspen Dental release with no claims, Kahoots' family ownership); a lender group's named members (Brigade, Arbour Lane, Anchorage at Gabe's); the sponsor behind a buyer ("affiliates of Bansk Group" behind PetIQ's buyer); brands mentioned on another subject's page (Monarch Dental, Affordable Dentures, MedVet); four facts in one long Unilever annual report (Liquid I.V., Nutrafol and its minority holders, Unilever's 3% holders); Giant Eagle's family ownership; Serta Simmons' post-restructuring owners; two operator details. Many of these also appear in other documents about the same brand.

**Version 6 (2026-11-14), on the 14 documents behind the real misses, run twice ($0.34).** Added: claim each named member of an owner group; claim the organization behind a buyer or parent ("affiliates of Bansk Group"); report every company a document mentions; several facts about one company are all reported. It recovered 11 of the 18 targeted facts across two runs (8 and 10 in single runs): Gabe's lender members, Bansk behind PetIQ's buyer, Golden Gate behind Tidal Wave, Smile Brands' and Affordable Care's brands, Giant Eagle's family ownership beside the Kroger deal, Kahoots, the 2017 Aspen Dental investment, Unilever's Liquid I.V., Nutrafol and its large holders. But "report every company" broke large portfolio pages: Leonard Green's 108-company page ran out of the 32,000-token output limit in both runs (invalid, so every claim lost; v5 read it), Roark's page overflowed once and once listed brand-to-company pairs without any company-to-Roark claim, and one run reversed a direction ("Serta Simmons Bedding owned_by Beautyrest"). v6 is not safe as written; it needs more output room, a rule that every company on an owner's portfolio page is owned by that owner first, and a direction reminder.

**Versions 7 and 8 (2026-11-14, $0.27).** v7 added: the object is always the owner (never the reverse); on an owner's portfolio page, first an owned_by claim from every listed company to the page's owner; output limit raised from 32,000 to 120,000 tokens. On the 14 documents, run twice: 11 and 9 of the 18 targeted facts (12 across both runs); Leonard Green's page read fully (108 and 106 of its 108 companies owned by Leonard Green; the answers needed about 36,000 tokens, so the old limit was what broke v6); no reversed directions. Roark's page stayed a blind spot (0 or 1 Roark claims; v5 made no claims there at all). v8 added that a portfolio page often states no relationship in words and every listed company is still the site owner's holding: one run claimed all 86 Roark companies with exactly the 30 former ones marked former, the other made 0 Roark claims; Leonard Green's page stayed correct (110 claims, 39 former, no bad quotes). Not fixed: Serta Simmons' post-restructuring owners, Nutrafol's minority holders, two operator details. A safeguard for "Extraction execution": re-read any portfolio page whose answer names no claim for the page's owner (the registry triggers the retry; nothing from it enters the prompt). v6 to v8 were tested only on these 14 documents.

**Version 8 on all 157 documents (2026-11-14, clean text, 120,000-token output limit, about $0.70).** Against v5 on the same text: 157 of 157 answers valid (v5: 156), 1,376 claims (v5: 615), 98.8% exact quotes (v5: 100%), 135 of 218 known facts on the strict metric (v5: 126 of 217). Blind precision check (40 v8 and 20 v5 claims, versions hidden): v8 38 of 40 fully correct, 2 partly right, none wrong; v5 20 of 20. The partly right ones: an ambiguous "in its acquisition" marked announced, and a quote naming Brigade only as a member of the lender group (the ownership is in the next sentence). **A risk the sample didn't show:** on RiverGlade's page v8 claimed 12 deals listed under "Prior to RiverGlade" (its team's deals at earlier firms) as RiverGlade's; all 12 failed the quote check only because the quotes included the heading, so quoted cleanly they would have published false ownership. v8's portfolio rule needs an exception for entries a page says are not the owner's holdings ("Prior to ...", "prior firm investments", team experience). Roark's page still came back with no Roark claims on this run (the re-read safeguard applies). Prompt: [extraction-test-prompt-v8](extraction-test-prompt-v8.md).

**Consistency.** v5 run twice on chunk 3: 236 and 186 claims; only 51% of distinct claims appear in both runs (the core facts are stable, the churn is in subsidiaries, brand lists and name variants); current/former or deal status differed on 5 of 141 shared claims; known facts 48 and 46 of 75, 51 in either run. A second read adds about 6% more known facts for about a third of a cent per document.

**Described owners.** v3's rule produces owners named "family", "employee" or "a group of its existing institutional investors". The engine must not resolve these generic names to one shared entity across brands (raised on "Entity resolution algorithm").

## Limits

One run, 50 documents, default thinking settings, one prompt (not tuned per model); precision checked on 20 claims per route only. Qwen3.8-Max untested. DeepSeek's own API can't pin a version and stores data in China (see the research note). Raw responses and scripts are kept outside the repo at `~/.local/share/extraction-eval/`.

## Haiku and DeepSeek through OpenRouter (2026-11-14)

At the developer's request, to judge DeepSeek through OpenRouter as the fallback route and compare Claude Haiku 5.5 on the same terms. Both read the 157 clean-text documents with the v8 prompt (tuned on DeepSeek, which may favor it), the brand named as before, a 120,000-token output limit, zero data retention and a strict JSON schema. DeepSeek was pinned to `deepseek-v4.1-flash-1017` on FP8 hosts, excluding Parasail and StepFun. Haiku ran on Google's endpoint (OpenRouter's choice). Each route ran twice. Spent: $5.99 of the OpenRouter balance ($4.98 left). Raw outputs: `~/.local/share/extraction-eval/out/` (`*-v8`, `*-v8-r2`), scorer `scripts/score_clean.py`.

| | Haiku 5.5 (OpenRouter) | DeepSeek 1017 (OpenRouter) | DeepSeek's own API (earlier v8 run) |
|---|---|---|---|
| Answers lost, two runs | 0 of 314 | 5 of 314 | 0 of 157 (one run) |
| Claims, run 1 / run 2 | 944 / 900 | 1,357 / 1,414 | 1,376 |
| Exact quotes, run 1 / run 2 | 100% / 99.7% | 91.2% / 99.6% | 98.8% |
| Known facts found (strict metric, of 218) | 122 / 119 | 133 / 136 | 135 |
| Billed per document | $0.0106 / $0.0108 | $0.0083 / $0.0098 | about $0.0045 |
| Median seconds | 9.7 | 17 | 11.7 |
| Distinct claims found in both runs | 68% | 64% | (v5: 51%) |

- **Haiku's cost is in long filings.** Its tokenizer counts about 60% more tokens than DeepSeek's for the same text (3.98M against 2.43M), so 14 filings crossed 100,000 prompt tokens, where its price rises from $0.10 / $0.50 to $0.50 / $2.50 per million. Those 14 cost $1.27 of run 1's $1.67 ($0.091 each); the other 143 documents cost $0.0028 each. DeepSeek through OpenRouter: $0.037 per long filing, $0.0056 per other document. Anthropic's own Batch API would halve Haiku's figures; OpenRouter offers no zero-retention batch.
- **Haiku skips large portfolio pages** (corrected below: on Leonard Green's page this came from the test's brand line, not the model). Leonard Green's 108-company page: 1 claim in both runs (DeepSeek through OpenRouter 71 and 107 Leonard Green claims; DeepSeek's own API 110). Roark's page: no Roark claims in either run (DeepSeek through OpenRouter 86 and 85, with exactly the 30 former ones marked former in run 1 and none in run 2).
- **"Prior to RiverGlade" affects both models.** Haiku run 1 and DeepSeek through OpenRouter run 2 each gave the 11 or 12 deals listed under "Prior to RiverGlade" as former RiverGlade holdings, with bare-name quotes that pass the quote check. The exception belongs in the prompt whichever model is used.
- **DeepSeek's losses came from hosts.** Run 1: Morph rewrote all 94 quotes on one portfolio page ("[link: Alexia]" where the page has "[link: Close]") and once returned nothing; Makora put a stray quote mark before all 22 quotes on one filing; Cohere cut one answer off. Run 2: Mistral (twice) and SiliconFlow spent the whole 120,000-token limit reasoning and returned no answer. Morph matched every quote in the first test. Hosts with no failures in either run: DeepInfra, InferenceNet, CoreWeave (plus Novita and Venice, with few documents). DeepSeek's own API never ran away like this.

**Blind precision check** (40 claims each from Haiku and DeepSeek through OpenRouter, 20 from DeepSeek's own API as a control, run 1, at most two per document per route; judged by a separate agent that never saw the key; items, verdicts and key in `out/precision5-*`):

| Route | Fully correct | Partly right | Wrong |
|---|---|---|---|
| Haiku 5.5 (OpenRouter) | 34 of 40 (85%) | 6 | 0 |
| DeepSeek 1017 (OpenRouter) | 37 of 40 (92.5%) | 3 | 0 |
| DeepSeek's own API (control) | 18 of 20 (90%) | 1 | 1 |

Haiku's partly right claims are mostly deal stage: announced deals given as completed or as current ownership (5 of 6), which would show a pending deal as done. DeepSeek's: one sponsor credited with control five sponsors share, a "decision to acquire" taken as a completed exit, a continuing owner named as acquirer. The wrong one: a bare menu item ("Golden Nozzle") quoted as a holding. The judge also flagged licensed brands on a maker's "Our Brands" page (Meyer listing KitchenAid) as a case for the prompt rules.

## Haiku without the brand line (2026-11-14 diagnostic)

Every run so far opened the request with "These documents were fetched while researching the brand X", which production will not send ("Extraction execution" Q3). Haiku also ran at its default effort (medium), thinking about 1,700 tokens on Leonard Green's page where DeepSeek thought 20,000 to 26,000. Before v7, every model, DeepSeek included, gave Leonard Green's page one claim. Three portfolio pages re-run with v8 ($0.11 on OpenRouter, a few cents on DeepSeek's own API; outputs `out/probe-*`, script in the session scratchpad):

| Run | Leonard Green: claims naming LGP (former) | Roark: claims naming Roark (former) | RiverGlade: former holdings from "Prior to RiverGlade" |
|---|---|---|---|
| Haiku, brand line, default effort (earlier runs) | 1 | 0 | 0 to 12 |
| Haiku, no brand line, default effort | 107 (36) | 0 | 11 |
| Haiku, no brand line, high effort | 111 (40) | 0 | 12 |
| Haiku, brand line, high effort | 111 (40) | 0 | 0 |
| DeepSeek's own API, no brand line | 108 (37) | 86 (30) | 12 |

- Leonard Green's page: Haiku reads it as fully as DeepSeek once the brand line goes or effort rises. With the brand line at medium effort it answered only for the named brand (Aspen Dental). The "skips portfolio pages" finding was a test artifact on this page.
- Roark's page (no relationship stated in words): Haiku gave brand-to-company claims from the entries ("GoTo Foods is the parent company of Auntie Anne's…") and no Roark claim in any setting. A real difference with v8 as written.
- Without the brand line, both models gave the "Prior to RiverGlade" deals as former RiverGlade holdings (11 and 12, every quote passing). The brand line had been hiding this for Haiku. It belongs to "Extraction prompt rules".
- Cost on Leonard Green's page with no brand line: Haiku about $0.023, DeepSeek's own API about $0.03 off-peak and $0.06 peak (50,800 output tokens).
- Every other Haiku figure above (known facts, precision) was measured with the brand line, so it may understate Haiku. Cross-model check from existing runs: DeepSeek's own API plus a Haiku run finds 144 known facts, the same as plus a second DeepSeek run (145 and 146); Haiku found 8 facts no DeepSeek run found (5 in filings), DeepSeek 27 that no Haiku run found (16 on pages).

## DeepSeek and Qwen3.8-27B with no brand named (2026-11-15)

At the developer's request, after Haiku testing was stopped: DeepSeek V4.1 Flash on DeepSeek's own API against Qwen3.8-27B through OpenRouter, both under production conditions: v8 prompt, no brand line, all 157 clean-text documents, two runs each. Qwen ran on zero-retention hosts at FP8 or BF16 with at least 131,072 output tokens (Chutes, Near AI, Ionstream, PrimeIntellect and Venice excluded for their 65,536 cap); its hosts allow 262,144 tokens of input plus output, so the two largest filings were read in windows (two and three) split at line breaks with about 2,000 tokens of overlap. DeepSeek ran with a 120,000-token output limit. Spent: OpenRouter $17.60 (Qwen runs $13.72, tuning $3.81), DeepSeek $1.37. Outputs `out/*-v8-nb`, `*-v8-nb2`, `*-v8q-qt*`; scripts `run.py` (`--no-brand`, Qwen windows), `compare_routes.py`, `sample_precision6.py`.

| | DeepSeek, own API | Qwen3.8-27B, OpenRouter |
|---|---|---|
| Answers lost (314) | 0 | 3, all on Wafer: two ran to the 131,072-token limit repeating text, one returned nothing after 43,000 reasoning tokens |
| Exact quotes | 94.4% / 99.9% (81 of run 1's 84 failures on TSG's page, "[link: Alexia]" for "[link: Close]") | 99.3% / 98.4% |
| Known facts per run (of 218) | 141 / 142 | 129 / 133 |
| Pages / portfolio pages / filings, per run | 98 / 13 / 30 and 97 / 16 / 29 | 89 / 13 / 27 and 92 / 15 / 26 |
| Known facts in either run | 149 (101 / 16 / 32) | 151 (101 / 15 / 35) |
| Run-to-run agreement, distinct claims | 71% | 53% |
| Blind precision, 40 claims each | 37 correct, 2 partly, 1 wrong (92.5%) | 37, 2, 1 (92.5%) |
| Cost per document | $0.0044 (off-peak Sunday) | $0.044 |
| Median / slowest answer | 13 s / 2.5 min | 80 s / 28 min |
| Output tokens per run | 0.87 million | 3.0 to 3.4 million (about 2.8 million reasoning) |
| Leonard Green, claims naming the firm | 108 / 108 | 1 / 108 |
| Roark, claims naming Roark (former) | 86 (30) / 85 (29) | 85 (0) / 86 (30) |
| "Prior to RiverGlade" false holdings | 12 / 12 | 0 / 12 |

- Without the brand line DeepSeek improved on every earlier DeepSeek run: more known facts, Roark read correctly in both runs, run-to-run agreement up from 64 to 65% to 71%. The TSG quote rewrite earlier blamed on the Morph host also happens on DeepSeek's own API, so it is the model on that page; the quote check rejects those claims.
- Qwen's runs swing: Leonard Green's page got one claim in run 1 after 175,000 characters of reasoning that planned all 108 companies ("If too long, maybe truncated") and 108 in run 2.
- Cross-model second read: DeepSeek plus a Qwen run finds 150 to 155 known facts, against 149 for two DeepSeek runs.
- **Qwen tuning round** (v8 plus two sentences: never shorten a long answer; claim described owners and owners who retain a stake), two runs on the 27 documents where Qwen v8 missed facts DeepSeek found ($3.81): known facts there rose from 19 to 34 and 42 (DeepSeek 44 and 41 on the same documents, chosen for Qwen's misses), and Leonard Green was read fully in both runs. But both runs made the "Prior to RiverGlade" error, one gave no Roark claims, and blind precision fell to 87.5% (35, 2, 3): "privately owned" claimed as an owner twice. No full run of the tuned prompt.
- Judge's notes for "Extraction prompt rules": "privately owned" and "run by family" name no owner; "an affiliate of" is not ownership; a stake type stated for a group of sponsors is not each sponsor's; Meyer's "Our Brands" list mixes owned and licensed brands (KitchenAid).

