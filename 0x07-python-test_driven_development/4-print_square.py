#!/usr/bin/python3
"""
    Function that prints a square made of # char
    size: size of square
    For size ge of zero
"""


def print_square(size):
    """Function that prints a square made of # char"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    if size == 0:
        print("")
    else:
        while i < size:
            print("#" * size)
            i = 1 + i
