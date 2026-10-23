import nbformat as nbf
import yaml
from glob import glob

# Page descriptions for search results and link previews
with open('descriptions.yml') as f:
    DESCRIPTIONS = yaml.safe_load(f)


def process_cell(cell):
    # get tags
    tags = cell['metadata'].get('tags', [])

    # add hide-cell tag to solutions
    if 'solution' in tags:
        # add the hide-cell tag
        tags.append('hide-cell')
        cell['metadata']['tags'] = tags

    # add reference label
    for tag in tags:
        if tag.startswith('chapter') or tag.startswith('section'):
            label = f'({tag})=\n'
            cell['source'] = label + cell['source']


def process_notebook(path):
    ntbk = nbf.read(path, nbf.NO_CONVERT)

    for cell in ntbk.cells:
        process_cell(cell)

    # myst-nb passes notebook metadata through as front matter:
    # html_meta becomes <meta name="description">; og:description overrides
    # the link-preview text, which would otherwise be the opening paragraph
    desc = DESCRIPTIONS.get(path.removesuffix('.ipynb'))
    if desc:
        ntbk.metadata['myst'] = {'html_meta': {'description': desc}}
        ntbk.metadata['og:description'] = desc
    else:
        print('no description for', path)

    nbf.write(ntbk, path)


# All notebooks copied into jb/ for the book (chapters + examples)
paths = glob("*.ipynb")

for path in sorted(paths):
    print('prepping', path)
    process_notebook(path)
