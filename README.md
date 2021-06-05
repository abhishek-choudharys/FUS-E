# FUS-E
## (Fuzzy unhindered search - Efficient)
Built on Python 3.9.

Text file used: The Project Gutenberg EBook of The Adventures of Sherlock Holmes by Sir Arthur Conan Doyle ( <a href="https://github.com/abhishek-choudharys/FUS-E/blob/main/largeText.txt">largeText.txt</a> ) </br>
Number of characters: 6488666

---
---
# Instructions to run:

## Method #1: The easy way!!!

## Method #2: The not-so-easy way.

Note: To avoid any unwanted hassles, you can easily run the code on Google Colab.

### 1. Let's install the necessary packages
Inorder to do this, please run the commands on screen.

``` python
pip install fuzzysearch
pip install fuzzywuzzy
pip install textdistance
```
**OR**

If you're using anaconda, please follow:

``` python
conda install -c conda-forge fuzzysearch
conda install -c conda-forge fuzzywuzzy
conda install -c conda-forge textdistance
```
**OR**

If you want to copy my exact anaconda environment, run: 
(This is not really necessary)
(Also, do this after downloading the repository)
``` python
conda env create -f environment. yml
```


Note: Only the _fuzzysearch_ library is actually required to perform the fuzzy search operation. Rest of the libraries have been used only for further testing.

### 2. Now let's run the code

Download the code using this command and set current location as the directory.
``` 
!git clone https://github.com/abhishek-choudharys/FUS-E.git
cd FUS-E
```

If you want to see the results on pre-defined input, just run timed_test.py.
``` 
run timed_test.py
```

If you want to test it on your input, run timed_test_custom.py.
You can enter your own search query here, based on largeText.txt.
``` 
run timed_test_custom.py
```
