# Build the notebook folder and zip file

# copy notebooks from soln

cp ../soln/chap*.ipynb .

# remove the solutions
python remove_soln.py

# commit the changes
git add chap*.ipynb
git commit -m "Updating the notebooks"

# build the zip file
cd ../..; zip -r ThinkDSPNotebooks.zip ThinkDSP2/notebooks/chap*.ipynb

# add and commit it
mv ThinkDSPNotebooks.zip ThinkDSP2
cd ThinkDSP2

git add ThinkDSPNotebooks.zip
git commit -m "Updating the zip file"

git push
