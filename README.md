# fun-projects

This repository includes my startup projects about Chinese Slang words
- [1. Project 1 - Basic Search](#1-project-1---basic-search)
- [2. Project 2 - TextRank](#2-project-2---textrank)

## 1. Project 1 - Basic Search

I provide an easy ETL process to extract the slang words from our existing csv forms to sqlite. 
And Users can feel free to play around with our data. The main purpose is to give anyone who is interested in Chinese
a better way to learn Chinese slang words

### 1.1 Prerequisites

- Python 3.x
- Pandas library
- SQLite3 library

### 1.2 Setup

1. Clone the repository or download the project files to your local machine.

2. Install the required dependencies by running the following command in your terminal or command prompt:

   ```
   #pip install SQLite3 #if you have not install SQLite3
   #pip install Pandas #if you have not install pandas
   ```

### 1.2 Run project

To load csv to sqllite and start API server, run the following command:

```
python Slang_seach.py
#python3 Slang_seach.py
```

Specifically,

#### Data Loading

The transaction data is loaded into the SQLite database using the `Extract_slang.py` script:

```
python Extract_slang.py
```

This script reads the `google_form_slangs.csv` and other 3  files, concatenate them into one dataframes (`allSlang_df`), and uploads them to the SQLite database (`ChineseSlangWords.db`).

#### Search 

To start the search engine, run the following command:

```
python Slang_search.py
```


## 2. Project 2 - TextRank

This is a short program built upon textrank4zh package and I am still developing new features for analyzing texts.

### 2.1 Run project

```
python textRank.py
#python3 textRank.py
```
