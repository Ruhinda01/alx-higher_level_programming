#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if len(sys.argv) == 2:
        q = sys.argv[1]
    payload = {'q': q}
    r = requests.post(url, data=payload)
    try:
        resp = r.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
    except ValueError:
        print("Not a valid JSON")
