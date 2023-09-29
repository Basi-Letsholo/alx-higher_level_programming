#!/usr/bin/python3
"""Sends POST request to url, displays reponse """


import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    url = sys.argv[1]
    input_email = sys.argv[2]

    data = {'email': input_email}
    data = urllib.parse.urlencode(data).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        email = response.read().decode('utf-8')

    print(email)
