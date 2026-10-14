# Doctrine + comparison + master revision bodies for Judgements & Doctrines.


def doctrine_body(definition, basis, origin, judgements, principles, exceptions, upsc):
    return (
        f"**Definition:** {definition}\n\n"
        f"**Constitutional Basis:** {basis}\n\n"
        f"**Origin:** {origin}\n\n"
        f"**Leading Judgements:** {judgements}\n\n"
        f"**Key Principles:** {principles}\n\n"
        f"**Exceptions:** {exceptions}\n\n"
        f"**UPSC Relevance:** {upsc}\n"
    )


DOC_SEVERABILITY = doctrine_body(
    definition="If part of a law is unconstitutional, only that part is void if it can be separated; the rest may stand.",
    basis="Art.13(1)/(2) — void to the extent of inconsistency/contravention.",
    origin="Borrowed common-law separability; crystallised in early SC cases (Gopalan, Balsara, R.M.D. Chamarbaugwala).",
    judgements="A.K. Gopalan (1950); State of Bombay v F.N. Balsara (1951); R.M.D. Chamarbaugwala (1957); Minerva Mills (1980); Kihoto Hollohan (1992).",
    principles="Legislative intent controls; if valid and invalid parts inextricably mixed, whole falls; leftover must be a workable code without judicial rewriting.",
    exceptions="Single scheme cases; truncated residue that is a different law; inseparable mixtures.",
    upsc="Often paired with eclipse; know Table 94.1 examples.",
)

DOC_WAIVER = doctrine_body(
    definition="Intentional relinquishment of a known right or privilege.",
    basis="General jurisprudence — but **not applicable to Fundamental Rights** in India.",
    origin="Common-law waiver; Indian position settled against FR waiver.",
    judgements="Basheshar Nath line / FR jurisprudence holding citizens cannot waive FRs.",
    principles="FRs are a matter of public policy; State cannot plead waiver to sustain FR violation.",
    exceptions="Ordinary contractual/statutory rights may be waived; FRs cannot.",
    upsc="One-line Prelims: Doctrine of waiver does **not** apply to FRs in India.",
)

DOC_ECLIPSE = doctrine_body(
    definition="A pre-Constitution law inconsistent with FRs is not dead — it is overshadowed (eclipsed) and becomes enforceable again if the inconsistency is removed (e.g. by amendment).",
    basis="Art.13(1) — pre-Constitution laws void to the extent of inconsistency with FRs.",
    origin="Bhikaji Narain Dhakras and related early cases.",
    judgements="Bhikaji Narain Dhakras; Deep Chand themes; contrast with post-Constitution voidness under Art.13(2).",
    principles="Applies primarily to **pre-Constitution** laws; eclipse lifts when inconsistency goes.",
    exceptions="Post-Constitution laws violating FRs are stillborn under Art.13(2) (not merely eclipsed) — classic exam distinction.",
    upsc="Eclipse vs Severability vs Waiver — frequent confusion trio.",
)

DOC_FEDERAL_BODY = """## Federal / legislative competence doctrines

### Doctrine of Pith and Substance
""" + doctrine_body(
    definition="Find the true nature and character of a law; incidental encroachment on another list does not invalidate it if the pith belongs to the enacting legislature’s list.",
    basis="Seventh Schedule distribution (Arts. 245–254).",
    origin="Canadian/Australian federal jurisprudence adapted in India.",
    judgements="Prafulla Kumar Mukherjee; State of Bombay v F.N. Balsara; later federal competence cases.",
    principles="Look at substance not form; incidental trenches allowed.",
    exceptions="Colourable legislation / fraud on the Constitution; occupied field / repugnancy in Concurrent List.",
    upsc="First tool when Union vs State list conflict appears.",
) + """
### Doctrine of Colourable Legislation
""" + doctrine_body(
    definition="What cannot be done directly cannot be done indirectly — Legislature cannot transgress competence under a pretence.",
    basis="Federal distribution + constitutional limits; related to fraud on the Constitution.",
    origin="Federal colourability jurisprudence.",
    judgements="K.C. Gajapati Narayan Deo; later competence/colourability cases.",
    principles="Examine substance and effect, not label; motive alone is not enough — look at competence trespass.",
    exceptions="If pith is within competence, law stands despite incidental effects.",
    upsc="Pair with pith and substance — colourable is the ‘fraudulent packaging’ counterpart.",
) + """
### Doctrine of Occupied Field
""" + doctrine_body(
    definition="When Union law comprehensively occupies a Concurrent List field, State law in that field may be inoperative to the extent of conflict/occupation.",
    basis="Arts. 246, 254 — Concurrent List; repugnancy rules.",
    origin="Federal occupied-field ideas linked to Art.254 repugnancy.",
    judgements="Classic Art.254 repugnancy cases; State laws yielding to exhaustive Central codes.",
    principles="Examine whether Parliament intended exhaustive coverage; direct conflict vs field occupation.",
    exceptions="Presidential assent pathways under Art.254(2); later Union law can still prevail.",
    upsc="Do not confuse with pith and substance (list entry) vs occupied field (Concurrent clash).",
) + """
### Doctrine of Territorial Nexus
""" + doctrine_body(
    definition="A State law can have extraterritorial effects if there is a real territorial nexus with the State.",
    basis="Art.245 — State laws may apply outside territory if nexus exists.",
    origin="Tax and regulatory nexus cases.",
    judgements="State of Bombay v R.M.D. Chamarbaugwala; Tata Iron & Steel tax nexus line.",
    principles="Nexus must be real and not illusory; used often in tax statutes.",
    exceptions="No nexus → invalid extraterritorial reach.",
    upsc="One-liner for Art.245 State extraterritoriality.",
) + """
### Implied Powers / Incidental & Ancillary Powers
""" + doctrine_body(
    definition="Power to legislate on a matter includes ancillary and incidental powers necessary to make the law effective; implied powers fill gaps fairly required by express grants.",
    basis="Reading Seventh Schedule entries broadly (ancillary doctrine).",
    origin="Federal interpretation practice.",
    judgements="United Provinces v Atiqa Begum themes; later entry-interpretation cases.",
    principles="Ancillary does not mean a new independent subject; cannot invade another list’s pith.",
    exceptions="Colourable expansion beyond competence.",
    upsc="Often a supporting sentence in federalism answers.",
)

DOC_INTERP_BODY = """## Interpretation doctrines

### Harmonious Construction
""" + doctrine_body(
    definition="Interpret constitutional / statutory provisions so they work together; avoid conflict if a consistent reading is possible.",
    basis="Holistic reading of the Constitution (FRs, DPSPs, institutional provisions).",
    origin="General interpretation canon; constitutionalised in FR–DPSP and institutional conflict cases.",
    judgements="Minerva Mills (FR–DPSP harmony); numerous conflict-avoidance holdings.",
    principles="Give effect to both provisions; prefer interpretation that reconciles.",
    exceptions="Where conflict is irreconcilable, hierarchy rules (e.g. basic structure / express precedence) apply.",
    upsc="Standard Mains phrase with Minerva Mills.",
) + """
### Liberal Interpretation (Literal / Purposive / Creative)
""" + doctrine_body(
    definition="Constitution as a living document — courts may use literal, purposive, or creative interpretation to realise constitutional values.",
    basis="Judicial role under Arts. 32/136/142 and constitutional supremacy.",
    origin="Culminates in expansive readings post-Maneka; Ch.94 liberal interpretation discussion.",
    judgements="Maneka Gandhi; Kesavananda (creative basic structure); rights-expansion cases.",
    principles="Literal: text first. Purposive: object and scheme. Creative: fill gaps to protect values (with institutional caution).",
    exceptions="Cannot rewrite clear text contrary to basic structure limits on courts either — legitimacy debates (activism).",
    upsc="Link to judicial activism vs restraint.",
) + """
### Prospective Overruling
""" + doctrine_body(
    definition="Court overrules prior law but applies the new rule only to future cases (or from a specified date), protecting past transactions.",
    basis="Judicial craft under Art.141 — declared law with temporal modulation.",
    origin="Golaknath (1967) famously applied it in India.",
    judgements="Golaknath; later selective uses.",
    principles="Balances justice of new rule with reliance on old rule.",
    exceptions="Not routine — used when retrospectivity would be chaotic.",
    upsc="Associate first with Golaknath.",
) + """
### Doctrine of Precedent
""" + doctrine_body(
    definition="Lower courts bound by higher court ratios; SC decisions bind all courts (Art.141).",
    basis="Art.141 — law declared by SC binding.",
    origin="Common-law stare decisis adapted to Indian hierarchy.",
    judgements="Practice directions on benches; larger Bench overruling smaller.",
    principles="Ratio binds; obiter persuasive; larger Bench can overrule.",
    exceptions="Per incuriam; distinguishing on facts; larger Bench reconsideration.",
    upsc="Art.141 one-liner + Bench strength hierarchy.",
)

DOC_EXTRAS_BODY = """## Extra doctrines (UPSC toolkit)

### Basic Structure
Limit on Art.368 — Parliament cannot destroy the Constitution’s basic features (Kesavananda). Open full [Basic Structure](/concepts/basic-structure) chapter for elements table.

### Judicial Review
Power of courts to test legislative/executive action (and amendments) for constitutionality — itself a basic feature (Indira, Minerva, L. Chandra Kumar, Coelho).

### Reading Down
Prefer an interpretation that saves a statute by narrowing it to constitutional bounds (e.g. Navtej on s.377).

### Proportionality
State restriction must have legitimate aim, rational nexus, necessity, and balancing — central after privacy/Aadhaar line.

### Public Trust
State as trustee of natural resources for the people (environment cases / M.C. Mehta line).

### Legitimate Expectation
Fairness doctrine in administrative law — procedural/substantive expectations from past practice/promises (limits apply).

### Doctrine of Pleasure
Union/State servants hold office during pleasure of President/Governor (Arts. 310/311 constraints).

### Doctrine of Lapse
Certain recommendations/office matters lapse on specified events (contextual — e.g. historical privy purse/political office contexts in polity questions; don’t over-extend).

**Mnemonic (federal):** **Pith – Colour – Occupied – Nexus** (+ Incidental).
**Mnemonic (FR tools):** **Eclipse – Severability – (No) Waiver**.
"""

MASTER_BODY = """## Master revision — Judgements & Doctrines

### Exam in 5 minutes
1. **S-G-K-I-M-C** amendment arc  
2. **GJM** Art.21 arc (Gopalan → Jabalpur → Maneka) + **Puttaswamy**  
3. **Bommai** = 356 review + secularism  
4. **Coelho** = 9th Schedule not immune  
5. **Eclipse ≠ Severability**; **Waiver ≠ FRs**  
6. **NJAC (2015)** struck; collegium returns  

### Master landmark table (flagships)

| Case | Year | One-line holding |
|------|------|------------------|
| Gopalan | 1950 | Narrow Art.21 |
| Champakam | 1951 | FR > DPSP → 15(4) |
| Shankari | 1951 | Can amend FRs |
| Golaknath | 1967 | Cannot amend FRs |
| Kesavananda | 1973 | Basic structure |
| Indira Gandhi | 1975 | 39th/329A(4) void |
| Jabalpur | 1976 | Emergency habeas denial (bad law) |
| Maneka | 1978 | Just-fair-reasonable Art.21 |
| Minerva | 1980 | Limited amending power basic |
| Indra Sawhney | 1992 | Mandal; 50%; creamy layer |
| Second Judges | 1993 | Collegium |
| Bommai | 1994 | Art.356 justiciable |
| Vishaka | 1997 | Harassment guidelines |
| Coelho | 2007 | 9th Schedule reviewable |
| NJAC | 2015 | 99th void |
| Shayara Bano | 2017 | Triple talaq void |
| Puttaswamy | 2017 | Privacy FR |
| Navtej | 2018 | s.377 read down |

### Article-wise anchors
- **Art.13/368:** Shankari → Golaknath → Kesavananda → Minerva → Coelho  
- **Art.21:** Gopalan → Maneka → expansions table → Puttaswamy  
- **Art.356:** Bommai  
- **Art.19:** Romesh Thappar; Shreya Singhal; Anuradha Bhasin; ADR  
- **Art.16:** Indra Sawhney  

### PYQ themes
Basic structure elements · Art.21 expansions · Bommai propositions · Privacy · Collegium/NJAC · 9th Schedule · Eclipse/Severability · Harmonious construction · FR vs DPSP · Judicial review vs activism
"""
