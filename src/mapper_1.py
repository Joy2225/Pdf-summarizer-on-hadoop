#!/usr/bin/env python3

import os
import sys
import string

# Function to extract text from a PDF
from PyPDF2 import PdfReader

# Function to extract text from a PDF
def extractText(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Specify the directory containing the PDF files
pdf_directory = "../tests"  # Change this to the path of your local folder

# List all PDF files in the directory
try:
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]
    if not pdf_files:
        print(f"No PDF files found in {pdf_directory}", file=sys.stderr)
    
    for pdf_file in pdf_files:
        input_file = os.path.join(pdf_directory, pdf_file)
        # print("Hiiiiii")
        try:
            text = extractText(input_file).encode()
            # Decode to a string, filter, and re-encode
#             valid_bytes = set(string.printable.encode())
#             print(valid_bytes)
#             text = b''.join(
#     b'0' + str(i).encode() if i < 10 else bytes([i])  # Prepend 0 for ASCII values < 10
#     for i in text
#     if i in valid_bytes
# )

            input_file = input_file.encode()
            with open("aaaa.txt", 'wb') as f:
                f.write(input_file+b"\t"+text)
            # print(f"{input_file}\t{text}")
        except Exception as e:
            print(f"Error processing {input_file}: {e}", file=sys.stderr)

except Exception as e:
    print(f"Error accessing directory {pdf_directory}: {e}", file=sys.stderr)



# for line in sys.stdin:
#     # line = line.strip()
#     # file_name, text = line.split("\t", 1)
#     # summary = summarize(text)
#     print(line)