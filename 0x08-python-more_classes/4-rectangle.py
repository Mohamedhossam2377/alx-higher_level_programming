#!/usr/bin/python3
"""
Defining an empty rectangle
"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Init the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string of rectagle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string of rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
