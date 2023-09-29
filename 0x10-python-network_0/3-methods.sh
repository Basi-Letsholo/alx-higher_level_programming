#!/bin/bash
# Displays all methods the server will accept from URL
curl -sI -X OPTIONS "$1" | awk -F 'Allow: ' 'NF>1{print $2}'
