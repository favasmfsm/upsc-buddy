"""Seed Laxmikanth Ch.23 Parliament — Procedure & Budget (visual revision — Part III)."""

from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "parliament-procedure-budget"
CHAPTER_SLUG = "parliament-procedure-budget"

ENTRY_PILLARS = [
    {
        "id": "devices",
        "articles": "Rules",
        "label": "Devices",
        "slug": "ppb-devices",
        "detail": "Question Hour · Zero Hour · motions · PoO · discussions · resolutions.",
        "tone": "teal",
    },
    {
        "id": "leg",
        "articles": "Arts 107–117",
        "label": "Legislative procedure",
        "slug": "ppb-legislative",
        "detail": "Public/private · ordinary · Money Bill · Financial Bills I & II.",
        "tone": "olive",
    },
    {
        "id": "joint",
        "articles": "Art. 108",
        "label": "Joint sitting",
        "slug": "ppb-joint-sitting",
        "detail": "Deadlock resolver — not for Money Bills or Art. 368 bills.",
        "tone": "gold",
    },
    {
        "id": "budget",
        "articles": "Art. 112",
        "label": "Budget",
        "slug": "ppb-budget",
        "detail": "AFS · railway merger · charged expenditure · six stages.",
        "tone": "orange",
    },
    {
        "id": "grants",
        "articles": "Art. 116",
        "label": "Other grants",
        "slug": "ppb-other-grants",
        "detail": "Supplementary · additional · excess · credit · exceptional · token · VoA.",
        "tone": "terracotta",
    },
    {
        "id": "funds",
        "articles": "Arts 266–267",
        "label": "Three funds",
        "slug": "ppb-funds",
        "detail": "Consolidated Fund · Public Account · Contingency Fund.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "ppb-engine-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "The engine room of the Union legislature",
        "topic_label": "Parliament — Procedure & Budget",
        "subject_label": "Arts 107–117 · Ch. 23 (pp. 349–369)",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating Zero Hour as a constitutional device",
            "Allowing joint sitting for Money Bills or CAA bills",
            "Confusing Money Bill with Financial Bill I / II",
            "Thinking charged expenditure is voted like DFGs",
        ],
        "insight": (
            "How the Houses debate, pass bills, break deadlocks, and unlock the purse — "
            "procedure is where Prelims traps cluster."
        ),
    },
    {
        "id": "ppb-entry-pillars",
        "type": "pillars",
        "title": "Six revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "ppb-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "Devices map → Ordinary vs Money vs Financial I/II table → Joint sitting "
            "(3 bills only since 1950) → Budget 6 stages → grants & three funds. "
            "Prior: Structure & Membership. Next: Powers & Privileges."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Devices of Parliamentary Proceedings",
        "slug": "ppb-devices",
        "sort_order": 1,
        "summary": (
            "Question Hour, Zero Hour (Indian innovation), motions catalogue, "
            "Point of Order, discussions, Special Mention, resolutions, Youth Parliament."
        ),
        "body": (
            "## Question Hour\n\n"
            "- First hour of a sitting; starred (oral + supplementaries), unstarred (written), "
            "short-notice questions\n\n"
            "## Zero Hour\n\n"
            "- **Indian innovation** (not in original Rules) — matters of public importance "
            "raised immediately after Question Hour\n"
            "- No formal mention in Rules of Procedure originally; evolved by practice\n\n"
            "## Motions (high-yield set)\n\n"
            "| Motion | Idea |\n"
            "|--------|------|\n"
            "| Closure | End debate now |\n"
            "| Privilege | Breach of privilege |\n"
            "| Calling Attention | Urgent public matter → minister statement |\n"
            "| Adjournment | Adjourn to discuss definite urgent matter |\n"
            "| No-Confidence | Only in **LS**; simple majority |\n"
            "| Confidence | Government seeks trust |\n"
            "| Censure | Condemns specific policy/minister |\n"
            "| Motion of Thanks | On President’s address |\n"
            "| No-Day-Yet-Named | Admitted but date not fixed |\n"
            "| Dilatory | Delay (adjourn consideration / circulate) |\n\n"
            "## Other devices\n\n"
            "- **Point of Order** — procedure/Rules breach; chair decides\n"
            "- **Half-an-Hour Discussion** — answer needing clarification\n"
            "- **Short Duration Discussion** — ~2 hours on matter of urgent public importance\n"
            "- **Special Mention** (RS) / similar LS practice\n"
            "- **Resolutions** — private member / government / statutory\n"
            "- **Youth Parliament** — awareness programme, not a House device\n"
        ),
        "articles": [
            ("Rules of Houses", "Question Hour, motions, and devices of proceedings."),
            ("Laxmikanth Ch. 23", "Devices — Zero Hour as Indian innovation; motion types."),
        ],
        "visual_blocks": [
            {
                "id": "ppb-devices-pillars",
                "type": "pillars",
                "title": "Device chips",
                "items": [
                    {
                        "id": "qh",
                        "articles": "1st hour",
                        "label": "Question Hour",
                        "slug": "ppb-devices",
                        "detail": "Starred · unstarred · short notice.",
                        "tone": "teal",
                    },
                    {
                        "id": "zh",
                        "articles": "Indian",
                        "label": "Zero Hour",
                        "slug": "ppb-devices",
                        "detail": "After QH — practice, not original Rules text.",
                        "tone": "olive",
                    },
                    {
                        "id": "ncm",
                        "articles": "LS only",
                        "label": "No-Confidence",
                        "slug": "ppb-devices",
                        "detail": "Only Lok Sabha — collective responsibility.",
                        "tone": "gold",
                    },
                    {
                        "id": "adj",
                        "articles": "Urgent",
                        "label": "Adjournment motion",
                        "slug": "ppb-devices",
                        "detail": "Definite matter of urgent public importance.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "ppb-zero-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Zero Hour trap",
                "body": (
                    "Zero Hour is an **Indian parliamentary innovation** — do not call it a "
                    "constitutional provision or an original Rules device."
                ),
            },
        ],
    },
    {
        "title": "Legislative Procedure in Parliament",
        "slug": "ppb-legislative",
        "sort_order": 2,
        "summary": (
            "Public vs private bills; ordinary bill stages; Money Bill (Art. 110) vs "
            "Financial Bills I & II (Art. 117); Speaker’s certificate."
        ),
        "body": (
            "## Public Bill vs Private Bill\n\n"
            "| | Public (Government) | Private Member |\n"
            "|---|---------------------|----------------|\n"
            "| Introduced by | Minister | Private member |\n"
            "| Chance of passage | High | Low |\n"
            "| Drafting | Official | Member |\n"
            "| Rejection | May → govt crisis (if major) | No |\n\n"
            "## Ordinary bills — path\n\n"
            "1. First reading (introduction) → 2. Second reading (principles → committee → clause) → "
            "3. Third reading (pass/reject as whole) → other House → President’s assent "
            "(assent / withhold / return once — suspensive veto).\n\n"
            "Deadlock with other House (reject / disagree amendments / 6 months inaction) → "
            "**joint sitting** possible.\n\n"
            "## Money Bills (Art. 110)\n\n"
            "Contains **only** Art. 110 matters (tax, borrowing, CFI/Contingency custody, "
            "appropriation, charged expenditure, receipts/audit, incidental).\n\n"
            "**Not** Money Bill merely for fines, licence fees, or local-body taxes.\n\n"
            "- Only in **LS**, only by **minister**, only on **President’s recommendation**\n"
            "- Speaker’s certificate **final**\n"
            "- RS: recommend only; return in **14 days**; LS may ignore\n"
            "- President: assent or withhold — **cannot return** for reconsideration\n"
            "- Defeat in LS → government resignation\n\n"
            "## Financial Bills\n\n"
            "| Kind | Article | Intro | RS power | Joint sitting |\n"
            "|------|---------|-------|----------|---------------|\n"
            "| Money Bill | 110 | LS + Pres. rec. | Recommend / 14 days | No |\n"
            "| Financial Bill I | 117(1) | LS + Pres. rec. | Amend/reject | Yes |\n"
            "| Financial Bill II | 117(3) | Either House | Like ordinary | Yes |\n\n"
            "- **All Money Bills are Financial Bills; not all Financial Bills are Money Bills**\n"
            "- FB-I: Art. 110 matters **plus** general legislation\n"
            "- FB-II: expenditure from CFI **without** Art. 110 matters; Pres. recommendation "
            "at **consideration**, not introduction\n"
        ),
        "articles": [
            ("Art. 107", "Provisions as to introduction and passing of bills."),
            ("Art. 109", "Special procedure in respect of Money Bills."),
            ("Art. 110", "Definition of Money Bills."),
            ("Art. 111", "Assent to Bills."),
            ("Art. 117", "Special provisions as to financial Bills."),
        ],
        "visual_blocks": [
            {
                "id": "ppb-money-compare",
                "type": "compare",
                "title": "Ordinary Bill vs Money Bill",
                "left": {
                    "title": "Ordinary Bill",
                    "items": [
                        "Either House",
                        "Minister or private member",
                        "RS can amend/reject (6 months)",
                        "Joint sitting possible",
                        "President may return",
                    ],
                },
                "right": {
                    "title": "Money Bill",
                    "items": [
                        "Only Lok Sabha",
                        "Only minister + Pres. rec.",
                        "RS recommends (14 days)",
                        "No joint sitting",
                        "President cannot return",
                    ],
                },
            },
            {
                "id": "ppb-fb-callout",
                "type": "callout",
                "tone": "tip",
                "title": "Financial Bill ladder",
                "body": (
                    "Money ⊂ Financial. FB-I ≈ Money on introduction rules but like ordinary "
                    "thereafter (joint sitting yes). FB-II ≈ ordinary except Pres. rec. at consideration."
                ),
            },
        ],
    },
    {
        "title": "Joint Sitting of Two Houses",
        "slug": "ppb-joint-sitting",
        "sort_order": 3,
        "summary": (
            "Art. 108 deadlock machinery for ordinary/financial bills — not Money Bills or "
            "constitutional amendments. Speaker chairs; used thrice since 1950."
        ),
        "body": (
            "## When deadlock arises\n\n"
            "After one House passes a bill and transmits it, deadlock if the other House:\n"
            "1. **Rejects** the bill, or\n"
            "2. Finally **disagrees** on amendments, or\n"
            "3. Takes **no action for 6 months** (exclude prorogation / adjournment >4 consecutive days)\n\n"
            "President may summon a joint sitting to deliberate and vote.\n\n"
            "## Scope\n\n"
            "- Applies to **ordinary** and **financial** bills\n"
            "- **Not** Money Bills (LS overrides) or **Art. 368** amendment bills (each House separately)\n"
            "- If bill already **lapsed** on LS dissolution → no joint sitting\n"
            "- If President has **notified** intention to summon, dissolution of LS does **not** stop the sitting\n\n"
            "## Procedure\n\n"
            "- Presides: **Speaker** → Dy Speaker → Dy Chairman RS (Chairman RS does **not** preside)\n"
            "- Quorum: **1/10** of total membership of both Houses\n"
            "- Rules of **Lok Sabha** apply\n"
            "- Pass by majority of members of both Houses present and voting\n"
            "- New amendments only if they caused disagreement or became necessary due to delay\n\n"
            "## Invoked thrice\n\n"
            "1. Dowry Prohibition Bill, 1960\n"
            "2. Banking Service Commission (Repeal) Bill, 1977\n"
            "3. Prevention of Terrorism Bill, 2002\n"
        ),
        "articles": [
            ("Art. 108", "Joint sitting of both Houses in certain cases."),
            ("Laxmikanth Ch. 23", "Three joint sittings since 1950."),
        ],
        "visual_blocks": [
            {
                "id": "ppb-joint-flow",
                "type": "flowchart",
                "title": "Can there be a joint sitting?",
                "root": "bill",
                "steps": [
                    {
                        "id": "bill",
                        "label": "What kind of bill?",
                        "options": [
                            {"label": "Money Bill / CAA bill", "next": "no"},
                            {"label": "Ordinary / Financial", "next": "dead"},
                        ],
                    },
                    {
                        "id": "dead",
                        "label": "Deadlock? (reject / disagree / 6 months)",
                        "options": [
                            {"label": "Yes + President summons", "next": "yes"},
                            {"label": "Bill already lapsed on dissolution", "next": "no"},
                        ],
                    },
                    {
                        "id": "yes",
                        "label": "Joint sitting",
                        "detail": "Speaker chairs · LS rules · simple majority of both Houses P&V",
                    },
                    {
                        "id": "no",
                        "label": "No joint sitting",
                        "detail": "Money → LS override; CAA → each House separately",
                    },
                ],
            },
        ],
    },
    {
        "title": "Budget in Parliament",
        "slug": "ppb-budget",
        "sort_order": 4,
        "summary": (
            "Annual Financial Statement (Art. 112); railway budget merged 2017; "
            "charged vs voted expenditure; six stages of enactment."
        ),
        "body": (
            "## What is the budget?\n\n"
            "- Constitution: **Annual Financial Statement** (Art. 112) — word “budget” not used\n"
            "- Estimated receipts & expenditure for the financial year (1 Apr–31 Mar)\n"
            "- Also: ways & means, previous year actuals, economic/financial policy\n\n"
            "## Railway Budget merger (2017)\n\n"
            "- Separate Railway Budget since **1924** (Acworth Committee 1921)\n"
            "- Merged into General Budget in **2017** → single **Union Budget**\n\n"
            "## Constitutional anchors\n\n"
            "- Laid by President before both Houses (112)\n"
            "- No DFG except on President’s recommendation (113)\n"
            "- No withdrawal from CFI except by appropriation law (114)\n"
            "- Tax Money/Finance bills: LS only + Pres. rec. (109, 117)\n"
            "- No tax except by law (265); Parliament may reduce/abolish but not increase tax\n"
            "- RS **cannot vote** DFGs; returns Money/Finance bill in 14 days\n"
            "- Charged expenditure: discussable, **not votable**\n"
            "- LS may approve/refuse/reduce DFG — **cannot increase**\n"
            "- Vote on Account allowed (116)\n\n"
            "## Charged expenditure (examples)\n\n"
            "President’s emoluments · salaries of RS Chairman/Dy Chairman & LS Speaker/Dy Speaker · "
            "SC judges’ salaries · CAG · FC Chairman/members · debt charges · certain pensions · "
            "arbitral awards · sums for Court decrees · any other declared by Parliament\n\n"
            "## Six stages of enactment\n\n"
            "1. **Presentation** of budget\n"
            "2. **General discussion**\n"
            "3. **Scrutiny by departmental committees** (DRSCs)\n"
            "4. **Voting on demands for grants** (+ cut motions)\n"
            "5. **Appropriation Bill**\n"
            "6. **Finance Bill**\n\n"
            "Cut motions: policy cut / economy cut / token cut — express disapproval within DFG voting."
        ),
        "articles": [
            ("Art. 112", "Annual financial statement."),
            ("Art. 113", "Procedure in Parliament with respect to estimates."),
            ("Art. 114", "Appropriation Bills."),
            ("Art. 265", "Taxes not to be imposed save by authority of law."),
        ],
        "visual_blocks": [
            {
                "id": "ppb-budget-stages",
                "type": "flowchart",
                "title": "Six stages",
                "root": "s1",
                "steps": [
                    {
                        "id": "s1",
                        "label": "1. Presentation",
                        "options": [{"label": "Next", "next": "s2"}],
                    },
                    {
                        "id": "s2",
                        "label": "2. General discussion",
                        "options": [{"label": "Next", "next": "s3"}],
                    },
                    {
                        "id": "s3",
                        "label": "3. DRSC scrutiny",
                        "options": [{"label": "Next", "next": "s4"}],
                    },
                    {
                        "id": "s4",
                        "label": "4. Vote DFGs (+ cut motions)",
                        "detail": "LS only — RS does not vote grants",
                        "options": [{"label": "Next", "next": "s5"}],
                    },
                    {
                        "id": "s5",
                        "label": "5. Appropriation Bill",
                        "options": [{"label": "Next", "next": "s6"}],
                    },
                    {
                        "id": "s6",
                        "label": "6. Finance Bill",
                        "detail": "Taxation proposals become law",
                    },
                ],
            },
            {
                "id": "ppb-charged-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Charged ≠ voted",
                "body": (
                    "Charged expenditure can be **discussed** but is **not submitted to the vote** "
                    "of Parliament (Art. 113)."
                ),
            },
        ],
    },
    {
        "title": "Other Grants",
        "slug": "ppb-other-grants",
        "sort_order": 5,
        "summary": (
            "Supplementary, additional, excess, vote of credit, exceptional grant, "
            "token grant, and Vote on Account — when each is used."
        ),
        "body": (
            "## Catalogue\n\n"
            "| Grant | When |\n"
            "|-------|------|\n"
            "| **Supplementary** | Amount authorised for a service is insufficient in the year |\n"
            "| **Additional** | Need for additional expenditure on a new service not contemplated in budget |\n"
            "| **Excess** | Money spent on a service beyond the amount granted for the year |\n"
            "| **Vote of Credit** | Sudden large demand / indefinite demand (blank cheque style) |\n"
            "| **Exceptional Grant** | Special purpose forming no part of ordinary expenditure service |\n"
            "| **Token Grant** | ₹1 demand to spend from existing savings by reappropriation |\n"
            "| **Vote on Account** | Advance grant for part of the year pending full DFG + Appropriation |\n\n"
            "Vote on Account is routine before elections / interim periods when full budget process "
            "cannot complete in time."
        ),
        "articles": [
            ("Art. 115", "Supplementary, additional or excess grants."),
            ("Art. 116", "Votes on account, votes of credit and exceptional grants."),
        ],
        "visual_blocks": [
            {
                "id": "ppb-grants-pillars",
                "type": "pillars",
                "title": "Grant chips",
                "items": [
                    {
                        "id": "sup",
                        "articles": "115",
                        "label": "Supplementary",
                        "slug": "ppb-other-grants",
                        "detail": "Authorised amount insufficient.",
                        "tone": "teal",
                    },
                    {
                        "id": "add",
                        "articles": "115",
                        "label": "Additional",
                        "slug": "ppb-other-grants",
                        "detail": "New service not in the budget.",
                        "tone": "olive",
                    },
                    {
                        "id": "exc",
                        "articles": "115",
                        "label": "Excess",
                        "slug": "ppb-other-grants",
                        "detail": "Spent beyond the grant — post-facto.",
                        "tone": "gold",
                    },
                    {
                        "id": "voa",
                        "articles": "116",
                        "label": "Vote on Account",
                        "slug": "ppb-other-grants",
                        "detail": "Advance for part of the year.",
                        "tone": "orange",
                    },
                ],
            },
        ],
    },
    {
        "title": "Funds of India",
        "slug": "ppb-funds",
        "sort_order": 6,
        "summary": (
            "Consolidated Fund of India, Public Account of India, and Contingency Fund of India — "
            "custody, appropriation, and when Parliament must authorise."
        ),
        "body": (
            "## Three funds\n\n"
            "### 1. Consolidated Fund of India (Art. 266)\n"
            "- All revenues, loans raised, loan repayments received by Government of India\n"
            "- **No money out** except under appropriation by law\n\n"
            "### 2. Public Account of India (Art. 266)\n"
            "- Provident funds, small savings, other deposits where government is banker\n"
            "- Disbursements **not** subject to parliamentary appropriation vote in the same way as CFI\n\n"
            "### 3. Contingency Fund of India (Art. 267)\n"
            "- Held by President; advances for unforeseen expenditure\n"
            "- Later authorised by Parliament; amount fixed by law\n\n"
            "### Memory\n"
            "**C-P-C** — Consolidated (appropriation) · Public (deposits) · Contingency (unforeseen advances)."
        ),
        "articles": [
            ("Art. 266", "Consolidated Funds and public accounts of India and of the States."),
            ("Art. 267", "Contingency Fund."),
        ],
        "visual_blocks": [
            {
                "id": "ppb-funds-tree",
                "type": "tree",
                "title": "Three funds",
                "root": {
                    "id": "funds",
                    "label": "Union funds",
                    "children": [
                        {
                            "id": "cfi",
                            "label": "Consolidated Fund",
                            "detail": "Appropriation Act required to withdraw",
                        },
                        {
                            "id": "pa",
                            "label": "Public Account",
                            "detail": "Government as banker — deposits",
                        },
                        {
                            "id": "cf",
                            "label": "Contingency Fund",
                            "detail": "President’s advances → later Parliament OK",
                        },
                    ],
                },
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "ppb-devices"),
    (HUB_SLUG, "parent", "ppb-legislative"),
    (HUB_SLUG, "parent", "ppb-joint-sitting"),
    (HUB_SLUG, "parent", "ppb-budget"),
    (HUB_SLUG, "parent", "ppb-other-grants"),
    (HUB_SLUG, "parent", "ppb-funds"),
    ("ppb-devices", "related", "ppb-legislative"),
    ("ppb-legislative", "related", "ppb-joint-sitting"),
    ("ppb-legislative", "related", "ppb-budget"),
    ("ppb-budget", "related", "ppb-other-grants"),
    ("ppb-budget", "related", "ppb-funds"),
    ("ppb-joint-sitting", "related", "psm-presiding-officers"),
    ("parliament-structure-membership", "related", HUB_SLUG),
    (HUB_SLUG, "related", "parliament-powers-privileges"),
    ("parliamentary-committees", "related", "ppb-budget"),
]

SAMPLE_PYQS = [
    (
        2014,
        "Zero Hour in Parliament refers to:",
        "An Indian innovation — matters of public importance raised immediately after Question Hour.",
        ["ppb-devices", HUB_SLUG],
    ),
    (
        2016,
        "Which of the following is not a Money Bill matter under Article 110?",
        "Imposition of fines / licence fees / local-body taxes alone does not make a bill a Money Bill.",
        ["ppb-legislative", HUB_SLUG],
    ),
    (
        2018,
        "Joint sitting of Parliament cannot be resorted to for:",
        "Money Bills and Constitution Amendment Bills — only ordinary/financial bills.",
        ["ppb-joint-sitting", "ppb-legislative"],
    ),
    (
        2020,
        "Expenditure charged on the Consolidated Fund of India is:",
        "Discussable but not votable by Parliament (Art. 113).",
        ["ppb-budget", "ppb-funds"],
    ),
    (
        2022,
        "A Vote on Account is meant to:",
        "Authorise advance expenditure for a part of the financial year pending full DFGs and Appropriation Act.",
        ["ppb-other-grants", "ppb-budget"],
    ),
]


class Command(BaseCommand):
    help = (
        "Seed Parliament: Procedure & Budget "
        "(Laxmikanth Ch.23 pp. 349–369) under Part III Central Government."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--academy",
            default="fortuneias",
            help="Academy slug to seed into (default: fortuneias).",
        )

    def handle(self, *args, **options):
        from academies.seed_utils import get_academy_or_fail
        from subjects.models import Section

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
                "title": "Parliament: Procedure & Budget",
                "sort_order": 7,
                "book_ref": "Laxmikanth 8th Ed, Ch. 23 (pp. 349–369) — Procedure & Budget",
                "summary": (
                    "Visual revision of Ch.23 part 2 — devices, legislative procedure, "
                    "joint sitting, budget stages, other grants, and three funds."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="central-government"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Parliament: Procedure & Budget",
                "summary": (
                    "Engine room of the Union legislature — devices, bills, deadlocks, "
                    "and the annual financial statement."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **engine room** mental model, then "
                    "**Devices** → **Legislative procedure** → **Joint sitting** → "
                    "**Budget** → **Other grants** → **Funds**. "
                    "Prior: Structure & Membership. Next: Powers & Privileges. "
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
            ref="Laxmikanth Ch. 23 (pp. 349–369)",
            excerpt=(
                "Parliament — devices, legislative procedure, joint sitting, "
                "budget, grants, and funds."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Arts 107–117, 266–267",
            excerpt="Legislative and financial procedure for the Union Parliament.",
            sort_order=1,
        )

        ppb_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            Q(source__slug__in=ppb_slugs) | Q(target__slug__in=ppb_slugs),
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
                existing = list(pyq.concepts.all())
                pyq.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Parliament Procedure & Budget seeded ({academy.slug}): "
                f"{chapter.title} with {len(CLUSTERS) + 1} concepts, "
                f"{created_edges} new edges, {len(SAMPLE_PYQS)} PYQs linked."
            )
        )
