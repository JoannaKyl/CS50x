# CS50x - Week 6: DNA
 
## Problem to Solve
DNA carriers of genetic information. 
This program aims to demonstrate how DNA profiling works and how forensic investigators can identify individuals based on DNA sequences.
It takes a sequence of DNA and compares it to a database of individuals, identifying the most likely owner of the DNA sequence.

### Download the Distribution Code
Download the Distribution Code in [CS50 DNA Problem Set](https://cs50.harvard.edu/x/2024/psets/6/dna/).

### Example DNA Database Format
A simple representation of a DNA database could be structured as a CSV file, where each row corresponds to an individual, and each column corresponds to a particular STR:
'''
name,AGAT,AATG,TATC
Alice,28,42,14 
Bob,17,22,19 
Charlie,36,18,25
'''
In above example:
- **Alice** has the STR **AGAT** repeated **28 times**, **AATG** repeated **42 times**, and **TATC** repeated **14 times**.
- **Bob** has the STRs **AGAT**, **AATG**, and **TATC** repeated **17**, **22**, and **19 times**, respectively.
- **Charlie** has **36**, **18**, and **25** repeats for the same STRs, respectively.

Given a DNA sequence, the program will determine which individual’s STR profile matches the longest consecutive sequences found in the DNA.

### Implementation and Example Usage

```
python dna.py databases/small.csv sequences/1.txt
Output:Bob
```
```
python dna.py databases/large.csv sequences/20.txt
Output:No match
```
## Credit
This project is part of Harvard's CS50x course. For more details, visit: [CS50 DNA Problem Set](https://cs50.harvard.edu/x/2024/psets/6/dna/).
