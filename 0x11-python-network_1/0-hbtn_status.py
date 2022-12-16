#!/usr/bin/python3
"""This script fetches the https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    req = urllib.rquest.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body_page = response.read()
        print("body_page response:")
        print("\t- type: {}".format(type(body_page)))
        print("\t- content: {}".format(body_page))
        print("\t- utf8 content: {}".format(body_page.decode("utf-8")))
