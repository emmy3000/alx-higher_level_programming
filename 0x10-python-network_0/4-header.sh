#!/bin/bash
# Script sends a GET request to a URL with a custom header & display the response body
curl -sL -H "X-School-User-Id: 98" "$1"
