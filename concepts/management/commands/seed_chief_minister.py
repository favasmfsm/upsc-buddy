"""Seed Laxmikanth Ch.31 Chief Minister (visual revision, pp. 469–473)."""

from django.core.management.base import BaseCommand

from concepts.models import (
    CaseLaw,
    Concept,
    ConceptArticle,
    ConceptEdge,
)
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "chief-minister"
CHAPTER_SLUG = "chief-minister"

ENTRY_PILLARS = [
    {
        "id": "position",
        "articles": "de jure / de facto",
        "label": "Position in the scheme",
        "slug": "cm-position",
        "detail": "Governor = head of State; CM = head of government (real executive).",
        "tone": "teal",
    },
    {
        "id": "appointment",
        "articles": "Art. 164 · Sarkaria",
        "label": "Appointment",
        "slug": "cm-appointment",
        "detail": "Majority convention; hung House; Sarkaria A-L-P-O; 6-month rule.",
        "tone": "olive",
    },
    {
        "id": "oath-term",
        "articles": "Oath · Bommai",
        "label": "Oath, term & salary",
        "slug": "cm-oath-term",
        "detail": "Office + secrecy; pleasure ≠ whim; majority lock (Bommai 1994).",
        "tone": "gold",
    },
    {
        "id": "powers-com",
        "articles": "vs CoM",
        "label": "Powers vs Council of Ministers",
        "slug": "cm-powers-com",
        "detail": "Recommend, allocate, dismiss, preside, guide, collapse — R-A-D-P-G-C.",
        "tone": "orange",
    },
    {
        "id": "powers-gov",
        "articles": "Art. 167",
        "label": "Powers vs Governor",
        "slug": "cm-powers-governor",
        "detail": "Principal channel of communication; advises key state appointments.",
        "tone": "terracotta",
    },
    {
        "id": "powers-leg",
        "articles": "vs House + roles",
        "label": "Legislature & other roles",
        "slug": "cm-powers-legislature",
        "detail": "Summon/dissolve advice; Planning Board; Zonal Councils; ISC/NITI.",
        "tone": "maroon",
    },
    {
        "id": "relations",
        "articles": "163 · 164 · 167",
        "label": "Relationship & articles",
        "slug": "cm-relations-articles",
        "detail": "Aid & advice spine; Table 31.1; PYQ themes.",
        "tone": "teal",
    },
    {
        "id": "vs-pm",
        "articles": "CM ↔ PM",
        "label": "CM vs Prime Minister",
        "slug": "cm-vs-pm",
        "detail": "163↔74 · 164↔75 · 167↔78; Assembly vs Lok Sabha; Governor discretion.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "cm-captain-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Captain of the state ship",
        "topic_label": "Chief Minister",
        "subject_label": "Arts 163 · 164 · 167",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating the Governor as the real executive",
            "Assuming the Governor can appoint any CM freely",
            "Confusing pleasure of the Governor with arbitrary dismissal",
            "Forgetting that CM resignation dissolves the whole CoM",
            "Skipping Sarkaria’s floor-test preference in hung Houses",
        ],
        "insight": (
            "The CM is the real executive at the state — analogous to the PM at the Centre, "
            "but Governor discretion can trim the CM’s room more than presidential practice usually does."
        ),
    },
    {
        "id": "cm-entry-pillars",
        "type": "pillars",
        "title": "Eight revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "cm-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Spine: Art. 163 (CoM aids & advises; Governor discretion carved out) · "
            "Art. 164 (CM appointment / pleasure / collective responsibility to Assembly) · "
            "Art. 167 (CM’s communication duties). "
            "Clear majority → no real discretion. Hung House → Sarkaria preference + VoC in 30 days. "
            "CM resigns or dies → whole Council of Ministers falls."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Position in the Scheme",
        "slug": "cm-position",
        "sort_order": 1,
        "summary": (
            "In the state’s parliamentary scheme, the Governor is the nominal executive "
            "and the Chief Minister is the real executive."
        ),
        "body": (
            "## State vs government\n\n"
            "- **Governor** — head of the **State**; de jure / nominal executive.\n"
            "- **Chief Minister** — head of the **government**; de facto / real executive.\n"
            "- Position of the CM at the state is **analogous to the PM** at the Centre.\n\n"
            "### Mains value-add\n"
            "Parliamentary form at the state mirrors the Union: crown (Governor) vs captain (CM). "
            "But the Governor’s **discretionary powers** can shrink CM authority more visibly "
            "than presidential discretion usually does at the Centre.\n\n"
            "**Mnemonic:** State wears the crown; Government runs the ship."
        ),
        "articles": [
            (
                "Art. 163",
                "Council of Ministers with the CM at the head to aid and advise the Governor.",
            ),
            (
                "Art. 164",
                "CM appointed by the Governor; collective responsibility of the CoM to the Assembly.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cm-position-compare",
                "type": "comparison",
                "title": "Governor vs Chief Minister",
                "columns": [
                    {
                        "id": "governor",
                        "heading": "Governor",
                        "points": [
                            "Head of the State",
                            "Nominal / de jure executive",
                            "Constitutional figurehead in parliamentary form",
                            "Acts on aid and advice of the CoM (Art. 163), except discretion",
                        ],
                    },
                    {
                        "id": "cm",
                        "heading": "Chief Minister",
                        "points": [
                            "Head of the government",
                            "Real / de facto executive",
                            "Leads the State Council of Ministers",
                            "Analogous to the Prime Minister at the Centre",
                        ],
                    },
                ],
            },
            {
                "id": "cm-position-callout",
                "type": "callout",
                "tone": "tip",
                "title": "One-liner",
                "body": (
                    "Governor = head of State (nominal). "
                    "CM = head of government (real). Do not swap these labels in Prelims."
                ),
            },
        ],
    },
    {
        "title": "Appointment of the Chief Minister",
        "slug": "cm-appointment",
        "sort_order": 2,
        "summary": (
            "Art. 164 only says the Governor appoints the CM — convention, hung-House "
            "discretion, and Sarkaria guidelines fill the gaps."
        ),
        "body": (
            "## Rule vs exception\n\n"
            "- Constitution: **no selection procedure** — only that the CM is appointed by the Governor (Art. 164).\n"
            "- **Convention (rule):** appoint the leader of the majority party in the Legislative Assembly.\n"
            "- **Discretion (exception):** hung House — usually largest party or coalition leader, "
            "then vote of confidence (typically within a month).\n"
            "- **Sudden death, no successor:** Governor may use judgement; if the ruling party elects "
            "a new leader, the Governor **must** appoint that leader.\n\n"
            "### High-yield facts\n"
            "- Majority need **not** be proved *before* appointment — may prove later within a reasonable period.\n"
            "- A **non-member** of the state legislature can be CM for **six months**; must join either "
            "House or ceases to be CM.\n"
            "- CM may be from **either House** — usually Assembly, but Council members have also been CM.\n\n"
            "### Sarkaria Commission (1983–88) — lock these\n"
            "1. Call the party/combination with the **widest support**; form a government — do not "
            "pick policies the Governor likes.\n"
            "2. Absolute majority party → its leader **automatically**.\n"
            "3. Else sound in order (**A-L-P-O**): pre-poll **A**lliance → **L**argest party + support → "
            "post-poll coalition all-in → post-poll with **O**utside support.\n"
            "4. Pick the leader most likely to command a majority.\n"
            "5. No absolute majority → seek **vote of confidence within 30 days**.\n"
            "6. Contested majority claims → **floor of the House**, not Governor’s private arithmetic.\n"
        ),
        "articles": [
            (
                "Art. 164",
                "The Chief Minister shall be appointed by the Governor.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cm-appointment-flow",
                "type": "flowchart",
                "title": "Who becomes CM?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Does any party have a clear Assembly majority?",
                        "detail": "Start from Legislative Assembly arithmetic, not gubernatorial whim.",
                        "options": [
                            {"label": "Yes — clear majority", "next": "majority"},
                            {"label": "No — hung House", "next": "hung"},
                            {"label": "CM dies; no obvious successor", "next": "death"},
                        ],
                    },
                    {
                        "id": "majority",
                        "label": "Appoint majority leader",
                        "detail": "Governor has no real choice — parliamentary convention binds.",
                    },
                    {
                        "id": "hung",
                        "label": "Limited discretion + Sarkaria",
                        "detail": (
                            "Follow A-L-P-O preference; appoint leader most likely to command "
                            "majority; VoC within 30 days if no absolute majority."
                        ),
                    },
                    {
                        "id": "death",
                        "label": "Individual judgement possible",
                        "detail": (
                            "If party elects a leader → must appoint. Else limited discretion "
                            "until succession is clear."
                        ),
                    },
                ],
            },
            {
                "id": "cm-sarkaria-tree",
                "type": "tree",
                "title": "Sarkaria hung-House order (A-L-P-O)",
                "root": {
                    "id": "hung",
                    "label": "No absolute majority",
                    "detail": "Sound parties/groups in this preference order",
                    "children": [
                        {
                            "id": "a",
                            "label": "A — Pre-poll alliance",
                            "detail": "Alliance formed before elections",
                        },
                        {
                            "id": "l",
                            "label": "L — Largest + support",
                            "detail": "Largest single party staking a claim with others/independents",
                        },
                        {
                            "id": "p",
                            "label": "P — Post-poll all-in",
                            "detail": "Post-electoral coalition; all partners join government",
                        },
                        {
                            "id": "o",
                            "label": "O — Outside support",
                            "detail": "Some join government; others (incl. independents) support from outside",
                        },
                    ],
                },
            },
            {
                "id": "cm-appointment-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam traps",
                "body": (
                    "Governor is not free to appoint anyone when there is a clear majority. "
                    "Non-member CM → max 6 months. CM may come from Legislative Council. "
                    "Majority need not be proved before appointment. Contested majority → floor test "
                    "(Sarkaria), not Raj Bhavan arithmetic."
                ),
            },
        ],
    },
    {
        "title": "Oath, Term & Salary",
        "slug": "cm-oath-term",
        "sort_order": 3,
        "summary": (
            "Office and secrecy oaths before the Governor; tenure during pleasure but "
            "tied to Assembly confidence; salary fixed by the state legislature."
        ),
        "body": (
            "## Oaths\n"
            "Before entering office, the Governor administers oaths of **office** and **secrecy** "
            "(same form as any state minister).\n\n"
            "### Oath of office (four points)\n"
            "1. True faith and allegiance to the Constitution\n"
            "2. Uphold sovereignty and integrity of India\n"
            "3. Faithfully discharge duties of office\n"
            "4. Do right to all people per Constitution and law — without fear or favour, "
            "affection or ill will\n\n"
            "### Oath of secrecy\n"
            "Not to reveal information known as a state minister except for due discharge of duties.\n\n"
            "## Term\n"
            "- Not fixed — holds office during the **pleasure of the Governor**.\n"
            "- Pleasure ≠ arbitrary dismissal: while the CM enjoys **Assembly majority**, "
            "the Governor cannot dismiss (**S.R. Bommai**, 1994).\n"
            "- Lose confidence → must resign, or the Governor may dismiss.\n"
            "- Note: practice has sometimes violated Bommai’s floor-test norm.\n\n"
            "## Salary\n"
            "Determined by the **state legislature** — MLA/MLC pay plus sumptuary allowance, "
            "free accommodation, travelling allowance, medical facilities, etc.\n"
        ),
        "articles": [
            (
                "Art. 164",
                "Ministers hold office during the pleasure of the Governor; collective responsibility to the Assembly.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cm-oath-pillars",
                "type": "pillars",
                "title": "Four points of the oath of office",
                "items": [
                    {
                        "id": "allegiance",
                        "articles": "1",
                        "label": "Allegiance",
                        "slug": "cm-oath-term",
                        "detail": "True faith and allegiance to the Constitution of India.",
                        "tone": "teal",
                    },
                    {
                        "id": "sovereignty",
                        "articles": "2",
                        "label": "Sovereignty & integrity",
                        "slug": "cm-oath-term",
                        "detail": "Uphold the sovereignty and integrity of India.",
                        "tone": "olive",
                    },
                    {
                        "id": "duties",
                        "articles": "3",
                        "label": "Discharge duties",
                        "slug": "cm-oath-term",
                        "detail": "Faithfully and conscientiously discharge the duties of office.",
                        "tone": "gold",
                    },
                    {
                        "id": "right",
                        "articles": "4",
                        "label": "Do right to all",
                        "slug": "cm-oath-term",
                        "detail": "Without fear or favour, affection or ill will — per Constitution and law.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "cm-oath-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Bommai lock",
                "body": (
                    "‘Pleasure of the Governor’ does not mean the Governor can sack a majority CM. "
                    "Bommai (1994): majority is tested on the floor of the House. "
                    "Sarkaria: do not decide contested majority outside the Assembly."
                ),
            },
        ],
    },
    {
        "title": "Powers vs Council of Ministers",
        "slug": "cm-powers-com",
        "sort_order": 4,
        "summary": (
            "As head of the State Council of Ministers, the CM recommends, allocates, "
            "controls, and can collapse the ministry."
        ),
        "body": (
            "## Six powers (R-A-D-P-G-C)\n\n"
            "1. **Recommend** persons for appointment as ministers — Governor appoints "
            "only those recommended by the CM.\n"
            "2. **Allocate / reshuffle** portfolios among ministers.\n"
            "3. **Dismiss** — ask a minister to resign or advise the Governor to dismiss "
            "in case of difference of opinion.\n"
            "4. **Preside** over meetings of the Council of Ministers and influence decisions.\n"
            "5. **Guide**, direct, control, and coordinate all ministers.\n"
            "6. **Collapse** the Council by resigning from office.\n\n"
            "### Vacuum vs vacancy\n"
            "- **Resignation or death of the CM** → entire Council of Ministers dissolves (vacuum).\n"
            "- **Resignation or death of any other minister** → only a vacancy the CM may fill.\n\n"
            "**Mnemonic:** R-A-D-P-G-C — Recommend, Allocate, Dismiss, Preside, Guide, Collapse."
        ),
        "articles": [
            (
                "Art. 164",
                "Other ministers are appointed by the Governor on the advice of the Chief Minister.",
            ),
            (
                "Art. 163",
                "Council of Ministers with the Chief Minister as the head.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cm-com-pillars",
                "type": "pillars",
                "title": "Six powers over the Council of Ministers",
                "items": [
                    {
                        "id": "recommend",
                        "articles": "R",
                        "label": "Recommend",
                        "slug": "cm-powers-com",
                        "detail": "Governor appoints only ministers recommended by the CM.",
                        "tone": "teal",
                    },
                    {
                        "id": "allocate",
                        "articles": "A",
                        "label": "Allocate",
                        "slug": "cm-powers-com",
                        "detail": "Assign and reshuffle portfolios among ministers.",
                        "tone": "olive",
                    },
                    {
                        "id": "dismiss",
                        "articles": "D",
                        "label": "Dismiss",
                        "slug": "cm-powers-com",
                        "detail": "Force resignation or advise gubernatorial dismissal.",
                        "tone": "gold",
                    },
                    {
                        "id": "preside",
                        "articles": "P",
                        "label": "Preside",
                        "slug": "cm-powers-com",
                        "detail": "Chairs CoM meetings and shapes decisions.",
                        "tone": "orange",
                    },
                    {
                        "id": "guide",
                        "articles": "G",
                        "label": "Guide",
                        "slug": "cm-powers-com",
                        "detail": "Guides, directs, controls, and coordinates ministers.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "collapse",
                        "articles": "C",
                        "label": "Collapse",
                        "slug": "cm-powers-com",
                        "detail": "CM’s resignation dissolves the whole Council.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "cm-com-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Vacuum vs vacancy",
                "body": (
                    "CM resigns or dies → vacuum: whole CoM falls. "
                    "Any other minister resigns or dies → vacancy only. Classic Prelims distinction."
                ),
            },
        ],
    },
    {
        "title": "Powers vs the Governor",
        "slug": "cm-powers-governor",
        "sort_order": 5,
        "summary": (
            "The CM is the principal channel between the Governor and the Council of Ministers "
            "(Art. 167) and advises key state appointments."
        ),
        "body": (
            "## Principal channel (Art. 167)\n\n"
            "It is the duty of the Chief Minister:\n"
            "(a) to communicate to the Governor all CoM decisions on state administration "
            "and proposals for legislation;\n"
            "(b) to furnish information the Governor may call for on those matters; and\n"
            "(c) if the Governor so requires, to submit for CoM consideration any matter "
            "decided by a minister but not yet considered by the Council.\n\n"
            "## Advice on appointments\n"
            "CM advises the Governor on important officials — Advocate General, chairman and "
            "members of the State Public Service Commission, State Election Commissioner, and so on.\n"
        ),
        "articles": [
            (
                "Art. 167",
                "Duties of the Chief Minister as respects the furnishing of information to the Governor, etc.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cm-art167-explorer",
                "type": "article_explorer",
                "title": "Article 167 explorer",
                "article_ref": "Article 167",
                "stages": [
                    {
                        "id": "communicate",
                        "label": "167(a) Communicate",
                        "detail": "All CoM decisions on state affairs and legislative proposals go to the Governor.",
                    },
                    {
                        "id": "furnish",
                        "label": "167(b) Furnish",
                        "detail": "Supply any related information the Governor calls for.",
                    },
                    {
                        "id": "submit",
                        "label": "167(c) Submit to CoM",
                        "detail": (
                            "If required, place a single-minister decision before the full Council "
                            "for collective consideration."
                        ),
                    },
                    {
                        "id": "why",
                        "label": "Why it matters",
                        "detail": (
                            "Institutional bridge — keeps the nominal head informed and protects "
                            "collective responsibility (state twin of Art. 78)."
                        ),
                    },
                ],
            },
            {
                "id": "cm-appointments-pillars",
                "type": "pillars",
                "title": "Key appointments advised by the CM",
                "items": [
                    {
                        "id": "ag",
                        "articles": "AG",
                        "label": "Advocate General",
                        "slug": "cm-powers-governor",
                        "detail": "Chief legal adviser to the state government.",
                        "tone": "teal",
                    },
                    {
                        "id": "spsc",
                        "articles": "SPSC",
                        "label": "State PSC",
                        "slug": "cm-powers-governor",
                        "detail": "Chairman and members of the State Public Service Commission.",
                        "tone": "olive",
                    },
                    {
                        "id": "sec",
                        "articles": "SEC",
                        "label": "State Election Commissioner",
                        "slug": "cm-powers-governor",
                        "detail": "Conducts elections to local bodies in the state.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "cm-gov-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims fact",
                "body": (
                    "Art. 167 = CM’s communication duties to the Governor. "
                    "Pair it with Art. 163 (aid & advice) and Art. 164 (appointment / responsibility). "
                    "Union twin of Art. 167 is Art. 78."
                ),
            },
        ],
    },
    {
        "title": "Legislature & Other Roles",
        "slug": "cm-powers-legislature",
        "sort_order": 6,
        "summary": (
            "As leader of the House and political head of the state system, the CM links "
            "the legislature, party, policy, and crisis management."
        ),
        "body": (
            "## In relation to the State Legislature\n"
            "1. Advises the Governor on **summoning and proroguing** sessions.\n"
            "2. Can recommend **dissolution of the Legislative Assembly** at any time.\n"
            "3. Announces government policies on the floor of the House.\n\n"
            "## Other powers & functions\n"
            "- Chair: **State Planning Board**.\n"
            "- **Vice-chairman** of the concerned Zonal Council by rotation (one year); "
            "Union Home Minister chairs all Zonal Councils.\n"
            "- Member: **Inter-State Council** and **Governing Council of NITI Aayog** "
            "(both headed by the PM).\n"
            "- Chief spokesman of the state government; **crisis manager-in-chief** "
            "at the political level during emergencies.\n"
            "- Leader of the state (receives public memoranda), leader of the party in power, "
            "and political head of the services.\n\n"
            "### Caveat\n"
            "Governor’s **discretionary powers** reduce to some extent the power, authority, "
            "influence, prestige, and role of the CM in state administration."
        ),
        "articles": [
            (
                "Art. 164",
                "Collective responsibility of the Council of Ministers to the Legislative Assembly of the state.",
            ),
            (
                "Art. 177",
                "Rights of Ministers as respects the Houses of the state legislature.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cm-leg-pillars",
                "type": "pillars",
                "title": "Three legislative levers",
                "items": [
                    {
                        "id": "summon",
                        "articles": "1",
                        "label": "Summon / prorogue",
                        "slug": "cm-powers-legislature",
                        "detail": "Advises the Governor on calling and ending sessions.",
                        "tone": "teal",
                    },
                    {
                        "id": "dissolve",
                        "articles": "2",
                        "label": "Dissolve Assembly",
                        "slug": "cm-powers-legislature",
                        "detail": "May recommend dissolution of the Legislative Assembly at any time.",
                        "tone": "olive",
                    },
                    {
                        "id": "announce",
                        "articles": "3",
                        "label": "Announce policy",
                        "slug": "cm-powers-legislature",
                        "detail": "States government policy on the floor of the House.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "cm-other-pillars",
                "type": "pillars",
                "title": "Other hats (scan)",
                "items": [
                    {
                        "id": "planning",
                        "articles": "SPB",
                        "label": "State Planning Board",
                        "slug": "cm-powers-legislature",
                        "detail": "CM is the chairman of the State Planning Board.",
                        "tone": "orange",
                    },
                    {
                        "id": "zonal",
                        "articles": "ZC",
                        "label": "Zonal Council",
                        "slug": "cm-powers-legislature",
                        "detail": "Vice-chairman by rotation (1 year); Home Minister chairs all.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "isc-niti",
                        "articles": "Bodies",
                        "label": "ISC & NITI",
                        "slug": "cm-powers-legislature",
                        "detail": "Member of Inter-State Council and NITI Governing Council (PM-headed).",
                        "tone": "maroon",
                    },
                    {
                        "id": "crisis-party",
                        "articles": "Power",
                        "label": "Crisis, party & services",
                        "slug": "cm-powers-legislature",
                        "detail": "Crisis manager; party leader; political head of services.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "cm-leg-callout",
                "type": "callout",
                "tone": "note",
                "title": "Mains VA",
                "body": (
                    "CM is real executive — but Governor discretion (hung House, dismissal "
                    "controversies, Article 356 interface) is the classic counterweight. "
                    "Use Sarkaria + Bommai when arguing for floor-test primacy."
                ),
            },
        ],
    },
    {
        "title": "Relationship & Articles at a Glance",
        "slug": "cm-relations-articles",
        "sort_order": 7,
        "summary": (
            "Arts 163–164–167 relationship spine, Table 31.1 articles, and high-yield PYQ themes."
        ),
        "body": (
            "## Relationship with the Governor\n"
            "- **Art. 163** — CoM with CM at the head aids and advises; exception where the "
            "Governor is required to act in **discretion**.\n"
            "- **Art. 164** — CM appointed by Governor; other ministers on CM’s advice; "
            "pleasure of Governor; **collective responsibility to the Legislative Assembly**.\n"
            "- **Art. 167** — CM’s duties to communicate / furnish / submit matters to the CoM.\n"
            "- Also revise: **Art. 166** (conduct of business of the state government), "
            "**Art. 177** (ministers’ rights in the Houses).\n\n"
            "## Table 31.1 — articles related to CM\n"
            "| Article | Subject |\n"
            "|---|---|\n"
            "| 163 | CoM to aid and advise Governor |\n"
            "| 164 | Other provisions as to Ministers |\n"
            "| 166 | Conduct of business of the Government of a State |\n"
            "| 167 | Duties of CM regarding information to Governor |\n"
            "| 177 | Rights of Ministers as respects the Houses |\n\n"
            "**Mnemonic spine:** 163 · 164 · 167 — advise · appoint · inform."
        ),
        "articles": [
            (
                "Art. 163",
                "Council of Ministers to aid and advise the Governor; discretion carved out.",
            ),
            (
                "Art. 164",
                "Appointment, pleasure, and collective responsibility of ministers.",
            ),
            (
                "Art. 166",
                "Conduct of business of the Government of a State.",
            ),
            (
                "Art. 167",
                "Duties of the Chief Minister as respects information to the Governor.",
            ),
            (
                "Art. 177",
                "Rights of Ministers as respects the Houses.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cm-articles-compare",
                "type": "comparison",
                "title": "Articles related to the CM (Table 31.1)",
                "columns": [
                    {
                        "id": "core",
                        "heading": "Core triad",
                        "points": [
                            "163 — CoM aids and advises the Governor",
                            "164 — Appointment, pleasure, collective responsibility",
                            "167 — CM’s information duties to the Governor",
                        ],
                    },
                    {
                        "id": "support",
                        "heading": "Also revise",
                        "points": [
                            "166 — Conduct of business of the state government",
                            "177 — Ministers’ rights in the Houses",
                            "Bommai — floor test for majority / dismissal",
                        ],
                    },
                ],
            },
            {
                "id": "cm-relations-tree",
                "type": "tree",
                "title": "163–164–167 at a glance",
                "root": {
                    "id": "cm-gov",
                    "label": "CM ↔ Governor",
                    "detail": "Constitutional relationship spine",
                    "children": [
                        {
                            "id": "a163",
                            "label": "Art. 163",
                            "detail": "Aid & advice; Governor discretion exception",
                        },
                        {
                            "id": "a164",
                            "label": "Art. 164",
                            "detail": "Appoint CM/ministers; pleasure; collective responsibility",
                        },
                        {
                            "id": "a167",
                            "label": "Art. 167",
                            "detail": "Communicate · furnish · submit to CoM",
                        },
                    ],
                },
            },
            {
                "id": "cm-pyq-themes",
                "type": "callout",
                "tone": "note",
                "title": "PYQ themes",
                "body": (
                    "Hung-assembly appointment / Sarkaria order; Art. 163/164/167 triad; "
                    "CM from Legislative Council; 6-month non-member rule; vacuum vs vacancy; "
                    "Bommai floor test; Art. 167 duties; Zonal Council vice-chair vs Home Minister chair."
                ),
            },
        ],
    },
    {
        "title": "Chief Minister vs Prime Minister",
        "slug": "cm-vs-pm",
        "sort_order": 8,
        "summary": (
            "Quick Union–State mirror: article twins, House of confidence, and where "
            "Governor discretion diverges from presidential practice."
        ),
        "body": (
            "## Analogous offices\n"
            "Laxmikanth’s framing: CM at the state ≈ PM at the Centre — real executive, "
            "head of government, leader of the CoM.\n\n"
            "### Article twins\n"
            "| State (CM) | Union (PM) | Theme |\n"
            "|---|---|---|\n"
            "| Art. 163 | Art. 74 | Aid & advice |\n"
            "| Art. 164 | Art. 75 | Appointment / pleasure / collective responsibility |\n"
            "| Art. 167 | Art. 78 | Communication duties |\n\n"
            "### Confidence House\n"
            "- CM / State CoM → collectively responsible to the **Legislative Assembly**.\n"
            "- PM / Union CoM → collectively responsible to the **Lok Sabha**.\n\n"
            "### Where they diverge (exam-useful)\n"
            "- Governor’s **express constitutional discretion** (Art. 163) is more prominent "
            "in state politics than presidential discretion in routine Union governance.\n"
            "- Sarkaria’s detailed appointment order and floor-test insistence are classic "
            "**state-side** revision themes.\n"
            "- CM sits on bodies the PM chairs (ISC, NITI Governing Council) and is "
            "Zonal Council vice-chair — PM has no Zonal Council twin.\n\n"
            "**Memory:** 163↔74 · 164↔75 · 167↔78 — same logic, different numbers."
        ),
        "articles": [
            (
                "Art. 163 / 74",
                "Aid and advice to Governor / President.",
            ),
            (
                "Art. 164 / 75",
                "Appointment and collective responsibility — Assembly / Lok Sabha.",
            ),
            (
                "Art. 167 / 78",
                "Communication duties of CM / PM.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cm-vs-pm-compare",
                "type": "comparison",
                "title": "Chief Minister vs Prime Minister",
                "columns": [
                    {
                        "id": "cm-col",
                        "heading": "Chief Minister",
                        "points": [
                            "Real executive of the State",
                            "Arts 163 · 164 · 167",
                            "Collective responsibility to Assembly",
                            "Advises Governor on AG, SPSC, SEC",
                            "Governor discretion more visible (hung House, Art. 163)",
                            "Zonal Council vice-chair; member of ISC / NITI GC",
                        ],
                    },
                    {
                        "id": "pm-col",
                        "heading": "Prime Minister",
                        "points": [
                            "Real executive of the Union",
                            "Arts 74 · 75 · 78",
                            "Collective responsibility to Lok Sabha",
                            "Advises President on AG, CAG, UPSC, EC, FC",
                            "Presidential discretion narrower in clear-majority politics",
                            "Chairs ISC, NITI Governing Council, and more",
                        ],
                    },
                ],
            },
            {
                "id": "cm-vs-pm-memory",
                "type": "callout",
                "tone": "tip",
                "title": "Memory box",
                "body": (
                    "Lock the twins: 163↔74 (advise), 164↔75 (appoint), 167↔78 (inform). "
                    "Then add: Assembly vs Lok Sabha; Sarkaria/Bommai are state-side staples; "
                    "R-A-D-P-G-C works for both CM and PM over their Councils."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "cm-position"),
    (HUB_SLUG, "parent", "cm-appointment"),
    (HUB_SLUG, "parent", "cm-oath-term"),
    (HUB_SLUG, "parent", "cm-powers-com"),
    (HUB_SLUG, "parent", "cm-powers-governor"),
    (HUB_SLUG, "parent", "cm-powers-legislature"),
    (HUB_SLUG, "parent", "cm-relations-articles"),
    (HUB_SLUG, "parent", "cm-vs-pm"),
    ("cm-position", "related", "cm-appointment"),
    ("cm-appointment", "related", "cm-oath-term"),
    ("cm-powers-com", "related", "cm-powers-governor"),
    ("cm-powers-governor", "related", "cm-powers-legislature"),
    ("cm-powers-legislature", "related", "cm-relations-articles"),
    ("cm-relations-articles", "related", "cm-vs-pm"),
    ("cm-powers-com", "related", "cm-relations-articles"),
    ("cm-appointment", "related", "cm-relations-articles"),
    (HUB_SLUG, "related", "prime-minister"),
    (HUB_SLUG, "related", "parliamentary-system"),
    (HUB_SLUG, "related", "ps-features"),
    ("cm-vs-pm", "related", "prime-minister"),
    ("cm-powers-governor", "related", "pm-powers-president"),
    ("cm-powers-com", "related", "pm-powers-com"),
]

SAMPLE_PYQS = [
    (
        2018,
        "Consider the appointment of the Chief Minister. Which of the following is correct?",
        "The Constitution does not require proof of majority before appointment; the Governor "
        "may appoint first and ask for a confidence vote within a reasonable period. "
        "Clear majority → appoint majority leader; hung House → limited discretion.",
        ["cm-appointment", HUB_SLUG],
    ),
    (
        2016,
        "Which of the following correctly describes the relationship between the Governor and the Chief Minister?",
        "Art. 163: CoM headed by CM aids and advises the Governor except where discretion applies. "
        "Art. 167: CM must communicate CoM decisions, furnish information, and if required "
        "submit single-minister decisions to the full CoM.",
        ["cm-powers-governor", "cm-relations-articles", HUB_SLUG],
    ),
    (
        2014,
        "With reference to the Council of Ministers in a state, resignation or death of the Chief Minister:",
        "Automatically dissolves the entire Council of Ministers (vacuum). Resignation or death "
        "of any other minister only creates a vacancy.",
        ["cm-powers-com", HUB_SLUG],
    ),
    (
        2013,
        "A person who is not a member of the state legislature can be appointed Chief Minister for:",
        "Six months — must get elected to the state legislature within that period or ceases to be CM. "
        "CM may be from either House (Assembly or Council).",
        ["cm-appointment", HUB_SLUG],
    ),
    (
        1994,
        "On dismissal of a Chief Minister who claims majority support, the preferred constitutional course is:",
        "Test majority on the floor of the Legislative Assembly (S.R. Bommai, 1994; Sarkaria). "
        "Governor should not decide contested majority claims outside the House.",
        ["cm-oath-term", "cm-appointment", HUB_SLUG],
    ),
]

LANDMARK_CASES = [
    {
        "title": "S.R. Bommai v. Union of India",
        "slug": "sr-bommai",
        "parties": "S.R. Bommai v. Union of India",
        "year": 1994,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Landmark on Article 356 and majority support of a ministry — "
            "cited for the rule that a CM enjoying Assembly majority cannot be dismissed at will."
        ),
        "holding": (
            "Majority support of the Council of Ministers should be tested on the floor of the "
            "Legislative Assembly. Pleasure of the Governor does not permit dismissal of a CM "
            "who still commands majority support."
        ),
        "concept_slugs": ["cm-oath-term", "cm-appointment", HUB_SLUG],
    },
]


class Command(BaseCommand):
    help = "Seed Chief Minister chapter (Laxmikanth Ch.31)."

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
                "title": "Chief Minister",
                "sort_order": 2,
                "book_ref": "Laxmikanth 8th Ed, Ch. 31 (pp. 469–473)",
                "summary": (
                    "Visual revision of Ch.31 — appointment, Sarkaria, oath/tenure, "
                    "powers vs CoM/Governor/Legislature, articles, and CM vs PM."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Chief Minister",
                "summary": (
                    "Real executive of the State — head of government under Arts 163, 164, and 167; "
                    "leader of the Council of Ministers and of the Assembly majority in practice."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **captain of the state ship** mental model, then "
                    "**Position** → **Appointment (incl. Sarkaria)** → **Oath & term**. "
                    "Drill **powers** (CoM → Governor → Legislature), then "
                    "**relations / articles** and **CM vs PM**. "
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
            ref="Laxmikanth Ch. 31",
            excerpt=(
                "Chief Minister — appointment, Sarkaria, powers, relations with Governor and CoM, "
                "Arts 163–164–167."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 163 & 164",
            excerpt=(
                "CoM headed by CM aids and advises; CM appointed by Governor; "
                "collective responsibility to the Legislative Assembly."
            ),
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 167",
            excerpt="Duties of the CM to communicate and furnish information to the Governor.",
            sort_order=2,
        )

        from django.db.models import Q

        cm_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            Q(source__slug__in=cm_slugs) | Q(target__slug__in=cm_slugs),
            source__subject=subject,
        ).delete()

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
            concepts = [by_slug[s] for s in slugs if s in by_slug]
            if concepts:
                existing = list(pyq.concepts.all())
                pyq.concepts.set({*existing, *concepts})

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

        from subjects.models import Section

        section = Section.objects.filter(
            subject=subject, slug="state-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Chief Minister chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(SAMPLE_PYQS)} PYQs linked."
            )
        )
