#!/usr/bin/python3
"""
Displays the value of the X-Request-Id header variable
from a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
from urllib.request import Request, urlopen
from sys import argv


def main():
    """
    Displays the value of the X-Request-Id header variable
    from a request to a given URL.
    """
    url = argv[1]
    req = Request(url)
    with urlopen(req) as res:
        x_request_id = res.info().get("x-request-id")
        print(x_request_id)


if __name__ == "__main__":
    main()
