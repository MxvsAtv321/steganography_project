from PIL import Image
import numpy as np
import sys
import os

def encode_data(image_path, data_path, output_path):
    try:
        #Loading the image
        image = Image.open(image_path)
        image_data = np.array(image)
        
        #Reading the binary data 
        with open(data_path, 'rb') as file:
            binary_data = file.read()
        
        #Converting binary data to bit stream
        data_bits = ''.join([format(byte, '08b') for byte in binary_data])
        #Adding a delimiter to mark the end of the data
        delimiter = '00000000' * 10  #delimiter=10 bytes of zero
        data_bits += delimiter
        
        #Making sure that the data can fit in the image
        max_bytes = image_data.size // 8
        if len(data_bits) > max_bytes:
            raise ValueError("Data is too large to fit in the image.")
        
        #Encoding data bits into the image
        data_index = 0
        for i in range(image_data.shape[0]):
            for j in range(image_data.shape[1]):
                for k in range(image_data.shape[2]):
                    if data_index < len(data_bits):
                        image_data[i, j, k] = (image_data[i, j, k] & ~1) | int(data_bits[data_index])
                        data_index += 1
        
        #Saving the modified image
        encoded_image = Image.fromarray(image_data)
        encoded_image.save(output_path)
        print(f"Data encoded into {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decode_data(image_path, output_path):
    try:
        #Loading the image
        image = Image.open(image_path)
        image_data = np.array(image)
        
        #Extracting data bits from the image
        data_bits = []
        for i in range(image_data.shape[0]):
            for j in range(image_data.shape[1]):
                for k in range(image_data.shape[2]):
                    data_bits.append(image_data[i, j, k] & 1)
        
        #Converting bits to bytes
        data_bytes = bytearray()
        for i in range(0, len(data_bits), 8):
            byte = data_bits[i:i+8]
            byte_str = ''.join(map(str, byte))
            data_bytes.append(int(byte_str, 2))
        
        #Finding the delimiter to mark the end of the data
        delimiter = bytearray([0] * 10)
        end_index = data_bytes.find(delimiter)
        if end_index != -1:
            data_bytes = data_bytes[:end_index]
        
        #Writing the binary data to the output file
        with open(output_path, 'wb') as file:
            file.write(data_bytes)
        
        print(f"Data decoded into {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python steganography.py <encode/decode> <arguments>")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "encode":
        if len(sys.argv) != 5:
            print("Usage: python steganography.py encode <input_image> <data_file> <output_image>")
            sys.exit(1)
        
        input_image = sys.argv[2]
        data_file = sys.argv[3]
        output_image = sys.argv[4]

        if not os.path.isfile(input_image):
            print(f"Error: Input image '{input_image}' does not exist.")
            sys.exit(1)
        
        if not input_image.lower().endswith(('.png', '.bmp', '.tiff', '.jpeg', '.jpg')):
            print(f"Error: Unsupported image format. Supported formats: PNG, BMP, TIFF, JPEG")
            sys.exit(1)
        
        encode_data(input_image, data_file, output_image)
    
    elif command == "decode":
        if len(sys.argv) != 4:
            print("Usage: python steganography.py decode <input_image> <output_file>")
            sys.exit(1)
        
        input_image = sys.argv[2]
        output_file = sys.argv[3]

        if not os.path.isfile(input_image):
            print(f"Error: Input image '{input_image}' does not exist.")
            sys.exit(1)
        
        if not input_image.lower().endswith(('.png', '.bmp', '.tiff', '.jpeg', '.jpg')):
            print(f"Error: Unsupported image format. Supported formats: PNG, BMP, TIFF, JPEG")
            sys.exit(1)

        decode_data(input_image, output_file)
    
    else:
        print("Invalid command. Use 'encode' or 'decode'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
