# B2B Lead Sourcing, Crawling, and High-Ticket Systems Positioning Pivot

This reference document outlines the programmatic workflow for scraping, crawling, and verifying local business leads (e.g., digital marketing/SEO agencies in Brazil) and the strategic positioning shift from low-ticket products to a high-ticket "Systems Operational Audit" to maximize conversion and accelerate cash flow during financial urgencies.

---

## 🚀 The Core Philosophy: The High-Ticket Systems Pivot

When a user has an urgent cash flow requirement (e.g., raising $200 / R$ 1.000 for medical treatments) and is selling digital products, there are two distinct paths:

1. **Low-Ticket Transactional Volume:** Selling R$ 297 (~$50) digital prompt bundles. This requires high volume, has higher conversion friction, and relies on immediate purchase intent.
2. **High-Ticket Systems Positioning (Recommended):** Offering a high-value operational service, such as a **"Diagnóstico de Gargalos & Arquitetura de Dados" (Operational Bottleneck & Airtable Audit)** for R$ 1.200 (~$200 USD). This leverages the user's premium, world-class skills (e.g., being the **8th global user of Airtable**, a physicist, or a systems architect).
   - *Why it works:* It collapses the required customer count from 5-6 low-ticket buyers to **just one single high-ticket buyer**. 
   - *The Onboarding Bonus:* The user includes their low-ticket prompt pack (e.g., *O Arsenal Soberano*) as a free onboarding integration gift, magnifying the perceived value of the audit.

---

## 🛠️ Programmatic B2B Sourcing & Crawling Engine (Python)

To feed the outreach pipeline, you can run an autonomous lead generation script. This Python script performs localized DuckDuckGo HTML searches, extracts unique domains, and crawls their homepages/contact pages to harvest verified contact emails.

```python
import urllib.request
import urllib.parse
import re
import ssl
import json
import time

# Disable SSL verification for crawling dynamic local sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

def search_ddg_domains(query):
    """Search DuckDuckGo HTML interface and extract unique, relevant domains."""
    encoded_query = urllib.parse.quote(query)
    url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
    req = urllib.request.Request(url, headers=headers)
    domains = []
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            links = re.findall(r'href="([^"]+)"', html)
            for link in links:
                if "uddg=" in link:
                    actual_url = urllib.parse.unquote(link.split("uddg=")[1].split("&")[0])
                    parsed = urllib.parse.urlparse(actual_url)
                    domain = parsed.netloc.replace("www.", "")
                    if domain and "." in domain and not any(x in domain for x in [
                        "duckduckgo", "youtube", "linkedin", "facebook", "instagram", 
                        "twitter", "medium", "clutch", "sortlist", "themanifest", "wikipedia"
                    ]):
                        if domain not in domains:
                            domains.append((domain, f"https://www.{domain}/"))
            return domains
    except Exception as e:
        print(f"DuckDuckGo search failed: {e}")
        return []

def extract_emails_from_url(url, timeout=6):
    """Fetch website HTML and harvest emails, filtering out common binary/design assets."""
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as response:
            html = response.read().decode('utf-8', errors='ignore')
            found = email_regex.findall(html)
            valid_emails = []
            for email in found:
                email_lower = email.lower()
                # Filter out standard template elements or image extensions
                if not any(ext in email_lower for ext in [
                    ".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", "w3.org", "sentry.io", "github.com", "domain.com"
                ]):
                    if email not in valid_emails and "%20" not in email:
                        valid_emails.append(email)
            return valid_emails
    except Exception:
        return []

# Example Usage: Sourcing localized agencies in Sao Paulo & Campinas
sp_domains = search_ddg_domains('"agência de marketing digital" "são paulo" site:.com.br')
time.sleep(2)
campinas_domains = search_ddg_domains('"agência de marketing digital" "campinas" site:.com.br')

all_domains = list(set(sp_domains + campinas_domains))
leads = []

for domain, url in all_domains[:15]:
    print(f"Crawling {domain}...")
    emails = extract_emails_from_url(url)
    
    # If homepage is empty, try the contact sub-page
    if not emails:
        contact_url = f"{url}contato"
        print(f"  Empty homepage. Trying contact page: {contact_url}")
        emails = extract_emails_from_url(contact_url, timeout=4)
        
    if emails:
        print(f"  -> Sourced verified emails: {emails}")
        leads.append({
            "domain": domain,
            "url": url,
            "emails": emails
        })
```

---

## 📋 Consolidated Lead Database Schema (`agency_leads_ptbr.json`)

To prevent duplicate runs and track outreach pipeline statuses, maintain a clean, flat JSON file containing only verified contacts.

```json
[
  {
    "domain": "digitallevolution.com.br",
    "url": "https://www.digitallevolution.com.br/",
    "emails": [
      "contato@digitallevolution.com.br"
    ]
  },
  {
    "domain": "lr3digital.com.br",
    "url": "https://www.lr3digital.com.br/",
    "emails": [
      "lr3digital.mkt@gmail.com"
    ]
  }
]
```

---

## 💬 The Dual-Track Sincere Outreach Structure (PT-BR)

Every agency on the lead list should be pitched using two tracks to provide execution flexibility. Maintain the "calm, sharp craftsman" persona with **zero banned words** (no leverage, alavancar, unlock, destravar, 10x, game-changer).

### Track A: Low-Ticket Prompt Pack (R$ 297 PIX on Hotmart)
- **Angle:** Focus on operational efficiency for the agency's writing/creative team.
- **Copy Template:**
```text
Assunto: Uma esteira com 1.056 prompts estruturados para a redação da [Nome da Agência]

Olá, pessoal da [Nome da Agência]!

Meu nome é Gabriel. Sou físico de formação, fotógrafo e designer de sistemas de dados e automação de conteúdo.

Acompanho o ecossistema de agências e sei como o tempo de criação de conteúdo, SEO e copywriting é o principal ralo financeiro na operação diária. Por isso, decidi abrir o meu sistema de prompts que utilizo em minhas próprias bases de dados.

Eu não crio "templates genéricos" ou ideias vagas para o ChatGPT. Eu desenho instruções determinísticas. São 1.056 prompts de alta performance, categorizados, etiquetados e testados exaustivamente para cobrir redação, planejamento de SEO, roteiros de YouTube, e-commerce e e-mail marketing.

Para agências digitais que buscam consistência mecânica sem perder a voz autoral dos clientes, o Arsenal Soberano funciona como uma esteira de produção refinada que economiza dezenas de horas de escrita por semana.

Disponibilizei o ecossistema completo com web apps offline dedicados e PDFs de suporte por R$ 297 (pagamento único via PIX, entrega imediata via Hotmart).

Vocês podem ver o sistema funcionando ao vivo aqui:
https://arsenal-sovereign-stack.netlify.app/

Estou abrindo esse sistema por esse valor por um motivo de força maior: sou pai solo e preciso cobrir os custos médicos de tratamento do meu filho mais novo. Se o sistema puder otimizar as entregas da [Nome da Agência] e poupar o time de tarefas manuais repetitivas, será uma excelente parceria.

Um abraço,
Gabriel Paiva
Físico & Designer de Sistemas
```

### Track B: High-Ticket Audit (R$ 1.200 Bottleneck & Airtable Audit)
- **Angle:** Position the user as the **8th global user of Airtable**, analyzing their broken spreadsheets and manual loops.
- **Copy Template:**
```text
Assunto: Uma proposta de auditoria operacional de processos e Airtable para a [Nome da Agência]

Olá, pessoal da [Nome da Agência]!

Meu nome é Gabriel. Sou físico teórico, fotógrafo e designer de sistemas. Também fui o 8º usuário global a criar uma conta no Airtable, tendo construído e arquitetado sistemas complexos de dados e automação de mídia ao longo da última década.

Muitas agências crescem rápido e acabam soterradas em planilhas desconexas, canais de Slack barulhentos e processos manuais que drenam a margem de lucro de cada projeto. Meu trabalho é encontrar esses gargalos operacionais e desenhar esteiras de dados que funcionem de forma silenciosa e previsível.

Gostaria de propor para a [Nome da Agência] um Diagnóstico de Gargalos de Processos:
1. Analiso o fluxo atual de trabalho e dados da agência (planilhas, CRM ou ferramentas de conteúdo).
2. Entrego um mapeamento limpo de onde vocês estão perdendo tempo e margem.
3. Desenho a estrutura ideal de um banco de dados unificado no Airtable para automatizar e rastrear a produção.

O diagnóstico e desenho da estrutura operacional custa R$ 1.200 (pagamento único). Como bônus de integração para o seu time de redação e SEO, incluo o acesso vitalício à minha biblioteca do "Arsenal Soberano" (um sistema com 1.056 prompts de alta performance para criação de conteúdo, que hoje vendo separadamente por R$ 297).

Caso queiram conhecer a engenharia por trás do Arsenal que seu time receberá:
https://arsenal-sovereign-stack.netlify.app/

Tenho poucas vagas para esse tipo de diagnóstico este mês e realizo esse serviço de forma direta e transparente. Se fizer sentido estruturar a casa para escalar a [Nome da Agência], será um prazer conversar.

Um abraço,
Gabriel Paiva
8º Usuário Global do Airtable & Designer de Sistemas
```

---

## 📨 Programmatic macOS Mail.app Dispatching & Clean-Up (AppleScript)

When B2B agency draft emails have been generated inside macOS **Mail.app**, sending them programmatically requires a robust and reliable automation path.

### The Hurdle
In AppleScript Mail.app, raw stored draft messages (`message` objects in `drafts mailbox`) do not understand the standard `.send()` command natively. Attempting to call `send draft_msg` will throw a runtime error.

### The Solution: Replication & Background Dispatch
To bypass this limitation, write a Python loop that uses AppleScript via `osascript`. The script:
1. Resolves the draft by its unique message `id`.
2. Extracts its subject, recipient, and body properties.
3. Creates a fresh, natively sendable `outgoing message` with those properties in background mode (`visible: false`).
4. Adds the recipient and triggers the `send` command.
5. Moves the original draft message natively to the `trash mailbox` in the background (which is 100% background-safe and does not require GUI focus, Accessibility permissions, or sending keystrokes).

```python
import subprocess
import time

def dispatch_and_cleanup_draft(draft_id, recipient_email):
    """
    Replicates a Mail.app draft message into a fresh outgoing message,
    sends it in the background, and cleanly moves the draft to trash.
    """
    as_code = f"""
    tell application "Mail"
        try
            set draft_msg to first message of drafts mailbox whose id is {draft_id}
            set the_subj to subject of draft_msg
            set the_content to content of draft_msg
            
            -- Create and dispatch outgoing message in background
            set new_msg to make new outgoing message with properties {{subject:the_subj, content:the_content, visible:false}}
            tell new_msg
                make new to recipient at end of to recipients with properties {{address:"{recipient_email}"}}
                send
            end tell
            
            -- Move draft to trash mailbox natively
            set mailbox of draft_msg to trash mailbox
            return "SUCCESS"
        on error errMsg
            return "ERROR: " & errMsg
        end try
    end tell
    """
    try:
        res = subprocess.run(["osascript", "-e", as_code], capture_output=True, text=True, timeout=15)
        return res.stdout.strip()
    except subprocess.TimeoutExpired:
        return "ERROR: Timeout"
    except Exception as e:
        return f"ERROR: {str(e)}"

# Example: Spaced dispatches to protect sender IP reputation
targets = [
    {"id": 52, "email": "contato@reviewcomunicacao.com.br"},
    {"id": 38, "email": "lr3digital.mkt@gmail.com"}
]

for t in targets:
    print(f"Sending to {t['email']}...")
    result = dispatch_and_cleanup_draft(t['id'], t['email'])
    print(f"Result: {result}")
    time.sleep(2) # 2-second safety delay
```

---

