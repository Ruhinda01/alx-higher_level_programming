#!/usr/bin/python3

def uppercase(str):
    up_str = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            up_str += chr(ord(ch) - 32)
        else:
            up_str += ch
    print("{}".format(up_str))
