import os
import sys

def rle_compress(input_path, output_path):
    try:
        with open(input_path, 'rb') as f:
            data = f.read()
        
        if not data:
            print("Error: Input file is empty.")
            return

        compressed = bytearray()
        i = 0
        while i < len(data):
            run_byte = data[i]
            run_length = 1
            
            while i + 1 < len(data) and data[i + 1] == run_byte and run_length < 255:
                run_length += 1
                i += 1
            
            compressed.append(run_length)
            compressed.append(run_byte)
            i += 1

        with open(output_path, 'wb') as f:
            f.write(compressed)
            
        print(f"Successfully compressed to {output_path}")
        print(f"Original size: {len(data)} bytes | Compressed size: {len(compressed)} bytes")

    except FileNotFoundError:
        print("Error: The specified file was not found.")

def rle_decompress(input_path, output_path):
    try:
        with open(input_path, 'rb') as f:
            data = f.read()

        if not data or len(data) % 2 != 0:
            print("Error: Invalid or corrupted compressed file.")
            return

        decompressed = bytearray()
        for i in range(0, len(data), 2):
            run_length = data[i]
            run_byte = data[i+1]
            decompressed.extend([run_byte] * run_length)

        with open(output_path, 'wb') as f:
            f.write(decompressed)
            
        print(f"Successfully decompressed to {output_path}")
        print(f"Decompressed size: {len(decompressed)} bytes")

    except FileNotFoundError:
        print("Error: The specified file was not found.")

def main():
    print("=== Python File Zipper (RLE) ===")
    action = input("Choose action (1: Compress, 2: Decompress): ").strip()
    
    if action not in ['1', '2']:
        print("Invalid choice. Exiting.")
        return
        
    input_file = input("Enter source file path: ").strip()
    output_file = input("Enter destination file path: ").strip()

    if action == '1':
        rle_compress(input_file, output_file)
    else:
        rle_decompress(input_file, output_file)

if __name__ == "__main__":
    main()
