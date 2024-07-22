#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print("{:d}".format(my_list[count]), end=" ")
            count += 1
        print()  # Print a newline after the loop
    except IndexError:
        print()  # Print a newline if there is an IndexError
    return count
