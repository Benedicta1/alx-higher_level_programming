#!/usr/bin/python3
'''takes your GitHub credentials
'''
if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/user'
    response = get(url, auth=(argv[1], argv[2]))
    print(response.json().get('id'))
