#!/bin/bash
# Sends request to URL and displays size of body
curl -sI "$1" | grep -i 'Content-Length:' | awk '{print $2}'
