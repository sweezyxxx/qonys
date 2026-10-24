"""Check stage evidence and documentation consistency without rendering images."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import re
from urllib.parse import unquote, urlsplit
import zipfile
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
STAGE = ROOT / 'docs/submission-2026-10-24'
WIKI = ROOT / 'docs/notion/project'
TITLE = ('Development of an AI-Powered Residential Real Estate Visualization and Intelligent Property Selection '
         'Platform with 3D Site Visualization, Floor-Level Layouts, and Interactive Mapping')
TEAM = ['Temirlan Almukhamedov', 'Yevgeniy Averyanov', 'Bexultan Nishanbek']
errors = []
checks = []

def check(value, label):
    (checks if value else errors).append(label)

def read(path):
    return path.read_text(encoding='utf-8')

def requirement_rows(text, prefix):
    return re.findall(r'^\| ('+prefix+r'-\d{2}) \| ([^\n]+) \| ([^\n]+) \| ([^\n]+) \|$', text, re.M)

manifest = json.loads(read(WIKI/'pages.json'))
pages = manifest['pages']
slugs = {p['slug'] for p in pages}
known = slugs | {'defence', 'product', 'modules', 'architecture-index', 'interfaces', 'ux',
                 'quality', 'team', 'defence-architecture', 'defence-prototype'}
check(len(pages) == len(slugs) == 22, '22 unique living topic pages')
check(len(manifest['branches']) == 8, 'Seven working sections and a separate defence branch')
all_wiki = ''
for page in pages:
    path = WIKI/(page['slug']+'.md')
    check(path.is_file(), f"Source exists: {page['slug']}")
    if not path.is_file():
        continue
    text = read(path)
    all_wiki += text+'\n'
    refs = set(re.findall(r'\[\[([a-z-]+)\]\]', text))
    check(refs <= known, f"Wiki references resolve: {page['slug']}")
check(TITLE in read(ROOT/'README.md'), 'Fixed project title preserved')
for path in [ROOT/'README.md', STAGE/'QONYS_analysis_design_2026-10-24.md']:
    text = read(path)
    indexes = [text.find(name) for name in TEAM]
    check(min(indexes) >= 0 and indexes == sorted(indexes), f'Team order: {path.name}')
for path in [STAGE/'15-requirements.md', WIKI/'requirements.md']:
    for prefix, count in [('FR',40),('NFR',10)]:
        rows = requirement_rows(read(path), prefix)
        expected = {f'{prefix}-{n:02}' for n in range(1,count+1)}
        check(len(rows) == count and {r[0] for r in rows} == expected,
              f'{path.parent.name}: {count} distinct {prefix} rows')
        check(all(all(c.strip() for c in r[1:]) for r in rows), f'{prefix} priorities and acceptance text present')
owned = {number for ids in manifest['functional_ownership'].values() for number in ids}
check(owned == set(range(1,41)), 'All functional requirements have module ownership')

verification = json.loads(read(STAGE/'verification.json'))
for document in [d for d in verification['documents'] if d['file']=='QONYS_analysis_design_2026-10-24.docx']:
    path = STAGE/document['file']
    check(path.is_file() and sha256(path.read_bytes()).hexdigest() == document['sha256'],
          f"Verified report hash: {document['file']}")
check(any(d['file']=='QONYS_analysis_design_2026-10-24.docx' for d in verification['documents']), 'Checked report is identified in verification record')
source = STAGE/'evidence/interviews/source-transcript.md'
check(sha256(source.read_bytes()).hexdigest() == verification['source_sha256'], 'Supplied transcript preserved byte-for-byte')
sessions = json.loads(read(STAGE/'evidence/interviews/session-records.json'))['sessions']
check({s['code']:s['interviewer'] for s in sessions} == dict(zip(['D1','B1','B2'], [TEAM[1],TEAM[2],TEAM[0]])), 'Interview allocation preserved')
with zipfile.ZipFile(STAGE/'QONYS_analysis_design_2026-10-24.docx') as archive:
    tree = ET.fromstring(archive.read('word/document.xml'))
    ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    doc_text = '\n'.join(node.text or '' for node in tree.findall('.//w:t', ns))
    check(all(name in doc_text for name in TEAM), 'DOCX contains confirmed team names')
    checked_report = next(d for d in verification['documents'] if d['file']=='QONYS_analysis_design_2026-10-24.docx')
    check(len(tree.findall('.//w:tbl', ns)) == checked_report['tables'], 'DOCX table count matches the verified report')
for name in ['01-system-context','02-use-cases','03-components']:
    for suffix in ['.svg','.png','.json', '.puml' if name=='02-use-cases' else '.mmd']:
        check((STAGE/'diagrams'/(name+suffix)).is_file(), f'Editable/readable diagram: {name+suffix}')
inspection = json.loads(read(STAGE/'prototype/inspection.json'))
check(inspection['outcome'] == 'Passed' and not inspection['browserErrors'], 'Recorded local prototype inspection passed')
check(len(list((STAGE/'prototype/screens').glob('*.png'))) == 9, 'Nine prototype screen exports retained')

# Check human navigation links without following network URLs or local-machine provenance.
nav_files = list(ROOT.glob('*.md')) + list((ROOT/'docs').glob('*.md')) + [
    ROOT/'backend/README.md', ROOT/'tests/README.md', STAGE/'README.md',
    STAGE/'QONYS_analysis_design_2026-10-24.md', STAGE/'diagrams/README.md']
for path in nav_files:
    for href in re.findall(r'!?\[[^\]]*\]\(([^\n)]+)\)', read(path)):
        href = href.strip('<>')
        if urlsplit(href).scheme or href.startswith('#'):
            continue
        target = (path.parent/unquote(href.split('#')[0])).resolve()
        check(target.exists(), f'Local navigation link: {path.relative_to(ROOT)} -> {href}')

result = {'checked_at_utc':datetime.now(timezone.utc).isoformat(),
          'scope':'Documentation consistency, preserved report/source hashes and recorded prototype evidence; no application acceptance or image review.',
          'passed':len(checks),'errors':errors,'checks':checks}
out = ROOT/'work/verification'
out.mkdir(parents=True,exist_ok=True)
(out/'documentation-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['scope','passed','errors']},indent=2))
raise SystemExit(bool(errors))
