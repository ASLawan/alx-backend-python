#!/usr/bin/env python3
"""
    Module implementing a function that returns another
    function - a Callable.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns another function - a Callable"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
