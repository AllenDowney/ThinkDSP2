# pip install jupyter-book ghp-import

# Build the Jupyter book version

# copy the notebooks
cp ../soln/chap[01][0-9]*.ipynb .
cp ../examples/cacophony.ipynb .
cp ../examples/dft_example.ipynb .
cp ../examples/fourth_wave.ipynb .
cp ../examples/phase.ipynb .
cp ../examples/pink_noise.ipynb .
cp ../examples/saxophone.ipynb .
cp ../examples/voss.ipynb .

# add tags to hide the solutions
python prep_notebooks.py

# build the HTML version
jb build .

# push it to GitHub
ghp-import -n -p -f _build/html
