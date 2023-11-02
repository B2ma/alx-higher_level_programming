#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me, server to respond with You got me!
curl -s -o /dev/null -w "%{http_code}" -X POST -d "You got me!" http://0.0.0.0:5000/catch_me
