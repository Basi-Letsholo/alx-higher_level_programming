#!/bin/bash
# Displays status code of request
curl -sI "$1" | grep -i 'HTTP/1.1' | awk '{print $2}'
