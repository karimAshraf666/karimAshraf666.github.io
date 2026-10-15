"""Render existing token and component sources into a small human reference."""
from pathlib import Path
import html,re
from portfolio_shell import apply_shell
ROOT=Path(__file__).resolve().parents[1]
esc=html.escape
token_text=(ROOT/'design/tokens/discovery.css').read_text(encoding='utf-8')
tokens=re.findall(r'(--wb-[\w-]+):\s*([^;]+);',token_text)
rows=''.join(f'<tr><td><code>{esc(name)}</code></td><td><code>{esc(value.strip())}</code></td></tr>' for name,value in tokens)
components=[]
for file in sorted((ROOT/'design/components').glob('*.crd.md')):
    value=file.read_text(encoding='utf-8')
    title=re.search(r'^# (.+)',value,re.M)[1]
    requirements=re.findall(r'^- ([A-Z]\d+: .+)',value,re.M)
    components.append(f'<article><h3>{esc(title)}</h3><ul>'+''.join(f'<li>{esc(item)}</li>' for item in requirements)+f'</ul><a href="{file.relative_to(ROOT).as_posix()}">Read the component source</a></article>')
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><title>Portfolio design reference | Karim Ashraf</title><meta name="robots" content="noindex"/><link rel="stylesheet" href="styles.css?v=20261006"/></head><body class="writing-page" id="top"><a class="skip-link" href="#reference">Skip to design reference</a><header class="site-header"></header><main id="reference" class="section-inner system-reference"><p class="eyebrow">Portfolio design reference</p><h1>One portfolio identity</h1><p>This page is generated from the token and component sources. It documents the navigation and discovery extension to the current portfolio.</p><p><a href="design/DESIGN.md">Design context</a> / <a href="design/BRIEF.md">Brief and reference lock</a> / <a href="design/ruled-out.md">Ruled-out directions</a></p><section><h2>Navigation states</h2><p>The Workbench link uses the cobalt action role. Hover darkens it, keyboard focus adds an outer ring, and mobile navigation keeps a Workbench shortcut visible.</p><div class="button-row"><a class="button" href="workbench.html">Open workbench</a><a class="button secondary" href="workbench.html#ai-skills">Browse AI skills</a></div></section><section><h2>Discovery tokens</h2><p>Color roles inherit from redesign.css. Font: Manrope with system-ui fallback. The extension uses an 8px spacing rhythm with a 4px substep, and the existing small-radius and rounded-button shapes.</p><table><thead><tr><th>Token</th><th>Value or role</th></tr></thead><tbody>{rows}</tbody></table></section><section><h2>Component behavior</h2>{''.join(components)}</section><section><h2>Copy and evidence</h2><p>Keep labels literal and short. Preserve role titles, dates, metric definitions and attribution. Avoid recency badges, unverified adoption claims and generic marketing promises.</p><p><a href="docs/EVIDENCE-INVENTORY.md">Evidence inventory</a></p></section></main><footer class="site-footer"><div class="footer-inner"><a href="index.html">Portfolio home</a></div></footer><script src="script.js?v=20261015c"></script></body></html>'''
(ROOT/'design-system.html').write_text(apply_shell(page,'design-system.html'),encoding='utf-8')
print(f'Generated design reference from {len(tokens)} tokens and {len(components)} component sources.')
