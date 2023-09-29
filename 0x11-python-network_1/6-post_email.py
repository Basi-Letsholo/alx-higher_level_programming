#!/usr/bin/python3
"""Sends a POST request to URL with email parameter."""


import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    input_email = sys.argv[2]
    parameters = {'email': input_email}

    response = requests.post(url, data=parameters)

    print(response.text)
