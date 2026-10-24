"""Build the living project wiki separately from the defence submission snapshot."""
from pathlib import Path
import html
import json
import re

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'docs'/'notion'/'project'
WORK=ROOT/'work'/'notion-migration'
SUBMISSION=ROOT/'docs'/'submission-2026-10-24'
WORK.mkdir(parents=True,exist_ok=True)
manifest=json.loads((SOURCE/'pages.json').read_text(encoding='utf-8'))
branches=manifest['branches']
leaves=manifest['pages']
old=json.loads((ROOT/'docs'/'notion'/'migration-2026-10-24.json').read_text(encoding='utf-8'))

def url(page):
    return page['url'].split('?')[0]

branch_slugs=['defence','product','modules','architecture-index','interfaces','ux','quality','team']
targets={slug:page for slug,page in zip(branch_slugs,branches)}
targets.update({p['slug']:p for p in leaves})
targets['defence-architecture']=old['created_pages'][6]
targets['defence-prototype']=old['created_pages'][7]

def mention(slug):
    return '<mention url="'+url(targets[slug])+'"/>'

def convert_tables(text):
    lines=text.splitlines()
    result=[]
    i=0
    code=False
    while i<len(lines):
        line=lines[i]
        if line.startswith('```'):
            code=not code
        if not code and line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[c.strip() for c in lines[i].strip('|').split('|')]
                if not all(re.fullmatch(r'[:\- ]+',c or '-') for c in cells):
                    rows.append(cells)
                i+=1
            assert len({len(r) for r in rows})==1
            result.append('<table fit-page-width="true" header-row="true">')
            for row in rows:
                result.append('\t<tr>')
                for cell in row:
                    parts=re.split(r'(<(?:mention|date)\b[^>]+/>)',cell)
                    safe=''.join(p if p.startswith(('<mention','<date')) else html.escape(p,quote=False) for p in parts)
                    result.append('\t\t<td>'+safe+'</td>')
                result.append('\t</tr>')
            result.append('</table>')
            continue
        result.append(line)
        i+=1
    return '\n'.join(result)

def render(text):
    def replace(m):
        assert m[1] in targets, m[1]
        return mention(m[1])
    text=re.sub(r'\[\[([a-z-]+)\]\]',replace,text)
    return convert_tables(text)

for required in ['requirements.md','decisions.md']:
    assert (SOURCE/required).is_file(), required

coverage={
    'accounts':[1,2,3,4,14], 'catalogue':[5,6,7,8,9,12],
    'apartments':[9,10,11,12,13,14,22,33], 'publication':list(range(15,23)),
    'selection':[23,24,25,26], 'regions':[7,8,21,27,28],
    'enquiries':[14,30,33,34,35], 'administration':[3,36,37,38,39,40],
    'visuals':[29,30,31,32]}
assert set().union(*(set(v) for v in coverage.values()))==set(range(1,41))

payloads=[]
for page in leaves:
    text=(SOURCE/(page['slug']+'.md')).read_text(encoding='utf-8')
    assert text.splitlines()[0]=='# '+page['title'], page['slug']
    text='\n'.join(text.splitlines()[1:]).strip()
    if page['slug']=='architecture':
        for marker,name in [('CONTEXT_DIAGRAM','01-system-context.mmd'),('COMPONENT_DIAGRAM','03-components.mmd')]:
            code=(SUBMISSION/'diagrams'/name).read_text(encoding='utf-8').strip()
            text=text.replace('{{'+marker+'}}','```mermaid\n'+code+'\n```')
    if page['slug']=='requirements':
        text+='\n\n## Functional ownership\n\n| Owning module | Requirement references |\n| --- | --- |\n'
        for slug,ids in coverage.items():
            text+='| [['+slug+']] | '+', '.join(f'FR-{i:02}' for i in ids)+' |\n'
    parent=branches[page['branch']]
    text='Documentation section: '+mention(branch_slugs[page['branch']])+'.\n\n'+text
    payloads.append({'slug':page['slug'],'page_id':page['id'],'title':page['title'],'content':render(text)})

descriptions={
    1:('Product purpose, users, journeys and scope. This section defines what QONYS provides and which role can perform each operation.',
       'The functional specification is organised by module in [[modules]]. [[navigation]] maps those behaviours to screens.'),
    2:('Functional specifications for the application modules. Each module describes responsibility, data context, workflow, permissions, edge cases and acceptance examples.',
       '[[requirements]] is the complete FR/NFR baseline. [[data]], [[states]] and [[contracts]] define shared relationships and integration rules.'),
    3:('System boundaries, runtime components, domain entities and lifecycle integrity. These pages connect the product rules to the application and persistence design.',
       '[[architecture]] owns component responsibilities. [[data]] owns entity meaning. [[states]] owns visibility, commercial and processing-state boundaries.'),
    4:('Application interactions and asynchronous work. These contracts coordinate the Flutter client, Django API, workers, files and external services.',
       'Logical operations describe their input, outcome and rejection behaviour. Implementation routes and executable schemas belong with the corresponding code and review.'),
    5:('Navigation, screen responsibilities, language handling and developer-supplied content. UI placement follows the domain rules rather than defining a separate version of them.',
       'The prototype reference is retained in [[defence-prototype]]. Current behaviour belongs to the functional modules and [[requirements]].'),
    6:('Functional and non-functional acceptance criteria, traceability and verification scenarios. The initial evaluation uses controlled single-user workflows and a small multilingual case set.',
       'An observed result identifies its implementation revision and conditions. The design-prototype inspection retained in [[defence]] is separate from application/AI verification.'),
    7:('Engineering ownership, delivery/review workflow, current decisions and risks. YouTrack tracks work; Git preserves implementation and versioned evidence; Notion maintains the current specification.',
       'The dated submission is retained under [[defence]]. Changes to the working specification identify affected requirements, modules, interfaces and verification cases.')}

for n in range(1,8):
    branch=branches[n]
    intro,ending=descriptions[n]
    text=intro+'\n\n'
    for page in leaves:
        if page['branch']==n:
            text+=f'<page url="{url(page)}">{page["title"]}</page>\n\n'
    text+=ending
    payloads.append({'slug':branch_slugs[n],'page_id':branch['id'],'title':branch['properties']['title'],'content':render(text)})

root='''QONYS is a platform for finding and comparing individual apartments across property developers, with linked building/floor plans, infrastructure maps and optional supplied visual assets. This workspace is organised as the working project specification.

## Product and functional specification

'''
for n in [1,2]:
    root+=f'<page url="{url(branches[n])}">{branches[n]["properties"]["title"]}</page>\n\n'
root+='## Architecture and engineering\n\n'
for n in [3,4,5,6,7]:
    root+=f'<page url="{url(branches[n])}">{branches[n]["properties"]["title"]}</page>\n\n'
root+='''## Working with the documentation

Start with [[overview]] and [[roles]] for the scope and access model. Open the relevant module before implementing a feature. Use [[data]], [[states]] and [[contracts]] for shared rules, and [[requirements]] with [[verification]] for acceptance.

Each rule has an owning page. Changes update the affected module, requirement and shared contract together. The submission report and its research material are retained separately below.

## Defence materials

'''+f'<page url="{url(branches[0])}">defence24.10.26</page>\n\n'
root+='''## Team and project links

Temirlan Almukhamedov — Systems Analyst and Technical Coordinator. Yevgeniy Averyanov — Backend Developer. Bexultan Nishanbek — Flutter Web Developer. Supervisor — Islam Omirzak.

[GitHub repository](https://github.com/sweezyxxx/qonys) · [YouTrack workspace](https://qonys.youtrack.cloud/)
'''
(WORK/'projectdoc-payloads.json').write_text(json.dumps(payloads,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(WORK/'projectdoc-root.md').write_text(render(root),encoding='utf-8')
(SOURCE/'pages.json').write_text(json.dumps({'root_id':'402878b5-3f09-80a9-beba-fc8ef6d32613','branches':branches,'pages':leaves,'functional_ownership':coverage},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert len(payloads)==29
all_text='\n'.join(p['content'] for p in payloads)
assert not re.search(r'\[\[[a-z-]+\]\]|\{\{[A-Z_]+\}\}',all_text)
assert not re.search(r'\]\((?:\.\./|evidence/|prototype/|diagrams/)',all_text)
req=next(p['content'] for p in payloads if p['slug']=='requirements')
for prefix,count in [('FR',40),('NFR',10)]:
    ids=re.findall(r'<td>('+prefix+r'-\d{2})</td>',req)
    assert len(ids)==len(set(ids))==count,(prefix,len(ids))
print(json.dumps({'working_sections':7,'topic_pages':22,'payloads':29,'FR':40,'NFR':10,'characters':sum(len(p['content']) for p in payloads)},indent=2))
