#!/usr/bin/env python3
"""Build the standalone design-system viewer and tokens.css.

    python3 design-system-2/scripts/build_preview.py

Writes, next to tokens.json:
  tokens.css    CSS custom properties for both themes + one class per type style
  tailwind/theme.css  the same tokens for Tailwind CSS v4 and shadcn/ui
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

# ---------- tailwind/theme.css (Tailwind CSS v4 + shadcn/ui) ----------
NEXT_FONT_VARS = {  # family key -> CSS variable set by tailwind/fonts.ts (next/font)
    "serif": "--font-newsreader", "sans": "--font-atkinson", "mono": "--font-plex-mono",
    "receipt": "--font-share-tech-mono", "doc": "--font-arimo", "hand": "--font-caveat",
}

# shadcn/ui role -> Red Thread token. Destructive is ink, not red: the thread is the
# only red, and a wrong answer is said in words (README section 3).
SHADCN = [
    ("background", "ground"), ("foreground", "ink"),
    ("card", "surface"), ("card-foreground", "ink"),
    ("popover", "surface-raised"), ("popover-foreground", "ink"),
    ("primary", "thread"), ("primary-foreground", "on-thread"),
    ("secondary", "surface-raised"), ("secondary-foreground", "ink"),
    ("muted", "surface"), ("muted-foreground", "ink-muted"),
    ("accent", "surface-raised"), ("accent-foreground", "ink"),
    ("destructive", "ink"),
    ("border", "line"), ("input", "line-strong"), ("ring", "focus"),
    ("chart-1", "thread"), ("chart-2", "brass"), ("chart-3", "solved"), ("chart-4", "ink-muted"), ("chart-5", "manila"),
    ("sidebar", "surface"), ("sidebar-foreground", "ink"),
    ("sidebar-primary", "thread"), ("sidebar-primary-foreground", "on-thread"),
    ("sidebar-accent", "surface-raised"), ("sidebar-accent-foreground", "ink"),
    ("sidebar-border", "line"), ("sidebar-ring", "focus"),
]


def build_tailwind_css():
    themes = [t["id"] for t in tokens["color"]["themes"]]
    first = themes[0]
    color_tokens = tokens["color"]["tokens"]
    shadows = tokens.get("shadow", {}).get("tokens", [])

    def val(v, th):
        return v if isinstance(v, str) else v.get(th, v.get(first))

    def ref(v):
        m = re.fullmatch(r"\{([^}]+)\}", v)
        return f"var(--{m.group(1)})" if m else v

    def font_stack(key, stack):
        var = NEXT_FONT_VARS.get(key)
        if not var:
            return stack
        head, _, rest = stack.partition(",")
        return f"var({var}, {head.strip()})" + ("," + rest if rest else "")

    o = [f"/* {tokens['name']} design system v2 for Tailwind CSS v4 and shadcn/ui.",
         "   Generated from tokens.json by scripts/build_preview.py. Do not edit by hand.",
         "   See tailwind/README.md. In app/globals.css, after @import \"tailwindcss\": */",
         "", "/* Themes: <html data-theme=\"night\"> (default) or \"paper\". shadcn's dark: classes follow Night. */",
         '@custom-variant dark (&:where([data-theme="night"], [data-theme="night"] *));',
         '@custom-variant paper (&:where([data-theme="paper"], [data-theme="paper"] *));', ""]

    for i, th in enumerate(themes):
        sel = f':root, [data-theme="{th}"]' if i == 0 else f'[data-theme="{th}"]'
        o.append(sel + " {")
        o.append(f"  color-scheme: {'dark' if th == 'night' else 'light'};")
        for t in color_tokens:
            v = t["value"]
            if i > 0 and (isinstance(v, str) or th not in v):
                continue
            o.append(f"  --{t['name']}: {ref(val(v, th))};")
        for t in shadows:
            v = t["value"]
            if i > 0 and (isinstance(v, str) or th not in v):
                continue
            o.append(f"  --rt-{t['name']}: {val(v, th)};")
        if i == 0:
            o.append("")
            o.append("  /* shadcn/ui roles */")
            for role, tok in SHADCN:
                o.append(f"  --{role}: var(--{tok});")
            o.append("  --radius: 10px;")
        o.append("}")
        o.append("")

    o.append(":root {")
    o.append("  /* Names the component CSS (components/bundle.css) reads */")
    for fam in ("spacing", "stroke"):
        for t in tokens.get(fam, {}).get("tokens", []):
            o.append(f"  --{t['name']}: {t['value']};")
    for t in shadows:
        o.append(f"  --{t['name']}: var(--rt-{t['name']});")
    o.append("}")
    o.append("")

    o.append("@theme static {")
    o.append("  /* font-serif (titles), font-sans (instructions), font-mono (labels), then evidence faces */")
    for key, stack in tokens["type"]["families"].items():
        o.append(f"  --font-{key}: {font_stack(key, stack)};")
    o.append("")
    o.append("  /* rounded-evidence (0) · rounded-tag · rounded-control · rounded-note · rounded-device · rounded-pill */")
    for t in tokens["radius"]["tokens"]:
        o.append(f"  --{t['name']}: {t['value']};")
    o.append("  /* shadcn's scale, pinned to the system's radii: sm = tag (badges, checkboxes),")
    o.append("     md = control (buttons, inputs, selects), lg and xl = note (dialogs, cards, sheets) */")
    o.append("  --radius-sm: 6px;\n  --radius-md: 10px;\n  --radius-lg: 16px;\n  --radius-xl: 16px;")
    o.append("")
    o.append("  /* The game is flat (README section 2). shadcn puts shadow-xs on inputs and buttons and")
    o.append("     shadow-sm on cards; both become a transparent shadow (not `none`, which would break the focus-ring list). md and up stay for menus and dialogs, which float. */")
    o.append("  --shadow-2xs: 0 0 #0000;\n  --shadow-xs: 0 0 #0000;\n  --shadow-sm: 0 0 #0000;")
    o.append("")
    o.append("  /* text-display-xl, text-title, text-label ... (size, leading, tracking, weight).")
    o.append("     A style that shares a colour's name (evidence) is left out: use type-evidence. */")
    colour_names = {t["name"] for t in color_tokens}
    for g in tokens["type"]["groups"]:
        for st in g["styles"]:
            n = st["name"]
            if n in colour_names:
                continue
            o.append(f"  --text-{n}: {st['fontSize']};")
            o.append(f"  --text-{n}--line-height: {st['lineHeight']};")
            if "letterSpacing" in st:
                o.append(f"  --text-{n}--letter-spacing: {st['letterSpacing']};")
            o.append(f"  --text-{n}--font-weight: {st['fontWeight']};")
    o.append("}")
    o.append("")

    o.append("@theme inline {")
    o.append("  /* bg-ground, text-ink, bg-note, text-evidence-ink, border-manila-line ... */")
    for t in color_tokens:
        o.append(f"  --color-{t['name']}: var(--{t['name']});")
    o.append("")
    o.append("  /* shadcn/ui: bg-background, text-primary-foreground, border-border ... */")
    for role, _ in SHADCN:
        o.append(f"  --color-{role}: var(--{role});")
    o.append("")
    o.append("  /* shadow-object: evidence only. The game is flat. */")
    o.append("  --shadow-object: var(--rt-shadow-object);")
    o.append("}")
    o.append("")

    o.append("/* type-display-xl, type-title, type-label ...: the whole style, family included */")
    for g in tokens["type"]["groups"]:
        for st in g["styles"]:
            fam = st.get("family", g["family"])
            props = [f"font-family: var(--font-{fam})", f"font-size: {st['fontSize']}",
                     f"line-height: {st['lineHeight']}", f"font-weight: {st['fontWeight']}"]
            if "letterSpacing" in st:
                props.append(f"letter-spacing: {st['letterSpacing']}")
            if "fontStyle" in st:
                props.append(f"font-style: {st['fontStyle']}")
            if st["name"] == "label":
                props.append("text-transform: uppercase")
            if st["name"] in ("evidence", "doc-body", "receipt"):
                props.append("font-variant-numeric: tabular-nums")
            o.append(f"@utility type-{st['name']} {{ {'; '.join(props)}; }}")
    o.append("")
    o.append("/* The two layers (README section 2) as single utilities */")
    o.append("@utility surface-note { background-color: var(--note); color: var(--note-ink); border: 1px solid var(--note-line); border-radius: var(--radius-note); box-shadow: none; }")
    o.append("@utility surface-evidence { background-color: var(--evidence); color: var(--evidence-ink); border-radius: var(--radius-evidence); box-shadow: var(--rt-shadow-object); }")
    o.append("@utility surface-manila { background-color: var(--manila); color: var(--manila-ink); border-radius: var(--radius-tag); }")
    o.append("@utility drop-object { filter: var(--rt-shadow-object-drop); }")
    o.append("")
    o.append("@layer base {")
    o.append("  * { border-color: var(--border); outline-color: color-mix(in oklab, var(--ring) 50%, transparent); }")
    o.append("  html { -webkit-text-size-adjust: 100%; }")
    o.append("  body { background-color: var(--background); color: var(--foreground); font-family: var(--font-sans); -webkit-font-smoothing: antialiased; }")
    o.append("  ::selection { background-color: var(--thread); color: var(--on-thread); }")
    o.append("  input, textarea { caret-color: var(--thread-text); }")
    o.append("  :focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }")
    o.append("  .tabular, table, time { font-variant-numeric: tabular-nums; }")
    o.append("}")
    return "\n".join(o) + "\n"


(DS / "tailwind").mkdir(exist_ok=True)
(DS / "tailwind" / "theme.css").write_text(build_tailwind_css(), encoding="utf-8")

# ---------- preview.html ----------
bundle_css = (DS / "components" / "bundle.css").read_text(encoding="utf-8")
bundle_js = (DS / "components" / "bundle.js").read_text(encoding="utf-8")
react = (DS / "vendor" / "react.production.min.js").read_text(encoding="utf-8")
react_dom = (DS / "vendor" / "react-dom.production.min.js").read_text(encoding="utf-8")

# Card order: cover, the Colours and Type references, then the bundle's component order.
header = json.loads(re.search(r"@ds-bundle: (\{.*?\}) \*/", bundle_js).group(1))
order = ["Cover", "Colours", "Type"] + [c["name"] for c in header["components"]]
# Then any other card folder (worked examples such as Case001), alphabetically.
order += sorted(d.name for d in (DS / "components").iterdir() if d.is_dir() and d.name not in order)
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
        "title": attrs.get("title", name),
        "group": attrs.get("group", ""),
        "subtitle": attrs.get("subtitle", ""),
        "height": int(attrs.get("height", 160)),
        "summary": summary,
        "doc": src[m.end():] if m else src,
    })


# Google Fonts for the standalone preview only. The app self-hosts them (tailwind/fonts.ts).
FONTS_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400'
    '&family=Atkinson+Hyperlegible+Next:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500'
    '&family=Share+Tech+Mono&family=Arimo:wght@400;700&family=Caveat:wght@500;600&display=swap">'
)


def js_str(s):
    # JSON string, safe inside an inline <script>.
    return json.dumps(s).replace("</", "<\\/").replace("<!--", "<\\!--")


shared_head = (
    FONTS_LINK
    + "<style>" + tokens_css + "</style>"
    "<style>" + bundle_css + "</style>"
    "<script>" + react + "</script>"
    "<script>" + react_dom + "</script>"
    "<script>" + bundle_js + "</script>"
    "<script>"
    "function rtReport(){var h=document.body?Math.ceil(document.body.getBoundingClientRect().height):0;"
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
<title>{html.escape(tokens['name'])}: design system preview</title>
<!-- Generated by design-system-2/scripts/build_preview.py. Do not edit by hand. -->
{FONTS_LINK}
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
.ds-toggle {{ display: inline-flex; border: 1px solid var(--line-strong); border-radius: var(--radius-tag); overflow: hidden; }}
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
.ds-frame {{ display: block; width: 100%; border: 1px solid var(--line); border-radius: var(--radius-tag); background: var(--ground); }}
.ds-cover .ds-frame {{ aspect-ratio: 960 / 320; height: auto; }}
@media (max-width: 600px) {{ .ds-top {{ position: static; padding: var(--space-3) var(--space-4); flex-wrap: wrap; }} .ds-nav {{ padding: var(--space-3) var(--space-4); gap: var(--space-2) var(--space-4); }} .ds-main {{ padding: var(--space-4); }} .ds-card h2 {{ font-size: 30px; }} }}
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
    var h2 = document.createElement('h2'); h2.textContent = c.title || c.name;
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
print(f"wrote {DS / 'tailwind' / 'theme.css'}")
print(f"wrote {DS / 'preview.html'} ({len(page) // 1024} KB, {len(cards)} cards)")
