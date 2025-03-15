# premagic-bulk-photo-downloader

This script downloads images based on a list of thumbnail URLs, extracts necessary parameters using regular expressions, and constructs a download URL to fetch the images from an S3 bucket. The images are then saved locally in a specified folder.

## Prerequisites

- Python 3.x
- `requests` library (for HTTP requests)

You can install the required library using `pip`:

```bash
pip install requests
