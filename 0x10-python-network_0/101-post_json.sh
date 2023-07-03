#!/bin/bash
# Script sends a JSON POST request to a URL and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
