# CS50x - Week 2: Scrabble

## Problem to Solve

In Scrabble, players create words to score points based on the individual letter values assigned to each letter in the English alphabet:

| Letter | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Points | 1 | 3 | 3 | 2 | 1 | 4 | 2 | 4 | 1 | 8 | 5 | 1 | 3 | 1 | 1 | 3 | 10| 1 | 1 | 1 | 1 | 4 | 4 | 8 | 4 | 10|

For example, the word "CODE" scores as follows:
- C = 3 points
- O = 1 point
- D = 2 points
- E = 1 point

Summing these, "CODE" is worth 7 points.

This c program determines the winner of a Scrabble-like game. It prompts each player to input their word and then calculate the scores to declare the winner. Depending on the scores, the program should print:
- “Player 1 wins!”
- “Player 2 wins!”
- “Tie!” 

## Implementation Details and Example Output
``` 
$ ./scrabble
Player 1: Question? 
Player 2: Question!
Tie!
```
``` 
$ ./scrabble
Player 1: red 
Player 2: wheelbarrow 
Player 2 wins!
```
``` 
$ ./scrabble
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```
## Credit

This project was developed as part of Harvard University's CS50x course. For more information, you can visit the official project page: [CS50 Scrabble Problem Set](https://cs50.harvard.edu/x/2024/psets/2/scrabble/).
