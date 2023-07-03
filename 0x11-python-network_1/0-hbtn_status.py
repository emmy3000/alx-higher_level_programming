#!/usr/bin/python3
"""
A script that fetches the status
from https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request

# Define the URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Send a request to the URL and open the response
with urllib.request.urlopen(url) as response:
    # Read the response as bytes
    content = response.read()

# Decode the content as UTF-8
utf8_content = content.decode('utf-8')

# Print the body response with descriptive information
print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", utf8_content)
