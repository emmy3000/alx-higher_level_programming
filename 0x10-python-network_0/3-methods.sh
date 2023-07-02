#!/bin/bash
# Script to display the HTTP methods accepted by a server for a given URL
curl -sI "$1" | grep -i "^allow:" | awk -F': ' '{print $2}'
