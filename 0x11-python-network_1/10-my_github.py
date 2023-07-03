#!/usr/bin/python3
"""
Fetches your GitHub ID using the GitHub API and Basic Authentication.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def fetch_github_id(username, token):
    """
    Fetches your GitHub ID using the GitHub API
    and Basic Authentication.

    Args:
        username (str): Your GitHub username.
        token (str): Your personal access token.

    Returns:
        int: Your GitHub ID.
    """
    auth = HTTPBasicAuth(username, token)
    response = requests.get("https://api.github.com/user", auth=auth)
    if response.status_code == 200:
        data = response.json()
        return data['id']
    else:
        raise Exception("Error while fetching GitHub ID. Error code: "
                        + str(response.status_code))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    try:
        github_id = fetch_github_id(username, token)
        print("Your GitHub ID is:", github_id)
    except Exception as e:
        print(str(e))
