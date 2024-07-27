#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request"""

import sys
import requests

url = "http://0.0.0.0:5000/search_user"
try:
    param = {'q': str(sys.argv[1])}
except IndexError:
    print("No result")
    exit()

r = requests.post(url, data=param)
try:
    body = r.json()
except requests.exceptions.JSONDecodeError:
    print('Not a valid JSON')
else:
    if body == {}:
        print("No result")
    else:
        print(r.text)
        print("[{}] {}".format(body.get('id'), body.get('name')))
