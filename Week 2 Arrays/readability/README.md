# CS50x - Week 2: Readability

## Problem to Solve

According to Scholastic, E.B. White’s *Charlotte’s Web* is considered to be between a second- and fourth-grade reading level, while Lois Lowry’s *The Giver* ranges from an eighth- to twelfth-grade reading level. But how is the reading level of a book determined?

While human experts can assess a book's appropriateness for different grades, an algorithm can also compute the reading level based on text analysis.

This project is a program in C, stored in `readability.c`, which calculates the approximate grade level required to comprehend a given text. The program should output the grade level as follows:

- Output “Grade X” where “X” is the computed grade level rounded to the nearest integer.
- If the grade level is 16 or higher, output “Grade 16+”.
- If the grade level is less than 1, output “Before Grade 1”.

## Implementation Details

The program analyze :

1. The total number of letters.
2. The total number of words.
3. The total number of sentences.

Using these metrics, you can apply the Coleman-Liau index formula to calculate the grade level.

### Example Output
``` 
$ ./readability 
Text: One fish. Two fish.Red fish.Blue fish. 
Before Grade 1
```

### Constraints

- The program can handle a variety of text inputs, including punctuation and multiple spaces.

## Credit

This project was developed as part of Harvard University's CS50x course. For more information, you can visit the official project page: [CS50 Readability Problem Set](https://cs50.harvard.edu/x/2024/psets/2/readability/).

**Note:** This repository contains my personal projects and files from Harvard University's CS50x course. If you’re currently enrolled, please respect academic integrity and complete assignments independently.
