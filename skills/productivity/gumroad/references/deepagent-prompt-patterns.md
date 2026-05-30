# Abacus DeepAgent — Prompt Patterns for Product Outreach

*Reference for prompting Abacus DeepAgent (browser-use + LLM workflow engine). Based on patterns Gabriel demonstrated. DeepAgent is a third-party agent engine at abacus.ai — these notes are for prompt reference, not for direct Hermes invocation.*

---

## Core Rule

DeepAgent is **literal and exhaustive**. Every instruction must be a precise command. One ambiguous phrase → 5 clarification questions. Write prompts like code, not conversation.

Ambiguous: *"Find some marketing people on LinkedIn and send them a nice message."*
Correct: *"Open LinkedIn. Search for 'content marketing manager'. Filter by 2nd degree. Open each profile. If the person works in marketing/content/SEO, send a connection request with the note: 'Hi [name], I build AI prompt packs for marketers. Would love to connect.'"*

---

## Pattern 1: CSV In → Actions → CSV Out

For batch outreach to a known list.

```
Build an AI agent that accepts a CSV file as input. Each row has Name, Email, and Company Name.
For every row:
1. Research the given company online to understand what it does and its industry challenges.
2. Read about our product from the following pages: [URLs]
3. Draft a nicely formatted personalized email to the person (use their name and company context)
   explaining how [product] can help their business. Use a professional, helpful tone.
4. Send the email through my Gmail account.
5. After sending, generate an updated CSV with: Name, Email, Company, Generated Email Text, and Status (Sent/Failed).

The agent should:
- Retry failed sends up to 2 times
- Output a downloadable CSV file
```

---

## Pattern 2: LinkedIn Browser Actions (Networking)

For finding and connecting with targets on LinkedIn.

```
Open LinkedIn. 
Search for "[role/industry]".
Filter by [distance: 1st/2nd/3rd degree].
Look through the first [N] profiles.

For each person:
- Check if they work in [target field/title]
- If yes, send a connection request with this note (personalize [name]):
  "Hi [name] — [personalized note referencing their work or company]"

After they accept, send this InMail:
"[message body]"

Output a table with: Name, Company, Role, Date Sent, Status (Connected/Declined/Pending)
```

---

## Pattern 3: Research & Structured Output (Jobs / Market Research)

For scanning a platform and extracting structured data.

```
Log in to my LinkedIn account.
Go to the Jobs section of my profile.
Make a list of 10 jobs (posted in the last one week) which are best fit for my profile
based on my profile and the job descriptions posted.

The output should be a table containing:
- Name of the company
- Role
- Link to hiring manager LinkedIn profile (if any)
- Location
- Link to the opening
- Why it's a good fit for me
```

---

## Pattern 4: Login → Navigate → Extract → Email + Spreadsheet

For pulling analytics or data from a platform and delivering it.

```
Log in to the [platform] account.
Click on [my name / profile / settings], then select [Usage Analytics / specific section].
Make sure the tab selected is [specific tab, NOT the other one].
Find the [specific data point] at the [level: workspace/account/project] level.
Send the [specific data] via email to [email address].

Along with the email, make an entry in an Excel sheet. The new entry should append to the existing list.

The email and Excel sheet should contain:
- Date, timestamp, account details, [specific data point 1], [specific data point 2]

Make sure the email is well formatted in a table format and accurate.
Note that it's very important that you fetch actual data from my account.
Do NOT use dummy or made-up data.

Repeat this task every day at [time and timezone].
```

---

## Pattern 5: Multi-Node Content Pipeline

For generating complete production-ready content packages via chained LLM + image gen nodes.

```
Create an AI workflow for generating complete [type] content packages with N nodes:

Nodes:
1. Manual Trigger — Form with: [inputs] (e.g. Topic, Platform dropdown, Tone dropdown)
2. Generate [Output 1] — LLM Agent: [specific instruction]
3. Write [Output 2] — LLM Agent: [specific instruction with format requirements]
4. Create [Output 3] — LLM Agent: [specific instruction]
5. Generate [Output 4] — [Image Generation / other tool]: [instruction]
6. Analyze Outputs — LLM Agent: Review and provide feedback
7. ... (more nodes)
N. Compile Final Report — Custom node: Format all outputs into [final format]

Critical Instructions for ALL LLM Nodes:
- Generate COMPLETE, PRODUCTION-READY content only
- NEVER ask questions or request additional information
- Use ONLY the trigger inputs and previous node outputs
- Provide final, usable outputs

Report Format:
- Clean [language] markdown (NO JSON)
- Clear section headings
- For each section: suggest 2-3 tools with clickable links
- Include step-by-step usage instructions
- Keep language simple and actionable
```

---

## Pattern 6: X/Twitter Automation (Learn → Optimize → Post)

For building a self-improving social media presence.

```
Set up a scheduled agent to run every day at [time].

On the first run:
- Analyze my Twitter history to understand topics I post about, tone, formats, language style, and apparent goals
- Store this as my evolving Twitter profile in the database

Every day after that:
- Pull my latest tweets and continuously refresh their detailed performance metrics in the database
- Learn from the performance numbers what topics, formats, timing, framing, and language styles are working and what are not
- Update my evolving Twitter profile and 'what works / what doesn't' patterns based on this data
- Do daily web research aligned with my evolving topics to find fresh trends, surprising insights, and early signals
- Save these findings into the database
- Generate 2-3 new tweet drafts optimized around what is working, never repeat or closely mirror past tweets, and deliberately vary wording, structure, and style while staying aligned with my profile
- Automatically post the selected tweets to my account and log them in the database

Each day, send me a short report with:
- What worked, what didn't
- New insights found
- The tweets that were published
```

---

## Common DeepAgent Prompt Rules

1. **No ambiguity.** Every instruction is a command. "Click on my name at the bottom left" — not "Find my profile."
2. **Complete outputs.** Every node produces a final, usable result — no "what format do you want?"
3. **Be explicit about NOT asking questions.** Add: "NEVER ask questions or request additional information."
4. **Specify real data.** When extracting data: "Use actual and real data. Do NOT use dummy or made-up data."
5. **State the negative.** Specify what NOT to do: "Make sure the tab selected is Workspace and NOT Account."
6. **Retry logic.** For sends/saves: "Retry failed sends up to 2 times."
7. **Schedule explicitly.** "Repeat this task every day at 9 PM PDT."
