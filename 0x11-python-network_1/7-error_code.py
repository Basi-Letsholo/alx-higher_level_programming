#!/usr/bin/python3
"""Sends url request and displays body or error code."""


import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code >= 400:
            print("Error code: {}".format(status_code))
