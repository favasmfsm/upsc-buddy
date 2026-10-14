"""Seed Laxmikanth Ch.20 Prime Minister (visual revision)."""

from django.core.management.base import BaseCommand

from concepts.models import (
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from subjects.models import Chapter, Subject

HUB_SLUG = "prime-minister"
CHAPTER_SLUG = "prime-minister"

ENTRY_PILLARS = [
    {
        "id": "position",
        "articles": "de jure / de facto",
        "label": "Position in the scheme",
        "slug": "pm-position",
        "detail": "President = head of State; PM = head of government (real executive).",
        "tone": "teal",
    },
    {
        "id": "appointment",
        "articles": "Art. 75",
        "label": "Appointment",
        "slug": "pm-appointment",
        "detail": "Majority convention; limited discretion; 6-month non-MP rule.",
        "tone": "olive",
    },
    {
        "id": "oath-term",
        "articles": "Oath · tenure",
        "label": "Oath, term & salary",
        "slug": "pm-oath-term",
        "detail": "Office + secrecy oaths; pleasure ≠ whim; confidence of Lok Sabha.",
        "tone": "gold",
    },
    {
        "id": "powers-com",
        "articles": "vs CoM",
        "label": "Powers vs Council of Ministers",
        "slug": "pm-powers-com",
        "detail": "Recommend, allocate, dismiss, preside, guide, collapse — R-A-D-P-G-C.",
        "tone": "orange",
    },
    {
        "id": "powers-pres",
        "articles": "Art. 78",
        "label": "Powers vs President",
        "slug": "pm-powers-president",
        "detail": "Principal channel of communication; advises key appointments.",
        "tone": "terracotta",
    },
    {
        "id": "powers-parl",
        "articles": "vs LS + roles",
        "label": "Parliament & other roles",
        "slug": "pm-powers-parliament",
        "detail": "Summon/dissolve advice; NITI chair; crisis manager; party & services head.",
        "tone": "maroon",
    },
    {
        "id": "role",
        "articles": "Quotes",
        "label": "Role descriptions",
        "slug": "pm-role-descriptions",
        "detail": "Primus inter pares → prime ministerial government.",
        "tone": "teal",
    },
    {
        "id": "extras",
        "articles": "74–78 · caretaker",
        "label": "Relations, caretaker & articles",
        "slug": "pm-relations-extras",
        "detail": "Art. 74/75/78 spine; caretaker limits; six CM→PM names.",
        "tone": "olive",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "pm-captain-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Captain of the ship",
        "topic_label": "Prime Minister",
        "subject_label": "Arts 74 · 75 · 78",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating the President as the real executive",
            "Assuming the President can pick any PM freely",
            "Forgetting that PM resignation dissolves the whole CoM",
            "Confusing pleasure of the President with arbitrary dismissal",
        ],
        "insight": (
            "The PM is the real executive — first among ministers in form, "
            "and often the centre of government in practice."
        ),
    },
    {
        "id": "pm-entry-pillars",
        "type": "pillars",
        "title": "Eight revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "pm-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Spine: Art. 74 (aid & advice) · Art. 75 (appointment / pleasure / collective "
            "responsibility to Lok Sabha) · Art. 78 (PM’s communication duties). "
            "Clear majority → no presidential discretion. Hung House / no successor → limited "
            "discretion. PM resigns or dies → whole Council of Ministers falls."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Position in the Scheme",
        "slug": "pm-position",
        "sort_order": 1,
        "summary": (
            "In India’s parliamentary scheme, the President is the nominal executive "
            "and the Prime Minister is the real executive."
        ),
        "body": (
            "## State vs government\n\n"
            "- **President** — head of the **State**; de jure / nominal executive.\n"
            "- **Prime Minister** — head of the **government**; de facto / real executive.\n"
            "- The Union executive includes the President, Vice-President, PM, and Council of Ministers.\n\n"
            "### Mains value-add\n"
            "Ambedkar: if any functionary under our Constitution is to be compared with the "
            "**US President**, it is the **Prime Minister** — not the President of the Union.\n\n"
            "**Mnemonic:** State wears the crown; Government runs the ship."
        ),
        "articles": [
            (
                "Art. 74",
                "Council of Ministers with the PM at the head to aid and advise the President.",
            ),
            (
                "Art. 75",
                "PM appointed by the President; collective responsibility of the CoM to the Lok Sabha.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pm-position-compare",
                "type": "comparison",
                "title": "President vs Prime Minister",
                "columns": [
                    {
                        "id": "president",
                        "heading": "President",
                        "points": [
                            "Head of the State",
                            "Nominal / de jure executive",
                            "Constitutional figurehead in parliamentary form",
                            "Acts on aid and advice of the CoM (Art. 74)",
                        ],
                    },
                    {
                        "id": "pm",
                        "heading": "Prime Minister",
                        "points": [
                            "Head of the government",
                            "Real / de facto executive",
                            "Leads the Council of Ministers",
                            "Closest analogue to the US President (Ambedkar)",
                        ],
                    },
                ],
            },
            {
                "id": "pm-position-callout",
                "type": "callout",
                "tone": "tip",
                "title": "One-liner",
                "body": (
                    "President = head of State (nominal). "
                    "PM = head of government (real). Do not swap these labels in Prelims."
                ),
            },
        ],
    },
    {
        "title": "Appointment of the Prime Minister",
        "slug": "pm-appointment",
        "sort_order": 2,
        "summary": (
            "Art. 75 only says the President appoints the PM — convention and limited "
            "discretion fill the gaps."
        ),
        "body": (
            "## Rule vs exception\n\n"
            "- Constitution: **no selection procedure** — only that the PM is appointed by the President (Art. 75).\n"
            "- **Convention (rule):** appoint the leader of the majority party in the Lok Sabha.\n"
            "- **Discretion (exception):** hung House / no clear majority — usually largest party or "
            "coalition leader, then vote of confidence (e.g. Charan Singh, 1979).\n"
            "- **Sudden death, no successor:** President may use judgement "
            "(Rajiv Gandhi 1984 vs earlier Nanda caretaker precedent after Nehru / Shastri).\n"
            "- If the ruling party elects a new leader after a PM’s death, the President **must** appoint that leader.\n\n"
            "### High-yield facts\n"
            "- Delhi HC (1980): need **not** prove majority *before* appointment — may prove later.\n"
            "- SC (1996): a **non-MP** can be PM for **six months**; must join either House or ceases to be PM.\n"
            "- PM may be from **either House** (Indira 1966, Deve Gowda 1996, Manmohan Singh 2004 from RS). "
            "Britain: PM must be from the Commons.\n"
        ),
        "articles": [
            (
                "Art. 75",
                "The Prime Minister shall be appointed by the President.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pm-appointment-flow",
                "type": "flowchart",
                "title": "Who becomes PM?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Does any party have a clear LS majority?",
                        "detail": "Start from Lok Sabha arithmetic, not presidential whim.",
                        "options": [
                            {"label": "Yes — clear majority", "next": "majority"},
                            {"label": "No — hung House", "next": "hung"},
                            {"label": "PM dies; no obvious successor", "next": "death"},
                        ],
                    },
                    {
                        "id": "majority",
                        "label": "Appoint majority leader",
                        "detail": "President has no real choice — parliamentary convention binds.",
                    },
                    {
                        "id": "hung",
                        "label": "Limited discretion",
                        "detail": (
                            "Usually largest party/coalition leader; ask for confidence vote "
                            "(e.g. Charan Singh 1979)."
                        ),
                    },
                    {
                        "id": "death",
                        "label": "Individual judgement possible",
                        "detail": (
                            "If party elects a leader → must appoint. Else discretion "
                            "(Rajiv 1984; earlier Nanda caretaker after Nehru/Shastri)."
                        ),
                    },
                ],
            },
            {
                "id": "pm-appointment-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam traps",
                "body": (
                    "President is not free to appoint anyone when there is a clear majority. "
                    "Non-MP PM → max 6 months. India allows PM from Rajya Sabha; Britain does not. "
                    "Majority need not be proved before appointment."
                ),
            },
        ],
    },
    {
        "title": "Oath, Term & Salary",
        "slug": "pm-oath-term",
        "sort_order": 3,
        "summary": (
            "Office and secrecy oaths before the President; tenure during pleasure but "
            "tied to Lok Sabha confidence; salary fixed by Parliament."
        ),
        "body": (
            "## Oaths\n"
            "Before entering office, the President administers oaths of **office** and **secrecy** "
            "(same form as any Union minister).\n\n"
            "### Oath of office (four points)\n"
            "1. True faith and allegiance to the Constitution\n"
            "2. Uphold sovereignty and integrity of India\n"
            "3. Faithfully discharge duties of office\n"
            "4. Do right to all people per Constitution and law — without fear or favour, "
            "affection or ill will\n\n"
            "### Oath of secrecy\n"
            "Not to reveal information known as a Union minister except for due discharge of duties.\n\n"
            "## Term\n"
            "- Not fixed — holds office during the **pleasure of the President**.\n"
            "- Pleasure ≠ arbitrary dismissal: while the PM enjoys **Lok Sabha majority**, "
            "the President cannot dismiss.\n"
            "- Lose confidence → must resign, or the President may dismiss "
            "(e.g. V.P. Singh 1990; Deve Gowda 1997).\n\n"
            "## Salary\n"
            "Determined by Parliament (Salaries and Allowances of Ministers Act, 1952) — "
            "MP pay plus ministerial allowances and facilities.\n"
        ),
        "articles": [
            (
                "Art. 75",
                "Ministers hold office during the pleasure of the President; collective responsibility to Lok Sabha.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pm-oath-pillars",
                "type": "pillars",
                "title": "Four points of the oath of office",
                "items": [
                    {
                        "id": "allegiance",
                        "articles": "1",
                        "label": "Allegiance",
                        "slug": "pm-oath-term",
                        "detail": "True faith and allegiance to the Constitution of India.",
                        "tone": "teal",
                    },
                    {
                        "id": "sovereignty",
                        "articles": "2",
                        "label": "Sovereignty & integrity",
                        "slug": "pm-oath-term",
                        "detail": "Uphold the sovereignty and integrity of India.",
                        "tone": "olive",
                    },
                    {
                        "id": "duties",
                        "articles": "3",
                        "label": "Discharge duties",
                        "slug": "pm-oath-term",
                        "detail": "Faithfully and conscientiously discharge the duties of office.",
                        "tone": "gold",
                    },
                    {
                        "id": "right",
                        "articles": "4",
                        "label": "Do right to all",
                        "slug": "pm-oath-term",
                        "detail": "Without fear or favour, affection or ill will — per Constitution and law.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "pm-oath-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "‘Pleasure of the President’ does not mean the President can sack a majority PM. "
                    "Confidence of the Lok Sabha is the real tenure lock."
                ),
            },
        ],
    },
    {
        "title": "Powers vs Council of Ministers",
        "slug": "pm-powers-com",
        "sort_order": 4,
        "summary": (
            "As head of the Union Council of Ministers, the PM recommends, allocates, "
            "controls, and can collapse the ministry."
        ),
        "body": (
            "## Six powers (R-A-D-P-G-C)\n\n"
            "1. **Recommend** persons for appointment as ministers — President can appoint "
            "only those recommended by the PM.\n"
            "2. **Allocate / reshuffle** portfolios among ministers.\n"
            "3. **Dismiss** — ask a minister to resign or advise the President to dismiss "
            "in case of difference of opinion.\n"
            "4. **Preside** over meetings of the Council of Ministers and influence decisions.\n"
            "5. **Guide**, direct, control, and coordinate all ministers.\n"
            "6. **Collapse** the Council by resigning from office.\n\n"
            "### Vacuum vs vacancy\n"
            "- **Resignation or death of the PM** → entire Council of Ministers dissolves (vacuum).\n"
            "- **Resignation or death of any other minister** → only a vacancy the PM may fill.\n\n"
            "**Mnemonic:** R-A-D-P-G-C — Recommend, Allocate, Dismiss, Preside, Guide, Collapse."
        ),
        "articles": [
            (
                "Art. 75",
                "Other ministers are appointed by the President on the advice of the Prime Minister.",
            ),
            (
                "Art. 74",
                "Council of Ministers with the Prime Minister at the head.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pm-com-pillars",
                "type": "pillars",
                "title": "Six powers over the Council of Ministers",
                "items": [
                    {
                        "id": "recommend",
                        "articles": "R",
                        "label": "Recommend",
                        "slug": "pm-powers-com",
                        "detail": "President appoints only ministers recommended by the PM.",
                        "tone": "teal",
                    },
                    {
                        "id": "allocate",
                        "articles": "A",
                        "label": "Allocate",
                        "slug": "pm-powers-com",
                        "detail": "Assign and reshuffle portfolios among ministers.",
                        "tone": "olive",
                    },
                    {
                        "id": "dismiss",
                        "articles": "D",
                        "label": "Dismiss",
                        "slug": "pm-powers-com",
                        "detail": "Force resignation or advise presidential dismissal.",
                        "tone": "gold",
                    },
                    {
                        "id": "preside",
                        "articles": "P",
                        "label": "Preside",
                        "slug": "pm-powers-com",
                        "detail": "Chairs CoM meetings and shapes decisions.",
                        "tone": "orange",
                    },
                    {
                        "id": "guide",
                        "articles": "G",
                        "label": "Guide",
                        "slug": "pm-powers-com",
                        "detail": "Guides, directs, controls, and coordinates ministers.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "collapse",
                        "articles": "C",
                        "label": "Collapse",
                        "slug": "pm-powers-com",
                        "detail": "PM’s resignation dissolves the whole Council.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pm-com-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Vacuum vs vacancy",
                "body": (
                    "PM resigns or dies → vacuum: whole CoM falls. "
                    "Any other minister resigns or dies → vacancy only. Classic Prelims distinction."
                ),
            },
        ],
    },
    {
        "title": "Powers vs the President",
        "slug": "pm-powers-president",
        "sort_order": 5,
        "summary": (
            "The PM is the principal channel between the President and the Council of Ministers "
            "(Art. 78) and advises key constitutional appointments."
        ),
        "body": (
            "## Principal channel (Art. 78)\n\n"
            "It is the duty of the Prime Minister:\n"
            "(a) to communicate to the President all CoM decisions on Union administration "
            "and proposals for legislation;\n"
            "(b) to furnish information the President may call for on those matters; and\n"
            "(c) if the President so requires, to submit for CoM consideration any matter "
            "decided by a minister but not yet considered by the Council.\n\n"
            "## Advice on appointments\n"
            "PM advises the President on important officials — Attorney General, CAG, "
            "UPSC chair and members, Election Commissioners, Finance Commission chair and "
            "members, and similar posts.\n"
        ),
        "articles": [
            (
                "Art. 78",
                "Duties of the Prime Minister as respects the furnishing of information to the President, etc.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pm-art78-explorer",
                "type": "article_explorer",
                "title": "Article 78 explorer",
                "article_ref": "Article 78",
                "stages": [
                    {
                        "id": "communicate",
                        "label": "78(a) Communicate",
                        "detail": "All CoM decisions on Union affairs and legislative proposals go to the President.",
                    },
                    {
                        "id": "furnish",
                        "label": "78(b) Furnish",
                        "detail": "Supply any related information the President calls for.",
                    },
                    {
                        "id": "submit",
                        "label": "78(c) Submit to CoM",
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
                            "collective responsibility."
                        ),
                    },
                ],
            },
            {
                "id": "pm-appointments-pillars",
                "type": "pillars",
                "title": "Key appointments advised by the PM",
                "items": [
                    {
                        "id": "ag",
                        "articles": "AG",
                        "label": "Attorney General",
                        "slug": "pm-powers-president",
                        "detail": "Chief legal adviser to the Government of India.",
                        "tone": "teal",
                    },
                    {
                        "id": "cag",
                        "articles": "CAG",
                        "label": "CAG",
                        "slug": "pm-powers-president",
                        "detail": "Comptroller and Auditor General of India.",
                        "tone": "olive",
                    },
                    {
                        "id": "upsc",
                        "articles": "UPSC",
                        "label": "UPSC",
                        "slug": "pm-powers-president",
                        "detail": "Chairman and members of the Union Public Service Commission.",
                        "tone": "gold",
                    },
                    {
                        "id": "ec",
                        "articles": "EC",
                        "label": "Election Commission",
                        "slug": "pm-powers-president",
                        "detail": "Election Commissioners (appointment advice).",
                        "tone": "orange",
                    },
                    {
                        "id": "fc",
                        "articles": "FC",
                        "label": "Finance Commission",
                        "slug": "pm-powers-president",
                        "detail": "Chairman and members of the Finance Commission.",
                        "tone": "terracotta",
                    },
                ],
            },
            {
                "id": "pm-pres-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Prelims fact",
                "body": (
                    "Art. 78 = PM’s communication duties to the President. "
                    "Pair it with Art. 74 (aid & advice) and Art. 75 (appointment / responsibility)."
                ),
            },
        ],
    },
    {
        "title": "Parliament & Other Roles",
        "slug": "pm-powers-parliament",
        "sort_order": 6,
        "summary": (
            "As leader of the Lower House and political head of the system, the PM links "
            "Parliament, party, policy, and crisis management."
        ),
        "body": (
            "## In relation to Parliament\n"
            "1. Advises the President on **summoning and proroguing** sessions.\n"
            "2. Can recommend **dissolution of the Lok Sabha** at any time.\n"
            "3. Announces government policies on the floor of the House.\n\n"
            "## Other powers & functions\n"
            "- Chair: **NITI Aayog**, National Integration Council, Inter-State Council, "
            "National Water Resources Council, and other bodies.\n"
            "- Shapes **foreign policy**; chief spokesman of the Union government.\n"
            "- **Crisis manager-in-chief** at the political level during emergencies.\n"
            "- Leader of the nation (receives public memoranda), leader of the party in power, "
            "and political head of the services.\n\n"
            "### Bridge to next stop\n"
            "These roles explain why observers speak of **prime ministerial government** — "
            "not merely a cabinet of equals."
        ),
        "articles": [
            (
                "Art. 75",
                "Collective responsibility of the Council of Ministers to the House of the People.",
            ),
            (
                "Art. 88",
                "Rights of Ministers as respects the Houses of Parliament.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pm-parl-pillars",
                "type": "pillars",
                "title": "Three parliamentary levers",
                "items": [
                    {
                        "id": "summon",
                        "articles": "1",
                        "label": "Summon / prorogue",
                        "slug": "pm-powers-parliament",
                        "detail": "Advises the President on calling and ending sessions.",
                        "tone": "teal",
                    },
                    {
                        "id": "dissolve",
                        "articles": "2",
                        "label": "Dissolve Lok Sabha",
                        "slug": "pm-powers-parliament",
                        "detail": "May recommend dissolution of the Lower House at any time.",
                        "tone": "olive",
                    },
                    {
                        "id": "announce",
                        "articles": "3",
                        "label": "Announce policy",
                        "slug": "pm-powers-parliament",
                        "detail": "States government policy on the floor of the House.",
                        "tone": "gold",
                    },
                ],
            },
            {
                "id": "pm-other-pillars",
                "type": "pillars",
                "title": "Other hats (scan)",
                "items": [
                    {
                        "id": "chair",
                        "articles": "Bodies",
                        "label": "Chair of key bodies",
                        "slug": "pm-powers-parliament",
                        "detail": "NITI Aayog, NIC, Inter-State Council, NWRC, and more.",
                        "tone": "orange",
                    },
                    {
                        "id": "foreign",
                        "articles": "External",
                        "label": "Foreign policy",
                        "slug": "pm-powers-parliament",
                        "detail": "Central role in shaping India’s external posture.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "crisis",
                        "articles": "Emergency",
                        "label": "Crisis manager",
                        "slug": "pm-powers-parliament",
                        "detail": "Political crisis manager-in-chief during emergencies.",
                        "tone": "maroon",
                    },
                    {
                        "id": "party-services",
                        "articles": "Power",
                        "label": "Party & services",
                        "slug": "pm-powers-parliament",
                        "detail": "Leader of the party in power; political head of the services.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "pm-parl-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Mains VA",
                "body": (
                    "Ambedkar’s US-President comparison + these multi-hats roles support the "
                    "‘prime ministerial government’ thesis — use in essays on parliamentary practice."
                ),
            },
        ],
    },
    {
        "title": "Role Descriptions",
        "slug": "pm-role-descriptions",
        "sort_order": 7,
        "summary": (
            "British theorists’ labels for the PM — from primus inter pares to "
            "prime ministerial government — also fit India."
        ),
        "body": (
            "## Must-recall phrases\n\n"
            "| Thinker | Label |\n"
            "|---|---|\n"
            "| Lord Morley | *primus inter pares* (first among equals); keystone of the cabinet arch |\n"
            "| Harcourt | *inter stellas luna minores* (moon among lesser stars) |\n"
            "| Jennings | Sun around which planets revolve; keystone of the constitution |\n"
            "| Laski | Central to cabinet’s formation, life, and death; pivot of government |\n"
            "| Greaves | Master of the Government |\n"
            "| Munro | Captain of the ship of the state |\n"
            "| Ramsay Muir | Steersman of the ship of the state |\n\n"
            "### Cabinet → prime ministerial government\n"
            "Crossman and others argue post-war practice transformed cabinet government into "
            "**prime ministerial government**. The same reading is often applied to India.\n\n"
            "**Three phrases to lock:** primus inter pares · moon among stars · captain of the ship."
        ),
        "articles": [],
        "visual_blocks": [
            {
                "id": "pm-role-compare",
                "type": "comparison",
                "title": "Classical vs modern reading",
                "columns": [
                    {
                        "id": "classical",
                        "heading": "Classical (cabinet equals)",
                        "points": [
                            "Primus inter pares — first among equals (Morley)",
                            "Keystone of the cabinet arch",
                            "Chair and coordinator more than boss",
                        ],
                    },
                    {
                        "id": "modern",
                        "heading": "Modern (PM-dominant)",
                        "points": [
                            "Sun / moon among lesser stars (Jennings / Harcourt)",
                            "Central to formation, life, and death of cabinet (Laski)",
                            "Prime ministerial government (Crossman et al.)",
                        ],
                    },
                ],
            },
            {
                "id": "pm-role-memory",
                "type": "callout",
                "tone": "tip",
                "title": "Memory box",
                "body": (
                    "Lock three: (1) primus inter pares, (2) moon among lesser stars, "
                    "(3) captain of the ship. Then add: India too is often called a "
                    "prime ministerial government in practice."
                ),
            },
        ],
    },
    {
        "title": "Relations, Caretaker & Articles",
        "slug": "pm-relations-extras",
        "sort_order": 8,
        "summary": (
            "Art. 74–75–78 relationship spine, caretaker government limits, six CM→PM names, "
            "and Table 20.1 articles at a glance."
        ),
        "body": (
            "## Relationship with the President\n"
            "- **Art. 74** — CoM with PM at the head aids and advises; President may require "
            "reconsideration once, then must act on the advice.\n"
            "- **Art. 75** — PM appointed by President; other ministers on PM’s advice; "
            "pleasure of President; **collective responsibility to Lok Sabha**.\n"
            "- **Art. 78** — PM’s duties to communicate / furnish / submit matters to the CoM.\n"
            "- Also revise: **Art. 77** (conduct of business of the GoI), **Art. 88** "
            "(ministers’ rights in the Houses).\n\n"
            "## Caretaker government\n"
            "- **Not in the Constitution** — situational / functional necessity.\n"
            "- Two meanings: (1) after dissolution till a new ministry; "
            "(2) resigned ministry asked to continue till alternative arrangements.\n"
            "- Role is **limited** — routine / day-to-day; no major new policy "
            "(Tarkunde Committee; 1979 Reddy communique; Calcutta HC).\n\n"
            "## CM → PM (six names)\n"
            "Morarji Desai · Charan Singh · V.P. Singh · P.V. Narasimha Rao · "
            "H.D. Deve Gowda · Narendra Modi.\n\n"
            "**Mnemonic:** M-C-V-N-D-M — *My CM Visit Needs Decisive Mandate*.\n"
            "- Rao = first South Indian PM; Modi = four-term Gujarat CM before 2014.\n"
        ),
        "articles": [
            (
                "Art. 74",
                "Council of Ministers to aid and advise the President; advice binding after reconsideration.",
            ),
            (
                "Art. 75",
                "Appointment, pleasure, and collective responsibility of ministers.",
            ),
            (
                "Art. 77",
                "Conduct of business of the Government of India.",
            ),
            (
                "Art. 78",
                "Duties of the Prime Minister as respects information to the President.",
            ),
            (
                "Art. 88",
                "Rights of Ministers as respects the Houses.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "pm-articles-compare",
                "type": "comparison",
                "title": "Articles related to the PM (Table 20.1)",
                "columns": [
                    {
                        "id": "core",
                        "heading": "Core triad",
                        "points": [
                            "74 — CoM aids and advises the President",
                            "75 — Appointment, pleasure, collective responsibility",
                            "78 — PM’s information duties to the President",
                        ],
                    },
                    {
                        "id": "support",
                        "heading": "Also revise",
                        "points": [
                            "77 — Conduct of business of the GoI",
                            "88 — Ministers’ rights in the Houses",
                            "42nd + 44th — advice to President is binding",
                        ],
                    },
                ],
            },
            {
                "id": "pm-caretaker-flow",
                "type": "flowchart",
                "title": "When is it a caretaker government?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What happened?",
                        "detail": "Caretaker is convention + necessity — not a constitutional office.",
                        "options": [
                            {"label": "Lok Sabha dissolved; polls pending", "next": "dissolved"},
                            {"label": "Ministry resigned / lost confidence", "next": "resigned"},
                            {"label": "New ministry already sworn in", "next": "normal"},
                        ],
                    },
                    {
                        "id": "dissolved",
                        "label": "Caretaker till new government",
                        "detail": "Hold free and fair polls; manage routine affairs only.",
                    },
                    {
                        "id": "resigned",
                        "label": "Asked to continue temporarily",
                        "detail": (
                            "President may ask outgoing CoM to continue till alternative "
                            "arrangements or elections conclude."
                        ),
                    },
                    {
                        "id": "normal",
                        "label": "Regular government",
                        "detail": "Full policy mandate — not a caretaker situation.",
                    },
                ],
            },
            {
                "id": "pm-cm-pillars",
                "type": "pillars",
                "title": "Six Chief Ministers who became PM",
                "items": [
                    {
                        "id": "desai",
                        "articles": "M",
                        "label": "Morarji Desai",
                        "slug": "pm-relations-extras",
                        "detail": "Bombay CM → first non-Congress PM (1977).",
                        "tone": "teal",
                    },
                    {
                        "id": "charan",
                        "articles": "C",
                        "label": "Charan Singh",
                        "slug": "pm-relations-extras",
                        "detail": "UP CM → PM after Janata fall (1979).",
                        "tone": "olive",
                    },
                    {
                        "id": "vp",
                        "articles": "V",
                        "label": "V.P. Singh",
                        "slug": "pm-relations-extras",
                        "detail": "UP CM → National Front PM (1989–90).",
                        "tone": "gold",
                    },
                    {
                        "id": "rao",
                        "articles": "N",
                        "label": "Narasimha Rao",
                        "slug": "pm-relations-extras",
                        "detail": "AP CM → first South Indian PM (1991–96).",
                        "tone": "orange",
                    },
                    {
                        "id": "gowda",
                        "articles": "D",
                        "label": "Deve Gowda",
                        "slug": "pm-relations-extras",
                        "detail": "Karnataka CM → United Front PM (1996).",
                        "tone": "terracotta",
                    },
                    {
                        "id": "modi",
                        "articles": "M",
                        "label": "Narendra Modi",
                        "slug": "pm-relations-extras",
                        "detail": "Four-term Gujarat CM → PM (2014).",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pm-caretaker-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Caretaker limits",
                "body": (
                    "No constitutional provision for ‘caretaker government’. "
                    "Expect only day-to-day administration — not major new policies, projects, "
                    "or big spending (Tarkunde / Reddy 1979 / Calcutta HC)."
                ),
            },
            {
                "id": "pm-pyq-themes",
                "type": "callout",
                "tone": "note",
                "title": "PYQ themes",
                "body": (
                    "Appointment discretion in hung Houses; Art. 74/75/78 triad; "
                    "PM from Rajya Sabha; 6-month non-MP rule; vacuum vs vacancy; "
                    "caretaker’s limited mandate; CM→PM list."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "pm-position"),
    (HUB_SLUG, "parent", "pm-appointment"),
    (HUB_SLUG, "parent", "pm-oath-term"),
    (HUB_SLUG, "parent", "pm-powers-com"),
    (HUB_SLUG, "parent", "pm-powers-president"),
    (HUB_SLUG, "parent", "pm-powers-parliament"),
    (HUB_SLUG, "parent", "pm-role-descriptions"),
    (HUB_SLUG, "parent", "pm-relations-extras"),
    ("pm-position", "related", "pm-appointment"),
    ("pm-appointment", "related", "pm-oath-term"),
    ("pm-powers-com", "related", "pm-powers-president"),
    ("pm-powers-president", "related", "pm-powers-parliament"),
    ("pm-powers-parliament", "related", "pm-role-descriptions"),
    ("pm-role-descriptions", "related", "pm-relations-extras"),
    ("pm-powers-com", "related", "pm-relations-extras"),
    (HUB_SLUG, "related", "parliamentary-system"),
    (HUB_SLUG, "related", "ps-features"),
    (HUB_SLUG, "related", "cabinet"),
    (HUB_SLUG, "related", "council-of-ministers"),
    (HUB_SLUG, "related", "president"),
    (HUB_SLUG, "related", "collective-responsibility"),
]

AMENDMENTS = [
    {
        "number": 42,
        "year": 1976,
        "title": "Forty-second Amendment",
        "summary": (
            "Among other changes, strengthened the position that the President acts on "
            "the aid and advice of the Council of Ministers."
        ),
        "effect": "With the 44th Amendment, ministerial advice to the President is binding.",
        "concept_slugs": [HUB_SLUG, "pm-relations-extras", "pm-powers-president"],
    },
    {
        "number": 44,
        "year": 1978,
        "title": "Forty-fourth Amendment",
        "summary": (
            "Restored and clarified the binding character of ministerial advice to the President "
            "after Emergency-era changes."
        ),
        "effect": "Together with the 42nd Amendment, advice under Art. 74 is binding.",
        "concept_slugs": [HUB_SLUG, "pm-relations-extras", "pm-powers-president"],
    },
]


class Command(BaseCommand):
    help = "Seed Prime Minister chapter (Laxmikanth Ch.20)."

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
                "title": "Prime Minister",
                "sort_order": 3,
                "book_ref": "Laxmikanth 8th Ed, Ch. 20 (pp. 308–314)",
                "summary": (
                    "Visual revision of Ch.20 — appointment, oath/tenure, powers vs "
                    "CoM/President/Parliament, role descriptions, caretaker, and articles."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Prime Minister",
                "summary": (
                    "Real executive of the Union — head of government under Arts 74, 75, and 78; "
                    "leader of the Council of Ministers and of the Lok Sabha majority in practice."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **captain of the ship** mental model, then "
                    "**Position** → **Appointment** → **Oath & term**. "
                    "Drill **powers** (CoM → President → Parliament), then "
                    "**role quotes** and **relations / caretaker / articles**. "
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
            ref="Laxmikanth Ch. 20",
            excerpt=(
                "Prime Minister — appointment, powers, relations with President and CoM, "
                "caretaker government, Arts 74–75–78."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 74 & 75",
            excerpt=(
                "CoM headed by PM aids and advises; PM appointed by President; "
                "collective responsibility to Lok Sabha."
            ),
            sort_order=1,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Art. 78",
            excerpt="Duties of the PM to communicate and furnish information to the President.",
            sort_order=2,
        )

        from django.db.models import Q

        pm_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            Q(source__slug__in=pm_slugs) | Q(target__slug__in=pm_slugs),
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

        for amd_data in AMENDMENTS:
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
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Prime Minister chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(AMENDMENTS)} amendments linked."
            )
        )
