#!/usr/bin/env bash
# Build (and optionally publish) the Jupyter Book.
#
# Prerequisites: pip install jupyter-book ghp-import
# From repo root: bash jb/build.sh
# Publish:        bash jb/build.sh --publish
#
# Tracked in jb/: _config.yml, _toc.yml, index.md, build.sh, prep_notebooks.py
# Generated at build time (not committed): *.ipynb copies, _build/

set -euo pipefail
cd "$(dirname "$0")"

PUBLISH=0
if [[ "${1:-}" == "--publish" ]]; then
  PUBLISH=1
fi

# Copy canonical notebooks into jb/ (sources: soln/ + examples/)
# chap12 is a stub — omit from the book until it has content
cp ../soln/chap0[0-9].ipynb ../soln/chap1[01].ipynb .
cp ../examples/cacophony.ipynb .
cp ../examples/dft_example.ipynb .
cp ../examples/fourth_wave.ipynb .
cp ../examples/phase.ipynb .
cp ../examples/pink_noise.ipynb .
cp ../examples/saxophone.ipynb .
cp ../examples/voss.ipynb .
cp ../examples/chap01preview.ipynb .
cp ../examples/chap10preview.ipynb .

# Hide solutions; add {ref} labels from chapter-/section- tags
python prep_notebooks.py

# Build HTML
jb build .

if [[ "$PUBLISH" -eq 1 ]]; then
  ghp-import -n -p -f _build/html
  echo ">>> Published to gh-pages"
else
  echo ">>> Build complete: jb/_build/html/"
  echo ">>> Publish with: bash jb/build.sh --publish"
fi
