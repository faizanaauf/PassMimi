import os
import requests
import zipfile
from io import BytesIO

# Cloud link to your ZIP wordlist (replace below with your link)
WORDLIST_URL = "https://drive.google.com/file/d/1cm8Xh8e4s0zFZlHtbnkJigG3JnkVdwHc/view?usp=drive_link"

DEST_DIR = "wordlists"

def download_and_extract():
    print("[INFO] Downloading wordlists from cloud...")
    os.makedirs(DEST_DIR, exist_ok=True)
    
    response = requests.get(WORDLIST_URL, stream=True)
    response.raise_for_status()
    
    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
        zip_ref.extractall(DEST_DIR)
    
    print("[INFO] Wordlists successfully extracted to:", DEST_DIR)

if __name__ == "__main__":
    download_and_extract()
