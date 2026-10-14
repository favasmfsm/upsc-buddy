"""Seed Laxmikanth Part VIII — Non-Constitutional Bodies (visual revision chapter)."""

from django.core.management.base import BaseCommand

from concepts.models import CaseLaw, Concept, ConceptArticle, ConceptEdge
from questions.models import PYQ
from subjects.models import Chapter, Subject

HUB_SLUG = "non-constitutional-bodies"
CHAPTER_SLUG = "non-constitutional-bodies"

BODY_PILLARS = [{'articles': 'Exec · 2015',
  'detail': 'Cabinet resolution think-tank — neither constitutional nor statutory.',
  'id': 'niti',
  'label': 'NITI Aayog',
  'slug': 'ncb-niti-aayog',
  'tone': 'teal'},
 {'articles': 'PHRA 1993',
  'detail': 'National Human Rights Commission — recommendatory watchdog.',
  'id': 'nhrc',
  'label': 'NHRC',
  'slug': 'ncb-nhrc',
  'tone': 'olive'},
 {'articles': 'PHRA 1993',
  'detail': 'State Human Rights Commission — List II/III; removed by President.',
  'id': 'shrc',
  'label': 'SHRC',
  'slug': 'ncb-shrc',
  'tone': 'gold'},
 {'articles': 'NCW Act 1990',
  'detail': 'National Commission for Women — MWCD; constituted 1992.',
  'id': 'ncw',
  'label': 'NCW',
  'slug': 'ncb-ncw',
  'tone': 'orange'},
 {'articles': 'CPCR 2005',
  'detail': 'Child rights — RTE, POCSO, JJ Act roles.',
  'id': 'ncpcr',
  'label': 'NCPCR',
  'slug': 'ncb-ncpcr',
  'tone': 'terracotta'},
 {'articles': 'NCM Act 1992',
  'detail': 'National Commission for Minorities — Minority Affairs.',
  'id': 'ncm',
  'label': 'NCM',
  'slug': 'ncb-ncm',
  'tone': 'maroon'},
 {'articles': 'RTI 2005',
  'detail': 'Central Information Commission — RTI appeals & penalties.',
  'id': 'cic',
  'label': 'CIC',
  'slug': 'ncb-cic',
  'tone': 'teal'},
 {'articles': 'RTI 2005',
  'detail': 'State Information Commission — Governor appointment.',
  'id': 'sic',
  'label': 'SIC',
  'slug': 'ncb-sic',
  'tone': 'olive'},
 {'articles': 'CVC Act 2003',
  'detail': 'Central Vigilance Commission — Santhanam → statutory 2003.',
  'id': 'cvc',
  'label': 'CVC',
  'slug': 'ncb-cvc',
  'tone': 'gold'},
 {'articles': 'DSPE 1946',
  'detail': 'Investigating agency — State consent; DoPT.',
  'id': 'cbi',
  'label': 'CBI',
  'slug': 'ncb-cbi',
  'tone': 'orange'},
 {'articles': 'Act 2013',
  'detail': 'Anti-corruption ombudsman — First ARC lineage.',
  'id': 'lokpal',
  'label': 'Lokpal & Lokayuktas',
  'slug': 'ncb-lokpal',
  'tone': 'terracotta'},
 {'articles': 'NIA Act 2008',
  'detail': 'Counter-terror agency — concurrent & extraterritorial reach.',
  'id': 'nia',
  'label': 'NIA',
  'slug': 'ncb-nia',
  'tone': 'maroon'},
 {'articles': 'DM Act 2005',
  'detail': 'Disaster apex — PM Chair; SDMA/DDMA/NDRF stack.',
  'id': 'ndma',
  'label': 'NDMA',
  'slug': 'ncb-ndma',
  'tone': 'teal'},
 {'articles': 'Advocates 1961',
  'detail': 'Legal profession regulator — standards & education.',
  'id': 'bci',
  'label': 'Bar Council of India',
  'slug': 'ncb-bci',
  'tone': 'olive'},
 {'articles': 'Executive',
  'detail': 'Non-statutory advisory — MoLJ order; reform reports.',
  'id': 'lci',
  'label': 'Law Commission',
  'slug': 'ncb-law-commission',
  'tone': 'gold'},
 {'articles': 'Delimitation Acts',
  'detail': 'Seat & boundary orders — final; freeze till post-2026 census.',
  'id': 'delim',
  'label': 'Delimitation Commission',
  'slug': 'ncb-delimitation',
  'tone': 'orange'},
 {'articles': 'NEC Act 1971',
  'detail': 'Regional planning body — DONER; HM Chair since 2018.',
  'id': 'nec',
  'label': 'North Eastern Council',
  'slug': 'ncb-nec',
  'tone': 'terracotta'}]

HUB_VISUAL_BLOCKS = [
    {
        "id": "ncb-identity-model",
        "type": "mental_model",
        "title": "Mental model",
        "metaphor": "Satellite network",
        "topic_label": "Non-Constitutional Bodies",
        "subject_label": "Indian polity",
        "relation_label": "Helps you separate",
        "protects_from": [
            "Mixing constitutional vs statutory vs executive",
            "Confusing NHRC with NCW/NCM",
            "CBI vs NIA vs Lokpal mandates",
            "Forgetting parent ministries",
        ],
        "insight": (
            "These bodies are created by Act or Cabinet — not by a Constitution Part. "
            "Classify first (type → ministry → mandate), then drill."
        ),
    },
    {
        "id": "ncb-seventeen-pillars",
        "type": "pillars",
        "title": "Seventeen bodies (Ch.56–72)",
        "items": BODY_PILLARS,
    },
    {
        "id": "ncb-hub-callout",
        "type": "callout",
        "tone": "tip",
        "title": "Revision path",
        "body": (
            "**Taxonomy** → bodies by family (Rights → Transparency → Accountability → "
            "Advisory/Legal/Regional) → **Master tables** → **Exam in 5 Minutes**. "
            "Highest traps: NITI type, SHRC removal, RTI 2019 tenure, CBI consent, "
            "Delimitation finality."
        ),
    },
]

CLUSTERS = [{'articles': [['Cabinet Resolution, 1 Jan 2015',
                'Created NITI Aayog as successor to the Planning Commission.'],
               ['Ministry of Planning', 'Parent ministry / administrative linkage.']],
  'body': '## Type of body\n'
          '\n'
          '**Executive / extra-constitutional** and **non-statutory** (Cabinet resolution). '
          'Premier policy think-tank.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Union Cabinet executive resolution (Cab. Sec. No. 511/2/1/2015-Cab.)\n'
          '- **Established:** 1 January 2015 (Planning Commission scrapped August 2014 '
          'announcement)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Planning**\n'
          '\n'
          '## Composition\n'
          '\n'
          '- **Chair:** Prime Minister\n'
          '- **Governing Council:** CMs of all States + CMs of UTs with legislatures + LGs of '
          'other UTs\n'
          '- **Regional Councils:** for specified periods / regions\n'
          '- **Vice-Chair** (Cabinet rank), full-time members (MoS rank), ≤2 part-time, ≤4 '
          'ex-officio Union Ministers, **CEO** (Secretary rank)\n'
          '- Special invitees as needed\n'
          '\n'
          '## Appointment\n'
          '\n'
          'PM appoints Vice-Chair, full-time members, CEO, and nominees as prescribed.\n'
          '\n'
          '## Qualifications\n'
          '\n'
          'Not fixed by statute — expertise-driven (policy, economics, development).\n'
          '\n'
          '## Tenure\n'
          '\n'
          'As prescribed; CEO on fixed tenure; Regional Councils for specified tenure.\n'
          '\n'
          '## Removal\n'
          '\n'
          'At pleasure / as per appointment terms (no statutory SC-inquiry removal process like '
          'NHRC/CIC).\n'
          '\n'
          '## Powers\n'
          '\n'
          '- Directional & policy inputs to Centre and States\n'
          '- No plan-approval / fund-disbursal power of old Planning Commission\n'
          '\n'
          '## Functions\n'
          '\n'
          '- Strategic & long-term policy design\n'
          '- Cooperative & competitive federalism\n'
          '- Monitoring, evaluation, innovation / Knowledge Hub\n'
          '- Team India Hub + Knowledge & Innovation Hub\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Centre + States/UTs — advice and coordination; bottom-up partnership model.\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Not a constitutional/statutory independent commission — Cabinet creation; advisory '
          'character.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Reports / advice to Government; Governing Council under PM; annual outputs & indices '
          'publicly released.\n'
          '\n'
          '## Important committees\n'
          '\n'
          'First ARC criticised Planning Commission as ‘Super Cabinet’. NDC (1952) powers '
          'reportedly to shift to NITI Governing Council (not fully done).\n'
          '\n'
          '## Important judgments\n'
          '\n'
          'N/A as primary case-law body — debate is institutional/federal, not justiciable '
          'status.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          '- DMEO (2015) attached office for monitoring & evaluation\n'
          '- NILERD under NITI\n'
          '- Aspirational Districts / competitive indices ecosystem\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'SDG India Index, School Education Quality Index, Health Index, Innovation Index; '
          'Aspirational Districts/Blocks; cooperative vs competitive federalism debates.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'NITI vs Planning Commission; cooperative federalism; is NITI constitutional/statutory?; '
          'composition of Governing Council.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: calling NITI a **statutory** or **constitutional** body — it is **neither**.\n'
          '- Trap: assuming it approves State plans/funds like old PC.\n'
          '- Trap: confusing NDC with NITI Governing Council.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Use NITI to argue **cooperative federalism** (Governing Council, bottom-up) vs '
          '**competitive federalism** (indices, rankings) — and limits of an advisory think-tank '
          'without hard fiscal levers.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Exec resolution 2015 · Mo Planning\n'
          '- PM Chair · VC Cabinet rank · CEO Secretary rank\n'
          '- Neither constitutional nor statutory\n'
          '- Think-tank + federalism platform, not Super Cabinet fund allocator\n',
  'slug': 'ncb-niti-aayog',
  'sort_order': 1,
  'summary': 'Executive policy think-tank (2015) — neither constitutional nor statutory; Ministry '
             'of Planning.',
  'title': 'NITI Aayog',
  'visual_blocks': [{'columns': [{'heading': 'What it is',
                                  'id': 'is',
                                  'points': ['Executive resolution body',
                                             'Policy think-tank',
                                             'Governing Council of CMs',
                                             'Cooperative + competitive federalism']},
                                 {'heading': 'What it is not',
                                  'id': 'isnt',
                                  'points': ['Not constitutional',
                                             'Not statutory',
                                             'Not a fund-approving Super Cabinet',
                                             'Not the Election/Finance Commission']}],
                     'id': 'niti-identity',
                     'title': 'NITI identity card',
                     'type': 'comparison'},
                    {'events': [{'detail': 'Executive body — plan allocation era.',
                                 'id': 'e1',
                                 'label': 'Planning Commission',
                                 'year': 1950},
                                {'detail': 'National Development Council for plan endorsement.',
                                 'id': 'e2',
                                 'label': 'NDC',
                                 'year': 1952},
                                {'detail': '1 Jan 2015 — think-tank + federal partnership.',
                                 'id': 'e3',
                                 'label': 'NITI Aayog',
                                 'year': 2015}],
                     'id': 'niti-timeline',
                     'title': 'From Planning Commission to NITI',
                     'type': 'timeline'},
                    {'body': 'NITI is **extra-constitutional and non-statutory**. Same creation '
                             'method as the old Planning Commission — Cabinet resolution.',
                     'id': 'niti-trap',
                     'title': 'Prelims trap',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [['Protection of Human Rights Act, 1993',
                'Establishes NHRC and framework for SHRCs.'],
               ['PHRA Amendment, 2019',
                'Chair eligibility, composition, tenure 5→3 years, more ex-officio members.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory** (not constitutional). National Human Rights Institution (Paris Principles '
          'aspiration).\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Protection of Human Rights Act, 1993 (amended 2019)\n'
          '- **Established:** 1993\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Home Affairs**\n'
          '\n'
          '## Composition\n'
          '\n'
          '- **Chair** + **5** members\n'
          '- **7 ex-officio:** Chairs of NCM, NCSC, NCST, NCW, NCBC, NCPCR + Chief Commissioner '
          'for Persons with Disabilities\n'
          '\n'
          '## Appointment\n'
          '\n'
          '**President** on recommendation of 6-member committee: PM (head), LS Speaker, RS Deputy '
          'Chairman, LoPs in both Houses, Union Home Minister. Sitting SC judge / HC CJ only after '
          'CJI consultation.\n'
          '\n'
          '## Qualifications\n'
          '\n'
          'Chair: retired CJI **or** SC judge (post-2019). Members: serving/retired SC judge; '
          'serving/retired HC CJ; 3 persons (≥1 woman) with HR knowledge/experience.\n'
          '\n'
          '## Tenure\n'
          '\n'
          '**3 years** or age **70**, whichever earlier; re-appointment allowed; **no further** '
          'Central/State employment after tenure.\n'
          '\n'
          '## Removal\n'
          '\n'
          '**President** — insolvency, paid employment, infirmity, unsound mind, conviction; '
          '**misbehaviour/incapacity** only after **Supreme Court inquiry**.\n'
          '\n'
          '## Powers\n'
          '\n'
          '- Inquire (suo motu / petition / court order)\n'
          '- Civil court powers while inquiring\n'
          '- Intervene in court proceedings; visit jails\n'
          '- Recommend compensation / prosecution; approach SC/HC\n'
          '- **Recommendatory** — not binding adjudication\n'
          '\n'
          '## Functions\n'
          '\n'
          'Watchdog of rights to life, liberty, equality, dignity (Constitution + international '
          'covenants enforceable in India); review safeguards; study treaties; promote HR '
          'literacy.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'HR violations by public servants; **≤1 year** limitation typically; **limited** '
          'armed-forces inquiry pathway; cannot inquire if already before another statutory '
          'commission in same matter (coordination rules).\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Fixed tenure, SC-inquiry removal, salary not varied to disadvantage, post-tenure '
          'employment bar.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Annual / special reports to Central Government → laid before Parliament.\n'
          '\n'
          '## Important committees\n'
          '\n'
          'Paris Principles on NHRIs; SC concerns on manpower (2017).\n'
          '\n'
          '## Important judgments\n'
          '\n'
          'Recommendatory nature often tested in PILs; focus on independence & compliance '
          'culture.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          '**PHRA Amendment 2019:** Chair eligibility widened; members 2→3 (≥1 woman); tenure 5→3; '
          'added NCBC, NCPCR, CCPD as ex-officio.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'NHRI accreditation / Paris Principles debates; custodial violence; civil society '
          'appointments controversy.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Composition & appointment committee; recommendatory powers; armed forces limitation; '
          '2019 amendment changes.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: NHRC is **constitutional** — False.\n'
          '- Trap: tenure still **5 years** — now **3**.\n'
          '- Trap: orders are **binding** like a court — they are **recommendatory**.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Link Paris Principles, recommendatory design, and federal HR architecture (NHRC–SHRC) '
          'when writing rights & governance answers.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Statutory 1993 · MHA\n'
          '- President + 6-member panel\n'
          '- 3 yrs / 70 · SC inquiry for misbehaviour\n'
          '- Recommendatory · 2019 amd key\n',
  'slug': 'ncb-nhrc',
  'sort_order': 2,
  'summary': 'Statutory NHRI under PHRA 1993 (amd. 2019) — recommendatory human-rights watchdog; '
             'MHA.',
  'title': 'National Human Rights Commission',
  'visual_blocks': [{'id': 'nhrc-appoint',
                     'root': 'need',
                     'steps': [{'id': 'need',
                                'label': 'Vacancy in NHRC Chair/Member?',
                                'options': [{'label': 'Yes — selection', 'next': 'panel'}]},
                               {'detail': 'PM, LS Speaker, RS Dy Chair, LoPs both Houses, Home '
                                          'Minister',
                                'id': 'panel',
                                'label': '6-member committee (PM head)',
                                'options': [{'label': 'Recommend → President appoints',
                                             'next': 'pres'}]},
                               {'detail': 'Sitting SC/HC CJ needs prior CJI consultation',
                                'id': 'pres',
                                'label': 'President appoints'}],
                     'title': 'NHRC appointment path',
                     'type': 'flowchart'},
                    {'body': 'Tenure **5→3 years**; Chair can be retired **SC judge** (not only '
                             'CJI); more ex-officio rights chairs.',
                     'id': 'nhrc-trap',
                     'title': '2019 memory',
                     'tone': 'trap',
                     'type': 'callout'},
                    {'body': 'Statutory · President+panel · recommendatory · MHA · compare with '
                             'SHRC removal (also President).',
                     'id': 'nhrc-tip',
                     'title': 'Exam in 5 minutes',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [['Protection of Human Rights Act, 1993',
                'Enables State Governments to constitute SHRCs.'],
               ['PHRA Amendment, 2019', 'HC Judge eligible as Chair; tenure aligned to 3 years.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory** (optional — constituted by State notification).\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Protection of Human Rights Act, 1993\n'
          '- **Established:** Framework 1993 (State-wise constitution thereafter)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          'State Home Department (functional); **removal is Central (President)**\n'
          '\n'
          '## Composition\n'
          '\n'
          '**Chair + 2 members**\n'
          '\n'
          '## Appointment\n'
          '\n'
          '**Governor** on committee: CM, Assembly Speaker, State Home Minister, LoP (+ Council '
          'Chair & LoP if bicameral). Sitting HC/District Judge after consultation with HC CJ.\n'
          '\n'
          '## Qualifications\n'
          '\n'
          'Chair: retired HC CJ **or** HC Judge (post-2019). Members: HR experience / judicial as '
          'prescribed.\n'
          '\n'
          '## Tenure\n'
          '\n'
          '**3 years** or age **70**; re-appointment; no further Central/State employment.\n'
          '\n'
          '## Removal\n'
          '\n'
          '**Only the President** (same grounds/process as NHRC) — **not** the Governor.\n'
          '\n'
          '## Powers\n'
          '\n'
          'Inquire HR violations on State/Concurrent subjects; civil court powers; recommendatory; '
          'Human Rights Courts in districts (State + HC CJ concurrence).\n'
          '\n'
          '## Functions\n'
          '\n'
          'State-level HR watchdog mirroring NHRC functions within State lists.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          '**List II & III** only. If NHRC or another statutory commission already inquiring → '
          'SHRC stays out. Centre may confer UT functions (Delhi exception → NHRC).\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Presidential removal + SC inquiry path for misbehaviour; post-tenure employment bar.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Reports to State Government → State Legislature.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          '2019: tenure cut; HC Judge can be SHRC Chair.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Uneven State constitution/vacancy issues; UT adaptations (J&K/Ladakh notes in book).\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'NHRC vs SHRC; who removes SHRC Chair; List II/III limit.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- **Highest trap:** SHRC members removed by **Governor** — False; only **President**.\n'
          '- Trap: SHRC can inquire Union List matters freely — No.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Federal rights architecture — appointment by Governor but removal by President shows '
          'Centre’s protective overlay.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Chair+2 · Governor appoints\n'
          '- President removes\n'
          '- List II/III only\n'
          '- 3 yrs / 70\n',
  'slug': 'ncb-shrc',
  'sort_order': 3,
  'summary': 'Optional State-level statutory HR body under PHRA 1993 — List II/III; removed only '
             'by President.',
  'title': 'State Human Rights Commission',
  'visual_blocks': [{'columns': [{'heading': 'Appointment',
                                  'id': 'appt',
                                  'points': ['Governor',
                                             'State political + LoP panel',
                                             'HC CJ consultation for sitting judges']},
                                 {'heading': 'Removal',
                                  'id': 'rem',
                                  'points': ['President only',
                                             'Same grounds as NHRC',
                                             'SC inquiry for misbehaviour/incapacity']}],
                     'id': 'shrc-vs',
                     'title': 'Appointment vs removal',
                     'type': 'comparison'},
                    {'body': 'Governor **appoints**; President **removes**. Do not mix with SIC '
                             '(Governor removes) or State PSC patterns.',
                     'id': 'shrc-trap',
                     'title': 'Classic Prelims trap',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [['National Commission for Women Act, 1990',
                'Statutory basis; Commission constituted 31 Jan 1992.']],
  'body': '## Type of body\n'
          '\n'
          '**Autonomous statutory** body.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** National Commission for Women Act, 1990\n'
          '- **Established:** Constituted **1992**\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Women and Child Development (MWCD)**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Chair + **5** members + Member-Secretary; among members ≥1 SC and ≥1 ST\n'
          '\n'
          '## Appointment\n'
          '\n'
          'All **nominated by Central Government** (MWCD).\n'
          '\n'
          '## Qualifications\n'
          '\n'
          'Committed to women’s causes / experience as prescribed in Act.\n'
          '\n'
          '## Tenure\n'
          '\n'
          '**3 years**; may resign to Central Government.\n'
          '\n'
          '## Removal\n'
          '\n'
          'Central Government — insolvency, moral-turpitude conviction, unsound mind, '
          'refusal/incapacity, 3 consecutive absences, abuse of office.\n'
          '\n'
          '## Powers\n'
          '\n'
          'Investigate safeguards & complaints; **civil court powers**; inspect jails/custody; '
          'fund litigation; advise on planning; Centre must consult on major women-related '
          'policy.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Protect, promote, and ensure women’s rights; review laws; recommend remedial '
          'legislation; awareness & research.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Women-related safeguards & grievances nationwide (Central statute).\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Statutory autonomy; but nomination/removal by Centre (weaker than NHRC SC-inquiry '
          'model).\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Reports to Central Government → Parliament.\n'
          '\n'
          '## Important committees\n'
          '\n'
          'Committee on Status of Women (1974); National Perspective Plan for Women (1988).\n'
          '\n'
          '## Important judgments\n'
          '\n'
          '**Vishaka v. State of Rajasthan (1997)** — workplace sexual harassment guidelines '
          '(linked theme).\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'Parivarik Mahila Lok Adalat initiatives; ongoing law-review roles.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Women’s reservation implementation debates; workplace harassment compliance; '
          'trafficking.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Composition; civil court powers; MWCD parentage; contrast with NHRC appointment model.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: NCW is constitutional — False.\n'
          '- Trap: President appoints like NHRC — **Centre nominates**.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Use NCW + Vishaka + legislative review duty for gender justice institutional answers.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Act 1990 · set up 1992 · MWCD\n'
          '- Chair+5+MS · Centre nominates\n'
          '- 3 years · civil court powers\n',
  'slug': 'ncb-ncw',
  'sort_order': 4,
  'summary': 'Statutory autonomous commission (NCW Act 1990; constituted 1992) under MWCD.',
  'title': 'National Commission for Women',
  'visual_blocks': [{'id': 'ncw-pillars',
                     'items': [{'articles': '1990/92',
                                'detail': 'NCW Act 1990; constituted 1992.',
                                'id': 'a',
                                'label': 'Legal basis',
                                'slug': 'ncb-ncw',
                                'tone': 'teal'},
                               {'articles': 'MWCD',
                                'detail': 'Ministry of Women & Child Development.',
                                'id': 'b',
                                'label': 'Parent',
                                'slug': 'ncb-ncw',
                                'tone': 'olive'},
                               {'articles': 'Civil court',
                                'detail': 'Inquire, summon, inspect custody, fund litigation.',
                                'id': 'c',
                                'label': 'Powers',
                                'slug': 'ncb-ncw',
                                'tone': 'gold'}],
                     'title': 'NCW at a glance',
                     'type': 'pillars'},
                    {'body': 'NCW vs NCPCR vs NCM — all statutory group-specific commissions; '
                             'different parent ministries & target groups.',
                     'id': 'ncw-tip',
                     'title': 'Compare trio',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [['Commissions for Protection of Child Rights Act, 2005',
                'NCPCR & State CPCRs; Children’s Courts.'],
               ['RTE / POCSO / JJ Act', 'Additional monitoring & inquiry mandates.']],
  'body': '## Type of body\n'
          '\n'
          '**Autonomous statutory** body.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Commissions for Protection of Child Rights Act, 2005 (in force 2007)\n'
          '- **Established:** Set up **2007**\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Women and Child Development**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Chair + **6** members (≥2 women); child = under **18** (UNCRC)\n'
          '\n'
          '## Appointment\n'
          '\n'
          'Central Government; Chair via **3-member selection committee** chaired by MWCD '
          'Minister.\n'
          '\n'
          '## Qualifications\n'
          '\n'
          'Experience in child welfare/education/psychology/law etc. as prescribed.\n'
          '\n'
          '## Tenure\n'
          '\n'
          '**3 years**; max **2 terms**; Chair ≤**65** yrs, members ≤**60** yrs.\n'
          '\n'
          '## Removal\n'
          '\n'
          'Central Government (misbehaviour/incapacity for Chair; plus insolvency, paid '
          'employment, etc.).\n'
          '\n'
          '## Powers\n'
          '\n'
          'Review laws; inquire violations; inspect juvenile homes; **civil court powers**; roles '
          'under **RTE 2009**, **POCSO 2012**, **JJ Act 2015**.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Protect child rights; monitor implementation; recommend reforms; awareness.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Child rights nationwide; coordinate with State CPCRs; Children’s Courts (State + HC '
          'CJ).\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Statutory autonomy with Central appointment/removal.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Reports to Central Government → Parliament.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'Expanded statutory roles via RTE/POCSO/JJ.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'POCSO implementation, online child safety, school safety, child labour.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Definition of child; composition; multi-Act mandate.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: NCPCR under MHA — No, **MWCD**.\n'
          '- Trap: child = 14/16 always — Act uses **under 18**.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Rights of children as justiciable ecosystem — NCPCR bridges welfare + criminal '
          'statutes.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- CPCR Act 2005 · 2007 · MWCD\n'
          '- Chair+6 · 3 yrs · age caps\n'
          '- RTE/POCSO/JJ add-ons\n',
  'slug': 'ncb-ncpcr',
  'sort_order': 5,
  'summary': 'Statutory child-rights commission (CPCR Act 2005; 2007) — MWCD; RTE/POCSO/JJ roles.',
  'title': 'National Commission for Protection of Child Rights',
  'visual_blocks': [{'id': 'ncpcr-acts',
                     'items': [{'articles': '2005',
                                'detail': 'Core commission statute.',
                                'id': 'cpcr',
                                'label': 'CPCR Act',
                                'slug': 'ncb-ncpcr',
                                'tone': 'teal'},
                               {'articles': '2009',
                                'detail': 'Monitor right to education.',
                                'id': 'rte',
                                'label': 'RTE Act',
                                'slug': 'ncb-ncpcr',
                                'tone': 'olive'},
                               {'articles': '2012',
                                'detail': 'Monitor & inquire child sexual offences themes.',
                                'id': 'pocso',
                                'label': 'POCSO',
                                'slug': 'ncb-ncpcr',
                                'tone': 'gold'},
                               {'articles': '2015',
                                'detail': 'Juvenile justice system oversight linkages.',
                                'id': 'jj',
                                'label': 'JJ Act',
                                'slug': 'ncb-ncpcr',
                                'tone': 'orange'}],
                     'title': 'Multi-Act mandate',
                     'type': 'pillars'},
                    {'body': 'NCPCR = **child under 18** + **MWCD** + **three add-on Acts** '
                             '(RTE/POCSO/JJ).',
                     'id': 'ncpcr-tip',
                     'title': 'Memory',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [['National Commission for Minorities Act, 1992',
                'Statutory commission from 1993; earlier executive body 1978.'],
               ['Notified minorities',
                'Muslims, Christians, Sikhs, Buddhists, Parsis; Jains added 2014.']],
  'body': '## Type of body\n'
          '\n'
          '**Autonomous statutory** (was executive 1978–93).\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** National Commission for Minorities Act, 1992 (in force 17 May 1993); '
          'earlier MHA resolution 12 Jan 1978\n'
          '- **Established:** Statutory Commission **1993**\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Minority Affairs** (carved from SJ&E, 2006)\n'
          '\n'
          '## Composition\n'
          '\n'
          'Chair + Vice-Chair + **5** members (**5 including Chair** from minority communities)\n'
          '\n'
          '## Appointment\n'
          '\n'
          'Nominated by **Central Government**.\n'
          '\n'
          '## Tenure\n'
          '\n'
          '**3 years**\n'
          '\n'
          '## Removal\n'
          '\n'
          'Central Government (grounds akin to NCW, including abuse detrimental to '
          'minorities/public interest).\n'
          '\n'
          '## Powers\n'
          '\n'
          'Monitor minority safeguards; complaints; studies; **civil court powers**; reports to '
          'Parliament.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Evaluate progress of minority development; recommend effective implementation of '
          'safeguards.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Notified minority communities at national level.\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Statutory but Centre-nominated.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Central Government → Parliament.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'Vice-Chair via Amendment Act 1995; Jains notified **2014**.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Minority educational institutions; notification debates; welfare schemes oversight.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Notified list; statutory vs earlier executive; parent ministry.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: NCM always existed as statutory since 1978 — **executive till 1993**.\n'
          '- Trap: Jains always included — added **2014**.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'From executive cell to statutory commission — institutionalisation of minority '
          'safeguards.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Act 1992 · statutory 1993 · Minority Affairs\n'
          '- Chair+VC+5 · 3 yrs\n'
          '- 6 notified communities (Jains 2014)\n',
  'slug': 'ncb-ncm',
  'sort_order': 6,
  'summary': 'Statutory minorities commission (NCM Act 1992; 1993) — Ministry of Minority Affairs.',
  'title': 'National Commission for Minorities',
  'visual_blocks': [{'events': [{'detail': 'MHA resolution — non-statutory.',
                                 'id': 'e1',
                                 'label': 'Executive body',
                                 'year': 1978},
                                {'detail': 'NCM Act 1992 in force.',
                                 'id': 'e2',
                                 'label': 'Statutory NCM',
                                 'year': 1993},
                                {'detail': 'Sixth notified minority community.',
                                 'id': 'e3',
                                 'label': 'Jains notified',
                                 'year': 2014}],
                     'id': 'ncm-timeline',
                     'title': 'NCM evolution',
                     'type': 'timeline'},
                    {'body': 'Notified: Muslims, Christians, Sikhs, Buddhists, Parsis + **Jains '
                             '(2014)**. Parent: **Minority Affairs**, not MHA.',
                     'id': 'ncm-trap',
                     'title': 'Prelims',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [['Right to Information Act, 2005', 'Establishes CIC & SICs.'],
               ['RTI Amendment Act, 2019',
                'Term & salary prescribed by Central Government; ended CEC/EC parity.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory** (not constitutional).\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Right to Information Act, 2005 (amended 2019)\n'
          '- **Established:** Established **2005**\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Personnel, Public Grievances and Pensions (DoPT)**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Chief Information Commissioner + ≤**10** Information Commissioners\n'
          '\n'
          '## Appointment\n'
          '\n'
          '**President** on committee: PM, LoP Lok Sabha, Union Cabinet Minister nominated by PM.\n'
          '\n'
          '## Qualifications\n'
          '\n'
          'Eminent persons with law/science/social service/management/journalism/etc. experience; '
          '**not** MPs/MLAs or office of profit as barred.\n'
          '\n'
          '## Tenure\n'
          '\n'
          'As **prescribed by Central Government** or age **65** (earlier fixed 5 years). Not '
          'eligible for reappointment as same; IC may become CIC (total service ≤5 years).\n'
          '\n'
          '## Removal\n'
          '\n'
          'President — standard grounds; misbehaviour/incapacity after **SC inquiry**.\n'
          '\n'
          '## Powers\n'
          '\n'
          'Complaints & second appeals; suo motu inquiry; civil court powers; secure compliance; '
          'penalty **₹250/day** up to **₹25,000**.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Adjudicate RTI disputes for Central/UT public authorities; promote transparency.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Central Government & UTs’ public authorities (as under RTI Act).\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'SC-inquiry removal; but **2019** shifted term/salary to Central prescription (debate on '
          'autonomy).\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Annual report to Central Government → Parliament.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          '**RTI Amendment 2019** — term & conditions by Centre; ended EC-like parity.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Vacancies, pendency, digital RTI, autonomy debate post-2019.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Appointment committee; penalties; 2019 amendment; CIC vs SIC.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: CIC is constitutional like EC — False.\n'
          '- Trap: Tenure still fixed 5 years in Act as before 2019 — now Centre-prescribed.\n'
          '- Trap: Salary still = CEC — ended by 2019.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Transparency vs institutional independence — analyse 2019 amendment critically.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- RTI 2005 · President + 3-member panel\n'
          '- ≤10 ICs · age 65 / Centre term\n'
          '- Penalty ₹250/day ≤ ₹25k · 2019 amd\n',
  'slug': 'ncb-cic',
  'sort_order': 7,
  'summary': 'Statutory RTI appellate body (RTI Act 2005; amd. 2019) — DoPT / Personnel.',
  'title': 'Central Information Commission',
  'visual_blocks': [{'id': 'cic-appoint',
                     'root': 'vac',
                     'steps': [{'id': 'vac',
                                'label': 'CIC / IC vacancy',
                                'options': [{'label': 'Selection committee', 'next': 'com'}]},
                               {'id': 'com',
                                'label': 'PM + LoP (LS) + Cabinet Minister (PM nominee)',
                                'options': [{'label': 'Recommend → President', 'next': 'ap'}]},
                               {'detail': 'Post-2019: term & salary as Central Govt prescribes',
                                'id': 'ap',
                                'label': 'President appoints'}],
                     'title': 'CIC appointment',
                     'type': 'flowchart'},
                    {'body': 'Do not quote pre-2019 **5-year / CEC salary parity** as current law '
                             'without noting the Amendment.',
                     'id': 'cic-trap',
                     'title': '2019 trap',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [['Right to Information Act, 2005', 'SICs for State public authorities.'],
               ['RTI Amendment Act, 2019', 'Term & conditions by Central Government.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory**.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Right to Information Act, 2005\n'
          '- **Established:** 2005 framework (all States constituted)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          'State General Administration / equivalent; statute is Central\n'
          '\n'
          '## Composition\n'
          '\n'
          'State Chief Information Commissioner + ≤**10** State ICs (number varies)\n'
          '\n'
          '## Appointment\n'
          '\n'
          '**Governor** on committee: CM, LoP Assembly, State Cabinet Minister nominated by CM.\n'
          '\n'
          '## Tenure\n'
          '\n'
          'As prescribed by **Central Government** or age **65**; no reappointment (same 5-yr '
          'total cap if promoted).\n'
          '\n'
          '## Removal\n'
          '\n'
          '**Governor** (same grounds as CIC; SC inquiry for misbehaviour/incapacity).\n'
          '\n'
          '## Powers\n'
          '\n'
          'Same RTI complaint/appeal/compliance/penalty model for **State** bodies.\n'
          '\n'
          '## Functions\n'
          '\n'
          'State transparency adjudication & annual reporting.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'State public authorities under RTI.\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'SC-inquiry removal; term/salary autonomy debate post-2019.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Annual report → State Legislature.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'RTI Amendment 2019 applies to SIC conditions too.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'State-level vacancies & pendency; autonomy concerns.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'CIC vs SIC appointment/removal; penalties identical.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: SIC removed by President — **Governor** removes.\n'
          '- Contrast carefully with **SHRC** (President removes).\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Federal RTI design — mirrored institutions with State appointment.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Governor appoints & removes\n'
          '- CM+LoP+Minister panel\n'
          '- Same penalties as CIC\n'
          '- 2019 Centre-prescribed term\n',
  'slug': 'ncb-sic',
  'sort_order': 8,
  'summary': 'State RTI commission under RTI Act 2005 — Governor appointment; Centre-prescribed '
             'tenure post-2019.',
  'title': 'State Information Commission',
  'visual_blocks': [{'columns': [{'heading': 'CIC',
                                  'id': 'cic',
                                  'points': ['President appoints',
                                             'President removes',
                                             'Central/UT authorities',
                                             'Report → Parliament']},
                                 {'heading': 'SIC',
                                  'id': 'sic',
                                  'points': ['Governor appoints',
                                             'Governor removes',
                                             'State authorities',
                                             'Report → State Legislature']}],
                     'id': 'sic-compare',
                     'title': 'CIC vs SIC — who acts?',
                     'type': 'comparison'},
                    {'body': 'SIC: Governor removes. SHRC: **President** removes. Highest '
                             'confusion pair in this Part.',
                     'id': 'sic-trap',
                     'title': 'Do not mix with SHRC',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [['Central Vigilance Commission Act, 2003',
                'Statutory status after Vineet Narain impetus.'],
               ['Santhanam Committee (1962–64)', 'Recommended CVC creation.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory** (originally **executive** 1964).\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Executive resolution 1964 → **CVC Act, 2003**; Whistle Blowers / PIDPI '
          'resolution 2004\n'
          '- **Established:** 1964 (statutory **2003**)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Personnel (DoPT)**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Central Vigilance Commissioner + ≤**2** Vigilance Commissioners\n'
          '\n'
          '## Appointment\n'
          '\n'
          '**President** (warrant) on 3-member committee: PM, Union Home Minister, LoP Lok Sabha.\n'
          '\n'
          '## Tenure\n'
          '\n'
          '**4 years** or age **65**; no further Central/State employment.\n'
          '\n'
          '## Removal\n'
          '\n'
          'President; misbehaviour/incapacity after **SC inquiry**.\n'
          '\n'
          '## Powers\n'
          '\n'
          'Inquire PC Act cases; **superintendence over CBI/DSPE** for PC Act corruption cases; '
          'advise Centre; vigilance administration; whistle-blower complaints.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Apex vigilance body for Central Government; integrity of administration.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Central Government employees / PC Act matters as specified; not a substitute criminal '
          'court.\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Statutory tenure + SC-inquiry removal; salary parity with UPSC Chair/member (book).\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Annual report to President → Parliament.\n'
          '\n'
          '## Important committees\n'
          '\n'
          '**Santhanam Committee** on Prevention of Corruption.\n'
          '\n'
          '## Important judgments\n'
          '\n'
          '**Vineet Narain (1998)** — CBI independence; led toward statutory CVC.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'Whistle Blowers Protection Act, 2014 ecosystem; CVC–CBI supervision interface.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Corruption investigations oversight; whistle-blower protection gaps.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Santhanam; statutory turn 2003; CVC vs CBI vs Lokpal.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: CVC always statutory since 1964 — **statutory only from 2003**.\n'
          '- Trap: CVC investigates all crimes — focus is **vigilance / PC Act** lane.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Institutional anti-corruption architecture: CVC supervision + CBI investigation + '
          'Lokpal oversight.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- 1964 exec → 2003 Act · Personnel\n'
          '- CVC+≤2 · PM-HM-LoP panel\n'
          '- 4 yrs/65 · CBI superintendence (PC Act)\n',
  'slug': 'ncb-cvc',
  'sort_order': 9,
  'summary': 'Statutory vigilance body (CVC Act 2003; exec since 1964) — Santhanam; Personnel.',
  'title': 'Central Vigilance Commission',
  'visual_blocks': [{'events': [{'detail': 'Santhanam follow-up.',
                                 'id': 'e1',
                                 'label': 'Executive CVC',
                                 'year': 1964},
                                {'detail': 'SC on CBI independence.',
                                 'id': 'e2',
                                 'label': 'Vineet Narain',
                                 'year': 1998},
                                {'detail': 'Statutory Commission.',
                                 'id': 'e3',
                                 'label': 'CVC Act',
                                 'year': 2003}],
                     'id': 'cvc-timeline',
                     'title': 'CVC status journey',
                     'type': 'timeline'},
                    {'body': '**Santhanam → 1964 CVC → Vineet Narain → 2003 Act**. Appointment '
                             'trio: **PM + HM + LoP(LS)**.',
                     'id': 'cvc-tip',
                     'title': 'Memory',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [['Delhi Special Police Establishment Act, 1946',
                'Legal power base for CBI investigation.'],
               ['MHA Resolution, 1963', 'CBI established; later under DoPT.']],
  'body': '## Type of body\n'
          '\n'
          '**Executive investigating agency** (not created by a dedicated CBI Act); powers via '
          '**DSPE Act, 1946**.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** MHA resolution **1963**; SPE origin 1941 → DSPE Act 1946; CBI '
          'organisational creation 1963\n'
          '- **Established:** CBI **1963**\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**DoPT, Ministry of Personnel** (not MHA currently)\n'
          '\n'
          '## Composition\n'
          '\n'
          'Director (IG of DSPE) + Special/Additional Directors + police hierarchy; Directorate of '
          'Prosecution (Lokpal Act ecosystem)\n'
          '\n'
          '## Appointment\n'
          '\n'
          'Director by Central Government on committee: **PM, LoP LS, CJI/nominee**. SP+ on '
          'CVC-led committee; Prosecution Director on CVC recommendation.\n'
          '\n'
          '## Tenure\n'
          '\n'
          'Director originally fixed **2 years** (CVC Act); **2021 amendment** allows extensions '
          'up to total **5 years** (1 year at a time).\n'
          '\n'
          '## Removal\n'
          '\n'
          'As per service rules / statutory protections for Director tenure; high political '
          'sensitivity.\n'
          '\n'
          '## Powers\n'
          '\n'
          'Investigate corruption, economic offences, serious & organised crime (general crime '
          'lane — **not** specialised terror like NIA); Interpol NCB role.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Premier investigating agency for complex/inter-State/Central cases as entrusted.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Needs **State consent** under DSPE (except railway areas / notified); Union Territories '
          'as applicable.\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Director selection panel + fixed tenure (debated after extension clause); CVC '
          'superintendence in PC Act cases; Vineet Narain legacy.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Administrative control DoPT; functional supervision interfaces with CVC/Lokpal as per '
          'law.\n'
          '\n'
          '## Important judgments\n'
          '\n'
          'SC **2014** struck down DSPE s.6A prior-sanction for JS+ (Art. 14). Vineet Narain on '
          'autonomy.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'Lokpal Act & DSPE Amendments 2014; Director tenure extension law **2021**.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'General consent withdrawals by States; federal friction; Director appointments.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Consent; parent ministry; CBI vs NIA; Director appointment panel.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: CBI under MHA — currently **DoPT/Personnel**.\n'
          '- Trap: CBI is statutory like NIA Act body — organisation is executive; powers from '
          'DSPE.\n'
          '- Trap: can enter any State freely — needs **consent**.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Federal criminal investigation — consent doctrine vs national agency needs.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- 1963 · DSPE 1946 · DoPT\n'
          '- Director: PM+LoP+CJI\n'
          '- State consent · 2021 tenure extensions\n',
  'slug': 'ncb-cbi',
  'sort_order': 10,
  'summary': 'Central investigating agency (1963) under DoPT — DSPE Act powers; State consent '
             'required.',
  'title': 'Central Bureau of Investigation',
  'visual_blocks': [{'columns': [{'heading': 'Legal reality',
                                  'id': 'legal',
                                  'points': ['Created by resolution 1963',
                                             'Powers from DSPE Act 1946',
                                             'DoPT administrative control',
                                             'State consent generally needed']},
                                 {'heading': 'Common myths',
                                  'id': 'myth',
                                  'points': ['‘CBI Act’ body like NIA',
                                             'Always under MHA',
                                             'Freely investigates in all States',
                                             'Same as NIA terror mandate']}],
                     'id': 'cbi-identity',
                     'title': 'CBI identity',
                     'type': 'comparison'},
                    {'body': 'Without State consent (or SC/HC order / Union territory rules), CBI '
                             'cannot investigate in that State — a perennial Prelims & Mains '
                             'theme.',
                     'id': 'cbi-trap',
                     'title': 'Consent trap',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [['Lokpal and Lokayuktas Act, 2013',
                'Establishes Lokpal at Centre; States to establish Lokayuktas.'],
               ['First ARC (1966–70)', 'Recommended Lokpal/Lokayukta.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory** (Lokpal); State **Lokayuktas** via State laws under the Act’s scheme.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Lokpal and Lokayuktas Act, **2013** (after ~10 failed Bills 1968–2011)\n'
          '- **Established:** Act 2013; first State Lokayukta — Maharashtra 1971 (Odisha Act '
          '1970)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Personnel**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Chair + ≤**8** members (**50% judicial**; **50%** SC/ST/OBC/minorities/women)\n'
          '\n'
          '## Appointment\n'
          '\n'
          'Selection Committee: PM, LS Speaker, LoP LS, CJI/nominee, eminent jurist; assisted by '
          'Search Committee.\n'
          '\n'
          '## Qualifications\n'
          '\n'
          'Judicial / non-judicial as prescribed; integrity & experience bars.\n'
          '\n'
          '## Tenure\n'
          '\n'
          'As provided in Act (fixed term / age limits as applicable).\n'
          '\n'
          '## Removal\n'
          '\n'
          'As per Act — President on SC reference process for specified grounds.\n'
          '\n'
          '## Powers\n'
          '\n'
          'Jurisdiction over PM (with exclusions), Ministers, MPs, Groups A–D; superintendence '
          'over investigating agencies incl. CBI for referred cases; attach/confiscate; '
          'prosecution sanction; timelines.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Inquire/investigate corruption complaints; oversee probes; order assets action.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Public servants as defined; **no suo motu** in classic design critique; **7-year** '
          'limitation; anonymous complaints barred (book drawbacks).\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Statutory selection breadth; operationalisation historically slow — exam theme.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'As per Act to Parliament / President pathways.\n'
          '\n'
          '## Important committees\n'
          '\n'
          'First ARC (Morarji Desai); Ombudsman model (Sweden 1809).\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'Institutionalisation after 2013; Directorate of Prosecution linkages with CBI.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Appointments, vacancies, complaint disposal; State Lokayukta unevenness.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'PM jurisdiction caveats; composition quotas; no suo motu; Lokpal vs CVC vs CBI.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: Lokpal can take up any matter suo motu like NHRC — book flags **no suo motu**.\n'
          '- Trap: Lokayukta identical in all States — States design within framework.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Anti-corruption architecture & political accountability — evaluate Lokpal design gaps.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Act 2013 · Personnel\n'
          '- Chair+≤8 · 50% judicial · diversity quota\n'
          '- PM+Speaker+LoP+CJI+jurist panel\n'
          '- No suo motu · 7-yr limit (critique)\n',
  'slug': 'ncb-lokpal',
  'sort_order': 11,
  'summary': 'Statutory anti-corruption ombudsman (Lokpal Act 2013) — First ARC lineage; State '
             'Lokayuktas.',
  'title': 'Lokpal and Lokayuktas',
  'visual_blocks': [{'id': 'lokpal-pillars',
                     'items': [{'articles': '≤8',
                                'detail': '50% judicial; 50% diversity quota.',
                                'id': 'comp',
                                'label': 'Composition',
                                'slug': 'ncb-lokpal',
                                'tone': 'teal'},
                               {'articles': '5',
                                'detail': 'PM, Speaker, LoP LS, CJI/nominee, jurist.',
                                'id': 'sel',
                                'label': 'Selection',
                                'slug': 'ncb-lokpal',
                                'tone': 'olive'},
                               {'articles': 'Critique',
                                'detail': 'No suo motu; 7-year limit; anonymous bar.',
                                'id': 'gap',
                                'label': 'Design gaps',
                                'slug': 'ncb-lokpal',
                                'tone': 'gold'}],
                     'title': 'Lokpal design keys',
                     'type': 'pillars'},
                    {'body': '**First ARC → decades of Bills → 2013 Act**. Distinguish Lokpal '
                             '(Centre) from Lokayukta (State).',
                     'id': 'lokpal-tip',
                     'title': 'Lineage',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [['National Investigation Agency Act, 2008', 'Constituted 2009 post-26/11.'],
               ['NIA Amendment Act, 2019',
                'Expanded schedule — trafficking, cyber-terror, explosives, etc.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory** central counter-terror / scheduled-offences agency.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** National Investigation Agency Act, **2008** (amd. **2019**)\n'
          '- **Established:** Constituted **2009** (post-26/11)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Home Affairs**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Headed by **Director-General** (powers akin to State DGP)\n'
          '\n'
          '## Appointment\n'
          '\n'
          'DG by **Central Government**\n'
          '\n'
          '## Tenure\n'
          '\n'
          'As per Central appointment / service rules.\n'
          '\n'
          '## Removal\n'
          '\n'
          'Central Government (service rules).\n'
          '\n'
          '## Powers\n'
          '\n'
          'Investigate & prosecute **Schedule** offences; concurrent jurisdiction; TFFC cell; '
          '**extraterritorial** probe of scheduled offences; 2019 expanded schedule.\n'
          '\n'
          '## Functions\n'
          '\n'
          'National terror & sovereignty/security offence investigation; specialised prosecution.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Scheduled offences nationwide + abroad (as Act allows); distinct from CBI’s general '
          'crime/corruption lane.\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Central agency — federal tensions over concurrent jurisdiction are a Mains theme.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'MHA administrative control; specialised NIA courts.\n'
          '\n'
          '## Important committees\n'
          '\n'
          'Second ARC ‘Combating Terrorism’ (2008, Veerappa Moily).\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          '**NIA Amendment 2019** — human trafficking, counterfeit currency, prohibited arms, '
          'cyber-terrorism, explosives, etc.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Schedule expansion cases; Centre–State investigation conflicts.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'NIA vs CBI; 2019 amendment; post-26/11 origin.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: NIA needs State consent like CBI always — NIA has **stronger concurrent** '
          'design for scheduled offences.\n'
          '- Trap: NIA = corruption agency — No, **scheduled/security** offences.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'National security federalism — concurrent investigation vs State police primacy.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Act 2008 · 2009 · MHA\n'
          '- DG · Schedule offences\n'
          '- 2019 expansion · extraterritorial\n',
  'slug': 'ncb-nia',
  'sort_order': 12,
  'summary': 'Statutory counter-terror agency (NIA Act 2008; amd. 2019) under MHA — concurrent & '
             'extraterritorial reach.',
  'title': 'National Investigation Agency',
  'visual_blocks': [{'columns': [{'heading': 'NIA',
                                  'id': 'nia',
                                  'points': ['NIA Act 2008',
                                             'MHA',
                                             'Terror/scheduled offences',
                                             'Concurrent + extraterritorial design']},
                                 {'heading': 'CBI',
                                  'id': 'cbi',
                                  'points': ['DSPE + 1963 resolution',
                                             'DoPT',
                                             'Corruption/econ/special crime',
                                             'State consent generally']}],
                     'id': 'nia-vs-cbi',
                     'title': 'NIA vs CBI (quick)',
                     'type': 'comparison'},
                    {'body': '**26/11 → NIA Act 2008 → agency 2009**. Amendment **2019** = '
                             'schedule expansion.',
                     'id': 'nia-tip',
                     'title': 'Origin cue',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [['Disaster Management Act, 2005', 'NDMA, SDMA, DDMA, NDRF institutional stack.'],
               ['Notified under Act, 2006', 'Statutory notification of NDMA.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory** apex body (initially executive moves in 2005; notified under Act 2006).\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Disaster Management Act, **2005**\n'
          '- **Established:** Constituted 2005; statutory notification **2006**\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Home Affairs**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Chair + ≤**9** members; **PM = ex-officio Chair**; VC = Cabinet status; other members = '
          'MoS status\n'
          '\n'
          '## Appointment\n'
          '\n'
          'Other members nominated by Chair (PM).\n'
          '\n'
          '## Tenure\n'
          '\n'
          'As prescribed / nomination terms.\n'
          '\n'
          '## Removal\n'
          '\n'
          'As per Act / government nomination terms.\n'
          '\n'
          '## Powers\n'
          '\n'
          'Lay DM policies/plans/guidelines; approve National Plan; guide SDMAs; coordinate; '
          'recommend funds; superintendence of **NDRF**; annual report to Parliament.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Prevention, mitigation, preparedness, response policy leadership.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'National disaster management; works with SDMA (CM Chair) & DDMA (Collector Chair).\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'PM-chaired — political apex with statutory duties.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Annual report → Parliament.\n'
          '\n'
          '## Important committees\n'
          '\n'
          'High-Powered Committee 1999; National Committee 2001 (Gujarat quake); tsunami 2004 '
          'impetus.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'NDMA–SDMA–DDMA–NDRF operationalisation; pandemic governance debates under DM Act.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Climate disasters, DM Act use in emergencies, NDRF deployments.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Institutional stack; PM Chair; DM Act federalism.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: NDMA Chair is Home Minister — **PM** is ex-officio Chair.\n'
          '- Trap: no State bodies — **SDMA/DDMA** exist.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Disaster federalism — centre guidelines + state/district execution + NDRF.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- DM Act 2005 · MHA\n'
          '- PM Chair · ≤9 members\n'
          '- SDMA (CM) · DDMA (Collector) · NDRF\n',
  'slug': 'ncb-ndma',
  'sort_order': 13,
  'summary': 'Statutory disaster apex (DM Act 2005) — PM Chair; SDMA/DDMA/NDRF framework; MHA.',
  'title': 'National Disaster Management Authority',
  'visual_blocks': [{'id': 'ndma-tree',
                     'root': {'children': [{'children': [{'detail': 'District plans & response',
                                                          'id': 'ddma',
                                                          'label': 'DDMA (Collector Chair)'}],
                                            'id': 'sdma',
                                            'label': 'SDMA (CM Chair)'},
                                           {'detail': 'Specialised response force',
                                            'id': 'ndrf',
                                            'label': 'NDRF'}],
                              'detail': 'National policies & NDRF superintendence',
                              'id': 'ndma',
                              'label': 'NDMA (PM Chair)'},
                     'title': 'NDMA institutional stack',
                     'type': 'tree'},
                    {'body': '**PM → CM → Collector** chairs the three tiers. NDRF under NDMA '
                             'superintendence.',
                     'id': 'ndma-tip',
                     'title': 'Memory',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [['Advocates Act, 1961', 'BCI & State Bar Councils.'],
               ['All India Bar Committee / Law Commission 14th Report', 'Historical pedigree.']],
  'body': '## Type of body\n'
          '\n'
          '**Autonomous statutory** professional regulator.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Advocates Act, **1961**\n'
          '- **Established:** Framework via 1961 Act (All India Bar Committee / Justice S.R. Das '
          '1951–53; Law Commission 14th Report 1958)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Department of Legal Affairs, Ministry of Law and Justice**\n'
          '\n'
          '## Composition\n'
          '\n'
          '1 member elected by each State Bar Council + **AGI & Solicitor-General** (ex-officio); '
          'Chair & Vice-Chair elected by Council (**2-year** term)\n'
          '\n'
          '## Appointment\n'
          '\n'
          'Members **elected** by SBCs; office-bearers elected internally (not Presidential '
          'commission style).\n'
          '\n'
          '## Tenure\n'
          '\n'
          'Member term = period as SBC member; Chair/VC **2 years**.\n'
          '\n'
          '## Removal\n'
          '\n'
          'As per Advocates Act / Council rules (professional body, not NHRC-style).\n'
          '\n'
          '## Powers\n'
          '\n'
          'Professional standards & discipline; supervise SBCs; legal education standards; '
          'recognise law degrees; legal aid; law reform suggestions.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Regulate advocates; maintain rolls via SBCs; uphold ethics.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Advocates across India via BCI–SBC system (~24 State Bar Councils).\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Elected professional self-regulation under statute.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Statutory regulator — not a classic ‘report to Parliament ministry commission’ in NHRC '
          'sense.\n'
          '\n'
          '## Important committees\n'
          '\n'
          'All India Bar Committee; linkage to Law Commission historical reports.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Legal education regulation debates; professional ethics; entry standards.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Elected composition; AG/SG ex-officio; education regulation.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: BCI Chair appointed by President like NHRC — **elected** by Council.\n'
          '- Trap: BCI is constitutional — False.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Self-regulation of professions vs State oversight — legal education quality.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Advocates Act 1961 · Law & Justice\n'
          '- Elected + AG/SG ex-officio\n'
          '- Chair/VC 2 yrs · standards & education\n',
  'slug': 'ncb-bci',
  'sort_order': 14,
  'summary': 'Statutory regulator of the legal profession (Advocates Act 1961) — Law & Justice.',
  'title': 'Bar Council of India',
  'visual_blocks': [{'id': 'bci-pillars',
                     'items': [{'articles': 'Ethics',
                                'detail': 'Professional conduct for advocates.',
                                'id': 'std',
                                'label': 'Standards & discipline',
                                'slug': 'ncb-bci',
                                'tone': 'teal'},
                               {'articles': 'Education',
                                'detail': 'Standards & degree recognition.',
                                'id': 'edu',
                                'label': 'Legal education',
                                'slug': 'ncb-bci',
                                'tone': 'olive'},
                               {'articles': 'SBCs',
                                'detail': 'State Bar Councils network.',
                                'id': 'sbc',
                                'label': 'Supervise SBCs',
                                'slug': 'ncb-bci',
                                'tone': 'gold'}],
                     'title': 'BCI functions',
                     'type': 'pillars'},
                    {'body': 'Unlike NHRC/CIC, BCI is **elected professional self-government** '
                             'under a statute.',
                     'id': 'bci-tip',
                     'title': 'Contrast',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [['Order of Central Government (MoLJ)',
                'Constituted from time to time; typically ~3-year term.'],
               ['First post-Independence Commission, 1955', 'M.C. Setalvad as first Chair.']],
  'body': '## Type of body\n'
          '\n'
          '**Non-statutory advisory** (executive) body.\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Order of Central Government (Department of Legal Affairs, MoLJ) from time '
          'to time\n'
          '- **Established:** First post-Independence Commission **1955** (British-era commissions '
          'from 1834 Macaulay onward)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Law and Justice**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Not fixed — Chair (usually SC/HC judge/jurist), full-time members, Member-Secretary '
          '(ILS Addl Secy/Secy rank), part-time members\n'
          '\n'
          '## Appointment\n'
          '\n'
          '**Central Government**\n'
          '\n'
          '## Tenure\n'
          '\n'
          'Typically **3 years** per Commission (terms sometimes extended)\n'
          '\n'
          '## Removal\n'
          '\n'
          'As per government appointment terms.\n'
          '\n'
          '## Powers\n'
          '\n'
          '**Recommendatory only** — repeal/reform/codification; DPSP-aligned legislation; '
          'justice-delivery reforms; ~277+ reports historically cited in book era.\n'
          '\n'
          '## Functions\n'
          '\n'
          'Advise Government on law reform; research & reports.\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Advisory — no adjudicatory power.\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Expert advisory; recommendations **non-binding**.\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Reports to Government (MoLJ); implementation discretionary.\n'
          '\n'
          '## Important committees\n'
          '\n'
          'Itself is the standing reform idea engine; pre-Independence products include IPC, CrPC, '
          'CPC, Evidence, Contract, TPA lineage themes.\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          'Successive Commission reconstitutions; report-driven Bills often cite LCI.\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'Which Commission is current; major reports used in legislative debates.\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Non-statutory character; recommendatory nature; historical continuity.\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: Law Commission is statutory like NITI is statutory — **both non-statutory**, '
          'but NITI is Cabinet resolution think-tank; LCI is MoLJ order advisory.\n'
          '- Trap: LCI judgments bind courts — **reports advise**.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Law reform pipeline — expert body without binding force; link to legislative quality.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Executive/MoLJ order · non-statutory\n'
          '- ~3-year Commissions · recommendatory\n'
          '- First 1955 (Setalvad)\n',
  'slug': 'ncb-law-commission',
  'sort_order': 15,
  'summary': 'Non-statutory advisory body (MoLJ order) — successive Commissions; reform reports.',
  'title': 'Law Commission of India',
  'visual_blocks': [{'columns': [{'heading': 'Law Commission',
                                  'id': 'lci',
                                  'points': ['Executive advisory',
                                             'MoLJ order',
                                             'Law reform reports',
                                             'Non-binding recommendations']},
                                 {'heading': 'Bar Council of India',
                                  'id': 'bci',
                                  'points': ['Statutory regulator',
                                             'Advocates Act 1961',
                                             'Profession & education',
                                             'Disciplinary powers']}],
                     'id': 'lci-compare',
                     'title': 'Law Commission vs BCI',
                     'type': 'comparison'},
                    {'body': 'Law Commission = **non-statutory advisory**. Do not club it with '
                             'statutory commissions like NHRC/CIC.',
                     'id': 'lci-trap',
                     'title': 'Type trap',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [['Delimitation Acts (1952, 1962/63, 1972/73, 2002)',
                'Successive statutory commissions.'],
               ['Arts 81, 82, 170, 330, 332',
                'Constitutional hooks for readjustment & reservation.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory** high-powered body (created when Parliament passes a Delimitation Act).\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** Successive **Delimitation Commission Acts**; constitutional Articles **81, '
          '82, 170, 330, 332**\n'
          '- **Established:** Commissions: **1952, 1963, 1973, 2002**; fresh panel **March 2020** '
          '(J&K; briefly NE)\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Law and Justice**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Typical: SC judge (serving/retired) **Chair** + **CEC/EC** + State EC (ex-officio); '
          'associate MPs/MLAs (**no vote**)\n'
          '\n'
          '## Appointment\n'
          '\n'
          'Central Government under the relevant Act\n'
          '\n'
          '## Tenure\n'
          '\n'
          'For the life of that Commission’s mandate\n'
          '\n'
          '## Removal\n'
          '\n'
          'As per Act — high-powered / insulated design\n'
          '\n'
          '## Powers\n'
          '\n'
          'Demarcate LS & Assembly constituencies; orders have **force of law**, **unchallengeable '
          'in court**; laid before LS/Assembly but **not modifiable**\n'
          '\n'
          '## Functions\n'
          '\n'
          'Readjust boundaries (and related reservation seats as mandated); implement freeze rules '
          'on seat totals\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'As specified in the Act (all-India or special territories like J&K 2020–22)\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Orders final — strongest finality among bodies in this Part\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'Orders published; copies laid before House — no amendment power\n'
          '\n'
          '## Important judgments\n'
          '\n'
          '**R.C. Poudyal (1993)** on vote parity themes; J&K delimitation order May 2022 context\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          '84th & 87th Amendments — freeze of seat totals till census after **2026**; J&K '
          'Delimitation 2020–22 (90 ACs: 43 Jammu / 47 Kashmir; ST/SC reservation)\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          '**Post-2026 delimitation politics**; federal representation debates; women’s '
          'reservation linkage to delimitation census\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          'Finality of orders; Delimitation vs EC; freeze till after 2026 census\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: Delimitation orders appealable like ordinary admin orders — **not '
          'justiciable**.\n'
          '- Trap: EC itself delimits seats alone — **Delimitation Commission** does (EC is '
          'member).\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Representation, federal bargain, and the 2026 freeze — demographic vs political '
          'equity.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- Statutory under Delimitation Acts · Law & Justice\n'
          '- SC judge + CEC/EC + SEC\n'
          '- Orders final · freeze till post-2026 census\n',
  'slug': 'ncb-delimitation',
  'sort_order': 16,
  'summary': 'Statutory high-powered body under successive Delimitation Acts — orders final; seat '
             'freeze till post-2026 census.',
  'title': 'Delimitation Commission of India',
  'visual_blocks': [{'events': [{'detail': 'Early post-Constitution delimitation.',
                                 'id': 'e1',
                                 'label': 'First Commission',
                                 'year': 1952},
                                {'detail': 'Orders around 2008.',
                                 'id': 'e2',
                                 'label': 'Kuldip Singh Commission',
                                 'year': 2002},
                                {'detail': 'Justice R.P. Desai — order 2022.',
                                 'id': 'e3',
                                 'label': 'J&K panel',
                                 'year': 2020},
                                {'detail': 'Seat-total readjustment politics.',
                                 'id': 'e4',
                                 'label': 'Freeze ends (after census)',
                                 'year': 2026}],
                     'id': 'delim-timeline',
                     'title': 'Delimitation commissions',
                     'type': 'timeline'},
                    {'body': 'Delimitation orders = force of law + **cannot be questioned in '
                             'court** + House cannot modify. Contrast with ordinary EC '
                             'administrative acts.',
                     'id': 'delim-trap',
                     'title': 'Finality',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [['North Eastern Council Act, 1971', 'In force 1 Aug 1972; repealed 1970 Act.'],
               ['NEC Amendment Act, 2002', 'Sikkim included; Regional Planning Body role.']],
  'body': '## Type of body\n'
          '\n'
          '**Statutory advisory / Regional Planning Body** (since 2002).\n'
          '\n'
          '## Legal basis & year\n'
          '\n'
          '- **Basis:** North Eastern Council Act, **1971** (in force 1 Aug **1972**); Amendment '
          'Act **2002**\n'
          '- **Established:** **1972**\n'
          '\n'
          '## Parent ministry\n'
          '\n'
          '**Ministry of Development of North Eastern Region (DONER)**\n'
          '\n'
          '## Composition\n'
          '\n'
          'Governors + CMs of **8** States (Arunachal, Assam, Manipur, Meghalaya, Mizoram, '
          'Nagaland, Sikkim, Tripura); 3 Presidential nominees; optional Union Minister; Chair & '
          'optional VC nominated by President\n'
          '\n'
          '## Appointment\n'
          '\n'
          'President nominates Chair/VC/extra members; since **July 2018** — Union **Home Minister '
          '= ex-officio Chair**; **DONER Minister = ex-officio VC**\n'
          '\n'
          '## Tenure\n'
          '\n'
          'As per nomination / ex-officio offices\n'
          '\n'
          '## Removal\n'
          '\n'
          'As per Act / office held\n'
          '\n'
          '## Powers\n'
          '\n'
          'Formulate regional plans (priority to multi-State schemes); review implementation & '
          'security/public order; powers delegated by Centre\n'
          '\n'
          '## Functions\n'
          '\n'
          'Regional planning, coordination, development review for NE\n'
          '\n'
          '## Jurisdiction\n'
          '\n'
          'Eight NE States; HQ **Shillong**\n'
          '\n'
          '## Independence & safeguards\n'
          '\n'
          'Statutory regional forum under Centre’s DONER ecosystem\n'
          '\n'
          '## Reporting structure\n'
          '\n'
          'To Central Government / as Act provides; planning interface with States\n'
          '\n'
          '## Important committees\n'
          '\n'
          'NEC Revitalisation Committee 2003–04 (P.P. Shrivastav)\n'
          '\n'
          '## Recent reforms\n'
          '\n'
          '2002 planning-body upgrade + Sikkim; 2018 HM/DONER chair pattern\n'
          '\n'
          '## Current affairs relevance\n'
          '\n'
          'NE connectivity, Act East, security–development balance in Council reviews\n'
          '\n'
          '## Frequently asked UPSC themes\n'
          '\n'
          '8 States; DONER; HM Chair since 2018; regional planning vs Zonal Councils\n'
          '\n'
          '## Common Prelims traps\n'
          '\n'
          '- Trap: NEC is constitutional like Interstate Council — **statutory**.\n'
          '- Trap: only 7 States — **Sikkim included (2002)** → **8**.\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          'Regional institutions for asymmetric development — NEC as planning & security review '
          'forum.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- NEC Act 1971 · 1972 · DONER\n'
          '- 8 States · Shillong\n'
          '- HM Chair / DONER VC (since 2018)\n',
  'slug': 'ncb-nec',
  'sort_order': 17,
  'summary': 'Statutory regional planning body (NEC Act 1971; amd. 2002) — DONER; HM Chair since '
             '2018.',
  'title': 'North Eastern Council',
  'visual_blocks': [{'id': 'nec-tree',
                     'root': {'children': [{'children': [{'detail': 'Governors + CMs as members',
                                                          'id': 'states',
                                                          'label': '8 NE States'}],
                                            'detail': 'HM Chair · DONER VC · 8 States',
                                            'id': 'nec',
                                            'label': 'NEC (Regional Planning Body)'}],
                              'id': 'doner',
                              'label': 'DONER Ministry'},
                     'title': 'NEC placement',
                     'type': 'tree'},
                    {'body': '**1971 Act / 1972 start · 2002 Sikkim+planning · 2018 HM Chair**. HQ '
                             'Shillong.',
                     'id': 'nec-tip',
                     'title': 'Memory',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [('Classification lens',
                'First ask: Constitution Part? Act of Parliament? Cabinet/executive order?'),
               ('Function lens',
                'Advisory / rights commission / transparency / vigilance / investigation / '
                'regulator / planning.')],
  'body': '## Why taxonomy first\n'
          '\n'
          'UPSC loves **type questions**. Before memorising tenure, lock the **creation source** '
          'and **function family**.\n'
          '\n'
          '## Constitutional vs Statutory vs Executive\n'
          '\n'
          '| Type | Created by | Examples in polity |\n'
          '|------|------------|-------------------|\n'
          '| Constitutional | Constitution | ECI, UPSC, FC, CAG, NHRC is **NOT** this |\n'
          '| Statutory | Act of Parliament/State | NHRC, CIC, CVC (2003), NIA, Lokpal, NDMA, NEC, '
          'BCI |\n'
          '| Executive | Cabinet resolution / govt order | **NITI Aayog**, **CBI** (org), **Law '
          'Commission** |\n'
          '\n'
          '## Advisory vs Regulatory vs Investigative\n'
          '\n'
          '- **Advisory / think-tank / planning:** NITI, Law Commission, NEC (regional planning), '
          'NDMA (policy apex)\n'
          '- **Rights / grievance commissions:** NHRC, SHRC, NCW, NCPCR, NCM\n'
          '- **Transparency:** CIC, SIC\n'
          '- **Vigilance / ombudsman:** CVC, Lokpal/Lokayukta\n'
          '- **Investigative agencies:** CBI, NIA\n'
          '- **Professional regulator:** BCI\n'
          '- **Spatial/electoral boundaries:** Delimitation Commission\n'
          '\n'
          '## Mnemonic — families\n'
          '\n'
          '**NITI thinks; Rights watch; RTI reveals; Vigilance & probe punish; Law shapes; NEC '
          'plans East.**\n'
          '\n'
          'Or: **T-R-I-V-I-A** — Think-tank, Rights, Information, Vigilance/Investigation, '
          'Institutional maps, All tables.\n'
          '\n'
          '## Exam in 5 minutes\n'
          '\n'
          '- NITI & Law Commission & CBI(org) ≠ statutory-in-the-NHRC-sense\n'
          '- CVC was executive (1964) → statutory (2003)\n'
          '- NCM was executive (1978) → statutory (1993)\n',
  'slug': 'ncb-taxonomy',
  'sort_order': 18,
  'summary': 'Constitutional vs statutory vs executive; advisory vs regulatory vs investigative — '
             'the classification map for Part VIII.',
  'title': 'Body Taxonomy',
  'visual_blocks': [{'id': 'tax-tree',
                     'root': {'children': [{'detail': 'NHRC, CIC, CVC, NIA, Lokpal, NDMA, BCI, '
                                                      'NEC…',
                                            'id': 'stat',
                                            'label': 'Statutory (Act)'},
                                           {'detail': 'NITI, Law Commission, CBI organisation',
                                            'id': 'exec',
                                            'label': 'Executive'}],
                              'id': 'ncb',
                              'label': 'Non-constitutional bodies'},
                     'title': 'Creation source map',
                     'type': 'tree'},
                    {'columns': [{'heading': 'Constitutional',
                                  'id': 'c',
                                  'points': ['Text of Constitution',
                                             'ECI, UPSC, CAG, FC',
                                             'Strongest formal status']},
                                 {'heading': 'Statutory',
                                  'id': 's',
                                  'points': ['Act of Legislature',
                                             'NHRC, CIC, NIA, Lokpal',
                                             'Independence varies by Act']},
                                 {'heading': 'Executive',
                                  'id': 'e',
                                  'points': ['Cabinet/govt order',
                                             'NITI, Law Commission',
                                             'Easiest to restructure']}],
                     'id': 'tax-compare',
                     'title': 'Constitutional vs Statutory vs Executive',
                     'type': 'comparison'},
                    {'body': '**T**hink-tank (NITI) · **R**ights commissions · **I**nformation '
                             '(CIC/SIC) · **V**igilance/Investigation · **I**nstitutional maps · '
                             '**A**ll master tables.',
                     'id': 'tax-tip',
                     'title': 'Memory aid · T-R-I-V-I-A',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [('PHRA 1993', 'NHRC + SHRC framework.'),
               ('Group-specific Acts', 'NCW 1990, NCM 1992, CPCR 2005.')],
  'body': '## Human rights architecture\n'
          '\n'
          '**NHRC** is the national umbrella NHRI; **SHRC** mirrors it for State/Concurrent lists. '
          'Group commissions (NCW, NCPCR, NCM) sit on **subject-specific** mandates — several are '
          '**ex-officio** on NHRC.\n'
          '\n'
          '## NHRC vs SHRC\n'
          '\n'
          '| Point | NHRC | SHRC |\n'
          '|-------|------|------|\n'
          '| Composition | Chair + 5 (+7 ex-officio) | Chair + 2 |\n'
          '| Appoints | President | Governor |\n'
          '| Removes | President | **President** (not Governor) |\n'
          '| Jurisdiction | Broader national HR | List II & III |\n'
          '| Reports | Parliament | State Legislature |\n'
          '\n'
          '## NCW vs NCPCR vs NCM\n'
          '\n'
          '| | NCW | NCPCR | NCM |\n'
          '|-|-----|-------|-----|\n'
          '| Act | 1990 (set up 1992) | CPCR 2005 (2007) | 1992 (1993) |\n'
          '| Parent | MWCD | MWCD | Minority Affairs |\n'
          '| Target | Women | Children (<18) | Notified minorities |\n'
          '| Civil court powers | Yes | Yes | Yes |\n'
          '\n'
          '## Ex-officio bridge\n'
          '\n'
          'NHRC ex-officio includes chairs of NCM, NCSC, NCST, NCW, NCBC, NCPCR + CCPD — **rights '
          'ecosystem linkage**.\n'
          '\n'
          '## Prelims traps\n'
          '\n'
          '- SHRC removed by Governor — **False**\n'
          '- NCM under MHA — **Minority Affairs**\n'
          '- NCPCR child age casually 14 — Act uses **under 18**\n',
  'slug': 'ncb-rights-compare',
  'sort_order': 19,
  'summary': 'NHRC vs SHRC and NCW vs NCPCR vs NCM — appointment, removal, jurisdiction, parent '
             'ministries.',
  'title': 'Rights Institutions Compare',
  'visual_blocks': [{'columns': [{'heading': 'NHRC',
                                  'id': 'n',
                                  'points': ['President appoints & removes',
                                             'Chair+5 + ex-officio',
                                             'National mandate',
                                             'Report → Parliament']},
                                 {'heading': 'SHRC',
                                  'id': 's',
                                  'points': ['Governor appoints; President removes',
                                             'Chair+2',
                                             'List II/III only',
                                             'Report → State Legislature']}],
                     'id': 'rights-nhrc-shrc',
                     'title': 'NHRC vs SHRC',
                     'type': 'comparison'},
                    {'columns': [{'heading': 'NCW',
                                  'id': 'w',
                                  'points': ['Women', 'MWCD', 'Act 1990 / 1992']},
                                 {'heading': 'NCPCR',
                                  'id': 'c',
                                  'points': ['Children <18', 'MWCD', '2005/2007 + RTE/POCSO/JJ']},
                                 {'heading': 'NCM',
                                  'id': 'm',
                                  'points': ['Minorities',
                                             'Minority Affairs',
                                             '1992/1993; Jains 2014']}],
                     'id': 'rights-trio',
                     'title': 'NCW vs NCPCR vs NCM',
                     'type': 'comparison'},
                    {'body': 'SHRC: **Governor appoints, President removes**. Do not apply the SIC '
                             'pattern here.',
                     'id': 'rights-trap',
                     'title': 'Highest trap',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [('RTI Act, 2005', 'Creates CIC and SICs.'),
               ('RTI Amendment, 2019', 'Term & salary prescribed by Central Government.')],
  'body': '## Twin design\n'
          '\n'
          'CIC and SIC are **mirrors**: same RTI powers/penalties; different appointing '
          'authorities and jurisdictions.\n'
          '\n'
          '## Comparison table\n'
          '\n'
          '| Point | CIC | SIC |\n'
          '|-------|-----|-----|\n'
          '| Appoints | President | Governor |\n'
          '| Panel | PM + LoP(LS) + Cabinet Minister | CM + LoP(Assembly) + State Minister |\n'
          '| Removes | President | Governor |\n'
          '| Jurisdiction | Central/UT authorities | State authorities |\n'
          '| Tenure | Centre-prescribed / age 65 | Same idea post-2019 |\n'
          '| Penalty | ₹250/day ≤ ₹25,000 | Same |\n'
          '\n'
          '## 2019 amendment — what changed\n'
          '\n'
          'Earlier narrative: fixed tenure & CEC/EC-like salary parity. **2019** — Central '
          'Government prescribes term & conditions (autonomy debate for Mains).\n'
          '\n'
          '## Trap vs SHRC\n'
          '\n'
          'SIC removal = **Governor**. SHRC removal = **President**. Never swap.\n',
  'slug': 'ncb-cic-sic',
  'sort_order': 20,
  'summary': 'RTI twin commissions — appointment, removal, tenure after 2019, jurisdiction, and '
             'identical penalty logic.',
  'title': 'CIC vs SIC',
  'visual_blocks': [{'columns': [{'heading': 'CIC',
                                  'id': 'cic',
                                  'points': ['President appoints/removes',
                                             'Central/UT public authorities',
                                             'Report → Parliament',
                                             '2019: Centre sets term/salary']},
                                 {'heading': 'SIC',
                                  'id': 'sic',
                                  'points': ['Governor appoints/removes',
                                             'State public authorities',
                                             'Report → Legislature',
                                             'Same penalty ceiling']}],
                     'id': 'cic-sic-compare',
                     'title': 'CIC vs SIC master',
                     'type': 'comparison'},
                    {'id': 'cic-sic-flow',
                     'root': 'ask',
                     'steps': [{'id': 'ask',
                                'label': 'Whose public authority?',
                                'options': [{'label': 'Central / UT', 'next': 'cic'},
                                            {'label': 'State', 'next': 'sic'}]},
                               {'detail': 'Second appeal / complaint under RTI',
                                'id': 'cic',
                                'label': 'Go to CIC'},
                               {'detail': 'State RTI second appeal / complaint',
                                'id': 'sic',
                                'label': 'Go to SIC'}],
                     'title': 'Which commission?',
                     'type': 'flowchart'},
                    {'body': 'SIC ≠ SHRC. Only SHRC among State rights bodies is removed by the '
                             '**President**.',
                     'id': 'cic-sic-trap',
                     'title': 'Removal swap trap',
                     'tone': 'trap',
                     'type': 'callout'}]},
 {'articles': [('Anti-corruption & security stack',
                'Transparency (CIC) ≠ Vigilance (CVC) ≠ Investigation (CBI/NIA) ≠ Ombudsman '
                '(Lokpal).')],
  'body': '## Five different jobs\n'
          '\n'
          '| Body | Core job | Parent | Consent / reach |\n'
          '|------|----------|--------|-----------------|\n'
          '| CIC | RTI adjudication | Personnel | Central/UT authorities |\n'
          '| CVC | Vigilance / PC Act superintendence | Personnel | Central vigilance lane |\n'
          '| CBI | Investigation (corruption/econ/special) | Personnel | **State consent** (DSPE) '
          '|\n'
          '| Lokpal | Corruption ombudsman oversight | Personnel | Public servants as in Act |\n'
          '| NIA | Scheduled terror/security offences | **MHA** | Concurrent + extraterritorial '
          'design |\n'
          '\n'
          '## Decision cues\n'
          '\n'
          '1. **RTI denial/delay?** → CIC/SIC\n'
          '2. **Vigilance advice / PC Act supervision?** → CVC\n'
          '3. **Need a probe agency for corruption/complex crime?** → CBI (consent!)\n'
          '4. **Complaint against high public servants under Lokpal Act?** → Lokpal\n'
          '5. **Terror / scheduled security offence?** → NIA\n'
          '\n'
          '## Mains line\n'
          '\n'
          'India’s accountability architecture is **layered but overlapping** — clarity of mandate '
          '+ independence + federal consent is the evaluative triangle.\n',
  'slug': 'ncb-accountability',
  'sort_order': 21,
  'summary': 'CIC vs CVC vs CBI vs Lokpal vs NIA — mandate, control, consent, and ‘which agency?’ '
             'decision tree.',
  'title': 'Accountability Architecture',
  'visual_blocks': [{'columns': [{'heading': 'CIC',
                                  'id': 'cic',
                                  'points': ['Transparency', 'RTI appeals', 'Penalties on PIOs']},
                                 {'heading': 'CVC',
                                  'id': 'cvc',
                                  'points': ['Vigilance apex',
                                             'PC Act lane',
                                             'Supervises CBI (PC)']},
                                 {'heading': 'CBI',
                                  'id': 'cbi',
                                  'points': ['Investigator', 'DSPE powers', 'State consent']},
                                 {'heading': 'Lokpal',
                                  'id': 'lok',
                                  'points': ['Ombudsman',
                                             'High public servants',
                                             'Can direct probes']},
                                 {'heading': 'NIA',
                                  'id': 'nia',
                                  'points': ['Counter-terror', 'Schedule offences', 'MHA']}],
                     'id': 'acc-matrix',
                     'title': 'Mandate matrix',
                     'type': 'comparison'},
                    {'id': 'acc-flow',
                     'root': 'q',
                     'steps': [{'id': 'q',
                                'label': 'What is the problem?',
                                'options': [{'label': 'RTI / transparency', 'next': 'rti'},
                                            {'label': 'Corruption complaint (ombudsman)',
                                             'next': 'lok'},
                                            {'label': 'Need investigation', 'next': 'inv'}]},
                               {'detail': 'Central/UT → CIC; State → SIC',
                                'id': 'rti',
                                'label': 'CIC or SIC'},
                               {'detail': 'As per Lokpal Act / State law',
                                'id': 'lok',
                                'label': 'Lokpal / Lokayukta'},
                               {'id': 'inv',
                                'label': 'Terror/scheduled?',
                                'options': [{'label': 'Yes — NIA', 'next': 'nia'},
                                            {'label': 'No — CBI/police (+ CVC if PC Act)',
                                             'next': 'cbi'}]},
                               {'detail': 'MHA · Schedule offences', 'id': 'nia', 'label': 'NIA'},
                               {'detail': 'Check State consent',
                                'id': 'cbi',
                                'label': 'CBI (+ CVC supervision in PC Act)'}],
                     'title': 'Which agency?',
                     'type': 'flowchart'},
                    {'body': 'CIC, CVC, CBI, Lokpal → **Personnel**. NIA → **Home**. That single '
                             'split clears many MCQs.',
                     'id': 'acc-tip',
                     'title': 'Parent cue',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [('Planning Commission (1950)', 'Executive body — plan approval culture.'),
               ('NITI Aayog (2015)',
                'Executive think-tank — cooperative & competitive federalism.')],
  'body': '## Big shift\n'
          '\n'
          '| Dimension | Planning Commission | NITI Aayog |\n'
          '|-----------|---------------------|------------|\n'
          '| Created | Executive resolution | Executive resolution |\n'
          '| Role | Plan formulation + allocation culture | Policy think-tank + federal forum |\n'
          '| Federal style | Top-down / Centre→State | Bottom-up partnership |\n'
          '| Funds | Strong plan-fund leverage (historical) | No Super-Cabinet allocator role |\n'
          '| States | Often petitioners | Governing Council partners |\n'
          '| NDC | Plan endorsement forum | Powers talked of shifting to NITI GC (incomplete) |\n'
          '\n'
          '## Mains value\n'
          '\n'
          'Use NITI to discuss **cooperative federalism** (Governing Council) and **competitive '
          'federalism** (indices) — and critique soft-power limits without fiscal teeth.\n'
          '\n'
          '## Prelims\n'
          '\n'
          'Both are **non-constitutional, non-statutory**. Replacing PC with NITI did **not** '
          'constitutionalise planning.\n',
  'slug': 'ncb-niti-vs-pc',
  'sort_order': 22,
  'summary': 'From command-and-control plan allocation to think-tank federal partnership — '
             'structure, funds, and NDC debate.',
  'title': 'NITI vs Planning Commission',
  'visual_blocks': [{'columns': [{'heading': 'Planning Commission',
                                  'id': 'pc',
                                  'points': ['1950 executive body',
                                             'Command-and-control image',
                                             'Plan approval leverage',
                                             'First ARC: ‘Super Cabinet’ critique']},
                                 {'heading': 'NITI Aayog',
                                  'id': 'niti',
                                  'points': ['2015 executive body',
                                             'Think-tank + Team India',
                                             'Cooperative + competitive federalism',
                                             'No classic plan-fund Super Cabinet']}],
                     'id': 'niti-pc',
                     'title': 'Planning Commission vs NITI',
                     'type': 'comparison'},
                    {'body': 'Same **legal type** (executive), different **political economy of '
                             'federalism**.',
                     'id': 'niti-pc-tip',
                     'title': 'One-liner',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [('Delimitation vs ECI',
                'Commission delimits; EC conducts elections & is typically a member.'),
               ('DM Act stack', 'NDMA–SDMA–DDMA–NDRF.')],
  'body': '## Delimitation Commission vs Election Commission\n'
          '\n'
          '| Point | Delimitation Commission | Election Commission |\n'
          '|-------|-------------------------|---------------------|\n'
          '| Status | Statutory (when Act made) | **Constitutional** |\n'
          '| Job | Draw/readjust constituencies | Conduct elections; electoral roll etc. |\n'
          '| Orders | Force of law; **not justiciable** | Electoral process under Constitution/RP '
          'Act |\n'
          '| Membership link | CEC/EC usually **member** | Separate constitutional body |\n'
          '\n'
          '## NDMA institutional framework\n'
          '\n'
          '**NDMA (PM)** → **SDMA (CM)** → **DDMA (Collector)** + **NDRF** under NDMA '
          'superintendence.\n'
          '\n'
          '## Parent ministry cheat sheet\n'
          '\n'
          '| Ministry | Bodies |\n'
          '|----------|--------|\n'
          '| Planning | NITI Aayog |\n'
          '| Home | NHRC, NIA, NDMA |\n'
          '| MWCD | NCW, NCPCR |\n'
          '| Minority Affairs | NCM |\n'
          '| Personnel | CIC, CVC, CBI, Lokpal |\n'
          '| Law & Justice | BCI, Law Commission, Delimitation |\n'
          '| DONER | NEC |\n'
          '| State | SHRC, SIC (functional) |\n'
          '\n'
          'SHRC/SIC are State-facing but created under Central statutes.\n',
  'slug': 'ncb-institutional-maps',
  'sort_order': 23,
  'summary': 'Delimitation vs EC, NDMA stack, and parent-ministry map for all Part VIII bodies.',
  'title': 'Institutional Maps',
  'visual_blocks': [{'columns': [{'heading': 'Delimitation Commission',
                                  'id': 'd',
                                  'points': ['Statutory under Delimitation Acts',
                                             'Boundary/seat orders',
                                             'Orders final / not justiciable',
                                             'Freeze politics till post-2026 census']},
                                 {'heading': 'Election Commission',
                                  'id': 'e',
                                  'points': ['Constitutional (Art. 324)',
                                             'Conduct free & fair elections',
                                             'CEC/EC sit on Delimitation panel',
                                             'Not the delimiting authority itself']}],
                     'id': 'maps-delim-ec',
                     'title': 'Delimitation vs EC',
                     'type': 'comparison'},
                    {'id': 'maps-ndma',
                     'root': {'children': [{'children': [{'id': 'ddma',
                                                          'label': 'DDMA — Collector Chair'}],
                                            'id': 'sdma',
                                            'label': 'SDMA — CM Chair'},
                                           {'detail': 'Response force',
                                            'id': 'ndrf',
                                            'label': 'NDRF'}],
                              'id': 'ndma',
                              'label': 'NDMA — PM Chair'},
                     'title': 'Disaster management stack',
                     'type': 'tree'},
                    {'body': '**Home** holds rights+security+disaster (NHRC/NIA/NDMA). '
                             '**Personnel** holds transparency+vigilance+probe+ombudsman '
                             '(CIC/CVC/CBI/Lokpal). **MWCD** = women+child. **DONER** = NEC.',
                     'id': 'maps-ministry',
                     'title': 'Parent ministry mnemonic',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [('Laxmikanth Part VIII', 'Ch.56–72 non-constitutional bodies.')],
  'body': '## Master comparison (scan)\n'
          '\n'
          '| Body | Type | Year/Act | Parent |\n'
          '|------|------|----------|--------|\n'
          '| NITI | Executive | 2015 resolution | Planning |\n'
          '| NHRC | Statutory | PHRA 1993 | Home |\n'
          '| SHRC | Statutory | PHRA 1993 | State / President removes |\n'
          '| NCW | Statutory | 1990/1992 | MWCD |\n'
          '| NCPCR | Statutory | 2005/2007 | MWCD |\n'
          '| NCM | Statutory | 1992/1993 | Minority Affairs |\n'
          '| CIC | Statutory | RTI 2005 | Personnel |\n'
          '| SIC | Statutory | RTI 2005 | State (Governor) |\n'
          '| CVC | Statutory | 2003 (exec 1964) | Personnel |\n'
          '| CBI | Executive+DSPE | 1963 | Personnel |\n'
          '| Lokpal | Statutory | 2013 | Personnel |\n'
          '| NIA | Statutory | 2008/2009 | Home |\n'
          '| NDMA | Statutory | 2005/2006 | Home |\n'
          '| BCI | Statutory | Advocates 1961 | Law & Justice |\n'
          '| Law Commission | Executive | MoLJ order | Law & Justice |\n'
          '| Delimitation | Statutory | Delimitation Acts | Law & Justice |\n'
          '| NEC | Statutory | 1971/1972 | DONER |\n'
          '\n'
          '## Legal basis cheat sheet\n'
          '\n'
          '- **Resolution/order:** NITI, Law Commission, CBI(org)\n'
          '- **PHRA:** NHRC, SHRC\n'
          '- **RTI:** CIC, SIC\n'
          '- **Special Acts:** NCW, NCPCR, NCM, CVC, Lokpal, NIA, NDMA, BCI, NEC, Delimitation '
          'Acts\n'
          '\n'
          '## Appointment & removal (high-yield)\n'
          '\n'
          '| Body | Appoints | Removes |\n'
          '|------|----------|---------|\n'
          '| NHRC | President | President (+SC inquiry path) |\n'
          '| SHRC | Governor | **President** |\n'
          '| CIC | President | President |\n'
          '| SIC | Governor | Governor |\n'
          '| CVC | President | President |\n'
          '| CBI Director | Centre on PM+LoP+CJI panel | Tenure protections / rules |\n'
          '| Lokpal | Selection committee | As per Act |\n'
          '\n'
          '## Powers & functions matrix (one line each)\n'
          '\n'
          '- NITI — advise & federal platform\n'
          '- NHRC/SHRC — inquire HR (recommendatory)\n'
          '- NCW/NCPCR/NCM — group rights + civil court powers\n'
          '- CIC/SIC — RTI appeals + penalties\n'
          '- CVC — vigilance + CBI PC-Act superintendence\n'
          '- CBI/NIA — investigate\n'
          '- Lokpal — corruption ombudsman\n'
          '- NDMA — disaster policy apex\n'
          '- BCI — regulate advocates\n'
          '- LCI — recommend law reform\n'
          '- Delimitation — final boundary orders\n'
          '- NEC — NE regional planning\n'
          '\n'
          '## One-page final summary\n'
          '\n'
          'Classify → parent ministry → appoint/remove → one core power → one trap. Then run the '
          'accountability decision tree and rights comparison once.\n',
  'slug': 'ncb-master-tables',
  'sort_order': 24,
  'summary': 'All-bodies master table, legal-basis sheet, appointment/removal, ministries, and '
             'powers matrix — final revision pack.',
  'title': 'Master Tables & Cheat Sheets',
  'visual_blocks': [{'columns': [{'heading': 'Executive',
                                  'id': 'exec',
                                  'points': ['NITI Aayog', 'Law Commission', 'CBI (organisation)']},
                                 {'heading': 'Statutory (sample)',
                                  'id': 'stat',
                                  'points': ['NHRC/SHRC',
                                             'CIC/SIC/CVC',
                                             'NIA/Lokpal/NDMA',
                                             'BCI/NEC/Delimitation',
                                             'NCW/NCPCR/NCM']}],
                     'id': 'master-type',
                     'title': 'Type cheat sheet',
                     'type': 'comparison'},
                    {'columns': [{'heading': 'Home',
                                  'id': 'home',
                                  'points': ['NHRC', 'NIA', 'NDMA']},
                                 {'heading': 'Personnel',
                                  'id': 'pers',
                                  'points': ['CIC', 'CVC', 'CBI', 'Lokpal']},
                                 {'heading': 'Others',
                                  'id': 'other',
                                  'points': ['Planning: NITI',
                                             'MWCD: NCW/NCPCR',
                                             'Minority Affairs: NCM',
                                             'Law: BCI/LCI/Delim',
                                             'DONER: NEC']}],
                     'id': 'master-ministry',
                     'title': 'Parent ministry clusters',
                     'type': 'comparison'},
                    {'body': 'For each body recite: **Type · Act/Year · Ministry · Who '
                             'appoints/removes · One power · One trap**. Finish with SHRC removal '
                             '+ CBI consent + NITI type + Delimitation finality.',
                     'id': 'master-final',
                     'title': 'One-page drill',
                     'tone': 'tip',
                     'type': 'callout'}]},
 {'articles': [('Prelims themes',
                'Type of body, appointment panels, tenure changes, consent, finality.'),
               ('Mains themes',
                'Federalism (NITI/NIA/CBI), RTI autonomy, anti-corruption architecture, disaster '
                'federalism.')],
  'body': '## PYQ themes (recurring)\n'
          '\n'
          '1. Is X constitutional / statutory / executive?\n'
          '2. Appointment committee composition (NHRC, CIC, CVC, CBI Director, Lokpal)\n'
          '3. Who removes SHRC / SIC members?\n'
          '4. RTI 2019 — term & salary\n'
          '5. CBI State consent / DSPE\n'
          '6. NITI vs Planning Commission\n'
          '7. Delimitation order finality & seat freeze\n'
          '8. NDMA chair (PM)\n'
          '9. NIA 2019 schedule expansion\n'
          '10. Notified minorities / Jains 2014\n'
          '\n'
          '## Frequently confused pairs\n'
          '\n'
          '- SHRC removal vs SIC removal\n'
          '- CBI vs NIA (ministry + mandate + consent)\n'
          '- CVC vs Lokpal vs CBI\n'
          '- NITI vs statutory commissions\n'
          '- Delimitation Commission vs ECI\n'
          '- NCW vs NCM parent ministries\n'
          '\n'
          '## Memory tricks\n'
          '\n'
          '- **Personnel pack:** CIC–CVC–CBI–Lokpal\n'
          '- **Home pack:** NHRC–NIA–NDMA\n'
          '- **MWCD twins:** NCW + NCPCR\n'
          '- **President removes SHRC** (exception memory)\n'
          '- **NITI = neither–nor** (not constitutional, not statutory)\n'
          '\n'
          '## Exam in 5 Minutes (chapter)\n'
          '\n'
          '1. Taxonomy table once\n'
          '2. Personnel pack + Home pack\n'
          '3. NHRC vs SHRC (removal!)\n'
          '4. CIC/SIC + 2019\n'
          '5. CBI consent + NIA schedule\n'
          '6. NITI neither-nor + Delimitation finality + PM chairs NDMA\n'
          '\n'
          '## Mains micro-quotes\n'
          '\n'
          '- Cooperative + competitive federalism (NITI)\n'
          '- Paris Principles / recommendatory NHRI (NHRC)\n'
          '- Transparency vs independence (RTI 2019)\n'
          '- Consent vs national investigation (CBI/NIA)\n'
          '- Disaster federalism (NDMA stack)\n',
  'slug': 'ncb-exam-pack',
  'sort_order': 25,
  'summary': 'PYQ themes, confused pairs, mnemonics, and a chapter-level 5-minute drill for '
             'Prelims and Mains.',
  'title': 'PYQs, Traps & Exam in 5 Minutes',
  'visual_blocks': [{'body': '1) NITI statutory  2) SHRC removed by Governor  3) CBI under MHA & '
                             'no consent needed  4) CIC still CEC-salary parity  5) Delimitation '
                             'orders appealable',
                     'id': 'exam-traps',
                     'title': 'Top 5 traps',
                     'tone': 'trap',
                     'type': 'callout'},
                    {'body': '**CIC + CVC + CBI + Lokpal** live under **Personnel**. **NHRC + NIA '
                             '+ NDMA** under **Home**.',
                     'id': 'exam-mnemonic',
                     'title': 'Memory aid · Personnel pack',
                     'tone': 'tip',
                     'type': 'callout'},
                    {'body': 'Neither-nor NITI → President-removes-SHRC → RTI-2019 → CBI-consent → '
                             'NIA-2019 → Delimitation-final → PM-NDMA. Then Personnel vs Home '
                             'packs.',
                     'id': 'exam-5min',
                     'title': 'Exam in 5 Minutes',
                     'tone': 'note',
                     'type': 'callout'}]}]

EDGES = [('non-constitutional-bodies', 'parent', 'ncb-niti-aayog'),
 ('non-constitutional-bodies', 'parent', 'ncb-nhrc'),
 ('non-constitutional-bodies', 'parent', 'ncb-shrc'),
 ('non-constitutional-bodies', 'parent', 'ncb-ncw'),
 ('non-constitutional-bodies', 'parent', 'ncb-ncpcr'),
 ('non-constitutional-bodies', 'parent', 'ncb-ncm'),
 ('non-constitutional-bodies', 'parent', 'ncb-cic'),
 ('non-constitutional-bodies', 'parent', 'ncb-sic'),
 ('non-constitutional-bodies', 'parent', 'ncb-cvc'),
 ('non-constitutional-bodies', 'parent', 'ncb-cbi'),
 ('non-constitutional-bodies', 'parent', 'ncb-lokpal'),
 ('non-constitutional-bodies', 'parent', 'ncb-nia'),
 ('non-constitutional-bodies', 'parent', 'ncb-ndma'),
 ('non-constitutional-bodies', 'parent', 'ncb-bci'),
 ('non-constitutional-bodies', 'parent', 'ncb-law-commission'),
 ('non-constitutional-bodies', 'parent', 'ncb-delimitation'),
 ('non-constitutional-bodies', 'parent', 'ncb-nec'),
 ('non-constitutional-bodies', 'parent', 'ncb-taxonomy'),
 ('non-constitutional-bodies', 'parent', 'ncb-rights-compare'),
 ('non-constitutional-bodies', 'parent', 'ncb-cic-sic'),
 ('non-constitutional-bodies', 'parent', 'ncb-accountability'),
 ('non-constitutional-bodies', 'parent', 'ncb-niti-vs-pc'),
 ('non-constitutional-bodies', 'parent', 'ncb-institutional-maps'),
 ('non-constitutional-bodies', 'parent', 'ncb-master-tables'),
 ('non-constitutional-bodies', 'parent', 'ncb-exam-pack'),
 ('ncb-niti-aayog', 'related', 'ncb-niti-vs-pc'),
 ('ncb-nhrc', 'related', 'ncb-shrc'),
 ('ncb-nhrc', 'related', 'ncb-rights-compare'),
 ('ncb-shrc', 'related', 'ncb-rights-compare'),
 ('ncb-ncw', 'related', 'ncb-rights-compare'),
 ('ncb-ncpcr', 'related', 'ncb-rights-compare'),
 ('ncb-ncm', 'related', 'ncb-rights-compare'),
 ('ncb-cic', 'related', 'ncb-sic'),
 ('ncb-cic', 'related', 'ncb-cic-sic'),
 ('ncb-sic', 'related', 'ncb-cic-sic'),
 ('ncb-cvc', 'related', 'ncb-accountability'),
 ('ncb-cbi', 'related', 'ncb-accountability'),
 ('ncb-lokpal', 'related', 'ncb-accountability'),
 ('ncb-nia', 'related', 'ncb-accountability'),
 ('ncb-cic', 'related', 'ncb-accountability'),
 ('ncb-ndma', 'related', 'ncb-institutional-maps'),
 ('ncb-delimitation', 'related', 'ncb-institutional-maps'),
 ('ncb-nec', 'related', 'ncb-institutional-maps'),
 ('ncb-taxonomy', 'related', 'ncb-master-tables'),
 ('ncb-master-tables', 'related', 'ncb-exam-pack'),
 ('non-constitutional-bodies', 'related', 'federal-system')]

SAMPLE_PYQS = [(2015,
  'NITI Aayog was established by which of the following?',
  'An executive resolution of the Union Cabinet (1 January 2015). It is neither a constitutional '
  'nor a statutory body.',
  ['ncb-niti-aayog', 'ncb-taxonomy', 'ncb-exam-pack']),
 (2017,
  'Consider the removal of the chairperson of a State Human Rights Commission. Who can remove the '
  'chairperson?',
  'Only the President of India (same grounds/process as NHRC), not the Governor — even though the '
  'Governor makes the appointment.',
  ['ncb-shrc', 'ncb-rights-compare', 'ncb-exam-pack']),
 (2019,
  'Which of the following changes were introduced regarding Information Commissioners by the RTI '
  'Amendment Act, 2019?',
  'Term of office and salary/conditions are to be prescribed by the Central Government (ending the '
  'earlier fixed-tenure / CEC-parity scheme in the parent Act narrative).',
  ['ncb-cic', 'ncb-cic-sic', 'ncb-exam-pack']),
 (2021,
  'The Central Bureau of Investigation generally requires which of the following to investigate a '
  'case in a State?',
  'Consent of the State Government under the DSPE Act framework (subject to court directions / UT '
  'exceptions).',
  ['ncb-cbi', 'ncb-accountability', 'ncb-exam-pack']),
 (2022,
  'Orders of the Delimitation Commission are best described as:',
  'Having the force of law, laid before the House but not modifiable by it, and not challengeable '
  'in court.',
  ['ncb-delimitation', 'ncb-institutional-maps', 'ncb-exam-pack']),
 (2018,
  'Who is the ex-officio chairperson of the National Disaster Management Authority?',
  'The Prime Minister of India.',
  ['ncb-ndma', 'ncb-institutional-maps', 'ncb-exam-pack'])]

LANDMARK_CASES = [
    {
        "title": "Vineet Narain v. Union of India",
        "slug": "vineet-narain",
        "parties": "Vineet Narain v. Union of India",
        "year": 1998,
        "court": CaseLaw.Court.SC,
        "summary": (
            "PIL on CBI independence and investigation of high-profile corruption cases."
        ),
        "holding": (
            "Supreme Court issued directions to insulate CBI from executive interference; "
            "impetus for a statutory Central Vigilance Commission."
        ),
        "concept_slugs": ["ncb-cbi", "ncb-cvc", "ncb-accountability", "non-constitutional-bodies"],
    },
    {
        "title": "Vishaka v. State of Rajasthan",
        "slug": "vishaka-guidelines",
        "parties": "Vishaka v. State of Rajasthan",
        "year": 1997,
        "court": CaseLaw.Court.SC,
        "summary": (
            "Workplace sexual harassment — guidelines framed in absence of legislation."
        ),
        "holding": (
            "Laid down binding Vishaka guidelines for prevention of sexual harassment at "
            "workplace until parliamentary law."
        ),
        "concept_slugs": ["ncb-ncw", "ncb-rights-compare", "non-constitutional-bodies"],
    },
]


class Command(BaseCommand):
    help = "Seed Non-Constitutional Bodies chapter (Laxmikanth Part VIII, Ch.56–72)."

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
                "title": "Non-Constitutional Bodies",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Part VIII, Ch. 56–72 (pp. 667–760+)",
                "summary": (
                    "Visual revision of Part VIII — NITI Aayog through North Eastern Council, "
                    "with taxonomy, comparisons, and exam packs."
                ),
                "is_published": True,
            },
        )

        section = Section.objects.filter(
            subject=subject, slug="non-constitutional-bodies"
        ).first()
        if section and chapter.section_id != section.id:
            chapter.section = section
            chapter.save(update_fields=["section"])

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Non-Constitutional Bodies",
                "summary": (
                    "Seventeen statutory/executive bodies from Laxmikanth Part VIII — "
                    "classify first, then revise with comparisons and exam traps."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **satellite-network mental model** and scan the **17 bodies**. "
                    "Drill by family: Rights → Transparency → Accountability → Advisory/Legal/Regional. "
                    "Finish with **Taxonomy**, **Master tables**, and **Exam in 5 Minutes**. "
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
            ref="Laxmikanth Part VIII (Ch.56–72)",
            excerpt="Non-Constitutional Bodies — NITI Aayog to North Eastern Council.",
            sort_order=0,
        )

        ncb_slugs = set(by_slug.keys())
        ConceptEdge.objects.filter(
            source__slug__in=ncb_slugs, source__subject=subject
        ).filter(
            target__slug__in=ncb_slugs | {"federal-system"}
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

        self.stdout.write(
            self.style.SUCCESS(
                f"Non-Constitutional Bodies seeded ({academy.slug}): {chapter.title} with "
                f"{len(CLUSTERS) + 1} concepts, {created_edges} new edges, "
                f"{len(LANDMARK_CASES)} cases, {len(SAMPLE_PYQS)} PYQs linked."
            )
        )
