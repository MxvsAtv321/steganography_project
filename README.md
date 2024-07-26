# steganography_project

# Steganography Project

This project focuses on
implementing a steganography tool using Python, which can encode and decode
hidden data (including text, files, and images) within cover images.

## Primary Objectives

The primary objective of this project is to develop a Python-based tool that
leverages the Least Significant Bit (LSB) method for steganography. The tool will
allow users to embed various types of data (text, files, images) within a cover
image and subsequently extract the hidden data. The key goals of this project
include:

1. Implementing the LSB steganography algorithm.
2. Ensuring the integrity and quality of the cover image while embedding the
secret image.
3. Providing a user-friendly command-line interface for encoding and decoding
operations.
4. Handling various image formats and ensuring compatibility.

## Methodology

The project employs the Least Significant Bit (LSB) technique, one of the simplest
yet effective methods for image steganography. This technique involves modifying
the least significant bits of the pixel values in the cover image to encode the bits
of the secret image. Given that the changes in the least significant bits are
imperceptible to the human eye, the cover image appears virtually unchanged.

## Project Structure

- `steganography.py`: The main Python script that performs the embedding.
- `images/`: Directory containing input images (`cover_image.png` and `secret_image.png`).
- `output/`: Directory where the output image (`output_image.png`) will be saved.

## Usage

### Encoding an Image

To embed a secret image within a cover image, use the encode command
followed by the paths to the cover image, secret image, and the output image.

```bash
python steganography.py encode images/cover_image.png images/secret_image.png output/output_image.png
```
### Decoding an Image

To extract the hidden image from an encoded image, use the decode command
followed by the paths to the encoded image and the output path for the extracted
image.

```bash
python steganography.py decode output/output_image.png output/extracted_secret_image.png 

