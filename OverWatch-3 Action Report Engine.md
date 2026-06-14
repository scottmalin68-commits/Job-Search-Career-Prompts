# METADATA
· Project OverWatch: Phase 3 Landscape Mapping Engine
· Author: Scott Malin, CISSP
· Version: 1.11.0
· Changelog (v1.11.0):
  · Added Quiet Hiring indicators and Stealth Expansion signals to track unadvertised team shifts.
  · Integrated Network Status tagging to flag Warm Network and Alumni connections based on past company overlap.
  · Renamed Section 4 to Quiet Hiring & Momentum Detection to refocus engine output on hidden market footprints.
· Changelog (v1.10.0):
  · Added Previous Report optional input to enable historical delta tracking.
  · Introduced Delta State Logic to tag signals as [NEW] or [PERSISTENT].
  · Updated output schema to highlight market changes and prevent duplicate action items.
· Changelog (v1.9.0):
  · Restructured output schema to introduce a Strategic TLDR & Action Matrix immediately following Section 1.
  · Moved top alignment lists from the bottom summary into the front-loaded TLDR section for immediate scannability.
  · Refructured the final section into a profile alignment and technical gap analysis matrix.

# OPTIONAL INPUTS

Career Profile (Preferred)

Resume (Accepted)

Previous Report (Optional)

If a Career Profile or Resume is provided:
· Use it to tune the analysis. High-alignment identities, technologies, departments, and organizations matching the user's documented background must be prioritized and highlighted.
· Compare observed data against documented experience, certifications, accomplishments, target roles, and stated career objectives.

If a Previous Report is provided:
· Perform a differential analysis between the new source JSON and the previous report.
· Tag entries or clusters as [NEW] if they appear for the first time in the current dataset.
· Tag entries or clusters as [PERSISTENT] if they were present in the previous report.
· Highlight any status or metric changes (e.g., an identity changing companies or a cluster increasing in signal strength).
· Ensure the Suggested Action Plan focuses on new leverage points rather than repeating identical tasks from the previous run.

If none are provided:
· Perform landscape analysis normally.
· Omit Target Alignment scoring and delta tracking.
· Do not infer user interests or career objectives.

# TARGET ALIGNMENT FRAMEWORK

IMPORTANT:
Target Alignment is independent from Confidence and Opportunity Value.

Confidence answers: "How certain are we that this signal was correctly identified?"
Opportunity Value answers: "How strategically useful is this signal?"
Target Alignment answers: "How closely does this signal align with the user's documented background and target direction?"

Assign one:

## VERY HIGH
Requirements: Strong overlap with target roles, technology overlap, functional overlap, and comparable seniority level.
## HIGH
Requirements: Significant overlap, adjacent technologies, and similar functional area.
## MODERATE
Requirements: Partial overlap, related discipline, and transferable experience.
## LOW
Requirements: Minimal overlap and limited relevance to documented goals.
## UNKNOWN
Requirements: Insufficient evidence to evaluate.

Only use information explicitly present within the Career Profile, Resume, or Source JSON. Do not infer interests or capabilities.

# STRICT DELIVERY PROTOCOL
Every engine execution must result in exactly two sequential codeblocks with zero pre-text, post-text, conversational framing, or meta-commentary.

## Codeblock 1: Metadata Destination
Deliver only the target text file name tracking variable using today's system date:
OverwatchReport-[MM-DD-YYYY].md

## Codeblock 2: The Intel Payload
Deliver the complete landscape report using clean Markdown layout (headings, bullets, dividers) based strictly on the sequence defined in the Presentation Output schema.

# LANDSCAPE PROCESSING ENGINE LOGIC

## STEP 2B — HISTORICAL DELTA ANALYSIS
*(Only run this step if a Previous Report is provided)*
· Compare all incoming identities, organizations, and technology arrays against the previous report.
· Map persistence: identify signals that remain stable, signals that have dropped off, and entirely new signals.

## STEP 2C — OPPORTUNITY CLUSTER ANALYSIS
For each technical domain group, identify:
Associated Identities:
· Name (If unavailable, use: "Unnamed Identity [Title/Identifier]")
· Title
· Confidence
· Delta State: [NEW / PERSISTENT] (If previous report is available)

If Target Alignment is available:
Cluster Alignment: [Very High / High / Moderate / Low / Unknown]
Cluster Alignment must be based solely on explicit profile or resume evidence.

## STEP 2D — OBSERVED OPPORTUNITY MAPPING
Review all records collectively to identify evidence-supported concentrations.

For each observed concentration:
Organization:
Observed Opportunity Theme:
Observed Evidence:
Associated Identities: (If name is missing, use: "Unnamed Identity [Title]")
Associated Technologies:
Confidence:
Opportunity Value:
If Target Alignment is available: Target Alignment:
If Previous Report is available: Delta State: [NEW / PERSISTENT / MODIFIED]

Use only evidence directly supported by observed records.
Acceptable language: Opportunity area observed, Technical specialization observed, Team focus observed, Role concentration observed, Functional concentration observed.
Do not state: Open jobs exist, Hiring is occurring, Future hiring is guaranteed.

## STEP 3 — NETWORK ENGAGEMENT CLASSIFICATION
For every Tier 1 identity assign:
Engagement Classification: [CONNECT / FOLLOW / MONITOR]
· Network Status: Tag as [WARM NETWORK / ALUMNI] if the identity shares a past organization or employer with the user.
If Career Profile or Resume is provided also assign: Target Alignment.
If Previous Report is available: Delta State: [NEW / PERSISTENT]
Provide evidence-based rationale focusing on common ground, shared networks, or institutional overlap.

## STEP 4A — ORGANIZATIONAL WATCHLIST
Identify organizations exhibiting multiple independent signals.

For each organization:
Organization:
Observed Signals: [Leadership visibility, Technical identity concentration, Technology concentration, Department concentration, Opportunity cluster activity, Stealth Expansion (internal team shifts or new headcount with no public job postings)]
Cluster Strength:
Confidence Distribution:
Opportunity Value:
If available: Target Alignment:
If Previous Report is available: Delta State: [NEW / PERSISTENT]
Evidence Summary:

Do not state hiring intent. Report only observed evidence.

# PRESENTATION OUTPUT SCHEMA

SECTION 1: QUERY EFFECTIVENESS ANALYSIS
[Provide metrics and Direct match analysis from source data]

---

SECTION 2: STRATEGIC TLDR & ACTION MATRIX
*(Only display this section if a Career Profile or Resume was provided)*
### Executive Summary
[A concise, 2-3 sentence engineering-grade synthesis of the landscape's primary technical concentrations and their direct relevance to the user's profile. If a previous report was provided, explicitly note the volume of new signals discovered since the last run]
### Top High-Alignment Targets
· **Top 3 Organizations:** [Extracted from observed data. Prepend "[NEW]" if applicable]
· **Top 3 Opportunity Clusters:** [Extracted from observed data. Prepend "[NEW]" if applicable]
· **Top 3 Target Identities:** [Extracted from Tier 1 data. Prepend "[NEW]" if applicable]
### Suggested Action Plan
[3-4 direct, evidence-based next steps for network engagement or positioning. If a previous report was provided, ensure these steps focus primarily on newly surfaced signals or changes in the landscape]

---

SECTION 3: OPPORTUNITY CLUSTER ANALYSIS
[Deliver clusters with associated technologies, identities, cluster alignment metrics, and NEW/PERSISTENT tags if a previous report is available]

---

SECTION 4: QUIET HIRING & MOMENTUM DETECTION
[List organizational signals without speculating on exact hiring counts. Highlight stealth expansion indicators, leadership changes, or sudden cluster growth where public job ads are missing]

---

SECTION 5: OBSERVED OPPORTUNITY MAPPING
[Deliver concentrations containing themes, evidence indicators, associated tech arrays, and delta markers]

---

SECTION 6: ORGANIZATIONAL WATCHLIST
[Deliver compound organizational signal summaries, explicitly grouping or flagging new additions to the watchlist]

---

SECTION 7: TIER 1 — VERIFIED IDENTITIES
For each entry:
Name: (If missing, use: "Unnamed Identity [Unique Attribute]")
Title:
Company:
LinkedIn URL (if available):
Confidence:
Opportunity Value:
If available: Target Alignment:
If available: Delta State:
Engagement Classification:
Network Status:
Structural Clues: (Bullet list)

---

SECTION 8: TIER 2 — UNMAPPED IDENTITY ANCHORS
[Profiles with partial metadata structural hooks. Include delta flags if tracking changes]

---

SECTION 9: TIER 3 — ANONYMOUS STRUCTURAL SIGNALS
[Anonymized architectural case vectors]

---

SECTION 10: STRATEGIC ALIGNMENT & GAP ANALYSIS
*(Only display this section if a Career Profile or Resume was provided)*
### Profile Alignment Matrix
[Brief breakdown of how the observed technical environments match the user's current certifications, core technologies, and experience level]
### Observed Technical Gaps
[Enumerate specific technologies, frameworks, or tools heavily present in high-value clusters that are missing or underrepresented in the user's profile. Note if these gaps are persistent across multiple analysis runs]