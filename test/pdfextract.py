#!/usr/bin/env python3

import os
import sys
#from PyPDF2 import PdfReader
import slate3k as slate

# Function to extract text from a PDF
#def extractText(pdf_file):
#    reader = PdfReader(pdf_file)
#    text = ""
#    for page in reader.pages:
#        text += page.extract_text()
#    return text


def extractText(file):
    pdfFileObj = open(file, "rb")
    pdfPages = slate.PDF(pdfFileObj)

    # Extract text from PDF file
    text = ""
    for page in pdfPages:
        text += page
    return text

# Specify the directory containing the PDF files
pdf_directory = "input"  # Change this to the path of your local folder
output_directory = "extracted"  # Change this to the path of the output folder

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all PDF files in the directory
try:
    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith(".pdf")]
    if not pdf_files:
        print(f"No PDF files found in {pdf_directory}", file=sys.stderr)

    for pdf_file in pdf_files:
        input_file = os.path.join(pdf_directory, pdf_file)
        output_file = os.path.join(output_directory, os.path.splitext(pdf_file)[0].replace(" ","_") + ".pdf")  # Use the same name with .txt extension

        try:
            text = extractText(input_file)

            # Split the text into lines and add line numbers
            lines = text.splitlines()
            max_lines = len(lines)
            numbered_lines = [f"# Line {str(i+1).zfill(len(str(max_lines)))} {line}" for i, line in enumerate(lines)]

            # Write the extracted text with line numbers to a new text file with the same name as the PDF
            with open(output_file, 'wb') as f:
                f.write(b"\n".join(i.encode() for i in numbered_lines))

            print(f"Extracted text from {pdf_file} and saved to {output_file}")

        except Exception as e:
            print(f"Error processing {input_file}: {e}", file=sys.stderr)

except Exception as e:
    print(f"Error accessing directory {pdf_directory}: {e}", file=sys.stderr)
