#!/usr/bin/python3
"""square module"""


class Square:
    """define square"""

    def __init__(self, size=0, position=(0, 0)):
        """size is length of side of the sqaure
        and position of new sqaure"""
        self.size = size
        self.position = position

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

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
