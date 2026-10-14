"""Seed Laxmikanth Ch.33 State Legislature (visual revision, pp. 480–507)."""

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

HUB_SLUG = "state-legislature"
CHAPTER_SLUG = "state-legislature"

ENTRY_PILLARS = [
    {
        "id": "org",
        "articles": "Art. 168–169",
        "label": "Organisation & Art. 169",
        "slug": "sl-organisation",
        "detail": "Unicameral/bicameral; ATUBMK six; create/abolish Council.",
        "tone": "teal",
    },
    {
        "id": "assembly",
        "articles": "Art. 170",
        "label": "Legislative Assembly",
        "slug": "sl-assembly",
        "detail": "60–500; delimitation freeze; SC/ST to 2030; Anglo-Indian ended.",
        "tone": "olive",
    },
    {
        "id": "council",
        "articles": "Art. 171",
        "label": "Legislative Council",
        "slug": "sl-council",
        "detail": "Max ⅓ of Assembly; 3-1-1-3-Rest composition; ⅚ + ⅙.",
        "tone": "gold",
    },
    {
        "id": "duration",
        "articles": "Art. 172",
        "label": "Duration of Houses",
        "slug": "sl-duration",
        "detail": "Assembly 5 yrs; Council permanent — ⅓ every 2 yrs.",
        "tone": "orange",
    },
    {
        "id": "membership",
        "articles": "Art. 173 / 190–192",
        "label": "Membership",
        "slug": "sl-membership",
        "detail": "Age 25/30; disqualifications; defection; vacation.",
        "tone": "terracotta",
    },
    {
        "id": "officers",
        "articles": "Art. 178–185",
        "label": "Presiding Officers",
        "slug": "sl-presiding-officers",
        "detail": "Speaker/Chairman; Money Bill certification; 10th Schedule.",
        "tone": "maroon",
    },
    {
        "id": "sessions",
        "articles": "Art. 174 / 189",
        "label": "Sessions & Quorum",
        "slug": "sl-sessions",
        "detail": "Summon/prorogue/dissolve; bill lapse rules; quorum.",
        "tone": "teal",
    },
    {
        "id": "ordinary",
        "articles": "Art. 196–197 / 200–201",
        "label": "Ordinary Bills",
        "slug": "sl-ordinary-bills",
        "detail": "4-month Council delay; no joint sitting; assent paths.",
        "tone": "olive",
    },
    {
        "id": "money",
        "articles": "Art. 198–199",
        "label": "Money Bills",
        "slug": "sl-money-bills",
        "detail": "Assembly only; 14 days; cannot return Money Bill.",
        "tone": "gold",
    },
    {
        "id": "reserved",
        "articles": "Art. 200–201",
        "label": "Reserved Bills",
        "slug": "sl-reserved-bills",
        "detail": "Sarkaria three baskets; President’s consideration.",
        "tone": "orange",
    },
    {
        "id": "budget",
        "articles": "Art. 202–207",
        "label": "Budget & Finance",
        "slug": "sl-budget-finance",
        "detail": "AFS → estimates → Appropriation; Financial Bills.",
        "tone": "terracotta",
    },
    {
        "id": "vs-parl",
        "articles": "Table 33.1",
        "label": "vs Parliament",
        "slug": "sl-vs-parliament",
        "detail": "Joint sitting? Override? Deadlock clocks.",
        "tone": "maroon",
    },
    {
        "id": "position",
        "articles": "Ch.33",
        "label": "Council Position",
        "slug": "sl-council-position",
        "detail": "Weaker than RS; utility vs criticism.",
        "tone": "teal",
    },
    {
        "id": "privileges",
        "articles": "Art. 194",
        "label": "Privileges",
        "slug": "sl-privileges",
        "detail": "Collective & individual; not for Governor.",
        "tone": "olive",
    },
    {
        "id": "refs",
        "articles": "Art. 168–212",
        "label": "Articles at a Glance",
        "slug": "sl-reference-tables",
        "detail": "Article map + Art. 169 Acts + bicameral seats.",
        "tone": "gold",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "sl-mental-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "State mini-Parliament",
        "topic_label": "State Legislature",
        "subject_label": "Arts 168–212 · Part VI",
        "relation_label": "Helps you avoid",
        "protects_from": [
            "Assuming joint sitting at state level",
            "Equating Council with Rajya Sabha power",
            "Mixing who decides which disqualification",
            "Forgetting Council is only a delaying chamber",
        ],
        "insight": (
            "Governor + Vidhan Sabha (+ Vidhan Parishad where it exists). "
            "The popular House dominates — Council delays, Assembly decides."
        ),
    },
    {
        "id": "sl-entry-pillars",
        "type": "pillars",
        "title": "Fifteen revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "sl-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Prelims killers",
        "body": (
            "No joint sitting in states. Ordinary bill: Council delay max **4 months** (3+1). "
            "Money Bill: **14 days**. Bicameral mnemonic **ATUBMK**. "
            "Art. 169 Act ≠ Art. 368 amendment."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Organisation & Art. 169",
        "slug": "sl-organisation",
        "sort_order": 1,
        "summary": (
            "No uniform pattern — most states unicameral; six bicameral. "
            "Art. 169 lets Parliament create or abolish a Council."
        ),
        "body": (
            "## Organisation of state legislature\n\n"
            "Arts **168–212** (Part VI) deal with organisation, composition, duration, officers, "
            "procedure, privileges and powers — parallel to Parliament, with key differences.\n\n"
            "- **Unicameral (most states):** Governor + Legislative Assembly.\n"
            "- **Bicameral (six):** Governor + Legislative Council (Vidhan Parishad) + "
            "Legislative Assembly (Vidhan Sabha).\n\n"
            "### Bicameral mnemonic — ATUBMK\n"
            "Andhra Pradesh, Telangana, Uttar Pradesh, Bihar, Maharashtra, Karnataka.\n\n"
            "- J&K Legislative Council abolished by the **J&K Reorganisation Act, 2019**.\n"
            "- Tamil Nadu Legislative Council Act, **2010** not enforced (Assembly later sought abolition).\n"
            "- **7th Amendment** provided for a Council in MP — Presidential notification never issued.\n\n"
            "### Art. 169 — create / abolish Council\n"
            "1. State Assembly passes a resolution by **special majority** "
            "(majority of total membership **and** ≥⅔ of members present and voting).\n"
            "2. Parliament passes an Act by **simple majority**.\n"
            "3. Not deemed an amendment under Art. **368**.\n\n"
            "Example: AP Council created 1957 → abolished 1985 → revived 2007 (Act 2005)."
        ),
        "articles": [
            ("Art. 168", "Constitution of Legislatures in states."),
            (
                "Art. 169",
                "Abolition or creation of Legislative Councils — Assembly resolution + Parliament Act.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "sl-org-tree",
                "type": "tree",
                "title": "What is the state legislature?",
                "root": {
                    "id": "leg",
                    "label": "State Legislature",
                    "detail": "Art. 168",
                    "children": [
                        {
                            "id": "gov",
                            "label": "Governor",
                            "detail": "Integral part (no privileges of the House)",
                        },
                        {
                            "id": "vs",
                            "label": "Vidhan Sabha",
                            "detail": "Popular House — always present",
                            "slug": "sl-assembly",
                        },
                        {
                            "id": "vp",
                            "label": "Vidhan Parishad",
                            "detail": "Only in ATUBMK six",
                            "slug": "sl-council",
                        },
                    ],
                },
            },
            {
                "id": "sl-org-timeline",
                "type": "timeline",
                "title": "Art. 169 Acts — create / abolish",
                "events": [
                    {
                        "id": "e1",
                        "year": 1969,
                        "label": "WB & Punjab abolish",
                        "detail": "Legislative Council (Abolition) Acts, 1969.",
                    },
                    {
                        "id": "e2",
                        "year": 1985,
                        "label": "AP abolish",
                        "detail": "Andhra Pradesh Legislative Council (Abolition) Act.",
                    },
                    {
                        "id": "e3",
                        "year": 1986,
                        "label": "TN abolish",
                        "detail": "Tamil Nadu Legislative Council (Abolition) Act.",
                    },
                    {
                        "id": "e4",
                        "year": 2005,
                        "label": "AP revive",
                        "detail": "Andhra Pradesh Legislative Council Act, 2005 (revived 2007).",
                    },
                    {
                        "id": "e5",
                        "year": 2010,
                        "label": "TN Act (not enforced)",
                        "detail": "Create Act passed; Assembly later sought abolition before enforcement.",
                    },
                    {
                        "id": "e6",
                        "year": 2019,
                        "label": "J&K Council ends",
                        "detail": "Reorganisation Act abolished the erstwhile Council.",
                    },
                ],
            },
            {
                "id": "sl-org-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Art. 169 Act is ordinary legislation (simple majority in Parliament) — "
                    "not a constitutional amendment under Art. 368. "
                    "Assembly side needs special majority first."
                ),
            },
        ],
    },
    {
        "title": "Legislative Assembly",
        "slug": "sl-assembly",
        "sort_order": 2,
        "summary": (
            "Directly elected popular House — strength generally 60–500, with special minima; "
            "delimitation freeze and reservation timelines matter for prelims."
        ),
        "body": (
            "## Composition of Assembly (Art. 170)\n\n"
            "- Direct election on universal adult franchise.\n"
            "- **Maximum 500, minimum 60** (population-linked).\n"
            "- Special minima: Arunachal/Sikkim/Goa **30**; Mizoram **40**; Nagaland **46**.\n"
            "- Some members in Sikkim and Nagaland also elected **indirectly**.\n\n"
            "### Constituencies & delimitation\n"
            "- Uniform ratio of population to seats across the state.\n"
            "- After each census: readjust seats and constituencies (Parliament fixes authority — "
            "Delimitation Commission Acts 1952, 1962, 1972, 2002).\n"
            "- **42nd** froze seats/constituencies at 1971 level till 2000; **84th** extended freeze "
            "to **2026** (encourage population control).\n"
            "- **84th** allowed rationalisation on 1991 figures; **87th** switched to **2001** census "
            "boundaries **without** changing total seats.\n\n"
            "### Reservation & Anglo-Indians\n"
            "- SC/ST assembly seats by population ratio — extended till **2030** (**104th**).\n"
            "- Governor’s Anglo-Indian nomination ended **25 Jan 2020** (**104th**; last extension "
            "was **95th** up to 2020)."
        ),
        "articles": [
            ("Art. 170", "Composition of the Legislative Assemblies."),
            ("104th Amendment", "SC/ST reservation till 2030; Anglo-Indian nomination discontinued."),
        ],
        "visual_blocks": [
            {
                "id": "sl-asm-compare",
                "type": "comparison",
                "title": "Strength floors",
                "columns": [
                    {
                        "id": "general",
                        "heading": "General rule",
                        "points": ["Minimum 60", "Maximum 500", "Direct election + UAF"],
                    },
                    {
                        "id": "special",
                        "heading": "Special minima",
                        "points": [
                            "AP / Sikkim / Goa → 30",
                            "Mizoram → 40",
                            "Nagaland → 46",
                            "Sikkim & Nagaland: some indirect seats",
                        ],
                    },
                ],
            },
            {
                "id": "sl-asm-timeline",
                "type": "timeline",
                "title": "Delimitation, reservation, Anglo-Indian",
                "events": [
                    {
                        "id": "t1",
                        "year": 1976,
                        "label": "42nd freeze",
                        "detail": "Seats & constituencies frozen at 1971 level till 2000.",
                    },
                    {
                        "id": "t2",
                        "year": 2001,
                        "label": "84th to 2026",
                        "detail": "Freeze extended; rationalisation on 1991 figures allowed.",
                    },
                    {
                        "id": "t3",
                        "year": 2003,
                        "label": "87th → 2001 census",
                        "detail": "Boundaries on 2001 data; total seats unchanged.",
                    },
                    {
                        "id": "t4",
                        "year": 2019,
                        "label": "104th Amendment",
                        "detail": "SC/ST reservation to 2030; Anglo-Indian nomination ends Jan 2020.",
                    },
                ],
            },
            {
                "id": "sl-asm-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims one-liner",
                "body": (
                    "Seat totals frozen till the first census after 2026; "
                    "constituency maps already use 2001 population (87th)."
                ),
            },
        ],
    },
    {
        "title": "Legislative Council",
        "slug": "sl-council",
        "sort_order": 3,
        "summary": (
            "Indirectly elected second chamber — max one-third of Assembly, min 40; "
            "five electoral streams plus Governor nominees."
        ),
        "body": (
            "## Composition of Council (Art. 171)\n\n"
            "- **Maximum:** one-third of the Assembly’s total strength.\n"
            "- **Minimum:** 40.\n"
            "- Actual strength fixed by **Parliament** (keeps Assembly predominant).\n\n"
            "### Mnemonic — 3-1-1-3-Rest\n"
            "Of total members:\n"
            "1. **1/3** — elected by local bodies (municipalities, district boards, etc.).\n"
            "2. **1/12** — graduates of 3 years’ standing residing in the state.\n"
            "3. **1/12** — teachers of 3 years’ standing (not below secondary).\n"
            "4. **1/3** — elected by Assembly members from persons who are **not** MLAs.\n"
            "5. **Remainder (~1/6)** — nominated by Governor "
            "(literature, science, art, cooperative movement, social service).\n\n"
            "**5/6 indirectly elected + 1/6 nominated.** Election by PR with STV.\n\n"
            "The Art. 171 scheme is **tentative** — Parliament may modify/replace it "
            "(has not done so yet)."
        ),
        "articles": [
            ("Art. 171", "Composition of the Legislative Councils."),
        ],
        "visual_blocks": [
            {
                "id": "sl-council-pillars",
                "type": "pillars",
                "title": "Five streams (3-1-1-3-Rest)",
                "items": [
                    {
                        "id": "local",
                        "articles": "1/3",
                        "label": "Local bodies",
                        "slug": "sl-council",
                        "detail": "Municipalities, district boards, etc.",
                        "tone": "teal",
                    },
                    {
                        "id": "grad",
                        "articles": "1/12",
                        "label": "Graduates",
                        "slug": "sl-council",
                        "detail": "3 years’ standing; resident in state.",
                        "tone": "olive",
                    },
                    {
                        "id": "teach",
                        "articles": "1/12",
                        "label": "Teachers",
                        "slug": "sl-council",
                        "detail": "3 years’ standing; not below secondary.",
                        "tone": "gold",
                    },
                    {
                        "id": "mla",
                        "articles": "1/3",
                        "label": "By MLAs",
                        "slug": "sl-council",
                        "detail": "Elect non-MLAs to the Council.",
                        "tone": "orange",
                    },
                    {
                        "id": "nom",
                        "articles": "~1/6",
                        "label": "Governor nominees",
                        "slug": "sl-council",
                        "detail": "Literature, science, art, co-ops, social service.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "sl-council-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": (
                    "5/6 elected + 1/6 nominated. Nomination fields: "
                    "**L-S-A-C-S** — Literature, Science, Art, Cooperatives, Social service."
                ),
            },
        ],
    },
    {
        "title": "Duration of Houses",
        "slug": "sl-duration",
        "sort_order": 4,
        "summary": (
            "Assembly is a 5-year House (dissolvable); Council is a permanent chamber "
            "with staggered retirement."
        ),
        "body": (
            "## Duration (Art. 172)\n\n"
            "### Assembly\n"
            "- Normal term **5 years** from first meeting after general election — "
            "expiry = automatic dissolution.\n"
            "- Governor may dissolve earlier for fresh elections.\n"
            "- During **national emergency**, Parliament may extend term by **1 year at a time**; "
            "extension cannot continue beyond **6 months** after emergency ends.\n\n"
            "### Council\n"
            "- **Continuing chamber** — not subject to dissolution.\n"
            "- **One-third** of members retire every **second year**; member’s term **6 years**.\n"
            "- Vacancies filled by fresh elections/nominations; retiring members eligible again "
            "any number of times."
        ),
        "articles": [
            ("Art. 172", "Duration of State Legislatures."),
        ],
        "visual_blocks": [
            {
                "id": "sl-duration-compare",
                "type": "comparison",
                "title": "Assembly vs Council (≈ LS vs RS)",
                "columns": [
                    {
                        "id": "asm",
                        "heading": "Legislative Assembly",
                        "points": [
                            "Not a continuing chamber",
                            "5-year normal term",
                            "Governor may dissolve early",
                            "Emergency extension: 1 year at a time; ≤6 months after end",
                        ],
                    },
                    {
                        "id": "coun",
                        "heading": "Legislative Council",
                        "points": [
                            "Permanent / continuing",
                            "Not dissolved",
                            "⅓ retire every 2 years",
                            "Individual term 6 years; re-election allowed",
                        ],
                    },
                ],
            },
            {
                "id": "sl-duration-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Trap",
                "body": (
                    "Only the Assembly dissolves. A bill pending only in the Council "
                    "(never passed by Assembly) does **not** lapse on dissolution — see Sessions."
                ),
            },
        ],
    },
    {
        "title": "Membership",
        "slug": "sl-membership",
        "sort_order": 5,
        "summary": (
            "Qualifications (25/30), constitutional and RPA disqualifications, oath, "
            "vacation of seats, and Tenth Schedule."
        ),
        "body": (
            "## Qualifications (Art. 173 + RPA 1951)\n\n"
            "- Citizen of India; oath/affirmation before EC-authorised person "
            "(faith to Constitution; sovereignty & integrity).\n"
            "- Age: Assembly **≥25**; Council **≥30**.\n"
            "- RPA: elector for an assembly constituency in the state "
            "(Council nominee must be a resident); SC/ST for reserved seats "
            "(may also contest unreserved).\n\n"
            "## Disqualifications\n\n"
            "**Constitution:** office of profit (except minister/exempted), unsound mind, "
            "undischarged insolvent, foreign citizenship/allegiance, or under parliamentary law.\n\n"
            "**RPA highlights:** corrupt practices; conviction with ≥2 years’ imprisonment "
            "(preventive detention ≠ disqualification); election-expense default; government "
            "contracts; certain corporation offices; dismissal for corruption/disloyalty; "
            "enmity/bribery convictions; social crimes (untouchability, dowry, sati).\n\n"
            "- Ordinary disqualification question → **Governor decides after EC opinion** (Art. 192).\n"
            "- **Defection (10th Schedule)** → Speaker (Assembly) / Chairman (Council). "
            "**Kihoto Hollohan (1992):** decision subject to judicial review.\n\n"
            "## Oath, penalty, vacation\n\n"
            "- Oath before Governor or nominee before taking seat (Art. 188).\n"
            "- Penalty **₹500/day** for sitting/voting without oath or while disqualified (Art. 193).\n"
            "- Vacate: double membership; disqualification; resignation accepted; "
            "**60 days** continuous absence without permission; election void; expulsion; "
            "elected President/VP; appointed Governor."
        ),
        "articles": [
            ("Art. 173", "Qualification for membership of the State Legislature."),
            ("Art. 190–193", "Vacation, disqualifications, decision thereon, penalty."),
            ("Tenth Schedule", "Disqualification on ground of defection."),
        ],
        "visual_blocks": [
            {
                "id": "sl-memb-compare",
                "type": "comparison",
                "title": "Who decides disqualification?",
                "columns": [
                    {
                        "id": "gov",
                        "heading": "Governor (+ EC)",
                        "points": [
                            "Constitutional / RPA disqualifications",
                            "Must obtain EC opinion and act accordingly",
                            "Art. 192",
                        ],
                    },
                    {
                        "id": "spk",
                        "heading": "Speaker / Chairman",
                        "points": [
                            "Tenth Schedule (defection)",
                            "Not the Governor",
                            "Judicially reviewable (Kihoto Hollohan)",
                        ],
                    },
                ],
            },
            {
                "id": "sl-memb-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Age trap",
                "body": "Assembly 25 · Council 30 — same as Lok Sabha / Rajya Sabha pattern.",
            },
        ],
    },
    {
        "title": "Presiding Officers",
        "slug": "sl-presiding-officers",
        "sort_order": 6,
        "summary": (
            "Speaker and Deputy Speaker of the Assembly; Chairman and Deputy Chairman "
            "of the Council — election, removal, and special Speaker powers."
        ),
        "body": (
            "## Speaker & Deputy Speaker (Assembly)\n\n"
            "- Elected by Assembly from among its members.\n"
            "- Vacate if: cease to be member; resign (to each other); removed by resolution of "
            "**majority of all the then members** (14 days’ notice).\n\n"
            "### Speaker’s core powers\n"
            "1. Maintain order and decorum.\n"
            "2. Final interpreter of Constitution / Rules / Procedure (in House context).\n"
            "3. Adjourn or suspend for want of quorum.\n"
            "4. No first vote; **casting vote** on equality.\n"
            "5. Allow secret sitting on Leader of House request.\n"
            "6. Decide whether a bill is a **Money Bill** — decision **final**.\n"
            "7. Decide **10th Schedule** disqualification of MLAs.\n"
            "8. Appoint committee chairpersons and supervise committees.\n\n"
            "## Chairman & Deputy Chairman (Council)\n\n"
            "- Parallel election / vacation / removal rules.\n"
            "- Powers ≈ Speaker **except** Money Bill certification "
            "(that special power belongs to the Speaker alone)."
        ),
        "articles": [
            ("Art. 178–181", "Speaker and Deputy Speaker of the Legislative Assembly."),
            ("Art. 182–185", "Chairman and Deputy Chairman of the Legislative Council."),
        ],
        "visual_blocks": [
            {
                "id": "sl-officers-compare",
                "type": "comparison",
                "title": "Speaker vs Chairman",
                "columns": [
                    {
                        "id": "spk",
                        "heading": "Speaker (Assembly)",
                        "points": [
                            "Presides over popular House",
                            "Certifies Money Bills — final",
                            "10th Schedule for MLAs",
                            "Casting vote; quorum control",
                        ],
                    },
                    {
                        "id": "ch",
                        "heading": "Chairman (Council)",
                        "points": [
                            "Presides over Council",
                            "No Money Bill certification",
                            "10th Schedule for MLCs",
                            "Otherwise largely parallel powers",
                        ],
                    },
                ],
            },
            {
                "id": "sl-officers-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Removal majority",
                "body": (
                    "Removal needs majority of **all the then members** of the House — "
                    "stricter than ordinary present-and-voting majority."
                ),
            },
        ],
    },
    {
        "title": "Sessions, Quorum & Language",
        "slug": "sl-sessions",
        "sort_order": 7,
        "summary": (
            "Summoning, adjournment, prorogation, dissolution and bill-lapse rules; "
            "quorum; language; rights of ministers and Advocate-General."
        ),
        "body": (
            "## Sessions (Art. 174)\n\n"
            "- **Summon:** Governor; gap between sessions ≤ **6 months** (≥2 meetings a year).\n"
            "- **Adjournment / sine die:** presiding officer (suspends a sitting).\n"
            "- **Prorogation:** Governor (ends a session); can also prorogue a sitting House.\n"
            "- **Dissolution:** only Assembly; ends the House’s life → fresh elections.\n\n"
            "### Bill lapse on dissolution (high yield)\n"
            "1. Bill pending in Assembly → **lapses**.\n"
            "2. Passed by Assembly, pending in Council → **lapses**.\n"
            "3. Pending in Council, **not** passed by Assembly → **does not lapse**.\n"
            "4. Passed by House(s), pending Governor/President assent → **does not lapse**.\n"
            "5. Returned by President for reconsideration → **does not lapse**.\n\n"
            "### Quorum & voting\n"
            "- Quorum: **10 members or 1/10** of total membership (incl. chair), whichever greater.\n"
            "- Decisions: majority of present and voting (ex-chair); casting vote on equality.\n\n"
            "### Language (Art. 210) & ministers/AG (Art. 177)\n"
            "- Floor languages: official language(s) of state / Hindi / English; mother tongue with permission.\n"
            "- English continuance after 1965: state legislature decides "
            "(HP/Manipur/Meghalaya/Tripura: 25 yrs; AP/Goa/Mizoram: 40 yrs).\n"
            "- Ministers & Advocate-General may speak in either House/committees — **no vote**. "
            "Non-member minister may participate in both Houses."
        ),
        "articles": [
            ("Art. 174", "Sessions of the State Legislature, prorogation and dissolution."),
            ("Art. 177", "Rights of Ministers and Advocate-General as respects the Houses."),
            ("Art. 189", "Voting in Houses; quorum."),
            ("Art. 210", "Language to be used in the Legislature."),
        ],
        "visual_blocks": [
            {
                "id": "sl-sessions-flow",
                "type": "flowchart",
                "title": "Does the bill lapse on Assembly dissolution?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Where is the bill?",
                        "detail": "Match status → lapse rule.",
                        "options": [
                            {"label": "Pending in Assembly", "next": "lapse"},
                            {"label": "Passed Assembly, pending Council", "next": "lapse"},
                            {"label": "Only in Council (never passed Assembly)", "next": "keep"},
                            {"label": "Passed; awaiting assent / President return", "next": "keep"},
                        ],
                    },
                    {
                        "id": "lapse",
                        "label": "Lapses",
                        "detail": "Must start afresh in the new Assembly.",
                    },
                    {
                        "id": "keep",
                        "label": "Does not lapse",
                        "detail": "Council-only pending bills and assent/reconsideration stages survive.",
                    },
                ],
            },
            {
                "id": "sl-sessions-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Adjourn ≠ Prorogue ≠ Dissolve",
                "body": (
                    "Adjournment = sitting (presiding officer). "
                    "Prorogation = session (Governor). "
                    "Dissolution = life of Assembly only."
                ),
            },
        ],
    },
    {
        "title": "Ordinary Bills",
        "slug": "sl-ordinary-bills",
        "sort_order": 8,
        "summary": (
            "Three readings; Council can delay up to four months; Assembly overrides; "
            "no joint sitting; Governor/President assent paths."
        ),
        "body": (
            "## Ordinary bills\n\n"
            "- May originate in **either** House (bicameral); minister or private member.\n"
            "- Three readings in each House; unicameral → straight to Governor after Assembly pass.\n\n"
            "### Council’s four options\n"
            "Pass as is · pass with amendments · reject · take no action.\n\n"
            "- If Council amends / rejects / sits for **3 months**, Assembly may pass again.\n"
            "- Second round: if Council rejects / unacceptable amendments / no pass within "
            "**1 month** → bill deemed passed as Assembly passed it the second time.\n"
            "- Max delay: **3 + 1 = 4 months**. **No joint sitting.**\n"
            "- Bill originating in Council and rejected by Assembly → **dead**.\n\n"
            "### Assent of Governor (Art. 200)\n"
            "1. Assent → Act.\n"
            "2. Withhold → bill ends.\n"
            "3. Return (ordinary bills) — suspensive veto; after re-pass, Governor **must** assent.\n"
            "4. Reserve for President.\n\n"
            "### Assent of President (Art. 201)\n"
            "Assent / withhold / return for reconsideration within **6 months**. "
            "Constitution is silent on whether President must assent after re-passage."
        ),
        "articles": [
            ("Art. 196", "Provisions as to introduction and passing of Bills."),
            ("Art. 197", "Restriction on powers of Legislative Council as to Bills other than Money Bills."),
            ("Art. 200", "Assent to Bills (Governor)."),
            ("Art. 201", "Bills reserved for consideration (President)."),
        ],
        "visual_blocks": [
            {
                "id": "sl-ord-flow",
                "type": "flowchart",
                "title": "Ordinary bill in a bicameral state",
                "root": "origin",
                "steps": [
                    {
                        "id": "origin",
                        "label": "Pass originating House (3 readings)",
                        "detail": "Either House may start an ordinary bill.",
                        "options": [{"label": "Send to other House", "next": "second"}],
                    },
                    {
                        "id": "second",
                        "label": "Second House",
                        "detail": "Pass / amend / reject / delay.",
                        "options": [
                            {"label": "Agree (with/without acceptable amends)", "next": "gov"},
                            {"label": "From Assembly: reject/delay → override path", "next": "override"},
                            {"label": "From Council: Assembly rejects", "next": "dead"},
                        ],
                    },
                    {
                        "id": "override",
                        "label": "Assembly passes 2nd time",
                        "detail": "Council gets ≤1 more month; then deemed passed.",
                        "options": [{"label": "To Governor", "next": "gov"}],
                    },
                    {
                        "id": "dead",
                        "label": "Bill dies",
                        "detail": "Council-origin bill rejected by Assembly ends.",
                    },
                    {
                        "id": "gov",
                        "label": "Governor: assent / withhold / return / reserve",
                        "detail": "After return + re-pass → must assent. Or reserve for President.",
                    },
                ],
            },
            {
                "id": "sl-ord-callout",
                "type": "callout",
                "tone": "trap",
                "title": "No joint sitting",
                "body": (
                    "Unlike Parliament, states have **no** Art. 108-style joint sitting. "
                    "Deadlock → Assembly override (assembly-origin bills only)."
                ),
            },
        ],
    },
    {
        "title": "Money Bills",
        "slug": "sl-money-bills",
        "sort_order": 9,
        "summary": (
            "Special procedure: Assembly-only introduction; Council recommendatory for 14 days; "
            "Governor/President cannot return a Money Bill."
        ),
        "body": (
            "## Money Bills (Art. 198–199)\n\n"
            "- Introduce **only in Assembly**, on **Governor’s recommendation**, by a **minister** "
            "(government bill).\n"
            "- Speaker decides Money Bill character — **final**.\n"
            "- Council **cannot** amend or reject; may only recommend; must return within **14 days**.\n"
            "- Assembly may accept or reject recommendations; if Council misses 14 days → "
            "deemed passed as Assembly passed it.\n\n"
            "### Assent\n"
            "- Governor: assent / withhold / reserve — **cannot return** for reconsideration.\n"
            "- President (if reserved): assent / withhold — **cannot return**.\n"
            "- Normally Governor assents (prior recommendation already given)."
        ),
        "articles": [
            ("Art. 198", "Special procedure in respect of Money Bills."),
            ("Art. 199", "Definition of “Money Bills”."),
        ],
        "visual_blocks": [
            {
                "id": "sl-money-flow",
                "type": "flowchart",
                "title": "Money Bill path",
                "root": "intro",
                "steps": [
                    {
                        "id": "intro",
                        "label": "Assembly + Governor recommendation + minister",
                        "detail": "Cannot start in Council; not by private member.",
                        "options": [{"label": "Passed by Assembly", "next": "council"}],
                    },
                    {
                        "id": "council",
                        "label": "Council ≤14 days (recommend only)",
                        "detail": "No amend/reject power.",
                        "options": [{"label": "Back to Assembly → assent", "next": "assent"}],
                    },
                    {
                        "id": "assent",
                        "label": "Governor / President",
                        "detail": "Assent, withhold, or reserve — never return a Money Bill.",
                    },
                ],
            },
            {
                "id": "sl-money-compare",
                "type": "comparison",
                "title": "Delay power of Council",
                "columns": [
                    {
                        "id": "ord",
                        "heading": "Ordinary bill",
                        "points": ["Max delay 4 months (3+1)", "Assembly can override", "No joint sitting"],
                    },
                    {
                        "id": "mon",
                        "heading": "Money Bill",
                        "points": [
                            "Max delay 14 days",
                            "Recommendatory only",
                            "Cannot amend or reject",
                        ],
                    },
                ],
            },
        ],
    },
    {
        "title": "Bills Reserved for President",
        "slug": "sl-reserved-bills",
        "sort_order": 10,
        "summary": (
            "Sarkaria Commission’s three categories of State bills reserved for "
            "the President’s consideration under Arts 200–201."
        ),
        "body": (
            "## Reserved bills (Art. 200–201)\n\n"
            "Sarkaria Commission (1983–88) classified reserved State bills into three baskets:\n\n"
            "### 1. Must be reserved\n"
            "- Derogate from High Court powers endangering its constitutional position (Art. **200**).\n"
            "- Taxes on water/electricity attracting Art. **288**.\n"
            "- During financial emergency under Art. **360**.\n\n"
            "### 2. May be reserved for specific purposes\n"
            "- Immunity from Arts **14/19**: estates etc. (Art. **31A**); DPSP effect (Art. **31C**).\n"
            "- Concurrent List bill needing President’s assent vs repugnancy (Art. **254**).\n"
            "- Trade/commerce restrictions without prior sanction (Art. **304**).\n\n"
            "### 3. Residual discretion\n"
            "- Other bills Governor may reserve under Art. **200** even if not in the above lists.\n\n"
            "**Mains line:** Reservation is a federal control valve — Centre can check State legislation "
            "that touches courts, concurrent field, or fundamental-rights carve-outs."
        ),
        "articles": [
            ("Art. 200", "Assent to Bills — includes reservation for the President."),
            ("Art. 201", "Bills reserved for consideration of the President."),
        ],
        "visual_blocks": [
            {
                "id": "sl-res-tree",
                "type": "tree",
                "title": "Sarkaria — three baskets",
                "root": {
                    "id": "res",
                    "label": "Reserved State Bills",
                    "detail": "Art. 200–201",
                    "children": [
                        {
                            "id": "must",
                            "label": "Must reserve",
                            "detail": "HC position · Art. 288 · Art. 360",
                        },
                        {
                            "id": "may",
                            "label": "May reserve (purpose)",
                            "detail": "31A / 31C · Art. 254 · Art. 304",
                        },
                        {
                            "id": "resd",
                            "label": "Residual Art. 200",
                            "detail": "Governor’s residual discretion",
                        },
                    ],
                },
            },
            {
                "id": "sl-res-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Mains value-add",
                "body": (
                    "Unlike a returned ordinary bill at state level (Governor must assent after re-pass), "
                    "after President returns a reserved bill and Houses re-pass it, "
                    "the Constitution does **not** say the President must assent."
                ),
            },
        ],
    },
    {
        "title": "Budget & Financial Procedure",
        "slug": "sl-budget-finance",
        "sort_order": 11,
        "summary": (
            "Lean map of Arts 202–207 — annual financial statement through Appropriation "
            "and Financial Bills, parallel to the Union pattern."
        ),
        "body": (
            "## State budget path (Arts 202–207)\n\n"
            "Table 33.3 lists the financial procedure articles. Use this as a revision spine "
            "(mirrors Union budget logic; Governor ≈ President’s financial role):\n\n"
            "1. **Art. 202** — Annual financial statement (State budget) laid each year.\n"
            "2. **Art. 203** — Procedure on estimates; demands for grants voted in **Assembly** "
            "(Council may discuss, not vote — see Council position).\n"
            "3. **Art. 204** — Appropriation Bill to authorise withdrawals from Consolidated Fund.\n"
            "4. **Art. 205** — Supplementary, additional or excess grants.\n"
            "5. **Art. 206** — Votes on account, votes of credit, exceptional grants.\n"
            "6. **Art. 207** — Special provisions as to Financial Bills.\n\n"
            "Money Bills (Art. 198–199) sit inside this financial architecture — "
            "Assembly predominance is absolute on grants and money."
        ),
        "articles": [
            ("Art. 202", "Annual financial statement."),
            ("Art. 203", "Procedure in Legislature with respect to estimates."),
            ("Art. 204", "Appropriation Bills."),
            ("Art. 205–207", "Supplementary grants; votes on account; Financial Bills."),
        ],
        "visual_blocks": [
            {
                "id": "sl-budget-flow",
                "type": "flowchart",
                "title": "State budget → Appropriation",
                "root": "afs",
                "steps": [
                    {
                        "id": "afs",
                        "label": "Annual financial statement (Art. 202)",
                        "detail": "Budget laid before the legislature.",
                        "options": [{"label": "Next", "next": "est"}],
                    },
                    {
                        "id": "est",
                        "label": "Estimates / DFGs (Art. 203)",
                        "detail": "Assembly votes demands; Council discusses only.",
                        "options": [{"label": "Next", "next": "app"}],
                    },
                    {
                        "id": "app",
                        "label": "Appropriation Bill (Art. 204)",
                        "detail": "Legalises withdrawals from Consolidated Fund.",
                        "options": [{"label": "Also know", "next": "extra"}],
                    },
                    {
                        "id": "extra",
                        "label": "205–207 extras",
                        "detail": "Supplementary/excess; votes on account/credit; Financial Bills.",
                    },
                ],
            },
            {
                "id": "sl-budget-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Money Bill vs Financial Bill",
                "body": (
                    "Money Bill = Art. 199 definition + Speaker’s certificate + strict 14-day Council role. "
                    "Financial Bills (Art. 207) have special introduction rules but are not identical "
                    "to Money Bills — don’t conflate in prelims."
                ),
            },
        ],
    },
    {
        "title": "Parliament vs State Legislature",
        "slug": "sl-vs-parliament",
        "sort_order": 12,
        "summary": (
            "High-yield comparison from Table 33.1 — ordinary and Money Bill differences "
            "that UPSC loves to twist."
        ),
        "body": (
            "## Ordinary bills — key contrasts\n\n"
            "| Point | Parliament | State |\n"
            "|---|---|---|\n"
            "| Deadlock clock (2nd House) | 6 months | 3 months |\n"
            "| Joint sitting | Yes (Art. 108) | **No** |\n"
            "| Override | Neither House alone | Assembly can override Council |\n"
            "| Upper-House origin rejected | Needs joint sitting or dies | Assembly reject → **dead** |\n\n"
            "## Money Bills — largely parallel\n\n"
            "- Only lower House; recommendation of President vs **Governor**; minister only.\n"
            "- Upper House: 14 days, recommendatory only; will of lower House prevails.\n"
            "- No deadlock-resolution mechanism needed — lower House prevails by design."
        ),
        "articles": [
            ("Table 33.1", "Comparing legislative procedure in Parliament and State Legislature."),
        ],
        "visual_blocks": [
            {
                "id": "sl-vs-compare",
                "type": "comparison",
                "title": "Ordinary bill deadlock — Centre vs State",
                "columns": [
                    {
                        "id": "parl",
                        "heading": "Parliament",
                        "points": [
                            "Deadlock after 6 months inaction/reject/unacceptable amends",
                            "Joint sitting can resolve",
                            "LS cannot simply override RS by re-passing",
                            "Applies whether bill started in LS or RS",
                        ],
                    },
                    {
                        "id": "state",
                        "heading": "State Legislature",
                        "points": [
                            "Deadlock after 3 months in Council",
                            "No joint sitting",
                            "Assembly re-passes → prevails (≤1 more month)",
                            "Council-origin bill rejected by Assembly dies",
                        ],
                    },
                ],
            },
            {
                "id": "sl-vs-callout",
                "type": "callout",
                "tone": "trap",
                "title": "PYQ hotspot",
                "body": (
                    "If a question says “joint sitting of state legislature” — almost always wrong. "
                    "Also watch 6 months (Parliament) vs 3 months (Council) vs 14 days (Money Bill)."
                ),
            },
        ],
    },
    {
        "title": "Position of Legislative Council",
        "slug": "sl-council-position",
        "sort_order": 13,
        "summary": (
            "Equal in a few spheres, unequal in most — weaker than Rajya Sabha; "
            "utility as revising chamber vs criticism as ornamental luxury."
        ),
        "body": (
            "## Equal with Assembly (broadly)\n\n"
            "Ordinary bills (till disagreement), ordinance approval, selecting ministers/CM "
            "(but CoM responsible only to Assembly), considering SFC/SPSC/CAG reports, "
            "enlarging SPSC jurisdiction.\n\n"
            "## Unequal (Assembly dominates)\n\n"
            "Money Bills; ordinary-bill final say (4-month delay only); DFG voting; "
            "no-confidence; Council-origin bills die if Assembly rejects; "
            "no role in President/RS elections; weak say in CA ratification; "
            "existence itself depends on Assembly via Art. 169.\n\n"
            "### Why weaker than Rajya Sabha?\n"
            "1. RS protects federal balance; Council has no federal role.\n"
            "2. Heterogeneous composition reduces revising strength.\n"
            "3. Democratic principle — popular House must prevail (British dilatory model).\n\n"
            "**Criticism:** secondary chamber, costly ornamental luxury, refuge for defeated politicians.\n\n"
            "**Utility:** checks hasty legislation; brings experts via nomination."
        ),
        "articles": [
            ("Art. 197–198", "Council’s restricted role on ordinary and Money Bills."),
            ("Art. 169", "Assembly can recommend abolition of the Council."),
        ],
        "visual_blocks": [
            {
                "id": "sl-pos-compare",
                "type": "comparison",
                "title": "Council vs Rajya Sabha",
                "columns": [
                    {
                        "id": "coun",
                        "heading": "Legislative Council",
                        "points": [
                            "Dilatory / advisory on ordinary bills",
                            "Heterogeneous (local bodies, teachers, nominees…)",
                            "No federal equilibrium role",
                            "Can be abolished via Art. 169",
                        ],
                    },
                    {
                        "id": "rs",
                        "heading": "Rajya Sabha",
                        "points": [
                            "Effective revising body (except money/govt control)",
                            "Mostly elected; represents states/UTs",
                            "Federal second chamber",
                            "Cannot be abolished by a state Assembly",
                        ],
                    },
                ],
            },
            {
                "id": "sl-pos-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Mains line",
                "body": (
                    "Council = House of Lords-style delaying chamber, not a federal Rajya Sabha. "
                    "Use this contrast in questions on bicameralism in states."
                ),
            },
        ],
    },
    {
        "title": "Privileges of State Legislature",
        "slug": "sl-privileges",
        "sort_order": 14,
        "summary": (
            "Collective and individual privileges under Art. 194 — extend to ministers and AG "
            "when participating, but not to the Governor."
        ),
        "body": (
            "## Why privileges?\n\n"
            "Special rights/immunities so Houses, committees and members can work independently. "
            "Also cover persons entitled to speak (ministers, Advocate-General). "
            "**Do not extend to the Governor.**\n\n"
            "### Collective\n"
            "Publish/prohibit publication of proceedings; exclude strangers / secret sittings; "
            "regulate procedure; punish breach/contempt; get arrest/detention info of members; "
            "inquire and summon witnesses; courts barred from inquiring into proceedings; "
            "no arrest/legal process in precincts without chair’s permission.\n\n"
            "### Individual\n"
            "1. Freedom from arrest **40 days before/after** session — **civil cases only** "
            "(not criminal / preventive detention).\n"
            "2. Freedom of speech in House/committees (subject to Constitution and rules).\n"
            "3. Exempt from jury service; may refuse to appear as witness while House is in session."
        ),
        "articles": [
            ("Art. 194", "Powers, privileges, etc., of the Houses and of members and committees."),
            ("Art. 195", "Salaries and allowances of members."),
        ],
        "visual_blocks": [
            {
                "id": "sl-priv-pillars",
                "type": "pillars",
                "title": "Two privilege baskets",
                "items": [
                    {
                        "id": "col",
                        "articles": "House",
                        "label": "Collective",
                        "slug": "sl-privileges",
                        "detail": "Publication, secrecy, contempt, inquiries, precincts, non-inquiry by courts.",
                        "tone": "teal",
                    },
                    {
                        "id": "ind",
                        "articles": "Member",
                        "label": "Individual",
                        "slug": "sl-privileges",
                        "detail": "Civil arrest immunity (±40 days), speech, jury/witness exemptions.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "sl-priv-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Arrest immunity is **civil only**. Criminal cases and preventive detention "
                    "are outside this privilege. Governor is **not** covered by House privileges."
                ),
            },
        ],
    },
    {
        "title": "Articles & Reference Tables",
        "slug": "sl-reference-tables",
        "sort_order": 15,
        "summary": (
            "Revision index of Arts 168–212, Art. 169 Acts, and bicameral strength anchors "
            "from Tables 33.2–33.4."
        ),
        "body": (
            "## Article groups (168–212)\n\n"
            "- **Organisation:** 168–172 (Houses, create/abolish, composition, duration).\n"
            "- **Membership & sessions:** 173–177, 188–193.\n"
            "- **Officers & secretariat:** 178–187.\n"
            "- **Privileges & pay:** 194–195.\n"
            "- **Legislative procedure:** 196–201.\n"
            "- **Financial procedure:** 202–207.\n"
            "- **General procedure / language / courts:** 208–212.\n"
            "- **Ordinance (listed in table):** 213 — Governor during recess (cross-link; deep dive elsewhere).\n\n"
            "## Bicameral seat anchors (Table 33.2 extract)\n\n"
            "| State | Assembly | Council |\n"
            "|---|---:|---:|\n"
            "| Andhra Pradesh | 175 | 58 |\n"
            "| Bihar | 243 | 75 |\n"
            "| Karnataka | 224 | 75 |\n"
            "| Maharashtra | 288 | 78 |\n"
            "| Telangana | 119 | 40 |\n"
            "| Uttar Pradesh | 403 | 100 |\n\n"
            "Full SC/ST reservation matrix and all unicameral strengths → open Laxmikanth Table 33.2.\n\n"
            "## Art. 169 Acts (Table 33.4)\n"
            "Abolish: WB 1969, Punjab 1969, AP 1985, TN 1986. "
            "Create: AP 2005, TN 2010 (not enforced)."
        ),
        "articles": [
            ("Arts 168–212", "State Legislature — organisation through procedure and privileges."),
            ("Art. 213", "Governor’s ordinance power during recess (listed at chapter close)."),
            ("Table 33.4", "Parliament’s Art. 169 Acts creating or abolishing Councils."),
        ],
        "visual_blocks": [
            {
                "id": "sl-ref-tree",
                "type": "tree",
                "title": "Arts 168–212 at a glance",
                "root": {
                    "id": "arts",
                    "label": "State Legislature Articles",
                    "detail": "Part VI",
                    "children": [
                        {
                            "id": "org",
                            "label": "168–172 Organisation",
                            "slug": "sl-organisation",
                        },
                        {
                            "id": "off",
                            "label": "178–187 Officers",
                            "slug": "sl-presiding-officers",
                        },
                        {
                            "id": "proc",
                            "label": "196–201 Bills & assent",
                            "slug": "sl-ordinary-bills",
                        },
                        {
                            "id": "fin",
                            "label": "202–207 Finance",
                            "slug": "sl-budget-finance",
                        },
                        {
                            "id": "priv",
                            "label": "194–195 Privileges",
                            "slug": "sl-privileges",
                        },
                    ],
                },
            },
            {
                "id": "sl-ref-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Last-minute card",
                "body": (
                    "ATUBMK · 3-1-1-3-Rest · 4 months / 14 days / no joint sitting · "
                    "Governor+EC vs Speaker on disqualification · 104th ended Anglo-Indian seats."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "sl-organisation"),
    (HUB_SLUG, "parent", "sl-assembly"),
    (HUB_SLUG, "parent", "sl-council"),
    (HUB_SLUG, "parent", "sl-duration"),
    (HUB_SLUG, "parent", "sl-membership"),
    (HUB_SLUG, "parent", "sl-presiding-officers"),
    (HUB_SLUG, "parent", "sl-sessions"),
    (HUB_SLUG, "parent", "sl-ordinary-bills"),
    (HUB_SLUG, "parent", "sl-money-bills"),
    (HUB_SLUG, "parent", "sl-reserved-bills"),
    (HUB_SLUG, "parent", "sl-budget-finance"),
    (HUB_SLUG, "parent", "sl-vs-parliament"),
    (HUB_SLUG, "parent", "sl-council-position"),
    (HUB_SLUG, "parent", "sl-privileges"),
    (HUB_SLUG, "parent", "sl-reference-tables"),
    ("sl-organisation", "related", "sl-council"),
    ("sl-assembly", "related", "sl-duration"),
    ("sl-council", "related", "sl-council-position"),
    ("sl-membership", "related", "sl-presiding-officers"),
    ("sl-ordinary-bills", "related", "sl-money-bills"),
    ("sl-ordinary-bills", "related", "sl-reserved-bills"),
    ("sl-money-bills", "related", "sl-budget-finance"),
    ("sl-ordinary-bills", "related", "sl-vs-parliament"),
    ("sl-sessions", "related", "sl-ordinary-bills"),
    (HUB_SLUG, "related", "parliamentary-system"),
    (HUB_SLUG, "related", "federal-system"),
    (HUB_SLUG, "related", "president"),
    (HUB_SLUG, "related", "emergency-provisions"),
    (HUB_SLUG, "related", "governor"),
    ("sl-reserved-bills", "related", "president"),
    ("sl-duration", "related", "emergency-provisions"),
]

SAMPLE_PYQS = [
    (
        2015,
        "Consider the following statements regarding Legislative Councils in states: "
        "They can be created or abolished by Parliament after a special-majority resolution "
        "of the concerned Assembly; such a law is not an amendment under Article 368.",
        "Both parts align with Art. 169 — Assembly special majority, then ordinary Parliament Act.",
        ["sl-organisation", HUB_SLUG],
    ),
    (
        2016,
        "Which of the following states have a bicameral legislature?",
        "Andhra Pradesh, Telangana, UP, Bihar, Maharashtra, Karnataka (ATUBMK).",
        ["sl-organisation"],
    ),
    (
        2017,
        "With reference to the Legislative Council, which statements about composition are correct?",
        "1/3 local bodies, 1/12 graduates, 1/12 teachers, 1/3 by MLAs (non-MLAs), remainder Governor nominees.",
        ["sl-council"],
    ),
    (
        2018,
        "There is no provision for joint sitting of both Houses of a state legislature to resolve a deadlock.",
        "Correct — Assembly overrides Council on ordinary bills; max Council delay is four months.",
        ["sl-ordinary-bills", "sl-vs-parliament"],
    ),
    (
        2019,
        "A Money Bill in a state legislature can be introduced only in the Legislative Assembly "
        "and the Council cannot amend or reject it.",
        "True — recommendatory role within 14 days; Speaker’s Money Bill decision is final.",
        ["sl-money-bills"],
    ),
    (
        2020,
        "Who decides disqualification of an MLA under the Tenth Schedule?",
        "Speaker of the Assembly (Chairman for MLC) — not the Governor; subject to judicial review.",
        ["sl-membership", "sl-presiding-officers"],
    ),
    (
        2021,
        "The special representation of Anglo-Indians in the Legislative Assemblies by nomination "
        "was discontinued by which amendment?",
        "104th Constitutional Amendment Act, 2019 (effect from 25 January 2020).",
        ["sl-assembly"],
    ),
    (
        2022,
        "Minimum age for membership of Legislative Assembly and Legislative Council is?",
        "25 years (Assembly) and 30 years (Council).",
        ["sl-membership"],
    ),
]

LANDMARK_CASES = [
    {
        "title": "Kihoto Hollohan v. Zachillhu",
        "slug": "kihoto-hollohan",
        "parties": "Kihoto Hollohan v. Zachillhu",
        "year": 1992,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Tenth Schedule defection decisions of Speaker/Chairman are subject to judicial review."
        ),
        "holding": (
            "The Speaker/Chairman’s order under the Tenth Schedule is not final and absolute — "
            "it is open to judicial review on constitutional grounds."
        ),
        "concept_slugs": ["sl-membership", "sl-presiding-officers", HUB_SLUG],
    },
]

AMENDMENTS = [
    {
        "number": 7,
        "year": 1956,
        "title": "Seventh Amendment",
        "summary": (
            "Reorganised states; provided for a Legislative Council in Madhya Pradesh "
            "(Presidential notification never issued)."
        ),
        "effect": "MP remains unicameral despite the constitutional provision for a Council.",
        "concept_slugs": ["sl-organisation", HUB_SLUG],
    },
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": "Froze assembly seats and territorial constituencies at the 1971 level till 2000.",
        "effect": "Started the delimitation freeze later extended by the 84th Amendment.",
        "concept_slugs": ["sl-assembly"],
    },
    {
        "number": 84,
        "year": 2001,
        "title": "Eighty-fourth Amendment",
        "summary": (
            "Extended the freeze on readjustment of assembly seats till 2026; "
            "allowed constituency rationalisation on 1991 figures."
        ),
        "effect": "Seat totals stay frozen to encourage population control measures.",
        "concept_slugs": ["sl-assembly"],
    },
    {
        "number": 87,
        "year": 2003,
        "title": "Eighty-seventh Amendment",
        "summary": "Delimitation of constituencies on 2001 census without altering total seats.",
        "effect": "Boundaries update; assembly strength numbers remain frozen.",
        "concept_slugs": ["sl-assembly"],
    },
    {
        "number": 95,
        "year": 2009,
        "title": "Ninety-fifth Amendment",
        "summary": "Last extension of Anglo-Indian nomination to assemblies up to 2020.",
        "effect": "Set up the final window before the 104th discontinued the provision.",
        "concept_slugs": ["sl-assembly"],
    },
    {
        "number": 104,
        "year": 2019,
        "title": "One Hundred and Fourth Amendment",
        "summary": (
            "Extended SC/ST reservation in assemblies till 2030; "
            "discontinued Anglo-Indian nomination (effect 25 Jan 2020)."
        ),
        "effect": "No more Governor-nominated Anglo-Indian MLAs; SC/ST seats continue to 2030.",
        "concept_slugs": ["sl-assembly", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed State Legislature chapter (Laxmikanth Ch.33, pp. 480–507)."

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
                "title": "State Legislature",
                "sort_order": 4,
                "book_ref": "Laxmikanth 8th Ed, Ch. 33",
                "summary": (
                    "Visual revision of Ch.33 — organisation, Assembly/Council, officers, "
                    "legislative & financial procedure, privileges, and article map (Arts 168–212)."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "State Legislature",
                "summary": (
                    "State mini-Parliament — Governor + Vidhan Sabha (+ Council where it exists); "
                    "popular House dominates."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **mini-Parliament mental model**, then scan organisation "
                    "(ATUBMK + Art. 169). Drill Assembly/Council composition, officers, and "
                    "bill procedures. Finish with **vs Parliament**, privileges, and the article map.\n\n"
                    "Anchor: **no joint sitting** · Council delay **4 months / 14 days** · "
                    "Assembly overrides."
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
            ref="Laxmikanth Ch. 33",
            excerpt="State Legislature — Arts 168–212; organisation to privileges.",
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Arts 168–212",
            excerpt="Part VI provisions on state legislatures.",
            sort_order=1,
        )

        sl_slugs = set(by_slug.keys())
        related_outside = {
            "parliamentary-system",
            "federal-system",
            "president",
            "emergency-provisions",
            "governor",
        }
        ConceptEdge.objects.filter(
            source__slug__in=sl_slugs | related_outside, source__subject=subject
        ).filter(target__slug__in=sl_slugs | related_outside).delete()

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
            subject=subject, slug="state-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"State Legislature chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments linked."
            )
        )
