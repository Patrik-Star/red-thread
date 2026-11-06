#!/usr/bin/env python3
"""Build the standalone design-system viewer and tokens.css.

    python3 design-system-2/scripts/build_preview.py

Writes, next to tokens.json:
  tokens.css    CSS custom properties for both themes + one class per type style
  preview.html  ONE self-contained page (tokens, styles, React, components and
                every components/*/preview.html inlined). Double-click it to open
                in a browser. Needs internet only for the Google Fonts.

Standard library only. Rerun after changing tokens.json, components/ or vendor/.
"""
import html
import json
import re
from pathlib import Path

DS = Path(__file__).resolve().parent.parent
tokens = json.loads((DS / "tokens.json").read_text(encoding="utf-8"))


def kebab(s):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", s).lower()


# ---------- tokens.css ----------
def build_tokens_css():
    themes = [t["id"] for t in tokens["color"]["themes"]]
    first = themes[0]

    def val(v, th):
        if isinstance(v, str):
            return v
        return v.get(th, v.get(first))

    def ref(v):  # "{alias}" -> var(--alias)
        m = re.fullmatch(r"\{([^}]+)\}", v)
        return f"var(--{m.group(1)})" if m else v

    per_theme = [("color", t) for t in tokens["color"]["tokens"]]
    per_theme += [("shadow", t) for t in tokens.get("shadow", {}).get("tokens", [])]

    out = [f"/* {tokens['name']} — generated from tokens.json by scripts/build_preview.py. Do not edit by hand. */", ""]
    for i, th in enumerate(themes):
        sel = f':root, [data-theme="{th}"]' if i == 0 else f'[data-theme="{th}"]'
        out.append(sel + " {")
        for _, t in per_theme:
            v = t["value"]
            if i > 0 and (isinstance(v, str) or th not in v):
                continue  # inherits the first theme
            out.append(f"  --{t['name']}: {ref(val(v, th))};")
        out.append("}")
        out.append("")

    out.append(":root {")
    for fam, block in tokens.items():
        if fam in ("name", "version", "color", "type", "shadow") or not isinstance(block, dict):
            continue
        for t in block.get("tokens", []):
            out.append(f"  --{t['name']}: {t['value']};")
    for key, stack in tokens["type"]["families"].items():
        out.append(f"  --font-{key}: {stack};")
    out.append("}")
    out.append("")

    for g in tokens["type"]["groups"]:
        for s in g["styles"]:
            fam = s.get("family", g["family"])
            props = [f"font-family: var(--font-{fam})"]
            for k in ("fontSize", "lineHeight", "fontWeight", "letterSpacing", "fontStyle"):
                if k in s:
                    props.append(f"{kebab(k)}: {s[k]}")
            out.append(f".{s['name']} {{ {'; '.join(props)}; }}")
    return "\n".join(out) + "\n", themes


tokens_css, themes = build_tokens_css()
(DS / "tokens.css").write_text(tokens_css, encoding="utf-8")

# ---------- preview.html ----------
bundle_css = (DS / "components" / "bundle.css").read_text(encoding="utf-8")
bundle_js = (DS / "components" / "bundle.js").read_text(encoding="utf-8")
react = (DS / "vendor" / "react.production.min.js").read_text(encoding="utf-8")
react_dom = (DS / "vendor" / "react-dom.production.min.js").read_text(encoding="utf-8")

# Card order: cover, the Colours reference, then the bundle's component order.
header = json.loads(re.search(r"@ds-bundle: (\{.*?\}) \*/", bundle_js).group(1))
order = ["Cover", "Colours"] + [c["name"] for c in header["components"]]
cards = []
for name in order:
    p = DS / "components" / name / "preview.html"
    if not p.exists():
        continue
    src = p.read_text(encoding="utf-8")
    m = re.match(r"<!--\s*@dsCard(.*?)-->\s*", src)
    attrs = {k: a or b for k, a, b in re.findall(r'(\w+)=(?:"([^"]*)"|(\S+))', m.group(1))} if m else {}
    readme = DS / "components" / name / "README.md"
    summary = ""
    if readme.exists():
        body = [l for l in readme.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
        summary = re.sub(r"[`*]", "", body[0]) if body else ""
    cards.append({
        "name": name,
        "group": attrs.get("group", ""),
        "subtitle": attrs.get("subtitle", ""),
        "height": int(attrs.get("height", 160)),
        "summary": summary,
        "doc": src[m.end():] if m else src,
    })


def js_str(s):
    # JSON string, safe inside an inline <script>.
    return json.dumps(s).replace("</", "<\\/").replace("<!--", "<\\!--")


shared_head = (
    "<style>" + tokens_css + "</style>"
    "<style>" + bundle_css + "</style>"
    "<script>" + react + "</script>"
    "<script>" + react_dom + "</script>"
    "<script>" + bundle_js + "</script>"
    "<script>"
    "function rtReport(){var h=Math.max(document.documentElement.scrollHeight,document.body?document.body.scrollHeight:0);"
    "parent.postMessage({rtCard:window.name,height:h},'*');}"
    "addEventListener('load',function(){rtReport();setTimeout(rtReport,300);setTimeout(rtReport,1200);});"
    "addEventListener('resize',rtReport);"
    "</script>"
)

page = f"""<!doctype html>
<html lang="en" data-theme="{themes[0]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(tokens['name'])} — design system preview</title>
<!-- Generated by design-system-2/scripts/build_preview.py. Do not edit by hand. -->
<style>
{bundle_css}
</style>
<style>
{tokens_css}
</style>
<style>
.ds-top {{ position: sticky; top: 0; z-index: 2; display: flex; align-items: center; justify-content: space-between; gap: var(--space-4); padding: var(--space-4) var(--space-8); background: var(--ground); border-bottom: 1px solid var(--line); }}
.ds-title {{ font: 400 28px/1 var(--font-serif); }}
.ds-title small {{ font: 500 11px/16px var(--font-mono); letter-spacing: .14em; text-transform: uppercase; color: var(--ink-muted); margin-left: var(--space-3); }}
.ds-toggle {{ display: inline-flex; border: 1px solid var(--line-strong); border-radius: var(--radius-sm); overflow: hidden; }}
.ds-toggle button {{ font: 500 13px/1 var(--font-sans); padding: 10px 16px; background: transparent; color: var(--ink); border: 0; cursor: pointer; min-height: 40px; }}
.ds-toggle button[aria-pressed="true"] {{ background: var(--ink); color: var(--ground); }}
.ds-toggle button:focus-visible {{ outline: 2px solid var(--focus); outline-offset: -2px; }}
.ds-nav {{ display: flex; flex-wrap: wrap; gap: var(--space-4); padding: var(--space-3) var(--space-8); border-bottom: 1px solid var(--line); }}
.ds-nav a {{ font: 500 11px/16px var(--font-mono); letter-spacing: .14em; text-transform: uppercase; color: var(--ink-muted); text-decoration: none; }}
.ds-nav a:hover {{ color: var(--ink); }}
.ds-main {{ max-width: 1040px; margin: 0 auto; padding: var(--space-8); }}
.ds-card {{ margin-bottom: var(--space-12); scroll-margin-top: 96px; }}
.ds-card header {{ display: flex; align-items: baseline; gap: var(--space-3); margin-bottom: var(--space-2); }}
.ds-card h2 {{ margin: 0; font: 400 36px/1.1 var(--font-serif); }}
.ds-card .ds-group {{ font: 500 11px/16px var(--font-mono); letter-spacing: .14em; text-transform: uppercase; color: var(--brass); }}
.ds-card p {{ margin: 0 0 var(--space-4); max-width: 680px; color: var(--ink-muted); font-size: 15px; line-height: 23px; }}
.ds-frame {{ display: block; width: 100%; border: 1px solid var(--line); border-radius: var(--radius-sm); background: var(--ground); }}
.ds-cover .ds-frame {{ aspect-ratio: 960 / 320; height: auto; }}
</style>
</head>
<body>
<div class="ds-top">
  <div class="ds-title">{html.escape(tokens['name'])}<small>Design system</small></div>
  <div class="ds-toggle" role="group" aria-label="Theme">
    {''.join(f'<button type="button" data-theme-btn="{t["id"]}" aria-pressed="{str(i == 0).lower()}">{html.escape(t["name"])}</button>' for i, t in enumerate(tokens["color"]["themes"]))}
  </div>
</div>
<nav class="ds-nav" id="nav"></nav>
<main class="ds-main" id="cards"></main>
<script>
(function () {{
  var SHARED = {js_str(shared_head)};
  var CARDS = {js_str(json.dumps(cards))};
  CARDS = JSON.parse(CARDS);
  var theme = {js_str(themes[0])};
  var main = document.getElementById('cards'), nav = document.getElementById('nav');
  var frames = [];

  function docFor(c) {{
    var d = c.doc.replace(/<html([^>]*)>/i, function (m, a) {{ return '<html' + a.replace(/\\sdata-theme="[^"]*"/, '') + ' data-theme="' + theme + '">'; }});
    if (/<head[^>]*>/i.test(d)) d = d.replace(/<head([^>]*)>/i, '<head$1>' + SHARED);
    else d = SHARED + d;
    return d;
  }}

  CARDS.forEach(function (c) {{
    var sec = document.createElement('section');
    sec.className = 'ds-card' + (c.name === 'Cover' ? ' ds-cover' : '');
    sec.id = c.name;
    var hd = document.createElement('header');
    var h2 = document.createElement('h2'); h2.textContent = c.name === 'Cover' ? 'Cover' : c.name;
    hd.appendChild(h2);
    if (c.group) {{ var g = document.createElement('span'); g.className = 'ds-group'; g.textContent = c.group; hd.appendChild(g); }}
    sec.appendChild(hd);
    if (c.subtitle || c.summary) {{ var p = document.createElement('p'); p.textContent = c.subtitle || c.summary; sec.appendChild(p); }}
    var f = document.createElement('iframe');
    f.className = 'ds-frame'; f.name = c.name; f.title = c.name + ' preview';
    if (c.name === 'Cover') {{ f.style.width = '960px'; f.style.maxWidth = '100%'; f.style.height = c.height + 'px'; f.setAttribute('scrolling', 'no'); }}
    else f.style.height = c.height + 'px';
    f.srcdoc = docFor(c);
    sec.appendChild(f);
    main.appendChild(sec);
    frames.push({{ el: f, card: c }});
    var a = document.createElement('a'); a.href = '#' + c.name; a.textContent = c.name; nav.appendChild(a);
  }});

  addEventListener('message', function (e) {{
    var d = e.data; if (!d || !d.rtCard) return;
    frames.forEach(function (fr) {{
      if (fr.card.name === d.rtCard && fr.card.name !== 'Cover') fr.el.style.height = Math.max(d.height, 60) + 'px';
    }});
  }});

  function setTheme(t) {{
    theme = t;
    document.documentElement.setAttribute('data-theme', t);
    document.querySelectorAll('[data-theme-btn]').forEach(function (b) {{ b.setAttribute('aria-pressed', String(b.getAttribute('data-theme-btn') === t)); }});
    frames.forEach(function (fr) {{ fr.el.srcdoc = docFor(fr.card); }});
  }}
  document.querySelectorAll('[data-theme-btn]').forEach(function (b) {{
    b.addEventListener('click', function () {{ setTheme(b.getAttribute('data-theme-btn')); }});
  }});
}})();
</script>
</body>
</html>
"""
(DS / "preview.html").write_text(page, encoding="utf-8")
print(f"wrote {DS / 'tokens.css'}")
print(f"wrote {DS / 'preview.html'} ({len(page) // 1024} KB, {len(cards)} cards)")
