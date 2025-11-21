# OSINT Knowledge Pack Documentation

This directory contains comprehensive OSINT knowledge and methodology documentation designed for AI systems conducting professional intelligence investigations.

## 📚 Documentation Files

### [01_project_osint_overview.md](01_project_osint_overview.md)
**Core mission and principles**
- Project mission statement
- OSINT definitions and concepts
- Core principles (legality, ethics, reliability)
- Four-phase workflow summary
- Investigation log requirements

### [02_osint_workflow_playbook.md](02_osint_workflow_playbook.md)
**Detailed investigation methodology**
- Phase 1: Quick Screening (15-30 min)
- Phase 2: Deep Dive (1-4 hours)
- Phase 3: Validation & Correlation (30-60 min)
- Phase 4: Synthesis & Recommendations (30-60 min)
- Pivoting strategies and examples
- End-to-end workflow examples

### [03_osint_tool_families.md](03_osint_tool_families.md)
**Comprehensive tool categorization**
- 28 OSINT tool families
- Search engines, people search, business intelligence
- Social media, technical infrastructure, geolocation
- Legal records, data leaks, image analysis
- 150+ example tools with use cases

### [04_priority_tool_shortlist.md](04_priority_tool_shortlist.md)
**High-priority A-list tools**
- Default go-to tools for every investigation
- Organized by category (search, people, business, technical)
- Google, Pipl, Shodan, OpenCorporates, and more
- Top 10 most essential tools

### [05_report_and_log_templates.md](05_report_and_log_templates.md)
**Professional report templates**
- Project Brief template
- Executive Summary (max 10 bullets)
- OSINT Source Table (investigation log)
- Detailed Analysis Report structure
- Risk Assessment Matrix
- JSON/YAML raw log schemas

### [06_source_scoring_and_ethics.md](06_source_scoring_and_ethics.md)
**Legal constraints and reliability scoring**
- Hard rules: what you CAN and CANNOT do
- GDPR, CCPA, ToS compliance
- Source reliability scoring (1-10 scale)
- FACT vs HIGH-PROBABILITY vs HYPOTHESIS framework
- Ethical decision matrix

---

## 🎯 How to Use This Knowledge Pack

### For AI Systems
These documents are designed to be loaded into AI model context (Claude, GPT, etc.) to enable professional OSINT capabilities.

**Recommended usage:**
1. Load all 6 files into AI context/knowledge base
2. Reference specific files based on task:
   - Starting investigation → 01, 02, 04
   - Choosing tools → 03, 04
   - Generating reports → 05
   - Checking legality → 06

### For Human Analysts
Use as training materials and reference guides for systematic OSINT investigations.

**Suggested reading order:**
1. **01_project_osint_overview.md** - Understand the framework
2. **06_source_scoring_and_ethics.md** - Learn legal boundaries
3. **02_osint_workflow_playbook.md** - Master the workflow
4. **03_osint_tool_families.md** - Explore tool categories
5. **04_priority_tool_shortlist.md** - Memorize A-list tools
6. **05_report_and_log_templates.md** - Use for every report

---

## 📖 Quick Reference

### Investigation Phases
1. **Screening** (15-30 min) - Baseline facts, red flags
2. **Deep Dive** (1-4 hours) - Exhaust tool families
3. **Validation** (30-60 min) - Cross-verify facts
4. **Synthesis** (30-60 min) - Generate report

### Source Reliability Scale
- **10/10** - Government records, official databases
- **7-9/10** - Verified news, professional databases
- **4-6/10** - Commercial aggregators, Wikipedia
- **1-3/10** - Anonymous posts, rumor sites

### Confidence Levels
- **FACT (90-100%)** - 3+ sources, authoritative
- **HIGH-PROBABILITY (70-89%)** - 2 sources, strong inference
- **HYPOTHESIS (<70%)** - Single source, speculative

### Top 10 Essential Tools
1. Google
2. Wayback Machine
3. Pipl
4. LinkedIn
5. Twitter Advanced Search
6. WHOIS Lookup
7. HaveIBeenPwned
8. OpenCorporates
9. Google Images / Yandex
10. OFAC Sanctions List

---

## 🔒 Legal & Ethical Principles

**Always remember:**
- ✅ Only public sources
- ✅ Respect Terms of Service
- ✅ Comply with GDPR, CCPA, FCRA
- ❌ No hacking or unauthorized access
- ❌ No harassment or harmful use
- ❌ No social engineering

**When in doubt, don't do it.**

---

## 📞 Support & Updates

This knowledge pack is maintained as part of the AI-OSINT-Framework project.

- **GitHub**: https://github.com/gacabartosz/AI-OSINT-Framework
- **Issues**: Report errors or suggest improvements via GitHub Issues
- **Updates**: This documentation is version-controlled and regularly updated

---

**Version**: 1.0.0
**Last Updated**: 2025-11-21
**Maintained by**: AI-OSINT-Framework Team
