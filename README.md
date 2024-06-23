# steganography_project

# Steganography Project

This project demonstrates how to use steganography to embed one image within another image using Python.

## Project Structure

- `steganography.py`: The main Python script that performs the embedding.
- `images/`: Directory containing input images (`cover_image.png` and `secret_image.png`).
- `output/`: Directory where the output image (`output_image.png`) will be saved.

## Usage

### Encoding an Image

To embed a secret image into a cover image, run the following command:

```bash
python steganography.py encode images/cover_image.png images/secret_image.png output/output_image.png
