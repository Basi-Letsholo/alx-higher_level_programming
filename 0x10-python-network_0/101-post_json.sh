#!/bin/bash
# Sends a post request with a json file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
