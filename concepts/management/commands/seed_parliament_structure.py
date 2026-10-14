"""Seed Laxmikanth Ch.23 Parliament — Structure & Membership (visual revision — Part III)."""

from django.core.management.base import BaseCommand
from django.db.models import Q

from concepts.models import Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "parliament-structure-membership"
CHAPTER_SLUG = "parliament-structure-membership"

ENTRY_PILLARS = [
    {
        "id": "org",
        "articles": "Art. 79",
        "label": "Organisation",
        "slug": "psm-organisation",
        "detail": "President + Rajya Sabha + Lok Sabha — British, not American pattern.",
        "tone": "teal",
    },
    {
        "id": "comp",
        "articles": "Arts 80–81",
        "label": "Composition",
        "slug": "psm-composition",
        "detail": "RS max 250 (12 nominated); LS max 550; Anglo-Indian ended 104th CAA.",
        "tone": "olive",
    },
    {
        "id": "elect",
        "articles": "Arts 81–82",
        "label": "LS elections",
        "slug": "psm-elections",
        "detail": "FPTP · delimitation freeze · SC/ST reservation till 2030.",
        "tone": "gold",
    },
    {
        "id": "duration",
        "articles": "Art. 83",
        "label": "Duration",
        "slug": "psm-duration",
        "detail": "RS continuing chamber (⅓ every 2 yrs); LS 5 years + emergency extension.",
        "tone": "orange",
    },
    {
        "id": "member",
        "articles": "Arts 84, 101–104",
        "label": "Membership",
        "slug": "psm-membership",
        "detail": "Qualifications, disqualifications, Tenth Schedule, vacating seats, oath.",
        "tone": "terracotta",
    },
    {
        "id": "officers",
        "articles": "Arts 89–98",
        "label": "Presiding officers",
        "slug": "psm-presiding-officers",
        "detail": "Speaker · Deputy · Pro Tem · RS Chairman (VP) · panels · secretariat.",
        "tone": "maroon",
    },
    {
        "id": "leaders",
        "articles": "Rules · 1977 Act",
        "label": "Leaders",
        "slug": "psm-leaders",
        "detail": "Leader of House · LoP (statutory) · Whips.",
        "tone": "teal",
    },
    {
        "id": "sessions",
        "articles": "Arts 85–88",
        "label": "Sessions",
        "slug": "psm-sessions",
        "detail": "Summon · adjourn · prorogue · dissolve · quorum · voting · lame-duck.",
        "tone": "olive",
    },
    {
        "id": "majority",
        "articles": "Art. 100+",
        "label": "Types of majority",
        "slug": "psm-majority",
        "detail": "Simple · Effective · Absolute · Special — match matter to majority.",
        "tone": "gold",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "psm-frame-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "The frame of the Union legislature",
        "topic_label": "Parliament — Structure & Membership",
        "subject_label": "Arts 79–122 · Ch. 23 (pp. 326–348)",
        "relation_label": "Protects you from",
        "protects_from": [
            "Treating the President as outside Parliament",
            "Confusing RS PR/STV with LS first-past-the-post",
            "Mixing simple vs effective majority for Speaker removal",
            "Assuming Anglo-Indian LS nomination still exists",
        ],
        "insight": (
            "Who sits, who chairs, how long they sit, and how the House is summoned — "
            "master the frame before procedure and powers."
        ),
    },
    {
        "id": "psm-entry-pillars",
        "type": "pillars",
        "title": "Nine revision stops",
        "items": ENTRY_PILLARS,
    },
    {
        "id": "psm-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision anchor",
        "body": (
            "President-in-Parliament → RS/LS numbers → FPTP vs PR → duration → "
            "qual/disqual/defection → Speaker special powers → sessions table → majority map. "
            "Next chapters: Procedure & Budget → Powers & Privileges."
        ),
    },
]

CLUSTERS = [
    {
        "title": "Organisation of Parliament",
        "slug": "psm-organisation",
        "sort_order": 1,
        "summary": (
            "Parliament = President + Council of States + House of the People. "
            "British Crown-in-Parliament pattern, not the US Congress model."
        ),
        "body": (
            "## Three parts (Art. 79)\n\n"
            "1. **President** — not a member of either House, yet an **integral** part of Parliament\n"
            "2. **Rajya Sabha** (Council of States) — Upper House / House of Elders\n"
            "3. **Lok Sabha** (House of the People) — Lower House / Popular House\n\n"
            "Hindi names adopted in **1954**.\n\n"
            "## Why President is part of Parliament\n\n"
            "- Bill needs **assent** to become law\n"
            "- Summons, prorogues, dissolves LS, addresses Houses, issues ordinances in recess\n\n"
            "## Comparative trap\n\n"
            "| Pattern | Legislature |\n"
            "|---------|-------------|\n"
            "| **India / UK** | Head of State **inside** Parliament |\n"
            "| **USA** | President **outside** Congress (Senate + House) |\n\n"
            "Parliamentary form → interdependence of legislature and executive → "
            "**President-in-Parliament** like **Crown-in-Parliament**."
        ),
        "articles": [
            ("Art. 79", "Constitution of Parliament — President, Council of States, House of the People."),
            ("Laxmikanth Ch. 23", "Organisation — British pattern vs American Congress."),
        ],
        "visual_blocks": [
            {
                "id": "psm-org-tree",
                "type": "tree",
                "title": "Parliament = three parts",
                "root": {
                    "id": "parl",
                    "label": "Parliament of India",
                    "children": [
                        {
                            "id": "pres",
                            "label": "President",
                            "detail": "Assent · summon · prorogue · dissolve LS",
                        },
                        {
                            "id": "rs",
                            "label": "Rajya Sabha",
                            "detail": "States & UTs + 12 nominated",
                            "slug": "psm-composition",
                        },
                        {
                            "id": "ls",
                            "label": "Lok Sabha",
                            "detail": "People · direct election",
                            "slug": "psm-composition",
                        },
                    ],
                },
            },
            {
                "id": "psm-org-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Exam trap",
                "body": (
                    "Privileges do **not** extend to the President even though he/she is part of Parliament. "
                    "See Powers & Privileges chapter."
                ),
            },
        ],
    },
    {
        "title": "Composition of the Two Houses",
        "slug": "psm-composition",
        "sort_order": 2,
        "summary": (
            "RS max 250 (238 elected + 12 nominated); LS max 550 (530 states + 20 UTs). "
            "Present strength ~245 RS / 543 LS. Anglo-Indian LS nomination ended by 104th CAA."
        ),
        "body": (
            "## Rajya Sabha\n\n"
            "| Slot | Cap |\n"
            "|------|-----|\n"
            "| States + UTs (indirect) | **238** |\n"
            "| Nominated by President | **12** |\n"
            "| **Maximum** | **250** |\n"
            "| **Present** | **245** (225 states + 8 UTs + 12 nominated) |\n\n"
            "- **States:** elected by elected MLAs — **PR by STV**; seats by population (4th Schedule)\n"
            "- **UTs:** electoral college; only **Delhi, Puducherry, J&K** have RS seats among UTs\n"
            "- **Nominated:** art, literature, science, social service — US Senate has **no** nominated members\n"
            "- Contrast USA: equal Senate seats per state; India: population-based RS seats\n\n"
            "## Lok Sabha\n\n"
            "| Slot | Cap |\n"
            "|------|-----|\n"
            "| States | **530** |\n"
            "| UTs | **20** |\n"
            "| **Maximum** | **550** |\n"
            "| **Present** | **543** (524 states + 19 UTs) |\n\n"
            "- Direct election; universal adult franchise; voting age **18** (61st CAA, 1988)\n"
            "- UT manner prescribed by Parliament (UT Direct Election Act, 1965)\n"
            "- **Anglo-Indian nomination** (2 seats) **discontinued** by **104th CAA, 2019** "
            "(ceased 25 Jan 2020); last extension was 95th CAA to 2020\n"
        ),
        "articles": [
            ("Art. 80", "Composition of the Council of States."),
            ("Art. 81", "Composition of the House of the People."),
            ("4th Schedule", "Allocation of RS seats to states and UTs."),
            ("104th CAA", "Ended Anglo-Indian nomination to LS and state assemblies."),
        ],
        "visual_blocks": [
            {
                "id": "psm-comp-compare",
                "type": "compare",
                "title": "RS vs LS at a glance",
                "left": {
                    "title": "Rajya Sabha",
                    "items": [
                        "Max 250 · present ~245",
                        "Indirect + 12 nominated",
                        "PR / STV for elected seats",
                        "Federal chamber",
                    ],
                },
                "right": {
                    "title": "Lok Sabha",
                    "items": [
                        "Max 550 · present 543",
                        "Direct election",
                        "FPTP / territorial",
                        "Popular chamber",
                    ],
                },
            },
        ],
    },
    {
        "title": "System of Elections to Lok Sabha",
        "slug": "psm-elections",
        "sort_order": 3,
        "summary": (
            "Territorial constituencies with dual uniformity; delimitation freeze to 2026; "
            "SC/ST reservation till 2030; FPTP preferred over PR for LS."
        ),
        "body": (
            "## Territorial constituencies\n\n"
            "Two uniformity rules:\n"
            "1. Seat–population ratio **same across states** (except states under 6 million)\n"
            "2. Population–seat ratio **same across constituencies within a state**\n\n"
            "## Readjustment / delimitation\n\n"
            "- After each census: reallocate LS seats to states **and** redraw constituencies\n"
            "- Delimitation Acts: 1952, 1962, 1972, 2002\n"
            "- **42nd CAA (1976):** froze allocation & division at **1971** level till 2000\n"
            "- **84th CAA (2001):** freeze extended to **2026**; allowed redrawing on 1991 figures "
            "without changing state seat totals\n"
            "- **87th CAA (2003):** redrawing on **2001** census (still without changing seat totals)\n\n"
            "## SC/ST reservation\n\n"
            "- Population-ratio seats; **no separate electorate** — all voters elect\n"
            "- SC/ST candidates may contest **general** seats too\n"
            "- Extended by decades; **104th CAA** continues reservation till **2030**\n\n"
            "## FPTP vs PR\n\n"
            "- LS: **first-past-the-post** / single-member territorial constituencies\n"
            "- RS, Legislative Councils, President, VP: **PR by STV**\n"
            "- Why not PR for LS: literacy complexity + multiparty instability under parliamentary govt\n"
        ),
        "articles": [
            ("Art. 81", "Uniformity of representation between states and within a state."),
            ("Art. 82", "Readjustment after each census."),
            ("84th & 87th CAA", "Freeze to 2026; delimitation on 2001 figures without changing seat totals."),
        ],
        "visual_blocks": [
            {
                "id": "psm-elect-flow",
                "type": "flowchart",
                "title": "Delimitation freeze path",
                "root": "start",
                "steps": [
                    {
                        "id": "start",
                        "label": "Census → readjust seats & constituencies",
                        "options": [{"label": "Constitutional default", "next": "freeze"}],
                    },
                    {
                        "id": "freeze",
                        "label": "42nd → freeze at 1971 till 2000",
                        "options": [{"label": "Extended", "next": "84"}],
                    },
                    {
                        "id": "84",
                        "label": "84th → freeze till 2026",
                        "detail": "Redraw boundaries without changing state seat numbers",
                        "options": [{"label": "Census base", "next": "87"}],
                    },
                    {
                        "id": "87",
                        "label": "87th → use 2001 census for boundaries",
                        "detail": "Seat totals per state still frozen",
                    },
                ],
            },
        ],
    },
    {
        "title": "Duration of the Two Houses",
        "slug": "psm-duration",
        "sort_order": 4,
        "summary": (
            "RS is a continuing chamber (6-year term by RPA; ⅓ retire every 2 years). "
            "LS normal term 5 years; emergency can extend by 1 year at a time."
        ),
        "body": (
            "## Rajya Sabha\n\n"
            "- **Permanent / continuing chamber** — not subject to dissolution\n"
            "- **One-third** of members retire every **second** year\n"
            "- Term of a member: **6 years** (Representation of the People Act, 1951 — "
            "Constitution left term to Parliament)\n"
            "- Retiring members eligible for re-election / renomination any number of times\n\n"
            "## Lok Sabha\n\n"
            "- Normal term: **5 years** from first meeting after general elections → automatic dissolution\n"
            "- President may dissolve earlier; **not** challengeable in court\n"
            "- During **national emergency**: Parliament may extend by law for **one year at a time**; "
            "extension cannot continue beyond **6 months** after emergency ends\n"
        ),
        "articles": [
            ("Art. 83", "Duration of Houses of Parliament."),
            ("RPA 1951", "RS member term fixed at six years."),
        ],
        "visual_blocks": [
            {
                "id": "psm-duration-compare",
                "type": "compare",
                "title": "Continuing vs dissolving",
                "left": {
                    "title": "Rajya Sabha",
                    "items": [
                        "Not dissolved",
                        "⅓ retire every 2 years",
                        "6-year individual term",
                    ],
                },
                "right": {
                    "title": "Lok Sabha",
                    "items": [
                        "Dissolves after 5 years",
                        "Can be dissolved early",
                        "Emergency extension (1 yr / time)",
                    ],
                },
            },
        ],
    },
    {
        "title": "Membership of Parliament",
        "slug": "psm-membership",
        "sort_order": 5,
        "summary": (
            "Constitutional + RPA qualifications and disqualifications; Tenth Schedule defection "
            "(Speaker/Chairman decide; Kihoto review); vacating seats; oath before vote/privileges."
        ),
        "body": (
            "## Qualifications (Art. 84 + RPA)\n\n"
            "- Citizen of India; oath before EC-authorised person\n"
            "- Age: **RS ≥ 30**, **LS ≥ 25**\n"
            "- Other qualifications as Parliament may prescribe\n"
            "- RPA: registered elector for a parliamentary constituency "
            "(state-elector rule for RS dropped 2003; SC upheld 2006)\n"
            "- Reserved seat → must be SC/ST (but SC/ST can also contest general seats)\n\n"
            "## Disqualifications (Art. 102 + RPA)\n\n"
            "Constitution: office of profit; unsound mind (court); undischarged insolvent; "
            "not a citizen / foreign allegiance; disqualified under parliamentary law.\n\n"
            "RPA adds electoral offences, 2+ year conviction (not preventive detention), "
            "election expense defaults, govt contracts, ≥25% govt corporation office, "
            "dismissal for corruption/disloyalty, enmity/bribery, social crimes (untouchability, dowry, sati).\n\n"
            "- Ordinary disqualifications → **President** decides after **EC opinion** (binding)\n"
            "- **Tenth Schedule** (defection) → **Speaker (LS) / Chairman (RS)**; "
            "**Kihoto Hollohan (1992)** — decision subject to **judicial review**\n\n"
            "## Vacating seats\n\n"
            "Double membership rules (RPA); disqualification; resignation (Chair/Speaker may refuse "
            "if not voluntary); absence **60 days** without permission; election void / expulsion / "
            "President–VP / Governor appointment.\n\n"
            "## Oath & salaries\n\n"
            "- Must take oath before sitting/voting/privileges; ₹500/day penalty otherwise\n"
            "- Salaries by Parliament; pension by statute (1976+); officers’ pay **charged** on CFI\n"
        ),
        "articles": [
            ("Art. 84", "Qualification for membership of Parliament."),
            ("Art. 102", "Disqualifications for membership."),
            ("10th Schedule", "Disqualification on ground of defection."),
            ("Art. 101", "Vacation of seats."),
        ],
        "visual_blocks": [
            {
                "id": "psm-member-flow",
                "type": "flowchart",
                "title": "Who decides disqualification?",
                "root": "q",
                "steps": [
                    {
                        "id": "q",
                        "label": "Ground of disqualification?",
                        "options": [
                            {"label": "Art. 102 / RPA (ordinary)", "next": "pres"},
                            {"label": "Tenth Schedule (defection)", "next": "spk"},
                        ],
                    },
                    {
                        "id": "pres",
                        "label": "President (after EC opinion)",
                        "detail": "EC opinion binds the President",
                    },
                    {
                        "id": "spk",
                        "label": "Speaker / Chairman",
                        "detail": "Kihoto — judicially reviewable",
                    },
                ],
            },
            {
                "id": "psm-defection-callout",
                "type": "callout",
                "tone": "trap",
                "title": "Defection traps",
                "body": (
                    "Voluntarily giving up party · voting against whip · independent joining a party · "
                    "nominated member joining after 6 months. Not decided by the President."
                ),
            },
        ],
    },
    {
        "title": "Presiding Officers of Parliament",
        "slug": "psm-presiding-officers",
        "sort_order": 6,
        "summary": (
            "LS Speaker/Deputy/Panel/Pro Tem; RS Chairman (VP)/Deputy/Panel; "
            "Speaker’s unique money-bill and joint-sitting powers; impartiality safeguards."
        ),
        "body": (
            "## Speaker of Lok Sabha\n\n"
            "- Elected by LS from among members; date fixed by President\n"
            "- Vacates if ceases to be member; resigns to Deputy Speaker; removed by "
            "**effective majority** after **14 days’** notice\n"
            "- On dissolution, continues till new LS meets\n"
            "- **Casting vote** only; final interpreter of Constitution/Rules/precedents in House\n"
            "- Certifies **Money Bill** (final); presides over **joint sitting**; Tenth Schedule for LS\n"
            "- Ex-officio chair: Indian Parliamentary Group; conference of legislative presiding officers\n"
            "- Appoints chairs of LS committees; chairs BAC, Rules, General Purposes\n\n"
            "### Impartiality safeguards\n"
            "Security of tenure (effective majority) · pay charged on CFI · conduct not criticisable "
            "except on substantive motion · procedure not in court jurisdiction · casting vote only · "
            "7th in Warrant of Precedence (with CJI).\n\n"
            "UK convention: Speaker leaves party — **not fully established in India**.\n\n"
            "## Deputy Speaker · Panel · Pro Tem\n\n"
            "- Deputy: elected after Speaker; not subordinate to Speaker; auto-chairs any committee "
            "he/she joins; usually from opposition (convention, with exceptions)\n"
            "- Panel of ≤10 chairpersons — only when Speaker/Deputy **absent**, not when office **vacant**\n"
            "- **Speaker Pro Tem:** President appoints (usually seniormost) for first sitting of new LS — "
            "oath to members + elect new Speaker; then office ends\n\n"
            "## Rajya Sabha\n\n"
            "- **VP = ex-officio Chairman**; not a member of the House\n"
            "- **Cannot** certify Money Bills or preside over joint sittings (Speaker’s special powers)\n"
            "- Deputy Chairman elected from RS members; panel of vice-chairpersons\n"
            "- Separate House secretariats headed by Secretary-General\n"
        ),
        "articles": [
            ("Arts 93–97", "Speakers and Deputy Speakers of the House of the People."),
            ("Arts 89–92", "Chairman and Deputy Chairman of the Council of States."),
            ("Art. 98", "Secretariat of Parliament."),
        ],
        "visual_blocks": [
            {
                "id": "psm-speaker-pillars",
                "type": "pillars",
                "title": "Speaker — high-yield powers",
                "items": [
                    {
                        "id": "money",
                        "articles": "Art. 110",
                        "label": "Money Bill certificate",
                        "slug": "psm-presiding-officers",
                        "detail": "Decision final — not even President can question.",
                        "tone": "teal",
                    },
                    {
                        "id": "joint",
                        "articles": "Art. 108",
                        "label": "Joint sitting chair",
                        "slug": "psm-presiding-officers",
                        "detail": "Speaker → Dy Speaker → Dy Chairman RS.",
                        "tone": "olive",
                    },
                    {
                        "id": "def",
                        "articles": "10th Sch.",
                        "label": "Defection (LS)",
                        "slug": "psm-membership",
                        "detail": "Subject to judicial review (Kihoto).",
                        "tone": "gold",
                    },
                    {
                        "id": "cast",
                        "articles": "Art. 100",
                        "label": "Casting vote",
                        "slug": "psm-presiding-officers",
                        "detail": "No first-instance vote — only to break a tie.",
                        "tone": "orange",
                    },
                ],
            },
        ],
    },
    {
        "title": "Leaders in Parliament",
        "slug": "psm-leaders",
        "sort_order": 7,
        "summary": (
            "Leader of the House (PM or nominee); Leader of Opposition (1977 Act; ~1/10 strength); "
            "Whips as party floor managers."
        ),
        "body": (
            "## Leader of the House\n\n"
            "- **LS:** PM if LS member, else a LS minister nominated by PM\n"
            "- **RS:** RS minister nominated by PM\n"
            "- Shapes business of the House; may nominate a deputy leader\n"
            "- US analogue: majority leader\n\n"
            "## Leader of the Opposition\n\n"
            "- Statutory recognition: **Salary and Allowances of Leaders of Opposition in Parliament Act, 1977**\n"
            "- Status ≈ Cabinet Minister\n"
            "- Party in opposition with **greatest numerical strength**, recognised by Speaker/Chairman\n"
            "- Directions: usually need **≥ 1/10** of total membership of that House as a party\n"
            "- First official LoP recognised in **1969**; US analogue: minority leader\n"
            "- UK **Shadow Cabinet** — not an Indian constitutional institution\n\n"
            "## Whips\n\n"
            "- Party functionaries ensuring attendance and voting discipline\n"
            "- Based on convention / party organisation, not a constitutional office\n"
        ),
        "articles": [
            ("Rules of LS/RS", "Leader of the House definitions."),
            ("1977 LoP Act", "Statutory recognition and facilities of Leaders of Opposition."),
        ],
        "visual_blocks": [
            {
                "id": "psm-leaders-callout",
                "type": "callout",
                "tone": "tip",
                "title": "LoP recognition",
                "body": (
                    "Greatest opposition strength + Speaker/Chairman recognition; "
                    "party usually needs one-tenth of House membership. Facilities ≈ Cabinet Minister."
                ),
            },
        ],
    },
    {
        "title": "Sessions of Parliament",
        "slug": "psm-sessions",
        "sort_order": 8,
        "summary": (
            "Summoning, adjournment vs prorogation vs dissolution, quorum 1/10, "
            "voting methods, language, ministers/AG rights, lame-duck session."
        ),
        "body": (
            "## Summoning · gap rule\n\n"
            "- President summons each House; **maximum gap** between two sessions: **6 months**\n"
            "- Usually three sessions: Budget, Monsoon, Winter\n\n"
            "## Adjournment vs Prorogation vs Dissolution\n\n"
            "| | Adjournment | Prorogation | Dissolution |\n"
            "|---|-------------|-------------|-------------|\n"
            "| Who | Presiding officer | President | President (LS only) |\n"
            "| Effect | Suspends sitting | Ends a session | Ends the House life |\n"
            "| Pending business | Continues | Does **not** kill bills (generally) | LS bills may **lapse** |\n\n"
            "- **Adjournment sine die:** indefinite adjournment without fixing next date\n"
            "- Only **Lok Sabha** can be dissolved; RS cannot\n\n"
            "## Quorum · voting · language\n\n"
            "- Quorum: **1/10** of total membership of the House\n"
            "- Default: simple majority of members present and voting; chair has casting vote\n"
            "- Methods: voice vote, division (AVR / slips / lobbies obsolete), secret ballot, physical count\n"
            "- Floor languages: **Hindi + English** (Official Languages Act continued English after 1965); "
            "mother tongue with permission; 8th Schedule interpretation\n\n"
            "## Ministers & Attorney General\n\n"
            "- Right to speak in either House / joint sitting / committees — **no vote** unless members\n"
            "- Enables LS minister in RS (and vice versa); non-member minister for up to 6 months\n\n"
            "## Lame-duck session\n\n"
            "Last session of the **outgoing** LS after a new LS is elected; members not re-elected = lame ducks. "
            "Historically used for Vote on Account before new House sits."
        ),
        "articles": [
            ("Art. 85", "Sessions of Parliament, prorogation and dissolution."),
            ("Art. 86", "Right of President to address and send messages."),
            ("Art. 87", "Special address by the President."),
            ("Art. 88", "Rights of Ministers and Attorney-General as respects Houses."),
            ("Art. 100", "Voting in Houses, power of Houses to act notwithstanding vacancies."),
        ],
        "visual_blocks": [
            {
                "id": "psm-sessions-compare",
                "type": "compare",
                "title": "Adjourn vs Prorogue vs Dissolve",
                "left": {
                    "title": "Adjournment",
                    "items": [
                        "Presiding officer",
                        "Pauses a sitting",
                        "Sine die = no next date",
                    ],
                },
                "right": {
                    "title": "Prorogation / Dissolution",
                    "items": [
                        "President prorogues → ends session",
                        "President dissolves LS only",
                        "Dissolution can lapse LS bills",
                    ],
                },
            },
        ],
    },
    {
        "title": "Types of Majority",
        "slug": "psm-majority",
        "sort_order": 9,
        "summary": (
            "Simple (present & voting), Effective (all then members), Absolute (total membership), "
            "and Special majorities — map each to the correct constitutional use."
        ),
        "body": (
            "## Four types\n\n"
            "### 1. Simple majority\n"
            "Members **present and voting** (Art. 100 default).\n"
            "Uses: ordinary/money/financial bills; Adjournment / No-Confidence / Confidence / "
            "Censure / Motion of Thanks; LS removal of VP (Art. 67); approval of Art. 356 / 360; "
            "election of Speaker, Dy Speaker, Dy Chairman RS; LS resolution disapproving national emergency continuance.\n\n"
            "### 2. Effective majority\n"
            "Majority of **all the then members** (exclude vacancies).\n"
            "Uses: removal of VP in **RS**; removal of Dy Chairman RS; removal of Speaker / Dy Speaker LS.\n\n"
            "### 3. Absolute majority\n"
            "Majority of **total membership** (ignore vacancies/absentees). "
            "Not a standalone constitutional requirement — appears as a **component** of special majority.\n\n"
            "### 4. Special majority\n"
            "Several constitutional flavours (e.g. Art. 368: majority of total membership **and** "
            "2/3 of members present and voting; Art. 61 impeachment; Art. 249; etc.). "
            "Always check **which** special majority the provision uses.\n\n"
            "### Memory\n"
            "**S-E-A-Sp** — Simple · Effective · Absolute · Special."
        ),
        "articles": [
            ("Art. 100", "Default simple majority of members present and voting."),
            ("Arts 67, 90, 94", "Effective majority removals."),
            ("Art. 368", "Special majority for constitutional amendment."),
        ],
        "visual_blocks": [
            {
                "id": "psm-majority-pillars",
                "type": "pillars",
                "title": "Majority map",
                "items": [
                    {
                        "id": "simple",
                        "articles": "Art. 100",
                        "label": "Simple",
                        "slug": "psm-majority",
                        "detail": "Present & voting — default rule.",
                        "tone": "teal",
                    },
                    {
                        "id": "eff",
                        "articles": "then members",
                        "label": "Effective",
                        "slug": "psm-majority",
                        "detail": "Total membership minus vacancies — removals.",
                        "tone": "olive",
                    },
                    {
                        "id": "abs",
                        "articles": "total",
                        "label": "Absolute",
                        "slug": "psm-majority",
                        "detail": "Total membership — part of special majority.",
                        "tone": "gold",
                    },
                    {
                        "id": "sp",
                        "articles": "Art. 368+",
                        "label": "Special",
                        "slug": "psm-majority",
                        "detail": "Check the exact formula in the Article.",
                        "tone": "orange",
                    },
                ],
            },
            {
                "id": "psm-majority-trap",
                "type": "callout",
                "tone": "trap",
                "title": "Speaker removal",
                "body": (
                    "Speaker / Deputy Speaker removal needs **effective majority**, not simple majority — "
                    "and 14 days’ advance notice."
                ),
            },
        ],
    },
]

EDGES = [
    (HUB_SLUG, "parent", "psm-organisation"),
    (HUB_SLUG, "parent", "psm-composition"),
    (HUB_SLUG, "parent", "psm-elections"),
    (HUB_SLUG, "parent", "psm-duration"),
    (HUB_SLUG, "parent", "psm-membership"),
    (HUB_SLUG, "parent", "psm-presiding-officers"),
    (HUB_SLUG, "parent", "psm-leaders"),
    (HUB_SLUG, "parent", "psm-sessions"),
    (HUB_SLUG, "parent", "psm-majority"),
    ("psm-organisation", "related", "psm-composition"),
    ("psm-composition", "related", "psm-elections"),
    ("psm-elections", "related", "psm-duration"),
    ("psm-membership", "related", "psm-presiding-officers"),
    ("psm-presiding-officers", "related", "psm-leaders"),
    ("psm-sessions", "related", "psm-majority"),
    ("psm-presiding-officers", "related", "psm-majority"),
    ("parliamentary-system", "related", HUB_SLUG),
    (HUB_SLUG, "related", "parliament-procedure-budget"),
    (HUB_SLUG, "related", "parliament-powers-privileges"),
]

SAMPLE_PYQS = [
    (
        2013,
        "The Parliament of India consists of:",
        "The President, the Council of States, and the House of the People (Art. 79).",
        ["psm-organisation", HUB_SLUG],
    ),
    (
        2015,
        "With reference to the Lok Sabha, consider statements on Anglo-Indian nomination:",
        "104th Constitutional Amendment discontinued nomination of Anglo-Indians to the Lok Sabha (from 25 Jan 2020).",
        ["psm-composition", HUB_SLUG],
    ),
    (
        2017,
        "Which of the following is not subject to dissolution?",
        "Rajya Sabha is a continuing chamber; only Lok Sabha is dissolved.",
        ["psm-duration", "psm-sessions"],
    ),
    (
        2019,
        "Disqualification under the Tenth Schedule is decided by:",
        "Speaker (Lok Sabha) or Chairman (Rajya Sabha); subject to judicial review (Kihoto Hollohan).",
        ["psm-membership", "psm-presiding-officers"],
    ),
    (
        2021,
        "Removal of the Speaker of the Lok Sabha requires:",
        "A resolution passed by an effective majority (majority of all the then members) after 14 days’ notice.",
        ["psm-majority", "psm-presiding-officers"],
    ),
]


class Command(BaseCommand):
    help = (
        "Seed Parliament: Structure & Membership "
        "(Laxmikanth Ch.23 pp. 326–348) under Part III Central Government."
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
                "title": "Parliament: Structure & Membership",
                "sort_order": 6,
                "book_ref": "Laxmikanth 8th Ed, Ch. 23 (pp. 326–348) — Structure & Membership",
                "summary": (
                    "Visual revision of Ch.23 part 1 — organisation, composition, elections, "
                    "duration, membership, officers, leaders, sessions, and types of majority."
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
                "title": "Parliament: Structure & Membership",
                "summary": (
                    "Frame of the Union legislature — who sits, who chairs, how long, "
                    "and how the Houses are summoned (Arts 79–122 opening half)."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **frame** mental model, then "
                    "**Organisation** → **Composition** → **Elections** → **Duration** → "
                    "**Membership** → **Officers** → **Leaders** → **Sessions** → **Majority**. "
                    "Continue with Procedure & Budget, then Powers & Privileges. "
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
            ref="Laxmikanth Ch. 23 (pp. 326–348)",
            excerpt=(
                "Parliament — organisation, composition, elections, duration, membership, "
                "presiding officers, leaders, sessions, types of majority."
            ),
            sort_order=0,
        )
        ConceptArticle.objects.create(
            concept=hub,
            ref="Arts 79–100",
            excerpt="Core structural provisions for the Union Parliament in Part V.",
            sort_order=1,
        )

        psm_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            Q(source__slug__in=psm_slugs) | Q(target__slug__in=psm_slugs),
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
                f"Parliament Structure & Membership seeded ({academy.slug}): "
                f"{chapter.title} with {len(CLUSTERS) + 1} concepts, "
                f"{created_edges} new edges, {len(SAMPLE_PYQS)} PYQs linked."
            )
        )
