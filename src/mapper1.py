#!/usr/bin/env python3

import os
import sys
from PyPDF2 import PdfReader

# Function to extract text from a PDF
def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Get the input file name
input_file = os.environ.get("map_input_file", "unknown_file")

# Process PDF file
try:
    text = extract_text(input_file)
    print(f"{input_file}\t{text}")
except Exception as e:
    print(f"Error processing {input_file}: {e}", file=sys.stderr)