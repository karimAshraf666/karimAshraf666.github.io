import re
from workbench_navigation import build_navigation

VERSION = '20261015c'

def apply_shell(text, name):
    home = name == 'index.html'
    prefix = '' if home else 'index.html'
    current = ' aria-current="page"'
    header = f'''<header class="site-header"><div class="header-inner">
      <a class="brand" href="{'#top' if home else 'index.html'}" aria-label="Karim Ashraf portfolio home"><span class="brand-mark" aria-hidden="true">K</span>Karim Ashraf</a>
      <a class="mobile-workbench-link" href="workbench.html"{' aria-current="page"' if name == 'workbench.html' else ''}><svg class="nav-workbench-mark" aria-hidden="true" viewBox="0 0 16 16" width="14" height="14" fill="currentColor"><path d="M1 1h5v5H1zM9 1h5v5H9zM1 9h5v5H1zM9 9h5v5H9z"/></svg>Workbench</a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav id="site-nav" aria-label="Primary navigation"><a href="{prefix}#work"{current if 'case-page' in text else ''}>Work</a><a href="{prefix}#about">About</a><a class="nav-workbench" href="workbench.html"{current if name == 'workbench.html' else ''}><svg class="nav-workbench-mark" aria-hidden="true" viewBox="0 0 16 16" width="14" height="14" fill="currentColor"><path d="M1 1h5v5H1zM9 1h5v5H9zM1 9h5v5H1zM9 9h5v5H9z"/></svg>Workbench</a><a href="{prefix}#contact">Contact</a><a class="nav-resume" href="Karim_Ashraf_Product_Designer_Resume_2026.pdf" target="_blank" rel="noopener noreferrer">Résumé ↗</a></nav>
    </div></header>'''
    text = re.sub(r'<header class="site-header">.*?</header>', lambda _: header, text, count=1, flags=re.S)
    text = re.sub(r'<link rel="stylesheet" href="redesign.css[^\"]*"\s*/?>\s*', '', text)
    text = re.sub(r'<link [^>]*(?:fonts.googleapis.com|fonts.gstatic.com|discovery.css)[^>]*>\s*', '', text)
    text = text.replace('</head>', f'<link rel="preconnect" href="https://fonts.googleapis.com" />\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;450;500;550;600;650;700;750;800&amp;display=swap" />\n<link rel="stylesheet" href="redesign.css?v={VERSION}" />\n<link rel="stylesheet" href="design/tokens/discovery.css?v={VERSION}" />\n<link rel="stylesheet" href="discovery.css?v={VERSION}" />\n</head>')
    text = re.sub(r'(script.js|workbench.js|workbench.css)\?v=\d+[a-z]*', lambda m: m[1]+f'?v={VERSION}', text)
    return text

def simplify_workbench(page):
    return apply_shell(build_navigation(page), 'workbench.html')
