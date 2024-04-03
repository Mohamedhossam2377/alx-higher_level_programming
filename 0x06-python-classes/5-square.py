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
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print sqaure"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
