#!/usr/bin/python3
"""github api."""


import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    headers = {'Authorization': f'Bearer {password}'}

    response = requests.get(url, headers=headers)

    if response.status_code >= 400:
        print(None)
        sys.exit(1)

    user_id = response.json().get("id")
    print(user_id)
