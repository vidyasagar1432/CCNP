# Creating Flashcard JSON from the CCNP Notes

This project turns the `.md` study notes into flip-card decks. Each deck is a
small JSON file saved **next to its `.md` file**. A build script bundles all of
them into `decks.js`, which `index.html` loads (works by double-clicking, no
server needed).

```
CCNP/
  index.html            app (already exists)
  decks.js              generated bundle (run build-decks.py)
  build-decks.py        bundles every Level*/<topic>.json → decks.js
  00. MOC - CCNP Study Map.md   top-level study planner / map of content
  Level 00 - Networking Basics/
    01. What is Networking.md      ← notes (source of truth)
    01. What is Networking.json    ← hand/AI-created deck for that topic
```

---

## 1. File location & naming

- Create **one JSON file per `.md` content file** (skip `index.md` / index topics).
- The JSON lives **beside its `.md`**, in the same `Level NN - Name/` folder.
- **Filename = the exact `.md` filename with the extension swapped to `.json`.**
  Example: `01. MAC Address.md` → `01. MAC Address.json`
  (keep any spaces/characters in the note's filename as-is).

## 2. Schema (follow exactly)

```json
{
  "title": "MAC Address",
  "level": 4,
  "levelTitle": "Level 04 - Ethernet & Switching",
  "exam": "ENCOR-350-401",
  "difficulty": "medium",
  "source": "01. MAC Address.md",
  "cards": [
    { "q": "How many bits is a MAC address?", "a": "48 bits (6 bytes).", "tag": "Core Concept", "context": "Exam" },
    { "q": "Broadcast MAC address?", "a": "FF:FF:FF:FF:FF:FF.", "tag": "Exam Trap", "context": "Exam" }
  ]
}
```

| Field | Source in the .md | Notes |
|-------|-------------------|-------|
| `title` | `# Heading` | Short topic name, no `#`. |
| `level` | frontmatter `level:` | Integer (0–30). |
| `levelTitle` | the folder name | Exactly `"Level NN - Name"`. |
| `exam` | frontmatter `exam:` | e.g. `ENCOR-350-401`. |
| `difficulty` | frontmatter `difficulty:` | `easy` / `medium` / `hard`. |
| `source` | the `.md` filename | Exact filename, incl. spaces, with `.md`. |
| `cards` | content sections | Array of `{ "q", "a", "tag", "context" }`. |

Frontmatter fallback (if the `.md` lacks a field): `level` from the folder
number (e.g. `4` for `Level 04 - …`), `exam` = `ENCOR-350-401`,
`difficulty` = `medium`. Do not invent any other metadata.

## 3. `tag` values — what each maps to

Use only these four values:

| tag | When to emit | Extraction rule |
|-----|--------------|-----------------|
| `Overview` | Top of the note | "What is X?" → the definition + purpose from the overview (usually 1–2 cards). |
| `Core Concept` | `## 2. Core Concepts` | Definitions, mechanics, diagrams-as-prose, lists (e.g. three duplex types), key formats/numbers. |
| `Quick Review` | `## 5. Quick Review Table` & comparison tables | Capture **unique** high-value facts from tables; do NOT make a card per row if the row merely repeats a fact already covered elsewhere. |
| `Exam Trap` | `## 4. Exam Traps` and `> Exam trap:` callouts | Capture misconceptions/distinctions not already covered; the answer must state the correct, exam-safe fact. |

## 3b. `context` — where the knowledge is useful

Every card also carries a `context` field (only one of these four):

| context | Meaning |
|---------|---------|
| `Exam` | Primarily tests CCNP/ENCOR-specific facts, commands, values, protocol behavior, terminology, or exam distinctions. |
| `Interview` | Primarily tests conceptual understanding, `why`/`how`, reasoning, troubleshooting logic, or explanations useful in networking interviews. |
| `Practical` | Primarily tests real-world configuration, operation, troubleshooting, or implementation knowledge. |
| `Both` | Genuinely useful for multiple purposes. **Prefer `Both`** when a card naturally serves more than one context. |

- `tag` = what kind of card; `context` = where the knowledge is useful. Different axes — never create a duplicate card just to assign a different `context`.
- The app's context filter: `All` shows everything; `Exam` shows `Exam`/`Both` (and cards with no context); `Interview` shows `Interview`/`Both`; `Practical` shows `Practical`/`Both`.

## 4. Writing rules for cards

- **Question** is phrased like an exam item (short, specific). Use "What is…?",
  "Which…?", "Where does…?", "What happens when…?".
- **Answer** is self-contained (no "as above", "see note"), 1–3 sentences, and
  must be exactly the kind of thing CCNP/ENCOR would test.
- **Keep the specifics**: numbers, sizes (48 bits / 6 bytes), ports (67/68 UDP),
  MAC formats (`0000.0C07.ACxx`), masks, command names.
- If the note has a **Quick Review Table**, mine it for unique facts/tables that
  add recall value; combine or skip rows that repeat existing cards.
- Config/verification commands → one "Core Concept" card (Q: "Command to view the
  MAC address table?" A: `show mac address-table`). Do not dump whole code blocks.
- **Plain text only**: no markdown (`##`, bullet `-`, code fences) and no HTML
  inside `q`/`a`. Unicode is fine: →, ≤, ~, ·, ½.
- **Cover every unique exam-relevant fact, section by section.** Every `##` /
  `###` subsection, table, exam trap, highlighted fact, list, command, and the
  "One-Minute Mental Model" must be represented **at least once** — but repeated
  statements get only ONE good card. A topic is done when no unique exam-relevant
  fact is left uncovered.
- No duplicates within a file, and `q` must never equal `a`.
- Every card needs a `context` (`Exam` / `Interview` / `Practical` / `Both`),
  chosen by where the knowledge is useful — prefer `Both` when in doubt.
- **Section 6 is the authoritative generation prompt** — where it differs from the
  rules above, follow section 6.

## 5. Validate after creating

```bash
# valid JSON check + build the bundle
python3 -c "import json; json.load(open('Level 04 - Ethernet & Switching/01. MAC Address.json'))"
python3 build-decks.py
```

Then double-click `index.html` — the new topic should appear with the right
card count.

---

## 6. Reusable AI prompt (copy-paste)

Paste this before the markdown file when asking an AI to build a deck. You can
paste several `.md` files at once and ask for one JSON per file (see "Batch" note
at the end).

> Create a flashcard JSON deck from the attached CCNP Markdown notes.
>
> IMPORTANT GOAL:
> Create high-quality CCNP/ENCOR study cards that are useful for both certification preparation and networking interviews/practical understanding. Do NOT create a card for every sentence.
>
> Prioritize:
> 1. Retention and active recall
> 2. CCNP/ENCOR exam usefulness
> 3. Networking interview readiness
> 4. Practical networking understanding
> 5. Unique exam-relevant knowledge
> 6. Avoiding redundant cards
>
> FULL COVERAGE means every UNIQUE exam-relevant fact is represented at least once. It does NOT mean repeated facts must become duplicate cards.
>
> FORMAT AND RULES — FOLLOW EXACTLY:
>
> 1. FILES:
>    - Create one JSON object per attached `.md` content file.
>    - Skip `index.md`.
>    - Do not combine multiple Markdown files into one JSON object.
>    - Read the ENTIRE Markdown file before generating its cards.
>
> 2. JSON SCHEMA:
>    Each JSON object must contain exactly these fields:
>
>    - `title`: the Markdown `#` heading
>    - `level`: the integer from frontmatter `level:`
>    - `levelTitle`: the exact folder name, for example `Level 04 - Ethernet & Switching`
>    - `exam`: the value from frontmatter `exam:`
>    - `difficulty`: the value from frontmatter `difficulty:`
>    - `source`: the exact `.md` filename
>    - `cards`: an array of `{ "q", "a", "tag", "context" }`
>
>    If any of these frontmatter fields is absent:
>    - `level`: derive it from the folder number, for example `4` from `Level 04 - Ethernet & Switching`
>    - `exam`: use `ENCOR-350-401`
>    - `difficulty`: use `medium`
>
>    Do not invent any other metadata.
>
> 3. `tag`:
>    The `tag` field may ONLY be one of:
>
>    - `Overview`
>    - `Core Concept`
>    - `Quick Review`
>    - `Exam Trap`
>
>    The `tag` describes WHAT KIND of knowledge the card tests.
>
> 4. `context`:
>    The `context` field may ONLY be one of:
>
>    - `Exam`
>    - `Interview`
>    - `Practical`
>    - `Both`
>
>    Use them as follows:
>
>    - `Exam`: Primarily tests CCNP/ENCOR-specific facts, commands, values,
>      protocol behavior, terminology, or exam distinctions.
>    - `Interview`: Primarily tests conceptual understanding, reasoning,
>      "why/how" knowledge, troubleshooting logic, or explanations useful
>      for networking interviews.
>    - `Practical`: Primarily tests real-world configuration, operation,
>      troubleshooting, or implementation knowledge.
>    - `Both`: Genuinely useful for both CCNP/ENCOR preparation and
>      networking interview/practical understanding.
>
>    Prefer `Both` when a card naturally serves multiple purposes.
>    Do NOT create duplicate cards solely to assign different contexts.
>
>    `tag` and `context` have different purposes:
>    - `tag` = what kind of card it is.
>    - `context` = where the knowledge is useful.
>
> 5. CARD QUALITY:
>    - Do NOT mechanically convert every bullet, sentence, table row, or repeated fact into a card.
>    - Combine closely related facts into one strong card when they form a natural recall unit.
>    - Never create duplicate cards that test essentially the same knowledge.
>    - If a fact already has a good card, do not create another card merely because it appears again in Quick Review, Exam Traps, or the One-Minute Mental Model.
>    - Preserve every UNIQUE exam-relevant fact somewhere in the deck.
>    - Optimize for active recall and long-term retention.
>    - Favor cards that can be answered from memory within a few seconds.
>    - Do not create cards simply to increase the card count.
>
> 6. AVOID OVERLOADED CARDS:
>    - Do not create vague "everything about X" cards.
>    - Prefer focused cards that test one concept or one tightly related recall unit.
>    - Combine multiple facts only when they naturally belong together, such as:
>      a protocol's fields, a command and its purpose, or a compact comparison.
>    - If combining facts makes the answer difficult to recall, split them into separate cards.
>    - Do not combine unrelated facts just to reduce the number of cards.
>
> 7. TARGET CARD COUNT:
>    - Small topic: approximately 10-20 cards.
>    - Normal topic: approximately 20-40 cards.
>    - Large/complex topic: approximately 40-60 cards if genuinely necessary.
>    - Do NOT force a specific number.
>    - Content determines the final count.
>    - Never add cards just to reach a target.
>    - Never remove a unique exam-relevant fact merely to stay within the target.
>
> 8. `Overview` CARDS:
>    - Usually 1-2 cards.
>    - Answer "What is this topic?" and/or "Why does it matter?"
>    - Combine basic introductory facts where appropriate.
>    - Use `context: "Both"` when the concept is useful for exam and interview understanding.
>
> 9. `Core Concept` CARDS:
>    Cover unique:
>    - Definitions
>    - Mechanics
>    - Relationships
>    - Processes
>    - Lists
>    - Formats
>    - Numbers
>    - Protocol behavior
>    - Important commands
>    - Important examples
>    - Troubleshooting concepts
>    - Practical behavior
>
>    Use one card for a coherent concept instead of splitting every sentence into separate cards.
>
> 10. `Quick Review` CARDS:
>     - Capture unique high-value facts from Quick Review/comparison tables.
>     - Do NOT create one card per table row if several rows are already covered by existing cards.
>     - If a table contains information already represented elsewhere, do not duplicate it.
>     - Create a Quick Review card when the table provides a useful independent comparison or compact recall item.
>     - Quick Review cards will usually have `context: "Exam"` or `context: "Both"`.
>
> 11. `Exam Trap` CARDS:
>     - Capture important exam traps and misconceptions.
>     - Do NOT duplicate an existing card merely because the same fact appears in an Exam Trap section.
>     - If the trap contains a unique distinction or misconception, create a card.
>     - The answer MUST state the correct, exam-safe fact clearly.
>     - Prioritize facts likely to distinguish a correct ENCOR answer from a tempting wrong answer.
>     - Exam Trap cards will normally have `context: "Exam"`.
>
> 12. ONE-MINUTE MENTAL MODEL:
>     - Extract the important unique concepts.
>     - Do NOT blindly turn every line into a card.
>     - Usually create 1-3 cards that test the overall mental model if it adds useful recall value.
>     - Do not duplicate concepts already adequately covered.
>     - Prefer `context: "Both"` when the mental model is useful for both exams and interviews.
>
> 13. FULL COVERAGE:
>     Make sure every UNIQUE exam-relevant fact from the entire Markdown file is represented somewhere in the cards, including:
>
>     - Every `##` section
>     - Every `###` section
>     - Definitions
>     - Explanations
>     - Lists
>     - Tables
>     - Commands
>     - Examples
>     - Highlighted facts
>     - Exam notes
>     - Exam traps
>     - Quick Review
>     - One-Minute Mental Model
>
>     However:
>     - Repeated information only needs ONE good card.
>     - Do not create duplicate cards for the same fact.
>     - If a whole section is absent, simply do not create cards for that section.
>     - Do not invent missing information.
>
> 14. QUESTION STYLE:
>     - Questions must be useful for both CCNP/ENCOR exam preparation and networking interviews.
>     - Prioritize CCNP/ENCOR exam-oriented knowledge and terminology.
>     - Prefer realistic exam-style questions for facts, commands, numbers,
>       protocol behavior, and important distinctions.
>     - Use practical or scenario-based questions when they improve understanding
>       or interview readiness.
>     - Prefer "why", "how", and "what happens when" questions for concepts and mechanics.
>     - Prefer direct recall questions for commands, values, formats, timers,
>       bit sizes, protocol identifiers, and other facts that must be memorized.
>     - Test one concept or one tightly related group of concepts per card.
>     - Preserve exact terminology from the source.
>     - Do not make questions unnecessarily complicated.
>
> 15. ANSWER STYLE:
>     - Self-contained.
>     - Normally 1-3 sentences.
>     - If a complete list, command sequence, comparison, or other source-specific
>       set of facts cannot fit naturally into 3 sentences, prioritize completeness
>       over the sentence limit.
>     - Concise but complete.
>     - Include all important specifics from the source.
>     - Preserve exact bit sizes, byte sizes, port numbers, timers, MAC formats,
>       protocol names, command names, values, and other exam-relevant details.
>     - If the answer is a list, include EVERY item from the source when those items
>       are part of the knowledge being tested.
>     - Never use an answer that requires the user to look back at the question
>       to understand it.
>     - No empty answers.
>     - `q` must never equal `a`.
>
> 16. SOURCE FIDELITY:
>     - Base the cards on the attached Markdown notes.
>     - Preserve the source's terminology, organization, facts, framing, and intended exam level.
>     - Do not silently introduce outside facts that are not supported by the Markdown.
>     - Do not correct, replace, reconcile, or expand source content using general
>       networking knowledge unless explicitly asked.
>     - If a source statement appears wrong or unusual, reproduce it as written.
>     - If something is ambiguous or unsupported by the source, do not invent an answer.
>     - The Markdown source is the authority for what should be included.
>
> 17. PLAIN TEXT:
>     - `q` and `a` must contain plain text only.
>     - No Markdown.
>     - No HTML.
>     - No code fences.
>     - Unicode is allowed.
>     - Commands such as `show mac address-table` may appear as plain text.
>     - Do not use Markdown formatting such as bold, backticks, bullets, or headings inside `q` or `a`.
>
> 18. JSON VALIDITY:
>     - Output must be valid JSON.
>     - Use double quotes for JSON strings.
>     - Escape quotes and special characters correctly.
>     - No trailing commas.
>     - No comments.
>     - Do not wrap the JSON in Markdown code fences.
>     - Do not include any text outside the JSON object.
>
> 19. FILE NAMING:
>     For each source file:
>     - Replace `.md` with `.json`.
>     - Keep the filename otherwise exactly unchanged.
>
>     Example:
>     `01. MAC Address.md` -> `01. MAC Address.json`
>
> 20. OUTPUT:
>     - Output valid JSON only.
>     - No explanation.
>     - No commentary.
>     - No headings.
>     - No Markdown fences.
>     - No additional fields.
>     - No text before or after the JSON.
>
> FINAL QUALITY CHECK BEFORE OUTPUT:
>
> - Did you read the entire Markdown file?
> - Is every UNIQUE exam-relevant fact represented?
> - Did you remove duplicate/redundant cards?
> - Are repeated Quick Review facts already covered instead of duplicated?
> - Are repeated Exam Trap facts already covered instead of duplicated?
> - Did you cover every relevant section, list, table, command, example, and highlighted fact?
> - Are commands, numbers, formats, protocol behavior, and important distinctions preserved?
> - Are cards focused enough for active recall?
> - Are any cards overloaded with unrelated information?
> - Is the card count reasonable for the amount of unique content?
> - Are the questions useful for both CCNP/ENCOR and networking interviews where appropriate?
> - Is the `context` classification accurate?
> - Is every `q` different from its `a`?
> - Are all answers self-contained?
> - Is every tag one of the four allowed values?
> - Is every context one of the four allowed values?
> - Does every card contain exactly `q`, `a`, `tag`, and `context`?
> - Does every JSON object contain exactly the required top-level fields?
> - Is the output valid JSON only?

**Batch mode** — to speed up large-scale creation, paste the prompt once and attach
several `.md` files from the *same* level. Ask for one JSON file per attached note
(all from that level, so `levelTitle` is identical). Review the output with
`python3 build-decks.py`, which reports the level/topic/card totals, and spot-check
a few decks in `index.html`.

---

# Appendix: Vault structure & study tips

## Map of Content (MOC)

A top-level study planner lives at `00. MOC - CCNP Study Map.md`. It links all 31
level `index.md` notes, a recommended study order, an ENCOR exam-weight table, and
cross-cutting themes. Open it in Obsidian to navigate the vault from one place.

## `difficulty` values

Each deck's `difficulty` is now meaningful (`easy` / `medium` / `hard`) rather than a
uniform default. The flashcard app doesn't currently expose a difficulty filter, but
the value is stored per deck so you can use it in Dataview queries or future features.

## Cross-level topic overlap (intentional)

The same topic legitimately appears at more than one level because each level has a
different angle. Cards are **not** deduplicated across levels — that's by design, so
you see the theory, the troubleshooting, and the lab version of a concept separately:

| Concept | Theory level | Other levels |
|---|---|---|
| STP | `Level 08` | `Level 29` (Troubleshooting), `Level 01` (as a cable type) |
| OSPF | `Level 10` | `Level 29` (Troubleshooting), `Level 30` (Labs) |
| EIGRP | `Level 11` | `Level 29` (Troubleshooting) |
| BGP | `Level 12` | `Level 29`, `Level 30` |
| NAT | `Level 15` | `Level 29` (Troubleshooting) |
| DHCP/DNS/SNMP/Syslog | `Level 16` | `Level 29`, `Level 26` |
| VPN (IPsec/DMVPN) | `Level 18` | `Level 30` (Labs) |
| SD-WAN | `Level 23` | `Level 29`, `Level 30` |
| VRF | `Level 20` (MPLS) | `Level 25` (Cloud) |
| Multicast | `Level 05`/`Level 06` | `Level 19` |
| Gateway redundancy | `Level 14` (FHRP) | `Level 27` (HA) |

When studying a specific topic, review its cards in all related levels for full
coverage (theory → troubleshooting → hands-on lab).