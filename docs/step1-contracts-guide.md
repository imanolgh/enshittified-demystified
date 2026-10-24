# Step 1 Guide — Hand-Writing `app/core/contracts.py`

Working guide for roadmap Step 1 (Phase 1, Day 1). The developer writes the file; this doc explains what each piece is, who produces and consumes it, which fields the design docs call for, and which decisions are open. Sources: `build_roadmap.md` Step 1, `evidence_layer_plan.md` §4 (schema) and §5 (pipeline stages), CLAUDE.md invariants.

> Note: Pydantic idioms below verified against current Pydantic v2 docs via Context7 (2026-09-14).

---

## What `contracts.py` is — and is not

This file holds the **Pydantic boundary contracts**: the shapes data must have to move between parts of the system. It is **not** the database. `core/models.py` (Step 2, SQLAlchemy) will mirror §4's tables; `contracts.py` defines what a connector hands to storage, what the LLM must return, and what the API serves. The two files will look similar — that's normal; they serve different masters (transport/validation vs. persistence).

It is called the constitution because every other component either emits these types or its output doesn't exist. Every constraint written here is enforced automatically at every boundary, forever.

Write the file top to bottom in the order below — each piece builds on the last.

---

## 1. The enums (shared vocabulary)

Small `StrEnum` classes (stdlib, Python 3.11+). They JSON-serialize as plain strings, compare equal to `"acquired_by"`, and print as their value in f-strings/logs. Chosen over the older `(str, Enum)` pattern because on Python 3.12 `f"{Predicate.OWNED_BY}"` gives `Predicate.OWNED_BY` with `(str, Enum)` but `owned_by` with `StrEnum`; Pydantic treats both identically.

| Enum | Values (source) | Why it's a contract |
|---|---|---|
| `Predicate` | see decision box below | closed set; invalid predicate = claim rejected for free |
| `SourceType` | `edgar, sos, portfolio_page, press_release, cafr, form5500, news, court, submission` (§4 documents) | drives the two-independent-sources rule and official-filing self-verify |
| `EntityType` | `business, brand, sponsor, fund, dso, pension, insurer, lender` (§4 entities) | resolution + serving vocabulary |
| `OwnershipType` | `pe_fund, pe_backed, conglomerate, family, employee_owned, trust, public, independent, unknown` (§4 edges) | the LLM classifies against this at extraction |
| `Confidence` | `verified, reported, estimated` (§4 edges) | claim-card honesty levels |

These live in contracts (not models.py) because both the DB and the boundaries need them; models.py imports them from here.

> **✅ RESOLVED (developer ruling, 2026-09-14) — 7 predicates.** The canonical set is CLAUDE.md's: `acquired_by, owned_by, operates_location_of, lends_to, allocates_to, holds_position, renamed_from`. The plan doc's `majority_stake`/`minority_stake` were dropped: they expressed ownership *degree*, and the schema's pattern is *relationships are vocabulary, degrees are values* — stake size/type goes in the claim's `value` JSONB (e.g. `{"stake_pct": 65, "stake_type": "majority"}`), same as `lends_to` @ rate and `allocates_to` @ %. This also keeps Stage 5 corroboration intact (claims group by subject/predicate/object). `evidence_layer_plan.md` §4 has been updated to match.

## 2. `RawDocument` — what every connector emits

- **Produced by:** every `source_connectors/` module. **Consumed by:** `store_document` (Step 4).
- **Mold:** §4 `documents` table, minus DB-assigned fields (`id`, `storage_path`).

Field inventory to work from:

| Field | Notes / decisions |
|---|---|
| `source_type` | the enum |
| `url` | provenance. Decide: bulk files and API pulls aren't URLs — broader provenance field, or optional-with-validator? |
| `retrieved_at` | timezone-aware datetime (validator to enforce tz-awareness) |
| `sha256` | 64 hex chars — `Field(pattern=r"^[a-f0-9]{64}$")`. Decide: connector computes it, or storage computes on ingest? Either defensible; pick one and know why. |
| `mime_type` | plain string |
| `raw_text` | nullable — a PDF has none until parsed |
| `meta` | dict for parsed tables etc. (§5 Stage 2.3) |
| payload | the raw bytes/text storage will persist — decide how it rides along |

## 3. `ExtractedClaim` — what the LLM must return (the anti-hallucination contract)

- **Produced by:** parsing the Anthropic response (Step 7). **Consumed by:** `verify_citations`, then the claims door.
- Anything failing validation is **dropped and logged before touching the DB** (§5 Stage 3.2) — every constraint here is a hallucination filter.
- **Mold:** §4 `claims` table, minus DB/pipeline-assigned fields (`id`, `quote_verified`, `quote_offset`, `status`). Note: at extraction time you have entity *names*, not ids — resolution assigns ids.

| Field | Notes / decisions |
|---|---|
| `subject` | name string, non-empty (`Field(min_length=1)`) |
| `predicate` | the enum |
| `object` | name string, non-empty |
| `verbatim_quote` | **required**, meaningful `min_length` — the soul of the product; `verify_citations` string-matches this |
| `event_date` | optional |
| `value` | optional dict (amounts, %, rates) |
| `ownership_type` | taxonomy classification |
| `doc_sha` | document reference — part of claim uniqueness: hash(subject, predicate, object, doc_sha, quote) |

Decisions:
- `ConfigDict(frozen=True)`? Claims are append-only — immutable instances match the domain.
- Do `extraction_model` / `extracted_at` ride on this model, or get attached by the task? (Argument for the task: the LLM shouldn't self-report its model name.)

## 4. The extraction result envelope — where `no_evidence_found` lives

**Biggest open design call.** §5 Stage 3 says extraction returns *either* claims *or* an explicit `no_evidence_found` — a first-class, publishable outcome. Two clean shapes:

1. **Envelope model** — `ExtractionResult` with `claims: list[ExtractedClaim]` and `no_evidence_found: bool`, plus a `model_validator` enforcing consistency (empty list ⟺ flag true). Explicit: the LLM must actively say "nothing here" rather than lazily returning `[]`. More aligned with the invariants.
2. **Empty list = no evidence, by convention.** Simpler, but silence and *verified absence* become indistinguishable — and the product treats them differently ("no PE evidence found (checked {date})" is publishable content).

Developer picks; be able to defend the choice.

## 5. `ResolvedEntity` — what resolution returns

- **Produced by:** `resolve_entity` (Step 9). **Consumed by:** the pipeline downstream.
- Inventory (§5 Stage 1.6 + §4 entities): `entity_id` · `canonical_name` · `entity_type` · matched-vs-created flag · match score · aliases recorded.
- Keep minimal now; Step 9 pressure-tests it and can extend it.

## 6. `ClaimCardOut` and `EdgeOut` — the public shapes

- **Produced by:** API routes (Steps 23, 26) — but defined now because the claim card *is* the product and belongs in the constitution.
- `ClaimCardOut` ≈ claim + quote + document provenance + verification status: "here's the assertion and exactly where it comes from."
- `EdgeOut` ≈ §4 edges: from/to, relation, `confidence`, `ownership_type`, effective date, supporting claim ids — retraction-aware.
- Mechanics: `ConfigDict(from_attributes=True)` so they can later be built directly from SQLAlchemy rows.
- Don't over-design today; the endpoints will refine them.

---

## Pydantic v2 idioms you'll use

- `class Predicate(StrEnum)` — string-enum behavior described above.
- `Field(min_length=1)`, `Field(pattern=...)` — declarative constraints.
- `@field_validator("quote")` with `@classmethod` stacked under it — anything a constraint can't express (the validator receives `cls`, not `self`).
- `@model_validator(mode="after")` on a method returning `Self` — cross-field consistency (the envelope).
- `model_config = ConfigDict(frozen=True)` — immutability.
- `ConfigDict(from_attributes=True)` — build Out-models from ORM rows.

## How to work

1. Rule on the predicate discrepancy first.
2. Write enums → `RawDocument` → `ExtractedClaim` → envelope → `ResolvedEntity` → Out models.
3. Test-drive in a REPL as you go: `uv run python`, then `ExtractedClaim.model_validate({...})` with junk input — if garbage gets through, add the constraint.
4. Definition of done: the file reads like the constitution — you can recite the system's rules from it the next morning. Then hand it over for the Step-1 validation test suite (Claude writes: bad predicate rejected, empty quote rejected, enum round-trips, serialization, frozen behavior, envelope consistency).
