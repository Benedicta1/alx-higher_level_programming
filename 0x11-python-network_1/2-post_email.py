#!/usr/bin/python3
"""script that  request to the passed URL with the email as a parameter
"""
if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv
body = urllib.parse.urlencode({'email': argv[2]})
    body = body.encode('ascii')
    with urllib.request.urlopen(argv[1], body) as url:
        print(url.read().decode('utf-8'))
