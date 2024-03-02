#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge
"""


if __name__ == "__main__":
    import sys
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url)
    response = r.json()

    for commit in response[:10]:
        print("{}: {}".format(
            commit.get('sha'),
            commit.get('commit').get('author').get('name')))
