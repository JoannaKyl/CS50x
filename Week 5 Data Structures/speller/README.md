# CS50x - Week 5: Speller

## Project Overview
The **Speller** implements a fast, efficient spell-checker using a hash table to quickly load, store, and retrieve words from a dictionary. 
This program is a solution to minimize the time required for loading, checking, sizing, and unloading operations.It can handle large dictionaries and texts.

## Problem Description

### Objective
- Implement a high-performance spell-checker that can quickly load a dictionary, check the spelling of words, and report statistics on runtime efficiency.

### Performance
- Design the program to be efficient in terms of real-world (wall-clock) time, as opposed to just theoretical (Big O) time.

## Program Structure

The project is structured across multiple files:

### `dictionary.h`
- Defines constants, includes necessary libraries, and prototypes functions that are implemented in `dictionary.c`.
- `LENGTH` is defined as 45, representing the maximum word length.
- Function Prototypes:
  - `bool check(const char *word)`: Checks if a word is in the dictionary.
  - `unsigned int hash(const char *word)`: Returns a hash value for a word.
  - `bool load(const char *dictionary)`: Loads the dictionary into memory.
  - `unsigned int size(void)`: Returns the total number of words in the dictionary.
  - `bool unload(void)`: Unloads the dictionary from memory.

### `dictionary.c`
- Defines a `struct node` for each entry in the hash table.
- Implements `check`, `hash`, `load`, `size`, and `unload` functions, which you must optimize to reduce execution time.
- Contains a `table` array representing the hash table, set to an initial size (`N`) of 26 but adjustable based on the hash function.

### `speller.c`
- Provides the main functionality and spell-check logic but does not require modification.
- Loads words from a dictionary into memory, checks text files word-by-word, and reports spelling errors and runtime statistics.

### `Makefile`
- Automates compilation of the project, specifying dependencies and rules to compile `speller`.

### `texts/`
- Contains text files for testing, including `grimm.txt`, `federalist.txt`, and others.

---

## Example Usage and Output

```
$ ./speller dictionaries/large texts/grimm.txt
```
````
...
...
WORDS MISSPELLED:     718                                                                           
WORDS IN DICTIONARY:  143091                                                                        
WORDS IN TEXT:        103614                                                                        
TIME IN load:         0.05                                                                          
TIME IN check:        0.09                                                                          
TIME IN size:         0.00                                                                          
TIME IN unload:       0.01                                                                          
TIME IN TOTAL:        0.15  
````
## Credit

This project was developed as part of Harvard University's CS50x course. For more details, visit:  [CS50 Speller Problem Set](https://cs50.harvard.edu/x/2024/psets/5/speller/#speller).

**Note:** This repository contains my personal projects and files from Harvard University's CS50x course. If you’re currently enrolled, please respect academic integrity and complete assignments independently.
