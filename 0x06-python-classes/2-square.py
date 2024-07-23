#!/usr/bin/python3
""" This is a module """


class Square:
    """ Square class """
    def __init__(self, size = 0):
        if int(size).isdigit():
            self.__size = size
        else:
            raise TypeError
        if size < 0:
            raise ValueError
