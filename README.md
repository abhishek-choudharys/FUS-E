![](https://github.com/abhishek-choudharys/FUS-E/blob/main/imgs/banner.png?raw=true)

![](https://estruyf-github.azurewebsites.net/api/VisitorHit?user=abhishek-choudharysf&repo=FUS-E&countColorcountColor&countColor=%237B1EEA) &nbsp; [![Support Server](https://img.shields.io/discord/591914197219016707.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge)](https://discord.gg/vwm8YNFCy8)




Built with Python 3.9.

Text file: The Project Gutenberg EBook of The Adventures of Sherlock Holmes by Sir Arthur Conan Doyle. (<a href="https://github.com/abhishek-choudharys/FUS-E/blob/main/largeText.txt">``` largeText.txt ```</a>)
<br>
**_Number of characters: 6488666_**

---
---
# Instructions to run:

## Method #1: The easy way!!!
Inorder to do this, just follow these steps.

### 1. Clone the repository
``` 
!git clone https://github.com/abhishek-choudharys/FUS-E.git
```
Or you can ```download``` it directly as a ```.zip``` file by clicking <a href = "https://github.com/abhishek-choudharys/FUS-E/archive/refs/heads/main.zip">here</a>. Then extract the contents and move to step 2.

### 2. Run the .exe file

- If you want to query on largeText.txt, just run <a href="https://github.com/abhishek-choudharys/FUS-E/blob/main/test_keyword.exe">**_``` test_keyword.exe ```_**</a>. Enter the query and see the results.
- _(Optional)_ If you want to select your own input file, just run <a href="https://github.com/abhishek-choudharys/FUS-E/blob/main/test_customFile.exe">**_``` test_customFile.exe ```_**</a>. Enter the address of the .txt file and then the search query.

To see example queries, scroll down to see <a href = "https://github.com/abhishek-choudharys/FUS-E/blob/main/README.md#results">examples</a>. <br>
(Be sure to run the .exe files while in the repo, otherwise there may be path conflicts.)

Easy Peasy Fuzzy Search. Show some love and drop a ⭐.

---
## Method #2: The i-want-to-see-the-code way.

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
conda env create -f src/environment.yml
```


Note: Only the _fuzzysearch_ library is actually required to perform the fuzzy search operation. Rest of the libraries have been used only for further testing.

### 2. Now let's run the code

Download the code using this command and set current location as the directory.
``` 
!git clone https://github.com/abhishek-choudharys/FUS-E.git
cd FUS-E
```

If you want to see the results on pre-defined input file by entering the keyword, just run ``` test_keyword.py ```.
You can enter your search query here, based on ``` largeText.txt ```.
``` 
run src/test_keyword.py
```

If you want to test it on your input file, run ``` test_customFile.py ```.
Enter the address of the text file when prompted, and then enter your query.
``` 
run src/test_customFile.py
```

---
# Results:
A couple of snapshots demonstrating the search.

<p align="center"> 
  <img src="https://github.com/abhishek-choudharys/FUS-E/blob/main/results/result1.png?raw=true" alt="Result 2" width="450"/>
  <img src="https://github.com/abhishek-choudharys/FUS-E/blob/main/results/result2.png?raw=true" alt="Result 2" width="370"/>
  
</p>

---
---
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) &nbsp; [![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://gitHub.com/abhishek-choudharys/)

