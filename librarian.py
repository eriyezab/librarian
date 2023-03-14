# server that listens to text messages and reacts to them

import sys
import os
import requests
import smtplib
#import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# global variables
from_email = os.environ.get("EMAIL_ADDRESS")
from_password = os.environ.get("EMAIL_PASSWORD")
to_kindle_email = os.environ.get("KINDLE_EMAIL")
#s3 = boto3.client('s3')

#bucket_name = "erizza-bucket-librarian-1"

"""
Given a text input, search on libgen for epub files and return a list of
the 3 most relavent results sorted by file size.
"""
def find_epub(title: str):
    results = []
    return results

"""
Download the epub.
"""
def download_epub(url):
    try:
        response = requests.get(url)
    except:
        return ''
    filename = response.headers.get('Content-Disposition').split('"')[1]
    if response.status_code == 200:
        #s3.put_object(Bucket=bucket_name, Key=filename, Body=response.content)
        print(f"{filename} found!")
        return filename, response.content
    else:
        print("Error downloading file")
        return '', None


def send_to_kindle(filename, file_data):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_kindle_email
    msg['Subject'] = ''

    # Attach the epub file
    epub_attachment = MIMEApplication(file_data, _subtype='epub')
    epub_attachment.add_header(
        'Content-Disposition', 'attachment', filename=f"{filename}")
    msg.attach(epub_attachment)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_kindle_email, msg.as_string())
        print(f"Sent {filename} to {to_kindle_email} successfully!")

if __name__ == "__main__":
    # print(find_epub("80 20 principle"))
    # link = "http://62.182.86.140/main/842000/8ece5c5ea1259bc706a12c2f1ec71206/Richard%20Koch%20-%20The%2080_20%20Principle_%20The%20Secret%20to%20Achieving%20More%20with%20Less-Crown%20Business%20%281999%29.epub"
    link2 = "http://62.182.86.140/main/461000/e5fa82c4419247652fc53c543cbb823f/Miguel%20de%20Cervantes%20Saavedra%2C%20Edith%20Grossman%20%28Translator%29%2C%20Harold%20Bloom%20%28Introduction%29%20-%20Don%20Quixote-Harper%20Perennial%20%282005%29.epub"
    title, data = download_epub(link2)
    send_to_kindle(title, data)
