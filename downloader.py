#!/usr/bin/env python
import requests
import re
import os

# Load thumbnail URLs (replace with actual list)
# Sample thumbnail URL: https://images.premagic.com/txpybWj566Knv6SyqwjHNeD89U%3D%2F%2F240x240%2Fsmart%2Ffilters%3Aquality%2840%29%3Asharpen%28-0.2%29%3Astrip_icc%28%29%3Astrip_exif%28%29%2FD36wX4CIc2RzDMcR-zDKRPkaIoFzGCgZ5-thumb_6wINoQheX36VsuLe-b%27dGh1bWJfSkFZMDk0OTcuSlBH%27.JPG
thumbnail_urls = []

folder_name = "FOLDER_NAME"

provider_id = "REPLACE_WITH_PROVIDER_ID"

os.makedirs(folder_name, exist_ok=True)

for url in thumbnail_urls:
    match1 = re.search(r'thumb_([^-]+)-', url)
    match2 = re.search(r"-b%27dGh1bWJf(.*?)%27", url)
    match3 = re.search(r"D36wX4CIc2RzDMcR-(.*?)-", url)
    if match1 and match2 and match3:
        image_id = match1.group(1)
        hashed_image_url = match2.group(1)
        hashed_folder_url = match3.group(1)
        download_url = f"https://s3-ap-southeast-1.amazonaws.com/asia-compressed-image-store/{provider_id}-{hashed_folder_url}-{image_id}-b'{hashed_image_url}'.JPG"
        print(f"Downloading {download_url}")
        response = requests.get(download_url)
        if response.status_code == 200:
            with open(f"{folder_name}/{image_id}.JPG", "wb") as file:
                file.write(response.content)
        else:
            print(f"Failed to download: {download_url}")
