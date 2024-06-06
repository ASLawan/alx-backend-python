#!/usr/bin/env python3
"""
    Module implementing a function that handles complex
    annotated types - returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of string and float"""
    return (k, float(v ** 2))
