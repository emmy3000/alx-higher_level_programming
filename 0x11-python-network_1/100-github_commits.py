#!/usr/bin/python3
"""
Fetches the 10 most recent commits from a GitHub repository.

Usage: ./100-github_commits.py <repository> <owner>
"""

import sys
import requests

if __name__ == "__main__":
    """
    Fetches the 10 most recent commits from a GitHub repository.

    Usage: ./fetch_commits.py <repository> <owner>
    """

    repository = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(owner, repository)

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
