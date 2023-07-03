#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
and displays the response body.

Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.parse
import urllib.request


def post_email(url, email):
    """
    Sends a POST request to the URL with the email as a parameter
    and displays the response body.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
