#!/usr/bin/env python3
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import sys
import os
import nltk

file_name = os.environ.get('map_input_file', 'unknown_file')

total=''
# Process lines from stdin
for line in sys.stdin:
    total+=file_name+" "+line
print(total)
