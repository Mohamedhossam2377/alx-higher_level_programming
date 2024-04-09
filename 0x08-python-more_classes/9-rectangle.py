#!/usr/bin/python3
"""
Defining an empty rectangle
"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """print message for every deletion of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        return self.width * self.height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """returns printable string of rectagle"""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """returns a string of rectangle for reproduction"""
        return "Rectangle(" + str(self.width) + ", " + str(self.heiht) + ")"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger of two rectangle

        Args:
            rect_1: first rectangle
            rect_2: second rectangle

        Raises:
            TypeError: if rect_1, rect_2 are not instances of rectangle

        Returns:
            the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        '''instantiates a new square.

        Args:
            size: size of new square

        Returns:
            class
        '''
        return cls(size, size)
