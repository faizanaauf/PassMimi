import os
import requests
import zipfile
from io import BytesIO

# Dropbox direct download link (use dl=1)
WORDLIST_URL = "https://www.dropbox.com/scl/fi/8bxum1rn8j2iw97i44izk/wordlists.zip?rlkey=kxijb72ndw90pkkn30nrcrroh&st=pmwi2iji&dl=1"
DEST_DIR = "wordlists"

def download_and_extract():
    print("[INFO] Downloading wordlists from cloud...")
    os.makedirs(DEST_DIR, exist_ok=True)
    
    response = requests.get(WORDLIST_URL, stream=True)
    response.raise_for_status()

    # Save to memory
    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
        zip_ref.extractall(DEST_DIR)
    
    print("[INFO] Wordlists successfully extracted to:", DEST_DIR)

if __name__ == "__main__":
    download_and_extract()
