#!/usr/bin/python3
def islower(c):
    str1 = "is lower"
    str2 = "is upper"
    if ord(c) >= 97 and ord(c) <= 122:
        print("{} {}".format(c, str1))
    else:
        print("{} {}".format(c, str2))
