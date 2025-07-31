#!/usr/bin/env python3
"""
Module that contains a function to return a tuple of a string
and squared number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with the string and the square
    of the number (as a float).
    """
    return (k, float(v ** 2))