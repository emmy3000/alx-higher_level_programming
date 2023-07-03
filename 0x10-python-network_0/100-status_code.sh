#!/bin/bash
# Script sends a request to a URL & display only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
