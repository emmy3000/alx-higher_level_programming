#!/bin/bash

################################################################################
# Script: 0-body_size.sh
# Description: This script sends a request to a specific URL using curl and
#		displays the size of the response body in bytes.
# Usage: ./0-body_size.sh <URL>
#	 Replace <URL> with the actual URL to test against.
################################################################################

# Check if URL argument is provided
if [ $# -eq 0 ]; then
	echo "Usage: ./0-body_size.sh <URL>"
	exit 1
fi

# Get the URL argument
url="$1"

# Send a request to the URL and save the response body
response=$(curl -s "$url" | wc -c)

# Display the size of the response body
echo "${response}"
