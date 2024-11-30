#!/usr/bin/env python3
import time
import os
import nltk
import re
import slate3k as slate
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
nltk.download("stopwords")
nltk.download("punkt_tab")
import requests
from pymongo import MongoClient
import requests

# def download_pdf_from_drive(drive_url, output_file):
#     try:
#         # Extract the FILE_ID from the Drive URL
#         file_id = drive_url.split('/')[5]
#         download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
        
#         # Send a GET request to the download URL
#         response = requests.get(download_url)
#         response.raise_for_status()  # Raise an exception for HTTP errors

#         # Save the content to the output file
#         with open(output_file, 'wb') as file:
#             file.write(response.content)
        
#         print(f"Downloaded successfully: {output_file}")
#     except Exception as e:
#         print(f"Error: {e}")

# # MongoDB connection string
# client = MongoClient('mongodb+srv://lamelegend:123@bdaproject.lb73a.mongodb.net/')

# # Select the database and collection
# db = client['BDA']
# collection = db['test']  # Assuming your collection is named 'links'

# # Create the 'input' directory if it doesn't exist
# if not os.path.exists('input1'):
#     os.makedirs('input1')

# # Fetch all documents from the collection
# documents = collection.find()

# # Loop through each document and download the PDF
# for idx, doc in enumerate(documents, start=1):
#     # Assuming the field with the PDF link is named 'url'
#     pdf_url = doc.get('url')
#     name = doc.get('name')
#     file_path = os.path.join('input1', name)

#     if pdf_url:
#         try:
#             download_pdf_from_drive(pdf_url, file_path)
#         except Exception as e:
#             print(f"Error downloading {pdf_url}: {e}")

# print("PDF download process completed.")

def extractText(file):
    
    try:
        pdfFileObj = open(file, "rb")
        pdfPages = slate.PDF(pdfFileObj)

        # Extract text from PDF file
        text = ""
        for page in pdfPages:
            text += page
        with open("extractedtext/"+file[8:-4]+".pdf", "wb") as file:
            file.write(text.encode())
        
    except Exception as e:
        print(file)
        print(f"Error: {e}")
        return -1


def summarize(text):
    # Process text by removing numbers and unrecognized punctuation
    processedText = re.sub("’", "'", text)
    processedText = re.sub("[^a-zA-Z' ]+", " ", processedText)
    stopWords = {"needn't", 'be', 'his', 'all', 'under', 'which', "haven't", 'won', 'you', "couldn't", 'then', 'between', 'having', 'll', 'yourselves', 'or', 'down', 'don', 'theirs', 's', 'what', 'because', 'am', 'their', 'against', "it's", 'my', 'why', 'had', 'couldn', 'your', 'was', 'here', 'with', 'out', 'should', 'about', 'them', 'too', 'been', "you've", 'most', 'ain', "you'd", 'm', 'before', "hadn't", 'needn', 'other', 'doesn', 'very', 'are', "mustn't", 'that', 'ours', 'didn', 'mightn', "didn't", 'i', 'but', 'is', 'in', 'to', 'such', 'so', 'no', "aren't", 'into', 'when', 'will', 'wouldn', 'if', 'own', "you'll", 'who', 'aren', 'have', 'we', 'by', 'where', 'during', 'its', 'now', 'than', "weren't", 'she', 'and', 'below', 'being', 'ourselves', 'haven', 'can', 'both', 'they', 'he', 'doing', 'only', 'herself', 'itself', 'each', 'hadn', 'weren', 'isn', "mightn't", 'more', 'shouldn', 'how', 'nor', "you're", 'were', 'from', "should've", 'of', 'wasn', 'a', 'her', 'until', 'him', 'hers', 'again', 'o', "isn't", 'those', 'yourself', "hasn't", "wouldn't", 'hasn', 't', 'any', 'shan', 'this', "she's", 'just', 'yours', 'the', 'd', 'few', 've', 'an', 'further', 'myself', "that'll", 'for', "shouldn't", 'above', 'whom', 'not', 'same', 'does', 'y', 'it', 're', 'through', 'while', 'after', "doesn't", 'mustn', "won't", 'some', 'once', 'himself', 'at', 'as', 'our', 'over', "don't", "shan't", 'has', 'do', 'ma', 'on', 'these', 'did', 'there', 'off', 'me', 'up', 'themselves', "wasn't"}


    words = word_tokenize(processedText)
    # print(words)

    # stopWords = set(punkt_tab.words("english"))

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
    # print(summary)


total_time=0
# for i in os.listdir("input1"):
#     if i.endswith(".pdf"):
#         text = extractText("input1/" + i)
#         if text == -1:
#             continue

# start_total = time.time()
for i in os.listdir("extractedtext"):
    if i.endswith(".pdf"):
        with open("extractedtext/"+i, "rb") as file:
            text = file.read()
        text=text.decode(errors='ignore')
        start=time.time()
        summary = summarize(text)
        end = time.time()
        total_time+=end-start
        # print(total_time)
        with open("summary/"+i[:-4]+"_summary.txt", "w") as file:
            file.write(summary)

print("Total time taken for summarizing all the pdfs is: ", total_time)
# end_total = time.time()
# print("Total time taken for summarizing all the pdfs is: ", end_total-start_total)