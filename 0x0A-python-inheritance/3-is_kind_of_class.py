#!/usr/bin/python3
"""Verifies if object is an instance or inherited"""


def is_kind_of_class(obj, a_class):
    """function return true if object is an instance of a class
    or a class that the class in question inherits from
    """
    return (isinstance(obj, a_class))
