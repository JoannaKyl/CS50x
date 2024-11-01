# CS50x - Week 1: Credit

## Problem to Solve

 Credit(Debit) card has a unique number stored in a database, which is used to identify the cardholder when a purchase is made. Different card companies have different card number formats: 

- American Express uses 15-digit numbers.
- MasterCard uses 16-digit numbers.
- Visa uses both 13- and 16-digit numbers.

This project involves creating a program that checks the validity of a given credit card number using the Luhn algorithm.

## Luhn’s Algorithm

Luhn's algorithm helps determine if a credit card number is syntactically valid. The algorithm involves the following steps:

1. Multiply every other digit by 2, starting with the second-to-last digit.
2. Add the digits of the products together.
3. Add this sum to the sum of the digits that weren’t multiplied by 2.
4. If the total modulo 10 is equal to 0, the number is valid.

### Example

For the credit card number `4003600000000014`, the steps would be:

- Underlined digits: `4003600000000014`
- Products: `2 + 0 + 0 + 0 + 0 + 12 + 0 + 8`
- Sum of products' digits: `2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13`
- Total sum: `13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20`

Since the last digit of the total sum (20) is 0, the card is valid.

## Implementation Details

The implementation involves creating a program in C, stored in `credit.c`, that:

- Prompts the user for a credit card number.
- Validates the card number using Luhn's algorithm.
- Determines the card type (American Express, MasterCard, or Visa) based on the number's format.
- Outputs the result as `AMEX`, `MASTERCARD`, `VISA`, or `INVALID`.

### Input and Output

The program should behave as follows:
``` 
$ ./credit
Number: 4003600000000014
VISA
```

### Constraints

- User input will be entirely numeric (no hyphens).
- The input will not have leading zeroes.

## Credit

This project was developed as part of Harvard University's CS50x course. For more information, you can visit the official project page: [CS50 Credit Problem Set](https://cs50.harvard.edu/x/2024/psets/1/credit/).

**Note:** This repository contains my personal projects and files from Harvard University's CS50x course. If you’re currently enrolled, please respect academic integrity and complete assignments independently.

