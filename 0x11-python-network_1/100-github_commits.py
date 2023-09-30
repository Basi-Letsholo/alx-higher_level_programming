#!/usr/bin/python3
"""Github commits."""


import sys
import requests

if __name__ == '__main__':

    owner = sys.argv[2]
    repo = sys.argv[1]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error")
        sys.exit(1)

    sha_items = []
    authors = []

    for item in response.json():
        if 'sha' in item:
            sha_items.append(item['sha'])

    for item in response.json():
        if 'commit' in item and 'author' in item['commit'] and \
                'name' in item['commit']['author']:
            authors.append(item['commit']['author']['name'])

    first_10 = sha_items[:10]
    first_authors = authors[:10]

    for i in range(0, 10):
        print(f'{first_10[i]}: {first_authors[i]}')
