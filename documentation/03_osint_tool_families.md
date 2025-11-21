# OSINT Tool Families

## Introduction

This document categorizes OSINT tools into logical "families" based on the type of intelligence they gather. Each family answers specific questions and serves particular use cases.

Use this as a reference guide when planning investigations. For each target type (person, company, domain, etc.), identify which families are relevant, then systematically work through 2–5 tools per family.

**Organized by intelligence type, not by specific vendor.**

---

## 1. OSINT Investigation Tools (Meta-Tools)

### What Questions This Family Answers
- What tools should I use for this investigation?
- Are there all-in-one platforms for OSINT?
- How can I automate multi-source searches?

### Typical Use Cases
- Starting point for complex investigations
- Automated reconnaissance
- Multi-tool orchestration
- Training and learning OSINT techniques

### Example Tools
- **OSINT Framework** (osintframework.com)
- **Maltego** (graph-based intelligence platform)
- **SpiderFoot** (automated OSINT scanner)
- **Recon-ng** (reconnaissance framework)
- **theHarvester** (information gathering tool)
- **Sherlock** (username search across platforms)

---

## 2. Search Engines & Web Discovery

### What Questions This Family Answers
- What websites mention the target?
- What indexed content exists about this topic?
- Are there specialized search angles (news, blogs, forums)?

### Typical Use Cases
- Initial reconnaissance
- Finding public mentions and references
- Discovering obscure or buried content
- Advanced operator searches (site:, inurl:, filetype:)

### Example Tools
- **Google** (google.com) – default general search
- **Google Advanced Search** – operator-based queries
- **Bing** (bing.com) – alternative indexing
- **DuckDuckGo** (duckduckgo.com) – privacy-focused
- **Yandex** (yandex.com) – Russian search, different results
- **Baidu** (baidu.com) – Chinese search
- **Startpage** (startpage.com) – anonymous Google proxy

---

## 3. Web Archiving & Historical Data

### What Questions This Family Answers
- What did this website look like in the past?
- Has content been deleted or changed?
- Can I recover deleted pages?

### Typical Use Cases
- Verifying historical claims
- Recovering deleted content
- Tracking website evolution
- Finding cached versions of pages

### Example Tools
- **Wayback Machine** (web.archive.org)
- **Archive.is / Archive.today** (archive.ph)
- **Cached Pages / Webcache** (Google Cache, Bing Cache)
- **Mementos Time Travel** (timetravel.mementoweb.org)
- **UK Web Archive** (webarchive.org.uk)

---

## 4. Documents, Academic & Patent Search

### What Questions This Family Answers
- Has the target authored any documents, papers, or patents?
- What presentations or slide decks exist?
- Are there leaked or public PDFs related to the target?

### Typical Use Cases
- Researching expertise and credentials
- Finding proprietary information in public docs
- Academic background verification
- Intellectual property searches

### Example Tools
- **Google Scholar** (scholar.google.com)
- **Google Patents** (patents.google.com)
- **USPTO** (uspto.gov) – US patents
- **SlideShare** (slideshare.net)
- **PDF Drive** (pdfdrive.com)
- **CORE** (core.ac.uk) – academic papers
- **Scribd** (scribd.com)

---

## 5. Social Network Search & Analysis

### What Questions This Family Answers
- What social media accounts does the target have?
- What do they post publicly?
- Who are their connections and associations?

### Typical Use Cases
- Profiling individuals
- Sentiment analysis
- Finding public statements and opinions
- Identifying networks and groups

### Example Tools
- **Social Searcher** (social-searcher.com) – multi-platform search
- **Social Mention** (socialmention.com)
- **Hootsuite** (monitoring and analytics)
- **Twint** (Twitter scraping tool, respects public data)
- **Social Blade** (social media statistics)

---

## 6. Facebook-Specific Tools

### What Questions This Family Answers
- What Facebook profiles match this person?
- What has this person publicly shared on Facebook?
- What groups or pages are they associated with?

### Typical Use Cases
- Profiling via public Facebook data
- Finding connections through mutual friends
- Locating public posts and photos

### Example Tools
- **Facebook Graph Search** (deprecated but some tools mimic it)
- **Facebook Search** (manual advanced search)
- **IntelTechniques Facebook Tools** (custom search tools)
- **Plessas Facebook Tools**
- **StalkScan** (public profile search, ethical use only)

**Note**: Respect Facebook ToS. Only access public data. Never scrape private profiles.

---

## 7. Twitter/X Search & Analysis

### What Questions This Family Answers
- What has this person tweeted?
- Who do they follow and interact with?
- What hashtags, topics, or events are they involved in?

### Typical Use Cases
- Timeline analysis
- Sentiment and opinion gathering
- Finding real-time updates
- Identifying influencers and networks

### Example Tools
- **Twitter Advanced Search** (twitter.com/search-advanced)
- **TweetDeck** (manage multiple feeds)
- **TweetBeaver** (analytics and search)
- **Twitonomy** (follower analysis)
- **Botometer** (bot detection)
- **Followerwonk** (Twitter analytics)

---

## 8. Reddit, Forums & Community Search

### What Questions This Family Answers
- What communities is the target active in?
- What topics do they discuss?
- Have they shared identifying information in posts?

### Typical Use Cases
- Finding niche interests and affiliations
- Uncovering opinions and expertise
- Identifying pseudonymous accounts

### Example Tools
- **Reddit Search** (reddit.com/search)
- **Pushshift Reddit Search** (redditsearch.io)
- **Reddit Investigator** (redditinvestigator.com)
- **BoardReader** (boardreader.com) – forum search
- **Tapatalk** (tapatalk.com) – forum aggregator
- **Google site:reddit.com** – advanced Reddit search

---

## 9. People Aggregators & Search Engines

### What Questions This Family Answers
- Where does this person live?
- What is their phone number, email, or address?
- Who are their relatives and associates?

### Typical Use Cases
- Identity verification
- Contact information discovery
- Background checks (using legal, public sources)

### Example Tools
- **Pipl** (pipl.com) – deep people search
- **Spokeo** (spokeo.com) – US-focused
- **PeekYou** (peekyou.com)
- **Radaris** (radaris.com)
- **ZoomInfo** (zoominfo.com) – B2B contacts
- **411.com** – US phone/address directory
- **WhitePages** (whitepages.com)

**Legal note**: Comply with FCRA, GDPR, CCPA when using people search tools.

---

## 10. Phone Number Search & Validation

### What Questions This Family Answers
- Who owns this phone number?
- Is this number active?
- What carrier/location is associated with it?

### Typical Use Cases
- Reverse phone lookup
- Verifying contact authenticity
- Identifying spam/scam numbers

### Example Tools
- **Truecaller** (truecaller.com)
- **Numberway** (numberway.com)
- **CallerSmart** (callersmart.com)
- **Carrier Lookup** (freecarrierlookup.com)
- **PhoneInfoga** (open-source phone number recon)
- **Twilio Lookup API** (API-based validation)

---

## 11. Email Search & Validation

### What Questions This Family Answers
- Is this email address valid and active?
- What accounts are associated with this email?
- Has this email been leaked in a breach?

### Typical Use Cases
- Contact discovery
- Verifying email legitimacy
- Breach exposure checks

### Example Tools
- **Hunter.io** (hunter.io) – find emails by domain
- **MailTester** (mailtester.com)
- **Email Hippo** (verify validity)
- **HaveIBeenPwned** (haveibeenpwned.com) – breach check
- **Dehashed** (dehashed.com) – leaked credentials
- **Snov.io** (email finder)

---

## 12. Crime, Criminal Records & Sanctions

### What Questions This Family Answers
- Does the target have a criminal record?
- Are they on any sanctions lists?
- Are there warrants, arrests, or convictions?

### Typical Use Cases
- Due diligence and risk assessment
- Sanctions compliance (OFAC, EU, UN)
- Background checks for employment or partnerships

### Example Tools
- **OFAC Sanctions List** (treasury.gov/ofac)
- **EU Sanctions Map** (sanctionsmap.eu)
- **UN Sanctions** (un.org/securitycouncil/sanctions)
- **FBI Most Wanted** (fbi.gov/wanted)
- **Interpol Wanted** (interpol.int/notice)
- **VINELink** (vinelink.com) – US inmate locator
- **Public court record databases** (see Court Records family)

**Legal note**: Many criminal records are restricted. Use only legally accessible public sources.

---

## 13. Court Records & Government Records

### What Questions This Family Answers
- Has the target been involved in lawsuits?
- What legal filings exist (civil, criminal, bankruptcy)?
- What government records are publicly accessible?

### Typical Use Cases
- Legal due diligence
- Verifying litigation history
- Finding public filings (property, corporate, divorce, etc.)

### Example Tools
- **PACER** (pacer.gov) – US federal court records
- **State court websites** (varies by jurisdiction)
- **CourtListener** (courtlistener.com) – free legal opinions
- **RECAP** (free.law/recap) – PACER archive
- **Justia** (justia.com) – legal search
- **PublicRecordsNow** (commercial aggregator)

**Legal note**: PACER requires account; respect access restrictions.

---

## 14. Business Entity Search

### What Questions This Family Answers
- Is this company legally registered?
- Who are the officers and directors?
- When was the company incorporated?
- What is the registered address?

### Typical Use Cases
- Corporate due diligence
- Verifying legitimacy of businesses
- Finding corporate officers and structure

### Example Tools
- **OpenCorporates** (opencorporates.com) – global registry
- **Secretary of State databases** (varies by US state)
- **Companies House** (companieshouse.gov.uk) – UK
- **EDGAR** (sec.gov/edgar) – US public company filings
- **Better Business Bureau** (bbb.org)
- **Dun & Bradstreet** (dnb.com) – business credit

---

## 15. Business Financial & Banking

### What Questions This Family Answers
- What is the company's revenue and financial status?
- Are there public financial filings?
- What is their credit rating?

### Typical Use Cases
- Investment due diligence
- Assessing financial stability
- Risk evaluation for partnerships

### Example Tools
- **SEC EDGAR** (sec.gov/edgar) – 10-K, 10-Q, 8-K filings
- **Yahoo Finance** (finance.yahoo.com)
- **Google Finance** (google.com/finance)
- **Crunchbase** (crunchbase.com) – startup funding data
- **PitchBook** (pitchbook.com)
- **D&B Hoovers** (business intelligence)

---

## 16. Property Search (Real Estate)

### What Questions This Family Answers
- What property does the target own?
- What is the property value and history?
- Are there liens or mortgages on the property?

### Typical Use Cases
- Asset searches
- Verifying addresses
- Property ownership investigations

### Example Tools
- **County assessor websites** (varies by location)
- **Zillow** (zillow.com) – US property data
- **Realtor.com** (realtor.com)
- **PropertyShark** (propertyshark.com)
- **Land Registry** (gov.uk/land-registry) – UK
- **Regrid** (regrid.com) – parcel data

---

## 17. Vehicles, VIN & License Plates

### What Questions This Family Answers
- Who owns this vehicle?
- What is the vehicle history?
- Has this VIN been reported stolen or salvaged?

### Typical Use Cases
- Vehicle history checks
- Verifying ownership
- License plate lookups (where legal)

### Example Tools
- **VINCheck** (vehiclehistory.gov) – NHTSA database
- **Carfax** (carfax.com) – vehicle history reports
- **AutoCheck** (autocheck.com)
- **License plate lookup services** (legality varies by jurisdiction)
- **State DMV databases** (limited public access)

**Legal note**: License plate searches have legal restrictions in many jurisdictions.

---

## 18. Vessels & Aviation

### What Questions This Family Answers
- Where is this ship or aircraft currently?
- What is the vessel/aircraft history and ownership?
- What routes has it traveled?

### Typical Use Cases
- Maritime and aviation tracking
- Ownership verification
- Route and travel pattern analysis

### Example Tools
- **MarineTraffic** (marinetraffic.com) – vessel tracking
- **VesselFinder** (vesselfinder.com)
- **FlightAware** (flightaware.com) – flight tracking
- **FlightRadar24** (flightradar24.com)
- **FAA Registry** (registry.faa.gov) – US aircraft
- **Lloyd's List Intelligence** (maritime data)

---

## 19. Data Leaks, Breaches & Paste Sites

### What Questions This Family Answers
- Has this email/username appeared in a data breach?
- Are there leaked credentials for this account?
- Has sensitive data been posted to paste sites?

### Typical Use Cases
- Security risk assessment
- Credential exposure checks
- Finding leaked corporate/personal data

### Example Tools
- **HaveIBeenPwned** (haveibeenpwned.com)
- **Dehashed** (dehashed.com)
- **LeakCheck** (leakcheck.io)
- **Pastebin** (pastebin.com) – manual searches
- **Psbdmp** (psbdmp.ws) – paste search engine
- **IntelX** (intelx.io) – darknet data

**Legal/ethical note**: Viewing leaked data may be legal, but using it unethically (e.g., credential stuffing) is illegal. Access responsibly.

---

## 20. Reverse Image Search & Facial Recognition

### What Questions This Family Answers
- Where else does this image appear online?
- Who is the person in this photo?
- Has this image been altered or manipulated?

### Typical Use Cases
- Verifying profile photos
- Finding other accounts using same image
- Detecting fake profiles
- Identifying individuals (ethically and legally)

### Example Tools
- **Google Images** (images.google.com) – reverse image search
- **Yandex Images** (yandex.com/images) – often superior for faces
- **TinEye** (tineye.com) – oldest/earliest appearance
- **PimEyes** (pimeyes.com) – facial recognition (ethical use only)
- **Social Catfish** (socialcatfish.com) – scam detection
- **FaceCheck.ID** (facecheck.id)

**Ethical note**: Facial recognition has serious privacy implications. Use only for legitimate purposes with legal basis.

---

## 21. Image & File Metadata Tools

### What Questions This Family Answers
- What camera took this photo?
- Where was this photo taken (GPS coordinates)?
- When was this file created/modified?
- Has this image been edited?

### Typical Use Cases
- Geolocation from photos
- Verifying authenticity of images
- Finding hidden metadata in documents

### Example Tools
- **EXIF viewers** (Jeffrey's EXIF Viewer, exifdata.com)
- **FotoForensics** (fotoforensics.com) – detect manipulation
- **Metadata2Go** (metadata2go.com)
- **ExifTool** (exiftool.org) – command-line extraction
- **InVID / WeVerify** (verification plugin for images/videos)

---

## 22. Maps, Geolocation & Satellite Imagery

### What Questions This Family Answers
- What does this address look like?
- What's at these GPS coordinates?
- What has changed at this location over time?

### Typical Use Cases
- Verifying addresses
- Property visualization
- Geolocation challenges (finding photo locations)
- Environmental and infrastructure analysis

### Example Tools
- **Google Maps** (maps.google.com)
- **Google Earth** (earth.google.com) – historical imagery
- **Street View** (embedded in Google Maps)
- **OpenStreetMap** (openstreetmap.org)
- **Zoom Earth** (zoom.earth) – satellite view
- **MapBox** (mapbox.com)
- **HERE WeGo** (wego.here.com)

---

## 23. Webcam Search & Live Feeds

### What Questions This Family Answers
- Are there live webcams near this location?
- What does this area look like in real time?
- Are there security cameras I can view legally?

### Typical Use Cases
- Real-time location verification
- Environmental context
- Weather and traffic conditions

### Example Tools
- **EarthCam** (earthcam.com) – public webcam directory
- **Insecam** (insecam.org) – unsecured webcams (ethical concerns)
- **Windy Webcams** (windy.com/webcams)
- **Skyline Webcams** (skylinewebcams.com)
- **Airport webcams** (various)

**Ethical note**: Do not access unauthorized or private camera feeds.

---

## 24. Timeline, Visualization & Graph Tools

### What Questions This Family Answers
- How can I visualize connections between entities?
- What is the timeline of events?
- How are these data points related?

### Typical Use Cases
- Building network graphs (people, companies, events)
- Timeline construction for investigations
- Visual presentations of findings

### Example Tools
- **Maltego** (maltego.com) – link analysis and graphing
- **Gephi** (gephi.org) – network visualization
- **Timeline JS** (timeline.knightlab.com)
- **Palantir Gotham** (enterprise-level, expensive)
- **i2 Analyst's Notebook** (IBM tool for LE/intel)
- **Cytoscape** (cytoscape.org) – network analysis

---

## 25. Charities & Non-Profit Organizations

### What Questions This Family Answers
- Is this charity legitimate?
- What are the organization's financials?
- Who are the board members and officers?

### Typical Use Cases
- Verifying non-profit legitimacy
- Donor due diligence
- Researching organizational structure

### Example Tools
- **GuideStar** (guidestar.org) – US non-profit database
- **Charity Navigator** (charitynavigator.org) – ratings
- **IRS Tax Exempt Organization Search** (irs.gov/charities)
- **ProPublica Nonprofit Explorer** (projects.propublica.org/nonprofits)
- **CharityWatch** (charitywatch.org)

---

## 26. E-Commerce & Marketplace Intelligence

### What Questions This Family Answers
- What products is this seller offering?
- What is the seller's reputation?
- Are there reviews or complaints?

### Typical Use Cases
- Seller verification
- Product research
- Scam detection

### Example Tools
- **Amazon Seller Lookup** (manual searches)
- **eBay Seller Check** (feedback analysis)
- **Etsy Shop Stats** (manual analysis)
- **Alibaba/AliExpress** (supplier verification)
- **Trustpilot** (trustpilot.com) – review aggregator
- **Fakespot** (fakespot.com) – fake review detection

---

## 27. Privacy & Opt-Out Tools

### What Questions This Family Answers
- How can targets remove their data from aggregators?
- What privacy protections exist?
- How do I reduce my own OSINT footprint?

### Typical Use Cases
- Privacy advocacy
- Helping clients reduce exposure
- Understanding data broker ecosystem

### Example Tools
- **DeleteMe** (deleteme.com) – paid removal service
- **PrivacyDuck** (privacyduck.com)
- **Opt-out guides** (various)
- **Data broker opt-out pages** (Spokeo, Whitepages, etc.)
- **GDPR/CCPA data deletion requests** (legal right to erasure)

**Note**: This family is defensive OSINT (protection), not offensive (gathering).

---

## 28. Domain, IP & Network Infrastructure

### What Questions This Family Answers
- Who owns this domain?
- What IP addresses are associated?
- What services are running on this server?
- What is the hosting provider?

### Typical Use Cases
- Technical reconnaissance
- Infrastructure mapping
- Cybersecurity assessments
- Ownership verification

### Example Tools
- **WHOIS Lookup** (whois.domaintools.com, who.is)
- **ViewDNS** (viewdns.info) – DNS tools
- **DNSdumpster** (dnsdumpster.com) – domain recon
- **Shodan** (shodan.io) – device/service search
- **Censys** (censys.io) – internet-wide scanning
- **RiskIQ PassiveTotal** (passivetotal.org)
- **SecurityTrails** (securitytrails.com)

---

## How to Use This Document

### For a Person Investigation
Prioritize these families:
- People Aggregators (#9)
- Social Networks (#5–8)
- Phone & Email (#10–11)
- Data Leaks (#19)
- Images (#20–21)
- Property/Vehicles (if relevant, #16–17)

### For a Company Investigation
Prioritize these families:
- Business Entity Search (#14)
- Business Financial (#15)
- Court Records (#13)
- Domain/Infrastructure (#28)
- News Search (#2)
- Officers → Person searches (#9)

### For a Domain/Website Investigation
Prioritize these families:
- Domain/IP/Infrastructure (#28)
- Web Archiving (#3)
- Search Engines (#2)
- SSL/Security (use Shodan/Censys from #28)

### For a Location Investigation
Prioritize these families:
- Maps & Satellite (#22)
- Webcams (#23)
- Property Search (#16)
- Image Geolocation (#21)

---

## Staying Current

OSINT tools change constantly. To stay updated:
- Follow OSINT communities (Reddit r/OSINT, Twitter #OSINT)
- Check OSINT Framework (osintframework.com) regularly
- Review GitHub OSINT tool repos
- Subscribe to OSINT newsletters (Week in OSINT, Sector035, etc.)
- Test new tools but **always verify legality and ethics**

---

**You now have a complete map of OSINT tool families.** Use this as your systematic investigation checklist. For each case, identify relevant families, pick 2–5 tools per family, and work through them methodically.
