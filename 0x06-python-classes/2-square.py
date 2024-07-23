#!/usr/bin/python3
""" This is a module """


class Square:
    """ Square class """
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError
        elif size < 0:
            raise ValueError
        else:
            self.__size = size
