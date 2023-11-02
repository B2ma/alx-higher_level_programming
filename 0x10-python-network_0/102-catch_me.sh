#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me, server to respond with You got me!
curl -s -X POST -d "You got me!" -L http://0.0.0.0:5000/catch_me
