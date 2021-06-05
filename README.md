# FUS-E
![](https://estruyf-github.azurewebsites.net/api/VisitorHit?user=abhishek-choudharysf&repo=FUS-E&countColorcountColor&countColor=%237B1E7A)

## (Fuzzy unhindered search - Efficient)
Built on Python 3.9.

Text file used: The Project Gutenberg EBook of The Adventures of Sherlock Holmes by Sir Arthur Conan Doyle ( <a href="https://github.com/abhishek-choudharys/FUS-E/blob/main/largeText.txt">largeText.txt</a> ) </br>
Number of characters: 6488666

---
---
# Instructions to run:

## Method #1: The easy way!!!
Inorder to do this, just follow these steps.

### 1. Clone the repository
``` 
!git clone https://github.com/abhishek-choudharys/FUS-E.git
```

### 2. Run the .exe file

- If you want to query on largeText.txt, just run <a href="https://github.com/abhishek-choudharys/FUS-E/blob/main/test_keyword.exe">**_test_keyword.exe_**</a>. Enter the query and see the results.
- _(Optional)_ If you want to select your own input file, just run <a href="https://github.com/abhishek-choudharys/FUS-E/blob/main/test_customFile.exe">**_test_customFile.exe_**</a>. Enter the address of the .txt file and then the search query.

Easy Peasy Fuzzy Search. Show some love and ⭐ the repository.

---
## Method #2: The I-want-to-see-the-code way.

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
conda env create -f src/environment. yml
```


Note: Only the _fuzzysearch_ library is actually required to perform the fuzzy search operation. Rest of the libraries have been used only for further testing.

### 2. Now let's run the code

Download the code using this command and set current location as the directory.
``` 
!git clone https://github.com/abhishek-choudharys/FUS-E.git
cd FUS-E
```

If you want to see the results on pre-defined input file by entering the keyword, just run test_keyword.py.
You can enter your search query here, based on largeText.txt.
``` 
run src/test_keyword.py
```

If you want to test it on your input file, run test_customFile.py.
Enter the address of the text file when prompted, and then enter your query.
``` 
run src/test_customFile.py
```
