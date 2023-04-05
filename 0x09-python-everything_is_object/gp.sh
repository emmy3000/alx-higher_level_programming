#!/bin/bash

message="$1"

# Add all changes
git add .

# Commit with the provided message
git commit -m "$message"

# Push changes to the remote repository
git push

