#!/bin/bash
################################################################################
# Script: 0-body_size.sh
# Description: This script sends a HTTP request to a specific URL using curl and
#		displays the size of the response body in bytes.
################################################################################

url="$1"

curl -s "$url" | wc -c
