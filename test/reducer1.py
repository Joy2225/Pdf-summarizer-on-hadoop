#!/usr/bin/env python3
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import sys
import re
import nltk
#nltk.download('punkt_tab')
#nltk.download('stopwords')
nltk.data.path.append('/user/joy/nltk_data')
nltk.data.path.append('/home/joy/nltk_data/')
def summarize(text):
    # Process text by removing numbers and unrecognized punctuation
    processedText = re.sub("’", "'", text)
    processedText = re.sub("[^a-zA-Z' ]+", " ", processedText)
    stopWords = {"needn't", 'be', 'his', 'all', 'under', 'which', "haven't", 'won', 'you', "couldn't", 'then', 'between', 'having', 'll', 'yourselves', 'or', 'down', 'don', 'theirs', 's', 'what', 'because', 'am', 'their', 'against', "it's", 'my', 'why', 'had', 'couldn', 'your', 'was', 'here', 'with', 'out', 'should', 'about', 'them', 'too', 'been', "you've", 'most', 'ain', "you'd", 'm', 'before', "hadn't", 'needn', 'other', 'doesn', 'very', 'are', "mustn't", 'that', 'ours', 'didn', 'mightn', "didn't", 'i', 'but', 'is', 'in', 'to', 'such', 'so', 'no', "aren't", 'into', 'when', 'will', 'wouldn', 'if', 'own', "you'll", 'who', 'aren', 'have', 'we', 'by', 'where', 'during', 'its', 'now', 'than', "weren't", 'she', 'and', 'below', 'being', 'ourselves', 'haven', 'can', 'both', 'they', 'he', 'doing', 'only', 'herself', 'itself', 'each', 'hadn', 'weren', 'isn', "mightn't", 'more', 'shouldn', 'how', 'nor', "you're", 'were', 'from', "should've", 'of', 'wasn', 'a', 'her', 'until', 'him', 'hers', 'again', 'o', "isn't", 'those', 'yourself', "hasn't", "wouldn't", 'hasn', 't', 'any', 'shan', 'this', "she's", 'just', 'yours', 'the', 'd', 'few', 've', 'an', 'further', 'myself', "that'll", 'for', "shouldn't", 'above', 'whom', 'not', 'same', 'does', 'y', 'it', 're', 'through', 'while', 'after', "doesn't", 'mustn', "won't", 'some', 'once', 'himself', 'at', 'as', 'our', 'over', "don't", "shan't", 'has', 'do', 'ma', 'on', 'these', 'did', 'there', 'off', 'me', 'up', 'themselves', "wasn't"}


    words = word_tokenize(processedText)

    # Normalize words with Porter stemming and build word frequency table
    stemmer = SnowballStemmer("english", ignore_stopwords=True)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        elif stemmer.stem(word) in freqTable:
            freqTable[stemmer.stem(word)] += 1
        else:
            freqTable[stemmer.stem(word)] = 1

    # Normalize every sentence in the text
    sentences = sent_tokenize(text)
    stemmedSentences = []
    sentenceValue = dict()
    for sentence in sentences:
        stemmedSentence = []
        for word in sentence.lower().split():
            stemmedSentence.append(stemmer.stem(word))
        stemmedSentences.append(stemmedSentence)

    # Calculate value of every normalized sentence based on word frequency table
    # [:12] helps to save space
    for num in range(len(stemmedSentences)):
        for wordValue in freqTable:
            if wordValue in stemmedSentences[num]:
                if sentences[num][:12] in sentenceValue:
                    sentenceValue[sentences[num][:12]] += freqTable.get(wordValue)
                else:
                    sentenceValue[sentences[num][:12]] = freqTable.get(wordValue)

    # Determine average value of a sentence in the text
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue.get(sentence)

    average = int(sumValues / len(sentenceValue))

    # Create summary of text using sentences that exceed the average value by some factor
    # This factor can be adjusted to reduce/expand the length of the summary
    summary = ""
    for sentence in sentences:
            if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (3.0 * average):
                summary += " " + " ".join(sentence.split())

    # Process the text in summary and write it to a new file
    summary = re.sub("’", "'", summary)
    summary = re.sub("[^a-zA-Z0-9'\"():;,.!?— ]+", " ", summary)
    return summary





total=''
for line in sys.stdin:
    total+=line

lines = total.strip().split("\n")

# Extract filename, line number, and content
parsed_lines = []
pattern = re.compile(r"(hdfs://.+?\.pdf)\s+# Line (\d+)(.*)")

for line in lines:
    match = pattern.match(line)
    if match:
        filename = match.group(1)
        line_number = int(match.group(2))
        content = match.group(3).strip()
        parsed_lines.append((filename, line_number, content))

# Sort by filename and line number
parsed_lines.sort(key=lambda x: (x[0], x[1]))

# Concatenate content by filename
file_content_dict = {}

for filename, _, content in parsed_lines:
    if filename not in file_content_dict:
        file_content_dict[filename] = content
    else:
        file_content_dict[filename] += (" " + content) if content else ""

# Output the concatenated result
for filename, content in file_content_dict.items():
    summary = summarize(content)
    file_content_dict[filename] = summary
print(file_content_dict)
