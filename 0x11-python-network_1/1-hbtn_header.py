#!/usr/bin/python3
"""Sends request to url and displays value of header"""

import sys
import urllib.request

if __name__ == "__main__":

    url = sys.argv[1]

    with urllib.request.urlopen(url) as data:
        value = data.getheader("X-Request-Id")

    print(value)
