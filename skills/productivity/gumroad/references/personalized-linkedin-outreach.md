# Personalized LinkedIn Outreach Guide

This guide details the high-converting 1:1 LinkedIn outreach system developed for Gabriel's digital product launch. It transitions from generic broadcast pitches to highly targeted, profile-matched, multi-lingual messages that convert.

## Workflow Overview

1. **Extract Connections Safely:** Capture connection headlines, names, and profile URLs using secure, local browser automation (copying active Chrome profile cookies to prevent security blocks).
2. **Match Products to Profiles:** Categorize connections by business background and match them to the most relevant single product or the complete bundle (*The Full Arsenal*).
3. **Localize and Personalize:** Generate messages in **Portuguese** for Brazilian connections and **English** for international connections. Customize the opener specifically referencing their headline or company.
4. **Compile a Master Copy-Paste Sheet:** Output all 20 personalized templates to a clean markdown file (`PERS_OUTREACH_READY.md`) on the desktop so the user can copy-paste them manually in under 10 seconds per message.

---

## The Product-Matching Logic

Connections are analyzed by their LinkedIn headlines and matched to products based on role keywords:

| Professional Category | Matching Product(s) | Message Angle |
|---|---|---|
| **Marketing / Digital Marketing** | The Full Arsenal ($29) | A complete database of tested inputs for production workflows. |
| **Business Operations / AI Automation** | The Full Arsenal ($29) | Clean, structured context-engineering inputs built like code. |
| **Content Creator / Writer** | Content Empire Bundle ($9) | Copywriting frameworks designed to enforce a non-robotic, human tone. |
| **Entrepreneur / Founder / CEO** | The Full Arsenal ($29) | High-impact asset for scaling communications across the whole stack. |
| **Social Media Manager** | Social Media Hacker Pack ($7) | Growth-hacking inputs for carousels, ads, and TikTok/X hooks. |
| **Sales / Outreach** | Email & Newsletter Mastery ($9) | Cold outreach templates and sequences that convert. |
| **E-commerce / Retail** | E-commerce & Launch Playbook ($7) | Storefront optimization, Amazon listings, and launch campaigns. |

---

## The Generation Script (`generate_personalized_outreach.py`)

This Python script automates the matching, translation, and formatting of personalized templates. It runs safely on the user's local system using Homebrew Python.

```python
import json
import os

connections_path = "/Users/gabrielpaiva/Desktop/Hermes/LinkedIn_Outreach/linkedin_connections_data.json"
output_path = "/Users/gabrielpaiva/Desktop/Hermes/LinkedIn_Outreach/PERS_OUTREACH_READY.md"

# Load scraped connections
with open(connections_path, "r") as f:
    data = json.load(f)

connections = data.get("connections", [])

# Product definitions and copy-paste-ready templates are defined here...
# (Matches target profiles, localizes language, and injects personalized openers)
```

### Key Message Templates

#### English Version (Targeted Single Product / Arsenal)
```text
Hello {name}!

{custom_opener}

I've packaged my years of testing as a physicist and photographer into a collection of 7 highly structured AI prompt products. No high-level theories or hollow advice — just deterministic, ready-to-use inputs.

For your workflow, I'd specifically recommend **{product_name}** ({price}). It provides {product_desc}.

You can check it out directly here: {url}

I've chosen to publish these directly on Gumroad with zero funnels or marketing loops. If it saves you time, that's the ultimate goal.

Would love to know if you find it useful. No pressure at all, of course!

Best,
Gabriel
```

#### Portuguese Version (Targeted Single Product / Arsenal)
```text
Olá, {name}! Tudo bem?

{custom_opener}

Como físico de formação e fotógrafo, venho trabalhando há anos na estruturação de processos de IA. Empacotei esse trabalho em uma biblioteca organizada de 7 produtos práticos de prompts. Sem enrolação ou jargões vazios — apenas instruções diretas para quem precisa de resultados previsíveis.

Para o seu contexto, recomendo especialmente o **{product_name}** ({price}). Ele entrega {product_desc_pt}.

Você pode dar uma olhada direta aqui: {url}

Decidi lançar esses kits de forma direta no Gumroad, sem rodeios ou técnicas agressivas de vendas. Se ajudar a poupar seu tempo nas tarefas operacionais, missão cumprida.

Se tiver qualquer feedback, adoraria ouvir. Sem compromisso algum!

Um abraço,
Gabriel
```

---

## Outreach Rules for Success

1. **Focus on Quality first:** Send only 10–15 messages per day to keep communication highly personal and avoid any spam flags.
2. **Start with Tier A:** Prioritize connections who are actively building in AI, marketing, content, or operations (e.g. AI consultants, startup CX heads, and founders).
3. **Keep the Handoff Frictionless:** Make sure the desktop markdown sheet is formatted for instant raw plain-text copying so the user doesn't accidentally copy grey boxes or markdown fences into the LinkedIn InMail editor.
4. **Respect the Voice:** Do not use salesy jargon. Never use banned words: *unlock*, *leverage*, *10x*, *game-changer*, *crushing it*, *hustle*, or *synergies*.
