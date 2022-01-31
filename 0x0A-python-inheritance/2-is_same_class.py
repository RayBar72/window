#!/usr/bin/python3
"""
Modulos with a function thar returns true
if object is exactly an instance of specific class
"""


def is_same_class(obj, a_class):
    """Function that reviews instance
        Vars:
         object
         Class
        Returns True o False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
