#!/usr/bin/python3
"""
Class Rectangle
"""


class BaseGeometry:
    """Class that contains a function area()"""

    def area(self):
        """Function that is not implemented and rise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise TypeError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class that inheritage from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation vars width and heigh
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
            """Function that calculates area"""
            return self.__width * self.__height

    def __str__(self):
        """
        Function that returns description of rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
