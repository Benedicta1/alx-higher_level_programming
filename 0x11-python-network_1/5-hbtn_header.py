#!/usr/bin/python3
"""variable X-Request-Id in the response header
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    response = get(argv[1])
    print(response.headers.get('x-request-id'))
