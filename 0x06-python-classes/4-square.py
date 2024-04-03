#!/usr/bin/python3
"""square module"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """size is length of side of the sqaure"""
        self.__size = size

    @property
    def size(self):
        """size is length of side of the sqaure"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
