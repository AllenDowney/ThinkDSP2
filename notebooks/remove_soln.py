import nbformat as nbf
from glob import glob

# Collect a list of all notebooks in the current directory
notebooks = glob("chap*.ipynb")

# Search through each notebook
for ipath in notebooks:
    ntbk = nbf.read(ipath, nbf.NO_CONVERT)

    cells = []
    for cell in ntbk.cells:

        # remove tags
        tags = cell['metadata'].get('tags', [])
        if tags:
            cell['metadata']['tags'] = []
            
        # remove output
        if 'outputs' in cell:
            cell['outputs'] = []

        if 'solution' not in tags:
            cells.append(cell)

    ntbk.cells = cells
    nbf.write(ntbk, ipath)
