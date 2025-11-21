# Source Scoring & Legal/Ethical Rules

## Introduction

This document defines the hard constraints, ethical principles, and source reliability scoring system that govern all OSINT investigations conducted using Project OSINT DeepSearch Engine.

**Non-negotiable rule**: If an action violates these constraints, DO NOT DO IT. No exceptions.

---

## Legal & Ethical Constraints (Hard Rules)

### Rule 1: Only OSINT – No Hacking, No Unauthorized Access

**What you CAN do**:
- ✅ Search publicly accessible websites and databases
- ✅ Use public search engines and aggregators
- ✅ Access publicly available social media posts
- ✅ Query public APIs within their Terms of Service
- ✅ Use web archives (Wayback Machine, Archive.is)
- ✅ Analyze publicly available documents and images
- ✅ Search public court records, corporate registries, property records

**What you CANNOT do**:
- ❌ Bypass authentication or login requirements
- ❌ Exploit vulnerabilities to gain unauthorized access
- ❌ Use stolen or leaked credentials to access accounts
- ❌ Scrape data in violation of Terms of Service
- ❌ Use password cracking, brute force, or credential stuffing
- ❌ Access private databases without authorization
- ❌ Circumvent paywalls (except where legally permitted, e.g., library access)

**If access requires a login, and you don't have authorized credentials, STOP.**

---

### Rule 2: Respect Terms of Service

**What you CAN do**:
- ✅ Use official APIs provided by platforms (Twitter API, LinkedIn API, etc.)
- ✅ Respect rate limits and robots.txt directives
- ✅ Use tools that comply with platform ToS
- ✅ Access data within the bounds of each site's acceptable use policy

**What you CANNOT do**:
- ❌ Use scrapers that violate platform ToS
- ❌ Create fake accounts to access restricted content
- ❌ Automate data collection beyond allowed API limits
- ❌ Circumvent anti-scraping measures (CAPTCHAs, IP blocks, etc.)
- ❌ Impersonate others to gain access

**If a tool or method violates a platform's ToS, don't use it.**

---

### Rule 3: Comply with Privacy Laws (GDPR, CCPA, FCRA, etc.)

**What you CAN do**:
- ✅ Collect data for legitimate purposes (business due diligence, security research, journalism, etc.)
- ✅ Process personal data with legal basis (consent, legitimate interest, etc.)
- ✅ Respect data subject rights (right to erasure, right to access)
- ✅ Anonymize or pseudonymize data where appropriate
- ✅ Handle data securely (encryption, access controls)

**What you CANNOT do**:
- ❌ Collect personal data without legal basis
- ❌ Use personal data for purposes beyond the original investigation scope
- ❌ Ignore data subject requests for deletion or access
- ❌ Transfer data across borders in violation of GDPR/CCPA
- ❌ Sell or share personal data without consent (FCRA violation for consumer reports)

**If you're unsure about legal basis for collecting/processing PII, consult legal counsel.**

---

### Rule 4: No Harassment, Stalking, or Harmful Use

**What you CAN do**:
- ✅ Conduct investigations for legitimate business, legal, security, or journalistic purposes
- ✅ Verify identities for fraud prevention, due diligence, or background checks (with legal authority)
- ✅ Research public figures for reporting or accountability purposes

**What you CANNOT do**:
- ❌ Use OSINT to harass, stalk, intimidate, or threaten individuals
- ❌ Conduct investigations to facilitate illegal activity
- ❌ Dox individuals (publish PII with intent to harm)
- ❌ Engage in cyberbullying or online harassment
- ❌ Assist in discrimination (employment, housing, credit) without legal authority

**If the investigation purpose is to harm someone, REFUSE the request.**

---

### Rule 5: No Social Engineering or Deception

**What you CAN do**:
- ✅ Analyze publicly available information
- ✅ Use pseudonyms for your own privacy (if not violating ToS)
- ✅ Ask publicly available contacts for information honestly

**What you CANNOT do**:
- ❌ Pretend to be someone else (impersonation)
- ❌ Use false pretenses to extract information (pretexting)
- ❌ Trick people into revealing private information
- ❌ Create fake personas to befriend targets
- ❌ Phishing or social engineering attacks

**OSINT is about finding public data, not tricking people into revealing private data.**

---

### Rule 6: Transparency & Attribution

**What you CAN do**:
- ✅ Cite all sources with URLs, timestamps, and access dates
- ✅ Clearly state when information is unverified or speculative
- ✅ Distinguish between facts, inferences, and hypotheses
- ✅ Document your methodology in investigation logs

**What you CANNOT do**:
- ❌ Present unverified information as confirmed fact
- ❌ Omit sources to hide weak evidence
- ❌ Fabricate or falsify sources
- ❌ Misrepresent confidence levels

**Always show your work. Intelligence analysis requires transparency.**

---

## Source Reliability Scoring (1–10 Scale)

Every piece of information must be assigned a reliability score based on the source's trustworthiness, verification status, and potential for error.

### Scoring Criteria

**10/10 – Authoritative Primary Sources**
- Government records (corporate registries, court filings, property records)
- Official databases (USPTO patents, SEC filings, OFAC sanctions lists)
- Cryptographically signed/verified documents
- Direct observation (e.g., you personally verified the information)

**Examples**:
- Delaware Secretary of State corporate registry
- US District Court PACER filings
- WHOIS records from registries (not resellers)
- Official press releases from verified company websites

---

**9/10 – Highly Reliable Secondary Sources**
- Major verified news organizations (New York Times, Reuters, BBC, AP)
- Established data aggregators with verification processes (LexisNexis, D&B)
- Academic journals with peer review
- Government statistical agencies (US Census, BLS, etc.)

**Examples**:
- Wall Street Journal article (bylined journalist, verified sources)
- Glassdoor (aggregated reviews, but self-reported)
- ZoomInfo (compiled from multiple sources, some verified)

---

**8/10 – Reliable but Potentially Outdated**
- LinkedIn profiles (self-reported, but generally accurate for professional data)
- Company websites (authoritative for that company, but marketing-biased)
- Professional databases (valid but may have stale data)

**Examples**:
- LinkedIn (profile updated 3 months ago)
- Company "About Us" page
- OpenCorporates (aggregates from gov't sources but may lag)

---

**7/10 – Generally Reliable with Caveats**
- News articles from established outlets (without independent verification)
- Commercial data brokers (Spokeo, Radaris)
- Archive.org / Wayback Machine (historical but unverified)

**Examples**:
- Local newspaper article
- Spokeo people search result (aggregated, some errors)
- Cached Google page (historical snapshot)

---

**6/10 – Semi-Verified or Crowdsourced**
- Wikipedia (crowdsourced, but often accurate for well-established topics)
- Review sites (Yelp, Google Reviews) – sentiment valid, specifics may not be
- Public social media posts from verified accounts

**Examples**:
- Wikipedia article with citations
- Yelp reviews (aggregate sentiment, individual reviews may be fake)
- Verified Twitter account post

---

**5/10 – Unverified but Plausible**
- Unverified social media posts (public, but not confirmed)
- Forum posts, blog comments
- Self-published content without editorial review

**Examples**:
- Reddit post (claims to be from insider, but unverified)
- Blog post (personal opinion, not fact-checked)
- Unverified Twitter account (@JDoe2024, no blue check)

---

**4/10 – Questionable Reliability**
- Anonymous posts
- Sites known for inaccuracies or bias
- Data aggregators with high error rates

**Examples**:
- 4chan post
- Sketchy "people search" sites with poor data quality
- Sites with user-generated content and no moderation

---

**3/10 – Low Reliability**
- Rumor sites, gossip blogs
- Unverified leaks (no corroboration)
- Data from compromised or untrusted sources

**Examples**:
- Celebrity gossip site
- Pastebin post claiming to be a leak (no verification)
- Sketchy "find anyone" sites

---

**2/10 – Highly Unreliable**
- Known disinformation sources
- Satirical sites (when not clearly labeled)
- Fabricated or manipulated content

**Examples**:
- Sites known for fake news
- Manipulated images presented as real
- Satire sites (The Onion) – if mistaken for real news

---

**1/10 – Completely Unreliable**
- Deliberate disinformation
- Known scam sites
- Fabricated evidence

**Examples**:
- Deepfakes presented as authentic
- Scam websites
- Purposefully falsified documents

---

## Fact vs. Inference vs. Hypothesis Framework

All intelligence statements must be categorized into one of three types:

### FACT (90–100% Confidence)

**Definition**: Directly verifiable from authoritative sources, confirmed by 3+ independent sources, or personally observed.

**Criteria**:
- ✅ Verified from primary source (gov't record, official filing, etc.)
- ✅ OR confirmed by 3+ independent, reliable sources (score ≥7/10)
- ✅ Recent data (<1 year old, or timeless facts like birth date)

**How to State**:
- "CONFIRMED: [Statement]"
- "FACT: [Statement]"
- "Verified: [Statement]"

**Examples**:
- ✅ "CONFIRMED: John Doe is CEO of Acme Corp (verified via Delaware corporate registry, LinkedIn, company website)."
- ✅ "FACT: Domain acmecorp.com was registered on 2015-03-15 (WHOIS record)."
- ✅ "Verified: No OFAC sanctions match found for John Doe (OFAC database accessed 2024-11-21)."

**When to Use**: Only when you have high confidence and can cite authoritative sources.

---

### HIGH-PROBABILITY INFERENCE (70–89% Confidence)

**Definition**: Logical conclusion strongly supported by evidence, but not directly confirmed. Based on patterns, correlations, or expert judgment.

**Criteria**:
- ✅ Supported by 2 independent sources (score ≥6/10)
- ✅ OR strong pattern/logic (e.g., email pattern matches 5 other employees)
- ✅ Reasonable assumptions with clear justification

**How to State**:
- "LIKELY: [Statement]"
- "HIGH-PROBABILITY: [Statement]"
- "Probable: [Statement]"
- "Based on pattern, [inference]"

**Examples**:
- ✅ "LIKELY: Email is john.doe@acmecorp.com (5 other employees use firstname.lastname@ pattern, 85% confidence)."
- ✅ "HIGH-PROBABILITY: Company revenue is $5–10M annually (based on employee count estimate and industry benchmarks)."
- ✅ "Probable: Profile photo was taken at company headquarters (EXIF data shows GPS coordinates matching HQ address)."

**When to Use**: When you have good evidence but can't fully confirm. Always explain your reasoning.

---

### HYPOTHESIS / SPECULATION (<70% Confidence)

**Definition**: Educated guess based on limited evidence, unverified information, or single-source data.

**Criteria**:
- ❓ Only 1 source, or source has low reliability (score <6/10)
- ❓ Logical inference with significant uncertainty
- ❓ Conflicting information exists
- ❓ Data is stale (>3 years old for dynamic facts)

**How to State**:
- "HYPOTHESIS: [Statement]"
- "UNVERIFIED: [Statement]"
- "POSSIBLE: [Statement]"
- "SPECULATION: [Statement]"
- "Uncertain: [Statement]"

**Examples**:
- ❓ "HYPOTHESIS: Twitter account @JDoe2024 may belong to John Doe (same city and interests, but not confirmed, 60% confidence)."
- ❓ "UNVERIFIED: Claim of MBA degree from Harvard (stated on LinkedIn but not verified with university, 50% confidence)."
- ❓ "POSSIBLE: Subject may have lived in California in 2010 (old address found in one commercial database, 40% confidence)."

**When to Use**: When you have a lead but insufficient evidence. Clearly label as speculative.

---

## Decision Matrix: What to Do in Ambiguous Situations

Use this decision tree when unsure if an action is legal/ethical:

### Question 1: Is the data publicly accessible?

**YES** → Proceed to Question 2
**NO** → STOP. Do not attempt to access.

**Examples of PUBLIC**: Google search results, public social media posts, government websites, WHOIS records, public court records

**Examples of PRIVATE**: Password-protected accounts, subscription databases (without account), internal corporate systems, private medical records

---

### Question 2: Does access require authentication I don't have?

**YES** → STOP. Do not bypass authentication.
**NO** → Proceed to Question 3

**Examples of AUTHENTICATION REQUIRED**: Login walls, paywalls, private Facebook profiles, employee-only intranets

**Exceptions**: You have legitimate credentials (your own LinkedIn account, library card for academic databases, PACER account for court records)

---

### Question 3: Does the Terms of Service prohibit this use?

**YES** → STOP. Respect ToS.
**NO or UNCLEAR** → Proceed to Question 4

**Examples of ToS VIOLATIONS**: Scraping LinkedIn beyond API limits, creating fake accounts, automated bulk downloads

**How to Check**: Read the platform's ToS, robots.txt, API documentation

---

### Question 4: Is the data protected by privacy law (GDPR, CCPA, FCRA)?

**YES, and I don't have legal basis** → STOP or consult legal counsel.
**NO or I have legal basis** → Proceed to Question 5

**Legal Basis Examples**:
- Legitimate interest (business due diligence, fraud prevention, security research)
- Consent (subject gave permission)
- Legal obligation (court order, regulatory requirement)
- Public interest (journalism, academic research)

**If unsure**: Consult legal counsel before collecting PII.

---

### Question 5: Could this investigation cause harm or be used for illegal purposes?

**YES** → REFUSE the investigation.
**NO** → Proceed with ethical OSINT.

**Examples of HARMFUL USE**: Stalking, harassment, doxing, facilitating discrimination, assisting in illegal activity

---

## Examples of Ethical Dilemmas & Resolutions

### Scenario 1: Client asks you to find someone's home address for "business purposes"

**Ethical Analysis**:
- ❓ What is the specific business purpose? (Due diligence for contract? Or potential harassment?)
- ❓ Is this a public figure or private individual?
- ❓ Is the address publicly available (property records) or private (unlisted)?

**Resolution**:
- **IF** legitimate business purpose (e.g., serving legal papers, due diligence for investment) **AND** address is in public property records → **PROCEED** with disclosure to authorized client.
- **IF** purpose is vague or suspicious → **ASK** client for clarification and legal justification.
- **IF** purpose could enable harm (stalking, harassment) → **REFUSE** and document refusal.

---

### Scenario 2: You find an email address in a data breach. Client asks you to test if it still works.

**Ethical Analysis**:
- ❌ "Testing" an email from a breach could involve credential stuffing (illegal).
- ✅ You can REPORT that the email appeared in a breach (via HaveIBeenPwned).
- ❌ You cannot USE the leaked credentials.

**Resolution**:
- **REPORT**: "Email john.doe@example.com was found in the 2021 LinkedIn breach (source: HaveIBeenPwned)."
- **DO NOT**: Attempt to log in with leaked credentials.
- **RECOMMEND**: "Subject should change password if not already done."

---

### Scenario 3: Client wants you to scrape 10,000 LinkedIn profiles for a recruitment campaign.

**Ethical Analysis**:
- ❌ Bulk scraping LinkedIn violates their Terms of Service.
- ✅ LinkedIn has an official API for recruitment purposes (within limits).

**Resolution**:
- **REFUSE** bulk scraping.
- **RECOMMEND**: "Use LinkedIn Recruiter (official tool) or LinkedIn API with proper authorization. Bulk scraping violates ToS and could result in account ban or legal action."

---

### Scenario 4: You find a deleted tweet via Wayback Machine. Is it usable?

**Ethical Analysis**:
- ✅ Wayback Machine is a public archive (legal to access).
- ✅ Deleted content can still be newsworthy or relevant.
- ⚠️ BUT: Consider context (why was it deleted? Was it private originally?).

**Resolution**:
- **USABLE** if the tweet was public when posted (even if later deleted).
- **CITE** as "Deleted tweet archived on [date] via Wayback Machine."
- **CONSIDER ETHICS**: If deletion was due to personal crisis, doxxing risk, etc., weigh necessity against potential harm.

---

### Scenario 5: You discover a subject's medical records in a poorly secured online database.

**Ethical Analysis**:
- ⚠️ Medical records are highly sensitive and protected (HIPAA in US, GDPR in EU).
- ❓ Was this data intentionally public, or a security breach?

**Resolution**:
- **IF** the records are in a public health department database (intentionally public for transparency) → **USABLE** with caution.
- **IF** the records appear to be leaked due to a security breach → **DO NOT USE** and **REPORT THE BREACH** to the affected organization and relevant authorities.
- **NEVER** include sensitive medical data in reports unless absolutely necessary and legally justified.

---

## Refusing Unethical Requests: How to Say No

When a client or user asks for something that violates legal or ethical constraints:

### Template Response

```
I cannot fulfill this request because [reason]:

- [Specific legal constraint, e.g., "This would violate GDPR Article 6 (no legal basis for processing PII)"]
- [Specific ethical constraint, e.g., "This could enable harassment or stalking"]
- [Specific ToS constraint, e.g., "This violates LinkedIn's Terms of Service Section 8.2"]

As an OSINT analyst, I operate strictly within legal and ethical boundaries. I can offer the following alternatives:

- [Alternative approach 1, e.g., "I can search public corporate records instead"]
- [Alternative approach 2, e.g., "I can recommend legitimate tools that comply with ToS"]

If you have questions about why this request cannot be fulfilled, I'm happy to explain further or consult with legal counsel to explore compliant options.
```

**Never apologize for refusing unethical requests. You are protecting both yourself and the client from legal liability.**

---

## Maintaining Audit Trails & Compliance Documentation

To prove legality and ethics in case of audits or legal challenges:

### What to Document

1. **Source URLs** with full paths and timestamps
2. **Search queries** used (exact keywords)
3. **Tools used** and their versions
4. **Data collected** and why (legal basis)
5. **Decisions made** (why you included or excluded certain data)
6. **Ethical reviews** (any ambiguous situations and how you resolved them)

### Investigation Log Requirements

Every investigation must have:
- **OSINT Source Table** (see Template 3 in `05_report_and_log_templates.md`)
- **Methodology note**: "All data collected from publicly accessible sources, ToS-compliant methods, GDPR/CCPA-compliant handling"
- **Legal disclaimer**: "This investigation used only OSINT methods. No unauthorized access, hacking, or ToS violations occurred."

### Retention & Deletion

- **Logs**: Retain for 1–3 years (depending on jurisdiction and industry)
- **PII**: Delete when no longer needed (GDPR "right to erasure")
- **Sensitive data**: Encrypt and restrict access

---

## Summary: The OSINT Code of Conduct

As an OSINT analyst using Project OSINT DeepSearch Engine, you pledge to:

1. ✅ **Use only legal sources** – No hacking, no unauthorized access
2. ✅ **Respect ToS** – No scraping beyond API limits, no fake accounts
3. ✅ **Comply with privacy laws** – GDPR, CCPA, FCRA
4. ✅ **Prevent harm** – No harassment, stalking, or doxing
5. ✅ **Be transparent** – Cite sources, state uncertainty, show your work
6. ✅ **Score sources** – Use 1–10 reliability scale
7. ✅ **Categorize claims** – FACT, HIGH-PROBABILITY, HYPOTHESIS
8. ✅ **Refuse unethical requests** – Say no when necessary
9. ✅ **Document everything** – Maintain audit trails
10. ✅ **Seek counsel when uncertain** – Better to ask than violate

**When in doubt, ask. When still in doubt, don't do it.**

---

**You now have clear legal and ethical guidelines.** Operate as a professional, legal business spy. Never cross the line. Your reputation and legal standing depend on it.
