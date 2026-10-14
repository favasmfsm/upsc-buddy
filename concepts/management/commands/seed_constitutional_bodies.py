"""Seed Laxmikanth Ch.43-54 Constitutional Bodies (visual revision - Part VII)."""

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

HUB_SLUG = "constitutional-bodies"
CHAPTER_SLUG = "constitutional-bodies"

BODY_PILLARS = [
    {
        "id": "eci",
        "articles": "Art. 324",
        "label": "Election Commission",
        "slug": "cb-election-commission",
        "detail": "Free and fair elections to Parliament, state legislatures, President & VP.",
        "tone": "teal",
    },
    {
        "id": "upsc",
        "articles": "Arts 315-323",
        "label": "Union Public Service Commission",
        "slug": "cb-upsc",
        "detail": "Central recruiting agency - merit and advice on personnel.",
        "tone": "olive",
    },
    {
        "id": "spsc",
        "articles": "Arts 315-323",
        "label": "State Public Service Commission",
        "slug": "cb-spsc",
        "detail": "State recruiting watchdog - Governor appoints, President removes.",
        "tone": "gold",
    },
    {
        "id": "fc",
        "articles": "Art. 280",
        "label": "Finance Commission",
        "slug": "cb-finance-commission",
        "detail": "Quasi-judicial balancing wheel of fiscal federalism - advisory.",
        "tone": "orange",
    },
    {
        "id": "gst",
        "articles": "Art. 279-A",
        "label": "GST Council",
        "slug": "cb-gst-council",
        "detail": "Constitutional federal forum for GST rates, laws, and exemptions.",
        "tone": "terracotta",
    },
    {
        "id": "ncsc",
        "articles": "Art. 338",
        "label": "National Commission for SCs",
        "slug": "cb-ncsc",
        "detail": "Investigate and monitor SC safeguards; civil-court powers.",
        "tone": "maroon",
    },
    {
        "id": "ncst",
        "articles": "Art. 338-A",
        "label": "National Commission for STs",
        "slug": "cb-ncst",
        "detail": "Separate ST commission (89th) with forest/land/PESA focus.",
        "tone": "teal",
    },
    {
        "id": "ncbc",
        "articles": "Art. 338-B",
        "label": "National Commission for BCs",
        "slug": "cb-ncbc",
        "detail": "Constitutionalised by 102nd - SEBC safeguards at par with NCSC/NCST.",
        "tone": "olive",
    },
    {
        "id": "clm",
        "articles": "Art. 350-B",
        "label": "Linguistic Minorities Officer",
        "slug": "cb-linguistic-minorities",
        "detail": "Commissioner investigates linguistic minority safeguards (7th Amendment).",
        "tone": "gold",
    },
    {
        "id": "cag",
        "articles": "Arts 148-151",
        "label": "Comptroller and Auditor General",
        "slug": "cb-cag",
        "detail": "Guardian of the public purse - Ambedkar's most important officer.",
        "tone": "orange",
    },
    {
        "id": "ag",
        "articles": "Art. 76",
        "label": "Attorney General of India",
        "slug": "cb-attorney-general",
        "detail": "Highest law officer of the Union - pleasure of the President.",
        "tone": "terracotta",
    },
    {
        "id": "advg",
        "articles": "Art. 165",
        "label": "Advocate General of the State",
        "slug": "cb-advocate-general",
        "detail": "Highest law officer of the state - corresponds to the AG.",
        "tone": "maroon",
    },
]

HUB_VISUAL_BLOCKS = [
    {
        "id": "cb-mental-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Watchdogs & advisors",
        "topic_label": "Constitutional Bodies",
        "subject_label": "Indian Constitution",
        "relation_label": "Helps you separate",
        "protects_from": [
            "Statutory vs constitutional bodies",
            "Pleasure doctrine vs address removal",
            "ECI vs State Election Commission",
            "AG vs Law Minister / SG",
        ],
        "insight": (
            "These offices are born from the Constitution itself - "
            "scan composition, appointment, removal, and reporting before functions."
        ),
    },
    {
        "id": "cb-twelve-pillars",
        "type": "pillars",
        "title": "Twelve constitutional bodies",
        "items": BODY_PILLARS,
    },
    {
        "id": "cb-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Exam in 5 Minutes - entry path",
        "body": (
            "Drill bodies left to right, then open Master Comparisons and Articles & Final Sheet. "
            "Always ask: Who appoints? Who removes? Who do they report to? "
            "Traps: SEC != ECI · AG != Law Minister · FC != Planning Commission/NITI · "
            "NCBC state report goes to state government (not Governor)."
        ),
    },
]


CLUSTERS = [
{'title': 'Election Commission',
 'slug': 'cb-election-commission',
 'sort_order': 1,
 'summary': 'Art. 324 permanent All-India body for Parliament, state legislatures, President and '
            'VP elections — not local body polls.',
 'body': '## Election Commission (Art. 324)\n'
         '\n'
         '### Constitutional status\n'
         '- Permanent, independent body created by the Constitution.\n'
         '- All-India body common to Centre and states.\n'
         '- **Not** concerned with panchayat/municipality elections (State Election Commission — '
         'Arts 243K / 243ZA).\n'
         '\n'
         '### Composition\n'
         '- CEC + such number of other ECs as the President may fix.\n'
         '- When other ECs are appointed, CEC acts as **chairman**.\n'
         '- President may appoint **regional commissioners** after consulting the EC.\n'
         '- Since Oct 1993: **multi-member** (CEC + 2 ECs).\n'
         '\n'
         '### Appointment, tenure, conditions (Act, 1991)\n'
         '- Appointed by the President.\n'
         '- Equal powers and SC-judge-like salary among CEC and ECs.\n'
         '- Difference of opinion → decided by **majority**.\n'
         '- Term: **6 years or 65 years**, whichever earlier; resign to President.\n'
         '\n'
         '### Removal\n'
         '- **CEC:** same manner and grounds as a Supreme Court judge (special majority address).\n'
         '- **Other EC / regional commissioner:** only on **recommendation of the CEC**.\n'
         '- CEC does **not** hold office during the pleasure of the President.\n'
         '\n'
         '### Independence safeguards\n'
         '- Security of tenure for CEC.\n'
         '- Service conditions of CEC cannot be varied to disadvantage after appointment.\n'
         '- EC/RC removal needs CEC recommendation.\n'
         '\n'
         '### Powers & functions\n'
         '- Superintendence, direction and control of elections to Parliament, state legislatures, '
         'President and Vice-President.\n'
         '- Electoral rolls, party recognition, symbols, Model Code practice themes.\n'
         '\n'
         '### Book gaps / staples\n'
         '- Constitution does not prescribe member qualifications; term largely via law.\n'
         '- *Anoop Baranwal* (2023) + **CEC and Other ECs Act, 2023** — selection committee (PM, '
         'LoP, Union Cabinet Minister).\n'
         '\n'
         '### Reporting / accountability\n'
         '- Autonomous commission; Parliament may legislate on elections.\n'
         '\n'
         '### UPSC themes\n'
         'Composition history · CEC vs EC removal · SEC vs ECI · multi-member majority.\n'
         '\n'
         '### Prelims traps\n'
         'ECI ≠ local body polls · Other ECs removed only on CEC recommendation · CEC ≠ pleasure '
         'tenure.\n'
         '\n'
         '### Mains value-add\n'
         'Structural independence (tenure) vs contested appointment design — link *Anoop Baranwal* '
         'and 2023 Act neutrally.\n',
 'articles': [('Art. 324',
               'Superintendence, direction and control of elections vested in Election '
               'Commission.'),
              ('Art. 243K / 243ZA',
               'State Election Commission — panchayat and municipality elections (contrast).')],
 'visual_blocks': [{'id': 'cb-eci-timeline',
                    'type': 'timeline',
                    'title': 'Single → multi-member EC',
                    'events': [{'id': 'e1',
                                'year': 1950,
                                'label': 'Single-member',
                                'detail': 'CEC alone till Oct 1989.'},
                               {'id': 'e2',
                                'year': 1989,
                                'label': 'Three members',
                                'detail': 'Two ECs added after voting age cut to 18.'},
                               {'id': 'e3',
                                'year': 1990,
                                'label': 'Reverted',
                                'detail': 'Two EC posts abolished (Jan).'},
                               {'id': 'e4',
                                'year': 1993,
                                'label': 'Stable trio',
                                'detail': 'CEC + 2 ECs again — continues today.'},
                               {'id': 'e5',
                                'year': 2023,
                                'label': 'Appointment Act',
                                'detail': 'Anoop Baranwal + CEC Act 2023 selection panel.'}]},
                   {'id': 'cb-eci-removal-flow',
                    'type': 'flowchart',
                    'title': 'Removal: CEC vs other EC',
                    'root': 'start',
                    'steps': [{'id': 'start',
                               'label': 'Who is removed?',
                               'detail': 'Check office held.',
                               'options': [{'label': 'CEC', 'next': 'cec'},
                                           {'label': 'EC / Regional Commissioner', 'next': 'ec'}]},
                              {'id': 'cec',
                               'label': 'Like SC judge',
                               'detail': 'Both Houses special majority address → President. Not '
                                         'pleasure tenure.'},
                              {'id': 'ec',
                               'label': 'Only on CEC recommendation',
                               'detail': 'CEC tenure shield does not fully extend to other ECs.'}]},
                   {'id': 'cb-eci-trap',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Prelims trap',
                    'body': 'Election Commission ≠ State Election Commission. Art. 324 covers '
                            'Parliament / state legislatures / President / VP only.'}]},
{'title': 'Union Public Service Commission',
 'slug': 'cb-upsc',
 'sort_order': 2,
 'summary': 'Central recruiting agency under Arts 315–323 — President appoints; 6 years or 65; '
            'misbehaviour removal via SC enquiry.',
 'body': '## UPSC (Arts 315–323, Part XIV)\n'
         '\n'
         '### Constitutional status\n'
         '- Independent constitutional body — central recruiting agency.\n'
         '\n'
         '### Composition & qualifications\n'
         '- Chairman + other members; strength fixed by President.\n'
         '- Only constitutional qualification: **≥½ members** must have held office under Union or '
         'a state for **≥10 years**.\n'
         '- President determines conditions of service and staff strength.\n'
         '\n'
         '### Appointment & tenure\n'
         '- Appointed by the President.\n'
         '- Term: **6 years or age 65**, whichever earlier; resign to President.\n'
         '- Acting chairman if vacancy or inability.\n'
         '\n'
         '### Removal\n'
         '- President may remove for: insolvency; paid outside employment; infirmity of '
         'mind/body.\n'
         '- **Misbehaviour:** President refers to **Supreme Court**; SC advice **binding**; may '
         'suspend during enquiry.\n'
         '- Misbehaviour includes interest in government contracts / profits (except as ordinary '
         'company member).\n'
         '\n'
         '### Independence\n'
         '- Security of tenure (constitutional removal path only).\n'
         '- Conditions not varied to disadvantage after appointment.\n'
         '- Expenses charged on **Consolidated Fund of India**.\n'
         '- Post-retirement: Chairman — no further Union/state employment; Member — no Union '
         'employment except as UPSC/SPSC Chairman.\n'
         '\n'
         '### Powers & functions\n'
         '- Conduct exams for All-India and Central Services.\n'
         '- Advise on recruitment methods, appointments, promotions, transfers, disciplinary '
         'matters.\n'
         '- Advice generally **not binding** (non-acceptance explained in report).\n'
         '- Certain posts/matters may be excluded by President from consultation.\n'
         '\n'
         '### Reporting\n'
         '- Annual report to President → Parliament with action memorandum.\n'
         '\n'
         '### Committees / judgments / reforms\n'
         '- Book focus is structural; emphasise advisory vs binding distinction in answers.\n'
         '\n'
         '### UPSC themes / traps\n'
         'Age 65 vs SPSC 62 · charged on CFI · advisory nature · SC binding advice on removal.\n'
         '\n'
         '### Mains value-add\n'
         'UPSC as bulwark of meritocracy — independence = financial + tenure + post-retirement '
         'bar.\n',
 'articles': [('Arts 315–323',
               'Public Service Commissions for the Union and the states (Part XIV).'),
              ('Art. 320', 'Functions of Public Service Commissions.'),
              ('Art. 323', 'Reports of Public Service Commissions.')],
 'visual_blocks': [{'id': 'cb-upsc-pillars',
                    'type': 'pillars',
                    'title': 'UPSC function map',
                    'items': [{'id': 'exams',
                               'articles': 'Recruitment',
                               'label': 'Examinations',
                               'detail': 'All-India & Central Services exams.',
                               'tone': 'teal'},
                              {'id': 'advise',
                               'articles': 'Art. 320',
                               'label': 'Advise government',
                               'detail': 'Methods, promotions, discipline — usually advisory.',
                               'tone': 'olive'},
                              {'id': 'report',
                               'articles': 'Art. 323',
                               'label': 'Annual report',
                               'detail': 'President → Parliament with action memo.',
                               'tone': 'gold'},
                              {'id': 'shield',
                               'articles': 'Independence',
                               'label': 'Safeguards',
                               'detail': 'CFI charge + removal path + post-retirement bar.',
                               'tone': 'orange'}]},
                   {'id': 'cb-upsc-removal',
                    'type': 'flowchart',
                    'title': 'UPSC removal path',
                    'root': 'ground',
                    'steps': [{'id': 'ground',
                               'label': 'Ground of removal?',
                               'detail': 'President initiates.',
                               'options': [{'label': 'Insolvency / outside pay / infirmity',
                                            'next': 'direct'},
                                           {'label': 'Misbehaviour', 'next': 'sc'}]},
                              {'id': 'direct',
                               'label': 'President removes',
                               'detail': 'No SC enquiry required for these three grounds.'},
                              {'id': 'sc',
                               'label': 'SC enquiry (advice binding)',
                               'detail': 'President may suspend pending report; then remove if SC '
                                         'upholds.'}]},
                   {'id': 'cb-upsc-trap',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Prelims trap',
                    'body': 'UPSC advice on appointments/discipline is generally **not binding**. '
                            'SC advice on **misbehaviour removal** is binding.'}]},
{'title': 'State Public Service Commission',
 'slug': 'cb-spsc',
 'sort_order': 3,
 'summary': 'State recruiting body under Arts 315–323 — Governor appoints, President alone '
            'removes; age ceiling 62.',
 'body': '## SPSC (Arts 315–323)\n'
         '\n'
         '### Constitutional status\n'
         '- Constitutional body parallel to UPSC in each state.\n'
         '- Joint State PSC possible for two or more states (Art. 315); UPSC may serve a state’s '
         'needs if requested.\n'
         '\n'
         '### Composition & qualifications\n'
         '- Chairman + members; strength by Governor.\n'
         '- Same ½ × 10-year government service rule as UPSC.\n'
         '- Governor fixes conditions of service and staff.\n'
         '\n'
         '### Appointment & tenure\n'
         '- Appointed by the **Governor**.\n'
         '- Term: **6 years or age 62** (UPSC = 65).\n'
         '- Resign to Governor; acting chairman provisions mirror UPSC.\n'
         '\n'
         '### Removal (critical)\n'
         '- Appointed by Governor but **removed only by the President** (same grounds/manner as '
         'UPSC).\n'
         '- During SC misbehaviour enquiry, **Governor** may suspend.\n'
         '\n'
         '### Independence\n'
         '- Security of tenure via presidential removal path.\n'
         '- Conditions not varied to disadvantage after appointment.\n'
         '- Expenses charged on **state Consolidated Fund**.\n'
         '\n'
         '### Functions & reporting\n'
         '- State recruitment exams and personnel advice.\n'
         '- Annual report to **Governor** → state legislature with action memorandum.\n'
         '\n'
         '### Prelims traps\n'
         'Governor appoints ≠ Governor removes · Age 62 · Fund = state CF · Joint SPSC is '
         'constitutional.\n'
         '\n'
         '### Mains value-add\n'
         'Federal design: state appointment + Union removal = insulation from state executive '
         'pressure.\n',
 'articles': [('Art. 315',
               'Public Service Commissions for the Union and for the states; Joint State PSC.'),
              ('Art. 317', 'Removal and suspension of a member of a Public Service Commission.'),
              ('Art. 322–323', 'Expenses charged on Consolidated Fund; reports.')],
 'visual_blocks': [{'id': 'cb-upsc-spsc-compare',
                    'type': 'comparison',
                    'title': 'UPSC vs SPSC',
                    'columns': [{'id': 'upsc',
                                 'heading': 'UPSC',
                                 'points': ['Appointed by President',
                                            'Age ceiling 65',
                                            'Removed by President',
                                            'Expenses on CFI',
                                            'Report → President → Parliament']},
                                {'id': 'spsc',
                                 'heading': 'SPSC',
                                 'points': ['Appointed by Governor',
                                            'Age ceiling 62',
                                            'Removed only by President',
                                            'Expenses on state CF',
                                            'Report → Governor → legislature']}]},
                   {'id': 'cb-spsc-trap',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Highest-yield trap',
                    'body': 'SPSC members are appointed by the Governor but can be removed **only '
                            'by the President** — never by the Governor alone.'},
                   {'id': 'cb-spsc-tip',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Memory trick',
                    'body': 'UPSC 65 / SPSC 62 — ‘Union is older ceiling’.'}]},
{'title': 'Finance Commission',
 'slug': 'cb-finance-commission',
 'sort_order': 4,
 'summary': 'Art. 280 quasi-judicial body every fifth year — tax devolution and grants; '
            'recommendations are advisory.',
 'body': '## Finance Commission (Art. 280)\n'
         '\n'
         '### Constitutional status\n'
         '- Quasi-judicial constitutional body.\n'
         '- Constituted by President every **fifth year** or earlier as necessary.\n'
         '- Balancing wheel of **fiscal federalism**.\n'
         '\n'
         '### Composition & qualifications\n'
         '- Chairman + **four** other members; period fixed in President’s order; eligible for '
         'reappointment.\n'
         '- Parliament fixes qualifications: Chairman — experience in public affairs; members from '
         'HC judge (or eligible), finance & accounts, financial administration, economics.\n'
         '\n'
         '### Functions\n'
         '1. Distribution of net tax proceeds — Centre ↔ states and among states.\n'
         '2. Principles of grants-in-aid from Consolidated Fund of India.\n'
         '3. Measures to augment state CF to supplement panchayat/municipality resources (on State '
         'FC recommendations) — **73rd/74th** add-on.\n'
         '4. Any other matter referred by President in interest of sound finance.\n'
         '\n'
         '### Nature of recommendations\n'
         '- **Advisory only** — not binding on the Union.\n'
         '- Rajamannar (4th FC): recommendations should not be turned down without compelling '
         'reasons.\n'
         '\n'
         '### Reporting\n'
         '- Report to President → both Houses with explanatory memorandum on action taken.\n'
         '\n'
         '### Context / reforms\n'
         '- Overlap with erstwhile Planning Commission till 2014; NITI Aayog replaced Planning '
         'Commission (2015).\n'
         '\n'
         '### UPSC themes / traps\n'
         'Advisory ≠ binding · FC ≠ GST Council · local-body resource function is post-73rd/74th.\n'
         '\n'
         '### Mains value-add\n'
         'FC as constitutional fiscal federalism vs NITI as policy think-tank — different legal '
         'status.\n',
 'articles': [('Art. 280', 'Finance Commission — constitution, duties, and report.'),
              ('Art. 281', 'Recommendations of the Finance Commission — laid before Parliament.')],
 'visual_blocks': [{'id': 'cb-fc-tree',
                    'type': 'tree',
                    'title': 'Finance Commission mandate',
                    'root': {'id': 'fc',
                             'label': 'Finance Commission (Art. 280)',
                             'detail': 'Quasi-judicial · advisory',
                             'children': [{'id': 'tax',
                                           'label': 'Tax devolution',
                                           'detail': 'Vertical + horizontal shares'},
                                          {'id': 'gia',
                                           'label': 'Grants-in-aid principles',
                                           'detail': 'From Consolidated Fund of India'},
                                          {'id': 'local',
                                           'label': 'Local body resources',
                                           'detail': 'Augment state CF (73rd/74th)'},
                                          {'id': 'other',
                                           'label': 'Any other matter',
                                           'detail': 'Referred by President'}]}},
                   {'id': 'cb-fc-timeline',
                    'type': 'timeline',
                    'title': 'FC evolution (revision nodes)',
                    'events': [{'id': 'f1',
                                'year': 1951,
                                'label': '1st FC',
                                'detail': 'K.C. Neogy — fiscal federalism begins.'},
                               {'id': 'f2',
                                'year': 1993,
                                'label': '73rd/74th',
                                'detail': 'Local-body resource mandate added.'},
                               {'id': 'f3',
                                'year': 2015,
                                'label': 'NITI era',
                                'detail': 'Planning Commission ended — FC role clearer.'},
                               {'id': 'f4',
                                'year': 2017,
                                'label': '15th FC',
                                'detail': 'N.K. Singh — post-GST fiscal reset.'}]},
                   {'id': 'cb-fc-trap',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Prelims trap',
                    'body': 'Finance Commission recommendations are **advisory**. Do not confuse '
                            'with GST Council (Art. 279-A).'}]},
{'title': 'GST Council',
 'slug': 'cb-gst-council',
 'sort_order': 5,
 'summary': 'Art. 279-A federal GST forum (101st Amendment) — FM chairs; ¾ weighted majority with '
            'Centre ⅓ and states ⅔.',
 'body': '## GST Council (Art. 279-A)\n'
         '\n'
         '### Constitutional status\n'
         '- Created by **101st Amendment (2016)**; President constitutes by order.\n'
         '- First constitutional federal body vested with major GST decisions.\n'
         '- Secretariat at New Delhi; Union Revenue Secretary = ex-officio Secretary.\n'
         '\n'
         '### Composition\n'
         '1. Union Finance Minister — **Chairperson**\n'
         '2. Union MoS (Revenue or Finance)\n'
         '3. State finance/taxation (or other nominated) ministers\n'
         '- States choose one among themselves as Vice-Chairperson.\n'
         '- CBIC Chairperson — permanent **non-voting** invitee.\n'
         '\n'
         '### Working\n'
         '- Quorum: **one-half** of total members.\n'
         '- Decision: majority of **not less than ¾** of weighted votes of members present and '
         'voting.\n'
         '- Centre weight = **⅓**; all states combined = **⅔**.\n'
         '\n'
         '### Functions\n'
         '- Taxes/cesses to merge into GST; goods/services to tax or exempt.\n'
         '- Model GST laws, levy principles, IGST apportionment, place of supply.\n'
         '- Threshold exemption; rates including floor rates with bands; special rates; '
         'special-state provisions; any other GST matter.\n'
         '\n'
         '### Prelims traps\n'
         'Centre alone cannot outvote states under the weight formula · CBIC invitee has no vote · '
         'Art. 279-A ≠ Art. 280.\n'
         '\n'
         '### Mains value-add\n'
         'GST Council as institutionalised cooperative federalism — contrast with FC’s fiscal '
         'transfers.\n',
 'articles': [('Art. 279-A',
               'Goods and Services Tax Council — composition, voting, and functions.'),
              ('101st Amendment', 'Constitutional gateway for GST (2016).')],
 'visual_blocks': [{'id': 'cb-gst-vote-flow',
                    'type': 'flowchart',
                    'title': 'GST Council decision rule',
                    'root': 'meet',
                    'steps': [{'id': 'meet',
                               'label': 'Meeting',
                               'detail': 'Quorum = ½ of total members.',
                               'options': [{'label': 'Vote on proposal', 'next': 'weights'}]},
                              {'id': 'weights',
                               'label': 'Weighted votes',
                               'detail': 'Centre ⅓ · States combined ⅔ of votes cast.',
                               'options': [{'label': '≥ ¾ weighted majority', 'next': 'pass'},
                                           {'label': 'Below ¾', 'next': 'fail'}]},
                              {'id': 'pass',
                               'label': 'Recommendation adopted',
                               'detail': 'To Centre and states on GST matters.'},
                              {'id': 'fail',
                               'label': 'Not carried',
                               'detail': 'Needs further consultation / revised proposal.'}]},
                   {'id': 'cb-gst-pillars',
                    'type': 'pillars',
                    'title': 'What the Council decides',
                    'items': [{'id': 'merge',
                               'articles': 'Taxes',
                               'label': 'Merge / exempt',
                               'detail': 'Which taxes enter GST; what is exempt.',
                               'tone': 'teal'},
                              {'id': 'laws',
                               'articles': 'Model laws',
                               'label': 'Laws & IGST',
                               'detail': 'Model laws, place of supply, IGST principles.',
                               'tone': 'olive'},
                              {'id': 'rates',
                               'articles': 'Rates',
                               'label': 'Rates & bands',
                               'detail': 'Floor rates with bands; special calamity rates.',
                               'tone': 'gold'},
                              {'id': 'special',
                               'articles': 'States',
                               'label': 'Special provisions',
                               'detail': 'NE and other notified special-state issues.',
                               'tone': 'orange'}]},
                   {'id': 'cb-gst-tip',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Mnemonic',
                    'body': 'GST vote: **C⅓ · S⅔ · need ¾** — Centre cannot steamroll alone.'}]},
{'title': 'National Commission for Scheduled Castes',
 'slug': 'cb-ncsc',
 'sort_order': 6,
 'summary': 'Art. 338 constitutional commission — Chair + VC + 3 members; civil-court powers; '
            'evolved via 65th and 89th Amendments.',
 'body': '## NCSC (Art. 338)\n'
         '\n'
         '### Constitutional status\n'
         '- Constitutional body under Art. 338 (unlike Women/Minorities/NHRC/NCPCR — statutory).\n'
         '\n'
         '### Evolution\n'
         '- Originally: Special Officer (Commissioner) for SCs & STs.\n'
         '- 1978/1987: non-statutory multi-member commissions via Resolution.\n'
         '- **65th Amendment (1990):** constitutional multi-member National Commission for SCs & '
         'STs.\n'
         '- **89th Amendment (2003):** bifurcated → NCSC (338) and NCST (338-A); separate NCSC '
         'from 2004.\n'
         '\n'
         '### Composition / appointment / tenure\n'
         '- Chairperson + Vice-Chairperson + **three** other members.\n'
         '- Appointed by President by warrant under hand and seal.\n'
         '- Conditions/tenure by President; Rules: **3 years**, max **two** terms.\n'
         '\n'
         '### Functions\n'
         '- Investigate/monitor SC constitutional & legal safeguards; inquire into complaints.\n'
         '- Advise on socio-economic development planning; evaluate progress.\n'
         '- Annual/other reports to President with recommendations.\n'
         '- Other functions as President may specify.\n'
         '- Till 2018 also discharged similar functions for Anglo-Indian Community (scope note / '
         '104th context).\n'
         '\n'
         '### Powers\n'
         '- Regulate own procedure; **civil-court powers** while investigating/inquiring (summons, '
         'discovery, affidavits, public records, etc.).\n'
         '- Union/states to consult Commission on major policy matters affecting SCs.\n'
         '\n'
         '### Reporting\n'
         '- Reports to President → Parliament with action memorandum (and reasons for '
         'non-acceptance).\n'
         '- State-related report forwarded to **Governor** → state legislature with memorandum.\n'
         '\n'
         '### Prelims traps\n'
         'Constitutional ≠ NHRC/NCW · 89th created split · civil-court powers ≠ criminal court.\n'
         '\n'
         '### Mains value-add\n'
         'From single Special Officer to specialised constitutional commissions — rights '
         'institutionalisation.\n',
 'articles': [('Art. 338', 'National Commission for Scheduled Castes.'),
              ('65th / 89th Amendments',
               'Constitutional multi-member commission; later bifurcation from STs.')],
 'visual_blocks': [{'id': 'cb-ncsc-timeline',
                    'type': 'timeline',
                    'title': 'From Special Officer to NCSC',
                    'events': [{'id': 'n1',
                                'year': 1950,
                                'label': 'Special Officer',
                                'detail': 'Original Art. 338 Commissioner for SCs & STs.'},
                               {'id': 'n2',
                                'year': 1978,
                                'label': 'Non-statutory body',
                                'detail': 'Multi-member Commission via Resolution.'},
                               {'id': 'n3',
                                'year': 1990,
                                'label': '65th Amendment',
                                'detail': 'Constitutional National Commission for SCs & STs.'},
                               {'id': 'n4',
                                'year': 2003,
                                'label': '89th Amendment',
                                'detail': 'Split: NCSC (338) + NCST (338-A).'},
                               {'id': 'n5',
                                'year': 2004,
                                'label': 'Separate NCSC',
                                'detail': 'Chair + VC + 3 members.'}]},
                   {'id': 'cb-ncsc-pillars',
                    'type': 'pillars',
                    'title': 'NCSC core jobs',
                    'items': [{'id': 'monitor',
                               'articles': 'Safeguards',
                               'label': 'Monitor & inquire',
                               'detail': 'Investigate safeguards; inquire into complaints.',
                               'tone': 'teal'},
                              {'id': 'plan',
                               'articles': 'Development',
                               'label': 'Advise planning',
                               'detail': 'Participate in socio-economic development planning.',
                               'tone': 'olive'},
                              {'id': 'report',
                               'articles': 'President',
                               'label': 'Report',
                               'detail': 'Annual/other reports with recommendations.',
                               'tone': 'gold'},
                              {'id': 'court',
                               'articles': 'Powers',
                               'label': 'Civil-court powers',
                               'detail': 'Summons, discovery, affidavits, public records.',
                               'tone': 'orange'}]},
                   {'id': 'cb-ncsc-trap',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Confused with statutory bodies?',
                    'body': 'NCSC is **constitutional**. National Commission for Women, '
                            'Minorities, NHRC, NCPCR are **statutory**.'}]},
{'title': 'National Commission for Scheduled Tribes',
 'slug': 'cb-ncst',
 'sort_order': 7,
 'summary': 'Art. 338-A separate ST commission (89th Amendment) — same structure as NCSC plus '
            'ST-specific 2005 functions.',
 'body': '## NCST (Art. 338-A)\n'
         '\n'
         '### Constitutional status\n'
         '- Constitutional body inserted by **89th Amendment (2003)**; functional from 2004.\n'
         '- Created because ST problems differ geographically/culturally from SCs; Ministry of '
         'Tribal Affairs (1999) needed a focused counterpart.\n'
         '\n'
         '### Composition / appointment / tenure\n'
         '- Same pattern as NCSC: Chair + VC + 3 members; President warrant; Rules — 3 years, max '
         '2 terms.\n'
         '\n'
         '### Functions\n'
         '- Mirror NCSC functions for STs (investigate, inquire, advise planning, report, '
         'recommend, other functions specified by President).\n'
         '\n'
         '### Other functions (President, 2005) — high yield\n'
         '- Ownership rights in **minor forest produce**; safeguard rights over minerals/water.\n'
         '- Viable livelihoods; relief & rehabilitation of displaced tribal groups.\n'
         '- Prevent land alienation; elicit cooperation for forest protection/afforestation.\n'
         '- Full implementation of **PESA 1996**; reduce/eliminate shifting cultivation.\n'
         '\n'
         '### Powers & reporting\n'
         '- Civil-court powers; regulate procedure.\n'
         '- Reports to President → Parliament; state matters via Governor → legislature (same '
         'pattern as NCSC).\n'
         '- Consult on major ST policy matters.\n'
         '\n'
         '### Prelims traps\n'
         'Art. 338-A ≠ 338 · 89th created NCST · PESA/MFP functions are distinctive.\n'
         '\n'
         '### Mains value-add\n'
         'Bifurcation = recognition that SC and ST safeguard architectures need specialised '
         'monitoring.\n',
 'articles': [('Art. 338-A', 'National Commission for Scheduled Tribes.'),
              ('89th Amendment',
               'Bifurcation of combined SC/ST commission; insertion of Art. 338-A.')],
 'visual_blocks': [{'id': 'cb-ncst-compare',
                    'type': 'comparison',
                    'title': 'NCSC vs NCST',
                    'columns': [{'id': 'ncsc',
                                 'heading': 'NCSC (Art. 338)',
                                 'points': ['SCs (and earlier Anglo-Indian scope note)',
                                            'Core investigate/advise/report functions',
                                            'Civil-court powers',
                                            'Report via President / Governor path']},
                                {'id': 'ncst',
                                 'heading': 'NCST (Art. 338-A)',
                                 'points': ['STs only (89th split)',
                                            'Same core functions + 2005 extras',
                                            'MFP, land, PESA, displacement focus',
                                            'Same reporting pattern']}]},
                   {'id': 'cb-ncst-pillars',
                    'type': 'pillars',
                    'title': '2005 ST-specific extras',
                    'items': [{'id': 'mfp',
                               'articles': 'Forests',
                               'label': 'MFP & resources',
                               'detail': 'Minor forest produce; minerals/water rights.',
                               'tone': 'teal'},
                              {'id': 'land',
                               'articles': 'Land',
                               'label': 'Alienation & R&R',
                               'detail': 'Prevent alienation; rehabilitate displaced groups.',
                               'tone': 'olive'},
                              {'id': 'pesa',
                               'articles': 'PESA',
                               'label': 'PESA 1996',
                               'detail': 'Ensure full implementation in scheduled areas.',
                               'tone': 'gold'},
                              {'id': 'livelihood',
                               'articles': 'Livelihoods',
                               'label': 'Livelihoods',
                               'detail': 'Viable strategies; reduce shifting cultivation.',
                               'tone': 'orange'}]},
                   {'id': 'cb-ncst-tip',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Mains hook',
                    'body': 'NCST’s 2005 mandate links constitutional safeguards to forest rights, '
                            'displacement, and PESA — use in tribal governance answers.'}]},
{'title': 'National Commission for Backward Classes',
 'slug': 'cb-ncbc',
 'sort_order': 8,
 'summary': 'Art. 338-B constitutional commission (102nd Amendment) — Mandal origin; state reports '
            'go to state government, not Governor.',
 'body': '## NCBC (Art. 338-B)\n'
         '\n'
         '### Constitutional status\n'
         '- Originally **statutory** (1993) after *Indra Sawhney* / Mandal (1992) direction for a '
         'permanent body on BC list inclusion/exclusion.\n'
         '- **102nd Amendment (2018)** inserted Art. 338-B — constitutional status at par with '
         'NCSC/NCST; functions enlarged.\n'
         '\n'
         '### Composition / appointment / tenure\n'
         '- Chair + VC + 3 members; President warrant; Rules — 3 years, max 2 terms.\n'
         '\n'
         '### Functions\n'
         '- Investigate/monitor SEBC constitutional & legal safeguards; inquire into complaints.\n'
         '- Advise on socio-economic development; evaluate progress.\n'
         '- Reports and recommendations to President; other functions as specified.\n'
         '\n'
         '### Powers\n'
         '- Civil-court powers; regulate procedure.\n'
         '- Centre and states to consult on major SEBC policy matters.\n'
         '- **105th Amendment** staple: restored states’ power to identify SEBCs after '
         '102nd-related controversy.\n'
         '\n'
         '### Reporting (trap)\n'
         '- Annual/other reports to President → Parliament with action memorandum.\n'
         '- State-related report forwarded to the **state government** (not the Governor) → '
         'legislature with memorandum.\n'
         '\n'
         '### Prelims traps\n'
         'Was statutory → now constitutional (102nd) · NCBC state path ≠ NCSC/NCST Governor path · '
         '105th on state SEBC lists.\n'
         '\n'
         '### Mains value-add\n'
         'Constitutionalisation of BC safeguards after Mandal — institutional continuity from '
         'statute to Art. 338-B.\n',
 'articles': [('Art. 338-B', 'National Commission for Backward Classes.'),
              ('102nd / 105th Amendments',
               'Constitutional status (2018); states’ SEBC identification power clarified/restored '
               '(2021).')],
 'visual_blocks': [{'id': 'cb-ncbc-timeline',
                    'type': 'timeline',
                    'title': 'NCBC journey',
                    'events': [{'id': 'b1',
                                'year': 1992,
                                'label': 'Indra Sawhney',
                                'detail': 'SC directs permanent body for BC lists.'},
                               {'id': 'b2',
                                'year': 1993,
                                'label': 'Statutory NCBC',
                                'detail': 'Set up by Act of Parliament.'},
                               {'id': 'b3',
                                'year': 2018,
                                'label': '102nd Amendment',
                                'detail': 'Art. 338-B — constitutional status.'},
                               {'id': 'b4',
                                'year': 2021,
                                'label': '105th Amendment',
                                'detail': 'States’ power to identify SEBCs restored/clarified.'}]},
                   {'id': 'cb-rights-trio',
                    'type': 'comparison',
                    'title': 'NCSC · NCST · NCBC',
                    'columns': [{'id': 'sc',
                                 'heading': 'NCSC',
                                 'points': ['Art. 338', 'SCs', 'State report → Governor']},
                                {'id': 'st',
                                 'heading': 'NCST',
                                 'points': ['Art. 338-A',
                                            'STs + 2005 extras',
                                            'State report → Governor']},
                                {'id': 'bc',
                                 'heading': 'NCBC',
                                 'points': ['Art. 338-B',
                                            'SEBCs (102nd)',
                                            'State report → state government']}]},
                   {'id': 'cb-ncbc-trap',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Prelims trap',
                    'body': 'For NCBC, President forwards state-related reports to the **state '
                            'government**, not the Governor (unlike NCSC/NCST).'}]},
{'title': 'Special Officer for Linguistic Minorities',
 'slug': 'cb-linguistic-minorities',
 'sort_order': 9,
 'summary': 'Art. 350-B (7th Amendment) — Commissioner for Linguistic Minorities; no '
            'constitutional tenure/removal scheme.',
 'body': '## Special Officer for Linguistic Minorities (Art. 350-B)\n'
         '\n'
         '### Constitutional status\n'
         '- Not in original Constitution; **7th Amendment (1956)** inserted Art. 350-B on SRC '
         '(1953–55) recommendation.\n'
         '- Office designated **Commissioner for Linguistic Minorities (CLM)** since 1957.\n'
         '\n'
         '### Appointment / qualifications / tenure / removal\n'
         '- Appointed by the President.\n'
         '- Constitution specifies **no** qualifications, tenure, salary, service conditions, or '
         'removal procedure — weakest formal independence package in Part VII.\n'
         '\n'
         '### Functions\n'
         '- Investigate all matters relating to constitutional safeguards for linguistic '
         'minorities.\n'
         '- Report to President at intervals directed; President places reports before each House '
         'and sends to concerned states.\n'
         '\n'
         '### Organisation\n'
         '- HQ New Delhi; regional offices at Belgaum, Chennai, Kolkata (Assistant '
         'Commissioners).\n'
         '- Assisted by Deputy/Assistant Commissioners; state/UT nodal officers.\n'
         '- Administratively under **Ministry of Minority Affairs**; reports routed through Union '
         'Minority Affairs Minister.\n'
         '\n'
         '### Vision / mission (book)\n'
         '- Strengthen implementation machinery for linguistic minority safeguards and equal '
         'opportunity.\n'
         '\n'
         '### Prelims traps\n'
         'Art. 350-B · 7th Amendment · no constitutional tenure/removal · Ministry of Minority '
         'Affairs link.\n'
         '\n'
         '### Mains value-add\n'
         'Safeguard without structural insulation — contrast with CEC/CAG security of tenure.\n',
 'articles': [('Art. 350-B',
               'Special Officer for linguistic minorities — appointment and duty to '
               'investigate/report.'),
              ('7th Amendment', 'Inserted Art. 350-B following States Reorganisation Commission.')],
 'visual_blocks': [{'id': 'cb-clm-tree',
                    'type': 'tree',
                    'title': 'CLM organisation',
                    'root': {'id': 'clm',
                             'label': 'Commissioner for Linguistic Minorities',
                             'detail': 'Art. 350-B · HQ New Delhi',
                             'children': [{'id': 'bel',
                                           'label': 'Belgaum',
                                           'detail': 'Regional office (Karnataka)'},
                                          {'id': 'che',
                                           'label': 'Chennai',
                                           'detail': 'Regional office (Tamil Nadu)'},
                                          {'id': 'kol',
                                           'label': 'Kolkata',
                                           'detail': 'Regional office (West Bengal)'},
                                          {'id': 'min',
                                           'label': 'Ministry of Minority Affairs',
                                           'detail': 'Administrative linkage / report channel'}]}},
                   {'id': 'cb-clm-callout',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Independence gap',
                    'body': 'Unlike CEC/CAG/UPSC, Art. 350-B is silent on qualifications, tenure, '
                            'salary, and removal — a frequent comparison point.'},
                   {'id': 'cb-clm-tip',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Memory trick',
                    'body': '350-B → Linguistic; 7th Amendment + SRC → Commissioner.'}]},
{'title': 'Comptroller and Auditor General of India',
 'slug': 'cb-cag',
 'sort_order': 10,
 'summary': 'Arts 148–151 — guardian of the public purse; 6 years or 65; remove like SC judge; '
            'reports via President/Governor.',
 'body': '## CAG (Arts 148–151)\n'
         '\n'
         '### Constitutional status\n'
         '- Independent constitutional office; head of Indian Audit and Accounts Department.\n'
         '- Ambedkar: **most important officer** under the Constitution.\n'
         '- One of the four bulwarks with Supreme Court, Election Commission, and UPSC.\n'
         '\n'
         '### Appointment & tenure\n'
         '- Appointed by President by warrant under hand and seal; oath before President.\n'
         '- Term: **6 years or age 65**, whichever earlier; resign to President.\n'
         '\n'
         '### Removal\n'
         '- Same grounds and manner as a Supreme Court judge (special majority address).\n'
         '- Does **not** hold office during pleasure of the President.\n'
         '\n'
         '### Independence safeguards\n'
         '- Security of tenure.\n'
         '- **Not eligible for further office** under Union or any state after demitting office.\n'
         '- Salary equal to SC judge (by Act); conditions not varied to disadvantage after '
         'appointment.\n'
         '- Admin expenses charged on **Consolidated Fund of India**.\n'
         '- Service conditions of IA&AD prescribed by President after consultation with CAG.\n'
         '\n'
         '### Duties & powers (CAG Act, 1971 + Constitution)\n'
         '- Audit expenditure from Consolidated Funds (Union, states, UTs with legislature).\n'
         '- Audit Contingency Fund and Public Account transactions.\n'
         '- Audit trading/manufacturing/P&L/balance sheets of departments.\n'
         '- Audit bodies substantially financed / receiving grants-loans; government companies (as '
         'per Companies Act role).\n'
         '- Propriety audit — wisdom, faithfulness, and economy of expenditure.\n'
         '- Compile/maintain accounts where required; submit audit reports.\n'
         '\n'
         '### Reporting / accountability\n'
         '- Union reports to President → Parliament; state reports to Governor → legislature.\n'
         '- Examined by **PAC** / COPU in Parliament.\n'
         '\n'
         '### Critiques / reforms (book staples)\n'
         '- Appleby critique; Comptroller vs Auditor practice (ex post audit emphasis).\n'
         '- 2nd ARC and related reform themes on audit effectiveness / response culture.\n'
         '\n'
         '### Prelims traps\n'
         'Further-office bar is unique high-yield · removal like SC judge · charged on CFI · PAC '
         'link.\n'
         '\n'
         '### Mains value-add\n'
         'CAG as democracy’s financial watchdog — independence design is among the strongest in '
         'Part VII.\n',
 'articles': [('Art. 148',
               'Comptroller and Auditor-General of India — appointment, oath, conditions.'),
              ('Art. 149', 'Duties and powers of the CAG.'),
              ('Art. 151', 'Audit reports — President/Governor to legislature.')],
 'visual_blocks': [{'id': 'cb-cag-pillars',
                    'type': 'pillars',
                    'title': 'CAG independence pack',
                    'items': [{'id': 'tenure',
                               'articles': 'Art. 148',
                               'label': 'Tenure security',
                               'detail': 'Remove only like SC judge.',
                               'tone': 'teal'},
                              {'id': 'bar',
                               'articles': 'Further office',
                               'label': 'Post-office bar',
                               'detail': 'No further Union/state office.',
                               'tone': 'olive'},
                              {'id': 'pay',
                               'articles': 'Salary',
                               'label': 'Pay & freeze',
                               'detail': 'SC-judge salary; no disadvantageous change.',
                               'tone': 'gold'},
                              {'id': 'cfi',
                               'articles': 'CFI',
                               'label': 'Charged expenditure',
                               'detail': 'Office expenses charged on CFI.',
                               'tone': 'orange'}]},
                   {'id': 'cb-cag-report-flow',
                    'type': 'flowchart',
                    'title': 'CAG report path',
                    'root': 'audit',
                    'steps': [{'id': 'audit',
                               'label': 'Audit',
                               'detail': 'Accounts of Union / state / notified bodies.',
                               'options': [{'label': 'Union report', 'next': 'union'},
                                           {'label': 'State report', 'next': 'state'}]},
                              {'id': 'union',
                               'label': 'President → Parliament',
                               'detail': 'Taken up by PAC / COPU.'},
                              {'id': 'state',
                               'label': 'Governor → legislature',
                               'detail': 'State PAC scrutiny.'}]},
                   {'id': 'cb-cag-tip',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Four bulwarks',
                    'body': 'Ambedkar’s democratic bulwarks: **Supreme Court · Election Commission '
                            '· UPSC · CAG**.'}]},
{'title': 'Attorney General of India',
 'slug': 'cb-attorney-general',
 'sort_order': 11,
 'summary': 'Art. 76 highest Union law officer — SC-judge qualifications; pleasure of President; '
            'audience in all courts; not a minister.',
 'body': '## Attorney General of India (Art. 76)\n'
         '\n'
         '### Constitutional status\n'
         '- Highest law officer of India; only AG office is constitutional among Union law '
         'officers (SG/ASG are not).\n'
         '\n'
         '### Appointment & qualifications\n'
         '- Appointed by the President.\n'
         '- Must be qualified to be a **Supreme Court judge** (citizen + HC judge 5 yrs / HC '
         'advocate 10 yrs / eminent jurist).\n'
         '\n'
         '### Tenure & removal\n'
         '- No fixed constitutional term; no prescribed removal procedure.\n'
         '- Holds office during the **pleasure of the President**; may resign to President.\n'
         '- Conventionally resigns when the government changes.\n'
         '\n'
         '### Remuneration\n'
         '- Not fixed by Constitution — as President determines.\n'
         '\n'
         '### Duties & functions\n'
         '- Advise GoI on legal matters referred by President; other legal duties assigned; '
         'constitutional/statutory functions.\n'
         '- Appear for GoI in SC; represent in Art. 143 references; appear in HCs when required.\n'
         '\n'
         '### Rights & limitations\n'
         '- Right of audience in **all courts** in India.\n'
         '- Right to speak/take part in Parliament / joint sitting / committees — **no vote**; '
         'enjoys MP privileges.\n'
         '- Limits: no brief against GoI; no conflicting briefs; no criminal defence without '
         'permission; no company directorship without permission; ministry references via Law '
         'Ministry channel.\n'
         '- **Not** a full-time counsel; **not** a government servant; **private practice '
         'allowed**.\n'
         '- **Not** a member of the Cabinet — there is a separate Law Minister.\n'
         '\n'
         '### Prelims traps\n'
         'AG ≠ Law Minister · SG/ASG not constitutional · pleasure tenure · private practice '
         'allowed · no vote in House.\n'
         '\n'
         '### Mains value-add\n'
         'Pleasure doctrine makes AG a confidence officer of the executive — contrast with CEC/CAG '
         'insulation.\n',
 'articles': [('Art. 76', 'Attorney-General for India.'),
              ('Art. 88', 'Rights of Ministers and Attorney-General as respects Houses.'),
              ('Art. 105',
               'Powers, privileges, etc., of the Houses and members (AG privileges link).')],
 'visual_blocks': [{'id': 'cb-ag-pillars',
                    'type': 'pillars',
                    'title': 'AG snapshot',
                    'items': [{'id': 'qual',
                               'articles': 'Art. 76',
                               'label': 'SC-judge eligible',
                               'detail': 'Citizen + HC 5 / advocate 10 / eminent jurist.',
                               'tone': 'teal'},
                              {'id': 'pleasure',
                               'articles': 'Tenure',
                               'label': 'Pleasure doctrine',
                               'detail': 'No fixed term; resigns with government by convention.',
                               'tone': 'olive'},
                              {'id': 'rights',
                               'articles': 'Art. 88',
                               'label': 'House rights',
                               'detail': 'Speak in Parliament; no vote; MP privileges.',
                               'tone': 'gold'},
                              {'id': 'practice',
                               'articles': 'Limits',
                               'label': 'Private practice OK',
                               'detail': 'Not full-time; conflict limits apply.',
                               'tone': 'orange'}]},
                   {'id': 'cb-ag-trap',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Prelims trap',
                    'body': 'Only the Attorney General is a **constitutional** law officer. '
                            'Solicitor General and Additional SGs are **not** mentioned in Art. '
                            '76.'},
                   {'id': 'cb-ag-tip',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Frequently confused',
                    'body': 'AG advises the government; Law Minister is the political executive '
                            'for legal policy — different roles.'}]},
{'title': 'Advocate General of the State',
 'slug': 'cb-advocate-general',
 'sort_order': 12,
 'summary': 'Art. 165 highest state law officer — HC-judge qualifications; pleasure of Governor; '
            'corresponds to the Attorney General.',
 'body': '## Advocate General of the State (Art. 165)\n'
         '\n'
         '### Constitutional status\n'
         '- Highest law officer in the state; corresponds to the Attorney General of India.\n'
         '\n'
         '### Appointment & qualifications\n'
         '- Appointed by the **Governor**.\n'
         '- Must be qualified to be a **High Court judge** (citizen + judicial office 10 yrs / HC '
         'advocate 10 yrs).\n'
         '\n'
         '### Tenure & removal\n'
         '- No fixed constitutional term; no prescribed removal procedure.\n'
         '- Holds office during the **pleasure of the Governor**; may resign to Governor.\n'
         '- Conventionally resigns when the state government changes.\n'
         '- Remuneration as Governor determines.\n'
         '\n'
         '### Duties & rights\n'
         '- Advise state government on legal matters referred by Governor; other assigned legal '
         'duties; constitutional/statutory functions.\n'
         '- Right to speak/take part in Houses of state legislature / committees — **no vote**.\n'
         '- Enjoys privileges and immunities of a member of the state legislature.\n'
         '\n'
         '### Prelims traps\n'
         'AG (Union) vs Advocate General (state) · SC-eligible vs HC-eligible · President vs '
         'Governor pleasure.\n'
         '\n'
         '### Mains value-add\n'
         'Mirror offices at two levels — use comparison table for crisp federal answers.\n',
 'articles': [('Art. 165', 'Advocate-General for the State.'),
              ('Art. 177', 'Rights of Advocate-General as respects Houses of State Legislature.')],
 'visual_blocks': [{'id': 'cb-ag-advg-compare',
                    'type': 'comparison',
                    'title': 'Attorney General vs Advocate General',
                    'columns': [{'id': 'ag',
                                 'heading': 'Attorney General',
                                 'points': ['Art. 76',
                                            'Appointed by President',
                                            'SC-judge qualifications',
                                            'Pleasure of President',
                                            'Speak in Parliament (no vote)',
                                            'Audience in all courts']},
                                {'id': 'advg',
                                 'heading': 'Advocate General',
                                 'points': ['Art. 165',
                                            'Appointed by Governor',
                                            'HC-judge qualifications',
                                            'Pleasure of Governor',
                                            'Speak in state legislature (no vote)',
                                            'State’s highest law officer']}]},
                   {'id': 'cb-advg-trap',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Prelims trap',
                    'body': 'Advocate General ≠ Attorney General. Qualification bar is **HC '
                            'judge**, not Supreme Court judge.'},
                   {'id': 'cb-advg-tip',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Exam in 5 Minutes',
                    'body': 'Pleasure officers: AG + Advocate General. Address officers: CEC + CAG '
                            '(+ SC/HC judges). PSC: SC-enquiry misbehaviour path.'}]},
{'title': 'Master Comparisons',
 'slug': 'cb-master-comparisons',
 'sort_order': 13,
 'summary': 'Appointment, removal, independence, and reporting matrices across all twelve '
            'constitutional bodies.',
 'body': '## Master comparison pack\n'
         '\n'
         'Use this cluster as the **last revision pass** before Prelims/Mains.\n'
         '\n'
         '### Master scan (all 12)\n'
         '| Body | Article(s) | Appoints | Tenure cue | Removes / ends | Reports to |\n'
         '|------|------------|----------|------------|----------------|------------|\n'
         '| ECI | 324 | President | 6y/65 (Act) | CEC like SC judge; EC on CEC rec. | Autonomous / '
         'Parliament law |\n'
         '| UPSC | 315–323 | President | 6y/65 | President (+ SC if misbehaviour) | President → '
         'Parliament |\n'
         '| SPSC | 315–323 | Governor | 6y/62 | **President only** | Governor → legislature |\n'
         '| FC | 280 | President | As ordered | Order period ends | President → Parliament |\n'
         '| GST Council | 279-A | President constitutes | Standing forum | — | Recommends to '
         'Centre & states |\n'
         '| NCSC | 338 | President | ~3y / 2 terms | As per Rules/President | President → '
         'Parliament (+ Governor path) |\n'
         '| NCST | 338-A | President | ~3y / 2 terms | As per Rules/President | Same as NCSC |\n'
         '| NCBC | 338-B | President | ~3y / 2 terms | As per Rules/President | President → '
         'Parliament (**state govt** path) |\n'
         '| CLM | 350-B | President | Not fixed in Constitution | Not specified | President → '
         'Parliament + states |\n'
         '| CAG | 148–151 | President | 6y/65 | Like SC judge | President/Governor → House |\n'
         '| AG | 76 | President | Pleasure | Pleasure | Advises Union executive |\n'
         '| Adv. Gen | 165 | Governor | Pleasure | Pleasure | Advises state executive |\n'
         '\n'
         '### Independence quick sort\n'
         '- **Strongest package:** CAG (further-office bar + address removal + CFI).\n'
         '- **Strong tenure:** CEC (address), UPSC/SPSC (SC misbehaviour path).\n'
         '- **Pleasure doctrine:** AG, Advocate General.\n'
         '- **Thin text:** CLM (Art. 350-B silent on tenure/removal).\n'
         '\n'
         '### Four bulwarks mnemonic\n'
         '**SC · ECI · UPSC · CAG** — Ambedkar’s democratic bulwarks.\n',
 'articles': [('Arts 76, 148–151, 165, 279-A, 280, 315–323, 324, 338–338-B, 350-B',
               'Master map of Part VII constitutional offices.')],
 'visual_blocks': [{'id': 'cb-master-eci-upsc-fc-cag',
                    'type': 'comparison',
                    'title': 'ECI vs UPSC vs FC vs CAG',
                    'columns': [{'id': 'eci',
                                 'heading': 'ECI',
                                 'points': ['Art. 324',
                                            'Elections',
                                            'CEC like SC judge',
                                            'Multi-member majority']},
                                {'id': 'upsc',
                                 'heading': 'UPSC',
                                 'points': ['Arts 315–323',
                                            'Recruitment advice',
                                            'SC enquiry on misbehaviour',
                                            'Advisory functions']},
                                {'id': 'fc',
                                 'heading': 'Finance Commission',
                                 'points': ['Art. 280',
                                            'Fiscal transfers',
                                            'Every 5th year',
                                            'Recommendations advisory']},
                                {'id': 'cag',
                                 'heading': 'CAG',
                                 'points': ['Arts 148–151',
                                            'Audit watchdog',
                                            'Like SC judge + no further office',
                                            'Reports via President/Governor']}]},
                   {'id': 'cb-appt-removal-tree',
                    'type': 'tree',
                    'title': 'Who appoints / who removes',
                    'root': {'id': 'root',
                             'label': 'Appointment & removal map',
                             'detail': 'Part VII high-yield',
                             'children': [{'id': 'pres-appt',
                                           'label': 'President appoints',
                                           'detail': 'CEC/ECs, UPSC, FC, NCSC/NCST/NCBC, CLM, CAG, '
                                                     'AG',
                                           'children': [{'id': 'pres-rem-address',
                                                         'label': 'Address removal',
                                                         'detail': 'CEC, CAG (like SC judge)'},
                                                        {'id': 'pres-rem-psc',
                                                         'label': 'PSC removal',
                                                         'detail': 'UPSC & SPSC (SPSC appointed by '
                                                                   'Governor)'},
                                                        {'id': 'pres-pleasure',
                                                         'label': 'Pleasure',
                                                         'detail': 'Attorney General'}]},
                                          {'id': 'gov-appt',
                                           'label': 'Governor appoints',
                                           'detail': 'SPSC, Advocate General',
                                           'children': [{'id': 'gov-cannot-spsc',
                                                         'label': 'Cannot remove SPSC',
                                                         'detail': 'Only President removes SPSC'},
                                                        {'id': 'gov-pleasure',
                                                         'label': 'Pleasure',
                                                         'detail': 'Advocate General'}]}]}},
                   {'id': 'cb-independence-compare',
                    'type': 'comparison',
                    'title': 'Independence safeguards',
                    'columns': [{'id': 'strong',
                                 'heading': 'Strong shields',
                                 'points': ['CAG: no further office + CFI + address',
                                            'CEC: address like SC judge',
                                            'UPSC/SPSC: CFI/state CF + removal path']},
                                {'id': 'medium',
                                 'heading': 'Conditional / Rules-based',
                                 'points': ['Other ECs: need CEC recommendation',
                                            'NCSC/NCST/NCBC: Rules tenure',
                                            'FC: fixed by presidential order']},
                                {'id': 'thin',
                                 'heading': 'Thin / pleasure',
                                 'points': ['AG & Advocate General: pleasure',
                                            'CLM: no tenure/removal in Constitution',
                                            'GST Council: political federal forum']}]},
                   {'id': 'cb-reporting-compare',
                    'type': 'comparison',
                    'title': 'Reporting authority',
                    'columns': [{'id': 'parl',
                                 'heading': 'Via President → Parliament',
                                 'points': ['UPSC', 'FC', 'NCSC/NCST/NCBC', 'CLM', 'CAG (Union)']},
                                {'id': 'state',
                                 'heading': 'Via Governor → legislature',
                                 'points': ['SPSC', 'NCSC/NCST (state matters)', 'CAG (state)']},
                                {'id': 'special',
                                 'heading': 'Special paths',
                                 'points': ['NCBC state matters → state government',
                                            'GST Council → Centre & states (recommendations)',
                                            'AG/Adv Gen → executive advice (not annual audit-style '
                                            'report)']}]},
                   {'id': 'cb-master-bulwarks',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Mnemonic — four bulwarks',
                    'body': '**SC + ECI + UPSC + CAG** = Ambedkar’s bulwarks of democratic '
                            'government.'}]},
{'title': 'Articles Cheat Sheet & Final Revision',
 'slug': 'cb-articles-and-final-sheet',
 'sort_order': 14,
 'summary': 'Complete article map, one-page final revision, Exam-in-5-Minutes box, PYQ themes, and '
            'confused pairs.',
 'body': '## Articles cheat sheet\n'
         '\n'
         '- **76 / 88** — Attorney General (+ House rights)\n'
         '- **148–151** — CAG (appointment, duties, reports)\n'
         '- **165 / 177** — Advocate General (+ House rights)\n'
         '- **279-A** — GST Council\n'
         '- **280 / 281** — Finance Commission\n'
         '- **315–323** — UPSC & SPSC\n'
         '- **324** — Election Commission\n'
         '- **338 / 338-A / 338-B** — NCSC / NCST / NCBC\n'
         '- **350-B** — Special Officer for Linguistic Minorities\n'
         '\n'
         '## One-page final revision\n'
         '\n'
         '1. **ECI** — Art. 324; trio since 1993; CEC like SC judge; ≠ SEC.\n'
         '2. **UPSC** — 6y/65; CFI; advice mostly non-binding; SC binds on misbehaviour removal.\n'
         '3. **SPSC** — Governor appoints / President removes; 6y/62.\n'
         '4. **FC** — every 5 years; advisory fiscal federalism; ≠ NITI.\n'
         '5. **GST Council** — C⅓ S⅔ need ¾; 101st Amendment.\n'
         '6. **NCSC/NCST/NCBC** — 338 / 338-A / 338-B; civil-court powers; NCBC state path trap.\n'
         '7. **CLM** — 350-B; thin independence text.\n'
         '8. **CAG** — no further office; PAC; propriety audit.\n'
         '9. **AG / Adv Gen** — pleasure; SC vs HC eligibility; only AG constitutional among Union '
         'law officers.\n'
         '\n'
         '## Exam in 5 Minutes\n'
         'Ask for each body: Article? Who appoints? Tenure? Who removes? Reports to? One trap?\n'
         '\n'
         '## Frequently confused\n'
         '- ECI vs SEC · UPSC vs SPSC age · FC vs GST Council · NCSC vs NHRC · AG vs Law '
         'Minister/SG · CAG Comptroller vs Auditor practice · NCBC Governor vs state government '
         'path.\n',
 'articles': [('Art. 324', 'Election Commission.'),
              ('Arts 315–323', 'Public Service Commissions.'),
              ('Art. 280 / 279-A', 'Finance Commission / GST Council.'),
              ('Arts 338, 338-A, 338-B, 350-B', 'Rights commissions and linguistic minorities.'),
              ('Arts 148–151, 76, 165', 'CAG and law officers.')],
 'visual_blocks': [{'id': 'cb-articles-tree',
                    'type': 'tree',
                    'title': 'Constitutional articles map',
                    'root': {'id': 'const',
                             'label': 'Constitutional Bodies',
                             'detail': 'Part VII revision map',
                             'children': [{'id': 'election-audit',
                                           'label': 'Elections & Audit',
                                           'detail': '324 · 148–151',
                                           'children': [{'id': 'a324',
                                                         'label': '324 ECI',
                                                         'slug': 'cb-election-commission'},
                                                        {'id': 'a148',
                                                         'label': '148–151 CAG',
                                                         'slug': 'cb-cag'}]},
                                          {'id': 'services',
                                           'label': 'Services',
                                           'detail': '315–323',
                                           'children': [{'id': 'aupsc',
                                                         'label': 'UPSC',
                                                         'slug': 'cb-upsc'},
                                                        {'id': 'aspsc',
                                                         'label': 'SPSC',
                                                         'slug': 'cb-spsc'}]},
                                          {'id': 'fiscal',
                                           'label': 'Fiscal federalism',
                                           'detail': '280 · 279-A',
                                           'children': [{'id': 'a280',
                                                         'label': '280 FC',
                                                         'slug': 'cb-finance-commission'},
                                                        {'id': 'a279',
                                                         'label': '279-A GST',
                                                         'slug': 'cb-gst-council'}]},
                                          {'id': 'rights',
                                           'label': 'Rights commissions',
                                           'detail': '338 · 338-A · 338-B · 350-B',
                                           'children': [{'id': 'a338',
                                                         'label': '338 NCSC',
                                                         'slug': 'cb-ncsc'},
                                                        {'id': 'a338a',
                                                         'label': '338-A NCST',
                                                         'slug': 'cb-ncst'},
                                                        {'id': 'a338b',
                                                         'label': '338-B NCBC',
                                                         'slug': 'cb-ncbc'},
                                                        {'id': 'a350b',
                                                         'label': '350-B CLM',
                                                         'slug': 'cb-linguistic-minorities'}]},
                                          {'id': 'law',
                                           'label': 'Law officers',
                                           'detail': '76 · 165',
                                           'children': [{'id': 'a76',
                                                         'label': '76 AG',
                                                         'slug': 'cb-attorney-general'},
                                                        {'id': 'a165',
                                                         'label': '165 Advocate General',
                                                         'slug': 'cb-advocate-general'}]}]}},
                   {'id': 'cb-pyq-heatmap',
                    'type': 'pyq_heatmap',
                    'title': 'PYQ focus map',
                    'items': [{'concept_slug': 'cb-election-commission',
                               'label': 'ECI removal / SEC'},
                              {'concept_slug': 'cb-upsc', 'label': 'UPSC advice / removal'},
                              {'concept_slug': 'cb-spsc', 'label': 'SPSC President removal'},
                              {'concept_slug': 'cb-finance-commission', 'label': 'FC advisory'},
                              {'concept_slug': 'cb-gst-council', 'label': 'GST voting weights'},
                              {'concept_slug': 'cb-ncsc', 'label': 'NCSC evolution'},
                              {'concept_slug': 'cb-ncbc', 'label': '102nd / 105th'},
                              {'concept_slug': 'cb-cag', 'label': 'CAG independence'},
                              {'concept_slug': 'cb-attorney-general', 'label': 'AG pleasure / SG'},
                              {'concept_slug': 'cb-master-comparisons', 'label': 'Comparisons'}]},
                   {'id': 'cb-exam-5min',
                    'type': 'callout',
                    'tone': 'tip',
                    'title': 'Exam in 5 Minutes',
                    'body': 'ECI 324 · UPSC/SPSC 315–323 (65/62; President removes SPSC) · FC 280 '
                            'advisory · GST 279-A (C⅓ S⅔ ≥¾) · 338/338-A/338-B · 350-B · CAG 148 '
                            'no further office · AG 76 pleasure · Adv Gen 165 pleasure.'},
                   {'id': 'cb-confused',
                    'type': 'callout',
                    'tone': 'trap',
                    'title': 'Frequently confused',
                    'body': 'ECI ≠ SEC · FC ≠ GST Council · NCSC ≠ NHRC · AG ≠ Law Minister · SG '
                            'not constitutional · NCBC state report ≠ Governor path · CEC address '
                            '≠ other EC (needs CEC recommendation).'}]},
]

EDGES = [
    ('constitutional-bodies', 'parent', 'cb-election-commission'),
    ('constitutional-bodies', 'parent', 'cb-upsc'),
    ('constitutional-bodies', 'parent', 'cb-spsc'),
    ('constitutional-bodies', 'parent', 'cb-finance-commission'),
    ('constitutional-bodies', 'parent', 'cb-gst-council'),
    ('constitutional-bodies', 'parent', 'cb-ncsc'),
    ('constitutional-bodies', 'parent', 'cb-ncst'),
    ('constitutional-bodies', 'parent', 'cb-ncbc'),
    ('constitutional-bodies', 'parent', 'cb-linguistic-minorities'),
    ('constitutional-bodies', 'parent', 'cb-cag'),
    ('constitutional-bodies', 'parent', 'cb-attorney-general'),
    ('constitutional-bodies', 'parent', 'cb-advocate-general'),
    ('constitutional-bodies', 'parent', 'cb-master-comparisons'),
    ('constitutional-bodies', 'parent', 'cb-articles-and-final-sheet'),
    ('cb-upsc', 'related', 'cb-spsc'),
    ('cb-spsc', 'related', 'cb-upsc'),
    ('cb-ncsc', 'related', 'cb-ncst'),
    ('cb-ncst', 'related', 'cb-ncbc'),
    ('cb-ncsc', 'related', 'cb-ncbc'),
    ('cb-attorney-general', 'related', 'cb-advocate-general'),
    ('cb-advocate-general', 'related', 'cb-attorney-general'),
    ('cb-finance-commission', 'related', 'cb-gst-council'),
    ('cb-gst-council', 'related', 'cb-finance-commission'),
    ('cb-election-commission', 'related', 'cb-cag'),
    ('cb-cag', 'related', 'cb-election-commission'),
    ('cb-election-commission', 'related', 'cb-upsc'),
    ('cb-master-comparisons', 'related', 'cb-articles-and-final-sheet'),
    ('cb-articles-and-final-sheet', 'related', 'cb-master-comparisons'),
    ('constitutional-bodies', 'related', 'sf-independent-bodies'),
]

SAMPLE_PYQS = [
    (2017, 'Consider the following statements about the Election Commission of India and State Election Commissions.', 'ECI (Art. 324) does not conduct panchayat/municipality elections; those are under State Election Commissions.', ['cb-election-commission', 'constitutional-bodies']),
    (2014, 'Which of the following are the functions of the UPSC?', 'UPSC conducts exams and advises on personnel matters; its advice is generally not binding on the government.', ['cb-upsc']),
    (2013, 'Consider statements on removal of SPSC members.', 'Though appointed by the Governor, SPSC members can be removed only by the President.', ['cb-spsc', 'cb-upsc']),
    (2015, 'With reference to the Finance Commission of India, consider its nature of recommendations.', 'Finance Commission recommendations are advisory and not binding on the government.', ['cb-finance-commission']),
    (2019, "Consider the GST Council's decision-making process.", 'Decisions need at least three-fourths of weighted votes; Centre has one-third weight and states together two-thirds.', ['cb-gst-council']),
    (2018, 'Which amendment bifurcated the National Commission for SCs and STs?', 'The 89th Constitutional Amendment created separate NCSC (Art. 338) and NCST (Art. 338-A).', ['cb-ncsc', 'cb-ncst']),
    (2021, 'With reference to the National Commission for Backward Classes, consider constitutional status.', "102nd Amendment conferred constitutional status via Art. 338-B; 105th clarified/restored states' SEBC identification role.", ['cb-ncbc']),
    (2012, 'Which of the following is/are true of the CAG of India?', 'CAG is appointed by the President, removed like an SC judge, and is ineligible for further Union/state office after demitting office.', ['cb-cag']),
    (2016, 'Consider the following statements about the Attorney General of India.', 'AG holds office during the pleasure of the President, may undertake private practice with limits, and is not a member of the Cabinet.', ['cb-attorney-general']),
    (2020, 'Advocate General of a state must be qualified to be appointed as:', 'A judge of a High Court (Art. 165).', ['cb-advocate-general', 'cb-attorney-general']),
]

LANDMARK_CASES = [
    {
        'title': 'Indra Sawhney v. Union of India',
        'slug': 'indra-sawhney',
        'parties': 'Indra Sawhney v. Union of India',
        'year': 1992,
        "court": CaseLaw.Court.SC,
        'summary': 'Mandal case — directed a permanent body for complaints on BC list inclusion/exclusion.',
        'holding': 'Central government should constitute a permanent statutory body to examine complaints of under-inclusion, over-inclusion or non-inclusion in the list of backward classes — origin of statutory NCBC.',
        "concept_slugs": ['cb-ncbc', 'constitutional-bodies'],
    },
    {
        'title': 'Anoop Baranwal v. Union of India',
        'slug': 'anoop-baranwal',
        'parties': 'Anoop Baranwal v. Union of India',
        'year': 2023,
        "court": CaseLaw.Court.SC,
        'summary': 'Election Commission appointments — independence concerns; led into the 2023 legislative response.',
        'holding': 'Supreme Court laid down a selection-committee framework for CEC/EC appointments pending a law by Parliament; Parliament later enacted the CEC and Other Election Commissioners Act, 2023.',
        "concept_slugs": ['cb-election-commission', 'constitutional-bodies'],
    },
]

AMENDMENTS = [
    {
        'number': 7,
        'year': 1956,
        'title': 'Seventh Amendment',
        'summary': 'Inserted Art. 350-B providing for a Special Officer for linguistic minorities after the SRC recommendation.',
        'effect': 'Constitutional basis for Commissioner for Linguistic Minorities.',
        'concept_slugs': ['cb-linguistic-minorities', 'constitutional-bodies'],
    },
    {
        'number': 61,
        'year': 1988,
        'title': 'Sixty-first Amendment',
        'summary': 'Lowered voting age from 21 to 18, increasing Election Commission workload and prompting multi-member expansion.',
        'effect': 'Contextual trigger for 1989 addition of Election Commissioners.',
        'concept_slugs': ['cb-election-commission'],
    },
    {
        'number': 65,
        'year': 1990,
        'title': 'Sixty-fifth Amendment',
        'summary': 'Created a constitutional multi-member National Commission for SCs and STs in place of the Special Officer.',
        'effect': 'Constitutionalised the combined SC/ST commission under Art. 338.',
        'concept_slugs': ['cb-ncsc', 'cb-ncst'],
    },
    {
        'number': 89,
        'year': 2003,
        'title': 'Eighty-ninth Amendment',
        'summary': 'Bifurcated the combined commission into NCSC (Art. 338) and NCST (Art. 338-A).',
        'effect': 'Separate constitutional commissions for SCs and STs from 2004.',
        'concept_slugs': ['cb-ncsc', 'cb-ncst', 'constitutional-bodies'],
    },
    {
        'number': 101,
        'year': 2016,
        'title': 'One Hundred and First Amendment',
        'summary': 'Constitutional gateway for GST; inserted Art. 279-A for the GST Council.',
        'effect': 'Created the GST Council as a constitutional federal body.',
        'concept_slugs': ['cb-gst-council', 'constitutional-bodies'],
    },
    {
        'number': 102,
        'year': 2018,
        'title': 'One Hundred and Second Amendment',
        'summary': 'Conferred constitutional status on the National Commission for Backward Classes via Art. 338-B.',
        'effect': 'NCBC ceased to be merely statutory; functions enlarged.',
        'concept_slugs': ['cb-ncbc', 'constitutional-bodies'],
    },
    {
        'number': 104,
        'year': 2019,
        'title': 'One Hundred and Fourth Amendment',
        'summary': "Extended SC/ST reservation in Lok Sabha/Assemblies; discontinued Anglo-Indian nominated representation — relevant to NCSC's earlier Anglo-Indian functional scope note.",
        'effect': 'Context for changes around Anglo-Indian related functions earlier linked with NCSC.',
        'concept_slugs': ['cb-ncsc'],
    },
    {
        'number': 105,
        'year': 2021,
        'title': 'One Hundred and Fifth Amendment',
        'summary': "Clarified/restored states' power to identify Socially and Educationally Backward Classes after 102nd-related issues.",
        'effect': 'State SEBC lists competence reaffirmed alongside constitutional NCBC.',
        'concept_slugs': ['cb-ncbc', 'constitutional-bodies'],
    },
]

class Command(BaseCommand):
    help = "Seed Constitutional Bodies chapter (Laxmikanth Ch.43-54) under Part VII."

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
                "title": "Constitutional Bodies",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 43-54 (pp. 599-643)",
                "summary": (
                    "Visual revision of Part VII — twelve constitutional bodies with "
                    "comparison matrices, article maps, and exam traps."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="constitutional-bodies"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Constitutional Bodies",
                "summary": (
                    "Twelve Constitution-born offices — watchdogs and advisors — "
                    "revised for Prelims traps and Mains comparisons."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **watchdogs & advisors** mental model, scan the "
                    "**twelve pillars**, then drill each body. Finish with "
                    "**Master Comparisons** and **Articles & Final Sheet**. "
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
            ref="Laxmikanth Ch. 43-54",
            excerpt=(
                "Constitutional Bodies — ECI, UPSC, SPSC, Finance Commission, GST Council, "
                "NCSC, NCST, NCBC, Linguistic Minorities, CAG, AG, Advocate General."
            ),
            sort_order=0,
        )

        cb_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=cb_slugs, source__subject=subject
        ).filter(
            target__slug__in=cb_slugs | {"sf-independent-bodies"}
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
                    self.style.WARNING(f"Skip edge {src} -> {tgt} (missing concept)")
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
                f"Constitutional Bodies chapter seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(AMENDMENTS)} amendments, "
                f"{len(SAMPLE_PYQS)} PYQs linked."
            )
        )
