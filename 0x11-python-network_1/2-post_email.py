#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request"""


import sys
import urllib.parse
from urllib.request import Request, urlopen

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        body = response.read()
        decode = response.headers.get_content_charset('utf-8')
        print("{}".format(body.decode(decode)))
