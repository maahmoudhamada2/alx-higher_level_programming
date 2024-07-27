#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL"""

import sys
import urllib
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            body = response.read()
            decode = response.headers.get_content_charset('utf-8')
            print("{}".format(body.decode(decode)))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
