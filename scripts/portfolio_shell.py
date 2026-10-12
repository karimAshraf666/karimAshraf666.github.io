import re

def apply_shell(text, name):
    home = name == 'index.html'
    prefix = '' if home else 'index.html'
    current = ' aria-current="page"'
    header = f'''<header class="site-header"><div class="header-inner">
      <a class="brand" href="{'#top' if home else 'index.html'}" aria-label="Karim Ashraf portfolio home"><span class="brand-mark" aria-hidden="true">K</span>Karim Ashraf</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav id="site-nav" aria-label="Primary navigation"><a href="{prefix}#work"{current if 'case-page' in text else ''}>Work</a><a href="{prefix}#about">About</a><a href="workbench.html"{current if name == 'workbench.html' else ''}>Workbench</a><a href="{prefix}#contact">Contact</a><a class="nav-resume" href="Karim_Ashraf_Product_Designer_Resume_2026.pdf" target="_blank" rel="noopener noreferrer">Résumé ↗</a></nav>
    </div></header>'''
    text = re.sub(r'<header class="site-header">.*?</header>', lambda _: header, text, count=1, flags=re.S)
    text = re.sub(r'<link rel="stylesheet" href="redesign.css[^\"]*"\s*/?>\s*', '', text)
    text = text.replace('</head>', '<link rel="stylesheet" href="redesign.css?v=20261012b" />\n</head>')
    text = re.sub(r'script.js\?v=\d+[a-z]*', 'script.js?v=20261012b', text)
    text = re.sub(r'workbench.js\?v=\d+[a-z]*', 'workbench.js?v=20261012b', text)
    return text

def simplify_workbench(page):
    controls = '''<div id="library-controls" hidden>
      <div class="library-viewbar"><div class="library-view-switch" role="group" aria-label="Resource views"><button id="all-resources" type="button" aria-pressed="true">All resources</button><button id="saved-only" type="button" aria-pressed="false">Saved</button></div></div>
      <div class="library-search">
        <label class="bench-field" for="resource-search"><span class="visually-hidden">Search the library</span><input id="resource-search" type="search" placeholder="Search patterns, tools or articles" /></label>
        <label class="bench-field" for="resource-industry"><span class="visually-hidden">Industry</span><select id="resource-industry"><option value="all">Any industry</option><option value="banking">Banking &amp; finance</option><option value="saas">B2B SaaS</option><option value="commerce">Commerce</option><option value="ai">AI products</option><option value="shared">Shared practices</option></select></label>
        <details class="library-options" id="library-options"><summary>Refine</summary><div class="library-options-panel"><label class="bench-field" for="resource-type">Resource type<select id="resource-type"><option value="all">All resource types</option><option>Systems &amp; UI kits</option><option>UX patterns</option><option>Articles &amp; guidance</option><option>Plugins</option><option>Tools</option></select></label></div></details>
      </div><div class="bench-result-bar"><p id="resource-count" role="status" aria-live="polite"></p><button class="bench-small-button" id="clear-filters" type="button" hidden>Reset</button><button class="bench-small-button" id="export-shortlist" type="button" hidden>Export saved list ↓</button></div>
    </div>
    '''
    page = re.sub(r'<div id="library-controls".*?(?=<div class="bench-grid" id="resource-grid">)', lambda _: controls, page, count=1, flags=re.S)
    for old,new in [('01 / Resource library','Library'),('02 / Practical tools','Tools'),('03 / Team kit','Team kit'),('04 / Working practices','Practices')]:
        page = page.replace(f'>{old}</a>', f'>{new}</a>')
    return apply_shell(page, 'workbench.html')
