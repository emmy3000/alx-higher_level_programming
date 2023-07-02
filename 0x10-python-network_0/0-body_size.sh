#!/bin/bash
################################################################################
# Script: 0-body_size.sh
# Description: This script sends a HTTP request to a specific URL using curl and
#		displays the size of the response body in bytes.
################################################################################

curl -s "$1" | wc -c
