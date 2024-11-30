import os
import requests
from pymongo import MongoClient
import requests

def download_pdf_from_drive(drive_url, output_file):
    try:
        # Extract the FILE_ID from the Drive URL
        file_id = drive_url.split('/')[5]
        download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
        
        # Send a GET request to the download URL
        response = requests.get(download_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Save the content to the output file
        with open(output_file, 'wb') as file:
            file.write(response.content)
        
        print(f"Downloaded successfully: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

# MongoDB connection string
client = MongoClient('mongodb+srv://lamelegend:123@bdaproject.lb73a.mongodb.net/')

# Select the database and collection
db = client['BDA']
collection = db['test']  # Assuming your collection is named 'links'

# Create the 'input' directory if it doesn't exist
if not os.path.exists('input1'):
    os.makedirs('input1')

# Fetch all documents from the collection
documents = collection.find()

# Loop through each document and download the PDF
for idx, doc in enumerate(documents, start=1):
    # Assuming the field with the PDF link is named 'url'
    pdf_url = doc.get('url')
    name = doc.get('name')
    file_path = os.path.join('input1', name)

    if pdf_url:
        try:
            download_pdf_from_drive(pdf_url, file_path)
        except Exception as e:
            print(f"Error downloading {pdf_url}: {e}")

print("PDF download process completed.")
