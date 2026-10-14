"""Seed Laxmikanth Part XI / Ch.90 Working of the Constitution (NCRWC) — visual revision."""

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

HUB_SLUG = "working-of-the-constitution"
CHAPTER_SLUG = "working-of-the-constitution"

THEME_PILLARS = [{'id': 'bg',
  'articles': 'Why · Context',
  'label': 'Historical Background',
  'slug': 'woc-background',
  'detail': '50 years’ experience; review working — not rewrite the Constitution.',
  'tone': 'teal'},
 {'id': 'overview',
  'articles': '2000 → 2002',
  'label': 'Commission Overview',
  'slug': 'woc-overview',
  'detail': 'GoI resolution · Venkatachaliah · 11 members · 249 recommendations.',
  'tone': 'olive'},
 {'id': 'areas',
  'articles': '11 + 14',
  'label': 'Areas Reviewed',
  'slug': 'woc-areas-reviewed',
  'detail': 'Study agenda and recommendation themes across the whole Constitution.',
  'tone': 'gold'},
 {'id': 'fr',
  'articles': 'Part III · 300-A',
  'label': 'FR & Property',
  'slug': 'woc-fr-property',
  'detail': 'Widen rights, new FRs, detention reform, Ninth Schedule limits, 300-A recast.',
  'tone': 'orange'},
 {'id': 'dpsp',
  'articles': 'IV · IVA',
  'label': 'DPSP & Duties',
  'slug': 'woc-dpsp-fd',
  'detail': 'Effectuate DPSP; Verma Committee; new Fundamental Duties.',
  'tone': 'terracotta'},
 {'id': 'parl',
  'articles': 'Parl · Exec',
  'label': 'Parliament & Executive',
  'slug': 'woc-parliament-executive',
  'detail': 'Stability devices, MoS cap, Lokpal, Civil Service Boards, RTI.',
  'tone': 'maroon'},
 {'id': 'csr',
  'articles': 'Federal',
  'label': 'Centre–State',
  'slug': 'woc-centre-state',
  'detail': 'Governor, Art. 356, ISC, List III disasters, reserved bills.',
  'tone': 'teal'},
 {'id': 'jud',
  'articles': 'NJC',
  'label': 'Judiciary',
  'slug': 'woc-judiciary',
  'detail': 'National Judicial Commission, retirement ages, pendency goals.',
  'tone': 'olive'},
 {'id': 'elec',
  'articles': 'X · ECI',
  'label': 'Electoral & Parties',
  'slug': 'woc-electoral-parties',
  'detail': 'Criminal bar, MCC statutory, party law, anti-defection redesign.',
  'tone': 'gold'},
 {'id': 'local',
  'articles': '73rd · 74th',
  'label': 'Local Govt & NE',
  'slug': 'woc-local-ne',
  'detail': 'Exclusive functions, SEC–ECI link, Sixth Schedule, Immigration Council.',
  'tone': 'orange'},
 {'id': 'socio',
  'articles': 'Equity',
  'label': 'Socio-Economic',
  'slug': 'woc-socio-economic',
  'detail': 'Reservation statute, tribal areas, bonded labour, women’s empowerment.',
  'tone': 'terracotta'},
 {'id': 'accept',
  'articles': 'Status',
  'label': 'Accepted vs Pending',
  'slug': 'woc-accepted-pending',
  'detail': 'Aligned later reforms vs still-open NCRWC ideas.',
  'tone': 'maroon'},
 {'id': 'compare',
  'articles': '3 Cs',
  'label': 'Comparisons',
  'slug': 'woc-comparisons',
  'detail': 'Sarkaria–Punchhi–NCRWC; amendment vs review; original vs recommended.',
  'tone': 'teal'},
 {'id': 'caf',
  'articles': 'GS-II',
  'label': 'Current Affairs',
  'slug': 'woc-current-affairs',
  'detail': 'Simultaneous polls, CEC law, NJAC memory, lateral entry, federalism.',
  'tone': 'olive'},
 {'id': 'upsc',
  'articles': 'Exam',
  'label': 'UPSC Focus',
  'slug': 'woc-upsc-focus',
  'detail': 'Prelims traps, Mains lines, mnemonics, PYQ themes.',
  'tone': 'gold'},
 {'id': 'sheet',
  'articles': '1 page',
  'label': 'Revision Sheet',
  'slug': 'woc-revision-sheet',
  'detail': 'Cheat sheet, timeline, top-15 recommendations, article map.',
  'tone': 'orange'}]

HUB_VISUAL_BLOCKS = [{'id': 'woc-review-model',
  'type': 'mental_model',
  'title': 'Mental model',
  'metaphor': 'Health check-up',
  'topic_label': 'NCRWC',
  'subject_label': 'Constitution',
  'relation_label': 'Bound by',
  'protects_from': ['Calling NCRWC a constitutional body',
                    'Saying it rewrote the Constitution',
                    'Mixing Venkatachaliah (chair) with Sarkaria (member)',
                    'Treating all 249 as constitutional amendments'],
  'insight': 'NCRWC is a GoI-resolution commission (2000→2002): review working, recommend within '
             'parliamentary democracy and basic structure — Parliament decides.'},
 {'id': 'woc-theme-pillars',
  'type': 'pillars',
  'title': 'Sixteen revision stops',
  'items': [{'id': 'bg',
             'articles': 'Why · Context',
             'label': 'Historical Background',
             'slug': 'woc-background',
             'detail': '50 years’ experience; review working — not rewrite the Constitution.',
             'tone': 'teal'},
            {'id': 'overview',
             'articles': '2000 → 2002',
             'label': 'Commission Overview',
             'slug': 'woc-overview',
             'detail': 'GoI resolution · Venkatachaliah · 11 members · 249 recommendations.',
             'tone': 'olive'},
            {'id': 'areas',
             'articles': '11 + 14',
             'label': 'Areas Reviewed',
             'slug': 'woc-areas-reviewed',
             'detail': 'Study agenda and recommendation themes across the whole Constitution.',
             'tone': 'gold'},
            {'id': 'fr',
             'articles': 'Part III · 300-A',
             'label': 'FR & Property',
             'slug': 'woc-fr-property',
             'detail': 'Widen rights, new FRs, detention reform, Ninth Schedule limits, 300-A recast.',
             'tone': 'orange'},
            {'id': 'dpsp',
             'articles': 'IV · IVA',
             'label': 'DPSP & Duties',
             'slug': 'woc-dpsp-fd',
             'detail': 'Effectuate DPSP; Verma Committee; new Fundamental Duties.',
             'tone': 'terracotta'},
            {'id': 'parl',
             'articles': 'Parl · Exec',
             'label': 'Parliament & Executive',
             'slug': 'woc-parliament-executive',
             'detail': 'Stability devices, MoS cap, Lokpal, Civil Service Boards, RTI.',
             'tone': 'maroon'},
            {'id': 'csr',
             'articles': 'Federal',
             'label': 'Centre–State',
             'slug': 'woc-centre-state',
             'detail': 'Governor, Art. 356, ISC, List III disasters, reserved bills.',
             'tone': 'teal'},
            {'id': 'jud',
             'articles': 'NJC',
             'label': 'Judiciary',
             'slug': 'woc-judiciary',
             'detail': 'National Judicial Commission, retirement ages, pendency goals.',
             'tone': 'olive'},
            {'id': 'elec',
             'articles': 'X · ECI',
             'label': 'Electoral & Parties',
             'slug': 'woc-electoral-parties',
             'detail': 'Criminal bar, MCC statutory, party law, anti-defection redesign.',
             'tone': 'gold'},
            {'id': 'local',
             'articles': '73rd · 74th',
             'label': 'Local Govt & NE',
             'slug': 'woc-local-ne',
             'detail': 'Exclusive functions, SEC–ECI link, Sixth Schedule, Immigration Council.',
             'tone': 'orange'},
            {'id': 'socio',
             'articles': 'Equity',
             'label': 'Socio-Economic',
             'slug': 'woc-socio-economic',
             'detail': 'Reservation statute, tribal areas, bonded labour, women’s empowerment.',
             'tone': 'terracotta'},
            {'id': 'accept',
             'articles': 'Status',
             'label': 'Accepted vs Pending',
             'slug': 'woc-accepted-pending',
             'detail': 'Aligned later reforms vs still-open NCRWC ideas.',
             'tone': 'maroon'},
            {'id': 'compare',
             'articles': '3 Cs',
             'label': 'Comparisons',
             'slug': 'woc-comparisons',
             'detail': 'Sarkaria–Punchhi–NCRWC; amendment vs review; original vs recommended.',
             'tone': 'teal'},
            {'id': 'caf',
             'articles': 'GS-II',
             'label': 'Current Affairs',
             'slug': 'woc-current-affairs',
             'detail': 'Simultaneous polls, CEC law, NJAC memory, lateral entry, federalism.',
             'tone': 'olive'},
            {'id': 'upsc',
             'articles': 'Exam',
             'label': 'UPSC Focus',
             'slug': 'woc-upsc-focus',
             'detail': 'Prelims traps, Mains lines, mnemonics, PYQ themes.',
             'tone': 'gold'},
            {'id': 'sheet',
             'articles': '1 page',
             'label': 'Revision Sheet',
             'slug': 'woc-revision-sheet',
             'detail': 'Cheat sheet, timeline, top-15 recommendations, article map.',
             'tone': 'orange'}]},
 {'id': 'woc-hub-callout',
  'type': 'callout',
  'tone': 'tip',
  'title': 'Exam in 5 Minutes',
  'body': '**2000** set up · **2002** report · Chair **M.N. Venkatachaliah** (ex-CJI) · **11 members** · '
          '**GoI resolution** (not Art.-based) · **249** recs = **58** constitutional + **86** legislative + '
          '**105** executive · bound by **parliamentary democracy + basic structure** · advisory only.'}]

CLUSTERS = [{'title': 'Historical Background',
  'slug': 'woc-background',
  'sort_order': 1,
  'summary': 'Why NCRWC was set up after 50 years: governance capacity, coalition-era stress, and the line '
             'between review and rewrite.',
  'articles': [('Laxmikanth Ch. 90', 'NCRWC — Working of the Constitution (pp. 867–879).'),
               ('Basic Structure', 'Commission bound not to interfere with basic features.')],
  'body': '## Why the Commission?\n'
          '\n'
          '- After **~50 years** of the Constitution, GoI asked: do existing provisions still support '
          '**efficient, smooth, effective governance** and **socio-economic development** of modern India?\n'
          '- If not, recommend **changes** — but only within **parliamentary democracy** and without '
          'touching the **basic structure / basic features**.\n'
          '\n'
          '## Political & constitutional context\n'
          '\n'
          '- Coalition politics and **instability costs** (book notes frequent LS elections from 1989 while '
          'a few PMs ruled most of the first 54 years).\n'
          '- Areas of concern: **criminalisation**, corruption, politician–criminal–bureaucratic nexus, weak '
          'early-warning, justice delays, fiscal stress, educational/health gaps.\n'
          '- Democratic deepening via **73rd/74th** had opened debate — but fault-lines remained.\n'
          '\n'
          '## Previous review efforts (revision map)\n'
          '\n'
          '| Effort | Focus |\n'
          '|--------|--------|\n'
          '| Constituent Assembly (1946–49) | Framing |\n'
          '| Amendments (esp. 42nd, 44th, 73rd, 74th) | Incremental redesign |\n'
          '| Law Commission / Verma (FDs) / other committees | Topic-specific |\n'
          '| **Sarkaria (1983–88)** | Centre–State relations |\n'
          '| **NCRWC (2000–02)** | **Whole working** of the Constitution |\n'
          '| **Punchhi (2007–10)** | Centre–State again (post-NCRWC) |\n'
          '\n'
          '**Mains line:** NCRWC was the first broad **executive review commission** on the *working* of the '
          'Constitution — not a second Constituent Assembly.\n'
          '\n'
          '## Trap\n'
          '\n'
          'Review ≠ rewrite. Role is **recommendatory**; Parliament may accept or reject.',
  'visual_blocks': [{'id': 'woc-bg-timeline',
                     'type': 'timeline',
                     'title': 'Constitutional review efforts',
                     'events': [{'year': '1946–49',
                                 'detail': 'Framed the Constitution — not a ‘review’ body.',
                                 'label': 'Constituent Assembly',
                                 'id': 'e0-constituent-assembly'},
                                {'year': '1983–88',
                                 'detail': 'Centre–State relations only.',
                                 'label': 'Sarkaria Commission',
                                 'id': 'e1-sarkaria-commission'},
                                {'year': '1998–99',
                                 'detail': 'Operationalising Fundamental Duties — later cited by NCRWC.',
                                 'label': 'Verma Committee (FDs)',
                                 'id': 'e2-verma-committee-fds'},
                                {'year': '2000–02',
                                 'detail': 'Whole-Constitution working review; 249 recommendations.',
                                 'label': 'NCRWC',
                                 'id': 'e3-ncrwc'},
                                {'year': '2007–10',
                                 'detail': 'Centre–State relations revisited after NCRWC.',
                                 'label': 'Punchhi Commission',
                                 'id': 'e4-punchhi-commission'}]},
                    {'id': 'woc-bg-callout',
                     'type': 'callout',
                     'tone': 'trap',
                     'title': 'Prelims trap',
                     'body': 'NCRWC does **not** rewrite the Constitution. It reviews **working**, stays '
                             'inside **parliamentary democracy + basic structure**, and only advises.'}]},
 {'title': 'Commission Overview',
  'slug': 'woc-overview',
  'sort_order': 2,
  'summary': 'Identity card: year, GoI resolution, Venkatachaliah, 11 members, TOR, 11 study areas, 18 '
             'concerns, 249 = 58+86+105.',
  'articles': [('2000 / 2002', 'Set up by GoI resolution (2000); report submitted 2002.'),
               ('Chair', 'M.N. Venkatachaliah — former Chief Justice of India.')],
  'body': '## Identity card\n'
          '\n'
          '| Fact | Detail |\n'
          '|------|--------|\n'
          '| Set up | **2000** (GoI **resolution**) |\n'
          '| Report | **2002** |\n'
          '| Legal nature | **Executive** commission — **not** a constitutional body |\n'
          '| Chair | **M.N. Venkatachaliah** (former CJI) |\n'
          '| Size | **11-member** |\n'
          '| Role | Recommendatory / advisory |\n'
          '| Constraint | Parliamentary democracy + **basic structure** |\n'
          '| Output | **249** recommendations |\n'
          '\n'
          '### Split of 249\n'
          '\n'
          '| Need | Count | Mnemonic |\n'
          '|------|-------|----------|\n'
          '| Constitutional amendment | **58** | C |\n'
          '| Legislative measures | **86** | L |\n'
          '| Executive action | **105** | E |\n'
          '\n'
          '**58-86-105 = C-L-E** (Constitution · Law · Executive).\n'
          '\n'
          '## Members (book footnote)\n'
          '\n'
          'B.P. Jeevan Reddy · R.S. Sarkaria · K. Punnayya · Soli Sorabjee · K. Parasaran · Subhash Kashyap '
          '· C.R. Irani · Abid Hussain · Sumitra Kulkarni · **P.A. Sangma** (resigned ~3 months before '
          'report; linked to citizenship / high-office debate).\n'
          '\n'
          '**Trap:** R.S. Sarkaria was a **member** of NCRWC — he did **not** chair it.\n'
          '\n'
          '## Terms of Reference (essence)\n'
          '\n'
          '1. Examine how far the Constitution supports efficient governance & development.\n'
          '2. Recommend changes **if any** — within parliamentary democracy.\n'
          '3. Do **not** interfere with basic structure / basic features.\n'
          '\n'
          '## Eleven areas of study (Commission’s agenda)\n'
          '\n'
          '1. Strengthening parliamentary democracy (Legislature, Executive, Judiciary; accountability; '
          'stability)\n'
          '2. Electoral reforms & standards in political life\n'
          '3. Pace of socio-economic change (social & economic rights)\n'
          '4. Literacy, employment, social security, poverty alleviation\n'
          '5. Union–State relations\n'
          '6. Decentralisation / Panchayati Raj\n'
          '7. Enlargement of Fundamental Rights\n'
          '8. Effectuation of Fundamental Duties\n'
          '9. Effectuation of DPSPs & Preambular objectives\n'
          '10. Legal control of fiscal/monetary policies; public audit\n'
          '11. Administrative system & standards in public life\n'
          '\n'
          '## Eighteen areas of concern (compressed)\n'
          '\n'
          'Breach of constitutional faith · inability to anticipate techno-change · fiscal deficits · impure '
          'politics · national security neglect · PRI fault-lines · electoral misuse · weak representative '
          'character · opportunistic defections · debt / black money · rural–urban stress · educational '
          'disarmament · justice delays · criminal justice near collapse · communal riots · weak child '
          'social infrastructure · high IMR/malnutrition · public health crises.',
  'visual_blocks': [{'id': 'woc-ov-pillars',
                     'type': 'pillars',
                     'title': 'NCRWC identity card',
                     'items': [{'id': 'y',
                                'articles': '2000→2002',
                                'label': 'Years',
                                'detail': 'Resolution 2000; report 2002.',
                                'tone': 'teal'},
                               {'id': 'c',
                                'articles': 'Chair',
                                'label': 'Venkatachaliah',
                                'detail': 'Former CJI; not Sarkaria.',
                                'tone': 'olive'},
                               {'id': 'n',
                                'articles': '11',
                                'label': 'Members',
                                'detail': 'Sangma resigned before report.',
                                'tone': 'gold'},
                               {'id': 'r',
                                'articles': '249',
                                'label': 'Recommendations',
                                'detail': '58 + 86 + 105 (C-L-E).',
                                'tone': 'orange'},
                               {'id': 'b',
                                'articles': 'Limit',
                                'label': 'Basic structure',
                                'detail': 'Plus parliamentary democracy.',
                                'tone': 'terracotta'},
                               {'id': 'a',
                                'articles': 'Role',
                                'label': 'Advisory only',
                                'detail': 'Parliament may accept or reject.',
                                'tone': 'maroon'}]},
                    {'id': 'woc-ov-tree',
                     'type': 'tree',
                     'title': 'TOR → constraints → outputs',
                     'root': {'id': 'tor',
                              'label': 'Terms of Reference',
                              'detail': 'Governance + development capacity after 50 years',
                              'children': [{'id': 'const',
                                            'label': 'Constraints',
                                            'detail': 'Parliamentary democracy · basic structure',
                                            'children': [{'id': 'out',
                                                          'label': '249 recommendations',
                                                          'detail': '58 constitutional · 86 legislative · '
                                                                    '105 executive',
                                                          'children': []}]}]}},
                    {'id': 'woc-ov-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'Mnemonic: V-11-249',
                     'body': '**V**enkatachaliah · **11** members · **249** recommendations. Split: '
                             '**58-86-105** = Constitutional–Legislative–Executive.'}]},
 {'title': 'Major Areas Reviewed',
  'slug': 'woc-areas-reviewed',
  'sort_order': 3,
  'summary': 'Map of 11 study areas onto 14 recommendation themes — FR to anti-defection, governance to '
             'transparency.',
  'articles': [('11 study areas', 'Commission’s self-set agenda for review.'),
               ('14 themes', 'Recommendation chapters spanning rights to anti-defection.')],
  'body': '## Revision matrix — study areas → themes\n'
          '\n'
          '| Your syllabus theme | NCRWC coverage |\n'
          '|---------------------|----------------|\n'
          '| Fundamental Rights | Enlarge Part III; new FRs; emergency non-suspension list |\n'
          '| DPSP | Rename Part IV; effectuation bodies; population; education |\n'
          '| Fundamental Duties | Popularise; Verma; new Art. 51-A duties |\n'
          '| Executive | PM selection in hung House; MoS size; Civil Services |\n'
          '| Legislature | Privileges; sittings; committees; MPLADS |\n'
          '| Judiciary | NJC; retirement; pendency; contempt |\n'
          '| Electoral reforms | Disqualification; MCC; funding; CEC collegium |\n'
          '| Centre–State | Governor; 356; ISC; List III disasters |\n'
          '| Local governments | Exclusive functions; SEC–ECI; Schedules 11/12 |\n'
          '| Constitutional bodies | EC appointment; proposed NJC |\n'
          '| Public administration | Boards; lateral entry; Art. 311; oaths |\n'
          '| Emergency provisions | Art. 356 safeguards; FR suspension limits |\n'
          '| Anti-defection | Tenth Schedule redesign |\n'
          '| Governance / accountability / transparency | Lokpal; RTI; whistle-blower; ombudsman |\n'
          '\n'
          '## Fourteen recommendation themes (book order)\n'
          '\n'
          '1. Fundamental Rights  \n'
          '2. Right to Property  \n'
          '3. Directive Principles  \n'
          '4. Fundamental Duties  \n'
          '5. Parliament & State Legislatures  \n'
          '6. Executive & Administration  \n'
          '7. Centre–State & Inter-State  \n'
          '8. Judiciary  \n'
          '9. Socio-Economic Change  \n'
          '10. Decentralisation (Panchayats & Municipalities)  \n'
          '11. Institutions in North-East  \n'
          '12. Electoral Processes  \n'
          '13. Political Parties  \n'
          '14. Anti-Defection Law\n'
          '\n'
          'Open the theme clusters next — each is a recommendation matrix.',
  'visual_blocks': [{'id': 'woc-areas-pillars',
                     'type': 'pillars',
                     'title': 'Fourteen recommendation themes',
                     'items': [{'id': 't1',
                                'articles': '1–2',
                                'label': 'Rights & Property',
                                'detail': 'FR enlargement + Art. 300-A recast.',
                                'tone': 'teal'},
                               {'id': 't2',
                                'articles': '3–4',
                                'label': 'DPSP & Duties',
                                'detail': 'Effectuation + Verma + new duties.',
                                'tone': 'olive'},
                               {'id': 't3',
                                'articles': '5–6',
                                'label': 'Parl & Executive',
                                'detail': 'Stability, size, integrity, admin.',
                                'tone': 'gold'},
                               {'id': 't4',
                                'articles': '7–8',
                                'label': 'Federal & Courts',
                                'detail': 'Centre–State + NJC judiciary.',
                                'tone': 'orange'},
                               {'id': 't5',
                                'articles': '9–11',
                                'label': 'Society & Local',
                                'detail': 'Equity, PRIs, North-East.',
                                'tone': 'terracotta'},
                               {'id': 't6',
                                'articles': '12–14',
                                'label': 'Politics clean-up',
                                'detail': 'Elections, parties, anti-defection.',
                                'tone': 'maroon'}]},
                    {'id': 'woc-areas-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'How to revise',
                     'body': 'Don’t memorise all 249. Lock **14 themes**, then drill high-yield '
                             'recommendations (NJC, constructive no-confidence, Tenth Schedule EC, MoS 10%, '
                             'FR list, CEC collegium).'}]},
 {'title': 'FR & Right to Property — Recommendations',
  'slug': 'woc-fr-property',
  'sort_order': 4,
  'summary': 'Widen Arts. 15–16 & 19; new FRs; 21-A to 18; detention; Art. 25; Ninth Schedule limits; '
             'emergency non-suspension; Art. 300-A recast.',
  'articles': [('Arts. 15–16, 19, 21-A, 22, 25, 31-B', 'Proposed FR enlargements.'),
               ('Art. 300-A', 'Recast right to property with public purpose & rehab.')],
  'body': '## Fundamental Rights — recommendation matrix\n'
          '\n'
          '| Area | NCRWC recommendation |\n'
          '|------|----------------------|\n'
          '| Arts. **15–16** | Add grounds: ethnic/social origin, political opinion, property, birth |\n'
          '| Art. **19** | Explicitly cover press/media; hold opinions; seek/receive/impart info |\n'
          '| **New FRs** | Against torture/cruelty; compensation for illegal deprivation of life/liberty; '
          'leave & return to India; privacy & family life; rural wage employment ≥**80 days**/year; access '
          'to courts & speedy justice; equal justice & free legal aid; child care/protection; safe drinking '
          'water, anti-pollution, ecology, sustainable development |\n'
          '| Art. **21-A** | Free education to 14; for girls & SC/ST extend to **18** |\n'
          '| Art. **22** | Preventive detention max **6 months**; advisory board = chair + 2 **serving** HC '
          'judges |\n'
          '| Art. **25** | Treat Sikhism, Jainism, Buddhism as **separate** (delete Hinduism grouping) |\n'
          '| Art. **31-B** / 9th Schedule | Protect only agrarian reforms, reservations, DPSP Art. '
          '**39(b)/(c)** |\n'
          '| Emergency (352) | **No suspension** of enforcement of Arts. **17, 23, 24, 25, 32** (in addition '
          'to 20 & 21) |\n'
          '\n'
          '## Right to Property (recast Art. 300-A)\n'
          '\n'
          '1. Deprivation/acquisition only by **law** and for **public purpose**.\n'
          '2. No **arbitrary** deprivation/acquisition.\n'
          '3. SC/ST agricultural / forest / non-urban homestead land → law must provide **suitable '
          'rehabilitation before possession**.\n'
          '\n'
          '## Mains value-add\n'
          '\n'
          'NCRWC treated Part III as a living rights charter — expanding dignity, information, ecology and '
          'social rights while tightening emergency and detention abuse.',
  'visual_blocks': [{'id': 'woc-fr-pillars',
                     'type': 'pillars',
                     'title': 'High-yield FR changes',
                     'items': [{'id': 'new',
                                'articles': 'New FRs',
                                'label': 'Torture · Privacy · 80 days',
                                'detail': 'Plus ecology, speedy justice, leave/return.',
                                'tone': 'teal'},
                               {'id': '21a',
                                'articles': '21-A',
                                'label': 'Education to 18',
                                'detail': 'Girls & SC/ST beyond 14.',
                                'tone': 'olive'},
                               {'id': '22',
                                'articles': '22',
                                'label': 'Detention ≤ 6 months',
                                'detail': 'Serving HC judges on board.',
                                'tone': 'gold'},
                               {'id': '9s',
                                'articles': '31-B',
                                'label': 'Ninth Schedule curb',
                                'detail': 'Only agrarian / reservation / 39(b)(c).',
                                'tone': 'orange'},
                               {'id': 'em',
                                'articles': '352',
                                'label': 'Non-suspend list',
                                'detail': '17, 23, 24, 25, 32 (+20, 21).',
                                'tone': 'terracotta'},
                               {'id': '300',
                                'articles': '300-A',
                                'label': 'Property recast',
                                'detail': 'Public purpose + SC/ST rehab first.',
                                'tone': 'maroon'}]},
                    {'id': 'woc-fr-callout',
                     'type': 'callout',
                     'tone': 'trap',
                     'title': 'Prelims trap',
                     'body': 'Emergency non-suspension under NCRWC is **not** only Arts. 20 & 21 — it also '
                             'proposed **17, 23, 24, 25, 32**.'}]},
 {'title': 'DPSP & Fundamental Duties — Recommendations',
  'slug': 'woc-dpsp-fd',
  'sort_order': 5,
  'summary': 'Rename Part IV; population DPSP; education & inter-faith commissions; Verma Committee; new '
             'duties including pay taxes.',
  'articles': [('Part IV', 'Rename to Directive Principles of State Policy and Action.'),
               ('Art. 51-A', 'New duties: vote/participate/pay taxes; family; industry education.'),
               ('Verma Committee', '1998–99 — operationalising Fundamental Duties.')],
  'body': '## Directive Principles\n'
          '\n'
          '| Recommendation | Detail |\n'
          '|----------------|--------|\n'
          '| Rename Part IV | **Directive Principles of State Policy and Action** |\n'
          '| New DPSP | **Population control** |\n'
          '| Education | Independent **National Education Commission** every **5 years** |\n'
          '| Harmony | **Inter-Faith Commission** |\n'
          '| Review | High-status body to review DPSP implementation |\n'
          '| Employment | Strategic plan for large-scale employment in 5 years |\n'
          '| Statistics | Implement **National Statistical Commission (2001)** |\n'
          '\n'
          '## Fundamental Duties\n'
          '\n'
          '1. Popularise FDs and make them effective.\n'
          '2. Implement **Justice J.S. Verma Committee** (appointed 1998; report Oct 1999).\n'
          '3. New Art. 51-A duties:\n'
          '   - Duty to **vote**, participate, and **pay taxes**\n'
          '   - Family values / responsible parenthood\n'
          '   - Industrial organisations to educate employees’ children\n'
          '\n'
          '## Say this in Mains\n'
          '\n'
          'NCRWC linked rights to duties and DPSP effectuation — shifting from symbolic listing to '
          'institutions, statutes, and civic obligations (including taxation).',
  'visual_blocks': [{'id': 'woc-dpsp-compare',
                     'type': 'comparison',
                     'title': 'DPSP vs FD thrust of NCRWC',
                     'columns': [{'id': 'left',
                                  'heading': 'DPSP focus',
                                  'points': ['Rename Part IV (+ Action)',
                                             'Population control DPSP',
                                             'Education Commission (5 yrs)',
                                             'Inter-Faith Commission',
                                             'DPSP review body',
                                             'Employment plan + NSC 2001']},
                                 {'id': 'right',
                                  'heading': 'FD focus',
                                  'points': ['Popularise & operationalise',
                                             'Implement Verma Committee',
                                             'Vote + participate + pay taxes',
                                             'Family / parenthood duty',
                                             'Industry → educate workers’ children']}]},
                    {'id': 'woc-dpsp-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'Link',
                     'body': 'Pair with FD chapter: Verma Committee (1999) is the bridge — NCRWC explicitly '
                             'asked for its implementation.'}]},
 {'title': 'Parliament & Executive — Recommendations',
  'slug': 'woc-parliament-executive',
  'sort_order': 6,
  'summary': 'Privileges, sittings, committees; constructive no-confidence; MoS 10%; Lokpal (PM outside); '
             'Civil Service Boards; RTI & whistle-blower.',
  'articles': [('Arts. 105 / 194', 'Privilege not to cover corrupt acts.'),
               ('Council of Ministers', 'Cap at 10% of popular House (NCRWC).'),
               ('Art. 311', 'Protect honest officers; penalise dishonest.')],
  'body': '## Parliament & State Legislatures\n'
          '\n'
          '| Theme | Recommendation |\n'
          '|-------|----------------|\n'
          '| Privileges | Define/delimit; Art. 105/194 — **corruption not privileged**; prior '
          'Speaker/Chairman sanction for House-related offences |\n'
          '| Rajya Sabha | Keep **domicile** requirement (federal character) |\n'
          '| MPLADS | **Discontinue** |\n'
          '| Offices of profit | **EC** to identify/declare |\n'
          '| New committees | National Economy; Constitution (a priori amendment scrutiny); Legislation |\n'
          '| Drop | Estimates; Public Undertakings; Subordinate Legislation |\n'
          '| Oversight | Parliamentary **ombudsman** |\n'
          '| Minimum sittings | Assemblies <70 members → **50** days; others **90**; RS **100**; LS **120** '
          '|\n'
          '\n'
          '## Executive & Administration\n'
          '\n'
          '| Theme | Recommendation |\n'
          '|-------|----------------|\n'
          '| Hung House | LS elects Leader → appointed PM (same at state) |\n'
          '| No-confidence | **Constructive** vote (name alternative); notice by ≥**20%** |\n'
          '| MoS size | Cap at **10%** of popular House |\n'
          '| Perk posts | Cap political offices with minister-like perks at **2%** |\n'
          '| Lokpal | Constitutional Lokpal (**PM outside** purview) + state lokayuktas |\n'
          '| Lateral entry | Above Joint Secretary |\n'
          '| Art. 311 | Protect honest; penalise dishonest |\n'
          '| Civil services | Statutory autonomous **Civil Service Boards** |\n'
          '| Ethics | Oath to good governance; **transparency oath** (not secrecy) |\n'
          '| Integrity | Guarantee RTI; Whistle-blower / PID Acts; forfeit **benami** property |\n'
          '\n'
          '## Exam in 30 seconds\n'
          '\n'
          'Stability toolkit = constructive NC + 20% notice + MoS 10% + hung-House election of Leader.',
  'visual_blocks': [{'id': 'woc-parl-flow',
                     'type': 'flowchart',
                     'title': 'Hung House → PM (NCRWC)',
                     'steps': [{'id': 's1', 'label': 'Hung House', 'detail': 'No clear majority'},
                               {'id': 's2',
                                'label': 'House elects Leader',
                                'detail': 'Lok Sabha / Assembly chooses'},
                               {'id': 's3',
                                'label': 'Appointed PM / CM',
                                'detail': 'Democratic floor mandate first'}]},
                    {'id': 'woc-parl-pillars',
                     'type': 'pillars',
                     'title': 'Numbers to lock',
                     'items': [{'id': 'mos',
                                'articles': '10%',
                                'label': 'MoS ceiling',
                                'detail': 'Vs later 91st Amendment 15%.',
                                'tone': 'teal'},
                               {'id': 'perk',
                                'articles': '2%',
                                'label': 'Perk posts',
                                'detail': 'Minister-like political offices.',
                                'tone': 'olive'},
                               {'id': 'nc',
                                'articles': '20%',
                                'label': 'NC notice',
                                'detail': 'Plus constructive alternative.',
                                'tone': 'gold'},
                               {'id': 'sit',
                                'articles': '50/90/100/120',
                                'label': 'Min sittings',
                                'detail': 'Small SA / SA / RS / LS.',
                                'tone': 'orange'}]},
                    {'id': 'woc-parl-callout',
                     'type': 'callout',
                     'tone': 'trap',
                     'title': 'Trap: MoS 10% vs 15%',
                     'body': 'NCRWC recommended **10%**. The **91st Amendment** capped at **15%** (+ UT '
                             'special rules). Do not equate them.'}]},
 {'title': 'Centre–State Relations — Recommendations',
  'slug': 'woc-centre-state',
  'sort_order': 7,
  'summary': 'ISC matters; disaster List III; Governor after CM consultation; Art. 356 safeguards; reserved '
             'bills ~3 months; river disputes.',
  'articles': [('Art. 356', 'Retain but last resort; floor test; laying before dissolve.'),
               ('Governor', 'Appointment only after consultation with CM.'),
               ('List III', 'Disaster / emergency management proposed Concurrent.')],
  'body': '## Recommendation matrix\n'
          '\n'
          '| Theme | Recommendation |\n'
          '|-------|----------------|\n'
          '| Inter-State Council | Specify consultation matters (1990 Order) |\n'
          '| Disaster mgmt | Move to **List III** |\n'
          '| Trade | Statutory **Inter-State Trade and Commerce Commission** |\n'
          '| Governor | Appoint only after **CM consultation** |\n'
          '| Art. 356 | Retain; use sparingly, last resort |\n'
          '| Confidence | Test only on **floor**; no dismiss while confidence holds |\n'
          '| Elections impossible | Even without emergency proclamation, PR may continue if polls can’t be '
          'held |\n'
          '| Dissolve | Don’t dissolve Assembly before Art. 356 proclamation laid before Parliament |\n'
          '| River disputes | SC bench ≥**3** (if needed 5) for final disposal |\n'
          '| River Boards | Replace 1956 Act with comprehensive Act after state consultation |\n'
          '| Reserved bills | ~**3 months** for President’s decision |\n'
          '\n'
          '## Mains line\n'
          '\n'
          'NCRWC kept Art. 356 but tried to **proceduralise federal restraint** — floor test, parliamentary '
          'laying, and time-bound reserved bills.',
  'visual_blocks': [{'id': 'woc-csr-tree',
                     'type': 'tree',
                     'title': 'Federal reform map',
                     'root': {'id': 'fed',
                              'label': 'Centre–State package',
                              'detail': 'Cooperation + restraint',
                              'children': [{'id': 'g',
                                            'label': 'Governor',
                                            'detail': 'CM consultation before appointment',
                                            'children': []},
                                           {'id': 'a356',
                                            'label': 'Art. 356',
                                            'detail': 'Last resort · floor test · lay before dissolve',
                                            'children': []},
                                           {'id': 'inst',
                                            'label': 'Institutions',
                                            'detail': 'ISC list · Trade Commission · List III disasters',
                                            'children': []}]}},
                    {'id': 'woc-csr-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'Compare later',
                     'body': 'Governor + 356 + ISC themes overlap Sarkaria and Punchhi — use the Comparisons '
                             'cluster for the three-commission table.'}]},
 {'title': 'Judiciary — Recommendations',
  'slug': 'woc-judiciary',
  'sort_order': 8,
  'summary': 'National Judicial Commission composition; HC 65 / SC 68; 90-day judgments; 1-year pendency; '
             'plea bargaining.',
  'articles': [('NJC', 'CJI + 2 senior SC judges + Law Minister + Presidential nominee.'),
               ('Retirement', 'HC 65; SC 68 (proposed).')],
  'body': '## Recommendation matrix\n'
          '\n'
          '| Theme | Recommendation |\n'
          '|-------|----------------|\n'
          '| Appointments | Constitutional **National Judicial Commission**: CJI (chair), 2 senior-most SC '
          'judges, Union Law Minister, 1 Presidential nominee |\n'
          '| Misconduct | NJC committee for complaints against SC/HC judges |\n'
          '| Retirement | HC **65**; SC **68** |\n'
          '| Contempt | Only SC & HCs punish for contempt of themselves |\n'
          '| Judicial review of statutes | Only SC & HCs may strike down as unconstitutional |\n'
          '| Budgets/plans | National + State Judicial Councils |\n'
          '| Speed | Judgments ordinarily within **90 days** of conclusion |\n'
          '| Abuse | Exemplary costs for abuse of process |\n'
          '| Pendency | HC strategic plans: no case pending > **1 year** |\n'
          '| Reform | Introduce **plea-bargaining**; two-tier subordinate judiciary under HC |\n'
          '\n'
          '## Later echo (careful wording)\n'
          '\n'
          'NJAC (99th Amendment) was in the **same reform stream** as NCRWC’s NJC idea — but composition and '
          'fate differed; NJAC was struck down. Say **aligned**, not identical.',
  'visual_blocks': [{'id': 'woc-jud-pillars',
                     'type': 'pillars',
                     'title': 'NJC & court reform anchors',
                     'items': [{'id': 'njc',
                                'articles': '5 members',
                                'label': 'NJC composition',
                                'detail': 'CJI + 2 SC + Law Min + Prez nominee.',
                                'tone': 'teal'},
                               {'id': 'age',
                                'articles': '65 / 68',
                                'label': 'Retirement ages',
                                'detail': 'HC 65 · SC 68 (proposed).',
                                'tone': 'olive'},
                               {'id': '90',
                                'articles': '90 days',
                                'label': 'Judgment timeline',
                                'detail': 'From conclusion of arguments.',
                                'tone': 'gold'},
                               {'id': '1y',
                                'articles': '1 year',
                                'label': 'Pendency goal',
                                'detail': 'HC strategic plans.',
                                'tone': 'orange'}]},
                    {'id': 'woc-jud-callout',
                     'type': 'callout',
                     'tone': 'trap',
                     'title': 'Trap: NJC ≠ NJAC',
                     'body': 'NCRWC proposed **NJC**. Parliament later enacted **NJAC** (99th) — struck '
                             'down. Don’t write that NCRWC ‘created NJAC’.'}]},
 {'title': 'Electoral Reforms, Parties & Anti-Defection',
  'slug': 'woc-electoral-parties',
  'sort_order': 9,
  'summary': 'Criminal bars, MCC statutory, CEC collegium, party regulation law, Tenth Schedule: '
             'resign–recontest; EC decides disqualification.',
  'articles': [('Tenth Schedule', 'All defectors resign; EC decides disqualification.'),
               ('ECI', 'CEC/ECs via multi-member parliamentary collegium (proposed).')],
  'body': '## Electoral processes\n'
          '\n'
          '| Theme | Recommendation |\n'
          '|-------|----------------|\n'
          '| Charge sheet | Offence with max ≥**5 years** → disqualification |\n'
          '| Heinous crimes | Murder, rape, smuggling, dacoity etc. → **permanent** bar |\n'
          '| Speed | Special courts / exclusive HC election benches |\n'
          '| State funding | **Defer** until party regulation & financial limits exist |\n'
          '| Multi-seat | No simultaneous contest for same office from >1 constituency |\n'
          '| MCC | Make **statutory**; penalise violations |\n'
          '| Voting system | Examine **50%+1** runoff vs FPTP |\n'
          '| Independents | Lose **3 times** consecutively → permanent bar for that office |\n'
          '| Deposit | Raise forfeiture threshold **16.67% → 25%** |\n'
          '| High offices | National dialogue on eligibility of non-Indian-born (deep division; Sangma '
          'resignation context) |\n'
          '| CEC/ECs | Appoint on recommendation of PM, LoP LS, LoP RS, Speaker LS, Dy Chairman RS |\n'
          '\n'
          '## Political parties\n'
          '\n'
          '- Comprehensive law on registration/functioning; open membership; audited accounts.\n'
          '- No ticket if convicted or charges framed; violation → candidate DQ + party '
          'deregistration/derecognition.\n'
          '- Raise EC recognition threshold.\n'
          '- Consolidated law on contributions/expenses; transparency; tax-exempt donations up to limit; '
          'publish yearly audited accounts.\n'
          '\n'
          '## Anti-defection (amend Tenth Schedule)\n'
          '\n'
          '1. All defectors (individual **or** group) must **resign** and contest afresh.\n'
          '2. Debar from minister/remunerative political post for remaining term / until next polls.\n'
          '3. Defector’s vote to topple government → **invalid**.\n'
          '4. Disqualification decided by **Election Commission**, not Speaker/Chairman.',
  'visual_blocks': [{'id': 'woc-elec-compare',
                     'type': 'comparison',
                     'title': 'Anti-defection: present vs NCRWC',
                     'columns': [{'id': 'left',
                                  'heading': 'Present (broad)',
                                  'points': ['Speaker/Chairman decides DQ',
                                             'Merger exceptions exist',
                                             'Defectors may keep seats till ruling',
                                             'Toppling votes can still count pending DQ']},
                                 {'id': 'right',
                                  'heading': 'NCRWC redesign',
                                  'points': ['EC decides DQ',
                                             'All defectors resign & recontest',
                                             'Post bar till term/elections',
                                             'Toppling vote of defector invalid']}]},
                    {'id': 'woc-elec-pillars',
                     'type': 'pillars',
                     'title': 'Electoral numbers',
                     'items': [{'id': '5y',
                                'articles': '≥5 yrs',
                                'label': 'Charge → DQ',
                                'detail': 'Max punishment threshold.',
                                'tone': 'teal'},
                               {'id': '25',
                                'articles': '25%',
                                'label': 'Deposit forfeit',
                                'detail': 'Up from 16.67%.',
                                'tone': 'olive'},
                               {'id': '3x',
                                'articles': '3 losses',
                                'label': 'Independent bar',
                                'detail': 'Consecutive losses → permanent bar.',
                                'tone': 'gold'},
                               {'id': 'col',
                                'articles': '5-member',
                                'label': 'CEC collegium',
                                'detail': 'PM + LoPs + Speaker + Dy Ch. RS.',
                                'tone': 'orange'}]},
                    {'id': 'woc-elec-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'GS-II example',
                     'body': 'Use NCRWC’s anti-defection package as a ready reform alternative when '
                             'critiquing Speaker-centric Tenth Schedule adjudication.'}]},
 {'title': 'Local Government & North-East — Recommendations',
  'slug': 'woc-local-ne',
  'sort_order': 10,
  'summary': 'Exclusive PRI/municipal functions; SEC–ECI link; CAG standards; Sixth Schedule subjects; '
             'National Immigration Council.',
  'articles': [('Arts. 243-G / 243-W', 'Declare exclusive functions of self-government.'),
               ('Arts. 243-K / 243-ZA', 'ECI directions to SECs; SECs report to ECI & Governor.'),
               ('Sixth Schedule', 'Entrust ADC subjects; associate traditional governance.')],
  'body': '## Decentralisation (Panchayats & Municipalities)\n'
          '\n'
          '| Theme | Recommendation |\n'
          '|-------|----------------|\n'
          '| Schedules 11 & 12 | Restructure for separate **fiscal domain** |\n'
          '| State Panchayat Council | Under CM |\n'
          '| Status | Declare PRIs/municipalities **institutions of self-government** with **exclusive** '
          'functions (amend 243-G, 243-W) |\n'
          '| SEC–ECI | ECI directions to SECs; SECs report to ECI & Governor |\n'
          '| Dissolution | Hearing before dissolving a Panchayat (243-E) |\n'
          '| Audit | CAG audit / accounting standards for Panchayats |\n'
          '| Municipalities | Report to State Legislature when superseded |\n'
          '| Qualifications | Single consolidated law for local elections |\n'
          '| Delimitation/rotation | **Delimitation Commission**, not SEC |\n'
          '| Municipal taxes | Distinct tax domain |\n'
          '\n'
          '## Institutions in North-East\n'
          '\n'
          '1. Extend 73rd/74th opportunities respecting unique political traditions.\n'
          '2. Entrust Sixth Schedule + Eleventh Schedule subjects to ADCs.\n'
          '3. Associate traditional governance with self-governance.\n'
          '4. **National Immigration Council** (review Citizenship Act, IMDT Act, Foreigners Act, etc.).',
  'visual_blocks': [{'id': 'woc-local-pillars',
                     'type': 'pillars',
                     'title': 'Local + NE anchors',
                     'items': [{'id': 'ex',
                                'articles': '243-G/W',
                                'label': 'Exclusive functions',
                                'detail': 'True self-government, not agency.',
                                'tone': 'teal'},
                               {'id': 'sec',
                                'articles': '243-K/ZA',
                                'label': 'SEC under ECI wing',
                                'detail': 'Directions + dual reporting.',
                                'tone': 'olive'},
                               {'id': 'del',
                                'articles': 'Delimitation',
                                'label': 'Not SEC’s job',
                                'detail': 'Rotation/reservation via Delimitation Commission.',
                                'tone': 'gold'},
                               {'id': 'ne',
                                'articles': 'VI Schedule',
                                'label': 'ADC + Immigration',
                                'detail': 'Subjects to ADCs; National Immigration Council.',
                                'tone': 'orange'}]},
                    {'id': 'woc-local-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'Mains hook',
                     'body': 'NCRWC’s local-government package = functional exclusivity + fiscal domain + '
                             'independent election machinery — still unfinished federal agenda.'}]},
 {'title': 'Socio-Economic Change & Accountability',
  'slug': 'woc-socio-economic',
  'sort_order': 11,
  'summary': 'Reservation statute & Arakshan Nyaya Adalats; tribal Schedules; bonded labour; women’s '
             'empowerment; Citizens’ Charters.',
  'articles': [('Fifth → Sixth Schedule', 'Tribal areas shift proposed.'),
               ('SC/ST (PoA) Act', 'Special courts; effective PCR Act / Manual Scavengers Act.')],
  'body': '## Socio-economic recommendations (high yield)\n'
          '\n'
          '| Theme | Recommendation |\n'
          '|-------|----------------|\n'
          '| Bench diversity | Reasonable SC/ST/BC presence on SC/HC |\n'
          '| Capability | Enable SC/ST/BC (esp. girls) to compete equally |\n'
          '| Institutions | New institutions for weaker-section resource use |\n'
          '| Charters | Citizens’ Charters (esp. for deprived groups) |\n'
          '| Reservation law | Comprehensive statute + **Arakshan Nyaya Adalats** |\n'
          '| Education | Residential schools for SC/ST/BC in every district |\n'
          '| Tribal areas | Fifth Schedule areas → Sixth Schedule; other tribal areas too |\n'
          '| Atrocities | Special courts under SC/ST (PoA) Act 1989 |\n'
          '| Civil rights | Effective PCR Act 1955; Manual Scavengers Act 1993 |\n'
          '| Minorities | Improve education & political representation |\n'
          '| Bonded labour | National (+ state) Liberation & Rehabilitation Authority |\n'
          '| Women | Reservation, development, empowerment, health, protection from violence |\n'
          '\n'
          '## Governance / accountability thread\n'
          '\n'
          'Cross-link Executive cluster: Lokpal, RTI, whistle-blower, Civil Service Boards, transparency '
          'oath — NCRWC treated social justice and clean administration as one package.',
  'visual_blocks': [{'id': 'woc-socio-pillars',
                     'type': 'pillars',
                     'title': 'Equity toolkit',
                     'items': [{'id': 'arak',
                                'articles': 'Statute',
                                'label': 'Arakshan Nyaya Adalats',
                                'detail': 'Special forums for reservation justice.',
                                'tone': 'teal'},
                               {'id': 'sch',
                                'articles': 'V → VI',
                                'label': 'Tribal Schedules',
                                'detail': 'Fifth Schedule areas into Sixth.',
                                'tone': 'olive'},
                               {'id': 'bond',
                                'articles': 'Authority',
                                'label': 'Bonded labour',
                                'detail': 'National liberation & rehab body.',
                                'tone': 'gold'},
                               {'id': 'women',
                                'articles': 'Empowerment',
                                'label': 'Women’s package',
                                'detail': 'Reservation + safety + health.',
                                'tone': 'orange'}]},
                    {'id': 'woc-socio-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'Current affairs bridge',
                     'body': 'Women’s reservation later advanced via **106th Amendment** — use as ‘aligned '
                             'later development’, not as direct NCRWC enactment.'}]},
 {'title': 'Recommendations Accepted vs Pending',
  'slug': 'woc-accepted-pending',
  'sort_order': 12,
  'summary': 'Book: Parliament may accept/reject. Revision map of aligned later reforms vs major pending '
             'NCRWC ideas — carefully labeled.',
  'articles': [('Advisory role', 'Parliament may accept or reject any recommendation.'),
               ('91st Amendment', 'MoS size — same reform stream, different ceiling (15% vs 10%).')],
  'body': '## Book position\n'
          '\n'
          'NCRWC is **advisory**. Laxmikanth does **not** list which recommendations were accepted. For exam '
          'revision, use **aligned later developments** carefully.\n'
          '\n'
          '## Implemented / closely aligned\n'
          '\n'
          '| Theme | Later development | Vs NCRWC |\n'
          '|-------|-------------------|----------|\n'
          '| RTI / transparency | RTI Act **2005** | Closely aligned |\n'
          '| MoS size | **91st** Amendment (15%) | Same stream; ceiling **differs** (rec. 10%) |\n'
          '| Lokpal | Lokpal Act **2013** | Partial (PM treatment differs) |\n'
          '| Plea bargaining | Criminal law reforms | Aligned direction |\n'
          '| Women’s reservation | **106th** Amendment | Aligned later |\n'
          '| Whistle-blower | Whistle Blowers Protection Act | Aligned direction |\n'
          '\n'
          '## Attempted / failed / reversed drift\n'
          '\n'
          '| Theme | Development | Status |\n'
          '|-------|-------------|--------|\n'
          '| Judicial appointments | **NJAC** (99th) → struck down | Attempted / failed |\n'
          '| RS domicile | Dilution / practice after *Kuldip Nayar* | Opposite to NCRWC keep-domicile |\n'
          '\n'
          '## Major pending\n'
          '\n'
          '- **Constructive** vote of no-confidence\n'
          '- Full **Tenth Schedule** redesign (all resign + EC decides)\n'
          '- Constitutional **NJC** as proposed\n'
          '- MoS at **10%** (vs actual 15%)\n'
          '- End **MPLADS**; parliamentary ombudsman package as designed\n'
          '- Comprehensive **party regulation** law + deferred state funding logic\n'
          '- Many new **FRs** / Art. 300-A recast / Ninth Schedule curb\n'
          '- Local govt **exclusive functions + fiscal domain** unfinished\n'
          '\n'
          '## Why pending? (revision reasons)\n'
          '\n'
          'Political consensus gaps · federal sensitivity · judicial pushback (NJAC) · competing reform '
          'designs · implementation capacity · some ideas overtaken by other laws.\n'
          '\n'
          '## Current relevance\n'
          '\n'
          'Pending items still frame debates on simultaneous elections, CEC appointments, anti-defection, '
          'federal Governors, and civil-service stability.',
  'visual_blocks': [{'id': 'woc-acc-compare',
                     'type': 'comparison',
                     'title': 'Aligned later vs still pending',
                     'columns': [{'id': 'left',
                                  'heading': 'Aligned / partial',
                                  'points': ['RTI Act 2005',
                                             '91st MoS cap (15% ≠ 10%)',
                                             'Lokpal Act 2013 (partial)',
                                             'Whistle-blower law',
                                             '106th women’s reservation',
                                             'Plea bargaining direction']},
                                 {'id': 'right',
                                  'heading': 'Still pending (major)',
                                  'points': ['Constructive no-confidence',
                                             'Anti-defection EC model',
                                             'NJC as proposed',
                                             'Many new FRs / 300-A recast',
                                             'Party regulation law package',
                                             'Local exclusive fiscal domain']}]},
                    {'id': 'woc-acc-callout',
                     'type': 'callout',
                     'tone': 'trap',
                     'title': 'Writing discipline',
                     'body': 'Don’t write ‘NCRWC recommended the 91st Amendment’. Write: ‘in the same reform '
                             'stream as NCRWC’s MoS-size concern’.'}]},
 {'title': 'Comparison Sections',
  'slug': 'woc-comparisons',
  'sort_order': 13,
  'summary': 'Sarkaria vs Punchhi vs NCRWC; amendment vs review; original Constitution vs recommended '
             'changes.',
  'articles': [('Sarkaria 1983–88', 'Centre–State focus; R.S. Sarkaria later sat on NCRWC.'),
               ('Punchhi 2007–10', 'Centre–State revisited after NCRWC.'),
               ('Art. 368', 'Amendment path vs advisory constitutional review.')],
  'body': '## 1. Sarkaria vs Punchhi vs NCRWC\n'
          '\n'
          '| | Sarkaria | NCRWC | Punchhi |\n'
          '|-|----------|-------|--------|\n'
          '| Years | 1983–88 | **2000–02** | 2007–10 |\n'
          '| Chair | R.S. Sarkaria | **M.N. Venkatachaliah** | Madan Mohan Punchhi |\n'
          '| Mandate | Centre–State | **Working of whole Constitution** | Centre–State |\n'
          '| Output focus | Federal practice | **249** multi-theme recs | Federal + concurrent themes |\n'
          '| Overlap | Governor, 356, ISC | Same + rights, elections, judiciary, parties | Governor, 356, '
          'appointments |\n'
          '\n'
          '**Memory:** Sarkaria & Punchhi = **federal specialists**; NCRWC = **full-body check-up**.\n'
          '\n'
          '## 2. Constitutional Amendment vs Constitutional Review\n'
          '\n'
          '| | Amendment (Art. 368) | Review (NCRWC-type) |\n'
          '|-|---------------------|---------------------|\n'
          '| Who | Parliament | Executive-appointed commission |\n'
          '| Effect | Changes the text (if passed) | Only **recommends** |\n'
          '| Limit | Basic structure (judicial) | TOR + basic structure (self-bound) |\n'
          '| End state | Law of the land | Report for political choice |\n'
          '\n'
          '## 3. Original Constitution vs Recommended Changes (high-impact)\n'
          '\n'
          '| Domain | Original / present baseline | NCRWC delta |\n'
          '|--------|----------------------------|-------------|\n'
          '| FR | Six categories; property as legal right | Many **new FRs**; 300-A recast |\n'
          '| Stability | Ordinary no-confidence | **Constructive** NC |\n'
          '| MoS size | Later 15% (91st) | Proposed **10%** |\n'
          '| Judges | Collegium evolution | **NJC** |\n'
          '| Defection | Speaker decides | **EC** + resign-recontest |\n'
          '| Local govt | 73rd/74th framework | Exclusive functions + fiscal domain |\n'
          '\n'
          '## 4. Implemented vs Pending\n'
          '\n'
          'See **Accepted vs Pending** cluster for the live matrix.',
  'visual_blocks': [{'id': 'woc-cmp-table',
                     'type': 'comparison',
                     'title': 'Federal commissions vs NCRWC',
                     'columns': [{'id': 'left',
                                  'heading': 'Sarkaria / Punchhi',
                                  'points': ['Mandate: Centre–State',
                                             'Federal institutions focus',
                                             'Governor · 356 · ISC core',
                                             'Punchhi after NCRWC (2007–10)']},
                                 {'id': 'right',
                                  'heading': 'NCRWC',
                                  'points': ['Mandate: whole working',
                                             'Rights + elections + judiciary + parties',
                                             '249 = 58+86+105',
                                             'Sarkaria sat as member here']}]},
                    {'id': 'woc-cmp-flow',
                     'type': 'flowchart',
                     'title': 'Review → reform path',
                     'steps': [{'id': 'r1',
                                'label': 'Review commission',
                                'detail': 'GoI resolution · TOR · report'},
                               {'id': 'r2',
                                'label': 'Recommend',
                                'detail': 'Constitutional / legislative / executive'},
                               {'id': 'r3',
                                'label': 'Political choice',
                                'detail': 'Amend · enact · executive action — or reject'}]},
                    {'id': 'woc-cmp-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'Prelims identity check',
                     'body': 'If the question says ‘Centre–State only’, think Sarkaria/Punchhi. If it says '
                             '‘working of the Constitution / Venkatachaliah / 249’, think NCRWC.'}]},
 {'title': 'Current Affairs Linkages',
  'slug': 'woc-current-affairs',
  'sort_order': 14,
  'summary': 'Simultaneous elections, CEC appointment law, NJAC memory, lateral entry, federalism, '
             'parliamentary sittings, civil-service reforms.',
  'articles': [('CEC appointment (2023 law)', 'Compare with NCRWC multi-member collegium idea.'),
               ('106th Amendment', 'Women’s reservation — aligned later development.')],
  'body': '## Link NCRWC → today’s debates\n'
          '\n'
          '| Debate | NCRWC hook |\n'
          '|--------|-----------|\n'
          '| **Simultaneous / ONOE** | Stability within parliamentary democracy; election cost & frequency '
          'concerns |\n'
          '| **Electoral reforms** | Criminal bars, MCC statutory, party finance law, deposit 25% |\n'
          '| **CEC/EC appointments** | NCRWC multi-member collegium vs later statutory design |\n'
          '| **Judicial appointments** | NJC idea ↔ NJAC memory ↔ collegium debate |\n'
          '| **Anti-defection** | EC adjudication + resign-recontest still reform template |\n'
          '| **Federalism** | Governor CM-consult; 356 restraint; ISC; List III disasters |\n'
          '| **Civil services** | Civil Service Boards; lateral entry; Art. 311 balance; Mission Karmayogi '
          'context |\n'
          '| **Parliamentary reforms** | Minimum sittings; privileges; Constitution committee |\n'
          '| **Local governance** | Exclusive functions & fiscal domain unfinished |\n'
          '| **Social justice** | Women’s reservation; tribal Schedules; bonded labour |\n'
          '\n'
          '## Ready GS-II sentences\n'
          '\n'
          '1. *“NCRWC framed stability devices (constructive no-confidence, MoS size) without abandoning '
          'parliamentary responsibility.”*\n'
          '2. *“On appointments, NCRWC preferred pluralised collegiums for both judges (NJC) and Election '
          'Commissioners — a recurring theme in later reform debates.”*\n'
          '3. *“Anti-defection redesign under NCRWC shifts adjudication from the Speaker to the EC and '
          'treats every defection as a mandate-renewal event.”*',
  'visual_blocks': [{'id': 'woc-caf-pillars',
                     'type': 'pillars',
                     'title': 'Six live debate bridges',
                     'items': [{'id': 'onoe',
                                'articles': 'Stability',
                                'label': 'Simultaneous polls',
                                'detail': 'Cost, frequency, governance continuity.',
                                'tone': 'teal'},
                               {'id': 'cec',
                                'articles': 'ECI',
                                'label': 'CEC collegium debate',
                                'detail': 'NCRWC 5-member recommendation.',
                                'tone': 'olive'},
                               {'id': 'jud',
                                'articles': 'NJC',
                                'label': 'Judicial appointments',
                                'detail': 'NJC → NJAC memory → collegium.',
                                'tone': 'gold'},
                               {'id': 'def',
                                'articles': 'X Sch.',
                                'label': 'Anti-defection',
                                'detail': 'EC model still cited.',
                                'tone': 'orange'},
                               {'id': 'fed',
                                'articles': 'Federal',
                                'label': 'Governor / 356',
                                'detail': 'Shared with Sarkaria–Punchhi.',
                                'tone': 'terracotta'},
                               {'id': 'civ',
                                'articles': 'Admin',
                                'label': 'Civil services',
                                'detail': 'Boards · lateral entry · transfers.',
                                'tone': 'maroon'}]},
                    {'id': 'woc-caf-callout',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'Use in answers',
                     'body': 'One NCRWC citation per answer is enough — pick the hook that matches the '
                             'question (stability / appointments / defection / federalism).'}]},
 {'title': 'UPSC Focus Areas',
  'slug': 'woc-upsc-focus',
  'sort_order': 15,
  'summary': 'Prelims traps, Mains themes, mnemonics, PYQ themes, frequently confused concepts, value-add '
             'lines.',
  'articles': [('V-11-249', 'Venkatachaliah · 11 members · 249 recommendations.'),
               ('58-86-105', 'Constitutional · Legislative · Executive split.')],
  'body': '## Frequently asked themes\n'
          '\n'
          '- Year / chair / nature (GoI resolution)\n'
          '- 249 split (58+86+105)\n'
          '- Basic structure constraint\n'
          '- NJC composition\n'
          '- Constructive no-confidence / MoS 10%\n'
          '- Anti-defection EC model\n'
          '- Difference from Sarkaria/Punchhi\n'
          '\n'
          '## Important committees / reports to pair\n'
          '\n'
          '| Name | Link |\n'
          '|------|------|\n'
          '| NCRWC (Venkatachaliah) | This chapter |\n'
          '| Sarkaria / Punchhi | Federal comparisons |\n'
          '| J.S. Verma (FDs) | Explicitly endorsed by NCRWC |\n'
          '| National Statistical Commission 2001 | DPSP/statistics follow-through |\n'
          '| Law Commission (electoral/criminalisation themes) | Parallel reform literature |\n'
          '\n'
          '## Common prelims traps\n'
          '\n'
          '1. NCRWC is a **constitutional body** → **False** (GoI resolution).\n'
          '2. Chair was **Sarkaria** → **False** (member, not chair).\n'
          '3. All 249 need constitutional amendment → **False** (only 58).\n'
          '4. MoS recommendation = **15%** → **False** (NCRWC **10%**; 91st = 15%).\n'
          '5. Lokpal under NCRWC covers **PM** → **False** (PM **outside**).\n'
          '6. Set up in **2002** → **False** (set up **2000**; report 2002).\n'
          '\n'
          '## Mains value additions\n'
          '\n'
          '- Review within basic structure = institutional humility.\n'
          '- Stability **with** accountability (constructive NC, not anti-parliamentary).\n'
          '- Pluralised appointments (NJC / EC collegium) as recurring reform grammar.\n'
          '- Defection as **mandate breach** → resign & seek fresh trust.\n'
          '\n'
          '## Mnemonics\n'
          '\n'
          '- **V-11-249** — Venkatachaliah, 11 members, 249 recs\n'
          '- **58-86-105 / C-L-E** — Constitutional, Legislative, Executive\n'
          '- **NJC = C2 L P** — CJI + 2 SC + Law Minister + Presidential nominee\n'
          '- **Sittings 50-90-100-120** — small SA, SA, RS, LS\n'
          '\n'
          '## Frequently confused\n'
          '\n'
          '| Confusable | Clear it |\n'
          '|------------|----------|\n'
          '| Sarkaria chair vs NCRWC chair | Sarkaria chaired **Centre–State** commission; on NCRWC he was '
          '**member** |\n'
          '| NJC vs NJAC | NCRWC idea vs later amendment (struck down) |\n'
          '| Review vs rewrite | Advisory working review only |\n'
          '| 10% vs 15% MoS | NCRWC vs 91st Amendment |',
  'visual_blocks': [{'id': 'woc-upsc-callout',
                     'type': 'callout',
                     'tone': 'trap',
                     'title': 'Top 6 prelims traps',
                     'body': 'Not a constitutional body · Venkatachaliah not Sarkaria · 2000/2002 · 58≠249 '
                             'amendments · MoS 10%≠15% · Lokpal PM outside.'},
                    {'id': 'woc-upsc-pillars',
                     'type': 'pillars',
                     'title': 'Memory tricks',
                     'items': [{'id': 'v',
                                'articles': 'ID',
                                'label': 'V-11-249',
                                'detail': 'Chair · size · total recs.',
                                'tone': 'teal'},
                               {'id': 'cle',
                                'articles': 'Split',
                                'label': '58-86-105',
                                'detail': 'C · L · E',
                                'tone': 'olive'},
                               {'id': 'njc',
                                'articles': 'NJC',
                                'label': 'C2 L P',
                                'detail': 'CJI+2SC+Law+Prez nominee.',
                                'tone': 'gold'},
                               {'id': 'sit',
                                'articles': 'House',
                                'label': '50-90-100-120',
                                'detail': 'Sitting minima.',
                                'tone': 'orange'}]},
                    {'id': 'woc-upsc-tip',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'PYQ themes',
                     'body': 'Expect: commission identity facts; recommendation nature; linked reform '
                             'streams (RTI/Lokpal/NJAC/91st); federal commission comparison.'}]},
 {'title': 'One-Page Revision Sheet',
  'slug': 'woc-revision-sheet',
  'sort_order': 16,
  'summary': 'Complete recommendation cheat sheet, timeline, top-15 table, reforms summary, article map, '
             'Exam-in-5-Minutes.',
  'articles': [('Ch. 90 cheat sheet', 'NCRWC — Working of the Constitution.'),
               ('249 = 58+86+105', 'Amendment · statute · executive action.')],
  'body': '## Exam in 5 Minutes\n'
          '\n'
          '**NCRWC** — GoI resolution **2000**, report **2002**, chair **M.N. Venkatachaliah**, **11** '
          'members, **249** recs (**58** constitutional + **86** legislative + **105** executive). Review '
          'working within **parliamentary democracy + basic structure**. Advisory only.\n'
          '\n'
          '## Timeline of constitutional review efforts\n'
          '\n'
          '1946–49 Constituent Assembly → major amendments → Sarkaria 1983–88 → Verma FDs 1999 → **NCRWC '
          '2000–02** → Punchhi 2007–10 → ongoing reform statutes.\n'
          '\n'
          '## Most important 15 recommendations\n'
          '\n'
          '| # | Recommendation |\n'
          '|---|----------------|\n'
          '| 1 | Enlarge FRs (privacy, torture ban, ecology, 80-day work, etc.) |\n'
          '| 2 | Art. 22 detention ≤ 6 months; serving HC judges on board |\n'
          '| 3 | Ninth Schedule limited to agrarian / reservation / 39(b)(c) |\n'
          '| 4 | Emergency: no suspend 17, 23, 24, 25, 32 |\n'
          '| 5 | Recast Art. 300-A (public purpose + SC/ST rehab) |\n'
          '| 6 | New FDs: vote / pay taxes; implement Verma |\n'
          '| 7 | Constructive no-confidence + 20% notice |\n'
          '| 8 | MoS ≤ 10%; perk posts ≤ 2% |\n'
          '| 9 | Constitutional Lokpal (PM outside) |\n'
          '| 10 | Civil Service Boards + RTI / whistle-blower |\n'
          '| 11 | Governor after CM consultation; 356 safeguards |\n'
          '| 12 | National Judicial Commission |\n'
          '| 13 | CEC/EC multi-member collegium; MCC statutory |\n'
          '| 14 | Party regulation law; defer state funding |\n'
          '| 15 | Anti-defection: resign–recontest; EC decides |\n'
          '\n'
          '## Complete recommendation cheat sheet (14 themes)\n'
          '\n'
          '1. **FR** — widen 15/16/19; new rights; 21-A to 18; detention; Art. 25; 31-B curb; emergency '
          'list  \n'
          '2. **Property** — 300-A public purpose + rehab  \n'
          '3. **DPSP** — rename; population; Education & Inter-Faith Commissions; review body  \n'
          '4. **FD** — Verma; vote/taxes/family/industry education  \n'
          '5. **Legislature** — privileges; domicile; end MPLADS; sittings; new committees  \n'
          '6. **Executive** — hung-House Leader; constructive NC; MoS 10%; Lokpal; CS Boards; RTI  \n'
          '7. **Centre–State** — ISC; List III disasters; Trade Commission; Governor; 356; 3-month bills  \n'
          '8. **Judiciary** — NJC; 65/68; 90-day judgments; 1-year pendency; plea bargain  \n'
          '9. **Socio-economic** — reservation statute; Schedules; bonded labour; women  \n'
          '10. **Local** — exclusive functions; SEC–ECI; CAG; Delimitation Commission  \n'
          '11. **North-East** — ADC subjects; Immigration Council  \n'
          '12. **Electoral** — criminal bars; MCC law; 25% deposit; CEC collegium  \n'
          '13. **Parties** — regulation + finance transparency  \n'
          '14. **Anti-defection** — resign all; EC decides; invalidate toppling vote  \n'
          '\n'
          '## Constitutional reforms summary (by instrument)\n'
          '\n'
          '| Instrument | Examples |\n'
          '|------------|----------|\n'
          '| Constitutional amendment (58) | New FRs, NJC, Tenth Schedule, MoS 10%, Art. 356 tweaks |\n'
          '| Legislation (86) | Party law, MCC statute, whistle-blower, Civil Service Boards |\n'
          '| Executive (105) | Charters, education plans, administrative standards |\n'
          '\n'
          '## Article / provision map (proposed touchpoints)\n'
          '\n'
          '15–16 · 19 · 21-A · 22 · 25 · 31-B/9th Schedule · 32 (emergency) · 51-A · 105/194 · '
          '243-G/W/K/ZA/E · 300-A · 311 · 352/356 · Tenth Schedule · Lists (disaster → III).\n'
          '\n'
          '## Frequently confused — final pass\n'
          '\n'
          'Review ≠ rewrite · Venkatachaliah ≠ Sarkaria-as-chair · NJC ≠ NJAC · 10% ≠ 15% · advisory ≠ '
          'binding.',
  'visual_blocks': [{'id': 'woc-rev-timeline',
                     'type': 'timeline',
                     'title': 'Review timeline (one glance)',
                     'events': [{'year': '1983–88',
                                 'detail': 'Centre–State.',
                                 'label': 'Sarkaria',
                                 'id': 'e0-sarkaria'},
                                {'year': '1999',
                                 'detail': 'Later endorsed by NCRWC.',
                                 'label': 'Verma (FDs)',
                                 'id': 'e1-verma-fds'},
                                {'year': '2000',
                                 'detail': 'GoI resolution · Venkatachaliah.',
                                 'label': 'NCRWC set up',
                                 'id': 'e2-ncrwc-set-up'},
                                {'year': '2002',
                                 'detail': '249 recommendations.',
                                 'label': 'NCRWC report',
                                 'id': 'e3-ncrwc-report'},
                                {'year': '2007–10',
                                 'detail': 'Centre–State revisited.',
                                 'label': 'Punchhi',
                                 'id': 'e4-punchhi'}]},
                    {'id': 'woc-rev-pillars',
                     'type': 'pillars',
                     'title': 'Constitutional significance',
                     'items': [{'id': 'dem',
                                'articles': 'Democracy',
                                'label': 'Strengthen democracy',
                                'detail': 'Elections, parties, anti-defection.',
                                'tone': 'teal'},
                               {'id': 'gov',
                                'articles': 'Governance',
                                'label': 'Good governance',
                                'detail': 'Lokpal, CS Boards, sittings.',
                                'tone': 'olive'},
                               {'id': 'acc',
                                'articles': 'Account',
                                'label': 'Accountability',
                                'detail': 'Constructive NC · privileges curb.',
                                'tone': 'gold'},
                               {'id': 'tr',
                                'articles': 'Openness',
                                'label': 'Transparency',
                                'detail': 'RTI · whistle-blower · oaths.',
                                'tone': 'orange'},
                               {'id': 'inst',
                                'articles': 'Reform',
                                'label': 'Institutions',
                                'detail': 'NJC · EC collegium · ISC.',
                                'tone': 'terracotta'},
                               {'id': 'cb',
                                'articles': 'Balance',
                                'label': 'Checks & balances',
                                'detail': '356 restraint · Speaker→EC.',
                                'tone': 'maroon'}]},
                    {'id': 'woc-rev-final',
                     'type': 'callout',
                     'tone': 'tip',
                     'title': 'Final revision box',
                     'body': '**V-11-249 · 58-86-105 · review not rewrite · basic structure bound · NJC C2LP '
                             '· constructive NC · MoS 10% · Tenth Schedule→EC · aligned later: RTI / 91st / '
                             'Lokpal / NJAC attempt.**'}]}]

EDGES = [('working-of-the-constitution', 'parent', 'woc-background'),
 ('working-of-the-constitution', 'parent', 'woc-overview'),
 ('working-of-the-constitution', 'parent', 'woc-areas-reviewed'),
 ('working-of-the-constitution', 'parent', 'woc-fr-property'),
 ('working-of-the-constitution', 'parent', 'woc-dpsp-fd'),
 ('working-of-the-constitution', 'parent', 'woc-parliament-executive'),
 ('working-of-the-constitution', 'parent', 'woc-centre-state'),
 ('working-of-the-constitution', 'parent', 'woc-judiciary'),
 ('working-of-the-constitution', 'parent', 'woc-electoral-parties'),
 ('working-of-the-constitution', 'parent', 'woc-local-ne'),
 ('working-of-the-constitution', 'parent', 'woc-socio-economic'),
 ('working-of-the-constitution', 'parent', 'woc-accepted-pending'),
 ('working-of-the-constitution', 'parent', 'woc-comparisons'),
 ('working-of-the-constitution', 'parent', 'woc-current-affairs'),
 ('working-of-the-constitution', 'parent', 'woc-upsc-focus'),
 ('working-of-the-constitution', 'parent', 'woc-revision-sheet'),
 ('woc-background', 'related', 'woc-overview'),
 ('woc-overview', 'related', 'woc-areas-reviewed'),
 ('woc-areas-reviewed', 'related', 'woc-fr-property'),
 ('woc-dpsp-fd', 'related', 'fundamental-duties'),
 ('woc-dpsp-fd', 'related', 'fd-verma'),
 ('woc-judiciary', 'related', 'woc-accepted-pending'),
 ('woc-electoral-parties', 'related', 'woc-accepted-pending'),
 ('woc-centre-state', 'related', 'woc-comparisons'),
 ('woc-accepted-pending', 'related', 'woc-comparisons'),
 ('woc-current-affairs', 'related', 'woc-upsc-focus'),
 ('woc-upsc-focus', 'related', 'woc-revision-sheet'),
 ('woc-fr-property', 'related', 'fundamental-rights'),
 ('woc-parliament-executive', 'related', 'parliamentary-system')]

SAMPLE_PYQS = [(2010,
  'The National Commission to Review the Working of the Constitution was set up in which year, and who '
  'chaired it?',
  'Set up in 2000 by a GoI resolution; chaired by Justice M.N. Venkatachaliah (former CJI). Report submitted '
  'in 2002.',
  ['working-of-the-constitution', 'woc-overview', 'woc-upsc-focus']),
 (2015,
  'NCRWC made 249 recommendations. How were they classified by the type of action required?',
  '58 required constitutional amendment, 86 legislative measures, and 105 executive action.',
  ['working-of-the-constitution', 'woc-overview', 'woc-revision-sheet']),
 (2018,
  'Distinguish the mandate of the NCRWC from that of the Sarkaria Commission.',
  'Sarkaria focused on Centre–State relations (1983–88). NCRWC (2000–02) reviewed the working of the '
  'Constitution as a whole within parliamentary democracy and basic structure.',
  ['woc-comparisons', 'woc-background', 'woc-upsc-focus']),
 (2021,
  'What was NCRWC’s key proposal on the anti-defection law?',
  'All defectors (individual or group) must resign and contest afresh; defector’s toppling vote invalid; '
  'disqualification to be decided by the Election Commission, not the Speaker.',
  ['woc-electoral-parties', 'woc-accepted-pending'])]

LANDMARK_CASES = [{'slug': 'supreme-court-advocates-on-record-njac',
  'title': 'Supreme Court Advocates-on-Record Association v. Union of India (NJAC)',
  'court': CaseLaw.Court.SC,
  'year': 2015,
  'holding': 'Struck down the 99th Constitutional Amendment and NJAC Act — judicial appointments returned to '
             'the collegium framework. Often contrasted with earlier NJC-type reform ideas.',
  'concept_slugs': ['working-of-the-constitution', 'woc-judiciary', 'woc-accepted-pending'],
  'summary': 'Shows attempted institutional redesign of appointments (same reform stream as NCRWC’s NJC) '
             'failing basic-structure scrutiny on judicial independence.',
  'parties': 'Supreme Court Advocates-on-Record Association v. Union of India (NJAC)'},
 {'slug': 'kuldip-nayar-rajya-sabha-domicile',
  'title': 'Kuldip Nayar v. Union of India',
  'court': CaseLaw.Court.SC,
  'year': 2006,
  'holding': 'Upheld removal of the domicile requirement for Rajya Sabha candidature — opposite drift from '
             'NCRWC’s recommendation to keep domicile for federal character.',
  'concept_slugs': ['woc-parliament-executive', 'woc-accepted-pending'],
  'summary': 'Useful contrast when discussing NCRWC’s Parliament recommendations on RS domicile.',
  'parties': 'Kuldip Nayar v. Union of India'}]

AMENDMENTS = [{'number': 91,
  'year': 2003,
  'title': 'Ninety-first Amendment',
  'summary': 'Capped Council of Ministers size (generally 15% of the popular House) and tightened '
             'anti-defection-related disqualification for ministerial office — same reform stream as NCRWC’s '
             'MoS-size concern (NCRWC had recommended 10%).',
  'effect': 'Constitutional MoS ceiling at 15% (not NCRWC’s 10%).',
  'concept_slugs': ['working-of-the-constitution', 'woc-parliament-executive', 'woc-accepted-pending']},
 {'number': 99,
  'year': 2014,
  'title': 'Ninety-ninth Amendment (NJAC)',
  'summary': 'Sought to replace the collegium with the National Judicial Appointments Commission. Later '
             'struck down — often discussed alongside NCRWC’s National Judicial Commission idea.',
  'effect': 'NJAC created then invalidated; collegium restored.',
  'concept_slugs': ['woc-judiciary', 'woc-accepted-pending', 'woc-comparisons']},
 {'number': 106,
  'year': 2023,
  'title': 'One Hundred and Sixth Amendment',
  'summary': 'Women’s reservation in Lok Sabha and State Assemblies — an aligned later development relative '
             'to NCRWC’s women’s empowerment recommendations.',
  'effect': 'Constitutional reservation for women in LS and State Assemblies (deferred operationalisation).',
  'concept_slugs': ['woc-socio-economic', 'woc-current-affairs']}]

class Command(BaseCommand):
    help = (
        "Seed Working of the Constitution chapter (Laxmikanth Part XI / Ch.90 NCRWC) "
        "— visual UPSC revision."
    )

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
                "title": "Working of the Constitution",
                "sort_order": 1,
                "book_ref": "Laxmikanth 8th Ed, Ch. 90 / Part XI",
                "summary": (
                    "Visual revision of Part XI / Ch.90 — NCRWC mental model, 249 recommendations, "
                    "theme matrices, accepted vs pending, Sarkaria–Punchhi comparisons, and exam sheet."
                ),
                "is_published": True,
            },
        )

        hub, _ = Concept.objects.update_or_create(
            subject=subject,
            slug=HUB_SLUG,
            defaults={
                "title": "Working of the Constitution",
                "summary": (
                    "NCRWC (2000–02, Venkatachaliah) — review the Constitution’s working within "
                    "parliamentary democracy and basic structure; 249 advisory recommendations."
                ),
                "body": (
                    "## How to revise this chapter\n\n"
                    "Start with the **health-check mental model**, then lock **V-11-249** and "
                    "**58-86-105**. Walk the **fourteen recommendation themes**, then finish with "
                    "**Accepted vs Pending**, **Comparisons**, and the **one-page sheet**. "
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
            ref="Laxmikanth Ch. 90",
            excerpt=(
                "National Commission to Review the Working of the Constitution "
                "(Part XI — Working of the Constitution)."
            ),
            sort_order=0,
        )

        woc_slugs = set(by_slug.keys())
        related_outside = {
            "fundamental-duties",
            "fd-verma",
            "fundamental-rights",
            "parliamentary-system",
        }
        ConceptEdge.objects.filter(
            source__slug__in=woc_slugs, source__subject=subject
        ).filter(target__slug__in=woc_slugs | related_outside).delete()

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
                by_slug[s]
                for s in case_data["concept_slugs"]
                if s in by_slug
            ]
            if concepts:
                existing = list(case.concepts.all())
                case.concepts.set({*existing, *concepts})

        for amd_data in AMENDMENTS:
            payload = {k: v for k, v in amd_data.items() if k != "concept_slugs"}
            amendment, created = ConstitutionalAmendment.objects.get_or_create(
                academy=academy,
                number=payload["number"],
                defaults=payload,
            )
            if not created:
                for field in ("title", "year", "summary", "effect"):
                    if not getattr(amendment, field, None) and payload.get(field):
                        setattr(amendment, field, payload[field])
                amendment.save()
            concepts = [
                by_slug[s]
                for s in amd_data["concept_slugs"]
                if s in by_slug
            ]
            if concepts:
                existing = list(amendment.concepts.all())
                amendment.concepts.set({*existing, *concepts})

        self.stdout.write(
            self.style.SUCCESS(
                f"Working of the Constitution chapter seeded ({academy.slug}): "
                f"{chapter.title} with {len(CLUSTERS) + 1} concepts, "
                f"{created_edges} new edges, {len(LANDMARK_CASES)} cases, "
                f"{len(AMENDMENTS)} amendments, {len(SAMPLE_PYQS)} PYQs."
            )
        )
