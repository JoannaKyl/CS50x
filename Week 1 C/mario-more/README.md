# CS50x - Week 1C: Mario (More Comfortable)

## Problem to Solve

In this assignment, we’ll recreate the classic Super Mario Brothers pyramid structure in the terminal, using hashes (`#`) to represent bricks. The task simulates Mario’s jump over adjacent pyramids at the start of World 1-1, where he must leap over a series of pyramid blocks.

### Program Requirements

1. **Pyramid Layout**:
   - The pyramid should align left and right structures separated by a two-hash (`# #`) gap.
   - Each pyramid grows in height with each row, matching user-defined input.

2. **User Input**:
   - The program prompts the user to enter the height of the pyramids, with values allowed between `1` and `8` only.
   - If an invalid input is provided, the program will reprompt the user for a valid height.

3. **Example Output**:

   For a height of `3`, the program would generate the following:
    
``` 
  #  #
 ##  ##
###  ###
```
