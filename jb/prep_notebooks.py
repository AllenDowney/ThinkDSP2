import nbformat as nbf
from glob import glob


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

    nbf.write(ntbk, path)


# All notebooks copied into jb/ for the book (chapters + examples)
paths = glob("*.ipynb")

for path in sorted(paths):
    print('prepping', path)
    process_notebook(path)
