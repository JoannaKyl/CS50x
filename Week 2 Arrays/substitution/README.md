# CS50x - Week 2: Substitution Cipher

## Problem to Solve
In a substitution cipher, we encrypt messages by replacing letters according to a key. For example, with the key:
 ```Key:   N Q X P O M A F T R H L Z G E C Y J I U W S K D V B
Alphabet:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```
"HELLO" can encrypted as "FOLLE".

## Details
This C program encrypts messages using a user-provided key as a command-line argument.

### Specifications
- The program must accept one command-line argument (the key).
- The key :
  - Contain exactly 26 alphabetic characters.
  - Case-insensitive.
  - Have each letter appear exactly once.
- The program :
  - Invalid input should result in an error message and return 1.
  - Prompt the user for plaintext and output the ciphertext while preserving the case.

### Example Usage
```                                                                    
$ ./substitution ABC                                                                                
Key must contain 26 characters.                                                                     
```
``` 
$ ./substitution YTNSHKVEFXRBAUQZCLWDMIPGJO                                                         
plaintext:  Hello!                                                                                  
ciphertext: Ehbbq!
```

## Credit

This project is part of Harvard's CS50x course. For more details, visit: [CS50 Substitution Problem Set](https://cs50.harvard.edu/x/2024/psets/2/substitution/).

