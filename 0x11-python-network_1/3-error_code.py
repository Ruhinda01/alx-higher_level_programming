#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    from urllib.error import HTTPError
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            html_decoded = html.decode('utf-8')
            print(html_decoded)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
