"""Build directory navigation from the existing resource cards, with no duplicated catalog."""
import html
import re
from collections import Counter

def build_navigation(page):
    counts = Counter(html.unescape(t) for t in re.findall(r'data-type="([^"]+)"', page))
    total = sum(counts.values())
    prompt_count = page.count('class="bench-prompt"')
    template_count = page.count('class="bench-template"')
    def category(route, label, count, extra=''):
        return f'<a href="#{route}" data-library-view="{route}" {extra}><span>{label}</span><span class="bench-nav-count" data-count="{route}">{count}</span></a>'
    sidebar = f'''<aside class="bench-sidebar" aria-label="Workbench navigation"><details id="workbench-navigation" open><summary>Browse workbench<span id="browse-current">All resources</span></summary><div class="bench-sidebar-body">
      <a class="bench-sidebar-title" href="#top">Design workbench</a>
      <nav aria-label="Resource categories"><p class="bench-nav-label">Resource library</p>
      {category('library','All resources',total,'aria-current="page"')}
      {category('ui-kits','Systems &amp; UI kits',counts['Systems & UI kits'])}
      {category('ux-patterns','UX patterns',counts['UX patterns'])}
      {category('plugins-tools','Plugins &amp; tools',counts['Plugins']+counts['Tools'])}
      {category('reading','Articles &amp; guides',counts['Articles & guidance'])}
      {category('saved','Saved resources',0)}
      <p class="bench-nav-label">AI for design</p>
      {category('ai-skills','AI skills',counts['AI skills'],'class="bench-ai-link"')}
      <a href="#ai-workflows" data-workbench-section="ai-workflows"><span>Reusable prompts</span><span class="bench-nav-count">{prompt_count}</span></a>
      </nav><nav aria-label="Team tools and templates"><p class="bench-nav-label">Use with a team</p>
      <a href="#tools" data-workbench-section="tools"><span>Practical tools</span><span class="bench-nav-count">3</span></a>
      <a href="#team-kit" data-workbench-section="team-kit"><span>Team templates</span><span class="bench-nav-count">{template_count}</span></a>
      <a href="#practices" data-workbench-section="practices"><span>Working practices</span></a></nav>
      <a class="bench-sidebar-download" href="resources/workbench/design-workbench-team-kit.zip" download>Download team kit <span aria-hidden="true">↓</span></a>
      </div></details></aside>'''
    hero = f'''<section class="bench-hero" aria-labelledby="bench-title"><p class="eyebrow">Karim Ashraf / Resources &amp; workflows</p><h1 id="bench-title">Design workbench</h1><p class="hero-deck">Patterns, tools and AI skills you can put to work. Find a reference, use a worksheet or take a workflow into your team.</p><div class="bench-start-links"><a href="#ai-skills" data-library-view="ai-skills">Browse {counts['AI skills']} AI skills <span aria-hidden="true">→</span></a><a href="#tools">Open practical tools <span aria-hidden="true">→</span></a><a href="resources/workbench/design-workbench-team-kit.zip" download>Download team kit <span aria-hidden="true">↓</span></a></div></section>'''
    page = re.sub(r'<section class="bench-hero".*?(?=<section class="bench-section" id="library")', lambda _: sidebar+'<div class="workbench-main">'+hero, page, count=1, flags=re.S)
    page = page.replace('<main>', '<main class="workbench-layout">', 1).replace('</main>', '</div></main>', 1)
    anchors = ''.join(f'<span class="bench-route-anchor" id="{r}"></span>' for r in ['ai-skills','ui-kits','ux-patterns','plugins-tools','reading','saved'])
    intro = f'''{anchors}<div class="bench-library-heading"><div><h2 id="library-title" tabindex="-1">All resources</h2><p id="library-description">Browse {total} references, tools and skills. Each comes with a worksheet and an AI agent guide.</p></div><a class="bench-agent-index" href="resources/workbench/AGENT-INDEX.md">Index for AI agents <span aria-hidden="true">↗</span></a></div>'''
    page = re.sub(r'(<section class="bench-section" id="library"[^>]*>).*?(?=<div id="library-controls")', lambda m:m[1]+intro, page, count=1, flags=re.S)
    controls = '''<div id="library-controls" hidden><div class="library-search"><label class="bench-field" for="resource-search"><span class="visually-hidden">Search resources</span><input id="resource-search" type="search" placeholder="Search resources" autocomplete="off" /></label><label class="bench-field" for="resource-industry"><span class="visually-hidden">Industry</span><select id="resource-industry"><option value="all">Any industry</option><option value="banking">Banking &amp; finance</option><option value="saas">B2B SaaS</option><option value="commerce">Commerce</option><option value="ai">AI products</option><option value="shared">Shared practices</option></select></label></div><div class="bench-result-bar"><p id="resource-count" role="status" aria-live="polite"></p><button class="bench-small-button" id="clear-filters" type="button" hidden>Clear search &amp; industry</button><button class="bench-small-button" id="export-shortlist" type="button" hidden>Export saved list ↓</button></div></div>'''
    page = re.sub(r'<div id="library-controls".*?(?=<div class="bench-grid" id="resource-grid">)',lambda _:controls,page,count=1,flags=re.S)
    page = page.replace('<p id="resource-empty"', '<button class="bench-small-button" id="search-all-resources" type="button" hidden>Search all resources</button><p id="resource-empty"', 1)
    prompt_match = re.search(r'<div class="bench-subheading"><h3>AI workflows you can reuse</h3>.*?(?=<div class="bench-subheading"><h3>Introduce)',page,re.S)
    if prompt_match:
        prompts=prompt_match[0]
        prompts=prompts[prompts.index('</div>')+6:]
        ai=f'<section class="bench-section" id="ai-workflows" aria-labelledby="ai-workflows-title"><div class="bench-intro"><p class="eyebrow">AI for design</p><div><h2 id="ai-workflows-title">Reusable AI prompts</h2><p>Use a focused prompt for states, research, prototype review or a component proposal. Each includes a human check.</p></div></div><div class="bench-ai-quicklinks"><a href="#ai-skills" data-library-view="ai-skills">Browse AI skills →</a><a href="resources/workbench/ai-context-pack.md" download>Download context pack ↓</a></div>{prompts}</section>'
        page=page[:prompt_match.start()]+page[prompt_match.end():]
        page=page.replace('<div class="bench-band"><section class="bench-section" id="tools"',ai+'<div class="bench-band"><section class="bench-section" id="tools"',1)
    page=page.replace('Turn a review into a useful team artifact.','Practical design tools').replace('Reusable files. A common way to work.','Team templates').replace('A small stack. A repeatable workflow.','Working practices')
    page=re.sub(r'(?<=>)0[1-4] / (?=[^<]+</p>)','',page)
    groups={'skill-website-craft':'Web & visual design','skill-design-loop':'Web & visual design','skill-design-dna':'Web & visual design','skill-scroll-craft':'Web & visual design','skill-agent-system':'Design systems','skill-component-crd':'Design systems','skill-humanizer':'Writing & research','skill-refero':'Writing & research','skill-motion-graphics':'Motion & film','skill-ai-film':'Motion & film','skill-film-joey':'Motion & film'}
    for rid,group in groups.items():
        page=page.replace(f'data-resource="{rid}"',f'data-resource="{rid}" data-skill-group="{html.escape(group)}"')
        page=re.sub(rf'(data-resource="{rid}".*?<p class="eyebrow">)AI skills',lambda m:m[1]+html.escape(group),page,count=1,flags=re.S)
    return page
