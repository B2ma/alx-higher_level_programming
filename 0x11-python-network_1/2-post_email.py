#!usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
import sys
from urllib.request import urlopen

url = sys.argv[1]
email = sys.argv[2]

data = urlib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data)
with uellib.request.urlopen(req) as response:
    body = response.read().decod('utf-8')
    print(body)

if __name__ == "__main__":
