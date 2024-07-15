#!/usr/bin/python3
def uppercase(str):
    for l in range(len(str)):
        c = ord(str[l])
        if c >= 97 and c <= 122:
            c -= 23
            print("{}".format(chr(c)), end="")
        else:
            print("{}".format(str[l]), end="")
