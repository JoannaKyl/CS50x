# CS50x - Week 4: Filter

## Project Overview

This project focuses on implementing image filters for bitmap (BMP) images.

## Problem to Solve

Images can be represented as a bitmap (a map of bits), where each pixel can have a different color. This project manipulates the RGB values of individual pixels to create your own image filters.

## Distribution Code

- **bmp.h**: Contains definitions for bitmap headers and the RGBTRIPLE structure used to represent pixel colors.
- **filter.c**: Provides and contains the main logic for applying the filters.
- **helpers.h**: Contains function prototypes for the filtering functions.
- **helpers.c**: Implement the filtering functions.
- **Makefile**: Defines how to compile the project.

## Example Usage
 
``` 
$ make filter
$ ./filter -g ./images/courtyard.bmp ./images/courtyard-grayscale.bmp  
$ ./filter -r ./images/stadium.bmp ./images/stadium-reflected.bmp     
$ ./filter -b ./images/tower.bmp ./images/tower-blurred.bmp            
$ ./filter -e ./images/yard.bmp ./images/yard-edges.bmp                
```

## Credit

This project was developed as part of Harvard University's CS50x course. For more details, visit: [CS50 Filter Problem page](https://cs50.harvard.edu/x/2024/psets/4/filter/more/)

**Note:** This repository contains my personal projects and files from Harvard University's CS50x course. If you’re currently enrolled, please respect academic integrity and complete assignments independently.
