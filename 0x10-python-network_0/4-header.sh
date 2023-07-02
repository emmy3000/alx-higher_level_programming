#!/bin/bash
# Script sends a GET request to a URL with a custom header & display the response body

URL=$1
HEADER="X-School-User-Id: 98"

curl -sL -H "$HEADER" "$URL"
