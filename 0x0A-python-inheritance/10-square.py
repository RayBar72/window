#!/usr/bin/python3
"""
Class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """
        Instantiation var size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Function that calculates area
        """
        return self.__size * self.__size
