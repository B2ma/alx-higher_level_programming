#!/bin/bash
#  Sends a DELETE request to the URL passed and displays the body of the response
curl -sX DELETE $1 -L
