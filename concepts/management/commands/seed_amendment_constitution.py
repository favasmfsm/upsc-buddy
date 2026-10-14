"""Seed Laxmikanth Ch.11 Amendment of the Constitution (visual revision chapter)."""

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

HUB_SLUG = "amendment-of-constitution"
CHAPTER_SLUG = "amendment-of-constitution"

THEME_PILLARS = [
    {
        "id": "art368",
        "articles": "Part XX · Art. 368",
        "label": "Art. 368 & Limit",
        "slug": "am-art368-limit",
        "detail": "Constituent power to add, vary, repeal — basic structure ceiling.",
        "tone": "teal",
    },
    {
        "id": "procedure",
        "articles": "Art. 368",
        "label": "Amendment Procedure",
        "slug": "am-procedure",
        "detail": "Eight steps — no joint sitting; President must assent (24th).",
        "tone": "olive",
    },
    {
        "id": "three-ways",
        "articles": "3 paths",
        "label": "Three Ways",
        "slug": "am-three-ways",
        "detail": "Simple · special · special + half the states.",
        "tone": "gold",
    },
    {
        "id": "simple",
        "articles": "Outside 368",
        "label": "Simple Majority",
        "slug": "am-simple-majority",
        "detail": "Ordinary-law majority — not deemed Art. 368 amendments.",
        "tone": "orange",
    },
    {
        "id": "special",
        "articles": "Art. 368",
        "label": "Special Majority",
        "slug": "am-special-majority",
        "detail": "Total membership + 2/3 present and voting — FR, DPSP, rest.",
        "tone": "terracotta",
    },
    {
        "id": "federal",
        "articles": "Art. 368 + states",
        "label": "Federal + States",
        "slug": "am-federal-states",
        "detail": "Special majority + ratification by half the states.",
        "tone": "maroon",
    },
    {
        "id": "criticism",
        "articles": "Ch. 11 close",
        "label": "Criticism & Balance",
        "slug": "am-criticism-balance",
        "detail": "Seven critiques; Wheare / Nehru / Ambedkar balance lines.",
        "tone": "teal",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "am-living-rulebook",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Living rulebook",
        "topic_label": "Amendment",
        "subject_label": "Constitution",
        "relation_label": "Upgrades via",
        "protects_from": [
            "UK-easy vs USA-hard stereotypes",
            "Treating every change as Art. 368",
            "Assuming joint sitting for CAB",
            "Ignoring the basic-structure ceiling",
        ],
        "insight": (
            "India’s amendment path is a synthesis — neither as easy as Britain nor as hard as the USA. "
            "Parliament holds constituent power under Art. 368, but cannot destroy the basic structure."
        ),
    },
    {
        "id": "am-theme-pillars",
        "type": "pillars",
        "title": "Seven revision themes",
        "items": THEME_PILLARS,
    },
    {
        "id": "am-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Lock: **3 paths** + **8 steps** + **no joint sitting** + **President must assent (24th)**. "
            "This is a visual revision layer — not a substitute for Laxmikanth."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Art. 368 & Limit",
        "slug": "am-art368-limit",
        "sort_order": 1,
        "summary": (
            "Part XX Art. 368 — Parliament may add, vary, or repeal; basic structure is the ceiling."
        ),
        "body": (
            "## Article 368 and its outer limit\n\n"
            "Like any written constitution, India’s can be amended to meet changing needs. "
            "The procedure is **neither as easy as Britain nor as difficult as the USA** — "
            "a synthesis of flexibility and rigidity.\n\n"
            "**Article 368** (Part XX) deals with Parliament’s power to amend and the procedure. "
            "In exercise of **constituent power**, Parliament may amend by **addition, variation, or repeal** "
            "any provision — in accordance with the laid-down procedure.\n\n"
            "### Ceiling\n"
            "Parliament **cannot** amend provisions that form the **basic structure**. "
            "Ruled in **Kesavananda Bharati (1973)**. Depth on elements lives in the Basic Structure chapter."
        ),
        "articles": [
            (
                "Article 368",
                "Power of Parliament to amend the Constitution and procedure therefor — "
                "addition, variation, or repeal in exercise of constituent power.",
            ),
            (
                "Part XX",
                "Amendment of the Constitution — houses Article 368.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "am-368-tree",
                "type": "tree",
                "title": "Where Art. 368 sits",
                "root": {
                    "id": "constitution",
                    "label": "Constitution",
                    "children": [
                        {
                            "id": "part-xx",
                            "label": "Part XX",
                            "detail": "Amendment of the Constitution",
                            "children": [
                                {
                                    "id": "art-368",
                                    "label": "Article 368",
                                    "slug": "am-art368-limit",
                                    "detail": "Constituent power + procedure",
                                },
                                {
                                    "id": "ceiling",
                                    "label": "Basic structure ceiling",
                                    "slug": "basic-structure",
                                    "detail": "Kesavananda — cannot destroy foundation",
                                },
                            ],
                        }
                    ],
                },
            },
            {
                "id": "am-368-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Art. 368 power is **wide, not absolute**. "
                    "‘Any provision’ still stops at the basic structure (Kesavananda)."
                ),
            },
        ],
    },
    {
        "title": "Amendment Procedure",
        "slug": "am-procedure",
        "sort_order": 2,
        "summary": (
            "Eight Art. 368 steps — initiate in either House; special majority each House; "
            "no joint sitting; President must assent."
        ),
        "body": (
            "## Procedure under Article 368\n\n"
            "High-yield traps only — walk the flowchart for the sequence.\n\n"
            "1. **Initiate** only by a bill in **either House of Parliament** — not in state legislatures.\n"
            "2. Introduced by a **minister or private member**; **no prior President permission**.\n"
            "3. Passed in **each House** by **special majority** "
            "(majority of total membership + 2/3 of members present and voting).\n"
            "4. Houses pass **separately** — **no joint sitting** if they disagree.\n"
            "5. If federal provisions: ratified by **half the states** by simple majority.\n"
            "6. Then presented to the President for assent.\n"
            "7. President **must** assent — cannot withhold or return "
            "(**24th Amendment, 1971** made this obligatory).\n"
            "8. Assent → Constitutional Amendment Act; Constitution stands amended."
        ),
        "articles": [
            (
                "Article 368",
                "Procedure for amendment — special majority; state ratification where required.",
            ),
            (
                "24th Amendment (1971)",
                "President must give assent to a Constitution Amendment Bill — cannot withhold or return.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "am-proc-flow",
                "type": "flowchart",
                "title": "Art. 368 procedure (8 steps)",
                "root": "initiate",
                "steps": [
                    {
                        "id": "initiate",
                        "label": "1. Bill in either House",
                        "detail": "Only Parliament — not state legislatures.",
                        "options": [
                            {"label": "Next", "next": "introduce"},
                        ],
                    },
                    {
                        "id": "introduce",
                        "label": "2. Minister or private member",
                        "detail": "No prior permission of the President.",
                        "options": [
                            {"label": "Next", "next": "special"},
                        ],
                    },
                    {
                        "id": "special",
                        "label": "3. Special majority in each House",
                        "detail": "Total membership majority + 2/3 present and voting.",
                        "options": [
                            {"label": "Next", "next": "separate"},
                        ],
                    },
                    {
                        "id": "separate",
                        "label": "4. Houses pass separately",
                        "detail": "No joint sitting if they disagree.",
                        "options": [
                            {"label": "Federal provision?", "next": "federal-ask"},
                        ],
                    },
                    {
                        "id": "federal-ask",
                        "label": "5. Federal provisions?",
                        "detail": "State ratification branch.",
                        "options": [
                            {"label": "Yes — needs states", "next": "ratify"},
                            {"label": "No — go to President", "next": "present"},
                        ],
                    },
                    {
                        "id": "ratify",
                        "label": "5b. Half the states ratify",
                        "detail": "Simple majority in each ratifying legislature.",
                        "options": [
                            {"label": "Next", "next": "present"},
                        ],
                    },
                    {
                        "id": "present",
                        "label": "6–7. Present to President",
                        "detail": "Assent is obligatory (24th Amendment).",
                        "options": [
                            {"label": "Assent given", "next": "act"},
                        ],
                    },
                    {
                        "id": "act",
                        "label": "8. Amendment Act",
                        "detail": "Constitution stands amended as per the Act.",
                    },
                ],
            },
            {
                "id": "am-proc-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam traps",
                "body": (
                    "No state initiation (except Legislative Council resolution request). "
                    "No prior President permission. **No joint sitting** for CAB. "
                    "President **must** assent after the 24th."
                ),
            },
        ],
    },
    {
        "title": "Three Ways to Amend",
        "slug": "am-three-ways",
        "sort_order": 3,
        "summary": (
            "Simple majority (outside 368), special majority, or special majority + half the states."
        ),
        "body": (
            "## Three ways\n\n"
            "Art. 368 text covers **two** types (special majority; special + half the states). "
            "Other articles allow **simple majority** changes — **not deemed amendments under Art. 368**.\n\n"
            "So the Constitution is amended in **three** ways:\n"
            "1. Simple majority of Parliament (outside Art. 368).\n"
            "2. Special majority of Parliament (Art. 368).\n"
            "3. Special majority of Parliament **and** ratification by half the state legislatures."
        ),
        "articles": [
            (
                "Article 368",
                "Provides special majority and special majority + state ratification paths.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "am-three-compare",
                "type": "comparison",
                "title": "Three amendment paths",
                "columns": [
                    {
                        "id": "simple",
                        "heading": "Simple majority",
                        "points": [
                            "Like ordinary legislation",
                            "Outside Art. 368",
                            "Not ‘deemed’ 368 amendments",
                            "e.g. new states, quorum, UTs",
                        ],
                    },
                    {
                        "id": "special",
                        "heading": "Special majority",
                        "points": [
                            "Under Art. 368",
                            "Total membership + 2/3 P&V",
                            "FR, DPSP, residual provisions",
                            "Each House separately",
                        ],
                    },
                    {
                        "id": "federal",
                        "heading": "Special + states",
                        "points": [
                            "Under Art. 368",
                            "Plus half the states (simple majority)",
                            "Federal structure items",
                            "Includes Art. 368 itself",
                        ],
                    },
                ],
            },
            {
                "id": "am-three-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Simple-majority constitutional changes **exist** but are **outside Art. 368**. "
                    "Do not say ‘every amendment needs special majority’."
                ),
            },
        ],
    },
    {
        "title": "Simple Majority (Outside 368)",
        "slug": "am-simple-majority",
        "sort_order": 4,
        "summary": (
            "Many provisions change like ordinary laws — five mnemonic buckets, all outside Art. 368."
        ),
        "body": (
            "## Amendment by simple majority\n\n"
            "Same majority as ordinary bills: majority of members **present and voting** in each House. "
            "**Outside the scope of Article 368** — not deemed constitutional amendments for 368 purposes.\n\n"
            "Memorise by **bucket**, not as an 18-item dump. Open Laxmikanth only if a PYQ cites an odd item."
        ),
        "articles": [
            (
                "Outside Article 368",
                "Simple-majority changes to listed provisions are not deemed amendments under Art. 368.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "am-simple-buckets",
                "type": "pillars",
                "title": "Five memory buckets",
                "items": [
                    {
                        "id": "states",
                        "articles": "Arts 2–4 etc.",
                        "label": "States & territory",
                        "slug": "am-simple-majority",
                        "detail": "Admission/establishment; formation/boundaries/names; Union territories.",
                        "tone": "teal",
                    },
                    {
                        "id": "housekeeping",
                        "articles": "Parliament",
                        "label": "Parliament housekeeping",
                        "slug": "am-simple-majority",
                        "detail": "Quorum, MPs’ salaries, rules, privileges, English in Parliament.",
                        "tone": "olive",
                    },
                    {
                        "id": "judiciary",
                        "articles": "SC tweaks",
                        "label": "Judiciary tweaks",
                        "slug": "am-simple-majority",
                        "detail": "Number of puisne SC judges; conferring more SC jurisdiction.",
                        "tone": "gold",
                    },
                    {
                        "id": "schedules",
                        "articles": "2nd · 5th · 6th",
                        "label": "Schedules / special areas",
                        "slug": "am-simple-majority",
                        "detail": "2nd Schedule emoluments; 5th & 6th Schedule administration.",
                        "tone": "orange",
                    },
                    {
                        "id": "other",
                        "articles": "Misc.",
                        "label": "Other",
                        "slug": "am-simple-majority",
                        "detail": (
                            "Legislative councils; citizenship acquisition/termination; "
                            "elections; delimitation; official language."
                        ),
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "am-simple-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Revision tip",
                "body": (
                    "If it feels like **administrative / housekeeping / map-making**, "
                    "odds favour **simple majority outside 368**."
                ),
            },
        ],
    },
    {
        "title": "Special Majority",
        "slug": "am-special-majority",
        "sort_order": 5,
        "summary": (
            "Majority of total membership + 2/3 present and voting — FR, DPSP, and residual provisions."
        ),
        "body": (
            "## Amendment by special majority\n\n"
            "Most provisions need Art. 368 special majority in **each House**:\n"
            "- Majority of the **total membership** of the House, **and**\n"
            "- Majority of **two-thirds** of members **present and voting**.\n\n"
            "**Total membership** = full strength of the House — vacancies and absentees still count "
            "in the denominator of ‘majority of total membership’.\n\n"
            "Lok Sabha Rules apply the special-majority requirement at **all effective stages**, "
            "not only the final vote.\n\n"
            "### What this path covers\n"
            "- Fundamental Rights\n"
            "- Directive Principles of State Policy\n"
            "- All other provisions **not** in the simple-majority or federal+states categories"
        ),
        "articles": [
            (
                "Article 368",
                "Special majority: majority of total membership + two-thirds of members present and voting.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "am-special-pillars",
                "type": "pillars",
                "title": "What special majority covers",
                "items": [
                    {
                        "id": "fr",
                        "articles": "Part III",
                        "label": "Fundamental Rights",
                        "slug": "am-special-majority",
                        "detail": "Amendable under Art. 368 special majority — subject to basic structure.",
                        "tone": "teal",
                    },
                    {
                        "id": "dpsp",
                        "articles": "Part IV",
                        "label": "Directive Principles",
                        "slug": "am-special-majority",
                        "detail": "Same special-majority track as FR.",
                        "tone": "olive",
                    },
                    {
                        "id": "rest",
                        "articles": "Residual",
                        "label": "All other (residual)",
                        "slug": "am-special-majority",
                        "detail": "Anything not in simple-majority or federal+states lists.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "am-special-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "**Two tests, not one:** majority of *total membership* **and** 2/3 of *present and voting*. "
                    "Total membership ignores vacancies/absentees for that count. "
                    "LS Rules: special majority at **all effective stages**."
                ),
            },
        ],
    },
    {
        "title": "Federal Provisions + States",
        "slug": "am-federal-states",
        "sort_order": 6,
        "summary": (
            "Federal structure items need special majority plus ratification by half the states — "
            "no time limit."
        ),
        "body": (
            "## Special majority + consent of states\n\n"
            "Federal-structure provisions need Art. 368 special majority **and** ratification by "
            "**half the state legislatures** by **simple majority**.\n\n"
            "- Remaining states’ silence does **not** matter once half consent.\n"
            "- **No time limit** for states to consent.\n"
            "- Constitution is silent on whether a state may **withdraw** approval after giving it.\n\n"
            "### Federal list (scan, don’t essay)\n"
            "1. Election of the President and its manner\n"
            "2. Extent of executive power of Union and states\n"
            "3. Supreme Court and High Courts\n"
            "4. Distribution of legislative powers\n"
            "5. GST Council (Art. 279-A — **101st Amendment, 2016**)\n"
            "6. Any list in the Seventh Schedule\n"
            "7. Representation of states in Parliament\n"
            "8. Power of Parliament to amend / Art. **368 itself**"
        ),
        "articles": [
            (
                "Article 368",
                "Federal provisions: special majority of Parliament + ratification by half the states.",
            ),
            (
                "Article 279-A",
                "GST Council — added by the 101st Amendment; federal ratification track.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "am-federal-pillars",
                "type": "pillars",
                "title": "Federal ratification list",
                "items": [
                    {
                        "id": "president",
                        "articles": "President",
                        "label": "President election",
                        "slug": "am-federal-states",
                        "detail": "Election of the President and its manner.",
                        "tone": "teal",
                    },
                    {
                        "id": "exec",
                        "articles": "Executive",
                        "label": "Executive extent",
                        "slug": "am-federal-states",
                        "detail": "Union and state executive power extent.",
                        "tone": "olive",
                    },
                    {
                        "id": "courts",
                        "articles": "SC / HC",
                        "label": "SC & High Courts",
                        "slug": "am-federal-states",
                        "detail": "Supreme Court and high courts.",
                        "tone": "gold",
                    },
                    {
                        "id": "lists",
                        "articles": "7th Sch.",
                        "label": "Powers & lists",
                        "slug": "am-federal-states",
                        "detail": "Legislative distribution; any Seventh Schedule list.",
                        "tone": "orange",
                    },
                    {
                        "id": "gst",
                        "articles": "101st · 279-A",
                        "label": "GST Council",
                        "slug": "am-federal-states",
                        "detail": "Added by 101st Amendment (2016).",
                        "tone": "terracotta",
                    },
                    {
                        "id": "rep-368",
                        "articles": "Rep + 368",
                        "label": "States in Parliament · Art. 368",
                        "slug": "am-federal-states",
                        "detail": "State representation in Parliament; amending power itself.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "am-federal-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam traps",
                "body": (
                    "**Half** the states suffice (not three-fourths like USA). "
                    "**No time limit** for ratification. "
                    "Silent on **withdrawal** of approval. "
                    "Art. **368 itself** is on this federal track."
                ),
            },
        ],
    },
    {
        "title": "Criticism & Balance",
        "slug": "am-criticism-balance",
        "sort_order": 7,
        "summary": (
            "Seven critique hooks; procedure still strikes a balance between flexibility and rigidity."
        ),
        "body": (
            "## Criticism — then the balance\n\n"
            "Critics flag sketchy procedure and Parliament-heavy design. Still, the process has been "
            "**simple enough to adapt** and **not so flexible** that ruling parties rewrite at whim.\n\n"
            "### Balance one-liners\n"
            "- **K.C. Wheare** — strikes a good balance between flexibility and rigidity; "
            "variety in amending process is wise but rare.\n"
            "- **Nehru** — no permanence in a Constitution; rigidity would stop a living nation’s growth.\n"
            "- **Ambedkar** — Assembly provided a **facile** procedure (not Canadian finality or "
            "American/Australian extraordinary terms)."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "am-crit-pillars",
                "type": "pillars",
                "title": "Seven criticism hooks",
                "items": [
                    {
                        "id": "c1",
                        "articles": "1",
                        "label": "No special body",
                        "slug": "am-criticism-balance",
                        "detail": "No Constitutional Convention / Assembly — power in Parliament (states rarely).",
                        "tone": "teal",
                    },
                    {
                        "id": "c2",
                        "articles": "2",
                        "label": "Parliament initiates",
                        "slug": "am-criticism-balance",
                        "detail": "States cannot initiate (except Legislative Council request).",
                        "tone": "olive",
                    },
                    {
                        "id": "c3",
                        "articles": "3",
                        "label": "Mostly Parliament alone",
                        "slug": "am-criticism-balance",
                        "detail": "Only few cases need half the states — USA needs three-fourths.",
                        "tone": "gold",
                    },
                    {
                        "id": "c4",
                        "articles": "4",
                        "label": "No state time frame",
                        "slug": "am-criticism-balance",
                        "detail": "No deadline to ratify; silent on withdrawing approval.",
                        "tone": "orange",
                    },
                    {
                        "id": "c5",
                        "articles": "5",
                        "label": "No joint sitting",
                        "slug": "am-criticism-balance",
                        "detail": "Deadlock on CAB has no joint sitting (unlike ordinary bills).",
                        "tone": "terracotta",
                    },
                    {
                        "id": "c6",
                        "articles": "6",
                        "label": "Like ordinary process",
                        "slug": "am-criticism-balance",
                        "detail": "Same legislative pathway except special majority.",
                        "tone": "maroon",
                    },
                    {
                        "id": "c7",
                        "articles": "7",
                        "label": "Too sketchy",
                        "slug": "am-criticism-balance",
                        "detail": "Wide scope for judicial interpretation of gaps.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "am-balance-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Balance quotes (one-liners)",
                "body": (
                    "**Wheare** — good balance; variety is wise. "
                    "**Nehru** — living constitution needs flexibility. "
                    "**Ambedkar** — facile procedure, not sealed finality."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "am-art368-limit"),
    (HUB_SLUG, "parent", "am-procedure"),
    (HUB_SLUG, "parent", "am-three-ways"),
    (HUB_SLUG, "parent", "am-simple-majority"),
    (HUB_SLUG, "parent", "am-special-majority"),
    (HUB_SLUG, "parent", "am-federal-states"),
    (HUB_SLUG, "parent", "am-criticism-balance"),
    (HUB_SLUG, "related", "sf-rigidity-flexibility"),
    (HUB_SLUG, "related", "basic-structure"),
    ("am-art368-limit", "related", "basic-structure"),
    ("am-art368-limit", "related", "am-procedure"),
    ("am-procedure", "related", "am-three-ways"),
    ("am-three-ways", "related", "am-simple-majority"),
    ("am-three-ways", "related", "am-special-majority"),
    ("am-three-ways", "related", "am-federal-states"),
    ("am-procedure", "related", "am-federal-states"),
    ("am-special-majority", "related", "am-federal-states"),
    ("am-criticism-balance", "related", "am-procedure"),
]

LANDMARK_CASES = [
    {
        "title": "Kesavananda Bharati v. State of Kerala",
        "slug": "kesavananda-bharati",
        "parties": "Kesavananda Bharati v. State of Kerala",
        "year": 1973,
        "court": CaseLaw.Court.SC,
        "summary": "Landmark basic-structure ruling limiting constituent power under Art. 368.",
        "holding": (
            "Parliament’s constituent power under Art. 368 does not enable it to alter the "
            "basic structure of the Constitution."
        ),
        "concept_slugs": [HUB_SLUG, "am-art368-limit"],
    },
]

AMENDMENTS = [
    {
        "number": 24,
        "year": 1971,
        "title": "Twenty-fourth Amendment",
        "summary": (
            "Made President’s assent to Constitution Amendment Bills obligatory; "
            "also amended Arts 13 and 368 affirming Parliament’s power over FR."
        ),
        "effect": (
            "President cannot withhold or return a CAB; Parliament’s reply to Golak Nath on FR."
        ),
        "concept_slugs": [HUB_SLUG, "am-procedure"],
    },
    {
        "number": 101,
        "year": 2016,
        "title": "One Hundred and First Amendment",
        "summary": (
            "Introduced GST; added Article 279-A (GST Council) among federal amendment items."
        ),
        "effect": "GST Council placed on the special majority + state ratification track.",
        "concept_slugs": [HUB_SLUG, "am-federal-states"],
    },
]

SAMPLE_PYQS = [
    (
        2013,
        "Which of the following are the ways of amending the Constitution of India? "
        "Consider simple majority, special majority, and special majority with state ratification.",
        "Three ways: simple majority (outside 368), special majority (368), "
        "special majority + ratification by half the states.",
        ["am-three-ways", HUB_SLUG],
    ),
    (
        2019,
        "Consider statements on Constitution Amendment Bills: joint sitting; "
        "prior President permission; assent after passage.",
        "No joint sitting for CAB; no prior President permission; after 24th, President must assent.",
        ["am-procedure"],
    ),
]


class Command(BaseCommand):
    help = "Seed Amendment of the Constitution chapter (Laxmikanth Ch.11) — visual revision."

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
                "title": "Amendment of the Constitution",
                "sort_order": 11,
                "book_ref": "Laxmikanth 8th Ed, Ch. 11",
                "summary": (
                    "Visual revision of Ch.11 — Art. 368, eight-step procedure, three amendment paths, "
                    "federal ratification, criticism, and the basic-structure ceiling."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Amendment of the Constitution",
                "summary": (
                    "Part XX / Art. 368 — how India amends: three paths, procedure traps, "
                    "and the basic-structure limit."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **living-rulebook mental model**, scan the **seven themes**, "
                    "then drill **procedure traps** and the **three paths**. "
                    "Open Basic Structure only for the ceiling doctrine. "
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
            ref="Laxmikanth Ch. 11",
            excerpt=(
                "Amendment of the Constitution — Art. 368 procedure, three ways, "
                "criticism, and basic-structure limit."
            ),
            sort_order=0,
        )

        am_slugs = set(by_slug.keys())
        related_outside = {"sf-rigidity-flexibility", "basic-structure"}
        ConceptEdge.objects.filter(
            source__slug__in=am_slugs, source__subject=subject
        ).filter(target__slug__in=am_slugs | related_outside).delete()

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
            amendment, _ = ConstitutionalAmendment.objects.update_or_create(
                academy=academy,
                number=payload["number"],
                defaults=payload,
            )
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
                f"Amendment chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(SAMPLE_PYQS)} PYQs, {len(LANDMARK_CASES)} cases, "
                f"{len(AMENDMENTS)} amendments."
            )
        )
