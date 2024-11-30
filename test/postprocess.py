#!/usr/bin/env python3

import os
import re

# Directory where Hadoop output files are stored
output_dir = "output"

# Combined output file from Hadoop
hadoop_output_file = os.path.join(output_dir, "part-00000")  # Adjust for multiple parts if needed

# Check if output xists
if not os.path.exists(hadoop_output_file):
    print(f"Error: Hadoop output file '{hadoop_output_file}' not found.")
    exit(1)

# Dictionary to store file-specific data
file_map = {}

# Function to read the dictionary from a text file

pdf_content_dict = eval(open(hadoop_output_file).read())


# Loop through the dictionary and create summary files
for pdf_path, content in pdf_content_dict.items():
    # Extract the PDF file name from the path
    pdf_name = os.path.basename(pdf_path[37:]).replace('.pdf', '')  # Remove ".pdf" extension
    summary_file_name = f"{pdf_name}_summary.txt"
    
    # Write the content to a summary file
    with open(output_dir+"/"+summary_file_name, 'w') as file:
        file.write(content)

    print(f"Summary file '{summary_file_name}' created with content.")
