"""Seed Laxmikanth Ch.17 Emergency Provisions (visual revision)."""

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

HUB_SLUG = "emergency-provisions"
CHAPTER_SLUG = "emergency-provisions"

ENTRY_PILLARS = [
    {
        "id": "types",
        "articles": "Part XVIII",
        "label": "Three types & rationale",
        "slug": "emg-three-types",
        "detail": "352 / 356 / 360 — federal → unitary without amendment.",
        "tone": "teal",
    },
    {
        "id": "grounds",
        "articles": "Art. 352",
        "label": "National — grounds",
        "slug": "emg-national-grounds",
        "detail": "War, external aggression, armed rebellion; cabinet written advice.",
        "tone": "olive",
    },
    {
        "id": "procedure",
        "articles": "1 month",
        "label": "National — procedure",
        "slug": "emg-national-procedure",
        "detail": "Special majority; 6-month renewals; LS can force revocation.",
        "tone": "gold",
    },
    {
        "id": "effects",
        "articles": "353–354",
        "label": "National — effects",
        "slug": "emg-national-effects",
        "detail": "Centre–state shift, House life extension, FR gateway.",
        "tone": "orange",
    },
    {
        "id": "fr",
        "articles": "358 · 359",
        "label": "Art. 358 vs 359",
        "slug": "emg-358-vs-359",
        "detail": "19 auto-external; enforcement order; 20–21 never sleep.",
        "tone": "terracotta",
    },
    {
        "id": "history",
        "articles": "1962·71·75",
        "label": "Declarations so far",
        "slug": "emg-national-history",
        "detail": "Three proclamations; Shah Commission → 44th shields.",
        "tone": "maroon",
    },
    {
        "id": "pr",
        "articles": "356 · 365",
        "label": "President’s Rule",
        "slug": "emg-presidents-rule",
        "detail": "Machinery failure; 2 months; max 3 years; HC untouched.",
        "tone": "teal",
    },
    {
        "id": "vs",
        "articles": "Table 17.1",
        "label": "352 vs 356",
        "slug": "emg-352-vs-356",
        "detail": "Centre grows over states vs Centre replaces one state.",
        "tone": "olive",
    },
    {
        "id": "bommai",
        "articles": "Bommai",
        "label": "Bommai & proper use",
        "slug": "emg-bommai",
        "detail": "Judicial review; floor test; Sarkaria proper/improper.",
        "tone": "gold",
    },
    {
        "id": "fin",
        "articles": "Art. 360",
        "label": "Financial Emergency",
        "slug": "emg-financial",
        "detail": "Never declared; indefinite once approved; salary cuts.",
        "tone": "orange",
    },
    {
        "id": "critique",
        "articles": "44th pack",
        "label": "Criticism & safeguards",
        "slug": "emg-criticism-safeguards",
        "detail": "CA debate + 44th firewall + Arts 352–360 glance.",
        "tone": "terracotta",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "emg-switch-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Federal → unitary switch",
        "topic_label": "Emergency Provisions",
        "subject_label": "Part XVIII · Arts 352–360",
        "relation_label": "Protects you from",
        "protects_from": [
            "Calling Art. 356 a ‘proclamation of emergency’",
            "Mixing 1-month vs 2-month approval clocks",
            "Thinking FR die under President’s Rule",
            "Forgetting 44th Amendment shields after 1975",
        ],
        "insight": (
            "In a crisis the Centre can become all-powerful and the system works "
            "as if unitary — without amending the Constitution."
        ),
    },
    {
        "id": "emg-entry-pillars",
        "type": "pillars",
        "title": "Eleven revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "emg-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Scan **352 / 356 / 360**. Constitution uses ‘proclamation of emergency’ only for 352. "
            "44th Amendment = anti-1975 firewall. Bommai = Art. 356 judicial-review bible. "
            "Mnemonic: War-Rebellion / Machinery / Money."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Three Types & Rationale",
        "slug": "emg-three-types",
        "sort_order": 1,
        "summary": (
            "Part XVIII enables Centre to meet abnormal situations — three emergencies "
            "that can turn federal into unitary without amendment."
        ),
        "body": (
            "## Why these provisions exist\n\n"
            "Safeguard sovereignty, unity, integrity, security, the democratic system, and the Constitution.\n\n"
            "### Unique feature (Mains line)\n"
            "During Emergency the Centre becomes all-powerful; states come under its control — "
            "federal structure becomes **unitary without a formal amendment**. "
            "Ambedkar: the Constitution can be federal in normal times and work as unitary in Emergency.\n\n"
            "### Three types\n"
            "1. **National Emergency (Art. 352)** — war / external aggression / armed rebellion. "
            "Constitution’s phrase: **‘proclamation of emergency’**.\n"
            "2. **President’s Rule (Art. 356)** — failure of constitutional machinery in a state. "
            "Also called State / Constitutional Emergency — but Constitution does **not** use ‘emergency’ here.\n"
            "3. **Financial Emergency (Art. 360)** — threat to financial stability or credit of India.\n\n"
            "**Mnemonic:** War-Rebellion / Machinery / Money → 352 / 356 / 360."
        ),
        "articles": [
            (
                "Part XVIII",
                "Emergency provisions — Articles 352 to 360.",
            ),
            (
                "Art. 352 · 356 · 360",
                "National Emergency, President’s Rule, and Financial Emergency.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-types-tree",
                "type": "tree",
                "title": "Part XVIII map",
                "root": {
                    "id": "part-xviii",
                    "label": "Part XVIII — Emergency",
                    "detail": "Arts 352–360",
                    "children": [
                        {
                            "id": "n352",
                            "label": "Art. 352 — National",
                            "slug": "emg-national-grounds",
                            "detail": "War / aggression / armed rebellion",
                        },
                        {
                            "id": "n356",
                            "label": "Art. 356 (+ 365) — President’s Rule",
                            "slug": "emg-presidents-rule",
                            "detail": "Failure of constitutional machinery",
                        },
                        {
                            "id": "n360",
                            "label": "Art. 360 — Financial",
                            "slug": "emg-financial",
                            "detail": "Stability / credit threatened",
                        },
                    ],
                },
            },
            {
                "id": "emg-types-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Ambedkar (Mains)",
                "body": (
                    "Unlike the American mould, India’s Constitution can be both federal and unitary "
                    "as circumstances demand — Emergency flips the switch without amendment."
                ),
            },
        ],
    },
    {
        "title": "National Emergency — Grounds",
        "slug": "emg-national-grounds",
        "sort_order": 2,
        "summary": (
            "Art. 352 — war, external aggression, or armed rebellion; imminent danger allowed; "
            "written cabinet recommendation; judicially reviewable after 44th / Minerva Mills."
        ),
        "body": (
            "## Grounds (Art. 352)\n\n"
            "President may proclaim when security of India **or a part** is threatened by:\n"
            "- war\n"
            "- external aggression\n"
            "- armed rebellion\n\n"
            "Imminent danger is enough — actual occurrence not required.\n\n"
            "### Labels\n"
            "- **External Emergency** — war or external aggression\n"
            "- **Internal Emergency** — armed rebellion\n\n"
            "### Key changes\n"
            "- **42nd:** emergency may be limited to a specified part of India.\n"
            "- **44th:** ‘armed rebellion’ replaces vague ‘internal disturbance’ "
            "(1975-style ground is dead).\n"
            "- **38th:** allowed fresh proclamations even if one already operates "
            "(war / aggression / rebellion / imminent danger).\n\n"
            "### Cabinet written recommendation (44th)\n"
            "Emergency only after **written** recommendation of the Cabinet "
            "(PM + other Cabinet-rank ministers) — not PM alone. "
            "1975: Indira Gandhi advised President without consulting Cabinet.\n\n"
            "### Judicial review\n"
            "38th made declaration immune → **44th deleted** that bar. "
            "**Minerva Mills (1980):** proclamation challengeable for malafide, "
            "wholly extraneous / irrelevant facts, or absurd / perverse satisfaction."
        ),
        "articles": [
            (
                "Article 352",
                "Proclamation of Emergency — war, external aggression, or armed rebellion.",
            ),
            (
                "44th Amendment",
                "Armed rebellion wording; written Cabinet recommendation; review restored.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-grounds-flow",
                "type": "flowchart",
                "title": "Which National Emergency ground?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What threatens security?",
                        "detail": "Match ground → label → Article 352.",
                        "options": [
                            {"label": "War or external aggression", "next": "ext"},
                            {"label": "Armed rebellion", "next": "int"},
                            {"label": "Mere ‘internal disturbance’", "next": "dead"},
                        ],
                    },
                    {
                        "id": "ext",
                        "label": "External Emergency",
                        "detail": "War / external aggression — Art. 19 can auto-suspend (358).",
                    },
                    {
                        "id": "int",
                        "label": "Internal Emergency",
                        "detail": "Armed rebellion — Art. 19 does NOT auto-suspend under 358.",
                    },
                    {
                        "id": "dead",
                        "label": "Not a ground after 44th",
                        "detail": "‘Internal disturbance’ used in 1975 — removed by 44th Amendment.",
                    },
                ],
            },
            {
                "id": "emg-grounds-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "After the 44th Amendment you cannot proclaim National Emergency on "
                    "‘internal disturbance’. Also: President needs written Cabinet concurrence — "
                    "not the Prime Minister alone."
                ),
            },
        ],
    },
    {
        "title": "National Emergency — Procedure",
        "slug": "emg-national-procedure",
        "sort_order": 3,
        "summary": (
            "Both Houses approve within 1 month by special majority; renew every 6 months; "
            "Lok Sabha can force revocation by simple majority."
        ),
        "body": (
            "## Parliamentary approval & duration\n\n"
            "- Must be approved by **both Houses within one month** (originally two; cut by 44th).\n"
            "- If approved → continues **six months**; renew with fresh approval every six months "
            "(indefinite in theory).\n"
            "- Approval / continuance resolution needs **special majority**: "
            "(a) majority of total membership, and (b) ≥ 2/3 of members present and voting.\n"
            "- If Lok Sabha is dissolved without approving: survives until **30 days** from first "
            "sitting of reconstituted LS, if Rajya Sabha has approved in the meantime.\n\n"
            "## Revocation\n\n"
            "- President may revoke anytime by later proclamation — **no** parliamentary approval needed.\n"
            "- **Must** revoke if Lok Sabha passes a resolution **disapproving** continuation "
            "(44th safeguard).\n"
            "- Disapproval: **Lok Sabha only** + **simple majority**.\n"
            "- If 1/10 of total LS members give written notice → special sitting within **14 days**.\n\n"
            "### Approve vs disapprove\n"
            "| | Approving continuance | Disapproving |\n"
            "|---|---|---|\n"
            "| House | Both Houses | Lok Sabha only |\n"
            "| Majority | Special | Simple |"
        ),
        "articles": [
            (
                "Article 352",
                "Proclamation, parliamentary approval, continuance, and revocation.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-proc-flow",
                "type": "flowchart",
                "title": "National Emergency life cycle",
                "root": "issue",
                "steps": [
                    {
                        "id": "issue",
                        "label": "President issues proclamation",
                        "detail": "After written Cabinet recommendation.",
                        "options": [
                            {"label": "Both Houses approve in 1 month", "next": "live"},
                            {"label": "Not approved in time", "next": "lapse"},
                        ],
                    },
                    {
                        "id": "live",
                        "label": "Lives 6 months",
                        "detail": "Renew every 6 months by special majority of both Houses.",
                        "options": [
                            {"label": "Renew", "next": "live"},
                            {"label": "President revokes", "next": "end"},
                            {"label": "LS disapproves (simple)", "next": "force"},
                        ],
                    },
                    {
                        "id": "lapse",
                        "label": "Proclamation falls",
                        "detail": "Unless LS-dissolution edge case (30-day window after reconstitution).",
                    },
                    {
                        "id": "force",
                        "label": "President must revoke",
                        "detail": "44th: LS disapproval forces end.",
                    },
                    {
                        "id": "end",
                        "label": "Emergency ends",
                        "detail": "No parliamentary approval needed for revocation proclamation.",
                    },
                ],
            },
            {
                "id": "emg-proc-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Approval clock mnemonic",
                "body": (
                    "National = **1 month + special majority**. "
                    "President’s Rule / Financial = **2 months + simple majority**."
                ),
            },
        ],
    },
    {
        "title": "National Emergency — Effects",
        "slug": "emg-national-effects",
        "sort_order": 4,
        "summary": (
            "Centre–state relations go unitary; Lok Sabha / assembly life can be extended; "
            "FR effects via Arts 358–359."
        ),
        "body": (
            "## Three effect buckets\n\n"
            "### 1. Centre–state relations\n"
            "- **Executive:** Centre may direct a state on **any** matter (states not suspended).\n"
            "- **Legislative:** Parliament may legislate on State List; state legislature continues "
            "but is overridden. Laws on state subjects lapse **6 months** after emergency ends. "
            "President may issue ordinances on state subjects if Parliament not in session.\n"
            "- **Financial (Art. 354):** President may modify Centre–state revenue distribution; "
            "order lasts till end of the financial year in which emergency ends; laid before Parliament.\n"
            "- **42nd:** executive + legislative consequences can extend to **other states** too, "
            "not only the emergency area.\n\n"
            "### 2. Life of Lok Sabha & state assemblies\n"
            "- Extend beyond 5 years by **1 year at a time** (any length while NE operates).\n"
            "- Extension cannot continue beyond **6 months** after emergency ceases.\n"
            "- Example: Fifth Lok Sabha (1971–77) extended twice.\n\n"
            "### 3. Fundamental Rights\n"
            "Arts **358** and **359** — drill the next cluster.\n\n"
            "**Trap:** Under 352, state governments continue; they are **not** dismissed "
            "(contrast Art. 356)."
        ),
        "articles": [
            (
                "Article 353",
                "Effect of Proclamation of Emergency — executive and legislative expansion.",
            ),
            (
                "Article 354",
                "Modify distribution of revenues while Proclamation of Emergency is in force.",
            ),
            (
                "Articles 358 & 359",
                "Suspension of Art. 19 / enforcement of other Fundamental Rights.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-effects-pillars",
                "type": "pillars",
                "title": "Five effect heads",
                "items": [
                    {
                        "id": "exec",
                        "articles": "Executive",
                        "label": "Any-matter directions",
                        "slug": "emg-national-effects",
                        "detail": "Centre directs states on any subject; governments continue.",
                        "tone": "teal",
                    },
                    {
                        "id": "leg",
                        "articles": "Legislative",
                        "label": "Parliament on State List",
                        "slug": "emg-national-effects",
                        "detail": "Overriding Union laws; lapse 6 months after emergency ends.",
                        "tone": "olive",
                    },
                    {
                        "id": "fin",
                        "articles": "Art. 354",
                        "label": "Revenue redistribution",
                        "slug": "emg-national-effects",
                        "detail": "President may reduce/cancel Centre→state transfers.",
                        "tone": "gold",
                    },
                    {
                        "id": "tenure",
                        "articles": "1 year",
                        "label": "House life extension",
                        "slug": "emg-national-effects",
                        "detail": "LS / assembly +1 year at a time; max +6 months after end.",
                        "tone": "orange",
                    },
                    {
                        "id": "fr",
                        "articles": "358·359",
                        "label": "Fundamental Rights",
                        "slug": "emg-358-vs-359",
                        "detail": "Open the 358 vs 359 comparison next.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "emg-effects-trap",
                "type": "callout",
                "tone": "trap",
                "title": "352 ≠ dismiss state ministry",
                "body": (
                    "National Emergency brings states under Centre’s control but does **not** dismiss "
                    "the state Council of Ministers. Dismissal / assumption of state executive is Art. 356."
                ),
            },
        ],
    },
    {
        "title": "Art. 358 vs Art. 359",
        "slug": "emg-358-vs-359",
        "sort_order": 5,
        "summary": (
            "High-weight prelims contrast — automatic Art. 19 suspension vs ordered suspension "
            "of enforcement; Arts 20 and 21 never sleep."
        ),
        "body": (
            "## Article 358 — Art. 19\n"
            "- Six rights under Art. 19 **automatically** suspend when NE is proclaimed.\n"
            "- After 44th: only for **External Emergency** (war / external aggression), "
            "not armed rebellion.\n"
            "- Operates for entire emergency; extends to whole country.\n"
            "- Only emergency-related laws (and action under them) get immunity.\n\n"
            "## Article 359 — enforcement\n"
            "- President may suspend the **right to move court** for specified FR — "
            "rights themselves stay theoretically alive.\n"
            "- Works for **both** External and Internal Emergency.\n"
            "- May cover whole/part country; duration = emergency or shorter period in the order.\n"
            "- After 44th: **Arts 20 and 21 cannot** have enforcement suspended.\n"
            "- Order must be laid before each House; only emergency-related laws get immunity.\n\n"
            "**Mnemonic:** 19 Auto-External; 20–21 Never Sleep."
        ),
        "articles": [
            (
                "Article 358",
                "Suspension of provisions of Article 19 during External Emergency.",
            ),
            (
                "Article 359",
                "Suspension of enforcement of specified Part III rights (except 20 & 21).",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-358-359-compare",
                "type": "comparison",
                "title": "Article 358 vs Article 359",
                "columns": [
                    {
                        "id": "a358",
                        "heading": "Art. 358",
                        "points": [
                            "Only Fundamental Rights under Art. 19",
                            "Automatic suspension on proclamation",
                            "External Emergency only (post-44th)",
                            "Entire duration of Emergency",
                            "Entire country",
                            "Art. 19 suspended completely",
                            "State may abridge Art. 19 rights",
                        ],
                    },
                    {
                        "id": "a359",
                        "heading": "Art. 359",
                        "points": [
                            "FR whose enforcement the Order names",
                            "Not automatic — needs Presidential Order",
                            "External and Internal Emergency",
                            "Period fixed in the Order (≤ Emergency)",
                            "Whole country or a part",
                            "Cannot touch enforcement of Arts 20 & 21",
                            "State may abridge only those specified rights",
                        ],
                    },
                ],
            },
            {
                "id": "emg-358-359-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims hook",
                "body": (
                    "Shared rule after 44th: immunity only for laws **related to the Emergency** "
                    "(and executive action under such laws) — not random laws."
                ),
            },
        ],
    },
    {
        "title": "Declarations Made So Far",
        "slug": "emg-national-history",
        "sort_order": 6,
        "summary": (
            "Three National Emergencies — 1962, 1971, 1975; Shah Commission damned 1975 "
            "and drove the 44th Amendment shields."
        ),
        "body": (
            "## Three proclamations\n\n"
            "1. **Oct 1962** — Chinese aggression in NEFA (now Arunachal). External. "
            "In force till **Jan 1968** — so no fresh proclamation needed for 1965 Pakistan war.\n"
            "2. **Dec 1971** — attack by Pakistan. External.\n"
            "3. **June 1975** — ‘internal disturbance’ (most controversial). "
            "Both 1971 and 1975 revoked in **March 1977**.\n\n"
            "### Aftermath\n"
            "1977 Lok Sabha elections: Congress lost; Janata came to power. "
            "**Shah Commission** investigated 1975 Emergency and did **not** justify it. "
            "Hence **44th Amendment (1978)** packed in safeguards against misuse."
        ),
        "articles": [
            (
                "Article 352",
                "National Emergency proclamations of 1962, 1971, and 1975.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-hist-timeline",
                "type": "timeline",
                "title": "National Emergency timeline",
                "events": [
                    {
                        "id": "e1962",
                        "year": 1962,
                        "label": "First NE — China",
                        "detail": "External aggression; lasted till January 1968.",
                    },
                    {
                        "id": "e1971",
                        "year": 1971,
                        "label": "Second NE — Pakistan",
                        "detail": "External aggression; still running when third began.",
                    },
                    {
                        "id": "e1975",
                        "year": 1975,
                        "label": "Third NE — internal",
                        "detail": "Internal disturbance; most misused; revoked March 1977.",
                    },
                    {
                        "id": "e1978",
                        "year": 1978,
                        "label": "44th Amendment",
                        "detail": "Shah Commission fallout → Emergency firewall.",
                    },
                ],
            },
            {
                "id": "emg-hist-trap",
                "type": "callout",
                "tone": "trap",
                "title": "1975 ground is dead",
                "body": (
                    "1975 used ‘internal disturbance’. After 44th, only war / external aggression / "
                    "armed rebellion remain — that 1975 ground cannot be reused."
                ),
            },
        ],
    },
    {
        "title": "President’s Rule",
        "slug": "emg-presidents-rule",
        "sort_order": 7,
        "summary": (
            "Art. 356 (via Art. 355 duty) and Art. 365 — take over a state; 2-month approval; "
            "max 3 years; High Court untouched."
        ),
        "body": (
            "## Grounds\n\n"
            "**Art. 355** duty: Centre must protect every state and ensure government is carried on "
            "per the Constitution — this duty justifies Art. 356 takeovers.\n\n"
            "1. **Art. 356:** President satisfied that state government cannot be carried on "
            "in accordance with the Constitution — on Governor’s report **or otherwise**.\n"
            "2. **Art. 365:** state fails to comply with / give effect to Centre’s directions → "
            "President may hold that Art. 356 situation has arisen.\n\n"
            "## Approval & duration\n\n"
            "- Both Houses within **two months**; **simple majority**.\n"
            "- Continues **six months**; extendable to max **three years** (six-month renewals).\n"
            "- Beyond **one year** (44th): only if (a) National Emergency is in operation "
            "in whole India / whole or part of that state, **and** (b) Election Commission certifies "
            "that assembly elections cannot be held.\n"
            "- President may revoke anytime — no parliamentary approval.\n"
            "- Footnote: Punjab PR (1987) extended to **five years** via **68th Amendment (1991)**.\n\n"
            "## Consequences\n\n"
            "President may: take state executive functions; declare state legislature powers "
            "exercisable by Parliament; take other necessary steps (except High Court).\n\n"
            "In practice: dismiss CoM; Governor runs state with advisors / Chief Secretary; "
            "assembly suspended or dissolved; Parliament passes state laws/budget "
            "(or delegates → **President’s Acts**). Laws survive after PR ends "
            "(state legislature may repeal/alter later).\n\n"
            "**HC status, powers, functions remain intact.**"
        ),
        "articles": [
            (
                "Article 355",
                "Union’s duty to protect states and ensure constitutional government.",
            ),
            (
                "Article 356",
                "Provisions in case of failure of constitutional machinery in states.",
            ),
            (
                "Article 365",
                "Effect of failure to comply with directions given by the Union.",
            ),
            (
                "Article 357",
                "Exercise of legislative powers under an Art. 356 proclamation.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-pr-flow",
                "type": "flowchart",
                "title": "Path to President’s Rule",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What failed?",
                        "detail": "Two constitutional doorways into Art. 356.",
                        "options": [
                            {
                                "label": "Constitutional machinery fails",
                                "next": "a356",
                            },
                            {
                                "label": "State ignores Union directions",
                                "next": "a365",
                            },
                        ],
                    },
                    {
                        "id": "a356",
                        "label": "Art. 356 directly",
                        "detail": "Governor’s report or otherwise — President proclaims.",
                    },
                    {
                        "id": "a365",
                        "label": "Art. 365 → Art. 356",
                        "detail": "Non-compliance lets President hold that 356 situation exists.",
                    },
                ],
            },
            {
                "id": "emg-pr-pillars",
                "type": "pillars",
                "title": "What the President acquires",
                "items": [
                    {
                        "id": "exec",
                        "articles": "Executive",
                        "label": "Take state executive",
                        "slug": "emg-presidents-rule",
                        "detail": "Dismiss CoM; Governor administers for the President.",
                        "tone": "teal",
                    },
                    {
                        "id": "leg",
                        "articles": "Art. 357",
                        "label": "Parliament / President’s Acts",
                        "slug": "emg-presidents-rule",
                        "detail": "May delegate law-making for the state to the President.",
                        "tone": "olive",
                    },
                    {
                        "id": "hc",
                        "articles": "Limit",
                        "label": "High Court untouched",
                        "slug": "emg-presidents-rule",
                        "detail": "Cannot assume HC powers or suspend HC provisions.",
                        "tone": "gold",
                    },
                ],
            },
        ],
    },
    {
        "title": "National Emergency vs President’s Rule",
        "slug": "emg-352-vs-356",
        "sort_order": 8,
        "summary": (
            "Table 17.1 revision — grounds, state machinery, law-making, max period, "
            "majority, FR impact, and revocation."
        ),
        "body": (
            "## One-line tell\n\n"
            "**352 = Centre grows over (all) states.** "
            "**356 = Centre replaces one state’s executive & legislature.**\n\n"
            "Scan the comparison visual for the eight classic contrasts "
            "(grounds, machinery, delegation, max period, which states, majority, FR, LS revocation)."
        ),
        "articles": [
            (
                "Article 352",
                "National Emergency — Centre acquires concurrent power over states.",
            ),
            (
                "Article 356",
                "President’s Rule — Centre assumes state executive and legislative power.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-352-356-compare",
                "type": "comparison",
                "title": "Art. 352 vs Art. 356 (Table 17.1)",
                "columns": [
                    {
                        "id": "ne",
                        "heading": "National Emergency (352)",
                        "points": [
                            "War / external aggression / armed rebellion",
                            "State executive & legislature continue; Centre gets concurrent power",
                            "Parliament alone legislates on State List (no delegation)",
                            "No maximum period; renew every 6 months",
                            "Centre–state relation with all states can change",
                            "Special majority for approval / continuance",
                            "Affects Fundamental Rights (358/359)",
                            "Lok Sabha can force revocation",
                        ],
                    },
                    {
                        "id": "pr",
                        "heading": "President’s Rule (356)",
                        "points": [
                            "Constitutional machinery failure (any reason)",
                            "State executive dismissed; assembly suspended/dissolved",
                            "Parliament may delegate law-making → President’s Acts",
                            "Maximum 3 years",
                            "Only the affected state’s relation with Centre changes",
                            "Simple majority for approval / continuance",
                            "No effect on Fundamental Rights",
                            "Only President can revoke (no LS disapproval route)",
                        ],
                    },
                ],
            },
            {
                "id": "emg-352-356-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Quick tell",
                "body": (
                    "Does FR get hit? Only under 352. Is the state ministry dismissed? Only under 356. "
                    "Special majority? Only National Emergency approvals."
                ),
            },
        ],
    },
    {
        "title": "Bommai & Proper / Improper Use",
        "slug": "emg-bommai",
        "sort_order": 9,
        "summary": (
            "Art. 356 is judicially reviewable; Bommai propositions; Sarkaria proper vs improper "
            "situations — floor test first."
        ),
        "body": (
            "## Judicial review of Art. 356\n\n"
            "38th made President’s satisfaction final → **44th deleted** that bar.\n\n"
            "### Bommai (1994) — revision spine\n"
            "1. Presidential proclamation is subject to judicial review.\n"
            "2. Satisfaction must rest on relevant material; malafide / extraneous / perverse → struck down.\n"
            "3. Burden on Centre to show relevant material exists.\n"
            "4. Court checks relevance, not correctness/adequacy of material.\n"
            "5. If invalid, court may restore dismissed government and revive assembly.\n"
            "6. Dissolve assembly only **after** Parliament approves; till then only suspend.\n"
            "7. Secularism is a basic feature — anti-secular state politics can invite 356.\n"
            "8. Confidence of the House is tested on the **floor**, not by Governor’s private count.\n"
            "9. New party at Centre cannot dismiss opposite-party state ministries wholesale.\n"
            "10. Exceptional power — use occasionally for special situations.\n\n"
            "### Proper use (Sarkaria / Bommai)\n"
            "Hung assembly; majority party declines to form ministry; defeat + no alternative; "
            "disregard of constitutional directions; internal subversion; physical breakdown.\n\n"
            "### Improper use\n"
            "No probe for alternative ministry; Governor’s armchair majority test; "
            "dismissal after LS defeat (1977/1980 pattern); mere internal disturbance; "
            "maladministration/corruption/finance crunch; no prior warning; intra-party score-settling.\n\n"
            "**Mnemonic:** Floor before fall; Suspend before dissolve.\n\n"
            "Ambedkar hoped 356 would be a ‘dead letter’; H.V. Kamath later: "
            "‘Dr. Ambedkar is dead and the Articles are very much alive.’"
        ),
        "articles": [
            (
                "Article 356",
                "President’s Rule — subject to judicial review after Bommai.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-bommai-compare",
                "type": "comparison",
                "title": "Proper vs improper use of Art. 356",
                "columns": [
                    {
                        "id": "proper",
                        "heading": "Proper",
                        "points": [
                            "Hung assembly after polls",
                            "Majority party refuses to form ministry",
                            "Ministry defeated; no alternative possible",
                            "Constitutional directions disregarded",
                            "Internal subversion / violent revolt",
                            "Physical breakdown of obligations",
                        ],
                    },
                    {
                        "id": "improper",
                        "heading": "Improper",
                        "points": [
                            "No attempt to find alternative ministry",
                            "Governor skips floor test",
                            "LS electoral defeat of ruling party (1977/1980)",
                            "Mere internal disturbance",
                            "Maladministration / corruption / money crunch",
                            "No warning; intra-party politics",
                        ],
                    },
                ],
            },
            {
                "id": "emg-bommai-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Mains value",
                "body": (
                    "Dead letter → deadly weapon. Bommai restored federal discipline: "
                    "floor test, suspend-before-dissolve, and secularism as a basic feature trigger."
                ),
            },
        ],
    },
    {
        "title": "Financial Emergency",
        "slug": "emg-financial",
        "sort_order": 10,
        "summary": (
            "Art. 360 — threat to financial stability or credit; 2-month simple-majority approval; "
            "indefinite duration; never declared so far."
        ),
        "body": (
            "## Grounds (Art. 360)\n\n"
            "President satisfied that financial stability or credit of India **or any part** "
            "of its territory is threatened.\n\n"
            "38th made satisfaction final → **44th deleted** — now open to judicial review.\n\n"
            "## Approval & duration\n\n"
            "- Both Houses within **two months**; **simple majority**.\n"
            "- Once approved → continues **indefinitely** until revoked "
            "(no maximum period; **no** six-month renewals).\n"
            "- President may revoke anytime — no parliamentary approval.\n\n"
            "## Effects\n\n"
            "1. Centre may direct states to observe canons of financial propriety "
            "(and other directions President deems necessary).\n"
            "2. Directions may require: reduction of state salaries/allowances; "
            "reservation of money bills / other financial bills for President after state legislature passes them.\n"
            "3. President may reduce salaries/allowances of Union servants and of "
            "**Supreme Court and High Court judges**.\n\n"
            "Centre acquires full financial control over states. "
            "Kunzru: threat to state financial autonomy. "
            "Ambedkar linked the idea to the US **National Recovery Act, 1933**.\n\n"
            "**Never declared** — even during the 1991 financial crisis."
        ),
        "articles": [
            (
                "Article 360",
                "Provisions as to Financial Emergency.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-fin-pillars",
                "type": "pillars",
                "title": "Financial Emergency at a glance",
                "items": [
                    {
                        "id": "ground",
                        "articles": "Art. 360",
                        "label": "Ground",
                        "slug": "emg-financial",
                        "detail": "Financial stability or credit of India / any part threatened.",
                        "tone": "teal",
                    },
                    {
                        "id": "process",
                        "articles": "2 months",
                        "label": "Process",
                        "slug": "emg-financial",
                        "detail": "Simple majority; then indefinite until revoked.",
                        "tone": "olive",
                    },
                    {
                        "id": "effects",
                        "articles": "Effects",
                        "label": "Salary & bill control",
                        "slug": "emg-financial",
                        "detail": "Cut state/Union/judge pay; reserve money bills for President.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "emg-fin-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Duration trap",
                "body": (
                    "Unlike 352/356, Financial Emergency needs **no** periodic six-month renewals "
                    "once Parliament has approved it. Also: never used so far."
                ),
            },
        ],
    },
    {
        "title": "Criticism, Defence & Safeguards",
        "slug": "emg-criticism-safeguards",
        "sort_order": 11,
        "summary": (
            "Constituent Assembly critics vs protagonists; 44th Amendment firewall; "
            "Articles 352–360 at a glance."
        ),
        "body": (
            "## Constituent Assembly debate\n\n"
            "**Critics:** federal character destroyed; Union executive concentrates power; "
            "President as dictator; state financial autonomy nullified; FR meaningless "
            "(Kamath — totalitarian fear; K.T. Shah — reaction/retrogression; "
            "T.T. Krishnamachari — constitutional dictatorship; Kunzru — financial autonomy).\n\n"
            "**Protagonists:** Alladi Krishnaswami Ayyar — ‘life-breath of the Constitution’; "
            "Mahabir Tyagi — ‘safety-valve’; Ambedkar admitted misuse for political purposes is possible.\n\n"
            "## 44th Amendment = Emergency firewall\n\n"
            "- Written Cabinet recommendation for NE\n"
            "- Approval window cut to **1 month**; **special majority**; 6-month renewals\n"
            "- Lok Sabha can force NE revocation; 1/10 → sitting in 14 days\n"
            "- ‘Armed rebellion’ replaces ‘internal disturbance’\n"
            "- Art. 19 suspends only in External Emergency; Arts **20 & 21** protected\n"
            "- Judicial review of NE / PR / FE satisfaction restored\n"
            "- PR beyond 1 year needs NE + EC certificate\n\n"
            "## Articles at a glance (Table 17.2)\n\n"
            "| Art. | Subject |\n"
            "|---|---|\n"
            "| 352 | Proclamation of Emergency |\n"
            "| 353 | Effect of Proclamation |\n"
            "| 354 | Revenue distribution during NE |\n"
            "| 355 | Union’s duty to protect states |\n"
            "| 356 | Failure of constitutional machinery |\n"
            "| 357 | Legislative powers under 356 |\n"
            "| 358 | Suspension of Art. 19 |\n"
            "| 359 | Suspension of enforcement of Part III rights |\n"
            "| 359A | Punjab application (repealed) |\n"
            "| 360 | Financial Emergency |"
        ),
        "articles": [
            (
                "Articles 352–360",
                "Full Part XVIII map — National, State, and Financial emergencies.",
            ),
            (
                "44th Amendment",
                "Core post-1975 safeguards against misuse of Emergency powers.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "emg-critique-compare",
                "type": "comparison",
                "title": "Critics vs protagonists",
                "columns": [
                    {
                        "id": "critics",
                        "heading": "Critics",
                        "points": [
                            "Kamath — totalitarian / police state fear",
                            "K.T. Shah — reaction and retrogression",
                            "T.T. Krishnamachari — constitutional dictatorship",
                            "Kunzru — threat to state financial autonomy",
                        ],
                    },
                    {
                        "id": "pros",
                        "heading": "Protagonists",
                        "points": [
                            "Alladi — ‘life-breath of the Constitution’",
                            "Tyagi — ‘safety-valve’ for the Constitution",
                            "Ambedkar — needed, but misuse possible",
                            "Design: federal in peace, unitary in crisis",
                        ],
                    },
                ],
            },
            {
                "id": "emg-arts-pillars",
                "type": "pillars",
                "title": "Articles 352–360 (scan)",
                "items": [
                    {
                        "id": "a352",
                        "articles": "352",
                        "label": "Proclamation of Emergency",
                        "slug": "emg-national-grounds",
                        "detail": "National Emergency grounds and process.",
                        "tone": "teal",
                    },
                    {
                        "id": "a356",
                        "articles": "356",
                        "label": "President’s Rule",
                        "slug": "emg-presidents-rule",
                        "detail": "Failure of constitutional machinery.",
                        "tone": "olive",
                    },
                    {
                        "id": "a358",
                        "articles": "358·359",
                        "label": "FR suspension",
                        "slug": "emg-358-vs-359",
                        "detail": "Art. 19 vs enforcement of other rights.",
                        "tone": "gold",
                    },
                    {
                        "id": "a360",
                        "articles": "360",
                        "label": "Financial Emergency",
                        "slug": "emg-financial",
                        "detail": "Stability / credit — never used.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "emg-44-tip",
                "type": "callout",
                "tone": "tip",
                "title": "44th = Emergency firewall",
                "body": (
                    "If a question asks how Emergency misuse was curbed after 1975, start with the 44th pack: "
                    "Cabinet writing, clocks, majorities, armed rebellion, 20–21, and judicial review."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "emg-three-types"),
    (HUB_SLUG, "parent", "emg-national-grounds"),
    (HUB_SLUG, "parent", "emg-national-procedure"),
    (HUB_SLUG, "parent", "emg-national-effects"),
    (HUB_SLUG, "parent", "emg-358-vs-359"),
    (HUB_SLUG, "parent", "emg-national-history"),
    (HUB_SLUG, "parent", "emg-presidents-rule"),
    (HUB_SLUG, "parent", "emg-352-vs-356"),
    (HUB_SLUG, "parent", "emg-bommai"),
    (HUB_SLUG, "parent", "emg-financial"),
    (HUB_SLUG, "parent", "emg-criticism-safeguards"),
    ("emg-three-types", "related", "emg-national-grounds"),
    ("emg-national-grounds", "related", "emg-national-procedure"),
    ("emg-national-procedure", "related", "emg-national-effects"),
    ("emg-national-effects", "related", "emg-358-vs-359"),
    ("emg-national-grounds", "related", "emg-national-history"),
    ("emg-presidents-rule", "related", "emg-352-vs-356"),
    ("emg-national-grounds", "related", "emg-352-vs-356"),
    ("emg-presidents-rule", "related", "emg-bommai"),
    ("emg-bommai", "related", "emg-352-vs-356"),
    ("emg-three-types", "related", "emg-financial"),
    ("emg-criticism-safeguards", "related", "emg-national-history"),
    ("sf-emergency", "related", HUB_SLUG),
    (HUB_SLUG, "related", "article-356"),
    ("emg-bommai", "related", "article-356"),
    ("emg-bommai", "related", "basic-structure"),
    ("federalism", "related", HUB_SLUG),
    ("parliamentary-system", "related", HUB_SLUG),
]

SAMPLE_PYQS = [
    (
        2018,
        "Which of the following are not necessarily the consequences of the proclamation of the President’s rule in a State?",
        "Fundamental Rights of citizens are not affected under Art. 356 (unlike National Emergency).",
        ["emg-presidents-rule", "emg-352-vs-356"],
    ),
    (
        2019,
        "With reference to National Emergency, which statement about Articles 358 and 359 is correct?",
        "Art. 358 automatically suspends Art. 19 in External Emergency; Art. 359 suspends enforcement of specified rights by order — Arts 20 & 21 protected.",
        ["emg-358-vs-359"],
    ),
    (
        2017,
        "Which of the following is/are among the Fundamental Duties of citizens laid down in the Indian Constitution? (linked theme often paired with Emergency FR questions)",
        "Use to contrast: FR may be restricted in Emergency; duties remain a separate Part IVA theme.",
        ["emg-358-vs-359", "emg-criticism-safeguards"],
    ),
    (
        2021,
        "Consider statements on proclamation of Emergency under Article 352 — parliamentary approval timeline and majority.",
        "Approved by both Houses within one month by special majority; continuance every six months.",
        ["emg-national-procedure"],
    ),
    (
        2015,
        "The Financial Emergency has been declared how many times so far?",
        "Never — Art. 360 has not been invoked (1991 crisis was a near-miss, not a proclamation).",
        ["emg-financial"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Minerva Mills v. Union of India",
        "slug": "minerva-mills",
        "parties": "Minerva Mills Ltd. v. Union of India",
        "year": 1980,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Among other holdings, clarified that a National Emergency proclamation "
            "can be challenged for malafide or extraneous / absurd satisfaction."
        ),
        "holding": (
            "Proclamation of National Emergency is open to judicial review on grounds of "
            "malafide, wholly extraneous or irrelevant facts, or absurd/perverse satisfaction."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "emg-national-grounds",
            "emg-criticism-safeguards",
        ],
    },
    {
        "title": "S.R. Bommai v. Union of India",
        "slug": "sr-bommai",
        "parties": "S.R. Bommai v. Union of India",
        "year": 1994,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Landmark ruling on Art. 356 — judicial review, floor test, suspend-before-dissolve, "
            "and secularism as a basic feature."
        ),
        "holding": (
            "Art. 356 proclamations are justiciable; assembly should not be dissolved before "
            "parliamentary approval; majority is tested on the floor of the House."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "emg-bommai",
            "emg-presidents-rule",
            "emg-352-vs-356",
        ],
    },
]

AMENDMENTS = [
    {
        "number": 38,
        "year": 1975,
        "title": "Thirty-eighth Amendment",
        "summary": (
            "Emergency-era changes — made presidential satisfaction for NE / PR / FE "
            "final and conclusive; allowed multiple NE proclamations."
        ),
        "effect": (
            "Attempted to oust judicial review of Emergency satisfaction "
            "(later rolled back by the 44th Amendment)."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "emg-national-grounds",
            "emg-bommai",
            "emg-financial",
        ],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Enabled limiting National Emergency to a part of India; temporarily raised "
            "President’s Rule initial approved period (later restored to six months by 44th)."
        ),
        "effect": (
            "Territorial flexibility for NE; also extended some NE executive/legislative "
            "consequences to other states."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "emg-national-grounds",
            "emg-national-effects",
            "emg-presidents-rule",
        ],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": (
            "Post-Emergency firewall — Cabinet writing, shorter approval, special majority, "
            "LS revocation, armed rebellion wording, Art. 19/20/21 shields, judicial review restored."
        ),
        "effect": "Core safeguards against 1975-style misuse of Emergency provisions.",
        "concept_slugs": [
            HUB_SLUG,
            "emg-national-grounds",
            "emg-national-procedure",
            "emg-358-vs-359",
            "emg-presidents-rule",
            "emg-criticism-safeguards",
            "emg-national-history",
        ],
    },
    {
        "number": 68,
        "year": 1991,
        "title": "Sixty-eighth Amendment",
        "summary": (
            "Allowed President’s Rule in Punjab (imposed May 1987) to continue for five years "
            "— an exceptional extension beyond the normal three-year cap."
        ),
        "effect": "State-specific exception to the three-year outer limit for Art. 356.",
        "concept_slugs": [HUB_SLUG, "emg-presidents-rule"],
    },
]


class Command(BaseCommand):
    help = "Seed Emergency Provisions chapter (Laxmikanth Ch.17)."

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
                "title": "Emergency Provisions",
                "sort_order": 5,
                "book_ref": "Laxmikanth 8th Ed, Ch. 17",
                "summary": (
                    "Visual revision of Ch.17 — Part XVIII Arts 352–360; national, "
                    "President’s Rule, and financial emergencies; 44th shields and Bommai."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Emergency Provisions",
                "summary": (
                    "Part XVIII — National Emergency, President’s Rule, and Financial Emergency; "
                    "federal → unitary switch with 44th Amendment safeguards."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **federal → unitary switch** mental model, then "
                    "**Three types** → **National grounds / procedure / effects** → "
                    "**358 vs 359**. Cover **President’s Rule**, the **352 vs 356** table, "
                    "**Bommai**, and **Financial Emergency**. Finish with **Criticism & 44th firewall**. "
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
            ref="Laxmikanth Ch. 17",
            excerpt=(
                "Emergency Provisions — Part XVIII Arts 352–360; national, state, "
                "and financial emergencies."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 352 · 356 · 360",
            excerpt="National Emergency, President’s Rule, and Financial Emergency.",
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="44th Amendment",
            excerpt="Post-1975 firewall against misuse of Emergency powers.",
            sort_order=2,
        )

        emg_slugs = set(by_slug.keys())
        related_outside = {
            "sf-emergency",
            "article-356",
            "basic-structure",
            "federalism",
            "parliamentary-system",
        }
        ConceptEdge.objects.filter(
            source__slug__in=emg_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=emg_slugs | related_outside).delete()

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
                by_slug[s] for s in case_data["concept_slugs"] if s in by_slug
            ]
            if concepts:
                existing = list(case.concepts.all())
                case.concepts.set({*existing, *concepts})

        for amd_data in AMENDMENTS:
            # Do not overwrite shared amendment blurbs owned by other chapter seeds.
            amendment = ConstitutionalAmendment.objects.filter(
                academy=academy, number=amd_data["number"]
            ).first()
            if amendment is None:
                payload = {k: v for k, v in amd_data.items() if k != "concept_slugs"}
                amendment = ConstitutionalAmendment.objects.create(
                    academy=academy, **payload
                )
            concepts = [
                by_slug[s] for s in amd_data["concept_slugs"] if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        from subjects.models import Section

        section = Section.objects.filter(
            subject=subject, slug="system-of-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Emergency Provisions chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments linked."
            )
        )
