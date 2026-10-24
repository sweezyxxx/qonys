"""Export the revised QONYS design figures from editable geometry, not old scope."""
from pathlib import Path
from html import escape
import json
import math

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs' / 'submission-2026-10-24' / 'diagrams'
FONTS = Path('C:/Windows/Fonts')


class Figure:
    def __init__(self, name, width, height):
        self.name, self.width, self.height = name, width, height
        self.nodes, self.edges, self.labels = [], [], []

    def node(self, xy, lines, kind='box', size=28):
        self.nodes.append(dict(xy=xy, lines=lines, kind=kind, size=size))

    def edge(self, points, arrow=True):
        self.edges.append(dict(points=points, arrow=arrow))

    def label(self, xy, lines, size=26, bold=False):
        self.labels.append(dict(xy=xy, lines=lines, size=size, bold=bold))

    def save(self):
        scale = 2
        image = Image.new('RGB', (self.width * scale, self.height * scale), 'white')
        draw = ImageDraw.Draw(image)
        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">',
               '<rect width="100%" height="100%" fill="white"/>']
        ink, fill, stroke = '#152b3b', '#f1f5f8', '#476174'

        def coords(values):
            return tuple(round(value * scale) for value in values)

        def text(xy, lines, size, bold=False, available=None):
            font = ImageFont.truetype(str(FONTS / ('arialbd.ttf' if bold else 'arial.ttf')), size * scale)
            leading = size + 8
            if available:
                for line in lines:
                    measured = draw.textlength(line, font=font) / scale
                    if measured > available[0] - 24:
                        raise ValueError(f'{self.name}: label too wide: {line!r} ({measured:.1f} > {available[0]-24})')
                if len(lines) * leading > available[1] - 10:
                    raise ValueError(f'{self.name}: label too tall: {lines!r}')
            for index, line in enumerate(lines):
                x, y = xy[0], xy[1] + (index - (len(lines)-1)/2) * leading
                draw.text(coords((x, y)), line, font=font, fill=ink, anchor='mm')
                svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" font-family="Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{ink}">{escape(line)}</text>')

        def line(points, arrow=False):
            draw.line([coords(point) for point in points], fill=stroke, width=4)
            svg.append('<polyline points="' + ' '.join(f'{x},{y}' for x, y in points) + f'" fill="none" stroke="{stroke}" stroke-width="2"/>')
            if arrow:
                (x, y), (px, py) = points[-1], points[-2]
                angle = math.atan2(y-py, x-px)
                triangle = [(x, y), (x-15*math.cos(angle-.4), y-15*math.sin(angle-.4)), (x-15*math.cos(angle+.4), y-15*math.sin(angle+.4))]
                draw.polygon([coords(point) for point in triangle], fill=stroke)
                svg.append('<polygon points="' + ' '.join(f'{x},{y}' for x, y in triangle) + f'" fill="{stroke}"/>')

        for node in self.nodes:
            if node['kind'] != 'boundary':
                continue
            x, y, width, height = node['xy']
            draw.rectangle(coords((x, y, x+width, y+height)), outline=stroke, width=4)
            svg.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="none" stroke="{stroke}" stroke-width="2"/>')
            text((x+width/2, y+25), node['lines'], node['size'], True)
        for edge in self.edges:
            line(edge['points'], edge['arrow'])
        for node in self.nodes:
            kind = node['kind']
            if kind == 'boundary':
                continue
            if kind == 'actor':
                x, y = node['xy']
                draw.ellipse(coords((x-17, y-46, x+17, y-12)), outline=stroke, width=4, fill='white')
                svg.append(f'<circle cx="{x}" cy="{y-29}" r="17" fill="white" stroke="{stroke}" stroke-width="2"/>')
                for points in [[(x,y-12),(x,y+35)],[(x-30,y+5),(x+30,y+5)],[(x,y+35),(x-26,y+68)],[(x,y+35),(x+26,y+68)]]:
                    line(points)
                text((x, y+95), node['lines'], node['size'], True)
                continue
            x, y, width, height = node['xy']
            bounds = coords((x, y, x+width, y+height))
            if kind == 'ellipse':
                draw.ellipse(bounds, fill='white', outline=stroke, width=4)
                svg.append(f'<ellipse cx="{x+width/2}" cy="{y+height/2}" rx="{width/2}" ry="{height/2}" fill="white" stroke="{stroke}" stroke-width="2"/>')
            else:
                draw.rectangle(bounds, fill=fill, outline=stroke, width=4)
                svg.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
            text((x+width/2, y+height/2), node['lines'], node['size'], available=(width, height))
        for label in self.labels:
            text(label['xy'], label['lines'], label['size'], label['bold'])
        svg.append('</svg>')
        (OUT / (self.name + '.svg')).write_text('\n'.join(svg), encoding='utf-8')
        (OUT / (self.name + '.json')).write_text(json.dumps(dict(width=self.width, height=self.height, nodes=self.nodes, edges=self.edges, labels=self.labels), indent=2), encoding='utf-8')
        image.save(OUT / (self.name + '.png'))


def context():
    f = Figure('01-system-context', 1600, 960)
    f.label((800, 42), ['QONYS — System context'], 36, True)
    f.node((60, 125, 360, 150), ['Buyer / visitor', 'Browse, compare, select', 'Verified: save / enquire'])
    f.node((60, 410, 360, 150), ['Property developer', 'Prepare owned content', 'Publish / handle enquiries'])
    f.node((60, 695, 360, 150), ['Platform administrator', 'Access and visibility', 'References, counts, audit'])
    f.node((580, 290, 440, 370), ['QONYS platform', 'Shared development catalogue', 'Building / floor / apartment links', 'Buyer selection and enquiries', 'Developer workspace', 'Local AI and supplied viewers'])
    f.node((1190, 190, 350, 150), ['OpenStreetMap sources', 'Map / infrastructure', 'External data dependency'])
    f.node((1190, 630, 350, 150), ['SMTP mail service', 'Verify / activate / reset', 'New-enquiry notifications'])
    f.edge([(420,200),(500,200),(500,370),(580,370)])
    f.edge([(420,485),(580,485)])
    f.edge([(420,770),(500,770),(500,580),(580,580)])
    f.edge([(1020,370),(1100,370),(1100,265),(1190,265)])
    f.edge([(1020,580),(1100,580),(1100,705),(1190,705)])
    f.label((800, 910), ['Local model execution belongs to QONYS; no paid model API is selected.', 'Enquiries do not purchase, pay for or automatically reserve property.'], 25)
    f.save()
    (OUT/'01-system-context.mmd').write_text('''flowchart LR
  B["Buyer / visitor"] -->|"Browse; verified save / enquire"| Q["QONYS platform"]
  D["Property developer"] -->|"Owned content, publication, enquiries"| Q
  A["Platform administrator"] -->|"Access, visibility, references, overview, audit"| Q
  Q -->|"Map tiles / infrastructure"| O["OpenStreetMap sources"]
  Q -->|"Account emails / enquiry notifications"| E["SMTP mail service"]
''', encoding='utf-8')


def use_cases():
    f = Figure('02-use-cases', 2100, 1200)
    f.label((1050, 38), ['QONYS — Use cases'], 36, True)
    f.node((60, 300, 1980, 790), ['QONYS system boundary'], 'boundary', 28)
    actors = [(400, ['Buyer / visitor']), (1050, ['Property developer']), (1700, ['Platform administrator'])]
    groups = [
        [(['UC-01 Browse and inspect', 'Catalogue, development, floor, apartment'], 'Browse and inspect catalogue/property'),
         (['UC-02 Select with AI', 'Preferences and actual catalogue matches'], 'Select with AI'),
         (['UC-03 Compare apartments', 'Up to four; across developments'], 'Compare apartments'),
         (['UC-04 Manage favourites and history', 'Verified buyer only'], 'Manage favourites and own enquiry history'),
         (['UC-05 Submit an enquiry', 'Verified buyer; current option / price'], 'Submit an enquiry')],
        [(['UC-06 Prepare private content', 'Save and resume an incomplete draft'], 'Prepare private development content'),
         (['UC-07 Review and link regions', 'AI suggestions plus manual correction'], 'Review and link floor / apartment regions'),
         (['UC-08 Maintain apartments / finishing', 'Prices, media and shared availability'], 'Maintain apartments and finishing'),
         (['UC-09 Publish and update', 'Complete first publication; valid saves live'], 'Publish a complete development and save updates'),
         (['UC-10 Handle enquiries', 'Processing states and archive'], 'Handle enquiries and archive')],
        [(['UC-11 Manage developer access', 'Manual verification; suspend / reactivate'], 'Manage developer access'),
         (['UC-12 Moderate development visibility', 'Hide with reason; restore after correction'], 'Moderate development visibility'),
         (['UC-13 Manage reference data', 'Edit / deactivate; protect referenced values'], 'Manage city and finishing reference data'),
         (['UC-14 View platform overview', 'Developers, buyers, published, hidden'], 'View platform overview'),
         (['UC-15 Inspect audit history', 'Automatic key-change records and filters'], 'Inspect audit history')]
    ]
    puml = ['@startuml', 'left to right direction', 'actor "Buyer / visitor" as B', 'actor "Property developer" as D', 'actor "Platform administrator" as A', 'rectangle "QONYS" {']
    for index, ((actor_x, actor_lines), cases) in enumerate(zip(actors, groups)):
        f.node((actor_x, 135), actor_lines, 'actor', 28)
        x, bus = 110 + index*650, 710 + index*650
        for row, (lines, semantic) in enumerate(cases):
            y, number = 350 + row*145, index*5 + row + 1
            f.node((x, y, 580, 130), lines, 'ellipse', 26)
            f.edge([(actor_x+30,140),(bus,140),(bus,y+65),(x+580,y+65)], arrow=False)
            puml.append(f'  usecase "UC-{number:02d} {semantic}" as U{number}')
    puml.append('}')
    for actor, start in [('B',1),('D',6),('A',11)]:
        puml.extend(f'{actor} -- U{number}' for number in range(start,start+5))
    puml += ['note bottom of U4 : Verified buyer only', 'note bottom of U5 : Verified buyer; current availability, finishing and price', '@enduml']
    f.label((1050, 1150), ['Guest access covers browsing, AI selection and comparison. Favourites and new enquiries require verified buyer access.'], 26)
    f.save()
    (OUT/'02-use-cases.puml').write_text('\n'.join(puml)+'\n', encoding='utf-8')


def components():
    f = Figure('03-components', 1800, 1120)
    f.label((900, 38), ['QONYS — Component architecture'], 36, True)
    f.node((560, 95, 680, 120), ['Flutter Web browser client', 'Catalogue, assistant, editor and accounts', 'Embedded Three.js / Pannellum'], size=28)
    f.node((60, 95, 360, 120), ['OpenStreetMap sources', 'Tiles / infrastructure'], size=28)
    f.node((1380, 95, 360, 120), ['SMTP mail service', 'Account / enquiry email'], size=28)
    f.node((470, 350, 860, 260), ['Django / DRF — one modular application', 'Identity / companies; catalogue / content / publication', 'Selection; region preparation and job orchestration', 'Personal features; enquiries and notification jobs', 'Administration, references and audit', 'Shared permissions, ownership and domain rules'], size=28)
    f.node((60, 420, 340, 160), ['Local Ollama runtime', 'Qwen3 model', 'Structured preferences'], size=28)
    f.node((1390, 350, 350, 110), ['RabbitMQ', 'Task references'], size=28)
    f.node((1390, 570, 350, 150), ['Celery workers', 'Shared application rules', 'Processing / email jobs'], size=28)
    f.node((1390, 830, 350, 130), ['SAM 2 + OpenCV', 'Project processing', 'Suggested regions / SVG'], size=28)
    f.node((470, 850, 400, 140), ['PostgreSQL', 'Owned records, prices, states', 'Snapshots, links, job metadata'], size=26)
    f.node((940, 850, 400, 140), ['Server filesystem storage', 'Uploads, SVG and GLB', 'Owned and private-file access'], size=26)
    f.edge([(900,215),(900,350)])
    f.label((1020, 280), ['HTTPS / API'], 26)
    f.edge([(560,155),(420,155)])
    f.label((490, 120), ['Tiles'], 23)
    f.edge([(470,395),(440,395),(440,270),(240,270),(240,215)])
    f.label((235, 310), ['Infrastructure import'], 24)
    f.edge([(470,540),(430,540),(430,650),(230,650),(230,580)])
    f.label((230, 700), ['Validated model adapter'], 24)
    f.edge([(1330,405),(1390,405)])
    f.edge([(1565,460),(1565,570)])
    f.label((1660, 515), ['Delivery'], 24)
    f.edge([(1565,720),(1565,830)])
    f.label((1660, 775), ['Region jobs'], 24)
    f.edge([(1390,645),(1360,645),(1360,560),(1330,560)])
    f.edge([(670,610),(670,850)])
    f.label((805, 760), ['Records / metadata'], 25)
    f.edge([(1120,610),(1120,850)])
    f.label((1240, 760), ['Managed files'], 25)
    f.edge([(1740,635),(1765,635),(1765,155),(1740,155)])
    f.label((1560, 275), ['Email jobs'], 24)
    f.label((900, 1060), ['Workers reuse the shared application and data-access layer.', 'Local inference and background image processing use controlled application interfaces.'], 25)
    f.save()
    (OUT/'03-components.mmd').write_text('''flowchart TB
  WEB["Flutter Web; embedded Three.js / Pannellum"] -->|HTTPS| API["Django / DRF modular application"]
  WEB -->|Map tiles| OSM["OpenStreetMap sources"]
  API -->|Infrastructure import| OSM
  API -->|Validated model adapter| LLM["Local Ollama / Qwen3"]
  API -->|Shared records / metadata| DB[("PostgreSQL")]
  API -->|Managed files| FS["Server filesystem storage"]
  API -->|Task references| MQ["RabbitMQ"]
  MQ -->|Delivery| WORK["Celery workers"]
  WORK -->|Reuse domain / data access| API
  WORK -->|Region processing| SEG["SAM 2 / OpenCV; project-specific grouping / SVG"]
  WORK -->|Email jobs| SMTP["SMTP mail service"]
''', encoding='utf-8')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    context()
    use_cases()
    components()
    (OUT/'README.md').write_text('''# Revised QONYS diagrams

These figures define the QONYS system context, use cases and component architecture for the analysis and design submission.

Each figure has an editable SVG, high-resolution PNG and geometry JSON. Context and components also have Mermaid sources; the Use Case Diagram has a PlantUML source. Semantic source and export labels are maintained together by scripts/build_submission_diagrams.py. The SVG/PNG exports are generated from the explicit geometry model, not by Mermaid/PlantUML layout engines.

Use landscape pages or a sufficiently large display for readable labels. The use-case figure uses three human business roles; verified-buyer conditions are stated on account-only goals. Software developers, a separate sales-manager role and paid AI providers are not introduced as business actors.

- [Context](01-system-context.svg) / [Mermaid](01-system-context.mmd)
- [Use cases](02-use-cases.svg) / [PlantUML](02-use-cases.puml)
- [Components](03-components.svg) / [Mermaid](03-components.mmd)
''', encoding='utf-8')
    print('Generated 3 revised figures: semantic sources, SVG, PNG and editable geometry JSON.')


if __name__ == '__main__':
    main()
