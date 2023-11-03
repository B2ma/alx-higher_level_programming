#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response
"""
import sys
from urllib.request import urlopen

url = sys.argv[1]
with urlopen(url) as response:
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)

if __name__ == "__main__":
    sys.exit(1)