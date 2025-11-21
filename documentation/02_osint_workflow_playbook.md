# OSINT Workflow Playbook

## Introduction

This playbook defines the systematic, four-phase OSINT investigation workflow used by Project OSINT DeepSearch Engine. Follow this methodology for every investigation to ensure comprehensive, reliable, and legally compliant intelligence gathering.

**Core workflow**: Screening → Deep Dive → Validation → Synthesis

Each phase builds on the previous, transforming raw queries into actionable intelligence.

---

## Phase 1: Quick Screening (15–30 minutes)

### Goals
- Establish baseline facts about the target
- Identify obvious red flags or deal-breakers
- Determine if deeper investigation is warranted
- Create initial pivot points for Phase 2

### Typical Questions
- Who/what is the target?
- Do they have an online presence?
- Are there any immediate red flags (sanctions, criminal records, scam reports)?
- What are the most promising leads to follow?

### Actions Checklist

#### 1. Search Engines (5 minutes)
- **Google**: Target name/domain in quotes, advanced operators (`site:`, `inurl:`, `filetype:`)
- **Bing**: Check for different indexing results
- **DuckDuckGo**: Privacy-focused results (sometimes surfaces different content)
- **Google Images**: Profile photos, logos, visual associations

**Log**: URLs of top 5–10 relevant results

#### 2. Social Media Presence (5 minutes)
- Search target on major platforms:
  - LinkedIn (professional identity)
  - Twitter/X (public statements, interests)
  - Facebook (if public profile available)
  - Instagram (personal/lifestyle)
  - GitHub (for tech professionals)
- Note usernames, profile URLs, bio information

**Log**: All discovered social profiles with URLs

#### 3. Domain/Technical (if applicable, 5 minutes)
- **WHOIS lookup**: Domain registration info, registrant, creation date
- **DNS records**: Hosting provider, mail servers, nameservers
- **Basic IP lookup**: Geolocation, hosting company

**Log**: Registrant info, hosting details, creation dates

#### 4. People/Company Basics (5–10 minutes)
- **People**: Quick search in Pipl, Spokeo, or similar aggregators
- **Companies**: OpenCorporates, Better Business Bureau, Glassdoor
- Note: Basic free searches only in Phase 1 (premium deep dives in Phase 2)

**Log**: Job titles, company affiliations, locations, known associates

#### 5. Red Flag Check (5 minutes)
- **Sanctions lists**: OFAC, EU sanctions, UN watchlists
- **Criminal records**: Public court databases, "most wanted" lists
- **Scam databases**: BBB complaints, scam report sites, consumer protection sites
- **Negative news**: Add "lawsuit," "fraud," "scam," "arrest" to searches

**Log**: Any red flags found (with severity assessment)

### Phase 1 Outputs
- **Initial Fact Sheet** (bulleted list):
  - Name, location, occupation/business
  - Primary online identities (social profiles, domains)
  - Known associates, affiliations, or companies
  - Red flags or areas of concern
  - Reliability score for each fact (1–10)

- **Pivot Points for Phase 2**:
  - Email addresses found
  - Phone numbers
  - Usernames
  - Company names
  - Domain names
  - Associates to research

### Decision Point
After Phase 1, decide:
- **PROCEED** to Phase 2 (target is relevant, leads are promising)
- **STOP** (insufficient data, target not found, or red flags make investigation inappropriate)
- **REFINE QUERY** (target ambiguous, need more specificity)

---

## Phase 2: Deep Dive (1–4 hours)

### Goals
- Exhaust all relevant OSINT tool families
- Execute intelligent pivots across data points
- Build comprehensive intelligence picture
- Collect raw evidence from diverse sources

### Typical Questions
- What is the complete online footprint?
- What are the connections and relationships?
- What historical data exists?
- What can we infer from metadata, patterns, and correlations?

### Systematic Tool Family Coverage

Work through each relevant OSINT family from `03_osint_tool_families.md`. For each:
1. Identify 2–5 tools from the family to use
2. Execute searches methodically
3. Document findings in OSINT source table
4. Extract new pivot points

#### Example Deep Dive Sequence for a Person

**A. Enhanced People Search** (20–30 min)
- Premium searches: Pipl, Spokeo, PeekYou, Radaris, ZoomInfo
- Phone number databases: Truecaller, Numberway, carrier lookup
- Email validation: Hunter.io, MailTester, email format checks
- Address history, relatives, neighbors (US people search sites)

**Log**: Full name variations, addresses (current + historical), phone numbers, email addresses, relatives, age, education

**B. Social Media Deep Mining** (30–45 min)
- LinkedIn: Full work history, connections, endorsements, posts
- Twitter/X: Advanced search for tweets, hashtags, timeline analysis, who they follow/interact with
- Facebook: Public posts, likes, group memberships, tagged photos (respect privacy settings)
- Reddit: Username search across comments/posts, subreddit participation
- Instagram: Posts, tags, geolocation data from photos
- Forums: Search username across multiple forums and communities

**Log**: Interests, opinions, affiliations, locations visited, associates, timeline of activities

**C. Data Leaks & Breaches** (15–20 min)
- HaveIBeenPwned: Check email for known breaches
- Dehashed: Search for leaked credentials (if legally permissible)
- Pastebin monitoring: Check for email/username in pastes
- Public leak archives: Search across known data dumps

**Log**: Compromised accounts, leaked passwords (hashed), breach dates, exposure scope

**D. Images & Metadata** (15–20 min)
- Reverse image search: Google Images, Yandex, TinEye (find where profile photos appear)
- EXIF metadata: Extract geolocation, camera info, timestamps from photos
- Facial recognition: PimEyes (if legally appropriate and necessary)

**Log**: Photo sources, geolocation coordinates, camera models, timestamps, similar faces

**E. Documents & Publications** (15–30 min)
- Google Scholar: Academic publications, citations
- Patent search: USPTO, Google Patents
- SlideShare, PDF Drive: Presentations, documents authored
- News archives: LexisNexis-style searches, Google News archive

**Log**: Publications, patents, conference presentations, media mentions

**F. Geolocation & Maps** (10–15 min)
- Google Maps/Street View: Verify addresses, business locations
- Satellite imagery: Zoom Earth, Google Earth for property analysis
- Webcam directories: Live feeds near locations of interest (EarthCam)
- Flight/vessel tracking: If target travels (FlightAware, MarineTraffic)

**Log**: Verified addresses, property details, visual confirmations, travel patterns

**G. Technical Infrastructure** (if domain/website involved, 20–30 min)
- Shodan, Censys: Scan for exposed services, open ports, banners
- ViewDNS: Historical DNS, reverse IP, shared hosting analysis
- SSL certificate analysis: Certificate transparency logs, certificate history
- Wayback Machine: Historical website snapshots
- GitHub: Code repositories, commits, issues (if developer)

**Log**: Server infrastructure, technology stack, historical changes, code activity

#### Example Deep Dive Sequence for a Company

**A. Corporate Records** (20–30 min)
- OpenCorporates: Filings, officers, addresses, status
- State registries: Secretary of State databases (Delaware, etc.)
- SEC EDGAR: Financial filings (10-K, 10-Q, 8-K) for public companies
- Better Business Bureau: Ratings, complaints, accreditation

**Log**: Incorporation date, officers/directors, registered agent, address, financial data, complaints

**B. Financial & Business Intelligence** (20–30 min)
- D&B, Hoovers: Business credit, revenue estimates
- Glassdoor: Employee reviews, salary data, interview experiences
- Crunchbase: Funding rounds, investors, acquisitions
- LinkedIn Company Page: Employee count, recent hires, company updates

**Log**: Revenue, employee count, funding, investors, key personnel, reputation

**C. Ownership & Connections** (20–30 min)
- Officers → Search each officer individually
- Officers' other companies → Search those companies
- Parent/subsidiary relationships
- Partnerships, vendors, clients (from press releases, contracts)

**Log**: Org chart, related entities, beneficial owners, business relationships

**D. Online Presence & Reputation** (15–20 min)
- Company website: Archive history via Wayback Machine
- Social media: Twitter, LinkedIn, Facebook pages
- News coverage: Google News, press release databases
- Reviews: Google Reviews, Yelp, Trustpilot, industry-specific review sites

**Log**: Messaging evolution, marketing claims, customer sentiment, media coverage

**E. Domain & Infrastructure** (15–20 min)
- WHOIS: Domain ownership, history
- DNS: Mail servers, subdomains, hosting
- SSL certificates: Validity, certificate authority, SANs (Subject Alternative Names)
- Shodan: Exposed services, security posture

**Log**: IT infrastructure, security issues, related domains

**F. Legal & Compliance** (15–20 min)
- Court records: PACER (US federal courts), state court databases
- Lawsuits: Search company name + "lawsuit," "litigation"
- Regulatory actions: FTC, SEC, FCC, industry regulators
- Sanctions/watchlists: OFAC, export control lists

**Log**: Legal issues, settlements, regulatory compliance, sanctions status

### Pivoting Strategies

Pivoting = using one data point to discover new data points. Examples:

#### Email → Domain → Company → People
1. Find email: `john.doe@acmecorp.com`
2. Extract domain: `acmecorp.com`
3. WHOIS lookup → Find company: Acme Corp
4. Search company → Find other employees
5. Repeat for each employee

#### Username → Cross-Platform → Real Identity
1. Find username: `@johndoe2024`
2. Search username across platforms (Namechk, KnowEm)
3. Find same username on GitHub → Real name in profile
4. Cross-reference real name → Confirm identity

#### Phone Number → Owner → Address → Associates
1. Find phone number: `(555) 123-4567`
2. Reverse lookup → Find owner name
3. Search name → Find address
4. Search address → Find neighbors/co-residents

#### Company → Officers → Other Companies → Network
1. Find company: Acme Corp
2. Check corporate filings → Find officers
3. Search each officer → Find their other companies
4. Build network graph of related entities

#### Image → Metadata → Location → Context
1. Download profile image
2. Extract EXIF → Find GPS coordinates
3. Map coordinates → Identify location
4. Search location → Find associated events, properties

### Best Practices During Phase 2

- **Work systematically**: Don't jump randomly between tools
- **Document everything**: Update OSINT source table in real-time
- **Note dead ends**: Record what you searched even if no results (saves duplication)
- **Set time limits**: Don't get stuck in rabbit holes (timebox each tool family)
- **Mark uncertainty**: Flag low-confidence findings for validation in Phase 3
- **Collect evidence**: Screenshot or archive key findings (data changes/disappears)

### Phase 2 Outputs
- **Comprehensive OSINT Source Table** (50+ rows typical):
  - Source name, URL, data type, findings, reliability score, timestamp, notes

- **Raw Intelligence Collection**:
  - All collected facts organized by category
  - Unverified inferences and hypotheses noted separately

- **Pivot Tracking Log**:
  - Diagram or list showing how you moved from initial target to expanded scope

- **Unanswered Questions List**:
  - Gaps in intelligence requiring validation or further research

---

## Phase 3: Validation & Correlation (30–60 minutes)

### Goals
- Verify critical facts across multiple independent sources
- Resolve contradictions in collected data
- Calculate confidence levels for key findings
- Separate facts from inferences explicitly
- Assess data freshness and relevance

### Typical Questions
- Can we confirm this fact from 3+ independent sources?
- Are there contradictions in the data?
- How recent is this information?
- What is our confidence level in each finding?

### Actions Checklist

#### 1. Multi-Source Validation (20–30 min)
For each critical fact:
- Attempt to verify from **3+ independent sources**
- Independent = different data providers, not aggregators citing same source
- Example:
  - Claim: "John Doe is CEO of Acme Corp"
  - Source 1: LinkedIn profile
  - Source 2: Delaware corporate registry
  - Source 3: Company website "About Us" page
  - **Result**: FACT (high confidence, 3 independent confirmations)

**Log**: For each fact, list all confirming sources + any contradicting sources

#### 2. Contradiction Resolution (10–15 min)
When sources disagree:
- Check data freshness (newer usually better, but not always)
- Assess source authority (government record > social media)
- Look for explanatory context (name change, job change, data error)
- If unresolvable, note both versions with confidence levels

Example:
- Source 1 (LinkedIn): "Senior Manager at Acme"
- Source 2 (Company website): "Director of Operations at Acme"
- Resolution: LinkedIn may be outdated (last updated 2022), company website is current (2024)
- **Conclusion**: Current title is "Director of Operations" (HIGH-PROBABILITY, 85% confidence)

**Log**: Contradictions found, resolution approach, final determination

#### 3. Freshness Assessment (10 min)
Mark each data point with freshness:
- **CURRENT**: Verified within last 30 days
- **RECENT**: 1–12 months old
- **DATED**: 1–3 years old
- **STALE**: >3 years old (may still be valuable but verify before relying on it)

Flag stale data that conflicts with recent data.

**Log**: Freshness tags for all key findings

#### 4. Confidence Scoring (10–15 min)
Assign confidence levels to all findings:

- **FACT** (≥90% confidence):
  - 3+ independent sources agree
  - At least one authoritative source (gov't, official registry)
  - Recent data (<1 year)

- **HIGH-PROBABILITY** (70–89% confidence):
  - 2 independent sources agree
  - Logical inference strongly supported by evidence
  - Data reasonably recent

- **HYPOTHESIS** (<70% confidence):
  - Single source or unverified
  - Logical inference with limited evidence
  - Conflicting information exists

**Log**: Confidence level for every finding

#### 5. Outlier & Anomaly Detection (10 min)
Look for patterns and outliers:
- Does anything seem unusual or inconsistent?
- Are there gaps in timeline (e.g., 2-year employment gap)?
- Do claimed credentials match actual background?
- Are there suspicious coincidences?

**Log**: Anomalies flagged for further investigation or reporting

### Phase 3 Outputs
- **Validated Intelligence Summary**:
  - Facts (90–100% confidence)
  - High-probability inferences (70–89%)
  - Hypotheses (<70%)

- **Contradiction Log**:
  - List of unresolved conflicts with analysis

- **Data Freshness Report**:
  - Percentage of current vs. stale data

- **Confidence-Weighted Findings**:
  - Key facts with reliability scores and confidence levels

---

## Phase 4: Synthesis & Recommendations (30–60 minutes)

### Goals
- Produce a professional intelligence report
- Deliver actionable insights, not just data dumps
- Provide clear recommendations with justification
- Ensure legal compliance and ethical transparency

### Typical Questions
- What are the key takeaways?
- What risks or opportunities exist?
- What should the client do with this intelligence?
- What are the limitations and caveats?

### Actions Checklist

#### 1. Write Executive Summary (15–20 min)
**Format**: Maximum 10 bullet points, each 1–2 sentences

Include:
- Target identity (confirmed facts only)
- Key findings (most important discoveries)
- Red flags (if any)
- Notable gaps in intelligence
- Overall risk/opportunity assessment

**Rules**:
- No jargon (clear, business-friendly language)
- Lead with conclusions, not process
- Cite confidence levels ("confirmed," "likely," "unverified")

**Example**:
```
EXECUTIVE SUMMARY: John Doe, Acme Corp

• CONFIRMED: John Doe is currently CEO of Acme Corp (Delaware C-corp, founded 2015).
• CONFIRMED: Clean sanctions record (OFAC, EU, UN) – no legal red flags identified.
• HIGH-PROBABILITY: Acme Corp revenue estimated $5-10M annually based on employee count and industry benchmarks.
• CONFIRMED: 2 prior lawsuits (both settled, no adverse judgments) related to contract disputes.
• UNVERIFIED: Social media activity minimal – limited insight into personal interests or political views.
• RISK: Domain security weak (outdated SSL certificate, low Shodan score).
• OPPORTUNITY: Acme has no direct online reputation issues – good standing on BBB and Glassdoor.
• GAP: No public financial filings (private company) – actual revenue unverifiable.
• RECOMMENDATION: Low-risk business counterparty; recommend standard due diligence contract review.
```

#### 2. Compile Detailed Findings (20–30 min)
Organize intelligence into logical sections:

**Suggested structure**:
- **Identity & Background**
- **Professional History**
- **Financial Profile** (if applicable)
- **Online Presence & Reputation**
- **Connections & Associations**
- **Legal & Compliance**
- **Technical/Infrastructure** (if applicable)
- **Risks Identified**
- **Opportunities Identified**

For each section:
- Lead with facts (90–100% confidence)
- Follow with high-probability inferences (70–89%)
- End with hypotheses (<70%) clearly labeled
- Cite sources inline or with footnotes

#### 3. Risk Assessment (10 min)
Categorize risks identified:

- **CRITICAL**: Sanctions, criminal activity, fraud, active lawsuits
- **HIGH**: Reputation damage, financial instability, legal liabilities
- **MEDIUM**: Negative reviews, minor legal issues, weak security
- **LOW**: Unverified claims, gaps in data, minor inconsistencies

For each risk:
- Describe the risk
- Cite evidence
- Assess likelihood and potential impact
- Suggest mitigation (if appropriate)

#### 4. Recommendations (10 min)
Provide clear, actionable next steps:

**Examples**:
- "PROCEED with standard contract terms – no elevated risk detected."
- "CONDUCT additional due diligence on financial stability before major investment."
- "AVOID business relationship – sanctions risk confirmed."
- "REQUEST direct verification of credentials (cannot confirm claimed degree from OSINT)."

**Always include**:
- Justification for recommendation (cite key findings)
- Caveats (what we couldn't verify)
- Suggested follow-up actions (if needed)

#### 5. Generate OSINT Source Table (10 min)
Compile complete investigation log (see template in `05_report_and_log_templates.md`)

Include all sources used, even if they yielded no results (shows thoroughness).

#### 6. Legal & Ethical Compliance Review (5 min)
Before finalizing report:
- Confirm all sources were legal and ethical
- Verify no ToS violations occurred
- Check for PII that should be redacted (if report is shared widely)
- Ensure all claims are properly attributed
- Add disclaimers about limitations and legal use

**Standard disclaimer**:
```
LEGAL DISCLAIMER: This report is based solely on open-source intelligence
gathered from publicly available sources. All methods comply with applicable
laws and Terms of Service. Information accuracy cannot be guaranteed.
This report is for informational purposes only and does not constitute
legal, financial, or professional advice.
```

### Phase 4 Outputs
- **Executive Summary** (max 10 bullets)
- **Detailed Intelligence Report** (5–20 pages typical)
- **OSINT Source Table** (complete investigation log)
- **Risk Assessment Matrix**
- **Recommendations & Next Steps**
- **Legal/Ethical Compliance Statement**

---

## Investigation Log Best Practices

Maintain a **live investigation log** throughout all phases. Log every search, even failures.

### What to Log
- **Source name** (tool or website)
- **URL or reference** (direct link if possible)
- **Search query** (exact keywords used)
- **Results summary** (what was found or "no results")
- **Reliability score** (1–10)
- **Timestamp** (when accessed)
- **Follow-up actions** (new pivots identified)

### Why Log Everything
- **Reproducibility**: Others can verify your work
- **Audit trail**: Prove legality and thoroughness
- **Efficiency**: Avoid duplicate searches
- **Learning**: Identify which sources are most valuable for future cases

---

## Common Pivoting Patterns

Master these pivot types:

### Identity Pivots
- Name → Social media → Email → Phone → Address
- Username → Cross-platform search → Real name → Full identity

### Corporate Pivots
- Company → Officers → Officers' other companies → Network map
- Domain → WHOIS → Registrant → Other domains owned

### Technical Pivots
- Domain → IP → Reverse IP → All domains on same server
- Email → Domain → Company → All employees → All employee emails

### Geolocation Pivots
- Address → Satellite view → Neighbors → Associates
- GPS coordinates (from EXIF) → Location → Events at location

### Temporal Pivots
- Current data → Wayback Machine → Historical data → Changes over time
- Recent news → Archive search → Full timeline

---

## Workflow Iteration & Recursion

OSINT investigations are rarely linear. You may:
- Return to Phase 1 for newly discovered entities (e.g., find a related company, screen it)
- Re-enter Phase 2 with new pivot points
- Repeat Phase 3 validation when new contradictions emerge

**Know when to stop**:
- All leads exhausted (no new pivots yielding results)
- Time/budget limit reached
- Client questions answered with high confidence
- Diminishing returns (new searches yielding redundant data)

---

## Example: End-to-End Workflow

**Scenario**: Client asks, "Tell me about Acme Corp before we sign a contract with them."

**Phase 1 (20 min)**:
- Google search: "Acme Corp" → Website found, basic info
- LinkedIn: Company page → 25 employees, tech industry
- OpenCorporates: Delaware C-corp, registered 2015, CEO John Doe
- WHOIS: acmecorp.com registered 2015, registrant matches CEO
- Red flag check: No sanctions, no major lawsuits
- **Decision**: Proceed to Phase 2 (legitimate company, promising leads)

**Phase 2 (2 hours)**:
- Corporate records: Full filing history, officer names, addresses
- Financial: No public filings (private), Glassdoor reviews (3.5/5 stars, ~30 reviews)
- Officers: Search CEO John Doe → LinkedIn, Twitter, previous company (sold in 2012)
- Domain: Shodan scan → 2 open ports, outdated SSL cert (minor risk)
- Social media: Company Twitter active, responsive to customers
- News: 3 press releases, 1 trade publication mention (positive)
- Legal: 2 settled lawsuits (contract disputes, no pattern)
- **Result**: 60 sources logged, comprehensive picture

**Phase 3 (45 min)**:
- Validated CEO identity (3 sources: LinkedIn, corporate registry, company website)
- Confirmed company legitimate (no contradictions)
- Noted stale data: Glassdoor reviews mostly 1-2 years old
- Assessed confidence: Most facts 90–100%, revenue estimate 60% (hypothesis)
- **Result**: High confidence in legitimacy, low confidence in financials

**Phase 4 (30 min)**:
- Executive summary: 8 bullets, focus on legitimacy + minor tech risk
- Detailed report: 8 pages
- Risk assessment: LOW overall, MEDIUM for outdated SSL
- Recommendation: "PROCEED with contract, but note weak domain security"
- OSINT source table: 60 rows
- **Delivered**: Complete intelligence package

---

## Troubleshooting Common Issues

### "I can't find anything on the target"
- Try name variations, nicknames, maiden names
- Search related entities (employer, family, known associates)
- Check for common names (add disambiguating details: city, age, occupation)
- Try international platforms (Yandex, Baidu if target has international ties)

### "Sources contradict each other"
- Check data freshness (people change jobs, move, etc.)
- Assess source authority (gov't > commercial > social media)
- Look for context (maybe both are correct at different times)
- Document the contradiction, let client decide if critical

### "I'm drowning in data"
- Focus on client's original questions
- Prioritize facts over hypotheses
- Use Phase 3 validation to filter low-quality data
- Timebox each tool family (don't get stuck)

### "Is this legal/ethical?"
- If in doubt, DON'T DO IT
- Consult `06_source_scoring_and_ethics.md`
- Ask yourself: "Is this public data? Am I respecting ToS? Would I be comfortable explaining this method in court?"
- When uncertain, ask client or legal counsel

---

## Summary Checklist

Use this checklist for every investigation:

**Phase 1**:
- [ ] Search engines checked
- [ ] Social media screened
- [ ] Domain/WHOIS looked up (if applicable)
- [ ] Basic people/company search done
- [ ] Red flags checked
- [ ] Initial fact sheet created
- [ ] Decision made: proceed/stop/refine

**Phase 2**:
- [ ] 10+ OSINT tool families used
- [ ] Intelligent pivots executed
- [ ] 30+ sources logged
- [ ] Raw intelligence collected
- [ ] Unanswered questions noted

**Phase 3**:
- [ ] Key facts validated (3+ sources)
- [ ] Contradictions resolved
- [ ] Freshness assessed
- [ ] Confidence levels assigned
- [ ] Anomalies flagged

**Phase 4**:
- [ ] Executive summary written (max 10 bullets)
- [ ] Detailed findings compiled
- [ ] Risk assessment done
- [ ] Recommendations provided
- [ ] OSINT source table generated
- [ ] Legal/ethical compliance confirmed

---

**Now you have the complete OSINT workflow.** Practice it on every case. Iterate and refine. Become a systematic, reliable, legal business spy.
