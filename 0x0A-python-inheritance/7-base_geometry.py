#!/usr/bin/python3
"""
Class BaseGometry
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
