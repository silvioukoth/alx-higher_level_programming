#!/usr/bin/python3
"""Sends and display the value of X-Request-Id variable"""
#Usage: ./1-hbtn_header.py <URL>

import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        for header in response.getheaders():
            if header[0] == 'X-Request-Id':
                print(header[1])
