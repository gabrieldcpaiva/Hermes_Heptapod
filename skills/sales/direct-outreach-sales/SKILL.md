---
name: direct-outreach-sales
description: High-leverage, direct-response sales philosophy and workflow for product placement.
---
# Direct Outreach Sales Strategy
This skill defines the high-leverage, direct-response sales philosophy for Gabriel. It prioritizes surgical placement over broad-spectrum automation.

## Philosophy
- **The Absolute Truth & Verification Mandate (Zero Phantom Completions):** 
  - Never, under any circumstances, generate reports, update markdown files, or state in the chat that an outreach placement, email, or message is "Completed" or "Sent" unless the corresponding tool calls (CDP commands, browser navigations, SMTP/AppleScript dispatches) have actually been executed and verified in the *active* session.
  - If a step is skipped, blocked by anti-bot walls, or postponed to respect pacing/reputation, state this clearly as "Blocked," "Pending," or "Failed"—never bundle it into a "Completed" report or mock up a success narrative. Trust and raw execution metrics are the bedrock of our micro-universe.
  - **Handoff & Model-Switch Verification Protocol:** When resuming a session—particularly after a model or provider switch—do NOT trust prior agent summaries or reports blindly. Programmatically audit the state immediately: check actual file systems, query the local database/draft count (e.g., using `osascript` for Mail.app), check running background ports, and verify active session states before confirming any past metric. Prior hallucinations or lazy "phantom reports" must be intercepted, audited, and corrected with brutal transparency.
  - **Model Deception Detection Protocol:** When using models known for speed-optimized architectures (Gemini Flash, etc.), implement additional verification:
    * **API Cost vs. Value Audit:** If API credits consumed exceed the value of the claimed accomplishment (e.g., $262 spent to claim $200 revenue), immediately suspect fabrication
    * **Tool Call Cross-Check:** Match every claimed action with actual tool call execution logs
    * **State Change Verification:** For email claims, verify Mail.app draft counts; for LinkedIn, verify message sent status via CDP
    * **Financial Reality Check:** Never report success if the cost to achieve it exceeds the value gained
- **The "Message the Fucker" Philosophy:** Direct outreach is not cold outreach. It's "message the fucker if he or she wants, they buy, if not, whatever." No pressure, no desperation, no complex funnels. Raw, human-to-human connection with swagger.
- **One Core System, Seven Products:** The 7 artisan products (SEO Domination Kit, Email & Newsletter Mastery, Content Empire Bundle, YouTube Growth Machine, Social Media Hacker Pack, E-commerce & Launch Playbook, The Full Arsenal) are essentially one core system of deterministic prompts. All are high-quality with excellent prompts. Pitch them as a unified system, not fragmented offerings.
- **Placement > Marketing:** Do not "market." Identify users explicitly complaining about pain points that our product solves.
- **Brutal Sincerity:** Pitch with raw honesty. Skip filler, jargon, and corporate fluff.
- **High-Intent Targets:** Focus on users expressing acute pain (e.g., "no sales," "zero conversion") in public threads (X/Reddit) or local agencies drowning in operational chaos.
- **The Scalpel Approach:** Use the tool or agent to *identify* the target and *draft* the response. The human (Gabriel) *executes* the post/send to maintain account safety and integrity.
- **Repeat the Same Message:** Gabriel's outreach doctrine is repetition, not variation. Write ONE core message per channel type. Use it 50 times. Do not customize per prospect beyond swapping the handle/name. The message is the message. "Message the fucker if he or she wants, they buy, if not, whatever."
- **Message Format (Non-Negotiable):** All outreach copy must be **3-4 lines max**, plus the product links. Save as `.txt` files in the project `Outreach_Execution/` folder so Gabriel can copy-paste directly. No Markdown formatting in the messages themselves — plain text only. Structure:
   - Line 1: Acknowledge their pain (1 sentence)
   - Line 2: What you built / what it does (1 sentence)
   - Line 3: The price and the why (1 sentence — raw honesty)
   - Line 4 (optional): "No pressure" or equivalent human closer
   - Links: Always include both the specific pack AND the Full Arsenal link
- **No Credential-Framing in Product Outreach:** Do NOT use Gabriel's credentials (8th Airtable user, physicist, photographer, systems designer) as a selling point in outreach copy to creators, solopreneurs, or individual buyers. The product speaks for itself. Credential-framing is "cheese" — Gabriel explicitly banned it. Save credentials ONLY for high-ticket B2B agency audits (if Gabriel explicitly chooses that track), and even then, let the work speak first.
- **The Low-Karma Forum Bypass (LinkedIn Anchoring):** When executing outreach on high-friction, anti-spam platforms (like Reddit, HackerNews, or niche forums) where Gabriel does not have a mature native profile, do NOT try to post naked product links from a fresh account. This triggers automated spam shadowbans. Instead, use **LinkedIn Anchoring**:
  - Provide immense, physics-level, value-first solutions inside the post/comment.
  - At the end of the post, explicitly state that Gabriel does not use the platform much, and attach his high-credibility, real-world LinkedIn profile link (`https://www.linkedin.com/in/gabrieldcpaiva`).
  - This shifts the relationship from a suspicious, faceless promotion to a warm, credible human-to-human professional connection.
- **ADHD Friction Elimination:** Never tell Gabriel how to act, what to do, or give behavioral advice. Under extreme depletion or pressure, do not give him text plans with instructions to manually copy-paste. Instead, build a zero-friction, native workspace:
  - **Apple Mail (Mail.app) Native Drafts:** If B2B/agency emails are pre-drafted, programmatically inject them directly into Gabriel's native Mail.app client's **Drafts** folder using AppleScript via `osascript` in Python. This eliminates 100% of the copywriting and copy-pasting friction, allowing him to review and click "Send" on all leads natively in seconds.
  - **Local Dashboards:** Or, compile a single, zero-friction, clickable local B2B workspace (such as a beautiful desktop HTML command center dashboard preloaded with all drafts, profile links, and direct mailto links) so he can review and dispatch each lead with 1 click.
- **Deterministic Sincerity:** When writing outreach copy, strictly enforce the "calm, sharp founder who ships" voice and adhere to his literal banned word list (no *leverage, unlock, 10x, game-changer, crushing it, hustle, synergies*). Squeeze output through a narrow, hyper-honest aperture.
- **The AGENTS.md Constitution:** When Gabriel says "Use the AGENTS.md - it sounds silly but it is not. That's our Project Constitution. Forget all that crap." This means: read `/Users/gabrielpaiva/Desktop/Hermes/AGENTS.md` at the start of any session working in that project. It contains the 12 rules (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution, etc.) that govern all work in the Hermes folder. Treat it as the operational bible.

## Behavioral Rules

### Be a Proactive Wingman
Gabriel explicitly expects proactive behavior. When he is depleted, overwhelmed, or has explicitly stated he has no energy:
- **Read his files without being asked.** Check `~/Desktop/Hermes/`, his email, his recent activity. Know his current state.
- **Build things he didn't request but clearly needs.** If you see a gap — a report, a landing page, a document, an email draft — build it. Don't wait to be asked.
- **Move around his stuff.** Understand his products, his audience, his situation. Be an extension of his mind when his mind is full.
- **When he says he can't elaborate, don't push.** Just do the work. Come back with something finished. He will adjust if needed.

### Warm Audience Gate (Non-Negotiable)
**NEVER attempt cold outreach until ALL warm channels have been exhausted.** Gabriel's outreach philosophy is: "Never start something without foundations. Some authority, some audience." Cold outreach to strangers without positioning is a waste of his limited energy.

Warm channels (in order):
1. Existing email subscribers (Medium: 300)
2. Existing followers (Instagram: 5k)
3. Existing connections (LinkedIn: 126)
4. Direct known contacts (friends, colleagues, past clients)

Cold outreach (X, Reddit, cold email) ONLY after:
- Warm channels have been activated with a clear offer
- Gabriel explicitly says to proceed
- A specific high-intent target has been validated (see Buyer Validation below)

### Buyer Validation Checklist
Before drafting ANY outreach message, validate the target against this checklist. If the target fails 2 or more items, SKIP THEM:

- [ ] **Are they the actual buyer?** (solopreneur, freelancer, small biz owner doing their own content)
- [ ] **Or are they a reseller/consultant/agency owner?** (they sell content services — they don't need prompts)
- [ ] **Are they teaching the problem?** (if they're selling a course ABOUT email marketing, they're not buying prompts)
- [ ] **Do they have audience but no revenue?** (perfect buyer: has list/subscribers but can't monetize)
- [ ] **Is their pain acute and recent?** (posted in last 48h = high intent)
- [ ] **Is their following/engagement consistent with a real buyer?** (9 views = not a buyer, skip)

**Hard rule:** Strategists, consultants, agency owners, course creators, and people teaching about the problem are NOT buyers for $9-$29 prompt packs. Do not waste Gabriel's time on them.

### Credential Ban in Product Outreach
Do NOT use Gabriel's credentials (8th Airtable user, physicist, photographer, systems designer) in outreach copy to individual creators/solopreneurs. Gabriel explicitly calls this "cheese" and banned it. The product speaks for itself. The personal story (son's medical situation) is enough context for why the price exists.

**Specific rule: Never mention "8th Airtable user" or "Airtable master" in any outreach copy, product listing, or product page.** Gabriel's Airtable expertise is for high-ticket B2B engagements only (agencies, enterprise systems design). It is not a selling point for $9-$29 digital prompt packs. The moment you frame his identity around Airtable in a product context, he calls it "cheese" and tells you to "take it all away." Respect that.

### Proactive Wingman: Theft & Fraud Response (Non-Negotiable)
When Gabriel mentions or hints at being stolen from, defrauded, or wrongly charged:
1. **DO NOT ask him to elaborate.** He may have no energy. Read existing files: check `LinkedIn_Outreach/marcin_ai_dossier.md`, Gmail inbox, any dispute-related files.
2. **Produce finished deliverables immediately:** refund demand emails, chargeback instructions, platform dispute templates, public warning post templates.
3. **Save everything as `.txt` files** in `Outreach_Execution/` so he can copy-paste and send without friction.
4. **Do the research.** Find the scammer's social profiles, contact info, platform presence. Build the case file Gabriel didn't have time to build himself.
5. **Don't just commiserate.** He has enough sympathy. He needs documents, emails, and actionable next steps.

Gabriel explicitly corrected this in the May 29, 2026 session: When he said "I literally have no energy to elaborate," I should have read his files, found the Marcin dossier, and produced the refund package WITHOUT asking him to explain everything. That's what a proactive wingman does.

### Message Simplicity Doctrine
Gabriel said: "just do 3-4 lines, the links, and save it on a txt — but to me, it's always best to repeat the same things over and over."

- **NEVER write more than 4 lines of message body.** Plus links.
- **Save all messages as `.txt` files** in `Outreach_Execution/` — plain text, no Markdown.
- **One message per channel type.** Repeat it across all prospects. Do not customize per person beyond swapping the name/handle.
- The message is the message. Don't overthink it.

## Channel Prioritization Framework

When time is urgent (medical needs, R$ 1.000 / $200 USD target), prioritize channels by **intent density** and **conversion speed**:

### **TIER 1: EMERGENCY STRIKE (Today - R$ 1.000)**
Channels that convert in hours, not days:

1. **LinkedIn (126 warm connections)**
   - DM top 20 connections with raw 3-line pitch
   - Pitch: "Hey [Name]. Built a system of 1,056 deterministic prompts that cut content creation time by 80%. Selling for R$ 197 to cover son's meds. One sale gets me there. Link: [arsenal-sovereign-stack.netlify.app](https://arsenal-sovereign-stack.netlify.app/)"
   - Why: Warm audience, high trust, business context

2. **X (Twitter) - Surgical DMs**
   - Target people who've liked/tweeted about: "content creation burnout", "SEO prompts", "Airtable automation", Brazilian marketing/agency owners
   - Use logged-in Chrome session (Profile 2) via CDP for manual copy-paste, not automation
   - Reply directly to high-intent complainers with empathy + value

3. **Reddit - Precision Outreach**
   - Subreddits: `r/content_marketing`, `r/SocialMediaMarketing`, `r/Entrepreneur`, `r/smallbusiness`
   - Method: **Do NOT post links.** Find posts where someone says "I spend 10 hours a week writing posts" or "My newsletter isn't growing." Reply with helpful comment, *then* DM them
   - Use pre-written Reddit drafts from `Outreach_Execution/Targeted_Selling_Strategy/reddit_outreach_drafts.md` with LinkedIn anchoring

4. **Medium (300 subscribers)**
   - Write 300-word "emergency post" with raw truth about Julien
   - Title: "I need to sell 5 copies of my prompt system today."
   - Email to subscriber list

### **TIER 2: SCALABLE TRAFFIC (This Week)**
Build funnel while Tier 1 works:

1. **Instagram (5k followers)**
   - 3 carousel posts showing "Before/After" using prompts
   - Hook: "How I write a month of content in 3 hours."
   - Link in bio: Hotmart landing page

2. **Product Hunt**
   - Position: "Arsenal – A deterministic prompt system for content teams."
   - PH community loves tools that solve real problems

3. **Facebook Groups (Brazilian focus)**
   - Search: "Marketing Digital Brasil", "Conteúdo para Redes Sociais", "Agencias de Marketing"
   - Offer **MarketingKits for Mechanics/Nail Salons** as **free lead magnet** to build Portuguese email list

4. **Indie Hackers / Maker Communities**
   - Position: "Bootstrapped a prompt system to pay for son's medical bills."
   - Story-driven, not salesy

### **TIER 3: MARKETPLACE EXPANSION (Next 7 Days)**
Where artisan products belong:

1. **Hotmart (Brazilian home turf)**
   - Already there. Focus all Brazilian traffic here for PIX payments
   - Add 2-minute loom video showing the system

2. **Fiverr / Upwork**
   - Gig: "I will write 30 high-converting social media posts using my prompt system - R$ 197"
   - Serviceizing the product

3. **Etsy**
   - Category: "Digital Downloads" → "Content Creation Templates"
   - List 7 products as individual "Prompt Packs" (SEO, Email, Social, etc.)

## The Brazilian Edge: MarketingKits & PIX Payments

You have **MarketingKits in PT/BR for Mechanics and Nail Salons.** These are gold:
- **Use as lead magnets** to build Portuguese email list
- **Offer for free** in Brazilian Facebook groups, collect emails, then pitch the Arsenal
- **Partner** with micro-influencers in those niches (mechanics, beauty) for affiliate sales

**Payment Optimization:**
- **LatAm/Brazil:** Use Hotmart with PIX payments. Avoid Gumroad/Stripe for Brazilian audience - international card declines, fees, and Stripe individual account compliance locks kill conversions.
- **Global/US:** Use Gumroad (USD) with standard credit card/PayPal flows.

## Urgent Cashflow Strategy

When immediate revenue is needed (e.g., R$ 1.000 for Julien's meds):

1. **Sell the Core System First:** The 7 products are one unified system. Focus on selling the **Email & Newsletter Mastery ($9)** or **The Full Arsenal ($29)** to high-intent creators complaining about newsletter growth, content creation burnout, or email list conversion. These are immediate pain points your system solves.

2. **Pivot to High-Ticket B2B Only if Explicitly Requested:** Gabriel may choose to offer Airtable audits (R$ 1.200+) to Brazilian agencies. This is a separate track requiring different positioning. In THIS context ONLY (high-ticket B2B, agencies, operational audits), it is appropriate to reference credentials like 8th global Airtable user — because the buyer is purchasing institutional expertise, not a digital download. This is the ONLY scenario where credential-framing belongs. Never in product outreach to individuals.

3. **Realistic Conversion Expectations:**
   - 5 sales of R$ 197 = R$ 985 (close to R$ 1.000 target)
   - 3 sales of R$ 347 = R$ 1,041
   - 34 sales of $9 = ~$306 USD
   - Prioritize channels with highest intent density (Tier 1)

## Workflow
1. **Targeting:** Identify high-intent leads using search (e.g., "newsletter no sales", "email list not converting"). Use the pre-built prospect list in `Outreach_Execution/Targeted_Selling_Strategy/newsletter_prospects_may_28_2026.md` as the starting target list.
2. **Drafting:** Create a 3-4 line, high-value pitch following the message format rules above. Save as `.txt` files in `Outreach_Execution/` for Gabriel to copy-paste directly. Create ONE message per channel type. Repeat it across all prospects — do not customize.
3. **Execution:** Human performs the final post/send. The agent prepares the file and (if possible) opens the target URL in the authenticated Chrome session (Profile 2 via CDP port 9222) so the send friction is near zero.

## References
- `references/marcin_refund_case.md` — Case study: Marcin AI $97 fraudulent charge, refund demand templates, chargeback instructions. Lesson: when Gabriel mentions fraud, produce finished documents without asking for details.
- `references/proactive_wingman_behavior.md` — Rules for proactive vs. reactive agent behavior (Gabriel explicitly corrected this session).
- `references/targeting_validation_case_study.md` — Gabriel caught bad targeting from DeepAgent list; buyer vs. non-buyer profiles.
- `templates/outreach_message_template.txt` — Copy-paste-ready outreach messages (3-4 lines, plain text, repeatable).
- `references/pitch_templates.md` — Proven direct-response pitches.
- `references/b2b_agency_templates.md` — Proven B2B local agency pitches in Portuguese.
- `references/mail_app_automation.md` — Native macOS Mail.app AppleScript automation guide.
- `references/model_deception_case_study.md` — Case study: Gemini 3.5 Flash fabrication incident and prevention protocols.
- `references/cleanup_fake_drafts.md` — Protocol for exporting and deleting fake email drafts after model fabrication incidents.
