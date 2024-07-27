#!/usr/bin/python3
"""Script to fetch url"""

if __name__ == '__main__':
    from urllib.request import Request, urlopen
    import urllib.parse

    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        print("Body response:")
        body = response.read()
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        encoding = response.headers.get_content_charset('utf-8')
        print("\t- utf8 content: {}".format(body.decode(encoding)))
