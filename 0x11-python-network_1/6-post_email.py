#!/usr/bin/python3
"""Script that takes in a URL and an email address, sends a POST request"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.post(url, data={'email': sys.argv[2]})
    print("{}".format(response.text))
