# ThinkDSP

*Think DSP* is an introduction to Digital Signal Processing in Python.

**Note: This repository contains the second edition of Think DSP, which is a work in progress.**

[The first edition is here](http://greenteapress.com/thinkdsp/html/index.html).

The premise of this book (and the other books in the Think X series) is that if you know how to program, you can use that skill to learn other things. I am writing this book because I think the conventional approach to digital signal processing is backward: most books (and the classes that use them) present the material bottom-up, starting with mathematical abstractions like phasors.

With a programming-based approach, I can go top-down, which means I can present the most important ideas right away. By the end of the first chapter, you can decompose a sound into its harmonics, modify the harmonics, and generate new sounds.

*Think DSP* is a Free Book. It is available under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/), which means that you are free to copy, distribute, and modify it, as long as you attribute the work and don't use it for commercial purposes.


## Work in Progress

In the first edition, the text was in LaTeX and the code was in Python modules.
For this edition, I have combined the text, code, exercises, and solutions into Jupyter notebooks.

At this point, I have tested that the code in the notebooks runs, but I have not checked (1) the references from the text to the figures, and (2) cross-references between sections.

I will work on these things gradually, but in the meantime, please let me know if you find problems.
The best way to do that is to [open an issue](https://github.com/AllenDowney/ThinkDSP2/issues).

If you would like to contribute a correction, please note that the source documents are the notebooks in the `soln` directory.
I use a script to generate the `notebooks` directory.
So if you make any changes, please

1) Make sure you have pulled the most recent notebook from the repository.

2) Make the minimal change/correction, and

3) Clear the output cells before you push your notebook and create a pull request.

If you are not comfortable using Git, it is probably better to create an issue and describe the change.



## Running the code

The chapters of this book are in Jupyter notebooks that contain the text, code, and exercises.

To run the notebooks code, you have two options:

**Option 1:** Run the notebooks on Google Colab (easiest, no installation required).

**Option 2:** Install Python, Jupyter and the required libraries on your computer.

The following sections explain these options in detail.


### Option 1: Run on Colab

Use these links to open the notebooks on Colab.  If you want to modify and save any of them, you can use Colab to save a copy in a Google Drive, in your own GitHub repo, or on your computer.

**Notebooks with no solutions:**

Use these links if you want to work on the exercises.

* [Chapter 1: Sounds and signals](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap01.ipynb)
* [Chapter 2: Harmonics](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap02.ipynb)
* [Chapter 3: Non-Periodic Signals](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap03.ipynb)
* [Chapter 4: Noise](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap04.ipynb)
* [Chapter 5: Autocorrelation](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap05.ipynb)
* [Chapter 6: Discrete Cosine Transform](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap06.ipynb)
* [Chapter 7: Discrete Fourier Transform](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap07.ipynb)
* [Chapter 8: Filtering and Convolution](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap08.ipynb)
* [Chapter 9: Differentiation and Integration](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap09.ipynb)
* [Chapter 10: LTI Systems](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap10.ipynb)
* [Chapter 11: Modulation and Sampling](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/notebooks/chap11.ipynb)



**Notebooks with solutions:**

Use these links if you want to see solutions to the exercises.

* [Chapter 1: Sounds and signals](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap01.ipynb)
* [Chapter 2: Harmonics](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap02.ipynb)
* [Chapter 3: Non-Periodic Signals](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap03.ipynb)
* [Chapter 4: Noise](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap04.ipynb)
* [Chapter 5: Autocorrelation](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap05.ipynb)
* [Chapter 6: Discrete Cosine Transform](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap06.ipynb)
* [Chapter 7: Discrete Fourier Transform](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap07.ipynb)
* [Chapter 8: Filtering and Convolution](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap08.ipynb)
* [Chapter 9: Differentiation and Integration](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap09.ipynb)
* [Chapter 10: LTI Systems](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap10.ipynb)
* [Chapter 11: Modulation and Sampling](https://colab.research.google.com/github/AllenDowney/ThinkDSP2/blob/main/soln/chap11.ipynb)



### Option 2: Install on your computer

**Step 1: Download the files**

You can download the [contents of the repository as a Zip file](https://github.com/AllenDowney/ThinkDSP2/archive/main.zip).
Or you can download [just the notebooks in this Zip file](https://raw.githubusercontent.com/AllenDowney/ThinkDSP2/main/ThinkDSPNotebooks.zip).

Or you can clone the repository:

```
git clone --depth 1 https://github.com/AllenDowney/ThinkDSP2.git
```

You should end up with a directory called `ThinkDSP2`.

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

If you prefer, you can create the environment manually:

```
cd ThinkDSP2
conda create -y --name ThinkDSP2 python=3.12
conda activate ThinkDSP2
pip install -U pip setuptools wheel
pip install -r requirements.txt
```

If you prefer not to use Conda, you can install the same requirements in your favorite environment manage.

Note: You don't have to install `thinkdsp.py` -- in fact, you can't because it is just a module, not a package.
When you run the notebooks, it checks whether you have `thinkdsp.py` and downloads it if you don't.
In the same way, you don't have to download the data files -- the notebooks will download them for you.


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

In the Jupyter interface, click on `notebooks` to see the notebooks with **no solutions** or `soln` to see the notebooks with solutions.
Click on one of the notebooks (files with the .ipynb extension).

Press "Shift-Enter" to run the first few cells. If the import statements run with no error messages, **you are all set**.

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
