#!/usr/bin/python3
"""Write a Python script that displays the value of the X-Request-Id
"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as respo:
        print(respo.getheader('X-Request-Id'))
