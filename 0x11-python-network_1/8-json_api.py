#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a given letter as a parameter.

Displays the response body in a specific format
based on the JSON data received.
"""
import sys
import requests


def search_user():
    """
    Sends a POST request to http://0.0.0.0:5000/search_user
    and displays the response body.
    """
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}

    response = requests.post(url, data=data)
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'),
                                   json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user()
