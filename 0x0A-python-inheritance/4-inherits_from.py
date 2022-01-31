#!/usr/bin/python3
"""
Modulos that reviews if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class 
"""


def inherits_from(obj, a_class):
    """
    Function that reviews if an object is an instance (directly or ind.)
    Vars:
        obj
        a_class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
