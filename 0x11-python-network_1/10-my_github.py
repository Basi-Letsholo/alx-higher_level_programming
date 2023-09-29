#!/usr/bin/python3
"""github api."""


import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    headers = {'Authorization': f'Basic {username}:{password}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        if user_id is not None:
            print(user_id)
        else:
            print(None)
    else:
        print(None)
