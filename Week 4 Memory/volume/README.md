#  CS50x - Week 4: Volume

## Project Overview

The Volume program modifies the volume of a WAV audio file by scaling its samples based on a user-specified factor. This allows users to increase or decrease the audio's loudness as needed.

## Problem Statement

WAV files store audio data as a sequence of samples, each represented as a 16-bit integer. The program will read a WAV file, modify its volume by a specified scaling factor, and save the modified audio to a new file.

## Implementation Details and Example Usage

- **File Name**: `volume.c`
- **Directory**: `volume`
- **Input**: The program accepts three command-line arguments:
  1. `input.wav` - The original WAV file.
  2. `output.wav` - The name for the new WAV file to be created.
  3. `factor` - A floating-point number representing the volume scaling factor.

``` 
$ ./volume input.wav output.wav 2.0                                                                 
```
### Download Distribution Files

Make sure to download the necessary distribution files from the following link:

[CS50 Volume Problem Distribution](https://cs50.harvard.edu/x/2024/psets/4/volume/)

## Credit

This project was developed as part of Harvard University's CS50x course. For more details, visit:  [CS50 Volume Problem Distribution](https://cs50.harvard.edu/x/2024/psets/4/volume/)

**Note:** This repository contains my personal projects and files from Harvard University's CS50x course. If you’re currently enrolled, please respect academic integrity and complete assignments independently.
