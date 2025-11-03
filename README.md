# ThinkDSP

*Think DSP* is an introduction to Digital Signal Processing in Python.

**Note: This repository contains the second edition of Think DSP, which is a work in progress.**

[The first edition is here](http://greenteapress.com/thinkdsp/html/index.html).

The premise of this book (and the other books in the Think X series) is that if you know how to program, you can use that skill to learn other things. I am writing this book because I think the conventional approach to digital signal processing is backward: most books (and the classes that use them) present the material bottom-up, starting with mathematical abstractions like phasors.

With a programming-based approach, I can go top-down, which means I can present the most important ideas right away. By the end of the first chapter, you can decompose a sound into its harmonics, modify the harmonics, and generate new sounds.

*Think DSP* is a Free Book. It is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/), which means that you are free to copy, distribute, and modify it, as long as you attribute the work and don't use it for commercial purposes.



## Running the code

Most of the code for this book is in Jupyter notebooks.
If you are not familiar with Jupyter, you can run a tutorial by [clicking here](https://jupyter.org/try).  Then select "Try Classic Notebook".  It will open a notebook with instructions for getting started.

To run the ThinkDSP code, you have two options:

**Option 1:** Run the notebooks on Google Colab (easiest, no installation required).

**Option 2:** Install Python and the required libraries on your computer.

The following sections explain these options in detail.

Note: I have heard from a few people who tried to run the code in Spyder.  Apparently there were problems, so I don't recommend it.

### Option 1: Run on Colab

Use these links to open the notebooks on Colab.  If you want to modify and save any of them, you can use Colab to save a copy in a Google Drive or your own GitHub repo, or on your computer.

* [chap01.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap01.ipynb)
* [chap02.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap02.ipynb)
* [chap03.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap03.ipynb)
* [chap04.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap04.ipynb)
* [chap05.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap05.ipynb)
* [chap06.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap06.ipynb)
* [chap07.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap07.ipynb)
* [chap08.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap08.ipynb)
* [chap09.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap09.ipynb)
* [chap10.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap10.ipynb)
* [chap11.ipynb](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap11.ipynb)



### Option 2: Install on your computer

This option requires that you have [Conda](https://docs.conda.io/en/latest/miniconda.html) (or [Anaconda](https://www.anaconda.com/products/distribution)) and `make` installed on your system.

**Step 1: Download the repository**

If you are a Git user, clone the repository:

```
git clone --depth 1 https://github.com/AllenDowney/ThinkDSP2.git
```

Otherwise, [download this Zip file](https://github.com/AllenDowney/ThinkDSP2/archive/main.zip) and unzip it.

Either way, you should end up with a directory called `ThinkDSP2`.

**Step 2: Create and activate a Conda environment**

Navigate to the repository directory and create the environment:

```
cd ThinkDSP2
make create_environment
conda activate ThinkDSP2
make requirements
```

This will:
- Create a new Conda environment called `ThinkDSP2` with Python 3.12
- Install all required packages from `requirements.txt`

**Alternative: Manual installation**

If you prefer not to use `make`, you can create the environment manually:

```
cd ThinkDSP2
conda create -y --name ThinkDSP2 python=3.12
conda activate ThinkDSP2
pip install -U pip setuptools wheel
pip install -r requirements.txt
```

**Step 3: Start Jupyter**

Make sure the Conda environment is activated (you should see `(ThinkDSP2)` in your terminal prompt), then run:

```
jupyter notebook
```

Or, if you prefer JupyterLab:

```
jupyter lab
```

Jupyter should launch your default browser or open a tab in an existing browser window.

**Step 4: Open a notebook**

In the Jupyter interface, click on `soln` to open the folder with the notebooks, then click on one of the notebooks (with the .ipynb extension).

Select a cell with import statements and press "Shift-Enter" to run the code. If it works and you get no error messages, **you are all set**.

If you get error messages about missing packages, make sure:
1. The Conda environment is activated (`conda activate ThinkDSP2`)
2. All packages were installed (`make requirements` or `pip install -r requirements.txt`)

If you run into problems with these instructions, let me know and I will make corrections.  Good luck!



## Freesound

Special thanks to Freesound (http://freesound.org), which is the source of many of the
sound samples I use in this book, and to the Freesound users who
uploaded those sounds.  I include some of their wave files in
the GitHub repository for this book, using the original file
names, so it should be easy to find their sources.

Unfortunately, most Freesound users don't make their real names
available, so I can only thank them using their user names.  Samples
used in this book were contributed by Freesound users: iluppai,
wcfl10, thirsk, docquesting, kleeb, landup, zippi1, themusicalnomad,
bcjordan, rockwehrmann, marchascon7, jcveliz.  Thank you all!

Here are links to the sources:

http://www.freesound.org/people/iluppai/sounds/100475/

http://www.freesound.org/people/wcfl10/sounds/105977/

http://www.freesound.org/people/Thirsk/sounds/120994/

http://www.freesound.org/people/ciccarelli/sounds/132736/

http://www.freesound.org/people/Kleeb/sounds/180960/

http://www.freesound.org/people/zippi1/sounds/18871/

http://www.freesound.org/people/themusicalnomad/sounds/253887/

http://www.freesound.org/people/bcjordan/sounds/28042/

http://www.freesound.org/people/rockwehrmann/sounds/72475/

http://www.freesound.org/people/marcgascon7/sounds/87778/

http://www.freesound.org/people/jcveliz/sounds/92002/
