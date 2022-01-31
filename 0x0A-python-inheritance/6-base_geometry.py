#!/usr/bin/python3
"""
Writting public instance method that raises exception
"""


class BaseGeometry:
    """Class that contains a function area()"""

    def area(self):
        """Function that is not implemented and rise exception"""
        raise Exception("area() is not implemented")
