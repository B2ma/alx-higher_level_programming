#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Your email is: {}".format(response.text.strip()))
