#!/usr/bin/env python3
#
# Version:              1.1
# winHunter Author:     Mithlonde
# Creation Date:        19/03/2024
# Website:              https://github.com/Mithlonde/utf8coder

import urllib.parse
import sys

def urlencode(input_string):
    #Encode the provided string using URL encoding with UTF-8 encoding
    return urllib.parse.quote(input_string, safe='', encoding='utf-8')

def main():
    if len(sys.argv) != 2:
        print("Usage: Python3 utf8encode.py 'string'")
        sys.exit(1)

    string_to_encode = sys.argv[1]
    encoded_string = urlencode(string_to_encode)
    print(encoded_string)

if __name__ == "__main__":
    main()