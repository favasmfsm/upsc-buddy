"""Seed Laxmikanth Ch.10 Fundamental Duties (visual revision chapter)."""

from django.core.management.base import BaseCommand

from concepts.models import (
    CaseLaw,
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "fundamental-duties"
CHAPTER_SLUG = "fundamental-duties"

THEME_PILLARS = [
    {
        "id": "origin",
        "articles": "1976 · 42nd",
        "label": "Origin & Swaran Singh",
        "slug": "fd-origin",
        "detail": "Emergency-era push; Committee 8 → Constitution 10; three rejected ideas.",
        "tone": "teal",
    },
    {
        "id": "list",
        "articles": "Art. 51A",
        "label": "Eleven Duties",
        "slug": "fd-list",
        "detail": "Scan (a)–(k); 86th added the education duty.",
        "tone": "olive",
    },
    {
        "id": "features",
        "articles": "Part IVA",
        "label": "Features",
        "slug": "fd-features",
        "detail": "Citizens only; moral + civic; non-justiciable like DPSP.",
        "tone": "gold",
    },
    {
        "id": "criticism",
        "articles": "Critics",
        "label": "Criticism",
        "slug": "fd-criticism",
        "detail": "Not exhaustive; vague; moral code; superfluous; Part-IV appendage.",
        "tone": "orange",
    },
    {
        "id": "significance",
        "articles": "Why it matters",
        "label": "Significance",
        "slug": "fd-significance",
        "detail": "Reminder, warning, inspiration; courts use FD to read laws.",
        "tone": "terracotta",
    },
    {
        "id": "verma",
        "articles": "1999",
        "label": "Verma Committee",
        "slug": "fd-verma",
        "detail": "Existing statutes already back some duties.",
        "tone": "maroon",
    },
    {
        "id": "triangle",
        "articles": "III · IV · IVA",
        "label": "FR–DPSP–FD Triangle",
        "slug": "fd-triangle",
        "detail": "Rights, principles, duties — one constitutional thread.",
        "tone": "teal",
    },
]

DUTY_PILLARS = [
    {
        "id": "d1",
        "articles": "51A(a)",
        "label": "Abide by Constitution",
        "slug": "fd-list",
        "detail": "Respect ideals, institutions, National Flag and National Anthem.",
        "tone": "teal",
    },
    {
        "id": "d2",
        "articles": "51A(b)",
        "label": "Freedom Struggle Ideals",
        "slug": "fd-list",
        "detail": "Cherish and follow the noble ideals of the national struggle.",
        "tone": "olive",
    },
    {
        "id": "d3",
        "articles": "51A(c)",
        "label": "Sovereignty & Unity",
        "slug": "fd-list",
        "detail": "Uphold and protect sovereignty, unity and integrity of India.",
        "tone": "gold",
    },
    {
        "id": "d4",
        "articles": "51A(d)",
        "label": "Defend the Country",
        "slug": "fd-list",
        "detail": "Defend India and render national service when called upon.",
        "tone": "orange",
    },
    {
        "id": "d5",
        "articles": "51A(e)",
        "label": "Harmony & Brotherhood",
        "slug": "fd-list",
        "detail": "Promote harmony; renounce practices derogatory to dignity of women.",
        "tone": "terracotta",
    },
    {
        "id": "d6",
        "articles": "51A(f)",
        "label": "Composite Culture",
        "slug": "fd-list",
        "detail": "Value and preserve the rich heritage of composite culture.",
        "tone": "maroon",
    },
    {
        "id": "d7",
        "articles": "51A(g)",
        "label": "Environment",
        "slug": "fd-list",
        "detail": "Protect forests, lakes, rivers, wildlife; compassion for living creatures.",
        "tone": "teal",
    },
    {
        "id": "d8",
        "articles": "51A(h)",
        "label": "Scientific Temper",
        "slug": "fd-list",
        "detail": "Develop scientific temper, humanism, spirit of inquiry and reform.",
        "tone": "olive",
    },
    {
        "id": "d9",
        "articles": "51A(i)",
        "label": "Public Property",
        "slug": "fd-list",
        "detail": "Safeguard public property and abjure violence.",
        "tone": "gold",
    },
    {
        "id": "d10",
        "articles": "51A(j)",
        "label": "Strive for Excellence",
        "slug": "fd-list",
        "detail": "Excellence in individual and collective activity for national rise.",
        "tone": "orange",
    },
    {
        "id": "d11",
        "articles": "51A(k) · 86th",
        "label": "Educate Child / Ward",
        "slug": "fd-list",
        "detail": "Opportunities for education to child/ward aged 6–14 (added 2002).",
        "tone": "terracotta",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "fd-civic-checklist",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Civic checklist",
        "topic_label": "Fundamental Duties",
        "subject_label": "Citizen",
        "relation_label": "Balances with",
        "protects_from": [
            "Treating FD as justiciable like FR",
            "Applying FD to foreigners",
            "Confusing 8 Committee duties with 10/11 in the text",
            "Assuming ‘non-justiciable’ means ‘no law can enforce’",
        ],
        "insight": (
            "Part IVA is a citizen checklist beside Part III rights — "
            "Art. 51A duties are non-justiciable, but Parliament can still legislate penalties."
        ),
    },
    {
        "id": "fd-theme-pillars",
        "type": "pillars",
        "title": "Seven revision themes",
        "items": THEME_PILLARS,
    },
    {
        "id": "fd-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Lock Part IVA · Art. 51A · citizens only · 42nd (10) + 86th (11th) → "
            "then scan duties and Verma statutes. "
            "This is a visual revision layer — not a substitute for Laxmikanth."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Origin & Swaran Singh",
        "slug": "fd-origin",
        "sort_order": 1,
        "summary": (
            "Original Constitution had no citizen duties; 42nd added Part IVA after "
            "Swaran Singh Committee (Emergency era)."
        ),
        "body": (
            "## Origin\n\n"
            "Framers put **State duties** in DPSP, not citizen duties. "
            "FD entered in **1976** (felt necessary during Internal Emergency 1975–77).\n\n"
            "Inspired by the **erstwhile USSR**. Among major democracies, "
            "**Japan** is the notable one with a citizen-duties list.\n\n"
            "### Swaran Singh Committee (1976)\n"
            "- Recommended a separate chapter on Fundamental Duties.\n"
            "- Suggested **eight** duties; **42nd Amendment** enacted **ten**.\n"
            "- Congress called non-inclusion of FD a ‘historical mistake’.\n\n"
            "### Rejected recommendations (high-yield)\n"
            "1. Parliament may impose **penalty/punishment** for non-compliance.\n"
            "2. Such penalty laws **barred from challenge** on FR / constitutional grounds.\n"
            "3. **Duty to pay taxes** as a Fundamental Duty.\n\n"
            "Janata Government later rolled back many 42nd changes (43rd/44th) but "
            "**kept Fundamental Duties** — eventual consensus; 86th added one more in 2002."
        ),
        "articles": [
            (
                "Article 51A",
                "Part IVA — code of Fundamental Duties; inserted by 42nd Amendment, 1976.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fd-origin-timeline",
                "type": "timeline",
                "title": "How Fundamental Duties entered",
                "events": [
                    {
                        "id": "e1950",
                        "year": 1950,
                        "label": "No citizen duties",
                        "detail": "Original text: FR + DPSP; no Fundamental Duties chapter.",
                    },
                    {
                        "id": "e1975",
                        "year": 1975,
                        "label": "Internal Emergency",
                        "detail": "Need for citizen duties felt during Emergency (1975–77).",
                    },
                    {
                        "id": "e1976",
                        "year": 1976,
                        "label": "42nd Amendment",
                        "detail": "Part IVA / Art. 51A — ten duties (Committee had suggested eight).",
                    },
                    {
                        "id": "e2002",
                        "year": 2002,
                        "label": "86th Amendment",
                        "detail": "Eleventh duty — education for child/ward aged 6–14.",
                    },
                ],
            },
            {
                "id": "fd-origin-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Committee recommended **8**; Constitution got **10** (1976), then **11** (2002). "
                    "Duty to pay taxes was recommended — **not** included."
                ),
            },
        ],
    },
    {
        "title": "Eleven Duties",
        "slug": "fd-list",
        "sort_order": 2,
        "summary": "Article 51A(a)–(k) — ten from 42nd; education duty (k) from 86th Amendment.",
        "body": (
            "## List under Article 51A\n\n"
            "It shall be the duty of every citizen of India:\n\n"
            "1. Abide by the Constitution; respect ideals, institutions, Flag, Anthem.\n"
            "2. Cherish noble ideals of the freedom struggle.\n"
            "3. Uphold sovereignty, unity and integrity of India.\n"
            "4. Defend the country; render national service when called upon.\n"
            "5. Promote harmony and brotherhood; renounce practices derogatory to dignity of women.\n"
            "6. Value and preserve composite culture.\n"
            "7. Protect and improve natural environment; compassion for living creatures.\n"
            "8. Develop scientific temper, humanism, spirit of inquiry and reform.\n"
            "9. Safeguard public property; abjure violence.\n"
            "10. Strive towards excellence in all spheres.\n"
            "11. Provide opportunities for education to child/ward **aged 6–14** "
            "(**86th Amendment, 2002**).\n\n"
            "### Memory groups\n"
            "- **Allegiance & defence** — (a)–(d)\n"
            "- **Society & culture** — (e)–(f)\n"
            "- **Mind & nature** — (g)–(h)\n"
            "- **Civic excellence & education** — (i)–(k)"
        ),
        "articles": [
            (
                "Article 51A(a)–(j)",
                "Ten Fundamental Duties inserted by the 42nd Amendment, 1976.",
            ),
            (
                "Article 51A(k)",
                "Duty to provide education to child/ward between 6 and 14 — 86th Amendment, 2002.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fd-eleven-pillars",
                "type": "pillars",
                "title": "Eleven duties at a glance",
                "items": DUTY_PILLARS,
            },
            {
                "id": "fd-list-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Only **(k)** is the 86th add-on. Pair with Art. 21A (RTE) — "
                    "same 6–14 age band, different Parts."
                ),
            },
        ],
    },
    {
        "title": "Features of Fundamental Duties",
        "slug": "fd-features",
        "sort_order": 3,
        "summary": "Moral + civic; Indian tradition codified; citizens only; non-justiciable like DPSP.",
        "body": (
            "## Features\n\n"
            "1. **Moral and civic** — e.g. cherishing freedom-struggle ideals (moral) vs "
            "respecting Constitution/Flag/Anthem (civic).\n"
            "2. **Codified Indian values** — tradition, mythology, religion, practices "
            "already part of Indian life.\n"
            "3. **Citizens only** — unlike some FRs that extend to all persons "
            "(e.g. Arts 14, 20, 21, 21A, 22–28).\n"
            "4. **Non-justiciable** — like DPSP; no direct court enforcement; "
            "no automatic legal sanction. **Parliament may enforce by legislation.**"
        ),
        "articles": [
            (
                "Article 51A",
                "Duties confined to citizens; Constitution does not provide direct judicial enforcement.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fd-features-compare",
                "type": "comparison",
                "title": "FD vs FR (quick contrast)",
                "columns": [
                    {
                        "id": "fd",
                        "heading": "Fundamental Duties",
                        "points": [
                            "Part IVA · Art. 51A",
                            "Citizens only",
                            "Non-justiciable",
                            "Parliament may legislate enforcement",
                            "Moral + civic mix",
                        ],
                    },
                    {
                        "id": "fr",
                        "heading": "Fundamental Rights",
                        "points": [
                            "Part III · Arts 12–35",
                            "Some for all persons; some citizens-only",
                            "Justiciable (Art. 32 / 226)",
                            "Direct court remedies",
                            "Limitations / reasonable restrictions apply",
                        ],
                    },
                ],
            },
            {
                "id": "fd-features-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Non-justiciable ≠ unenforceable forever. "
                    "Parliament is free to attach penalty by ordinary law "
                    "(Swaran Singh wanted this in the Constitution itself — rejected)."
                ),
            },
        ],
    },
    {
        "title": "Criticism",
        "slug": "fd-criticism",
        "sort_order": 4,
        "summary": "Five stock critiques — incomplete list, vague phrases, moral code, superfluous, weak placement.",
        "body": (
            "## Criticism\n\n"
            "1. **Not exhaustive** — omits voting, paying taxes, family planning, etc. "
            "(tax duty was a Swaran Singh suggestion).\n"
            "2. **Vague phrases** — ‘noble ideals’, ‘composite culture’, ‘scientific temper’ "
            "invite many readings.\n"
            "3. **Moral precepts** — non-justiciable character; Committee had wanted penalties.\n"
            "4. **Superfluous** — critics said citizens would do these anyway without a chapter.\n"
            "5. **Weak placement** — appendage to Part IV reduces stature; "
            "critics preferred placement after Part III (on par with FR)."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "fd-criticism-pillars",
                "type": "pillars",
                "title": "Five criticisms",
                "items": [
                    {
                        "id": "c1",
                        "articles": "Gap",
                        "label": "Not exhaustive",
                        "slug": "fd-criticism",
                        "detail": "No tax / vote / family-planning duty in the list.",
                        "tone": "teal",
                    },
                    {
                        "id": "c2",
                        "articles": "Wording",
                        "label": "Vague",
                        "slug": "fd-criticism",
                        "detail": "Noble ideals, composite culture, scientific temper.",
                        "tone": "olive",
                    },
                    {
                        "id": "c3",
                        "articles": "Force",
                        "label": "Moral code",
                        "slug": "fd-criticism",
                        "detail": "Non-justiciable; no automatic sanction.",
                        "tone": "gold",
                    },
                    {
                        "id": "c4",
                        "articles": "Need",
                        "label": "Superfluous",
                        "slug": "fd-criticism",
                        "detail": "Would be followed even if not written.",
                        "tone": "orange",
                    },
                    {
                        "id": "c5",
                        "articles": "Place",
                        "label": "Part-IV appendage",
                        "slug": "fd-criticism",
                        "detail": "Should have sat after Part III with FR.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "fd-criticism-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Pair with significance: critics called FD superfluous; "
                    "Janata still retained them after Emergency rollbacks."
                ),
            },
        ],
    },
    {
        "title": "Significance",
        "slug": "fd-significance",
        "sort_order": 5,
        "summary": "Reminder, warning, inspiration; aid to constitutional interpretation; enforceable via statute.",
        "body": (
            "## Significance\n\n"
            "1. **Reminder** — rights come with duties to country, society, fellow citizens.\n"
            "2. **Warning** — against anti-national / anti-social acts (e.g. burning flag, "
            "destroying public property).\n"
            "3. **Inspiration** — discipline and active participation in national goals.\n"
            "4. **Interpretation aid** — courts may use Art. 51A when testing validity / "
            "reading ambiguous laws "
            "(*Mohan Kumar Singhania*, 1991; *Ramlila Maidan Incident*, 2012).\n"
            "5. **Enforceable by law** — Parliament can prescribe penalty for failure.\n\n"
            "Indira Gandhi framed FD as democratic balance — duties consciousness "
            "alongside rights consciousness. Opposition opposed inclusion; "
            "post-Emergency Janata did **not** repeal FD."
        ),
        "articles": [
            (
                "Article 51A",
                "Used by courts as an interpretive aid; Parliament may enforce by legislation.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "fd-significance-pillars",
                "type": "pillars",
                "title": "Five significance hooks",
                "items": [
                    {
                        "id": "s1",
                        "articles": "1",
                        "label": "Reminder",
                        "slug": "fd-significance",
                        "detail": "Enjoy rights → remember duties.",
                        "tone": "teal",
                    },
                    {
                        "id": "s2",
                        "articles": "2",
                        "label": "Warning",
                        "slug": "fd-significance",
                        "detail": "Against anti-national / anti-social acts.",
                        "tone": "olive",
                    },
                    {
                        "id": "s3",
                        "articles": "3",
                        "label": "Inspiration",
                        "slug": "fd-significance",
                        "detail": "Discipline; active citizens, not spectators.",
                        "tone": "gold",
                    },
                    {
                        "id": "s4",
                        "articles": "Courts",
                        "label": "Interpretation",
                        "slug": "fd-significance",
                        "detail": "Singhania / Ramlila — FD guides reading of laws.",
                        "tone": "orange",
                    },
                    {
                        "id": "s5",
                        "articles": "Statute",
                        "label": "Legislative teeth",
                        "slug": "fd-significance",
                        "detail": "Parliament may attach penalty by law.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "fd-significance-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "FD survived 43rd/44th rollbacks — signal of consensus. "
                    "86th (2002) later expanded the list."
                ),
            },
        ],
    },
    {
        "title": "Verma Committee",
        "slug": "fd-verma",
        "sort_order": 6,
        "summary": "1999 Verma Committee mapped existing laws that already implement some duties.",
        "body": (
            "## Verma Committee on Fundamental Duties (1999)\n\n"
            "Identified legal provisions already available for implementing some duties:\n\n"
            "1. **Prevention of Insults to National Honour Act, 1971** — "
            "Constitution, Flag, Anthem.\n"
            "2. **Criminal laws** — enmity between sections (language, race, birth, religion).\n"
            "3. **Protection of Civil Rights Act, 1955** — caste/religion offences "
            "(earlier Untouchability Offences Act till 1976).\n"
            "4. **IPC** — imputations prejudicial to national integration.\n"
            "5. **Unlawful Activities (Prevention) Act, 1967** — communal organisation "
            "as unlawful association.\n"
            "6. **Representation of the People Act, 1951** — disqualification for "
            "corrupt practices (religion-based soliciting / promoting enmity).\n"
            "7. **Wildlife (Protection) Act, 1972** — trade in rare/endangered species.\n"
            "8. **Forest (Conservation) Act, 1980** — deforestation / diversion of forest land."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "fd-verma-pillars",
                "type": "pillars",
                "title": "Eight legal backstops",
                "items": [
                    {
                        "id": "v1",
                        "articles": "1971",
                        "label": "National Honour Act",
                        "slug": "fd-verma",
                        "detail": "Insults to Constitution, Flag, Anthem.",
                        "tone": "teal",
                    },
                    {
                        "id": "v2",
                        "articles": "IPC+",
                        "label": "Criminal laws",
                        "slug": "fd-verma",
                        "detail": "Enmity between sections of people.",
                        "tone": "olive",
                    },
                    {
                        "id": "v3",
                        "articles": "1955",
                        "label": "PCRA",
                        "slug": "fd-verma",
                        "detail": "Caste/religion related offences.",
                        "tone": "gold",
                    },
                    {
                        "id": "v4",
                        "articles": "IPC",
                        "label": "National integration",
                        "slug": "fd-verma",
                        "detail": "Prejudicial imputations / assertions.",
                        "tone": "orange",
                    },
                    {
                        "id": "v5",
                        "articles": "1967",
                        "label": "UAPA",
                        "slug": "fd-verma",
                        "detail": "Communal org → unlawful association.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "v6",
                        "articles": "1951",
                        "label": "RPA",
                        "slug": "fd-verma",
                        "detail": "Disqualification for religion-based corrupt practice.",
                        "tone": "maroon",
                    },
                    {
                        "id": "v7",
                        "articles": "1972",
                        "label": "Wildlife Act",
                        "slug": "fd-verma",
                        "detail": "Trade in rare / endangered species.",
                        "tone": "teal",
                    },
                    {
                        "id": "v8",
                        "articles": "1980",
                        "label": "Forest Act",
                        "slug": "fd-verma",
                        "detail": "Checks deforestation / diversion.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "fd-verma-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims anchor",
                "body": (
                    "Verma = **existing statutes**, not new constitutional force. "
                    "Pair Flag/Anthem duty with Prevention of Insults Act (1971)."
                ),
            },
        ],
    },
    {
        "title": "FR–DPSP–FD Triangle",
        "slug": "fd-triangle",
        "sort_order": 7,
        "summary": "Parts III, IV and IVA form one thread — rights, governance principles, citizen duties.",
        "body": (
            "## Constitutional triangle\n\n"
            "In *Ramlila Maidan Incident* (2012), the Court noted a **common thread** "
            "through Parts III, IV and IVA:\n\n"
            "- **Part III** — Fundamental Rights (justiciable).\n"
            "- **Part IV** — Directive Principles (non-justiciable State duties).\n"
            "- **Part IVA** — Fundamental Duties (non-justiciable citizen duties).\n\n"
            "When interpreting any one, weigh impact on the other two.\n\n"
            "| | Who is bound | Justiciable? |\n"
            "|---|---|---|\n"
            "| FR | State (mainly) | Yes |\n"
            "| DPSP | State | No |\n"
            "| FD | Citizens | No (unless statute) |"
        ),
        "articles": [
            ("Part III", "Fundamental Rights — justiciable guarantees."),
            ("Part IV", "Directive Principles — non-justiciable State guidelines."),
            ("Part IVA", "Fundamental Duties — non-justiciable citizen duties."),
        ],
        "visual_blocks": [
            {
                "id": "fd-triangle-compare",
                "type": "comparison",
                "title": "Three Parts, one thread",
                "columns": [
                    {
                        "id": "fr",
                        "heading": "Part III · FR",
                        "points": [
                            "Citizen / person rights",
                            "Justiciable (Art. 32 / 226)",
                            "Limits State power",
                        ],
                    },
                    {
                        "id": "dpsp",
                        "heading": "Part IV · DPSP",
                        "points": [
                            "Duties of the State",
                            "Non-justiciable",
                            "Socio-economic democracy goals",
                        ],
                    },
                    {
                        "id": "fd",
                        "heading": "Part IVA · FD",
                        "points": [
                            "Duties of citizens",
                            "Non-justiciable",
                            "Balance beside rights",
                        ],
                    },
                ],
            },
            {
                "id": "fd-triangle-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision trio",
                "body": (
                    "FR justiciable · DPSP non-justiciable · FD non-justiciable — "
                    "but FD still matter for interpretation and statute-backed enforcement."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "fd-origin"),
    (HUB_SLUG, "parent", "fd-list"),
    (HUB_SLUG, "parent", "fd-features"),
    (HUB_SLUG, "parent", "fd-criticism"),
    (HUB_SLUG, "parent", "fd-significance"),
    (HUB_SLUG, "parent", "fd-verma"),
    (HUB_SLUG, "parent", "fd-triangle"),
    (HUB_SLUG, "related", "sf-fundamental-duties"),
    (HUB_SLUG, "related", "fundamental-rights"),
    (HUB_SLUG, "related", "directive-principles"),
    ("fd-origin", "related", "fd-list"),
    ("fd-features", "related", "fd-triangle"),
    ("fd-features", "related", "fundamental-rights"),
    ("fd-significance", "related", "fd-criticism"),
    ("fd-significance", "related", "fd-triangle"),
    ("fd-list", "related", "fd-verma"),
    ("fd-triangle", "related", "fundamental-rights"),
    ("fd-triangle", "related", "directive-principles"),
    ("fd-triangle", "related", "sf-dpsp"),
]

SAMPLE_PYQS = [
    (
        2017,
        "Which of the following is/are among the Fundamental Duties of citizens laid down "
        "in the Indian Constitution? "
        "1. To preserve the rich heritage of our composite culture "
        "2. To protect the weaker sections from social injustice "
        "3. To develop the scientific temper and spirit of inquiry "
        "4. To strive towards excellence in all spheres of individual and collective activity",
        "1, 3 and 4 are Art. 51A duties. Protecting weaker sections from social injustice "
        "is a DPSP theme (Art. 46), not an FD.",
        ["fd-list", "fd-triangle"],
    ),
    (
        2015,
        "Consider the following statements regarding Fundamental Duties: "
        "1. They are confined to citizens only. "
        "2. They are justiciable. "
        "Which of the statements is/are correct?",
        "Only 1. FD are non-justiciable (like DPSP); Parliament may still enforce by law.",
        ["fd-features"],
    ),
    (
        2012,
        "According to the Constitution of India, which of the following are fundamental "
        "for the governance of the country? / related FD–DPSP contrast themes.",
        "DPSP are fundamental in governance of the country (Art. 37). "
        "FD are citizen duties under Art. 51A — do not confuse the two phrases.",
        ["fd-triangle", "fd-features"],
    ),
    (
        2011,
        "Under the Constitution of India, which one of the following is not a Fundamental Duty?",
        "Classic trap: duty to pay taxes / cast vote often appear as distractors — "
        "not in Art. 51A (tax was a rejected Swaran Singh idea).",
        ["fd-list", "fd-origin", "fd-criticism"],
    ),
    (
        2002,
        "The 86th Constitutional Amendment is related to which Fundamental Duty?",
        "Added Art. 51A(k) — provide opportunities for education to child/ward aged 6–14 "
        "(alongside Art. 21A).",
        ["fd-list", "fd-origin"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Mohan Kumar Singhania v. Union of India",
        "slug": "mohan-kumar-singhania",
        "parties": "Mohan Kumar Singhania v. Union of India",
        "year": 1991,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Supreme Court held that Article 51A (Fundamental Duties) can aid "
            "interpretation of ambiguous laws when testing constitutionality."
        ),
        "holding": (
            "Fundamental Duties under Article 51A may be used to interpret ambiguous "
            "laws in order to determine their constitutionality."
        ),
        "concept_slugs": [HUB_SLUG, "fd-significance", "fd-triangle"],
    },
    {
        "title": "Re, Ramlila Maidan Incident",
        "slug": "ramlila-maidan-incident",
        "parties": "Re, Ramlila Maidan Incident",
        "year": 2012,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Court observed a common thread through Parts III, IV and IVA — "
            "rights, principles of governance, and citizen duties."
        ),
        "holding": (
            "While interpreting any of Parts III, IV or IVA, courts should examine "
            "the scope and impact on all three constitutional aspects."
        ),
        "concept_slugs": [HUB_SLUG, "fd-triangle", "fd-significance"],
    },
]

AMENDMENTS = [
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Inserted Part IVA and Article 51A — ten Fundamental Duties — "
            "on Swaran Singh Committee recommendations during Emergency era."
        ),
        "effect": "Created Fundamental Duties chapter; ten citizen duties in Art. 51A.",
        "concept_slugs": [HUB_SLUG, "fd-origin", "fd-list"],
    },
    {
        "number": 86,
        "year": 2002,
        "title": "Eighty-sixth Amendment",
        "summary": (
            "Added the eleventh Fundamental Duty — provide opportunities for education "
            "to child/ward between six and fourteen years (Art. 51A(k)); also inserted Art. 21A."
        ),
        "effect": "Art. 51A expanded to eleven duties; paired with Right to Education.",
        "concept_slugs": [HUB_SLUG, "fd-list", "fd-origin"],
    },
]


class Command(BaseCommand):
    help = "Seed Fundamental Duties chapter (Laxmikanth Ch.10) — visual revision."

    def add_arguments(self, parser):
        parser.add_argument(
            "--academy",
            default="fortuneias",
            help="Academy slug to seed into (default: fortuneias).",
        )

    def handle(self, *args, **options):
        from academies.seed_utils import get_academy_or_fail

        academy = get_academy_or_fail(options["academy"])
        subject, _ = Subject.objects.get_or_create(
            academy=academy,
            slug="polity",
            defaults={
                "name": "Polity",
                "description": "Indian Constitution and political system for UPSC.",
                "is_active": True,
            },
        )

        chapter, _ = Chapter.objects.update_or_create(
            subject=subject,
            slug=CHAPTER_SLUG,
            defaults={
                "title": "Fundamental Duties",
                "sort_order": 10,
                "book_ref": "Laxmikanth 8th Ed, Ch. 10",
                "summary": (
                    "Visual revision of Ch.10 — civic-checklist mental model, eleven duties, "
                    "features, criticism, significance, Verma statutes, and FR–DPSP–FD triangle."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Fundamental Duties",
                "summary": (
                    "Part IVA · Art. 51A — eleven non-justiciable citizen duties "
                    "(42nd + 86th Amendments)."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **civic-checklist mental model**, then scan the "
                    "**seven themes**. Lock 8→10→11 counts and citizens-only / non-justiciable. "
                    "Finish with Verma statutes and the FR–DPSP–FD triangle. "
                    "This is a visual revision layer — not a substitute for Laxmikanth."
                ),
                "visual_blocks": HUB_VISUAL_BLOCKS,
                "chapter": chapter,
                "sort_order": 0,
                "status": Concept.Status.PUBLISHED,
            },
        )

        by_slug = {HUB_SLUG: hub}

        for cluster in CLUSTERS:
            concept, _ = Concept.objects.update_or_create(
                subject=subject,
                slug=cluster["slug"],
                defaults={
                    "title": cluster["title"],
                    "summary": cluster["summary"],
                    "body": cluster["body"],
                    "visual_blocks": cluster["visual_blocks"],
                    "chapter": chapter,
                    "sort_order": cluster["sort_order"],
                    "status": Concept.Status.PUBLISHED,
                },
            )
            by_slug[cluster["slug"]] = concept
            ConceptArticle.objects.filter(concept=concept).delete()
            for i, (ref, excerpt) in enumerate(cluster["articles"]):
                ConceptArticle.objects.create(
                    concept=concept,
                    ref=ref,
                    excerpt=excerpt,
                    sort_order=i,
                )

        ConceptArticle.objects.filter(concept=hub).delete()
        ConceptArticle.objects.create(
            concept=hub,
            ref="Laxmikanth Ch. 10",
            excerpt="Fundamental Duties — Part IVA, Article 51A (eleven duties).",
            sort_order=0,
        )

        fd_slugs = set(by_slug.keys())
        related_outside = {
            "sf-fundamental-duties",
            "fundamental-rights",
            "directive-principles",
            "sf-dpsp",
        }
        ConceptEdge.objects.filter(
            source__slug__in=fd_slugs, source__subject=subject
        ).filter(target__slug__in=fd_slugs | related_outside).delete()

        created_edges = 0
        for src, rel, tgt in EDGES:
            source = by_slug.get(src) or Concept.objects.filter(
                subject=subject, slug=src
            ).first()
            target = by_slug.get(tgt) or Concept.objects.filter(
                subject=subject, slug=tgt
            ).first()
            if not source or not target:
                self.stdout.write(
                    self.style.WARNING(f"Skip edge {src} → {tgt} (missing concept)")
                )
                continue
            _, was_created = ConceptEdge.objects.get_or_create(
                source=source,
                target=target,
                relation_type=rel,
            )
            if was_created:
                created_edges += 1

        for year, question, answer, slugs in SAMPLE_PYQS:
            pyq, _ = PYQ.objects.get_or_create(
                academy=academy,
                year=year,
                question=question,
                defaults={"answer_key": answer},
            )
            if not pyq.answer_key and answer:
                pyq.answer_key = answer
                pyq.save(update_fields=["answer_key"])
            concepts = [by_slug[s] for s in slugs if s in by_slug]
            if concepts:
                pyq.concepts.add(*concepts)

        for case_data in LANDMARK_CASES:
            payload = {k: v for k, v in case_data.items() if k != "concept_slugs"}
            case, _ = CaseLaw.objects.update_or_create(
                academy=academy,
                slug=payload["slug"],
                defaults=payload,
            )
            concepts = [
                by_slug[s]
                for s in case_data["concept_slugs"]
                if s in by_slug
            ]
            if concepts:
                existing = list(case.concepts.all())
                case.concepts.set({*existing, *concepts})

        for amd_data in AMENDMENTS:
            payload = {k: v for k, v in amd_data.items() if k != "concept_slugs"}
            amendment, created = ConstitutionalAmendment.objects.get_or_create(
                academy=academy,
                number=payload["number"],
                defaults=payload,
            )
            # Do not overwrite broader summaries seeded by other chapters (e.g. 42nd).
            if not created:
                for field in ("title", "year", "summary", "effect"):
                    if not getattr(amendment, field, None) and payload.get(field):
                        setattr(amendment, field, payload[field])
                amendment.save()
            concepts = [
                by_slug[s]
                for s in amd_data["concept_slugs"]
                if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Fundamental Duties chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs."
            )
        )
