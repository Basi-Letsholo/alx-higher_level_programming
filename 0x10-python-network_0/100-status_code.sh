#!/bin/bash
# Displays status code of request
curl -sI -o /dev/null -w "%{http_code}" "$1"
