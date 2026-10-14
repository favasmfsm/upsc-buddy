"""Seed Laxmikanth Ch.22 Cabinet Committees (visual revision)."""

from django.core.management.base import BaseCommand

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "cabinet-committees"
CHAPTER_SLUG = "cabinet-committees"

ENTRY_PILLARS = [
    {
        "id": "features",
        "articles": "8 features",
        "label": "Features",
        "slug": "cc-features",
        "detail": "Extra-constitutional; PM sets up; decide + Cabinet can review.",
        "tone": "teal",
    },
    {
        "id": "types",
        "articles": "2 types",
        "label": "Standing vs Ad hoc",
        "slug": "cc-standing-vs-adhoc",
        "detail": "Permanent policy organs vs temporary problem-solvers.",
        "tone": "olive",
    },
    {
        "id": "eight",
        "articles": "8 standing",
        "label": "Eight committees",
        "slug": "cc-eight-committees",
        "detail": "PEAP–SAIE map — functions in one line each.",
        "tone": "gold",
    },
    {
        "id": "power",
        "articles": "High-yield 4",
        "label": "Power four",
        "slug": "cc-power-committees",
        "detail": "Political Affairs, ACC, CCS, CCEA — exam favourites.",
        "tone": "orange",
    },
    {
        "id": "chair",
        "articles": "Rules",
        "label": "Composition & chair",
        "slug": "cc-composition-chair",
        "detail": "Membership varies; if PM is a member, PM always chairs.",
        "tone": "terracotta",
    },
    {
        "id": "goms",
        "articles": "GoMs · ARC",
        "label": "GoMs + 2nd ARC",
        "slug": "cc-goms-arc",
        "detail": "Ad hoc coordination; selective, empowered, time-bound use.",
        "tone": "maroon",
    },
    {
        "id": "exam",
        "articles": "Prelims · Mains",
        "label": "Exam revision",
        "slug": "cc-exam-revision",
        "detail": "Prelims facts, PYQ themes, mains value-adds, traps.",
        "tone": "teal",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "cc-load-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Sub-cabinets that share the Cabinet’s load",
        "topic_label": "Cabinet Committees",
        "subject_label": "Rules of Business · Ch. 22",
        "relation_label": "Protects you from",
        "protects_from": [
            "Calling them constitutional bodies",
            "Memorising fixed membership lists",
            "Forgetting Cabinet can review their decisions",
            "Treating GoMs as the same as standing committees",
        ],
        "insight": (
            "Division of labour and delegation — committees decide and coordinate, "
            "but the Cabinet remains supreme and can review."
        ),
    },
    {
        "id": "cc-entry-pillars",
        "type": "pillars",
        "title": "Seven revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "cc-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Scan Features → Standing vs Ad hoc → Eight map → Power four → GoMs. "
            "Anchors: extra-constitutional (Rules of Business); Political Affairs = Super-Cabinet; "
            "ACC = higher appointments; if PM is a member → PM chairs."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Features of Cabinet Committees",
        "slug": "cc-features",
        "sort_order": 1,
        "summary": (
            "Eight compressed features — extra-constitutional origin, PM control, "
            "membership/chair rules, and decide-then-Cabinet-review."
        ),
        "body": (
            "## Eight features (revision spine)\n\n"
            "1. **Extra-constitutional** — not mentioned in the Constitution; "
            "Rules of Business provide for them.\n"
            "2. **Two types** — standing (permanent) and ad hoc (temporary).\n"
            "3. **Set up by the PM** — number, nomenclature, and composition vary with need.\n"
            "4. **Membership** — usually Cabinet Ministers; non-cabinet ministers may be "
            "members or attend as special invitees.\n"
            "5. **Mix of ministers** — portfolio ministers plus other senior ministers.\n"
            "6. **Chair** — mostly PM-headed; other senior Cabinet Ministers may chair; "
            "if the PM is a member, the PM invariably presides.\n"
            "7. **Decide + review** — they formulate proposals and take decisions; "
            "the Cabinet can review those decisions.\n"
            "8. **Workload tool** — reduce Cabinet load; enable in-depth examination and "
            "coordination (division of labour + effective delegation).\n\n"
            "### Memory aid — E-S-P-M-C-D-W\n"
            "**E**xtra-constitutional · **S**tanding/ad hoc · **P**M sets · "
            "**M**embership · **C**hair rule · **D**ecide+review · **W**orkload tool."
        ),
        "articles": [
            (
                "Rules of Business",
                "Extra-constitutional footing — committees are not listed in the Constitution.",
            ),
            (
                "Laxmikanth Ch. 22",
                "Features of Cabinet Committees — origin, types, PM control, decide + Cabinet review.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-features-pillars",
                "type": "pillars",
                "title": "Eight feature chips",
                "items": [
                    {
                        "id": "extra",
                        "articles": "1",
                        "label": "Extra-constitutional",
                        "slug": "cc-features",
                        "detail": "Not in the Constitution; Rules of Business enable them.",
                        "tone": "teal",
                    },
                    {
                        "id": "types",
                        "articles": "2",
                        "label": "Standing + ad hoc",
                        "slug": "cc-standing-vs-adhoc",
                        "detail": "Permanent organs vs temporary problem committees.",
                        "tone": "olive",
                    },
                    {
                        "id": "pm-sets",
                        "articles": "3",
                        "label": "PM sets them up",
                        "slug": "cc-features",
                        "detail": "Number, names, and composition change with exigencies.",
                        "tone": "gold",
                    },
                    {
                        "id": "members",
                        "articles": "4–5",
                        "label": "Membership mix",
                        "slug": "cc-composition-chair",
                        "detail": "Mostly Cabinet Ministers; MoS / invitees possible; seniors included.",
                        "tone": "orange",
                    },
                    {
                        "id": "chair",
                        "articles": "6",
                        "label": "Chair rule",
                        "slug": "cc-composition-chair",
                        "detail": "Usually PM; if PM is a member → PM always chairs.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "decide",
                        "articles": "7",
                        "label": "Decide + review",
                        "slug": "cc-features",
                        "detail": "Committees decide; Cabinet can review their decisions.",
                        "tone": "maroon",
                    },
                    {
                        "id": "workload",
                        "articles": "8",
                        "label": "Workload + depth",
                        "slug": "cc-features",
                        "detail": "Division of labour and delegation for coordination.",
                        "tone": "teal",
                    },
                    {
                        "id": "memory",
                        "articles": "Aid",
                        "label": "E-S-P-M-C-D-W",
                        "slug": "cc-features",
                        "detail": "Memory chain for the eight-feature spine.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "cc-features-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Cabinet Committees are not constitutional bodies. "
                    "Do not treat Art. 77 (conduct of business) as a list of committees — "
                    "Rules of Business are the practical footing."
                ),
            },
        ],
    },
    {
        "title": "Standing vs Ad hoc Committees",
        "slug": "cc-standing-vs-adhoc",
        "sort_order": 2,
        "summary": (
            "Standing = permanent policy domains; ad hoc = temporary special problems, "
            "then disbanded (e.g. 1962 Emergency Committee)."
        ),
        "body": (
            "## Two types\n\n"
            "| | Standing | Ad hoc |\n"
            "|---|---|---|\n"
            "| Nature | Permanent | Temporary |\n"
            "| Purpose | Ongoing policy domains | Special problems |\n"
            "| End | Continue | Disbanded when task done |\n"
            "| Example | Political Affairs, CCS, ACC… | Emergency Committee (1962, Chinese invasion) |\n\n"
            "Both are Cabinet Committees — difference is **duration and purpose**, not legal status."
        ),
        "articles": [
            (
                "Ad hoc example",
                "Emergency Committee set up in 1962 after the Chinese invasion — classic ad hoc case.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-types-compare",
                "type": "comparison",
                "title": "Standing vs Ad hoc",
                "columns": [
                    {
                        "id": "standing",
                        "heading": "Standing",
                        "points": [
                            "Permanent nature",
                            "Ongoing policy domains",
                            "Continue across normal business",
                            "Examples: Political Affairs, CCS, ACC, CCEA…",
                        ],
                    },
                    {
                        "id": "adhoc",
                        "heading": "Ad hoc",
                        "points": [
                            "Temporary nature",
                            "Special / emergent problems",
                            "Disbanded after task completed",
                            "Example: Emergency Committee (1962)",
                        ],
                    },
                ],
            },
            {
                "id": "cc-types-note",
                "type": "callout",
                "tone": "note",
                "title": "Prelims hook",
                "body": (
                    "If a question cites the 1962 Chinese invasion committee — answer **ad hoc**, "
                    "not standing."
                ),
            },
        ],
    },
    {
        "title": "Eight Standing Cabinet Committees",
        "slug": "cc-eight-committees",
        "sort_order": 3,
        "summary": (
            "Laxmikanth’s eight functional standing committees — one-line functions "
            "and PEAP–SAIE mnemonic."
        ),
        "body": (
            "## Eight standing committees (as in Laxmikanth 8th Ed)\n\n"
            "Number and names **vary with the PM** — treat this as the revision map, not a frozen roster.\n\n"
            "| Code | Committee | One-line function |\n"
            "|---|---|---|\n"
            "| CCPA | Political Affairs | Domestic + foreign policy — **Super-Cabinet** |\n"
            "| CCEA | Economic Affairs | Direct and coordinate the economic sphere |\n"
            "| ACC | Appointments | Higher appointments: Central Secretariat, PSUs, banks, FIs |\n"
            "| CCPArl | Parliamentary Affairs | Progress of government business in Parliament |\n"
            "| CCS | Security | Defence, law & order, internal security, atomic energy |\n"
            "| CCAccom | Accommodation | Allotment of government accommodation |\n"
            "| CCIG | Investment & Growth | Capital inflows, exports, import substitution, EoDB |\n"
            "| CCESD | Employment & Skill Dev | Skills, employability, women workforce participation |\n\n"
            "### Mnemonic — PEAP of SAIE\n"
            "**P**olitical · **E**conomic · **A**ppointments · **P**arliamentary / "
            "**S**ecurity · **A**ccommodation · **I**nvestment · **E**mployment."
        ),
        "articles": [
            (
                "Laxmikanth Ch. 22",
                "List and functions of the eight standing Cabinet Committees.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-eight-pillars",
                "type": "pillars",
                "title": "Eight-committee scan",
                "items": [
                    {
                        "id": "ccpa",
                        "articles": "CCPA",
                        "label": "Political Affairs",
                        "slug": "cc-power-committees",
                        "detail": "Domestic + foreign policy — Super-Cabinet.",
                        "tone": "teal",
                    },
                    {
                        "id": "ccea",
                        "articles": "CCEA",
                        "label": "Economic Affairs",
                        "slug": "cc-power-committees",
                        "detail": "Directs and coordinates economic activities.",
                        "tone": "olive",
                    },
                    {
                        "id": "acc",
                        "articles": "ACC",
                        "label": "Appointments",
                        "slug": "cc-power-committees",
                        "detail": "Higher appointments in Secretariat, PSUs, banks, FIs.",
                        "tone": "gold",
                    },
                    {
                        "id": "ccparl",
                        "articles": "CCPArl",
                        "label": "Parliamentary Affairs",
                        "slug": "cc-eight-committees",
                        "detail": "Progress of government business in Parliament.",
                        "tone": "orange",
                    },
                    {
                        "id": "ccs",
                        "articles": "CCS",
                        "label": "Security",
                        "slug": "cc-power-committees",
                        "detail": "Defence, L&O, internal security, atomic energy.",
                        "tone": "terracotta",
                    },
                    {
                        "id": "accom",
                        "articles": "CCAccom",
                        "label": "Accommodation",
                        "slug": "cc-eight-committees",
                        "detail": "Allotment of government accommodation.",
                        "tone": "maroon",
                    },
                    {
                        "id": "ccig",
                        "articles": "CCIG",
                        "label": "Investment & Growth",
                        "slug": "cc-eight-committees",
                        "detail": "Capital inflows, exports, import substitution, EoDB.",
                        "tone": "teal",
                    },
                    {
                        "id": "ccesd",
                        "articles": "CCESD",
                        "label": "Employment & Skill",
                        "slug": "cc-eight-committees",
                        "detail": "Skills, employability, women workforce participation.",
                        "tone": "olive",
                    },
                ],
            },
            {
                "id": "cc-eight-mnemonic",
                "type": "callout",
                "tone": "tip",
                "title": "Memory aid",
                "body": (
                    "PEAP of SAIE — Political, Economic, Appointments, Parliamentary / "
                    "Security, Accommodation, Investment, Employment. "
                    "Names and number can change — PM decides."
                ),
            },
        ],
    },
    {
        "title": "Power Four — High-Yield Committees",
        "slug": "cc-power-committees",
        "sort_order": 4,
        "summary": (
            "Political Affairs (Super-Cabinet), ACC, CCS, and CCEA — "
            "the four most tested standing committees."
        ),
        "body": (
            "## Four committees that carry exam weight\n\n"
            "1. **Political Affairs (CCPA)** — most powerful; often called a **“Super-Cabinet”**; "
            "all policy matters on domestic and foreign affairs.\n"
            "2. **Appointments Committee (ACC)** — higher-level appointments in the Central "
            "Secretariat, Public Enterprises, Banks, and Financial Institutions.\n"
            "3. **Cabinet Committee on Security (CCS)** — defence, law and order, internal "
            "security, and atomic energy.\n"
            "4. **Cabinet Committee on Economic Affairs (CCEA)** — directs and coordinates "
            "governmental activities in the economic sphere.\n\n"
            "### Mains value-add\n"
            "Committees enable specialised deliberation without bloating the full Cabinet. "
            "Risk: a Super-Cabinet / inner-cabinet pattern can sideline the full Cabinet — "
            "efficiency vs collective Cabinet responsibility."
        ),
        "articles": [
            (
                "Super-Cabinet",
                "Political Affairs Committee — most powerful of the Cabinet Committees.",
            ),
            (
                "ACC",
                "Decides higher appointments in Central Secretariat, PSUs, banks, and FIs.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-power-compare",
                "type": "comparison",
                "title": "Role vs UPSC angle",
                "columns": [
                    {
                        "id": "role",
                        "heading": "Core role",
                        "points": [
                            "CCPA — domestic + foreign policy",
                            "ACC — top personnel gatekeeper",
                            "CCS — security & atomic energy nucleus",
                            "CCEA — economic steering",
                        ],
                    },
                    {
                        "id": "upsc",
                        "heading": "Typical UPSC angle",
                        "points": [
                            "CCPA = Super-Cabinet (most powerful)",
                            "ACC = match function to body",
                            "CCS = defence + internal security + AE",
                            "CCEA = economic coordination, not budget law",
                        ],
                    },
                ],
            },
            {
                "id": "cc-power-tip",
                "type": "callout",
                "tone": "tip",
                "title": "Rank hook",
                "body": (
                    "Of all Cabinet Committees, Political Affairs is the most powerful — "
                    "remember the label Super-Cabinet."
                ),
            },
        ],
    },
    {
        "title": "Composition & Chairmanship",
        "slug": "cc-composition-chair",
        "sort_order": 5,
        "summary": (
            "Membership varies; usually Cabinet Ministers; PM almost always chairs "
            "when a member — do not memorise fixed rosters."
        ),
        "body": (
            "## Who sits / who chairs (rules, not names)\n\n"
            "- Membership **size varies** from committee to committee.\n"
            "- Usually **only Cabinet Ministers**; non-cabinet ministers may be appointed "
            "as members or attend as **special invitees**.\n"
            "- Include ministers in charge of covered subjects **plus** other senior ministers.\n"
            "- Mostly headed by the **Prime Minister**; sometimes another senior Cabinet Minister.\n"
            "- **Iron rule:** if the PM is a member of a committee, the PM **invariably** "
            "presides over it.\n\n"
            "Do not memorise chairperson/membership lists — they change with each reconstitution."
        ),
        "articles": [
            (
                "Chair rule",
                "If the Prime Minister is a member of a committee, he/she invariably presides.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-chair-flow",
                "type": "flowchart",
                "title": "Who chairs?",
                "root": "ask",
                "steps": [
                    {
                        "id": "ask",
                        "label": "Is the PM a member of this committee?",
                        "detail": "Chairmanship follows membership, not a fixed schedule.",
                        "options": [
                            {"label": "Yes — PM is a member", "next": "pm"},
                            {"label": "No — PM not a member", "next": "senior"},
                        ],
                    },
                    {
                        "id": "pm",
                        "label": "PM invariably chairs",
                        "detail": "Iron rule — no exception when the PM sits on the committee.",
                    },
                    {
                        "id": "senior",
                        "label": "Senior Cabinet Minister may chair",
                        "detail": "Most committees are still often PM-headed overall; composition varies.",
                    },
                ],
            },
            {
                "id": "cc-chair-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Do not memorise fixed membership lists or assume only Cabinet Ministers "
                    "can ever attend — non-cabinet ministers may be members or special invitees."
                ),
            },
        ],
    },
    {
        "title": "Groups of Ministers & 2nd ARC",
        "slug": "cc-goms-arc",
        "sort_order": 6,
        "summary": (
            "GoMs as ad hoc coordination tools (some empowered); "
            "2nd ARC warned against proliferation without time limits."
        ),
        "body": (
            "## Groups of Ministers (GoMs)\n\n"
            "- Constituted **in addition** to Cabinet Committees to look into issues/subjects.\n"
            "- Some are **empowered** to take decisions on behalf of the Cabinet; "
            "others only make **recommendations**.\n"
            "- Ad hoc bodies — concerned ministers inducted; **disbanded** when advice crystallises.\n"
            "- Viable instrument of **inter-ministry coordination**.\n\n"
            "### 2nd ARC (Veerappa Moily, 2005–2009)\n"
            "1. Too many GoMs → irregular meetings → **delays** on major issues.\n"
            "2. Prefer **selective** use — empowered GoMs with **prescribed time limits**.\n"
            "3. Existing coordination must actually work — clear mandate + deadlines.\n\n"
            "ARC story = organisational effectiveness, not a constitutional amendment theme."
        ),
        "articles": [
            (
                "2nd ARC",
                "Report on Organisational Structure of Government of India (2009) — GoMs observations.",
            ),
            (
                "GoMs",
                "Ad hoc; some decide for Cabinet, others recommend; disbanded when task done.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-goms-compare",
                "type": "comparison",
                "title": "Cabinet Committees vs GoMs",
                "columns": [
                    {
                        "id": "ccs",
                        "heading": "Cabinet Committees",
                        "points": [
                            "Standing + ad hoc types",
                            "Rules of Business footing",
                            "Often ongoing policy domains",
                            "Decide; Cabinet can review",
                        ],
                    },
                    {
                        "id": "goms",
                        "heading": "Groups of Ministers",
                        "points": [
                            "Typically ad hoc coordination",
                            "Issue/subject specific",
                            "Empowered or recommendatory",
                            "Disbanded when advice crystallises",
                        ],
                    },
                ],
            },
            {
                "id": "cc-goms-note",
                "type": "callout",
                "tone": "note",
                "title": "ARC one-liner",
                "body": (
                    "2nd ARC: fewer, selective, empowered, time-bound GoMs — "
                    "proliferation without deadlines causes delay."
                ),
            },
        ],
    },
    {
        "title": "Exam Revision Box",
        "slug": "cc-exam-revision",
        "sort_order": 7,
        "summary": (
            "Prelims facts, PYQ themes, mains value-adds, and a 30-second revision script."
        ),
        "body": (
            "## Prelims facts\n\n"
            "- Extra-constitutional; enabled by **Rules of Business**.\n"
            "- Standing vs ad hoc; **PM** constitutes; names/number vary.\n"
            "- **Political Affairs** = Super-Cabinet (most powerful).\n"
            "- **ACC** = higher appointments (Secretariat, PSUs, banks, FIs).\n"
            "- **CCS** = defence + L&O + internal security + atomic energy.\n"
            "- Committees decide; **Cabinet can review**.\n"
            "- **1962 Emergency Committee** = classic ad hoc example.\n\n"
            "## PYQ themes\n\n"
            "- Constitutional vs extra-constitutional nature.\n"
            "- Who sets up; variability of number and names.\n"
            "- Super-Cabinet identification (Political Affairs).\n"
            "- ACC function match.\n\n"
            "## Mains value-adds\n\n"
            "- Efficiency of specialised committees vs risk to **collective Cabinet responsibility**.\n"
            "- GoMs as coordination tools — ARC warning against proliferation.\n"
            "- Chain: parliamentary executive → Cabinet → committees as working organs.\n\n"
            "### 30-second script\n"
            "Extra-constitutional sub-cabinets set by PM → standing/ad hoc → "
            "PEAP–SAIE map → Super-Cabinet / ACC / CCS → GoMs selective & time-bound."
        ),
        "articles": [
            (
                "Prelims pack",
                "Extra-constitutional; Super-Cabinet; ACC; CCS; Cabinet review; 1962 ad hoc.",
            ),
        ],
        "visual_blocks": [
            {
                "id": "cc-exam-pillars",
                "type": "pillars",
                "title": "Three exam lanes",
                "items": [
                    {
                        "id": "prelims",
                        "articles": "Facts",
                        "label": "Prelims facts",
                        "slug": "cc-exam-revision",
                        "detail": "Nature, Super-Cabinet, ACC, CCS, review, 1962 ad hoc.",
                        "tone": "teal",
                    },
                    {
                        "id": "mains",
                        "articles": "VA",
                        "label": "Mains value-adds",
                        "slug": "cc-exam-revision",
                        "detail": "Efficiency vs collective responsibility; ARC on GoMs.",
                        "tone": "gold",
                    },
                    {
                        "id": "traps",
                        "articles": "Avoid",
                        "label": "Traps",
                        "slug": "cc-exam-revision",
                        "detail": "Not constitutional; don’t freeze membership lists.",
                        "tone": "maroon",
                    },
                ],
            },
            {
                "id": "cc-exam-script",
                "type": "callout",
                "tone": "tip",
                "title": "30-second revision",
                "body": (
                    "Extra-constitutional · PM sets · standing/ad hoc · PEAP–SAIE · "
                    "Political Affairs = Super-Cabinet · ACC = appointments · "
                    "CCS = security · Cabinet can review · GoMs selective & time-bound."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "cc-features"),
    (HUB_SLUG, "parent", "cc-standing-vs-adhoc"),
    (HUB_SLUG, "parent", "cc-eight-committees"),
    (HUB_SLUG, "parent", "cc-power-committees"),
    (HUB_SLUG, "parent", "cc-composition-chair"),
    (HUB_SLUG, "parent", "cc-goms-arc"),
    (HUB_SLUG, "parent", "cc-exam-revision"),
    ("cc-features", "related", "cc-standing-vs-adhoc"),
    ("cc-eight-committees", "related", "cc-power-committees"),
    ("cc-standing-vs-adhoc", "related", "cc-goms-arc"),
    ("cc-composition-chair", "related", "cc-features"),
    ("cc-power-committees", "related", "cc-exam-revision"),
    ("parliamentary-system", "related", HUB_SLUG),
    ("ps-features", "related", HUB_SLUG),
]

SAMPLE_PYQS = [
    (
        2015,
        "Cabinet Committees in India are:",
        "Extra-constitutional bodies provided for under the Rules of Business — not mentioned in the Constitution.",
        ["cc-features", "cc-exam-revision"],
    ),
    (
        2017,
        "Which Cabinet Committee is often described as a ‘Super-Cabinet’?",
        "Cabinet Committee on Political Affairs — the most powerful Cabinet Committee.",
        ["cc-power-committees", "cc-eight-committees"],
    ),
    (
        2019,
        "The Appointments Committee of the Cabinet decides higher-level appointments in:",
        "Central Secretariat, Public Enterprises, Banks, and Financial Institutions.",
        ["cc-power-committees", "cc-eight-committees"],
    ),
    (
        2021,
        "With reference to Groups of Ministers (GoMs), which statement is most accurate?",
        "Ad hoc coordination bodies — some empowered to decide for the Cabinet, others recommend; 2nd ARC urged selective, time-bound use.",
        ["cc-goms-arc", "cc-exam-revision"],
    ),
]


class Command(BaseCommand):
    help = "Seed Cabinet Committees chapter (Laxmikanth Ch.22)."

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
                "title": "Cabinet Committees",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 22",
                "summary": (
                    "Visual revision of Ch.22 — features, standing/ad hoc, eight committees, "
                    "power four, composition rules, GoMs, and 2nd ARC."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Cabinet Committees",
                "summary": (
                    "Sub-cabinets that share the Cabinet’s load — extra-constitutional "
                    "organs under Rules of Business; Cabinet can review their decisions."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **sub-cabinets** mental model, then "
                    "**Features** → **Standing vs Ad hoc** → **Eight committees**. "
                    "Drill **Power four** and **Composition & chair**, finish with "
                    "**GoMs + 2nd ARC** and the **Exam box**. "
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
            ref="Laxmikanth Ch. 22",
            excerpt=(
                "Cabinet Committees — features, standing/ad hoc list, functions, "
                "GoMs, and 2nd ARC observations."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Rules of Business",
            excerpt="Extra-constitutional footing for Cabinet Committees.",
            sort_order=1,
        )

        cc_slugs = set(by_slug.keys())
        # Only clear edges that touch this chapter — do not wipe PS↔PS links.
        from django.db.models import Q

        ConceptEdge.objects.filter(
            Q(source__slug__in=cc_slugs) | Q(target__slug__in=cc_slugs),
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
            if not pyq.answer_key and answer:
                pyq.answer_key = answer
                pyq.save(update_fields=["answer_key"])
            concepts = [by_slug[s] for s in slugs if s in by_slug]
            if concepts:
                pyq.concepts.add(*concepts)

        from subjects.models import Section

        section = Section.objects.filter(
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        self.stdout.write(
            self.style.SUCCESS(
                f"Cabinet Committees chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
