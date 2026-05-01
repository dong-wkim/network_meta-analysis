
cp ../README.ipynb ./README.ipynb
pandoc -o README.md README.ipynb
pandoc -o ./sphinx/README.rst README.md
pandoc -o ./jupyter-book/README.myst README.md


