#!/usr/bin/python3
""" fectches url with requests module"""


import requests


if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    text = response.text

    print('Body response:')
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))
