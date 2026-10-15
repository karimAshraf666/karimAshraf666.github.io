"""Check public page links, confidentiality and the generated resource collection."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,zipfile

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,path):
        super().__init__();self.ids=[];self.refs=[];self.resources=[];self.images=[]
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='img':self.images.append(a)
        if 'data-resource' in a:self.resources.append(a['data-resource'])
        for key in ('src','href'):
            if key in a:self.refs.append(a[key])
paths=[*ROOT.glob('*.html'),*(ROOT/'resources/workbench/resource-guides').glob('*.html')]
pages={p.resolve():Page(p) for p in paths}
checked=0
for p,page in pages.items():
    assert len(page.ids)==len(set(page.ids)),f'Duplicate IDs in {p.name}'
    assert '\u2014' not in p.read_text(encoding='utf-8'),f'Em dash in {p.name}'
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        target=(p.parent/unquote(u.path)).resolve() if u.path else p
        assert target.exists(),f'{p.name}: missing {ref}'
        if u.fragment and target.suffix=='.html':assert u.fragment in pages[target].ids,f'{p.name}: missing anchor {ref}'
        assert 'assets/money-fellows/' not in ref,f'Uncleared resource in {p.name}'
        checked+=1
    if p.parent==ROOT:
        for image in page.images:
            assert image.get('alt'),f'Missing image alternative in {p.name}'
            assert image.get('width') and image.get('height'),f'Missing image dimensions in {p.name}'
for p in [*ROOT.glob('*.css'),*ROOT.glob('design/tokens/*.css')]:
    assert '\u2014' not in p.read_text(encoding='utf-8'),f'Em dash in {p.name}'
kit=ROOT/'resources/workbench'
catalog=json.loads((kit/'resource-catalog.json').read_text(encoding='utf-8'))['resources']
ids=[r['id'] for r in catalog]
assert len(ids)==len(set(ids))
assert set(pages[(ROOT/'workbench.html').resolve()].resources)==set(ids)
for resource in catalog:
    for key in ['humanTemplate','csvTemplate','agentGuide']:assert (kit/resource[key]).is_file()
for name in ['design-workbench-team-kit.zip','design-ai-skills.zip']:
    with zipfile.ZipFile(kit/name) as z:assert z.testzip() is None
for archive in (kit/'skill-downloads').glob('*.zip'):
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        folder=kit/'skills'/archive.stem
        expected={p.relative_to(kit/'skills').as_posix():p for p in folder.rglob('*') if p.is_file()}
        assert set(z.namelist())==set(expected),f'Incomplete skill package: {archive.name}'
        for name,path in expected.items():assert z.read(name)==path.read_bytes(),f'Stale skill file: {name}'
print(f'Passed: {len(pages)} pages, {checked} local references, {len(ids)} resource packages, image dimensions, anchors and archive integrity.')
