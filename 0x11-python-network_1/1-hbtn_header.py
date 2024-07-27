#!/usr/bin/python3
"""Script sends a req to the URL and displays value of the X-Request-Id var"""
import sys
from urllib.request import urlopen

if __name__ == '__main__':
    url = sys.argv[1]
    with urlopen(url) as response:
        value = response.headers.get('X-Request-Id')
        print(value)
