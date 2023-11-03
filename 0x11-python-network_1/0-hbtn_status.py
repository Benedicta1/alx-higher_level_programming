#!/usr/bin/python
'''
fetches https://alx-intranet.hbtn.io/status
'''
import urllib.request as reque

if __name__ == '__main__':
    with reque.urlopen('https://alx-intranet.hbtn.io/status') as respo:
        content = respo.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
