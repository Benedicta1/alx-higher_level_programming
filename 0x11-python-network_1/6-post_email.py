#!/usr/bin/python3
"""passed URL with the email as a parameter
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    response = post(argv[1], data={'email': argv[2]})
    print(response.text)
