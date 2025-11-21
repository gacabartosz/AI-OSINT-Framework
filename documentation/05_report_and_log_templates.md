# Report & Log Templates

## Introduction

This document provides ready-to-use templates for OSINT investigation outputs. Use these templates to ensure consistency, professionalism, and completeness in every report you generate.

**Templates included**:
1. Project Brief
2. Executive Summary
3. OSINT Source Table (Investigation Log)
4. Detailed Analysis Report
5. Risk Assessment Matrix
6. Recommendations & Next Steps
7. Raw OSINT Log (JSON/YAML)

---

## Template 1: Project Brief

**Purpose**: Document the investigation scope and objectives at the start.

```markdown
# PROJECT BRIEF

## Investigation ID
[Unique identifier, e.g., OSINT-2024-001]

## Date Initiated
[YYYY-MM-DD]

## Investigator
[Your name or team]

## Client / Requestor
[Client name or internal department]

## Target / Subject
[Name, domain, company, or identifier being investigated]

## Investigation Objectives
[List 3–5 specific questions to answer, e.g.:]
- Verify identity and background of John Doe
- Assess business legitimacy of Acme Corp
- Identify any legal or reputational risks
- Find contact information for subject
- Map relationships and affiliations

## Scope & Constraints
**In Scope**:
- Public records (US and international where legal)
- Social media (public profiles only)
- Corporate filings and financial records
- Domain and infrastructure analysis

**Out of Scope**:
- Private or password-protected data
- Unauthorized access attempts
- Social engineering or pretexting
- Dark web or illegal sources (unless explicitly authorized for security research)

## Time & Budget
- **Estimated time**: [X hours / Y days]
- **Budget**: [$ amount or N/A]
- **Deadline**: [YYYY-MM-DD]

## Legal & Ethical Constraints
- Comply with GDPR, CCPA, FCRA
- No ToS violations
- No illegal access
- Respect privacy and data protection laws

## Deliverables
- [ ] Executive Summary (max 10 bullets)
- [ ] Detailed Intelligence Report
- [ ] OSINT Source Table
- [ ] Risk Assessment
- [ ] Recommendations

## Approval
**Authorized by**: [Name, Title]
**Date**: [YYYY-MM-DD]

---
```

---

## Template 2: Executive Summary

**Purpose**: Provide decision-makers with key findings in 10 bullets or less.

```markdown
# EXECUTIVE SUMMARY

**Target**: [Subject name/entity]
**Investigation Date**: [YYYY-MM-DD]
**Investigator**: [Your name]

---

## Key Findings

1. **[FINDING CATEGORY]**: [One-sentence finding with confidence level]
   Example: *CONFIRMED: John Doe is CEO of Acme Corp (verified via Delaware corporate registry, LinkedIn, company website).*

2. **[FINDING CATEGORY]**: [One-sentence finding]
   Example: *CLEAN RECORD: No sanctions (OFAC, EU, UN) or criminal records found.*

3. **[FINDING CATEGORY]**: [One-sentence finding]
   Example: *FINANCIAL RISK: Company has 2 prior lawsuits (both settled, no adverse judgments).*

4. **[FINDING CATEGORY]**: [One-sentence finding]
   Example: *ONLINE REPUTATION: Glassdoor rating 3.5/5 (30 reviews, mostly positive).*

5. **[FINDING CATEGORY]**: [One-sentence finding]
   Example: *TECHNICAL SECURITY: Domain has outdated SSL certificate (minor risk).*

6. **[FINDING CATEGORY]**: [One-sentence finding]
   Example: *HYPOTHESIS: Email pattern suggests john.doe@acmecorp.com is valid (not confirmed).*

7. **[FINDING CATEGORY]**: [One-sentence finding]

8. **[FINDING CATEGORY]**: [One-sentence finding]

9. **[GAP/LIMITATION]**: [What you couldn't verify]
   Example: *LIMITATION: No public financial filings (private company) – actual revenue unverifiable.*

10. **[OVERALL ASSESSMENT]**: [Final risk/opportunity statement]
   Example: *RECOMMENDATION: Low-risk business counterparty; proceed with standard contract due diligence.*

---

**Confidence Level**: [High / Medium / Low]
**Reliability Score**: [Average source reliability, e.g., 8.2/10]

---
```

**Rules**:
- Maximum 10 bullets
- Each bullet = 1–2 sentences
- Use labels: CONFIRMED, HIGH-PROBABILITY, HYPOTHESIS, GAP, RISK, OPPORTUNITY
- Avoid jargon (write for non-technical audience)
- Lead with most critical findings first

---

## Template 3: OSINT Source Table (Investigation Log)

**Purpose**: Document every source used in the investigation.

```markdown
# OSINT SOURCE TABLE

| # | Source Name | URL / Reference | Data Type | Key Findings | Reliability Score (1–10) | Timestamp (UTC) | Notes |
|---|-------------|-----------------|-----------|--------------|--------------------------|-----------------|-------|
| 1 | Google Search | https://google.com/search?q=... | General | Found LinkedIn profile, company website | 7 | 2024-11-21 14:30 | Initial recon |
| 2 | LinkedIn | https://linkedin.com/in/johndoe | Person | CEO at Acme Corp, 15 years experience | 8 | 2024-11-21 14:35 | Public profile |
| 3 | WHOIS Lookup | https://who.is/whois/acmecorp.com | Domain | Registered 2015, registrant matches CEO | 9 | 2024-11-21 14:40 | Domain ownership confirmed |
| 4 | OpenCorporates | https://opencorporates.com/companies/... | Company | Delaware C-corp, active status | 10 | 2024-11-21 14:50 | Authoritative source |
| 5 | OFAC Sanctions | https://sanctionssearch.ofac.treas.gov | Compliance | No matches found | 10 | 2024-11-21 15:00 | Clean record |
| 6 | Glassdoor | https://glassdoor.com/Reviews/... | Reputation | 3.5/5 stars, 30 reviews | 6 | 2024-11-21 15:15 | Mixed reviews |
| 7 | Twitter | https://twitter.com/acmecorp | Social Media | Active since 2016, 500 followers | 5 | 2024-11-21 15:30 | Limited activity |
| 8 | HaveIBeenPwned | https://haveibeenpwned.com | Breach | CEO email found in 1 breach (LinkedIn 2021) | 9 | 2024-11-21 15:45 | Password likely changed |
| 9 | Shodan | https://shodan.io/host/... | Infrastructure | 2 open ports, outdated SSL cert | 8 | 2024-11-21 16:00 | Security concern |
| 10 | PACER | https://pacer.gov | Legal | 2 civil lawsuits (both settled 2018-2020) | 10 | 2024-11-21 16:20 | No ongoing litigation |

---

**Total Sources Consulted**: 10
**Average Reliability Score**: 8.2/10
**Date Range**: 2024-11-21 14:30 – 16:20 UTC

---
```

**CSV Format** (alternative):
```csv
Source Name,URL,Data Type,Key Findings,Reliability Score,Timestamp,Notes
Google Search,https://google.com/search?q=...,General,Found LinkedIn and website,7,2024-11-21 14:30,Initial recon
LinkedIn,https://linkedin.com/in/johndoe,Person,CEO at Acme Corp,8,2024-11-21 14:35,Public profile
...
```

---

## Template 4: Detailed Analysis Report

**Purpose**: Full intelligence report with comprehensive findings.

```markdown
# DETAILED INTELLIGENCE REPORT

**Target**: [Subject name/entity]
**Investigation ID**: [OSINT-2024-001]
**Date**: [YYYY-MM-DD]
**Investigator**: [Your name]
**Classification**: [Confidential / Internal Use / Public]

---

## Table of Contents

1. Executive Summary
2. Investigation Methodology
3. Identity & Background
4. Professional History
5. Financial Profile
6. Online Presence & Reputation
7. Connections & Associations
8. Legal & Compliance
9. Technical / Infrastructure Analysis
10. Risks Identified
11. Opportunities Identified
12. Gaps & Limitations
13. Recommendations
14. Source Table
15. Appendices

---

## 1. Executive Summary

[Insert 10-bullet executive summary from Template 2]

---

## 2. Investigation Methodology

**Approach**: Four-phase OSINT workflow (Screening → Deep Dive → Validation → Synthesis)

**Tools Used**: [List of primary tools, e.g., Google, LinkedIn, WHOIS, OpenCorporates, Shodan, etc.]

**Time Spent**: [X hours over Y days]

**Data Sources**: [Number of sources consulted, e.g., 50 sources across 15 tool families]

**Legal Compliance**: All methods 100% legal, ToS-compliant, GDPR/CCPA-compliant.

---

## 3. Identity & Background

### Confirmed Facts
- **Full Name**: [Name]
- **Age / DOB**: [If publicly available and relevant]
- **Location**: [City, State, Country]
- **Occupation**: [Job title, company]

**Sources**: [LinkedIn (reliability 8/10), corporate registry (10/10), etc.]

### Aliases / Variations
- [List any known aliases, maiden names, usernames]

### Social Media Profiles
- **LinkedIn**: [URL] – [Brief description]
- **Twitter**: [URL] – [Brief description]
- **Facebook**: [URL or "No public profile found"]
- **Other**: [GitHub, Instagram, etc.]

### Contact Information
- **Email**: [If found and relevant]
- **Phone**: [If found and relevant]
- **Address**: [If found and relevant to investigation]

**Note**: Redact sensitive PII if report will be shared beyond client.

---

## 4. Professional History

### Current Position
- **Company**: [Name]
- **Title**: [Role]
- **Since**: [Date]

**Sources**: [LinkedIn, company website, etc.]

### Employment History
| Dates | Company | Title | Notes |
|-------|---------|-------|-------|
| 2020–Present | Acme Corp | CEO | Founded company |
| 2015–2020 | Previous Corp | VP Operations | Promoted from Director |
| 2010–2015 | Another Inc | Manager | Early career |

**Sources**: LinkedIn (8/10), previous company websites via Wayback Machine (7/10)

### Education
- **Degree**: [Degree, Major]
- **Institution**: [University]
- **Year**: [Graduation year]

**Verification Status**: [VERIFIED via LinkedIn + university records / UNVERIFIED (self-reported only)]

### Certifications & Licenses
- [List any relevant professional certifications]

---

## 5. Financial Profile

### Company Financials (if applicable)
- **Revenue**: [Estimated range, e.g., $5–10M annually]
- **Employee Count**: [Number]
- **Funding**: [If startup: rounds, investors, valuation]
- **Credit Rating**: [If available from D&B, etc.]

**Sources**: Glassdoor employee count estimate (6/10), Crunchbase (7/10), no public filings (private company)

### Personal Financials (if relevant and publicly available)
- **Property Ownership**: [Addresses, values from public assessor databases]
- **Vehicles**: [If relevant]
- **Other Assets**: [Only if part of investigation scope]

**Legal Note**: Personal financial data is sensitive – include only if necessary and legally obtained.

---

## 6. Online Presence & Reputation

### Website / Domain Analysis
- **Primary Domain**: [domain.com]
- **Registration Date**: [YYYY-MM-DD]
- **Hosting**: [Provider]
- **SSL Status**: [Valid / Expired / Self-signed]
- **Security Posture**: [Shodan scan results summary]

### Social Media Activity
- **Twitter**: [Follower count, activity level, topics discussed]
- **LinkedIn**: [Connection count, post frequency, engagement]
- **Other Platforms**: [Instagram, Facebook, Reddit, etc.]

### Reputation & Reviews
- **Glassdoor** (employer reviews): [Rating, # of reviews, key themes]
- **BBB** (business reviews): [Rating, complaints, accreditation]
- **Trustpilot** (customer reviews): [Rating, # of reviews]
- **News Coverage**: [Positive / Negative / Neutral summary]

**Sentiment Analysis**: [Overall positive / mixed / negative]

---

## 7. Connections & Associations

### Business Relationships
- **Partners**: [List key business partners, vendors, clients if known]
- **Board Memberships**: [If applicable]
- **Advisors**: [If applicable]

### Personal Associations
- **Family**: [Only include if relevant and publicly disclosed]
- **Professional Network**: [LinkedIn connections analysis, mutual connections with client, etc.]

### Related Entities
- **Other Companies**: [List any other companies owned/operated by subject]

**Network Map**: [Optional: Include visual graph if using Maltego or similar]

---

## 8. Legal & Compliance

### Criminal Records
**Status**: [CLEAR / RECORDS FOUND]

**Details**: [None found / List records if applicable]

**Sources**: [Public court databases, FBI Most Wanted, state records]

### Civil Litigation
| Case # | Court | Type | Status | Outcome |
|--------|-------|------|--------|---------|
| 2020-CV-12345 | Superior Court | Contract Dispute | Settled | No adverse judgment |
| 2018-CV-67890 | Federal Court | Employment | Dismissed | Dismissed with prejudice |

**Sources**: PACER (10/10), CourtListener (9/10)

### Sanctions & Watchlists
- **OFAC**: [CLEAR / MATCH FOUND]
- **EU Sanctions**: [CLEAR / MATCH FOUND]
- **UN Sanctions**: [CLEAR / MATCH FOUND]
- **PEP Lists**: [CLEAR / MATCH FOUND]

**Compliance Status**: [COMPLIANT / AT RISK / NON-COMPLIANT]

### Regulatory Actions
[Any FTC, SEC, FCC, or industry-specific regulatory actions]

---

## 9. Technical / Infrastructure Analysis

**Applicable for domain/website investigations**

### Domain Information
- **Domain**: [domain.com]
- **Registrar**: [Name]
- **Registrant**: [Name (if not privacy-protected)]
- **Creation Date**: [YYYY-MM-DD]
- **Expiration Date**: [YYYY-MM-DD]

### DNS & Hosting
- **Nameservers**: [List]
- **Mail Servers**: [MX records]
- **Hosting Provider**: [Company, location]
- **IP Address**: [x.x.x.x]
- **IP Geolocation**: [City, Country]

### Security Analysis
- **SSL Certificate**: [Issuer, expiration, validity]
- **Open Ports**: [List from Shodan scan]
- **Exposed Services**: [HTTP, SSH, FTP, etc.]
- **Vulnerabilities**: [CVEs if found]
- **Security Headers**: [Analysis from securityheaders.com]

### Historical Data
- **Wayback Machine**: [# of snapshots, date range]
- **DNS History**: [Previous hosting, changes over time]

---

## 10. Risks Identified

### Critical Risks (Immediate Action Required)
[None identified / List critical risks]

### High Risks (Require Attention)
- **Example**: Outdated SSL certificate (expires in 30 days)
- **Example**: Subject email found in data breach (credential exposure)

### Medium Risks (Monitor)
- **Example**: Mixed Glassdoor reviews (potential HR issues)
- **Example**: 2 settled lawsuits (no pattern, but note litigation history)

### Low Risks (Informational)
- **Example**: Social media activity minimal (limited reputational insight)

**Risk Matrix**:

| Risk | Severity | Likelihood | Impact | Mitigation |
|------|----------|------------|--------|------------|
| SSL Certificate Expiring | Medium | High (30 days) | Medium | Notify client to renew |
| Email in Breach | Medium | Confirmed | Low | Password likely changed |
| Litigation History | Low | Past events | Low | Monitor for new cases |

---

## 11. Opportunities Identified

[If applicable, e.g., for competitive intelligence or business development]

- **Example**: Company has strong Glassdoor rating (good employer brand)
- **Example**: No direct competitors in X market segment (market opportunity)
- **Example**: CEO is active on LinkedIn (potential outreach channel)

---

## 12. Gaps & Limitations

### What We Couldn't Verify
- **Example**: Actual company revenue (no public filings for private company)
- **Example**: Personal political affiliations (no public statements found)
- **Example**: Full list of clients/customers (not disclosed publicly)

### Data Freshness Concerns
- **Example**: Glassdoor reviews mostly 1–2 years old (may not reflect current status)
- **Example**: LinkedIn last updated 6 months ago

### Out-of-Scope Items
- **Example**: Dark web monitoring not performed (out of scope)
- **Example**: In-person surveillance not conducted (OSINT only)

---

## 13. Recommendations

### Immediate Actions
- [ ] [Action 1, e.g., "Proceed with contract negotiations – low risk"]
- [ ] [Action 2, e.g., "Request direct verification of CEO's claimed degree"]

### Follow-Up Investigations
- [ ] [Action 3, e.g., "Monitor for new court filings over next 90 days"]
- [ ] [Action 4, e.g., "Conduct financial audit if deal proceeds"]

### Risk Mitigation
- [ ] [Action 5, e.g., "Include standard indemnification clauses in contract"]

### Overall Recommendation
**[PROCEED / PROCEED WITH CAUTION / DO NOT PROCEED / REQUIRES FURTHER INVESTIGATION]**

**Justification**: [1–2 sentence summary of why]

---

## 14. Source Table

[Insert full OSINT Source Table from Template 3]

---

## 15. Appendices

### Appendix A: Screenshots
[Include relevant screenshots of key findings]

### Appendix B: Network Graph
[If applicable, include Maltego or similar visualization]

### Appendix C: Timeline
[If applicable, chronological timeline of events]

### Appendix D: Raw Data Exports
[If applicable, attach CSV/JSON exports]

---

## Legal Disclaimer

This report is based solely on open-source intelligence gathered from publicly available sources. All methods used comply with applicable laws including GDPR, CCPA, and FCRA. Information accuracy cannot be guaranteed, and this report should be used in conjunction with other due diligence methods.

This report is for informational purposes only and does not constitute legal, financial, or professional advice.

**Confidentiality**: This report contains sensitive information and should be handled according to client's data protection policies.

---

**Report Prepared By**: [Your Name, Title]
**Date**: [YYYY-MM-DD]
**Version**: [1.0]

---
```

---

## Template 5: Risk Assessment Matrix

```markdown
# RISK ASSESSMENT MATRIX

| Risk Category | Risk Description | Severity | Likelihood | Impact | Overall Risk Score | Mitigation Strategy |
|---------------|------------------|----------|------------|--------|-------------------|---------------------|
| **Legal** | 2 settled lawsuits (contract disputes) | Medium | Past event | Low | **MEDIUM** | Monitor for new filings |
| **Compliance** | No sanctions matches | None | N/A | N/A | **NONE** | N/A |
| **Financial** | Unknown actual revenue (private company) | Medium | Uncertain | Medium | **MEDIUM** | Request financial statements |
| **Reputation** | Mixed Glassdoor reviews (3.5/5) | Low | Current | Low | **LOW** | Monitor employee sentiment |
| **Security** | Outdated SSL certificate | Medium | High (30 days) | Medium | **MEDIUM-HIGH** | Notify to renew immediately |
| **Privacy** | Email in data breach (LinkedIn 2021) | Medium | Confirmed | Low | **LOW-MEDIUM** | Assume password changed |

---

**Risk Scoring**:
- **Severity**: Critical, High, Medium, Low, None
- **Likelihood**: Certain, High, Medium, Low, Unlikely, Past Event
- **Impact**: Critical, High, Medium, Low, Negligible
- **Overall Risk Score**: Calculated from Severity × Likelihood × Impact

**Color Coding**:
- 🔴 **CRITICAL / HIGH**: Immediate action required
- 🟡 **MEDIUM**: Monitor and address
- 🟢 **LOW**: Informational only
- ⚪ **NONE**: No risk identified

---
```

---

## Template 6: JSON/YAML Raw OSINT Log

**Purpose**: Machine-readable investigation log for automation and archiving.

### JSON Format

```json
{
  "investigation": {
    "id": "OSINT-2024-001",
    "target": "John Doe / Acme Corp",
    "date_initiated": "2024-11-21",
    "investigator": "Jane Analyst",
    "status": "Completed",
    "total_sources": 50,
    "average_reliability": 8.2,
    "total_time_hours": 4.5
  },
  "sources": [
    {
      "id": 1,
      "name": "Google Search",
      "url": "https://google.com/search?q=John+Doe+Acme+Corp",
      "data_type": "General",
      "findings": "Found LinkedIn profile, company website, news article",
      "reliability_score": 7,
      "timestamp": "2024-11-21T14:30:00Z",
      "notes": "Initial reconnaissance"
    },
    {
      "id": 2,
      "name": "LinkedIn",
      "url": "https://linkedin.com/in/johndoe",
      "data_type": "Person",
      "findings": "CEO at Acme Corp since 2020, 15 years experience in tech",
      "reliability_score": 8,
      "timestamp": "2024-11-21T14:35:00Z",
      "notes": "Public profile, verified"
    },
    {
      "id": 3,
      "name": "WHOIS Lookup",
      "url": "https://who.is/whois/acmecorp.com",
      "data_type": "Domain",
      "findings": "Registered 2015-03-15, registrant: John Doe",
      "reliability_score": 9,
      "timestamp": "2024-11-21T14:40:00Z",
      "notes": "Domain ownership confirmed"
    }
  ],
  "findings": {
    "facts": [
      "John Doe is CEO of Acme Corp (confirmed via 3 sources: LinkedIn, corporate registry, company website)",
      "No OFAC sanctions found (verified 2024-11-21)"
    ],
    "high_probability": [
      "Email pattern is firstname.lastname@acmecorp.com (85% confidence based on pattern analysis)"
    ],
    "hypotheses": [
      "Twitter account @JDoe2024 may belong to John Doe (60% confidence, same city but not verified)"
    ]
  },
  "risks": [
    {
      "category": "Security",
      "description": "Outdated SSL certificate on acmecorp.com",
      "severity": "Medium",
      "likelihood": "High",
      "impact": "Medium"
    }
  ],
  "recommendations": [
    "Proceed with standard contract negotiations – low overall risk",
    "Request SSL certificate renewal from Acme Corp"
  ]
}
```

### YAML Format

```yaml
investigation:
  id: OSINT-2024-001
  target: John Doe / Acme Corp
  date_initiated: 2024-11-21
  investigator: Jane Analyst
  status: Completed
  total_sources: 50
  average_reliability: 8.2
  total_time_hours: 4.5

sources:
  - id: 1
    name: Google Search
    url: https://google.com/search?q=John+Doe+Acme+Corp
    data_type: General
    findings: Found LinkedIn profile, company website, news article
    reliability_score: 7
    timestamp: 2024-11-21T14:30:00Z
    notes: Initial reconnaissance

  - id: 2
    name: LinkedIn
    url: https://linkedin.com/in/johndoe
    data_type: Person
    findings: CEO at Acme Corp since 2020, 15 years experience in tech
    reliability_score: 8
    timestamp: 2024-11-21T14:35:00Z
    notes: Public profile, verified

  - id: 3
    name: WHOIS Lookup
    url: https://who.is/whois/acmecorp.com
    data_type: Domain
    findings: Registered 2015-03-15, registrant John Doe
    reliability_score: 9
    timestamp: 2024-11-21T14:40:00Z
    notes: Domain ownership confirmed

findings:
  facts:
    - John Doe is CEO of Acme Corp (confirmed via 3 sources)
    - No OFAC sanctions found

  high_probability:
    - Email pattern is firstname.lastname@acmecorp.com (85% confidence)

  hypotheses:
    - Twitter @JDoe2024 may belong to John Doe (60% confidence)

risks:
  - category: Security
    description: Outdated SSL certificate on acmecorp.com
    severity: Medium
    likelihood: High
    impact: Medium

recommendations:
  - Proceed with standard contract negotiations – low overall risk
  - Request SSL certificate renewal from Acme Corp
```

---

## Usage Guidelines

### When to Use Each Template

1. **Project Brief**: Start of every investigation (before data collection)
2. **Executive Summary**: For decision-makers, C-suite, time-constrained audiences
3. **OSINT Source Table**: For transparency, reproducibility, audit trails
4. **Detailed Analysis Report**: For comprehensive investigations, legal proceedings, due diligence
5. **Risk Assessment Matrix**: For risk management, compliance teams
6. **JSON/YAML Log**: For automation, databases, long-term archiving

### Customization

- **Add/remove sections** as needed for your specific use case
- **Adjust detail level** based on audience (executive vs. analyst)
- **Include/exclude PII** based on data protection requirements and need-to-know
- **Adapt language** for industry (legal, finance, security, journalism)

### Quality Checklist

Before finalizing any report:
- [ ] All sources cited with URLs and timestamps
- [ ] Reliability scores assigned to all sources
- [ ] Facts clearly separated from inferences and hypotheses
- [ ] Confidence levels stated explicitly
- [ ] Gaps and limitations documented
- [ ] Legal/ethical compliance confirmed
- [ ] Sensitive data redacted if necessary
- [ ] Report reviewed for accuracy and clarity

---

**You now have professional templates for all OSINT outputs.** Use these consistently to deliver high-quality, actionable intelligence reports.
