#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if str(abs(value)).isdigit():
            print("{:d}".format(value))
            return True
        else:
            raise Exception
    except:
        return False
