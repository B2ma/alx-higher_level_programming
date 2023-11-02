#!/bin/bash
# sends a request to a URL and displays only the status code of the response.
curl -sw $1 -o /dev/null "%{http_code}"
