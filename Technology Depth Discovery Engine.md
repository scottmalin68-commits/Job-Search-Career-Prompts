# TITLE: Technology Depth Discovery Engine
# VERSION: 1.1.1
# AUTHOR: Scott Malin, CISSP
# LAST UPDATED: 2026-06-22
# Career Profile enhancement Prompt

The Technology Depth Discovery Engine (TDDE) analyzes a jobseeker's professional materials, including a resume, profile, portfolio, application packet, skills inventory, project summary, certification record, academic work, volunteer experience, or similar reference document, and produces an evidence-based Technology Proficiency Matrix.

Unlike traditional self-assessments, this system derives proficiency levels from documented experience, accomplishments, responsibilities, project ownership, and measurable outcomes.

The objective is to create a reusable technology intelligence layer that can be appended to a jobseeker profile and consumed by downstream systems such as:
- Resume Tailoring Systems
- Interview Preparation Systems
- Competency Fit Analysis Engines
- Career Intelligence Systems
- Skills Gap Analysis Tools
- Personal Career Operating Systems

The system prioritizes evidence over assumptions and confidence scoring over speculation.

--------------------------------------------------
CHANGELOG
--------------------------------------------------

v1.1.1 — 2026-06-22
- Added explicit metric decoupling warning to Phase 5 to prevent confidence scores from lazy-matching documentation strength scores during processing fatigue.

v1.1.0 — 2026-06-22
- Added Recency Adjustment Rule to prevent historical experience from inflating current depth assessments.
- Added Scale Weighting Rule to recognize enterprise ownership, production scope, and organizational impact.
- Added Framework Assessment Rule for more accurate scoring of compliance and governance experience.
- Added Documentation Strength Score to measure how well proficiency is supported by source materials.
- Added Level U — Documentation Insufficient to separate unsupported mentions from true Awareness-level experience.
- Clarified independence of proficiency, confidence, and documentation quality assessments.

v1.0.1 — 2026-06-22
- Added Strict Grounding Rule to prevent context leaks and inferred adjacent technologies.
- Added Ambiguity Rule to force low-tier defaults instead of model guessing.
- Added token and fatigue constraints (15-word bullet limits, 3-bullet summary limits) to maintain consistency across long outputs.

==================================================
SYSTEM GUARDRAILS (ANTI-HALLUCINATION & ANTI-DRIFT)
==================================================

> Strict Grounding Rule:
>
> Every single bullet point in the Technology Evidence Map must map back to a specific, verifiable sentence or phrase in the source material.
>
> If a specific tool version, environment scale, adjacent technology, integration, capability, or action is not explicitly written, it does not exist.
>
> Do not infer related tools, platforms, products, vendors, frameworks, or ecosystems.

> Ambiguity Rule:
>
> If the evidence for a technology is ambiguous, default to:
>
> - Low Confidence
> - Level 1 — Awareness
>
> Do not split the difference.
> Do not estimate.
> Do not guess.

> Recency Adjustment Rule:
>
> When multiple proficiency levels appear plausible, favor the level supported by the most recent documented experience.
>
> Historical expertise may be noted separately but should not automatically represent current operational depth.
>
> Current experience should be weighted more heavily than legacy experience.

> Scale Weighting Rule:
>
> Environment size, production criticality, regulatory requirements, business impact, and organizational scope may strengthen depth and confidence assessments when explicitly supported by evidence.
>
> Enterprise ownership should be weighted more heavily than small-scale administration when both are otherwise comparable.

> Framework Assessment Rule:
>
> Governance frameworks, compliance standards, and security methodologies must be evaluated based on demonstrated implementation, assessment, audit participation, control ownership, compliance leadership, program development, or strategic governance activities.
>
> Mere framework mentions do not constitute proficiency.

> Length & Fatigue Control:
>
> - Evidence bullets must remain under 15 words.
> - Executive Summary sections are limited to 3 bullets each.
> - Avoid unnecessary narrative.
> - Maintain consistent formatting across all phases.

Analyze the supplied jobseeker materials.

Perform all phases sequentially.

Do not skip phases.
Do not infer expertise without evidence.
If insufficient evidence exists, explicitly state uncertainty.

==================================================
PHASE 1 — TECHNOLOGY INVENTORY DISCOVERY
==================================================

Identify and catalog all technologies referenced within the supplied material.

Include:

Security Technologies
- EDR
- XDR
- PAM
- SIEM
- Vulnerability Management Platforms
- IAM Solutions
- Security Products

Infrastructure Technologies
- Operating Systems
- Virtualization
- Networking
- Endpoint Management

Cloud Technologies
- AWS
- Azure
- GCP
- Cloud Security Platforms

Programming and Automation
- PowerShell
- Python
- Bash
- Other Languages

Frameworks and Standards
- NIST
- CIS Controls
- PCI DSS
- SOC2
- ISO 27001
- Other Governance Frameworks

Methodologies
- DevSecOps
- Agile
- ITIL
- Incident Response
- Threat Modeling

Create a consolidated technology inventory.

Deduplicate:
- Equivalent technologies
- Duplicate naming conventions
- Product aliases

Never invent technologies.

==================================================
PHASE 2 — EVIDENCE COLLECTION
==================================================

For each identified technology:

Collect all supporting evidence.

Search for:
- Ownership
- Administration
- Engineering
- Design
- Architecture
- Migration
- Automation
- Deployment
- Troubleshooting
- Leadership
- Strategic Planning

Capture evidence using concise bullets.
Maximum: 15 words per bullet.

Example:

Technology:
PowerShell

Evidence:
- Developed automation scripts
- Automated vulnerability reporting
- Reduced manual effort through scripting

==================================================
PHASE 3 — DOCUMENTATION STRENGTH ASSESSMENT
==================================================

Evaluate how well the source material documents the technology.

Documentation Strength:

Excellent
- Multiple accomplishments
- Quantified impact
- Clear ownership
- Repeated evidence

Good
- At least one meaningful accomplishment
- Clear practical usage

Fair
- Mentioned with limited supporting context

Poor
- Listed but largely unsupported

This score evaluates documentation quality.
It does NOT evaluate proficiency.

A technology may have:
- High proficiency
- Poor documentation

or

- Moderate proficiency
- Excellent documentation

==================================================
PHASE 4 — PROFICIENCY ASSESSMENT
==================================================

Assign proficiency based only on evidence.

Use the following scale.

Level U — Documentation Insufficient
Indicators:
- Listed only
- No usable evidence
- No observable activity
- Experience cannot be validated

Level 1 — Awareness
Indicators:
- Mentioned
- Limited exposure
- No direct usage evidence

Level 2 — Working Knowledge
Indicators:
- Routine usage
- Basic administration
- User-level familiarity

Level 3 — Intermediate
Indicators:
- Repeated practical usage
- Project participation
- Independent operation

Level 4 — Advanced
Indicators:
- Engineering
- Design
- Optimization
- Significant implementation work

Level 5 — Subject Matter Expert (SME)
Indicators:
- Enterprise ownership
- Primary support responsibility
- Platform leadership
- Deep troubleshooting expertise

Level 6 — Strategic Authority
Indicators:
- Architecture ownership
- Enterprise strategy
- Organizational standards creation
- Cross-functional leadership

Assign the highest level fully supported by evidence.
Never inflate ratings.

Never assign Level 5 or Level 6 without direct evidence.

==================================================
PHASE 5 — CONFIDENCE ASSESSMENT
==================================================

Confidence measures evidence quality and validity trail. Do not match it automatically to the Phase 3 score; evaluate it independently.

Assign confidence levels.

High Confidence
Requirements:
- Multiple supporting examples
- Strong documented ownership
- Clear evidence trail

Medium Confidence
Requirements:
- Some evidence
- Partial ownership
- Limited supporting detail

Low Confidence
Requirements:
- Sparse evidence
- Ambiguous references
- Assumptions would otherwise be required

Confidence measures evidence quality.
Confidence does NOT measure skill level.

==================================================
PHASE 6 — UNCERTAINTY DISCOVERY
==================================================

Identify technologies where evidence is insufficient.

For each item:

Generate targeted clarification questions.

Questions must:
- Be concise
- Resolve uncertainty
- Avoid leading language

Example:

Azure was identified but ownership level is unclear.
Which best describes your experience?
A. User
B. Administrator
C. Engineer
D. Architect

Only generate questions for:
- Low Confidence technologies
- Documentation Insufficient technologies
- Ambiguous technologies

Do not generate questions for High Confidence technologies.

==================================================
PHASE 7 — TECHNOLOGY PROFICIENCY MATRIX
==================================================

Generate:

## Technology Proficiency Matrix

### Strategic Authority
[List]

### SME
[List]

### Advanced
[List]

### Intermediate
[List]

### Working Knowledge
[List]

### Awareness
[List]

### Documentation Insufficient
[List]

==================================================
PHASE 8 — TECHNOLOGY EVIDENCE MAP
==================================================

For every technology:

Technology:
[Name]

Depth:
[Level]

Confidence:
[Level]

Documentation Strength:
[Level]

Evidence:
- Item (Max 15 words)
- Item (Max 15 words)
- Item (Max 15 words)

Repeat for all identified technologies.

==================================================
PHASE 9 — SKILL GAP DISCOVERY
==================================================

Identify potential weaknesses.

Examples:
- Frequently requested market technologies not present
- Emerging technologies with limited evidence
- Documentation gaps
- Depth inconsistencies
- Overrepresented versus underrepresented areas

Classify each finding:
Low Priority
Medium Priority
High Priority

Provide rationale.

Focus on both:
- Skill gaps
- Documentation gaps

==================================================
PHASE 10 — CAREER INTELLIGENCE SUMMARY
==================================================

Generate an Executive Summary.

Include:

1. Strongest Technology Domains
   - Maximum 3 bullets

2. Demonstrated Areas of Expertise
   - Maximum 3 bullets

3. Technologies Showing Enterprise Ownership
   - Maximum 3 bullets

4. Technologies Requiring Validation
   - Maximum 3 bullets

5. Recommended Additions to Jobseeker Materials
   - Maximum 3 bullets

Limit observations to actionable findings.

==================================================
ADDITIONAL CONSIDERATIONS
==================================================

- Distinguish execution from oversight.
- Distinguish implementation from support.
- Distinguish administration from architecture.
- Note recency when available.
- Note duration when available.
- Note frequency when available.
- Capture environment scale when available.
- Capture production scope when available.
- Capture regulatory environments when available.
- Separate direct experience from certification exposure.
- Separate direct experience from coursework.
- Separate direct experience from lab work.
- Separate direct experience from self-study.
- Note measurable business outcomes.
- Note risk reduction outcomes.
- Note cost avoidance outcomes.
- Note operational efficiency outcomes.
- Highlight weak documentation areas.
- Recommend stronger accomplishment statements where evidence is thin.
- Flag adjacent technologies only when explicitly evidenced.
- Consider implementation, administration, engineering, architecture, leadership, and strategy separately.

==================================================
FINAL OUTPUT REQUIREMENTS
==================================================

The final output must contain:

1. Technology Inventory
2. Technology Proficiency Matrix
3. Technology Evidence Map
4. Clarification Questions (If Required)
5. Skill Gap Discovery
6. Career Intelligence Summary

==================================================
MANDATORY RESTRICTIONS
==================================================

Never invent technologies.
Never infer expertise from job titles alone.
Never infer adjacent technologies.
Never assign SME or Strategic Authority without documented evidence.
Never elevate proficiency because a certification exists.

If evidence is insufficient:
State:
"Insufficient evidence available."

Do not speculate.
Confidence ratings must reflect evidence quality.
Documentation Strength must reflect documentation quality.
Proficiency must reflect demonstrated depth.
Treat all three as independent assessments.

