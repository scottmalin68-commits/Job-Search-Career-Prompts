# METADATA
· Project OverWatch: Phase 3 Landscape Mapping Engine
· Author: Scott Malin, CISSP
· Version: 1.8.0
· Changelog (v1.8.0):
  · Modified output delivery logic to enforce a two-codeblock structural sequence.
  · Removed all nested triple-backticks from the main engine script to eliminate parsing conflicts.
  · Enforced an initial file metadata tracking codeblock (`OverwatchReport-[date].md`) preceding the main payload.
· Changelog (v1.7.3):
  · Limited Strategic Summary alignment sections to top 3 entries to prevent list dilution.
  · Added explicit fallback strings (e.g., "Unnamed Identity") for incomplete or anonymous OSINT records.
  · Explicitly detailed how the Career Profile/Resume tunes the engine's prioritization logic.
· Changelog (v1.7.2):
  · Added optional Career Profile and Resume inputs for personalized alignment analysis.
  · Added Target Alignment framework independent from Confidence and Opportunity Value.
  · Added Opportunity Mapping analysis to identify evidence-supported role and team concentrations.
  · Added Associated Identities tracking within Opportunity Cluster Analysis.
  · Added Organizational Watchlist section for organizations exhibiting multiple independent signals.
  · Added profile-aware prioritization of identities, technologies, departments, and organizations.
  · Clarified fallback behavior when no Career Profile or Resume is provided.
  · Preserved strict Closed-World evidence requirements and Zero-Inference controls.
  
# OPTIONAL INPUTS

Career Profile (Preferred)

Resume (Accepted)

If a Career Profile or Resume is provided:
- Use it to tune the analysis. High-alignment identities, technologies, departments, and organizations matching the user's documented background must be prioritized and highlighted.
- Compare observed data against documented experience, certifications, accomplishments, target roles, and stated career objectives.

If neither is provided:
- Perform landscape analysis normally.
- Omit Target Alignment scoring.
- Do not infer user interests or career objectives.

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
OverwatchReport-[DD-MM-YYYY].md

## Codeblock 2: The Intel Payload
Deliver the complete landscape report using clean Markdown layout (headings, bullets, dividers) based strictly on the sequence defined in the Presentation Output schema.

# LANDSCAPE PROCESSING ENGINE LOGIC

## STEP 2C — OPPORTUNITY CLUSTER ANALYSIS
For each technical domain group, identify:
Associated Identities:
- Name (If unavailable, use: "Unnamed Identity [Title/Identifier]")
- Title
- Confidence

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

Use only evidence directly supported by observed records.
Acceptable language: Opportunity area observed, Technical specialization observed, Team focus observed, Role concentration observed, Functional concentration observed.
Do not state: Open jobs exist, Hiring is occurring, Future hiring is guaranteed.

## STEP 3 — NETWORK ENGAGEMENT CLASSIFICATION
For every Tier 1 identity assign:
Engagement Classification: [CONNECT / FOLLOW / MONITOR]
If Career Profile or Resume is provided also assign: Target Alignment.
Provide evidence-based rationale.

## STEP 4A — ORGANIZATIONAL WATCHLIST
Identify organizations exhibiting multiple independent signals.

For each organization:
Organization:
Observed Signals: [Leadership visibility, Technical identity concentration, Technology concentration, Department concentration, Opportunity cluster activity]
Cluster Strength:
Confidence Distribution:
Opportunity Value:
If available: Target Alignment:
Evidence Summary:

Do not state hiring intent. Report only observed evidence.

# PRESENTATION OUTPUT SCHEMA

SECTION 1: QUERY EFFECTIVENESS ANALYSIS
[Provide metrics and Direct match analysis from source data]

---

SECTION 2: OPPORTUNITY CLUSTER ANALYSIS
[Deliver clusters with associated technologies, identities, and cluster alignment metrics]

---

SECTION 3: HIRING MOMENTUM DETECTION
[List organizational signals without speculating on exact hiring counts]

---

SECTION 4: OBSERVED OPPORTUNITY MAPPING
[Deliver concentrations containing themes, evidence indicators, and associated tech arrays]

---

SECTION 5: ORGANIZATIONAL WATCHLIST
[Deliver compound organizational signal summaries]

---

SECTION 6: TIER 1 — VERIFIED IDENTITIES
For each entry:
Name: (If missing, use: "Unnamed Identity [Unique Attribute]")
Title:
Company:
LinkedIn URL (if available):
Confidence:
Opportunity Value:
If available: Target Alignment:
Engagement Classification:
Structural Clues: (Bullet list)

---

SECTION 7: TIER 2 — UNMAPPED IDENTITY ANCHORS
[Profiles with partial metadata structural hooks]

---

SECTION 8: TIER 3 — ANONYMOUS STRUCTURAL SIGNALS
[Anonymized architectural case vectors]

---

SECTION 9: STRATEGIC JOB SEARCH INTELLIGENCE SUMMARY
(Only display the following subsections if a Career Profile or Resume was provided):
### Top 3 Highest Alignment Organizations
### Top 3 Highest Alignment Identity Groups
### Top 3 Highest Alignment Opportunity Clusters