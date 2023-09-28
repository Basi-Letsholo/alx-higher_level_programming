#!/bin/bash
# sends GET request and displays body
curl -sX GET -o body -w "%{http_code}" "$1" && cat body
