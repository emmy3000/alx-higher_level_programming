#!/usr/bin/python3
"""
A script that takes in a URL, sends a request,
and displays the value of the X-Request-Id header variable.
"""

import urllib.request
import sys

# Retrieve the URL from command-line argument
url = sys.argv[1]

# Send a request to the URL and open the response
with urllib.request.urlopen(url) as response:
    # Get the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')

# Print the value of the X-Request-Id variable
print(x_request_id)
