# CS50x - Week 3: Plurality

## Problem to Solve

Elections can vary, but one simple method is the **plurality vote** (or **first-past-the-post**). In this system, each voter selects one candidate, and the candidate with the most votes wins.

### Implementation and Example Usage

This program simulates a plurality election. Here’s how it should work:

``` 
$ ./plurality Alice Bob Charlie                                                                     
Number of voters: 3                                                                                 
Vote: Alice                                                                                         
Vote: Alice                                                                                         
Vote: Bob                                                                                           
Alice 
```
``` 
$ ./plurality Alice Bob Charlie                                                                     
Number of voters: 3                                                                                 
Vote: David                                                                                         
Invalid vote.                                                                                       
Vote: Alice                                                                                         
Vote: Alice                                                                                         
Alice         
```

## Credit

This project is part of Harvard's CS50x course. For more details, visit: [CS50 Substitution Problem Set](https://cs50.harvard.edu/x/2024/psets/2/substitution/).
