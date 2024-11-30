#!/usr/bin/env python3

import os

# Directory where Hadoop output files are stored
output_dir = "output"
hadoop_output_file = os.path.join(output_dir, "part-00000")  # Adjust for multiple parts if needed

# Check if output exists
if not os.path.exists(hadoop_output_file):
    print(f"Error: Hadoop output file '{hadoop_output_file}' not found.")
    exit(1)

# Dictionary to store summaries by file name
file_map = {}

# Read Hadoop output and group by input file names
with open(hadoop_output_file, "r") as infile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        file_name, summary = line.split("\t", 1)
        file_map[file_name] = summary

# Write summaries into separate files
for file_name, summary in file_map.items():
    output_file_name = os.path.basename(file_name) + "_summary.txt"
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, "w") as outfile:
        outfile.write(summary)

    print(f"Created output file: {output_file_path}")
