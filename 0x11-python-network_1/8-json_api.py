#!/usr/bin/python3
"""sends a post request to url with parameter as letter inputted."""


import sys
import requests

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    parameters = {'q': letter}
    response = requests.post(url, data=parameters)

    data = response.json()

    if isinstance(data, dict) and len(data) > 0:
        data_id = data.get('id')
        data_name = data.get('name')
        print('[{}] {}'.format(data_id, data_name))
    elif isinstance(data, dict) and len(data) == 0:
        print('No result')
    else:
        print('Not a valid JSON')
