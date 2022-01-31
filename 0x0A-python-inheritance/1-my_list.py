#!/usr/bin/python3
"""
Class that inherits from list
"""


class MyList(list):
    """
    Son list
    """
    def print_sorted(self):
        """
            Function that prints
        """
        print(sorted(self))
