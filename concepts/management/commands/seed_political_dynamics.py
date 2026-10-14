"""Seed Laxmikanth Part X Political Dynamics (visual revision chapter)."""

from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import (
    CaseLaw,
    Concept,
    ConceptArticle,
    ConceptEdge,
    ConstitutionalAmendment,
)
from questions.models import PYQ
from subjects.models import Chapter, Section, Subject

HUB_SLUG = "political-dynamics"
CHAPTER_SLUG = "political-dynamics"

ENTRY_PILLARS = [
    {
        "id": "parties",
        "articles": "Ch.79 · 804–809",
        "label": "Political Parties",
        "slug": "pd-political-parties",
        "detail": "Party system · registration · national vs state · symbols.",
        "tone": "teal",
    },
    {
        "id": "regional",
        "articles": "Ch.80 · 810–812",
        "label": "Regional Parties",
        "slug": "pd-regional-parties",
        "detail": "Causes · federalism · coalition kingmakers · dysfunctions.",
        "tone": "olive",
    },
    {
        "id": "elections",
        "articles": "Ch.81 · 813–820",
        "label": "Elections",
        "slug": "pd-elections",
        "detail": "Arts 324–329 · process · EVM–VVPAT · MCC · ECI.",
        "tone": "gold",
    },
    {
        "id": "laws",
        "articles": "Ch.82 · 821–824",
        "label": "Election Laws",
        "slug": "pd-election-laws",
        "detail": "RPA 1950/1951 · delimitation · petitions · corrupt practices.",
        "tone": "orange",
    },
    {
        "id": "reforms",
        "articles": "Ch.83 · 825–834",
        "label": "Electoral Reforms",
        "slug": "pd-electoral-reforms",
        "detail": "Committees · funding · criminalization · Bonds judgment.",
        "tone": "terracotta",
    },
    {
        "id": "voting",
        "articles": "Ch.84 · 835–838",
        "label": "Voting Behaviour",
        "slug": "pd-voting-behaviour",
        "detail": "Caste · religion · leadership · media · issue voting.",
        "tone": "maroon",
    },
    {
        "id": "coalition",
        "articles": "Ch.85 · 839–843",
        "label": "Coalition Government",
        "slug": "pd-coalition-government",
        "detail": "NF · NDA · UPA · merits/demerits · management.",
        "tone": "teal",
    },
    {
        "id": "defection",
        "articles": "Ch.86 · 844–848",
        "label": "Anti-Defection Law",
        "slug": "pd-anti-defection",
        "detail": "10th Schedule · 52nd/91st · Speaker · Kihoto.",
        "tone": "olive",
    },
    {
        "id": "pressure",
        "articles": "Ch.87 · 849–853",
        "label": "Pressure Groups",
        "slug": "pd-pressure-groups",
        "detail": "Types · methods · parties vs groups · civil society.",
        "tone": "gold",
    },
    {
        "id": "integration",
        "articles": "Ch.88 · 854–858",
        "label": "National Integration",
        "slug": "pd-national-integration",
        "detail": "Obstacles · NIC · secularism · internal security link.",
        "tone": "orange",
    },
    {
        "id": "fp",
        "articles": "Ch.89 · 859+",
        "label": "Foreign Policy",
        "slug": "pd-foreign-policy",
        "detail": "Art.51 · NAM · Gujral · Act East · doctrines map.",
        "tone": "terracotta",
    },
    {
        "id": "compare",
        "articles": "Master tables",
        "label": "Master Comparisons",
        "slug": "pd-master-comparisons",
        "detail": "Nine high-yield side-by-side contrasts.",
        "tone": "maroon",
    },
    {
        "id": "exam",
        "articles": "Prelims · Mains",
        "label": "Exam Kit",
        "slug": "pd-exam-kit",
        "detail": "Articles · Acts · timelines · traps · one-pager.",
        "tone": "teal",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "pd-os-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Operating system",
        "topic_label": "Political Dynamics",
        "subject_label": "Indian Polity",
        "relation_label": "Runs on",
        "protects_from": [
            "Parties & elections",
            "Voting & coalitions",
            "Anti-defection guardrails",
            "Integration & foreign posture",
        ],
        "insight": (
            "Part X is the political OS of the Constitution — how power is contested, "
            "converted into government, constrained, and projected abroad."
        ),
    },
    {
        "id": "pd-entry-pillars",
        "type": "pillars",
        "title": "Thirteen revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "pd-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Spine: Parties → Elections/Laws/Reforms → Behaviour → Coalitions → "
            "Anti-defection → Pressure groups → Integration → Foreign policy. "
            "Finish with Master Comparisons + Exam Kit. Visual revision — not a Laxmikanth substitute."
        ),
    },
]


def _std_body(sections: dict) -> str:
    """Build markdown body from the standard 12-section skeleton."""
    order = [
        ("Constitutional and Legal Background", "const"),
        ("Historical Evolution", "hist"),
        ("Objectives", "obj"),
        ("Key Features", "feat"),
        ("Institutional Framework", "inst"),
        ("Important Laws and Constitutional Provisions", "laws"),
        ("Committees and Commissions", "comm"),
        ("Important Supreme Court Judgments", "sc"),
        ("Recent Reforms and Current Affairs", "ca"),
        ("Frequently Asked UPSC Themes", "themes"),
        ("Common Prelims Traps", "traps"),
        ("Mains Value Additions", "mains"),
    ]
    parts = [f"## {sections.get('title', 'Topic')}\n"]
    for heading, key in order:
        parts.append(f"### {heading}\n\n{sections[key].strip()}\n")
    return "\n".join(parts)


CLUSTERS = [
    {
        "title": "Political Parties",
        "slug": "pd-political-parties",
        "sort_order": 1,
        "summary": (
            "Indian multi-party system, ECI registration/recognition, national vs state "
            "criteria, symbols, funding and internal democracy essentials."
        ),
        "body": _std_body(
            {
                "title": "Political Parties",
                "const": (
                    "- Parties are voluntary associations seeking power by constitutional means.\n"
                    "- ECI registers parties under **RPA 1951**; recognition as national/state is "
                    "performance-based (Symbols Order / ECI criteria).\n"
                    "- Constitution does not define ‘political party’ in detail — Tenth Schedule "
                    "later gives constitutional recognition to parties for anti-defection."
                ),
                "hist": (
                    "- Pre-independence associations → Congress dominance (‘Congress system’ — "
                    "Rajni Kothari) → post-1967 regional rise → 1977/1989 competitive multi-party "
                    "→ coalition era → contemporary bipolar contests with strong regional players."
                ),
                "obj": (
                    "- Aggregate interests; contest elections; form government/opposition; "
                    "socialise citizens into democratic politics; provide leadership."
                ),
                "feat": (
                    "- **Indian party system hallmarks:** multi-party; one-dominant phase; weak "
                    "ideology (except a few); personality cult; traditional bases "
                    "(caste/religion/language); regional parties; factions/defections; weak "
                    "national opposition historically.\n"
                    "- World types: one-party / two-party / multi-party — India is multi-party."
                ),
                "inst": (
                    "- **Election Commission:** registration, recognition, symbols, broadcasts "
                    "time, electoral-roll access privileges for recognised parties.\n"
                    "- Categories: **National**, **State (regional)**, **Registered-unrecognised**."
                ),
                "laws": (
                    "- **RPA 1951** — registration of political parties.\n"
                    "- ECI Symbols Order — reserved vs free symbols.\n"
                    "- **National party (any one):** (1) 6% votes in ≥4 states + 4 LS seats; "
                    "(2) 2% LS seats from ≥3 states; (3) state party in 4 states.\n"
                    "- **State party (any one):** 6%+2 assembly seats; 6%+1 LS seat from state; "
                    "3% assembly seats or 3 seats (whichever more); 1 LS seat per 25 allotted; "
                    "or **8%** votes in state (LS or assembly)."
                ),
                "comm": (
                    "- ECI guidelines on party constitution, internal elections, and financial "
                    "disclosure (exam essentials).\n"
                    "- Law Commission / ARC reports often urge stronger **internal democracy**."
                ),
                "sc": (
                    "- Funding/transparency line often linked to **ADR** litigation (candidate "
                    "affidavits; later electoral bonds — see Reforms cluster).\n"
                    "- Symbol disputes decided with high deference to ECI expertise."
                ),
                "ca": (
                    "- Recognition numbers change after each general election (book: 7 national / "
                    "52 state on eve of 2019 LS).\n"
                    "- Ongoing debates: party funding transparency, opaque donations, "
                    "internal democracy, star-campaigner norms."
                ),
                "themes": (
                    "- National vs state recognition criteria (numbers).\n"
                    "- Reserved vs free symbols.\n"
                    "- Features of Indian party system; ‘Congress system’."
                ),
                "traps": (
                    "- **Registration ≠ recognition.**\n"
                    "- 8% vote route is for **state** party, not national.\n"
                    "- National route needs **four LS seats** with the 6%-in-4-states path — "
                    "not four state assemblies."
                ),
                "mains": (
                    "- Link weak ideology + personality cult to coalition bargaining.\n"
                    "- Argue internal democracy as missing link for accountable politics."
                ),
            }
        ),
        "articles": [
            ("Laxmikanth Ch. 79", "Political parties — system features, recognition, symbols."),
            ("RPA 1951", "Registration of political parties; election conduct framework."),
        ],
        "visual_blocks": [
            {
                "id": "pd-party-compare",
                "type": "comparison",
                "title": "National vs State vs Registered-unrecognised",
                "columns": [
                    {
                        "id": "nat",
                        "heading": "National party",
                        "points": [
                            "All-India recognition",
                            "Reserved symbol nationwide",
                            "Broadcast time + roll access",
                            "Any of 3 ECI routes (6%×4+4 seats / 2% LS / state in 4)",
                        ],
                    },
                    {
                        "id": "state",
                        "heading": "State party",
                        "points": [
                            "Recognised in that state",
                            "Reserved symbol in the state",
                            "Same privilege class in state",
                            "Any of 5 ECI routes (incl. 8% votes)",
                        ],
                    },
                    {
                        "id": "unrec",
                        "heading": "Registered-unrecognised",
                        "points": [
                            "Registered under RPA 1951",
                            "Chooses from free symbols",
                            "Fewer statutory privileges",
                            "Can graduate via poll performance",
                        ],
                    },
                ],
            },
            {
                "id": "pd-party-timeline",
                "type": "timeline",
                "title": "Party-system phases",
                "events": [
                    {
                        "id": "e1",
                        "year": 1952,
                        "label": "Congress system",
                        "detail": "One-dominant party; multi-party formally.",
                    },
                    {
                        "id": "e2",
                        "year": 1967,
                        "label": "Regional rise",
                        "detail": "Post-4th general election — defections & state alternatives.",
                    },
                    {
                        "id": "e3",
                        "year": 1989,
                        "label": "Coalition era",
                        "detail": "Hung LS becomes common; regional parties as kingmakers.",
                    },
                    {
                        "id": "e4",
                        "year": 2014,
                        "label": "Competitive multi-party",
                        "detail": "Strong national poles + enduring regional bargains.",
                    },
                ],
            },
            {
                "id": "pd-party-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Register (RPA) → Recognise (ECI poll criteria) → Symbol (reserved/free). "
                    "National: 6% in 4 states + 4 LS seats OR 2% LS from 3 states OR state party "
                    "in 4 states. State: remember the lone **8% votes** shortcut."
                ),
            },
        ],
    },
    {
        "title": "Role of Regional Parties",
        "slug": "pd-regional-parties",
        "sort_order": 2,
        "summary": (
            "Features, classification, causes, federal impact, coalition role, and "
            "dysfunctions of regional parties."
        ),
        "body": _std_body(
            {
                "title": "Role of Regional Parties",
                "const": (
                    "- Operate mainly within a state/region; seek state power and greater autonomy "
                    "within the Union.\n"
                    "- Recognised as **state parties** by ECI when criteria met."
                ),
                "hist": (
                    "- Early confinement to state politics → post-1967 expansion → decisive "
                    "national role after hung Parliaments and coalition governments."
                ),
                "obj": (
                    "- Articulate regional aspirations; check over-centralisation; provide "
                    "governance alternatives at state level; bargain in national coalitions."
                ),
                "feat": (
                    "- Regional base; identity (culture/ethnicity/language); local grievances; "
                    "state-power focus; autonomy demand.\n"
                    "- **Classification:** ethnicity/culture-based; all-India outlook but weak "
                    "national base; split-offs from nationals; personality-based parties."
                ),
                "inst": (
                    "- State governments; NDA/UPA-type alliances; Inter-State Council / federal "
                    "bargaining arenas; Rajya Sabha influence via state politics."
                ),
                "laws": (
                    "- Same recognition/symbols framework as state parties.\n"
                    "- Coalition CMPs and Common Minimum Programmes as political (not statutory) tools."
                ),
                "comm": (
                    "- Sarkaria / Punchhi themes on Centre–state relations often referenced when "
                    "discussing regional party impact on federalism (cross-link, not Part X text)."
                ),
                "sc": (
                    "- Few Part-X-specific party cases; federal disputes and Governor controversies "
                    "often surface where regional parties govern."
                ),
                "ca": (
                    "- Enduring kingmaker potential in hung situations; strong single-state "
                    "dominant parties; alliance fluidity."
                ),
                "themes": (
                    "- Causes of rise; positive role vs dysfunctions; federalism & coalitions."
                ),
                "traps": (
                    "- Regional party ≠ always ‘state party’ in ECI sense (performance needed).\n"
                    "- Not all regional parties are secessionist — most work within the Union."
                ),
                "mains": (
                    "- Balance: deepen democracy & federalism vs regionalism/populism risks.\n"
                    "- Use as bridge answer between party system and coalition politics."
                ),
            }
        ),
        "articles": [
            ("Laxmikanth Ch. 80", "Regional parties — features, causes, role, dysfunctions."),
        ],
        "visual_blocks": [
            {
                "id": "pd-reg-pillars",
                "type": "pillars",
                "title": "Causes · Roles · Dysfunctions",
                "items": [
                    {
                        "id": "causes",
                        "articles": "Why they rise",
                        "label": "Causes",
                        "detail": (
                            "Pluralism · imbalances · identity · linguistic states · "
                            "charisma · Congress centralisation · weak national Opposition."
                        ),
                        "tone": "teal",
                    },
                    {
                        "id": "roles",
                        "articles": "What they add",
                        "label": "Positive roles",
                        "detail": (
                            "State governance · end one-party dominance · federal voice · "
                            "competition · check Centre · coalition partners."
                        ),
                        "tone": "olive",
                    },
                    {
                        "id": "dys",
                        "articles": "Costs",
                        "label": "Dysfunctions",
                        "detail": (
                            "Regional over national · identity politics · inter-state deadlocks · "
                            "populism · bargaining in coalitions."
                        ),
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pd-reg-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Regional parties = federal pressure valves + coalition pivots. "
                    "Mains frame: causes → democratic gains → dysfunctions → reform "
                    "(national interest + cooperative federalism)."
                ),
            },
            {
                "id": "pd-reg-note",
                "type": "callout",
                "tone": "note",
                "title": "Cross-link",
                "body": (
                    "Read with Coalition Government and Federal System — regional parties are "
                    "the hinge between state aspirations and national power-sharing."
                ),
            },
        ],
    },
    {
        "title": "Elections",
        "slug": "pd-elections",
        "sort_order": 3,
        "summary": (
            "Constitutional electoral framework Arts 324–329, process chain, EVM–VVPAT, "
            "MCC, and Election Commission machinery."
        ),
        "body": _std_body(
            {
                "title": "Elections",
                "const": (
                    "- **Art. 324** — ECI superintendence, direction, control of elections.\n"
                    "- **325** — single general electoral roll; no religion/race/caste/sex bar.\n"
                    "- **326** — adult suffrage.\n"
                    "- **327/328** — Parliament / state legislature may make election laws.\n"
                    "- **329** — bar to court interference in electoral matters (petitions via statute)."
                ),
                "hist": (
                    "- First general elections 1951–52 → paper ballots → EVM rollout → "
                    "VVPAT for verifiability; MCC evolves as soft-law discipline."
                ),
                "obj": (
                    "- Free, fair, periodic elections; convert adult franchise into legitimate "
                    "representative government."
                ),
                "feat": (
                    "- FPTP for LS/assemblies; single roll; independent ECI; observers "
                    "(General, Expenditure, Police); MCC during election window."
                ),
                "inst": (
                    "- Election Commission; Chief Electoral Officers; DEOs; Returning Officers; "
                    "observers; political parties and candidates."
                ),
                "laws": (
                    "- Part XV Arts 324–329; RPA 1950/1951 (detailed in next cluster); "
                    "Conduct of Election Rules; MCC (not a statute — ECI enforcement tool)."
                ),
                "comm": (
                    "- ECI is both constitutional authority and reform recommender."
                ),
                "sc": (
                    "- Art. 329 jurisprudence channels challenges to **election petitions** "
                    "after results (not parallel civil suits).\n"
                    "- Courts generally uphold ECI primacy on process integrity."
                ),
                "ca": (
                    "- EVM–VVPAT verification debates; MCC enforcement intensity; "
                    "voter turnout / awareness drives."
                ),
                "themes": (
                    "- Art. 324–329 map; election process steps; EVM advantages; MCC nature."
                ),
                "traps": (
                    "- MCC is **not** an Act of Parliament.\n"
                    "- Art. 329 does not make elections non-justiciable forever — petitions "
                    "lie as per RPA after election."
                ),
                "mains": (
                    "- Free & fair elections as basic structure adjacent theme; ECI independence "
                    "as democracy’s infrastructure."
                ),
            }
        ),
        "articles": [
            ("Arts. 324–329", "Election Commission and electoral constitutional framework."),
            ("Laxmikanth Ch. 81", "Elections — process, machinery, EVM, article map."),
        ],
        "visual_blocks": [
            {
                "id": "pd-elec-flow",
                "type": "flowchart",
                "title": "Election process (revision chain)",
                "root": "notify",
                "steps": [
                    {
                        "id": "notify",
                        "label": "Notification",
                        "detail": "Election schedule notified; MCC typically bites.",
                        "options": [{"label": "Next", "next": "roll"}],
                    },
                    {
                        "id": "roll",
                        "label": "Electoral roll",
                        "detail": "Claims, objections, corrections under RPA 1950 framework.",
                        "options": [{"label": "Next", "next": "nom"}],
                    },
                    {
                        "id": "nom",
                        "label": "Nomination & scrutiny",
                        "detail": "File, scrutinise, withdraw; affidavits & deposits.",
                        "options": [{"label": "Next", "next": "camp"}],
                    },
                    {
                        "id": "camp",
                        "label": "Campaign",
                        "detail": "Speeches, media, expenditure limits, MCC.",
                        "options": [{"label": "Next", "next": "poll"}],
                    },
                    {
                        "id": "poll",
                        "label": "Polling (EVM+VVPAT)",
                        "detail": "Secret ballot via EVM; VVPAT slip verify trail.",
                        "options": [{"label": "Next", "next": "count"}],
                    },
                    {
                        "id": "count",
                        "label": "Counting & result",
                        "detail": "Faster with EVMs; declaration; then petition window.",
                    },
                ],
            },
            {
                "id": "pd-elec-tree",
                "type": "tree",
                "title": "Articles 324–329 map",
                "root": {
                    "id": "pxv",
                    "label": "Part XV — Elections",
                    "children": [
                        {
                            "id": "a324",
                            "label": "324 — ECI control",
                            "detail": "Superintendence, direction, control",
                        },
                        {
                            "id": "a325",
                            "label": "325 — Single roll",
                            "detail": "No religion/race/caste/sex ineligibility",
                        },
                        {
                            "id": "a326",
                            "label": "326 — Adult suffrage",
                            "detail": "18+ (after 61st Amendment)",
                        },
                        {
                            "id": "a327",
                            "label": "327 — Parliament’s power",
                            "detail": "Laws for Union/state elections",
                        },
                        {
                            "id": "a328",
                            "label": "328 — State legislature",
                            "detail": "State election matters (subject to 327)",
                        },
                        {
                            "id": "a329",
                            "label": "329 — Court bar",
                            "detail": "Challenge via election petition statute",
                        },
                    ],
                },
            },
            {
                "id": "pd-elec-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "324 ECI · 325 one roll · 326 adult vote · 327/328 law-making · 329 petition path. "
                    "Process: Notify → Roll → Nominate → Campaign → Poll → Count. "
                    "EVM + VVPAT; MCC = soft law with hard ECI teeth."
                ),
            },
        ],
    },
    {
        "title": "Election Laws",
        "slug": "pd-election-laws",
        "sort_order": 4,
        "summary": (
            "RPA 1950 vs 1951, delimitation, qualifications/disqualifications, corrupt "
            "practices, offences, and election petitions."
        ),
        "body": _std_body(
            {
                "title": "Election Laws",
                "const": (
                    "- Arts 327–329 empower statute-based electoral law and channel disputes.\n"
                    "- Twin pillars: **RPA 1950** (seats, rolls, delimitation hooks) and "
                    "**RPA 1951** (conduct, membership, disputes)."
                ),
                "hist": (
                    "- 1950 Act for rolls/allocation; 1951 Act completes conduct & disputes; "
                    "Delimitation Acts periodically (e.g. **2002**); rules/orders under ECI."
                ),
                "obj": (
                    "- Operationalise free and fair elections; define who votes/contests; "
                    "punish corrupt practices; adjudicate results."
                ),
                "feat": (
                    "- **RPA 1950:** seat allocation; electoral officers; voter qualification; "
                    "rolls; UT Rajya Sabha seats; civil-court bar on some matters.\n"
                    "- **RPA 1951:** qualifications/disqualifications; party registration; "
                    "nomination–poll–counting; expenses; **election petitions to High Court** "
                    "(appeal to SC); corrupt practices & offences; bye-elections."
                ),
                "inst": (
                    "- Parliament (laws); ECI (administration); High Courts (petitions); "
                    "Delimitation Commission (when constituted)."
                ),
                "laws": (
                    "- RPA 1950; RPA 1951; Delimitation Act 2002; Parliament (Prevention of "
                    "Disqualification) Act 1959; Conduct of Election Rules; ECI orders."
                ),
                "comm": (
                    "- Delimitation Commission (statutory, periodic) — distinct from permanent ECI."
                ),
                "sc": (
                    "- Election petition jurisprudence under RPA 1951; corrupt-practice proofs "
                    "are strict."
                ),
                "ca": (
                    "- Election Laws (Amendment) Act, 2021 — Aadhaar linking to electoral roll "
                    "(voluntary/optional framing in debates) as exam-essential reform note."
                ),
                "themes": (
                    "- 1950 vs 1951 split; petition forum; corrupt practice vs electoral offence."
                ),
                "traps": (
                    "- Petitions go to **High Court**, not directly to Supreme Court (appeal later).\n"
                    "- Corrupt practices (election voiding) ≠ all criminal electoral offences."
                ),
                "mains": (
                    "- Clean politics needs both preventive process law and effective petition "
                    "remedy — link to criminalisation reforms."
                ),
            }
        ),
        "articles": [
            ("RPA 1950", "Seats, rolls, electoral officers, delimitation-related provisions."),
            ("RPA 1951", "Conduct, membership, petitions, corrupt practices."),
            ("Laxmikanth Ch. 82", "Election laws overview."),
        ],
        "visual_blocks": [
            {
                "id": "pd-rpa-compare",
                "type": "comparison",
                "title": "RPA 1950 vs RPA 1951",
                "columns": [
                    {
                        "id": "r50",
                        "heading": "RPA 1950",
                        "points": [
                            "Allocation of seats",
                            "Electoral rolls & voter qualifications",
                            "Election officers framework",
                            "Delimitation-related enabling provisions",
                            "Not the full ‘conduct’ statute",
                        ],
                    },
                    {
                        "id": "r51",
                        "heading": "RPA 1951",
                        "points": [
                            "Qualifications / disqualifications of members",
                            "Party registration & election conduct",
                            "Nomination, poll, counting, expenses",
                            "Election petitions (HC → SC)",
                            "Corrupt practices & electoral offences",
                        ],
                    },
                ],
            },
            {
                "id": "pd-corrupt-pillars",
                "type": "pillars",
                "title": "Corrupt practices vs electoral offences",
                "items": [
                    {
                        "id": "cp",
                        "articles": "RPA 1951",
                        "label": "Corrupt practices",
                        "detail": (
                            "Bribery, undue influence, appeal to religion/caste (as defined), "
                            "false statements, etc. — can void election via petition."
                        ),
                        "tone": "terracotta",
                    },
                    {
                        "id": "eo",
                        "articles": "Criminal side",
                        "label": "Electoral offences",
                        "detail": (
                            "Statutory offences (personation, booth capture-related crimes, etc.) "
                            "— criminal liability track."
                        ),
                        "tone": "maroon",
                    },
                    {
                        "id": "pet",
                        "articles": "Remedy",
                        "label": "Election petition",
                        "detail": "Present to High Court; appeal to Supreme Court; civil-court bar.",
                        "tone": "teal",
                    },
                ],
            },
            {
                "id": "pd-laws-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam in 5 Minutes",
                "body": (
                    "1950 = who is on the roll / seats. 1951 = how elections are fought & disputed. "
                    "Petition → HC first. Delimitation Commission ≠ Election Commission."
                ),
            },
        ],
    },
    {
        "title": "Electoral Reforms",
        "slug": "pd-electoral-reforms",
        "sort_order": 5,
        "summary": (
            "Committee trail, reform eras, criminalization, funding, Electoral Bonds "
            "judgment, simultaneous elections and digital campaigning essentials."
        ),
        "body": _std_body(
            {
                "title": "Electoral Reforms",
                "const": (
                    "- Reforms flow through constitutional practice, RPA amendments, ECI "
                    "instructions, and judicial directions on transparency."
                ),
                "hist": (
                    "- Pre-1996 → **1996 package** → post-1996 → since **2010** (book’s four heads).\n"
                    "- Continuous committee recommendations since Tarkunde / Goswami era."
                ),
                "obj": (
                    "- Reduce money/muscle power; clean candidate field; transparent funding; "
                    "faster disputes; higher integrity of rolls and campaigns."
                ),
                "feat": (
                    "- Affidavits on criminal/assets; expenditure ceilings; paid news concerns; "
                    "NOTA; VVPAT; funding instruments (including historical Electoral Bonds)."
                ),
                "inst": (
                    "- Parliament; ECI; Law Commission; judiciary (disclosure & funding cases)."
                ),
                "laws": (
                    "- Successive RPA amendments; Finance Acts (Bonds scheme historically); "
                    "Election Laws (Amendment) Act 2021."
                ),
                "comm": (
                    "- **Must-remember list:** Tarkunde; Dinesh Goswami (1990); Indrajit Gupta "
                    "(state funding, 1998); Law Commission 170th (1999), 244th (2014), 255th "
                    "(2015); NCRWC (Venkatachaliah); ECI 2004 proposals; 2nd ARC Ethics; "
                    "Tankha (2010); J.S. Verma (2013)."
                ),
                "sc": (
                    "- **ADR / PUCL** line — candidate disclosure.\n"
                    "- **Electoral Bonds** scheme struck down (SC, 2024) — opacity vs voter’s "
                    "right to information (exam essential)."
                ),
                "ca": (
                    "- Simultaneous elections / One Nation One Election debate.\n"
                    "- Digital campaigning, deepfakes, platform regulation — emerging reform basket.\n"
                    "- Criminalization: chargesheeted candidates contesting remains a live issue."
                ),
                "themes": (
                    "- Committee names; criminalization; funding; Bonds judgment; ONOE."
                ),
                "traps": (
                    "- Bonds were a **scheme** (not a constitutional amendment) — now invalidated.\n"
                    "- State funding recommended (Gupta) ≠ fully implemented."
                ),
                "mains": (
                    "- Structure: problem (money/muscle/opacity) → committee ideas → judicial "
                    "push → incomplete political will. Close with practical reform package."
                ),
            }
        ),
        "articles": [
            ("Laxmikanth Ch. 83", "Electoral reforms — committees and reform eras."),
        ],
        "visual_blocks": [
            {
                "id": "pd-reform-timeline",
                "type": "timeline",
                "title": "Electoral reforms timeline (exam spine)",
                "events": [
                    {
                        "id": "r1",
                        "year": 1990,
                        "label": "Goswami Committee",
                        "detail": "Major electoral reform blueprint.",
                    },
                    {
                        "id": "r2",
                        "year": 1996,
                        "label": "1996 reforms",
                        "detail": "Book’s landmark reform package year.",
                    },
                    {
                        "id": "r3",
                        "year": 1998,
                        "label": "Indrajit Gupta",
                        "detail": "State funding of elections report.",
                    },
                    {
                        "id": "r4",
                        "year": 2010,
                        "label": "Reforms since 2010",
                        "detail": "Tankha; later Law Commission 244/255; tech reforms.",
                    },
                    {
                        "id": "r5",
                        "year": 2018,
                        "label": "Electoral Bonds",
                        "detail": "Scheme notified — later struck down (2024).",
                    },
                    {
                        "id": "r6",
                        "year": 2024,
                        "label": "Bonds judgment",
                        "detail": "SC: opaque bonds unconstitutional.",
                    },
                ],
            },
            {
                "id": "pd-reform-pillars",
                "type": "pillars",
                "title": "Four reform baskets",
                "items": [
                    {
                        "id": "crime",
                        "articles": "Muscle",
                        "label": "Criminalization",
                        "detail": "Disclosure, disqualification debates, fast-track trials.",
                        "tone": "maroon",
                    },
                    {
                        "id": "fund",
                        "articles": "Money",
                        "label": "Funding",
                        "detail": "Ceilings, state funding idea, Bonds saga, donor transparency.",
                        "tone": "gold",
                    },
                    {
                        "id": "proc",
                        "articles": "Process",
                        "label": "Process & law",
                        "detail": "Petition speed, MCC bite, simultaneous polls debate.",
                        "tone": "teal",
                    },
                    {
                        "id": "tech",
                        "articles": "Tech",
                        "label": "Technology",
                        "detail": "EVM–VVPAT, digital campaigns, roll–Aadhaar linking debates.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "pd-reform-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Committees: Goswami · Gupta · LC 170/244/255 · NCRWC · ECI · ARC · Tankha. "
                    "Bonds (2018) → SC invalidates (2024). ONOE = debate, not settled law."
                ),
            },
        ],
    },
    {
        "title": "Voting Behaviour",
        "slug": "pd-voting-behaviour",
        "sort_order": 6,
        "summary": (
            "Meaning, significance, and determinants of voting behaviour — social, "
            "economic, political, and media-leadership factors."
        ),
        "body": _std_body(
            {
                "title": "Voting Behaviour",
                "const": (
                    "- Behavioural dimension of Art. 326 adult franchise — how citizens actually "
                    "choose, not merely the legal right to vote."
                ),
                "hist": (
                    "- Early Congress loyalty → identity mobilisation → performance/anti-incumbency "
                    "waves → media-amplified leadership contests."
                ),
                "obj": (
                    "- Explain election outcomes; design campaigns; assess democratic maturity "
                    "(identity vs issue voting)."
                ),
                "feat": (
                    "- **Determinants:** caste, religion, language, region, personality, money, "
                    "ruling-party performance, party identification, ideology, media, campaign, "
                    "family political background, economic conditions, political events."
                ),
                "inst": (
                    "- Parties, candidates, media, civil society, Election Commission (facilitates "
                    "turnout/awareness)."
                ),
                "laws": (
                    "- Legal frame is neutral adult suffrage; behaviour is socio-political."
                ),
                "comm": (
                    "- Election studies (CSDS etc.) often cited in Mains — optional enrichment."
                ),
                "sc": (
                    "- Not a judgment-heavy topic; link lightly to free-and-fair election ideals."
                ),
                "ca": (
                    "- Social media micro-targeting; issue-based youth voting pockets; "
                    "welfare delivery as performance cue."
                ),
                "themes": (
                    "- List determinants; caste/religion vs development; leadership charisma."
                ),
                "traps": (
                    "- Voting behaviour ≠ electoral system (FPTP).\n"
                    "- No single determinant explains India — always multi-causal."
                ),
                "mains": (
                    "- Group answers: Social | Economic | Political | Media/Leadership. "
                    "End with shift toward issue-based voting as incomplete but desirable."
                ),
            }
        ),
        "articles": [
            ("Laxmikanth Ch. 84", "Voting behaviour — significance and determinants."),
        ],
        "visual_blocks": [
            {
                "id": "pd-vote-pillars",
                "type": "pillars",
                "title": "Determinants — four buckets",
                "items": [
                    {
                        "id": "soc",
                        "articles": "Identity",
                        "label": "Social",
                        "detail": "Caste · religion · language · region · community networks.",
                        "tone": "teal",
                    },
                    {
                        "id": "eco",
                        "articles": "Pocket",
                        "label": "Economic",
                        "detail": "Inflation · jobs · welfare delivery · local development.",
                        "tone": "olive",
                    },
                    {
                        "id": "pol",
                        "articles": "Politics",
                        "label": "Political",
                        "detail": "Party ID · ideology · performance · events · factionalism.",
                        "tone": "gold",
                    },
                    {
                        "id": "med",
                        "articles": "Influence",
                        "label": "Media & leadership",
                        "detail": "Charisma · campaign · media · money · family background.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pd-vote-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Mnemonic **CRRL-PMP-IM**: Caste, Religion, Region/Language, Personality, "
                    "Money, Performance, Party-ID/Ideology, Media. Always say ‘multi-causal’."
                ),
            },
            {
                "id": "pd-vote-note",
                "type": "callout",
                "tone": "note",
                "title": "Mains structure",
                "body": (
                    "Intro (franchise → behaviour) → social → economic → political → media → "
                    "evaluation (identity vs issues) → way forward (civic education, transparency)."
                ),
            },
        ],
    },
    {
        "title": "Coalition Government",
        "slug": "pd-coalition-government",
        "sort_order": 7,
        "summary": (
            "Meaning, features, formation, National Front/NDA/UPA evolution, merits, "
            "demerits, and coalition management."
        ),
        "body": _std_body(
            {
                "title": "Coalition Government",
                "const": (
                    "- Parliamentary system allows ministry commanding LS confidence — may be "
                    "single-party or multi-party coalition.\n"
                    "- No separate ‘coalition article’; governed by conventions + Art. 75/164."
                ),
                "hist": (
                    "- Rare early decades → post-1989 normal → **National Front** → **UF** → "
                    "**NDA** → **UPA** → contemporary patterns (majority or coalition-backed)."
                ),
                "obj": (
                    "- Form a majority where no party alone has seats; accommodate diversity; "
                    "seize/share power via minimum programme."
                ),
                "feat": (
                    "- ≥2 partners; temporary alliance; compromise; CMP; pragmatism over "
                    "rigid ideology; dynamic partners."
                ),
                "inst": (
                    "- Steering/coordination committees; Common Minimum Programme; coalition "
                    "dharma; larger Councils of Ministers historically (capped later by 91st)."
                ),
                "laws": (
                    "- Anti-defection shapes floor stability; 91st Amendment caps ministry size "
                    "(link to Anti-Defection cluster)."
                ),
                "comm": (
                    "- Political, not committee-led topic — NCRWC noted oversized ministries."
                ),
                "sc": (
                    "- Confidence/majority tests and Governor discretion cases sit nearby "
                    "(floor test culture)."
                ),
                "ca": (
                    "- Pre-poll vs post-poll alliances; national parties still need regional "
                    "partners in many states."
                ),
                "themes": (
                    "- Merits/demerits; federalism; NF/NDA/UPA; instability vs accommodation."
                ),
                "traps": (
                    "- Coalition ≠ always unstable (some completed terms).\n"
                    "- CMP is political, not constitutional law."
                ),
                "mains": (
                    "- Thesis: coalitions deepen federal bargain but dilute coherent policy; "
                    "management institutions matter more than moralising instability."
                ),
            }
        ),
        "articles": [
            ("Laxmikanth Ch. 85", "Coalition government — features, formation, merits/demerits."),
        ],
        "visual_blocks": [
            {
                "id": "pd-coal-timeline",
                "type": "timeline",
                "title": "Coalition phases (memory spine)",
                "events": [
                    {
                        "id": "c1",
                        "year": 1989,
                        "label": "National Front",
                        "detail": "Outside support patterns; hung LS politics consolidates.",
                    },
                    {
                        "id": "c2",
                        "year": 1996,
                        "label": "United Front",
                        "detail": "Deve Gowda / Gujral era coalitions.",
                    },
                    {
                        "id": "c3",
                        "year": 1999,
                        "label": "NDA",
                        "detail": "BJP-led multi-party coalition model.",
                    },
                    {
                        "id": "c4",
                        "year": 2004,
                        "label": "UPA",
                        "detail": "Congress-led coalition with CMP politics.",
                    },
                    {
                        "id": "c5",
                        "year": 2014,
                        "label": "Contemporary",
                        "detail": "Stronger national poles; alliances still matter in states.",
                    },
                ],
            },
            {
                "id": "pd-coal-compare",
                "type": "comparison",
                "title": "Coalition vs single-party majority",
                "columns": [
                    {
                        "id": "coal",
                        "heading": "Coalition government",
                        "points": [
                            "Accommodates diversity",
                            "Strengthens federal bargain",
                            "Checks majoritarian excess",
                            "Risk: instability, policy dilution, large cabinets",
                        ],
                    },
                    {
                        "id": "maj",
                        "heading": "Single-party majority",
                        "points": [
                            "Clear mandate & coherent policy",
                            "Stronger PM/CM leadership",
                            "Faster decisions",
                            "Risk: majoritarian tilt, weaker bargaining for regions",
                        ],
                    },
                ],
            },
            {
                "id": "pd-coal-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Coalition = compromise + CMP + coordination committee. "
                    "Merits: diversity/federalism. Demerits: instability/blackmail/policy dilution. "
                    "Map: NF → UF → NDA → UPA."
                ),
            },
        ],
    },
    {
        "title": "Anti-Defection Law",
        "slug": "pd-anti-defection",
        "sort_order": 8,
        "summary": (
            "Tenth Schedule via 52nd Amendment, grounds and exceptions, Speaker’s role, "
            "91st Amendment changes, Kihoto Hollohan, and reform debates."
        ),
        "body": _std_body(
            {
                "title": "Anti-Defection Law",
                "const": (
                    "- **52nd Amendment (1985)** inserted **Tenth Schedule** + related articles.\n"
                    "- **91st Amendment (2003)** removed split exception; barred defecting "
                    "legislators from ministerial office; capped Council of Ministers size "
                    "(15% of House; smaller assemblies special floor)."
                ),
                "hist": (
                    "- Aaya Ram Gaya Ram culture post-1967 → 52nd Amendment → criticisms → "
                    "91st plugs split loophole & ministry size."
                ),
                "obj": (
                    "- Check opportunistic defections; stabilise governments; give constitutional "
                    "recognition to political parties."
                ),
                "feat": (
                    "- **Disqualification grounds:** voluntarily giving up party membership; "
                    "voting/abstaining contrary to party whip (subject to exceptions).\n"
                    "- **Exceptions:** merger (⅔ of legislative party); Speaker/Chairman resigning "
                    "from party on election as presiding officer (and not rejoining while in office).\n"
                    "- **Deciding authority:** Speaker/Chairman; rule-making power."
                ),
                "inst": (
                    "- Speaker/Chairman as adjudicatory authority; party whips; courts on limited "
                    "judicial review."
                ),
                "laws": (
                    "- Tenth Schedule; Arts related via 52nd/91st (incl. 75/164 size limits; "
                    "disqualification for ministerial berth)."
                ),
                "comm": (
                    "- Goswami; NCRWC — urged stronger anti-defection and criticised Speaker role / "
                    "split logic."
                ),
                "sc": (
                    "- **Kihoto Hollohan (1992):** Tenth Schedule largely valid; Speaker’s order "
                    "subject to judicial review; paragraph making Speaker’s decision final "
                    "struck as unconstitutional to that extent.\n"
                    "- Later cases stress timely decisions / reviewability (exam essentials)."
                ),
                "ca": (
                    "- Mass ‘merger’ politics; demands to transfer adjudication to independent "
                    "tribunal; whip vs legislative freedom debate."
                ),
                "themes": (
                    "- Grounds/exceptions; 91st changes; Speaker vs judiciary; dissent vs defection."
                ),
                "traps": (
                    "- Split exception **removed** by 91st — only merger (⅔) remains.\n"
                    "- Independent who joins a party can attract disqualification; nominated "
                    "member rules differ — don’t conflate.\n"
                    "- Speaker’s decision is **not** immune from judicial review (Kihoto)."
                ),
                "mains": (
                    "- Balance stability vs intra-party democracy; propose independent "
                    "adjudication + narrowed whip scope for conscience votes."
                ),
            }
        ),
        "articles": [
            ("Tenth Schedule", "Anti-defection — grounds, exceptions, deciding authority."),
            ("52nd Amendment", "Inserted Tenth Schedule (1985)."),
            ("91st Amendment", "Merged loophole closed; ministry caps; bar on ministerial office."),
            ("Laxmikanth Ch. 86", "Anti-defection law evaluation and 91st changes."),
        ],
        "visual_blocks": [
            {
                "id": "pd-def-flow",
                "type": "flowchart",
                "title": "Does anti-defection bite?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "What did the member do?",
                        "detail": "Map conduct to Tenth Schedule.",
                        "options": [
                            {"label": "Voluntarily gave up party membership", "next": "dq"},
                            {"label": "Voted/abstained against whip", "next": "whip"},
                            {"label": "Went with a ⅔ merger", "next": "ok"},
                            {"label": "Speaker resigns party on taking chair", "next": "ok"},
                        ],
                    },
                    {
                        "id": "whip",
                        "label": "Check exceptions",
                        "detail": "Prior permission / condonation windows matter.",
                        "options": [
                            {"label": "No valid exception", "next": "dq"},
                            {"label": "Valid exception", "next": "ok"},
                        ],
                    },
                    {
                        "id": "dq",
                        "label": "Disqualification risk",
                        "detail": "Speaker decides; judicial review available (Kihoto).",
                    },
                    {
                        "id": "ok",
                        "label": "Protected / exception",
                        "detail": "Merger (⅔) or Speaker exception — not individual split.",
                    },
                ],
            },
            {
                "id": "pd-def-compare",
                "type": "comparison",
                "title": "Pre-91st vs post-91st anti-defection",
                "columns": [
                    {
                        "id": "pre",
                        "heading": "Before 91st (2003)",
                        "points": [
                            "Split exception existed (group defection path)",
                            "Ministry size less tightly capped by Constitution",
                            "Defectors could still chase office politically",
                        ],
                    },
                    {
                        "id": "post",
                        "heading": "After 91st (2003)",
                        "points": [
                            "Split exception deleted — merger needs ⅔",
                            "Council of Ministers capped (15% rule etc.)",
                            "Disqualified member barred from ministerial berth",
                        ],
                    },
                ],
            },
            {
                "id": "pd-def-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam in 5 Minutes",
                "body": (
                    "52nd → 10th Schedule. Grounds: quit party / defy whip. Exception: ⅔ merger "
                    "(not 1/3 split). Speaker decides but **Kihoto** = judicial review. "
                    "91st = no split + ministry cap + no immediate ministerial reward."
                ),
            },
        ],
    },
    {
        "title": "Pressure Groups",
        "slug": "pd-pressure-groups",
        "sort_order": 9,
        "summary": (
            "Characteristics, Indian typology, methods, and contrast with political parties, "
            "interest groups, NGOs and civil society."
        ),
        "body": _std_body(
            {
                "title": "Pressure Groups",
                "const": (
                    "- Extra-constitutional organised interests influencing policy without "
                    "necessarily seeking formal office."
                ),
                "hist": (
                    "- Trade unions and business chambers from colonial/early Republic era → "
                    "proliferation of identity, professional, and issue groups."
                ),
                "obj": (
                    "- Influence legislation/administration; protect sectional interests; "
                    "articulate demands outside party channels."
                ),
                "feat": (
                    "- Organised; interest-based; may lack electoral ambition; use lobbying, "
                    "propaganda, protest, litigation, strikes, donations, expert advice."
                ),
                "inst": (
                    "- Business (FICCI, ASSOCHAM); unions (INTUC, AITUC, CITU, BMS, HMS); "
                    "agrarian; professional (IMA, BCI); students; religious/caste/tribal/"
                    "linguistic; ideology-based (environment, civil liberties); anomic groups."
                ),
                "laws": (
                    "- Regulated indirectly (labour law, FCRA for NGOs, IPC for unlawful "
                    "methods) — not a single ‘pressure group Act’."
                ),
                "comm": (
                    "- Civil society / NGO debates in governance reports (ARC ethics themes)."
                ),
                "sc": (
                    "- PIL often used by issue groups (environmental/rights) — link to activism."
                ),
                "ca": (
                    "- Professional lobbying norms; FCRA tightening; digital advocacy."
                ),
                "themes": (
                    "- Parties vs pressure groups; types in India; democratic contribution vs "
                    "sectionalism."
                ),
                "traps": (
                    "- Pressure group ≠ political party (even if affiliated).\n"
                    "- Anomic groups (ULFA etc. in book list) are not ‘normal’ democratic lobbies."
                ),
                "mains": (
                    "- Healthy pluralism needs transparent lobbying + strong parties; "
                    "unregulated money influence is the dark side."
                ),
            }
        ),
        "articles": [
            ("Laxmikanth Ch. 87", "Pressure groups — meaning, techniques, Indian types."),
        ],
        "visual_blocks": [
            {
                "id": "pd-pg-compare",
                "type": "comparison",
                "title": "Political parties vs pressure groups",
                "columns": [
                    {
                        "id": "pp",
                        "heading": "Political parties",
                        "points": [
                            "Seek political power / office",
                            "Broad programmes & ideology claims",
                            "Contest elections",
                            "Accountable via votes",
                        ],
                    },
                    {
                        "id": "pg",
                        "heading": "Pressure groups",
                        "points": [
                            "Influence those in power",
                            "Narrow / sectional interests",
                            "Usually do not form government",
                            "Accountable weakly / indirectly",
                        ],
                    },
                ],
            },
            {
                "id": "pd-pg-types",
                "type": "pillars",
                "title": "Indian pressure-group types (scan)",
                "items": [
                    {
                        "id": "biz",
                        "articles": "Business",
                        "label": "Business & unions",
                        "detail": "FICCI/ASSOCHAM; INTUC/AITUC/CITU/BMS/HMS.",
                        "tone": "teal",
                    },
                    {
                        "id": "id",
                        "articles": "Identity",
                        "label": "Identity groups",
                        "detail": "Caste, religious, linguistic, tribal organisations.",
                        "tone": "olive",
                    },
                    {
                        "id": "issue",
                        "articles": "Issue",
                        "label": "Issue / civil society",
                        "detail": "Environment, women’s rights, civil liberties, NGOs.",
                        "tone": "gold",
                    },
                    {
                        "id": "anom",
                        "articles": "Caution",
                        "label": "Anomic / violent",
                        "detail": "Extra-legal outfits — not democratic pressure politics.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pd-pg-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Parties seek power; pressure groups seek influence. Methods: lobby–propaganda–"
                    "protest–litigation. Types: business, labour, agrarian, professional, identity, "
                    "ideology, anomic."
                ),
            },
        ],
    },
    {
        "title": "National Integration",
        "slug": "pd-national-integration",
        "sort_order": 10,
        "summary": (
            "Meaning, constitutional hooks, obstacles (regionalism, communalism, casteism, "
            "linguism), NIC/NFCH, and internal security linkages."
        ),
        "body": _std_body(
            {
                "title": "National Integration",
                "const": (
                    "- Preamble (unity & integrity); secularism; Fundamental Duties "
                    "(promote harmony); single citizenship; emergency/unity provisions as "
                    "extreme backdrop."
                ),
                "hist": (
                    "- Partition trauma → linguistic reorganisation → periodic communal/regional "
                    "crises → institutional responses (NIC, NFCH)."
                ),
                "obj": (
                    "- Emotional + political cohesion of a diverse people into one constitutional "
                    "nation without erasing pluralism."
                ),
                "feat": (
                    "- **Obstacles:** regionalism (secession/statehood/UT upgrades/inter-state "
                    "disputes); communalism; casteism; linguism."
                ),
                "inst": (
                    "- **National Integration Council (NIC)** — review integration issues, advise.\n"
                    "- **National Foundation for Communal Harmony (NFCH)** — victim support, "
                    "harmony programmes, studies, awards."
                ),
                "laws": (
                    "- Constitutional morality + ordinary criminal/public-order law; special "
                    "statutes in extreme cases (not the focus of this chapter)."
                ),
                "comm": (
                    "- NIC as the standing political-consultative forum on integration."
                ),
                "sc": (
                    "- Secularism/basic structure cases sit adjacent (cross-link Salient Features / "
                    "Basic Structure)."
                ),
                "ca": (
                    "- Communal harmony messaging; regional autonomy bargains; internal security "
                    "overlap with extremism/separatism."
                ),
                "themes": (
                    "- Four obstacles; NIC vs NFCH; secularism as integrative principle."
                ),
                "traps": (
                    "- Regionalism is not always anti-national — autonomy demands ≠ secession.\n"
                    "- NIC is not a court; NFCH is not a police agency."
                ),
                "mains": (
                    "- Integration = unity with diversity; tools: constitutional design, "
                    "development balance, secular politics, security with rights."
                ),
            }
        ),
        "articles": [
            ("Laxmikanth Ch. 88", "National integration — obstacles, NIC, NFCH."),
        ],
        "visual_blocks": [
            {
                "id": "pd-ni-pillars",
                "type": "pillars",
                "title": "Four obstacles + institutional response",
                "items": [
                    {
                        "id": "reg",
                        "articles": "Space",
                        "label": "Regionalism",
                        "detail": "Secession, statehood, UT upgrades, border/water disputes.",
                        "tone": "teal",
                    },
                    {
                        "id": "com",
                        "articles": "Faith",
                        "label": "Communalism",
                        "detail": "Religion-based parties/groups, riots, sacred-site disputes.",
                        "tone": "olive",
                    },
                    {
                        "id": "caste",
                        "articles": "Hierarchy",
                        "label": "Casteism",
                        "detail": "Caste parties/groups, ticket calculus, reservation conflicts.",
                        "tone": "gold",
                    },
                    {
                        "id": "lang",
                        "articles": "Tongue",
                        "label": "Linguism",
                        "detail": "Language agitations & identity politics; NIC/NFCH respond.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "pd-ni-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Obstacles: Regionalism · Communalism · Casteism · Linguism. "
                    "NIC = political advisory on integration. NFCH = harmony programmes + "
                    "victim care. Link to secularism + internal security without collapsing them."
                ),
            },
            {
                "id": "pd-ni-note",
                "type": "callout",
                "tone": "note",
                "title": "NIC vs NFCH",
                "body": (
                    "NIC reviews national integration and recommends — political forum. "
                    "NFCH funds/programmes communal harmony and supports child victims of "
                    "societal violence — implementation/outreach body."
                ),
            },
        ],
    },
    {
        "title": "Foreign Policy",
        "slug": "pd-foreign-policy",
        "sort_order": 11,
        "summary": (
            "Art. 51 basis, principles, Panchsheel, NAM, Gujral Doctrine, nuclear doctrine, "
            "Act East / Neighbourhood First, and exam-essential doctrine map."
        ),
        "body": _std_body(
            {
                "title": "Foreign Policy",
                "const": (
                    "- **Article 51 (DPSP):** promote international peace and security; just "
                    "relations; international law/treaty respect; encourage settlement of disputes "
                    "by arbitration."
                ),
                "hist": (
                    "- Nehruvian NAM/Panchsheel → wars & realism adjustments → Gujral Doctrine "
                    "(1996) → Look East → **Act East** → Neighbourhood First / Indo-Pacific "
                    "framing (exam labels)."
                ),
                "obj": (
                    "- Book principles: world peace; anti-colonialism; anti-racialism; "
                    "non-alignment — plus contemporary goals of strategic autonomy, growth, "
                    "and diaspora links."
                ),
                "feat": (
                    "- **Panchsheel:** mutual respect for territorial integrity/sovereignty; "
                    "non-aggression; non-interference; equality & mutual benefit; peaceful "
                    "coexistence.\n"
                    "- **Gujral Doctrine:** non-reciprocal goodwill to smaller neighbours "
                    "(with caveats on hostile pairs).\n"
                    "- **Nuclear doctrine essentials:** credible minimum deterrence; No First "
                    "Use posture (as declared policy).\n"
                    "- **Act East / Connect Central Asia / Neighbourhood First / Indo-Pacific.**"
                ),
                "inst": (
                    "- MEA; PMO; armed forces/diplomacy dual track; multilateral forums "
                    "(UN, NAM, SCO, Quad as partnership format — essentials only)."
                ),
                "laws": (
                    "- Art. 51; treaty practice under Constitution; executive lead in foreign "
                    "affairs."
                ),
                "comm": (
                    "- Policy doctrines are executive/political statements more than committee "
                    "products."
                ),
                "sc": (
                    "- Limited; foreign policy largely executive domain (with treaty/legislative "
                    "edges)."
                ),
                "ca": (
                    "- Neighbourhood First; Act East; Indo-Pacific partnerships; diaspora "
                    "diplomacy; multi-alignment language alongside strategic autonomy."
                ),
                "themes": (
                    "- Art. 51; Panchsheel; NAM; Gujral; nuclear doctrine; Act East."
                ),
                "traps": (
                    "- Art. 51 is **DPSP**, not a justiciable right.\n"
                    "- NAM ≠ isolation; Act East ≠ only ASEAN trade — strategic + connectivity."
                ),
                "mains": (
                    "- Continuity (autonomy, peace) + change (multi-alignment, economics). "
                    "Close with neighbourhood stability as force-multiplier."
                ),
            }
        ),
        "articles": [
            ("Art. 51", "DPSP — international peace and security."),
            ("Laxmikanth Ch. 89", "Foreign policy — principles and doctrines."),
        ],
        "visual_blocks": [
            {
                "id": "pd-fp-doctrines",
                "type": "comparison",
                "title": "Foreign policy doctrines (one-liners)",
                "columns": [
                    {
                        "id": "old",
                        "heading": "Foundational",
                        "points": [
                            "Panchsheel — five coexistence principles",
                            "NAM — strategic autonomy in Cold War",
                            "Art. 51 — constitutional peace orientation",
                        ],
                    },
                    {
                        "id": "mid",
                        "heading": "1990s–2000s",
                        "points": [
                            "Gujral Doctrine — generous neighbourhood",
                            "Nuclear doctrine — credible minimum + NFU",
                            "Look East → deeper Asia engagement",
                        ],
                    },
                    {
                        "id": "now",
                        "heading": "Contemporary labels",
                        "points": [
                            "Act East — strategic + economic East",
                            "Neighbourhood First — priority periphery",
                            "Indo-Pacific — wider maritime theatre",
                        ],
                    },
                ],
            },
            {
                "id": "pd-fp-timeline",
                "type": "timeline",
                "title": "Foreign policy evolution (compressed)",
                "events": [
                    {
                        "id": "f1",
                        "year": 1954,
                        "label": "Panchsheel",
                        "detail": "Five principles enter diplomatic vocabulary.",
                    },
                    {
                        "id": "f2",
                        "year": 1961,
                        "label": "NAM summit era",
                        "detail": "Non-Alignment as identity of foreign policy.",
                    },
                    {
                        "id": "f3",
                        "year": 1996,
                        "label": "Gujral Doctrine",
                        "detail": "Non-reciprocal goodwill to neighbours.",
                    },
                    {
                        "id": "f4",
                        "year": 2014,
                        "label": "Act East / Neighbourhood First",
                        "detail": "Updated regional priorities (exam labels).",
                    },
                ],
            },
            {
                "id": "pd-fp-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes",
                "body": (
                    "Art.51 DPSP. Principles: peace, anti-colonialism, anti-racialism, NAM. "
                    "Doctrines: Panchsheel · Gujral · Nuclear · Act East · Neighbourhood First. "
                    "Continuity = strategic autonomy."
                ),
            },
        ],
    },
    {
        "title": "Master Comparisons",
        "slug": "pd-master-comparisons",
        "sort_order": 12,
        "summary": (
            "Nine high-yield comparison tables for Part X — parties, laws, coalitions, "
            "defection, voting determinants, and foreign-policy doctrines."
        ),
        "body": (
            "## Master Comparisons — how to use\n\n"
            "Scan each visual once before Prelims. For Mains, lift **2–3 contrasts** into "
            "definitions and evaluation paragraphs.\n\n"
            "### Covered contrasts\n\n"
            "1. National vs State parties\n"
            "2. Political parties vs Pressure groups\n"
            "3. Coalition vs Majority government\n"
            "4. RPA 1950 vs 1951\n"
            "5. Election Commission vs Delimitation Commission\n"
            "6. Elections (process) vs Electoral Reforms (agenda)\n"
            "7. Foreign policy doctrines\n"
            "8. Anti-defection provisions (pre/post 91st)\n"
            "9. Voting behaviour determinants summary\n"
        ),
        "articles": [
            ("Laxmikanth Part X", "Cross-cutting comparison sheet for Ch.79–89."),
        ],
        "visual_blocks": [
            {
                "id": "pd-mc-nat-state",
                "type": "comparison",
                "title": "National Parties vs State Parties",
                "columns": [
                    {
                        "id": "n",
                        "heading": "National",
                        "points": [
                            "All-India recognition",
                            "Reserved symbol nationwide",
                            "3 recognition routes",
                            "Also called all-India parties",
                        ],
                    },
                    {
                        "id": "s",
                        "heading": "State",
                        "points": [
                            "State-specific recognition",
                            "Reserved symbol in that state",
                            "5 recognition routes (incl. 8% votes)",
                            "Also called regional parties",
                        ],
                    },
                ],
            },
            {
                "id": "pd-mc-eci-delim",
                "type": "comparison",
                "title": "Election Commission vs Delimitation Commission",
                "columns": [
                    {
                        "id": "eci",
                        "heading": "Election Commission",
                        "points": [
                            "Permanent constitutional body (Art. 324)",
                            "Conducts elections continuously",
                            "Registers/recognises parties; MCC",
                            "Ongoing electoral roll & process role",
                        ],
                    },
                    {
                        "id": "dc",
                        "heading": "Delimitation Commission",
                        "points": [
                            "Statutory, constituted periodically",
                            "Redraws constituencies / seat allocation tasks",
                            "Orders have special finality features",
                            "Not a standing election manager",
                        ],
                    },
                ],
            },
            {
                "id": "pd-mc-elec-reform",
                "type": "comparison",
                "title": "Elections vs Electoral Reforms",
                "columns": [
                    {
                        "id": "el",
                        "heading": "Elections (process)",
                        "points": [
                            "What happens every cycle",
                            "Notify → roll → nominate → poll → count",
                            "EVM–VVPAT, MCC, observers",
                            "Arts 324–329 operational face",
                        ],
                    },
                    {
                        "id": "er",
                        "heading": "Electoral Reforms (agenda)",
                        "points": [
                            "What should improve the system",
                            "Committees + amendments + judgments",
                            "Funding, criminalization, tech, ONOE",
                            "Continuous democracy upgrade project",
                        ],
                    },
                ],
            },
        ],
    },
    {
        "title": "Exam Kit",
        "slug": "pd-exam-kit",
        "sort_order": 13,
        "summary": (
            "Articles cheat sheet, Acts summary, reforms timeline, doctrines, anti-defection "
            "quick reference, PYQ themes, traps, and one-page final revision."
        ),
        "body": (
            "## Constitutional articles cheat sheet\n\n"
            "- **324** ECI · **325** single roll · **326** adult suffrage · **327/328** election "
            "laws · **329** petition path\n"
            "- **Tenth Schedule** anti-defection · **52nd / 91st** Amendments\n"
            "- **Art. 51** foreign policy DPSP · **75/164** ministry size (via 91st)\n\n"
            "## Election laws summary\n\n"
            "- **RPA 1950** — seats, rolls, officers\n"
            "- **RPA 1951** — conduct, parties, petitions, corrupt practices\n"
            "- **Delimitation Act 2002** — constituency redraw framework\n\n"
            "## Political parties (micro)\n\n"
            "- Register ≠ recognise · National 3 routes · State 5 routes (remember **8%**)\n\n"
            "## Electoral reforms timeline\n\n"
            "- Goswami (1990) → 1996 reforms → Gupta funding (1998) → LC/NCRWC/ECI/ARC → "
            "Bonds 2018 → Bonds struck down 2024\n\n"
            "## Foreign policy doctrines\n\n"
            "- Panchsheel · NAM · Gujral · Nuclear · Act East · Neighbourhood First\n\n"
            "## Anti-defection quick reference\n\n"
            "- Grounds: quit party / defy whip\n"
            "- Exception: ⅔ merger (split gone)\n"
            "- Speaker decides; **Kihoto** = judicial review\n"
            "- 91st: no ministerial reward + size caps\n\n"
            "## Frequently confused\n\n"
            "- MCC vs statute · Corrupt practice vs offence · ECI vs Delimitation Commission\n"
            "- Pressure group vs party · Regional party vs state party (ECI)\n"
            "- NAM vs isolation · Art. 51 justiciability\n\n"
            "## PYQ themes\n\n"
            "- National/state recognition criteria\n"
            "- Tenth Schedule / 91st Amendment\n"
            "- RPA 1950 vs 1951\n"
            "- Electoral reforms & funding transparency\n"
            "- Coalition merits/demerits\n"
            "- Panchsheel / Gujral / Art. 51\n"
        ),
        "articles": [
            ("Laxmikanth Part X", "Final revision sheet for Political Dynamics."),
        ],
        "visual_blocks": [
            {
                "id": "pd-exam-pillars",
                "type": "pillars",
                "title": "One-page final revision",
                "items": [
                    {
                        "id": "a",
                        "articles": "Law",
                        "label": "Articles & Acts",
                        "detail": "324–329 · 10th Sch · 52/91 · RPA 50/51 · Art.51",
                        "tone": "teal",
                    },
                    {
                        "id": "b",
                        "articles": "Politics",
                        "label": "Parties & coalitions",
                        "detail": "Recognise routes · regional pivot · NF–NDA–UPA",
                        "tone": "olive",
                    },
                    {
                        "id": "c",
                        "articles": "Process",
                        "label": "Elections & reforms",
                        "detail": "Process chain · committees · Bonds 2024 · ONOE debate",
                        "tone": "gold",
                    },
                    {
                        "id": "d",
                        "articles": "Guardrails",
                        "label": "Defection & integration",
                        "detail": "Whip/merger · Kihoto · RCCL obstacles · NIC/NFCH",
                        "tone": "maroon",
                    },
                    {
                        "id": "e",
                        "articles": "External",
                        "label": "Foreign policy",
                        "detail": "Panchsheel · NAM · Gujral · Act East · Neighbourhood First",
                        "tone": "terracotta",
                    },
                    {
                        "id": "f",
                        "articles": "Behaviour",
                        "label": "Voting behaviour",
                        "detail": "CRRL-PMP-IM multi-causal model",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "pd-exam-60",
                "type": "callout",
                "tone": "tip",
                "title": "Exam in 5 Minutes — whole Part X",
                "body": (
                    "Parties (register→recognise→symbol) → Elections (324–329 + process) → "
                    "Laws (1950 rolls / 1951 fight) → Reforms (committees + Bonds↓) → "
                    "Behaviour (multi-causal) → Coalitions (CMP) → Defection (⅔ merger, Kihoto) → "
                    "Pressure (influence≠office) → Integration (RCCL) → FP (Art.51 + doctrines)."
                ),
            },
            {
                "id": "pd-exam-traps",
                "type": "callout",
                "tone": "trap",
                "title": "Last-minute traps",
                "body": (
                    "8% is state-party route · MCC not an Act · petition to HC · split exception "
                    "dead since 91st · Art.51 is DPSP · Bonds scheme invalidated · "
                    "Delimitation Commission ≠ ECI."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "pd-political-parties"),
    (HUB_SLUG, "parent", "pd-regional-parties"),
    (HUB_SLUG, "parent", "pd-elections"),
    (HUB_SLUG, "parent", "pd-election-laws"),
    (HUB_SLUG, "parent", "pd-electoral-reforms"),
    (HUB_SLUG, "parent", "pd-voting-behaviour"),
    (HUB_SLUG, "parent", "pd-coalition-government"),
    (HUB_SLUG, "parent", "pd-anti-defection"),
    (HUB_SLUG, "parent", "pd-pressure-groups"),
    (HUB_SLUG, "parent", "pd-national-integration"),
    (HUB_SLUG, "parent", "pd-foreign-policy"),
    (HUB_SLUG, "parent", "pd-master-comparisons"),
    (HUB_SLUG, "parent", "pd-exam-kit"),
    ("pd-political-parties", "related", "pd-regional-parties"),
    ("pd-regional-parties", "related", "pd-coalition-government"),
    ("pd-elections", "related", "pd-election-laws"),
    ("pd-election-laws", "related", "pd-electoral-reforms"),
    ("pd-coalition-government", "related", "pd-anti-defection"),
    ("pd-political-parties", "related", "pd-pressure-groups"),
    ("pd-national-integration", "related", "pd-foreign-policy"),
    ("pd-anti-defection", "related", "parliamentary-system"),
    ("pd-regional-parties", "related", "federal-system"),
    ("pd-elections", "related", "sf-adult-franchise"),
    ("pd-exam-kit", "related", "pd-master-comparisons"),
    ("pd-master-comparisons", "related", "pd-political-parties"),
]

SAMPLE_PYQS = [
    (
        2017,
        "How do national parties differ from state parties in terms of Election Commission "
        "recognition criteria?",
        "National: any of (1) 6% votes in ≥4 states + 4 LS seats; (2) 2% LS seats from ≥3 states; "
        "(3) state party in 4 states. State: any of five routes including 6%+seats thresholds, "
        "3% assembly seats/3 seats, 1 LS per 25 seats, or 8% votes in the state.",
        [HUB_SLUG, "pd-political-parties", "pd-master-comparisons"],
    ),
    (
        2019,
        "Discuss the significance of the Tenth Schedule. How did the 91st Amendment alter "
        "the anti-defection framework?",
        "Tenth Schedule (52nd Amendment) disqualifies for voluntarily giving up membership or "
        "defying whip, with merger exception. 91st removed split exception, barred disqualified "
        "members from ministerial office, and capped Council of Ministers size.",
        ["pd-anti-defection", "pd-exam-kit"],
    ),
    (
        2015,
        "Distinguish between the Representation of the People Act, 1950 and 1951.",
        "1950 deals mainly with seat allocation, electoral rolls and related machinery; 1951 "
        "covers conduct of elections, qualifications/disqualifications, party registration, "
        "petitions, corrupt practices and offences.",
        ["pd-election-laws", "pd-master-comparisons"],
    ),
    (
        2018,
        "Coalition governments are both a necessity and a challenge in Indian politics. Comment.",
        "Necessity in hung verdicts and diverse society — accommodates regions and checks "
        "majoritarianism. Challenge — instability, policy dilution, oversized cabinets, and "
        "regional bargaining in national decisions. Management via CMP and coordination bodies.",
        ["pd-coalition-government", HUB_SLUG],
    ),
    (
        2020,
        "What is the constitutional basis of India’s foreign policy orientation towards "
        "international peace?",
        "Article 51 (DPSP) directs the State to promote international peace and security, "
        "maintain just relations, foster respect for international law/treaties, and encourage "
        "arbitration of disputes — the constitutional hook for Panchsheel/NAM tradition.",
        ["pd-foreign-policy", "pd-exam-kit"],
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
            "Landmark on Tenth Schedule — Speaker’s anti-defection decisions are subject to "
            "judicial review."
        ),
        "holding": (
            "Tenth Schedule largely upheld; vesting finality in the Speaker without judicial "
            "review was unconstitutional to that extent; Speaker acts as a tribunal under the "
            "Schedule and orders are reviewable."
        ),
        "concept_slugs": [HUB_SLUG, "pd-anti-defection", "pd-exam-kit"],
    },
    {
        "title": "Union of India v. Association for Democratic Reforms",
        "slug": "adr-disclosure",
        "parties": "Union of India v. Association for Democratic Reforms",
        "year": 2002,
        "court": CaseLaw.Court.SC,
        "summary": "Voters’ right to know candidate background — disclosure push for clean politics.",
        "holding": (
            "Right to information about candidates’ criminal, educational and asset particulars "
            "is part of free speech/informed voting — foundational for electoral reforms."
        ),
        "concept_slugs": [HUB_SLUG, "pd-electoral-reforms", "pd-elections"],
    },
    {
        "title": "Association for Democratic Reforms v. Union of India (Electoral Bonds)",
        "slug": "electoral-bonds-judgment",
        "parties": "Association for Democratic Reforms v. Union of India",
        "year": 2024,
        "court": CaseLaw.Court.SC,
        "summary": "Supreme Court struck down the Electoral Bonds Scheme for opacity in political funding.",
        "holding": (
            "Anonymous electoral bonds violated voters’ right to information and constitutional "
            "requirements of transparency in political funding; scheme held unconstitutional."
        ),
        "concept_slugs": [
            HUB_SLUG,
            "pd-electoral-reforms",
            "pd-exam-kit",
            "pd-political-parties",
        ],
    },
]

AMENDMENTS = [
    {
        "number": 52,
        "year": 1985,
        "title": "Fifty-second Amendment",
        "summary": "Inserted the Tenth Schedule — anti-defection law.",
        "effect": "Constitutionalised party discipline and defection-based disqualification.",
        "concept_slugs": [HUB_SLUG, "pd-anti-defection", "pd-exam-kit"],
    },
    {
        "number": 61,
        "year": 1989,
        "title": "Sixty-first Amendment",
        "summary": "Lowered voting age from 21 to 18 under Article 326.",
        "effect": "Expanded adult franchise; key electoral constitutional reform.",
        "concept_slugs": [HUB_SLUG, "pd-elections", "pd-exam-kit"],
    },
    {
        "number": 91,
        "year": 2003,
        "title": "Ninety-first Amendment",
        "summary": (
            "Strengthened anti-defection (removed split exception), barred defecting legislators "
            "from ministerial office, and capped Council of Ministers size."
        ),
        "effect": "Closed major defection loophole; linked disqualification to office denial.",
        "concept_slugs": [
            HUB_SLUG,
            "pd-anti-defection",
            "pd-coalition-government",
            "pd-exam-kit",
        ],
    },
]


class Command(BaseCommand):
    help = "Seed Political Dynamics chapter (Laxmikanth Part X visual revision)."

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
                "title": "Political Dynamics",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Part X, Ch. 79–89, pp. 804–865",
                "summary": (
                    "Visual revision of Part X — parties, elections, laws, reforms, voting "
                    "behaviour, coalitions, anti-defection, pressure groups, national "
                    "integration, and foreign policy."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="political-dynamics"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Political Dynamics",
                "summary": (
                    "Part X political operating system — parties to foreign policy, "
                    "redesigned for UPSC revision."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **operating system** mental model, then walk the thirteen "
                    "stops. Lock recognition criteria, Arts 324–329, RPA 1950/1951, Tenth "
                    "Schedule/91st, and foreign-policy doctrines. Finish with Master Comparisons "
                    "and Exam Kit. This is a visual revision layer — not a substitute for Laxmikanth."
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
            ref="Laxmikanth Part X",
            excerpt=(
                "Political Dynamics — parties, elections, reforms, coalitions, "
                "anti-defection, pressure groups, integration, foreign policy."
            ),
            sort_order=0,
        )

        pd_slugs = set(by_slug.keys())
        related_outside = {
            "parliamentary-system",
            "federal-system",
            "sf-adult-franchise",
        }
        ConceptEdge.objects.filter(
            Q(source__slug__in=pd_slugs) | Q(target__slug__in=pd_slugs),
            source__subject=subject,
        ).filter(
            Q(source__slug__in=pd_slugs | related_outside)
            | Q(target__slug__in=pd_slugs | related_outside)
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
            if not pyq.answer_key and answer:
                pyq.answer_key = answer
                pyq.save(update_fields=["answer_key"])
            concepts = [by_slug[s] for s in slugs if s in by_slug]
            for s in slugs:
                if s not in by_slug:
                    extra = Concept.objects.filter(subject=subject, slug=s).first()
                    if extra:
                        concepts.append(extra)
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
            payload = {k: v for k, v in amd_data.items() if k != "concept_slugs"}
            amendment, _ = ConstitutionalAmendment.objects.update_or_create(
                academy=academy,
                number=payload["number"],
                defaults=payload,
            )
            concepts = [
                by_slug[s] for s in amd_data["concept_slugs"] if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Political Dynamics chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs."
            )
        )
