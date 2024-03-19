#!/usr/bin/env python3
#
# Version:              1.1
# winHunter Author:     Mithlonde
# Creation Date:        19/03/2024
# Website:              https://github.com/Mithlonde/utf8coder

import urllib.parse
import sys

def urldecode(input_string):
    # Decode the provided URL-encoded string from stdin
    return urllib.parse.unquote(input_string, encoding='utf-8')

def main():
    if len(sys.argv) != 2:
        print("Usage: Python3 utf8decode.py 'encoded_string'")
        sys.exit(1)

    encoded_string = sys.argv[1]
    decoded_string = urldecode(encoded_string)
    print(decoded_string)

if __name__ == "__main__":
    main()