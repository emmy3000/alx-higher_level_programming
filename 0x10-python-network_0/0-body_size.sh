#!/bin/bash
# Script retrieves the size in bytes of a HTTP response by passing a URL as arg
curl -s "$1" | wc -c
