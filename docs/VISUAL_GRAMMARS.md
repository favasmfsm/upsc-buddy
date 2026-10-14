# Visual Grammars

UPSC Buddy teaches with a **visual language**: pick the grammar that fits the idea. Do not force every topic into one mind-map.

**Authoring rule:** per concept use **1 primary + ≤2 support** grammars. The concept `visual-grammar-catalog` demos every template.

**Page IA (when content exists):** Mental model → Overview → Drill-down → Cases → Amendments → PYQs → Related.

Decision trees and restriction trees both use `flowchart` (branching via `options`).

---

## 1. Mental model — `mental_model`

**When:** First intuition before Articles (shield, map metaphor, etc.).

```json
{
  "id": "mm-1",
  "type": "mental_model",
  "title": "Mental model",
  "metaphor": "Shield",
  "topic_label": "Fundamental Rights",
  "subject_label": "Citizen",
  "relation_label": "Protects you from",
  "protects_from": ["State abuse", "Discrimination"],
  "insight": "Short takeaway sentence."
}
```

`topic_label` is the large heading under the metaphor. `relation_label` defaults to “Protects you from” when omitted.

## 2. Hierarchy / constitution map — `tree`

**When:** Show where a topic sits in a larger structure.

```json
{
  "id": "tree-1",
  "type": "tree",
  "title": "Where FR sits",
  "root": {
    "id": "constitution",
    "label": "Constitution",
    "children": [
      {
        "id": "fr",
        "label": "Fundamental Rights",
        "slug": "fundamental-rights",
        "detail": "Part III",
        "children": [
          { "id": "eq", "label": "Equality", "slug": "fr-equality-14-18" }
        ]
      },
      { "id": "dpsp", "label": "DPSP", "slug": "directive-principles" }
    ]
  }
}
```

## 3. Pillars — `pillars`

**When:** Parallel categories students must scan and open.

```json
{
  "id": "pillars-1",
  "type": "pillars",
  "title": "Six pillars",
  "items": [
    {
      "id": "eq",
      "articles": "Arts 14–18",
      "label": "Equality",
      "slug": "fr-equality-14-18",
      "detail": "...",
      "tone": "teal"
    }
  ]
}
```

## 4. Timeline — `timeline`

**When:** Evolution, amendments, historical sequence.

```json
{
  "id": "tl-1",
  "type": "timeline",
  "title": "Right to Property",
  "events": [
    { "id": "e1", "year": 1950, "label": "FR (property)", "detail": "..." },
    { "id": "e2", "year": 1978, "label": "44th Amendment", "detail": "..." }
  ]
}
```

## 5. Relationship graph — `relation_graph`

**When:** Show concept edges (parent/related). Fetches live graph API.

```json
{
  "id": "rg-1",
  "type": "relation_graph",
  "title": "Concept relations",
  "root_slug": "fundamental-rights",
  "depth": 2
}
```

Also available as full page: `/concepts/[slug]/graph`.

## 6. Decision tree — `flowchart` (branching)

**When:** “Which Article / path applies?”

Use `root` + `steps[].options[{ label, next }]`.

## 7. Citizen journey — `journey`

**When:** Real-life story path (not a decision fork).

```json
{
  "id": "j-1",
  "type": "journey",
  "title": "Government job",
  "stages": [
    { "id": "s1", "label": "Citizen", "detail": "..." },
    { "id": "s2", "label": "Article 16", "slug": "fr-equality-14-18", "detail": "..." }
  ]
}
```

## 8. Compare view — `comparison`

**When:** Side-by-side contrasts (FR vs DPSP, Money Bill vs Finance Bill).

## 9. Restriction visualization — `flowchart` (branching)

Same type as #6; title content as restriction grounds (e.g. Art. 19(2)).

## 10. PYQ heatmap — `pyq_heatmap`

**When:** Relative exam frequency. Counts filled live from PYQ↔concept links.

```json
{
  "id": "heat-1",
  "type": "pyq_heatmap",
  "title": "PYQ focus",
  "items": [{ "concept_slug": "fr-equality-14-18", "label": "Equality" }]
}
```

## 11. Article explorer — `article_explorer`

**When:** Drill Article → topic → exceptions → cases → PYQs → CA (authored stages).

```json
{
  "id": "ae-1",
  "type": "article_explorer",
  "title": "Article 19",
  "article_ref": "Article 19",
  "stages": [
    { "id": "topic", "label": "Freedom of Speech", "detail": "..." },
    { "id": "ex", "label": "Exceptions", "detail": "..." }
  ]
}
```

## 12. Court cases network — `case_network`

**When:** Cases radiating from an Article/hub.

```json
{
  "id": "cn-1",
  "type": "case_network",
  "title": "Art. 21 cases",
  "hub_label": "Article 21",
  "cases": [
    { "id": "mg", "label": "Maneka Gandhi", "year": 1978, "detail": "...", "case_slug": "maneka-gandhi" }
  ]
}
```

## 13. Memory palace — `memory_palace`

**When:** Place-based recall (courtroom loci, not 3D).

```json
{
  "id": "mp-1",
  "type": "memory_palace",
  "title": "Courtroom",
  "setting": "Supreme Court courtroom",
  "loci": [
    { "id": "l1", "place": "Judge's bench", "association": "Article 32", "detail": "..." }
  ]
}
```

## 14. What-if simulator — `simulator`

**When:** Interactive scenario (state machine). No scoring backend.

```json
{
  "id": "sim-1",
  "type": "simulator",
  "title": "Newspaper ban",
  "start": "q1",
  "nodes": {
    "q1": {
      "prompt": "Which right?",
      "choices": [{ "label": "Art. 19", "next": "end" }]
    },
    "end": { "prompt": "Done.", "choices": [] }
  }
}
```

---

## 15. Image — `image`

**When:** Show a real diagram / map / photo (geography maps, physical processes). Self-host assets under `frontend/public/` and reference by path.

```json
{
  "id": "img-1",
  "type": "image",
  "title": "Three types of plate boundaries",
  "src": "/geo/geomorphology/plate-boundaries.png",
  "alt": "Divergent, convergent, and transform plate boundaries",
  "caption": "Convergent → mountains/trenches; divergent → ridges; transform → faults.",
  "source": "Wikimedia Commons (public domain)"
}
```

## 16. Annotated image — `annotated_image`

**When:** "Label the diagram" recall — an image with numbered markers the student can hover/click. `x`/`y` are percentages (0–100) of image width/height.

```json
{
  "id": "aimg-1",
  "type": "annotated_image",
  "title": "Internal structure of the Earth",
  "src": "/geo/geomorphology/earth-interior.png",
  "alt": "Cross-section of Earth's layers",
  "markers": [
    { "id": "crust", "x": 82, "y": 20, "label": "Crust", "detail": "Thin outer layer (5–70 km)." },
    { "id": "mantle", "x": 65, "y": 45, "label": "Mantle", "detail": "Silicate rock; asthenosphere below lithosphere." },
    { "id": "core", "x": 50, "y": 50, "label": "Core", "detail": "Outer (liquid) + inner (solid) — Fe/Ni." }
  ],
  "caption": "Hover a marker to reveal the layer.",
  "source": "Wikimedia Commons (CC BY-SA)"
}
```

---

## Utility types

| Type | Role |
|------|------|
| `map` | Chip cluster + textual edges |
| `image` | Self-hosted diagram / map / photo with caption + attribution |
| `annotated_image` | Image with numbered hover/click markers for label-recall |
| `callout` | Tip / trap / note |
| `markdown` | Prose inside the visual column |
