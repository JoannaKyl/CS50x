# CS50x - Week 4: Recovery

## Project Overview
This project aims to recover JPEG images from a forensic image file (`card.raw`) of a memory card from which photos were deleted. The recovery program detects JPEG signatures and reconstructs the lost images.

## Background

JPEG files begin with the following byte sequence:
- `0xff 0xd8 0xff` followed by `0xe0` to `0xef`.

The program reads the forensic image in blocks of 512 bytes, looking for JPEG signatures. Once found, it opens a new file to store the image data until another signature is encountered.

## Implementation Details

- **File Name**: `recover.c`
- **Directory**: `recover`
- **Input**: The program accepts a command-line argument specifying the forensic image file.

### Example Usage
```
./recover card.raw
```

## Credit

This project was developed as part of Harvard University's CS50x course. For more details, visit:  [CS50 Recover Problem Set](https://cs50.harvard.edu/x/2024/psets/4/recover/).

**Note:** This repository contains my personal projects and files from Harvard University's CS50x course. If you’re currently enrolled, please respect academic integrity and complete assignments independently.
