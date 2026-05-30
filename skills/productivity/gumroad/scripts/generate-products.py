#!/usr/bin/env python3
"""
Generate a self-contained offline HTML webapp + PDF from a CSV prompt file.

Usage:
  python3 generate-products.py <csv_path> <output_html> <output_pdf> <title> <subtitle>

CSV must have columns: Type, Category, Prompt, Tags, Date Added, MVP
(standard Content_Master export format)

Generates:
  - Single HTML file: dark theme, category sidebar, search, copy-to-clipboard, works offline
  - PDF: cover page, table of contents, categorized prompts

Requirements:
  - Python 3.9+
  - fpdf2: pip3 install --user fpdf2
  - Arial Unicode.ttf at /Library/Fonts/Arial Unicode.ttf (macOS)
"""
import csv, json, re, os, sys
from datetime import datetime

def slugify(text):
    return re.sub(r'[^a-zA-Z0-9]+', '_', text).strip('_')

def parse_csv(csv_path):
    prompts_by_cat = {}
    categories_order = []
    total = 0
    with open(csv_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            prompt_text = row.get('Prompt', '').strip()
            if not prompt_text:
                continue
            cat = row.get('Category', 'General').strip() or 'General'
            if cat not in prompts_by_cat:
                prompts_by_cat[cat] = []
                categories_order.append(cat)
            prompts_by_cat[cat].append({
                'title': row.get('Type', '').strip() or f'Prompt {len(prompts_by_cat[cat]) + 1}',
                'prompt': prompt_text,
                'tags': row.get('Tags', '').strip(),
            })
            total += 1
    return prompts_by_cat, categories_order, total

def generate_html(csv_path, output_html, title, subtitle):
    prompts_by_cat, categories_order, total = parse_csv(csv_path)
    data = {
        'title': title, 'subtitle': subtitle, 'total': total,
        'generated': datetime.now().strftime('%B %d, %Y'),
        'categories': [{'name': cat, 'slug': slugify(cat), 'count': len(prompts_by_cat[cat]), 'prompts': prompts_by_cat[cat]} for cat in categories_order]
    }
    json_data = json.dumps(data, ensure_ascii=False)
    html = build_html(json_data, title, subtitle, total)
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html)
    return total

def generate_pdf(csv_path, output_pdf, title, subtitle):
    import site
    site.addsitedir(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
    from fpdf import FPDF
    FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
    prompts_by_cat, categories_order, total = parse_csv(csv_path)

    class PromptPDF(FPDF):
        def header(self):
            self.set_font('AR', 'B', 9)
            self.set_text_color(150, 150, 150)
            self.cell(0, 6, 'Content_Master', new_x='LMARGIN', new_y='NEXT', align='R')
            self.line(20, self.get_y(), 190, self.get_y())
            self.ln(3)
        def footer(self):
            self.set_y(-15)
            self.set_font('AR', '', 8)
            self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', new_x='RIGHT', new_y='TOP', align='C')

    pdf = PromptPDF()
    pdf.alias_nb_pages()
    pdf.add_font('AR', '', FONT_PATH)
    pdf.add_font('AR', 'B', FONT_PATH)
    pdf.add_font('AR', 'I', FONT_PATH)

    pdf.add_page()
    pdf.set_y(50)
    pdf.set_font('AR', 'B', 24)
    pdf.multi_cell(0, 12, title, align='C')
    pdf.ln(4)
    pdf.set_font('AR', '', 13)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 7, subtitle, align='C')
    pdf.ln(6)
    pdf.set_font('AR', '', 10)
    pdf.cell(0, 6, f'{total} prompts | {len(categories_order)} categories', new_x='LMARGIN', new_y='NEXT', align='C')
    pdf.cell(0, 6, 'gpframes.com', new_x='LMARGIN', new_y='NEXT', align='C')

    pdf.add_page()
    pdf.set_font('AR', 'B', 16)
    pdf.cell(0, 10, 'What Is Inside', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(3)
    pdf.set_font('AR', '', 10)
    for i, cat in enumerate(categories_order, 1):
        pdf.cell(0, 6, f'{i}. {cat}  ({len(prompts_by_cat[cat])} prompts)', new_x='LMARGIN', new_y='NEXT')

    for cat in categories_order:
        pdf.add_page()
        pdf.set_font('AR', 'B', 14)
        pdf.cell(0, 10, cat, new_x='LMARGIN', new_y='NEXT')
        pdf.line(20, pdf.get_y(), 80, pdf.get_y())
        pdf.ln(5)
        for j, item in enumerate(prompts_by_cat[cat], 1):
            if pdf.get_y() > 255:
                pdf.add_page()
            pdf.set_font('AR', 'B', 9)
            pdf.cell(0, 5, f'{j}. {item["title"]}', new_x='LMARGIN', new_y='NEXT')
            pdf.set_font('AR', '', 9)
            pdf.set_text_color(80, 80, 80)
            pdf.multi_cell(0, 4.5, item['prompt'])
            pdf.set_text_color(0, 0, 0)
            if item['tags']:
                pdf.set_font('AR', 'I', 8)
                pdf.cell(0, 4, f'Tags: {item["tags"]}', new_x='LMARGIN', new_y='NEXT')
            pdf.line(25, pdf.get_y(), 185, pdf.get_y())
            pdf.ln(3)

    pdf.output(output_pdf)
    return total

def build_html(json_data, title, subtitle, total):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Content_Master</title>
<style>
:root{{--bg:#0f1117;--bg-card:#1a1d27;--bg-card-hover:#222633;--bg-sidebar:#141720;--border:#2a2d3a;--text:#e4e6f0;--text-muted:#8b8fa3;--text-dim:#5a5e72;--accent:#6366f1;--accent-hover:#818cf8;--accent-glow:rgba(99,102,241,0.15);--success:#34d399;--tag-bg:rgba(99,102,241,0.12);--tag-text:#a5b4fc;--font:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.6}}
.header{{background:var(--bg-sidebar);border-bottom:1px solid var(--border);padding:16px 24px;position:sticky;top:0;z-index:100;display:flex;align-items:center;justify-content:space-between}}
.header h1{{font-size:1.25rem;font-weight:700}}
.header p{{font-size:.8rem;color:var(--text-muted)}}
.badge{{background:var(--accent-glow);color:var(--accent-hover);padding:4px 12px;border-radius:20px;font-size:.75rem;font-weight:600}}
.layout{{display:flex;min-height:calc(100vh - 65px)}}
.sidebar{{width:260px;min-width:260px;background:var(--bg-sidebar);border-right:1px solid var(--border);padding:20px 12px;position:sticky;top:65px;height:calc(100vh - 65px);overflow-y:auto}}
.sidebar h3{{font-size:.7rem;text-transform:uppercase;letter-spacing:.1em;color:var(--text-dim);padding:0 12px;margin-bottom:12px}}
.cat-btn{{display:flex;justify-content:space-between;width:100%;padding:8px 12px;margin-bottom:2px;border:none;border-radius:8px;background:transparent;color:var(--text-muted);font-size:.82rem;cursor:pointer;text-align:left;font-family:var(--font)}}
.cat-btn:hover{{background:rgba(99,102,241,.08);color:var(--text)}}
.cat-btn.active{{background:var(--accent-glow);color:var(--accent-hover);font-weight:600}}
.cat-btn .count{{background:rgba(255,255,255,.06);padding:1px 7px;border-radius:10px;font-size:.7rem}}
.main{{flex:1;padding:28px 32px;max-width:900px}}
.search-box{{width:100%;padding:10px 14px;background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:8px;color:var(--text);font-size:.85rem;margin-bottom:16px;outline:none;font-family:var(--font)}}
.search-box:focus{{border-color:var(--accent)}}
.results-info{{font-size:.85rem;color:var(--text-muted);margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid var(--border)}}
.prompt-card{{background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:14px}}
.prompt-card:hover{{border-color:rgba(99,102,241,.3);background:var(--bg-card-hover)}}
.prompt-header{{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;margin-bottom:12px}}
.prompt-cat{{display:inline-block;font-size:.65rem;text-transform:uppercase;letter-spacing:.08em;font-weight:700;color:var(--accent-hover);background:var(--tag-bg);padding:3px 10px;border-radius:6px;margin-bottom:8px}}
.prompt-title{{font-size:.95rem;font-weight:600;flex:1}}
.copy-btn{{background:var(--accent);color:#fff;border:none;padding:7px 16px;border-radius:8px;font-size:.78rem;font-weight:600;cursor:pointer;white-space:nowrap;display:flex;align-items:center;gap:6px;flex-shrink:0;font-family:var(--font)}}
.copy-btn:hover{{background:var(--accent-hover)}}
.copy-btn.copied{{background:var(--success)}}
.prompt-text{{font-size:.85rem;color:var(--text-muted);line-height:1.7;white-space:pre-wrap;background:rgba(0,0,0,.2);padding:14px;border-radius:8px;max-height:200px;overflow-y:auto}}
.prompt-tags{{margin-top:10px;font-size:.72rem;color:var(--text-dim);font-style:italic}}
.prompt-tags span{{color:var(--tag-text)}}
.empty-state{{text-align:center;padding:60px 20px;color:var(--text-dim)}}
.footer{{text-align:center;padding:24px;color:var(--text-dim);font-size:.75rem;border-top:1px solid var(--border);margin-top:40px}}
.footer a{{color:var(--accent-hover);text-decoration:none}}
@media(max-width:768px){{.sidebar{{display:none}}.main{{padding:16px}}}}
</style>
</head>
<body>
<div class="header">
  <div><h1>{title}</h1><p>{subtitle}</p></div>
  <span class="badge">{total} prompts</span>
</div>
<div class="layout">
  <aside class="sidebar"><h3>Categories</h3><div id="category-list"></div></aside>
  <main class="main">
    <input type="text" class="search-box" id="search" placeholder="Search prompts...">
    <div class="results-info" id="results-info"></div>
    <div id="prompts-container"></div>
    <div class="footer"><p>Content_Master by <a href="https://gpframes.com">Gabriel Paiva</a></p></div>
  </main>
</div>
<script>
const DATA={json_data};
let activeCat='all',sq='';
function rc(){{const c=document.getElementById('category-list');let h=`<button class="cat-btn active" onclick="fc('all',this)"><span>All Categories</span><span class="count">${{DATA.total}}</span></button>`;DATA.categories.forEach(x=>{{h+=`<button class="cat-btn" onclick="fc('${{x.slug}}',this)"><span>${{x.name}}</span><span class="count">${{x.count}}</span></button>`}});c.innerHTML=h;}}
function fc(s,b){{activeCat=s;document.querySelectorAll('.cat-btn').forEach(x=>x.classList.remove('active'));if(b)b.classList.add('active');rp();}}
function esc(t){{const d=document.createElement('div');d.textContent=t;return d.innerHTML}}
function rp(){{
  const c=document.getElementById('prompts-container'),info=document.getElementById('results-info');
  let h='',n=0;
  DATA.categories.forEach(cat=>{{if(activeCat!=='all'&&cat.slug!==activeCat)return;cat.prompts.forEach((p,i)=>{{
    if(sq){{const q=sq.toLowerCase();if(!p.prompt.toLowerCase().includes(q)&&!p.title.toLowerCase().includes(q)&&!cat.name.toLowerCase().includes(q))return;}}
    n++;const pid=`p${{cat.slug}}${{i}}`;
    h+=`<div class="prompt-card"><div class="prompt-header"><div><span class="prompt-cat">${{cat.name}}</span><div class="prompt-title">${{p.title}}</div></div><button class="copy-btn" onclick="cp(this,'${{pid}}')">Copy</button></div><div class="prompt-text" id="${{pid}}">${{esc(p.prompt)}}</div>${{p.tags?'<div class="prompt-tags">Tags: '+esc(p.tags)+'</div>':''}}</div>`;
  }});}});
  if(!n)h='<div class="empty-state"><h2>No prompts found</h2></div>';
  info.textContent=`Showing ${{n}} of ${{DATA.total}} prompts`;c.innerHTML=h;
}}
function cp(btn,id){{navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>{{btn.classList.add('copied');btn.textContent='Copied!';setTimeout(()=>{{btn.classList.remove('copied');btn.textContent='Copy';}},2000);}})}}
document.getElementById('search').addEventListener('input',e=>{{sq=e.target.value;rp();}});rc();rp();
</script>
</body>
</html>'''

if __name__ == '__main__':
    if len(sys.argv) < 6:
        print("Usage: python3 generate-products.py <csv> <out_html> <out_pdf> <title> <subtitle>")
        sys.exit(1)
    t = generate_html(sys.argv[1], sys.argv[2], sys.argv[4], sys.argv[5])
    t = generate_pdf(sys.argv[1], sys.argv[3], sys.argv[4], sys.argv[5])
    print(f"Done: {t} prompts -> {sys.argv[2]} + {sys.argv[3]}")
