#!/usr/bin/python3
"""Holberton School Interview"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    def commit_date(inter):
        return inter.get('commit').get('author').get('date')

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    response = get(url)
    commit_list = response.json()
    list_by_date = sorted(commit_list, key=commit_date, reverse=True)
    for i, obj_dict in enumerate(list_by_date):
        if i > 9:
            break
        print('{}: {}'.format(obj_dict.get('sha'),
                              obj_dict.get
                                  'commit').get('author').get('name')))
