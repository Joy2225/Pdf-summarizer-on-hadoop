


import os
import re

# Function to read the dictionary from a text file and convert it to a dictionary
def read_dict_from_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Remove the curly braces and extra spaces
    file_content = file_content.strip('{}').strip()

    # Define a regex pattern to capture the key-value pairs (path and content)
    pattern = r"'([^']+)'\s*:\s*\"([^\"]+)\""
    
    # Find all matches based on the pattern
    matches = re.findall(pattern, file_content)
    
    # Convert matches into a dictionary
    content_dict = {match[0]: match[1] for match in matches}
    
    return content_dict

# Path to the input text file
input_file_path = 'a.txt'

# Read the dictionary from the file
pdf_content_dict = read_dict_from_file(input_file_path)

# Loop through the dictionary and create summary files
for pdf_path, content in pdf_content_dict.items():
    # Extract the PDF file name from the path
    pdf_name = os.path.basename(pdf_path).replace('.pdf', '')  # Remove ".pdf" extension
    summary_file_name = f"{pdf_name}_summary.txt"
    
    # Write the content to a summary file
    with open(summary_file_name, 'w') as file:
        file.write(content)

    print(f"Summary file '{summary_file_name}' created with content.")
