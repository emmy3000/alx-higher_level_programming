#!/bin/bash
# Script to send a POST request to a URL with query parameters and display the response body
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
