#!/bin/bash
# Script used in making a request & capture the response containing `You got me!`
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
