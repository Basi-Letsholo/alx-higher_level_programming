#!/usr/bin/python3
"""Fectches given url"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as status:
    html = status.read()

print('Body response:')
print('\t- type: {}'.format(type(html)))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.format(html.decode('utf-8')))
