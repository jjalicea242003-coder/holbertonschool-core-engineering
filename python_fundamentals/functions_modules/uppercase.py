#!/usr/bin/env python3

def uppercase(text):
    result = ""

    for char in text:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char

    print("{}".format(result))
