#!/usr/bin/env python3

import sys
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
a=''''''
# Initialize NLTK components
stopwords_set = set(stopwords.words("english"))
stemmer = SnowballStemmer("english", ignore_stopwords=True)

# Function to summarize text
def summarize(text):
    # Preprocess text
    processed_text = re.sub("[^a-zA-Z' ]+", " ", text)
    words = word_tokenize(processed_text)
    
    # Build word frequency table
    freq_table = {}
    for word in words:
        word = word.lower()
        if word not in stopwords_set:
            stemmed_word = stemmer.stem(word)
            freq_table[stemmed_word] = freq_table.get(stemmed_word, 0) + 1

    # Normalize sentences
    sentences = sent_tokenize(text)
    sentence_values = {}
    for sentence in sentences:
        for word_value in freq_table:
            if word_value in sentence.lower():
                sentence_values[sentence] = sentence_values.get(sentence, 0) + freq_table[word_value]

    # Calculate average sentence value
    average_value = sum(sentence_values.values()) / len(sentence_values)

    # Create summary
    summary = " ".join(sentence for sentence in sentences if sentence_values.get(sentence, 0) > 1.5 * average_value)
    return summary
    # processed_text = re.sub("[^a-zA-Z' ]+", " ", text)
    # words = word_tokenize(processed_text)
    # stopWords = {"needn't", 'be', 'his', 'all', 'under', 'which', "haven't", 'won', 'you', "couldn't", 'then', 'between', 'having', 'll', 'yourselves', 'or', 'down', 'don', 'theirs', 's', 'what', 'because', 'am', 'their', 'against', "it's", 'my', 'why', 'had', 'couldn', 'your', 'was', 'here', 'with', 'out', 'should', 'about', 'them', 'too', 'been', "you've", 'most', 'ain', "you'd", 'm', 'before', "hadn't", 'needn', 'other', 'doesn', 'very', 'are', "mustn't", 'that', 'ours', 'didn', 'mightn', "didn't", 'i', 'but', 'is', 'in', 'to', 'such', 'so', 'no', "aren't", 'into', 'when', 'will', 'wouldn', 'if', 'own', "you'll", 'who', 'aren', 'have', 'we', 'by', 'where', 'during', 'its', 'now', 'than', "weren't", 'she', 'and', 'below', 'being', 'ourselves', 'haven', 'can', 'both', 'they', 'he', 'doing', 'only', 'herself', 'itself', 'each', 'hadn', 'weren', 'isn', "mightn't", 'more', 'shouldn', 'how', 'nor', "you're", 'were', 'from', "should've", 'of', 'wasn', 'a', 'her', 'until', 'him', 'hers', 'again', 'o', "isn't", 'those', 'yourself', "hasn't", "wouldn't", 'hasn', 't', 'any', 'shan', 'this', "she's", 'just', 'yours', 'the', 'd', 'few', 've', 'an', 'further', 'myself', "that'll", 'for', "shouldn't", 'above', 'whom', 'not', 'same', 'does', 'y', 'it', 're', 'through', 'while', 'after', "doesn't", 'mustn', "won't", 'some', 'once', 'himself', 'at', 'as', 'our', 'over', "don't", "shan't", 'has', 'do', 'ma', 'on', 'these', 'did', 'there', 'off', 'me', 'up', 'themselves', "wasn't"}

    # stemmer = SnowballStemmer("english", ignore_stopwords=True)
    # freqTable = dict()
    # for word in words:
    #     word = word.lower()
    #     if word in stopWords:
    #         continue
    #     elif stemmer.stem(word) in freqTable:
    #         freqTable[stemmer.stem(word)] += 1
    #     else:
    #         freqTable[stemmer.stem(word)] = 1

    # # Normalize every sentence in the text
    # sentences = sent_tokenize(text)
    # stemmedSentences = []
    # sentenceValue = dict()
    # for sentence in sentences:
    #     stemmedSentence = []
    #     for word in sentence.lower().split():
    #         stemmedSentence.append(stemmer.stem(word))
    #     stemmedSentences.append(stemmedSentence)

    # # Calculate value of every normalized sentence based on word frequency table
    # # [:12] helps to save space
    # for num in range(len(stemmedSentences)):
    #     for wordValue in freqTable:
    #         if wordValue in stemmedSentences[num]:
    #             if sentences[num][:12] in sentenceValue:
    #                 sentenceValue[sentences[num][:12]] += freqTable.get(wordValue)
    #             else:
    #                 sentenceValue[sentences[num][:12]] = freqTable.get(wordValue)

    # # Determine average value of a sentence in the text
    # sumValues = 0
    # for sentence in sentenceValue:
    #     sumValues += sentenceValue.get(sentence)

    # average = int(sumValues / len(sentenceValue))

    # # Create summary of text using sentences that exceed the average value by some factor
    # # This factor can be adjusted to reduce/expand the length of the summary
    # summary = ""
    # for sentence in sentences:
    #         if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (3.0 * average):
    #             summary += " " + " ".join(sentence.split())

    # # Process the text in summary and write it to a new file
    # summary = re.sub("’", "'", summary)
    # summary = re.sub("[^a-zA-Z0-9'\"():;,.!?— ]+", " ", summary)
    # return summary

# Process lines from stdin
for line in a:
    line = line.strip()
    file_name, text = line.split("\t", 1)
    summary = summarize(text)
    print(f"{file_name}\t{summary}")