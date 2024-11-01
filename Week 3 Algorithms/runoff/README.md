# CS50x - Week 3: Runoff 

## Problem to Solve

In previous plurality elections, voters cast a single vote for their preferred candidate, which can lead to ties or results that don’t reflect the voters' true preferences. For example, in an election with three candidates, a tie may occur between two candidates, leaving the election unresolved.

### Ranked-Choice Voting
To address the limitations of plurality voting, ranked-choice voting allows voters to rank candidates by preference. In this system, if no candidate receives a majority (over 50%) of first-choice votes, the candidate with the fewest votes is eliminated, and their voters' next preferences are considered in an "instant runoff." This process continues until a candidate secures a majority.

### Implementation and Example Usage

This programs simulate a runoff election. Here’s how it should work:

``` 
$ ./runoff Alice Bob Charlie                                                                        
Number of voters: 3                                                                                 
Rank 1: Alice                                                                                       
Rank 2: Bob                                                                                         
Rank 3: Charlie  

Rank 1: Bob                                                                                         
Rank 2: Alice                                                                                       
Rank 3: Charlie

Rank 1: Bob                                                                                         
Rank 2: Alice                                                                                       
Rank 3: Charlie                                                                                     
                                                                                                    
Rank 1: Alice                                                                                       
Rank 2: Bob                                                                                         
Rank 3: Charlie                                                                                     
                                                                                                    
Alice          
```
```
$ ./runoff Alice Bob Charlie                                                                        
Number of voters: 3                                                                                 
Rank 1: David                                                                                       
Invalid vote. 
```
 
## Credit
This project is part of Harvard's CS50x course. For more details, visit: [CS50 Runoff Voting](https://cs50.harvard.edu/x/2024/psets/3/runoff/).

**Note:** This repository contains my personal projects and files from Harvard University's CS50x course. If you’re currently enrolled, please respect academic integrity and complete assignments independently.

