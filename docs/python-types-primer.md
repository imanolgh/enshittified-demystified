# Python Types Primer — for the Evidence Engine

The core Python data structures and type-annotation vocabulary used throughout this project, angled at a developer coming from PHP/Laravel. Each entry covers the structure itself, its annotation form (what you'll write in `contracts.py`, function signatures, and services), and where it shows up in this codebase.

---

## `list` — ordered, mutable, homogeneous-by-convention

The workhorse. PHP's numeric-indexed array.

```python
claims = []                    # empty
claims.append(claim)           # push
claims[0], claims[-1]          # first, last (negative index = from the end)
len(claims)                    # count()
claims[2:5]                    # slice: elements 2,3,4 (end-exclusive)
```

- Mutable: grows, shrinks, elements reassignable in place.
- Convention: all elements the same type, and annotations state it: `list[ExtractedClaim]`.
- In Pydantic, `claims: list[ExtractedClaim]` means "validate every element of the incoming array as an ExtractedClaim."

**Project use cases:** the extraction envelope's `claims: list[ExtractedClaim]`; a connector returning `list[RawDocument]`; `supporting_claim_ids` on edges; any API response returning multiple cards.

## `tuple` — ordered, **immutable**, heterogeneous-by-convention

No direct PHP analog: a fixed-length, frozen sequence where *position means something*.

```python
point = (3, 5)                 # parentheses; technically the comma makes the tuple
subject, pred, obj = triple    # unpacking
def resolve(...) -> tuple[int, float]:  # multi-value return
    return entity_id, score            # caller: entity_id, score = resolve(...)
```

- Immutable → hashable → usable as dict keys and set members (lists are not).
- Annotation is positional: `tuple[str, Predicate, str]` = exactly three elements, those types, those positions.

**Project use cases:** multi-value returns (`entity_id, score`); the claim-grouping key in Stage 5 — group claims by the tuple `(subject, predicate, object)`, which works as a dict key precisely because tuples are hashable.

## `set` — unordered, unique elements, O(1) membership

No real PHP equivalent (closest abuse: `array_unique` or array keys). A bag of distinct values with instant lookup.

```python
seen = set()                   # NOTE: {} is an empty DICT, not an empty set
seen.add(doc.sha256)
if sha in seen: ...            # O(1) — the whole point
a | b, a & b, a - b            # union, intersection, difference
```

- Mutable, unordered, no duplicates; elements must be hashable.
- Rare as a Pydantic field; common in logic.

**Project use cases:** sha256 dedup during crawls (the diff loop); the two-independent-sources rule — `len({c.source_type for c in group}) >= 2` counts *distinct* sources for free; comparing this crawl's roster against last crawl's (`new = current - previous`) for Acquisition Alarm.

## `dict` — key → value mapping

PHP's associative array; the second workhorse.

```python
meta = {"table_count": 3, "parser": "camelot"}
meta["parser"]                 # KeyError if missing — loud, unlike PHP's null
meta.get("parser")             # None if missing — the quiet version
meta.get("parser", "none")     # with default
for key, value in meta.items(): ...
"parser" in meta               # key membership
```

- Mutable; preserves insertion order (guaranteed since Python 3.7).
- Annotation names both sides: `dict[str, Any]`.
- Instinct check: a dict whose shape is *known and stable* is a Pydantic model waiting to be written. Reach for `dict` only when the shape is genuinely open.

**Project use cases:** `value: dict | None` on claims (amounts, %, stake info — deliberately shapeless); `meta` on documents (parsed tables); selector configs for the registry-driven sponsor crawler; grouping claims: `groups: dict[tuple[str, str, str], list[ExtractedClaim]]`.

## Union types — "either this or that"

Not a container — annotation vocabulary. Modern spelling is the pipe (Python 3.10+):

```python
event_date: date | None = None   # the one you'll write constantly
url: str | None                  # nullable string — PHP's ?string
identifier: int | str            # genuinely either
```

- Older spelling: `Optional[str]` / `Union[int, str]` from `typing` — same meaning, prefer `|`.
- **Nullable ≠ omittable.** `str | None` says None is an allowed *value*; whether the field may be *absent* comes from having a default (`= None`). They usually travel together but are separate ideas.
- Pydantic validates unions member-by-member; a union of models (discriminated union) is a real design tool — e.g. an extraction result that is either a claims envelope or a `no_evidence_found` marker.

**Project use cases:** nearly every optional field in `contracts.py` (`raw_text: str | None`, `event_date: date | None`, `value: dict | None`); potentially the extraction envelope design.

## Comprehensions — filter/map/collect in one expression

Laravel's `collect()->filter()->map()->values()` chain, built into the language. Read them left to right: *expression, loop, condition*.

**List comprehension** — produces a list:

```python
accepted = [c for c in claims if c.status == "accepted"]  # filter
names    = [c.subject for c in claims]                    # map
shas     = [d.sha256 for d in docs if d.raw_text]         # both at once
```

**Set comprehension** — same syntax, `{}`, produces a set (dedups automatically):

```python
source_types = {c.source_type for c in group}      # distinct sources in one line
if len(source_types) >= 2: publish_verified()      # the two-source rule, literally
```

**Dict comprehension** — `{key: value ...}`:

```python
by_sha = {d.sha256: d for d in documents}          # index a list by a field
```

Style rule for this project: one loop, at most one `if` — matching the "boring, explicit" quality bar. If a comprehension needs nesting or a second condition, write a normal `for` loop instead.

## The supporting cast (annotation vocabulary you'll also write)

| Annotation | What | Project use |
|---|---|---|
| `str`, `int`, `float`, `bool` | scalars; Pydantic coerces or rejects per its rules | everywhere |
| `datetime`, `date` (from `datetime` module) | timestamps vs calendar dates — distinct types | `retrieved_at: datetime` (tz-aware, validator-enforced) vs `event_date: date \| None` |
| `Enum` / `StrEnum` | closed vocabularies; `StrEnum` members are real strings, so they serialize and print as plain strings | `Predicate`, `SourceType`, `EntityType`, `OwnerKind`, `BusinessCategory`, `Confidence` |
| `Any` (from `typing`) | opt out of checking — use sparingly, on purpose | `dict[str, Any]` for `value`/`meta` |
| `None` | PHP's null; also a function's implicit return | defaults, sentinels |
| `Self` (from `typing`) | "this class" — return type of `@model_validator(mode="after")` | the extraction envelope's consistency check |

## Three traps

1. `{}` is an empty **dict**; empty set is `set()`.
2. **Mutable default arguments**: `def f(items: list = [])` shares ONE list across every call — classic Python bug. Correct: default `None` and create inside, or in Pydantic use `Field(default_factory=list)`. (Pydantic model fields don't share this bug, but know the rule.)
3. `dict["missing_key"]` **raises** `KeyError` rather than returning null — decide per call site whether loud (`[]`) or quiet (`.get()`) is correct; loud is usually right in pipeline code, where a missing key means a bug upstream.
