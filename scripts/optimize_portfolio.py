"""Apply the shared shell and improve delivery of existing approved image assets."""
from pathlib import Path
import re
from PIL import Image
from portfolio_shell import apply_shell

ROOT=Path(__file__).resolve().parents[1]
PREVIEWS=ROOT/'assets/previews'
PREVIEWS.mkdir(exist_ok=True)
sources=['assets/sharwa/cover.png','assets/sharwa/screen-01.png','assets/playful/home-october-2026.jpg','assets/1mt/inveasy/cover.png','assets/uxcel-skill-graph-clean.png']
mapping={}
saved=0
for source in sources:
    original=ROOT/source
    target=PREVIEWS/(original.parent.name+'-'+original.stem+'.webp')
    with Image.open(original) as image:
        image.thumbnail((1200,1200))
        image.convert('RGB').save(target,'WEBP',quality=86,method=6)
    mapping[source]=target.relative_to(ROOT).as_posix()
    saved+=original.stat().st_size-target.stat().st_size

for page in ROOT.glob('*.html'):
    if page.name=='design-system.html':continue
    text=page.read_text(encoding='utf-8')
    if page.name=='index.html':
        for source,target in mapping.items():text=text.replace(f'src="{source}"',f'src="{target}"')
        old=re.search(r'<section class="section"[^>]*aria-labelledby="workbench-invite-title".*?</section>',text,re.S)
        if old:
            text=text[:old.start()]+text[old.end():]
            invite='''<section class="section" id="workbench-preview" aria-labelledby="workbench-invite-title"><div class="section-inner"><div class="workbench-invite"><div><p class="eyebrow">For designers &amp; teams</p><h2 id="workbench-invite-title">Design tools, AI skills<br />and reusable workflows.</h2><p>Browse industry patterns, try the review tools, or download worksheets for people and AI agents.</p><div class="bench-start-links"><a href="workbench.html#ai-skills">Browse AI skills →</a><a href="workbench.html#tools">Try the tools →</a></div></div><a class="button" href="workbench.html">Open the workbench →</a></div></div></section>'''
            position=text.index('<section class="section" id="positioning"')
            text=text[:position]+invite+'\n'+text[position:]
    def image_attrs(match):
        tag=match[0]
        source=re.search(r'src="([^"]+)"',tag)
        if not source:return tag
        target=ROOT/source[1]
        if not target.is_file():return tag
        try:
            with Image.open(target) as image:w,h=image.size
        except Exception:return tag
        if not re.search(r'\bwidth=',tag):tag=tag.replace('<img ',f'<img width="{w}" height="{h}" ',1)
        if 'decoding=' not in tag:tag=tag.replace('<img ','<img decoding="async" ',1)
        return tag
    text=re.sub(r'<img\b[^>]*>',image_attrs,text)
    text=apply_shell(text,page.name)
    page.write_text('\n'.join(line.rstrip() for line in text.splitlines())+'\n',encoding='utf-8')

css=ROOT/'redesign.css'
text=css.read_text(encoding='utf-8')
text=re.sub(r"^@import[^\n]+\n\s*",'',text)
css.write_text(text,encoding='utf-8')
print(f'Applied shared shell and intrinsic image sizes. Preview assets save {saved:,} bytes across {len(mapping)} distinct originals.')
