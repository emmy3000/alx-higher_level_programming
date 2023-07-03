#!/usr/bin/python3
"""
Displays the value of the X-Request-Id header variable
from a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request


if __name__ == "__main__":
    # Get the URL from command-line argument
    url = sys.argv[1]

    # Send a request to the URL
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        # Retrieve the value of the X-Request-Id header
        x_request_id = dict(response.headers).get("X-Request-Id")

        # Display the X-Request-Id value
        print(x_request_id)
