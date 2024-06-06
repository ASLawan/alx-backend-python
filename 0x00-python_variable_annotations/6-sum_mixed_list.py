#!/usr/bin/env python3
"""
    Module implementing a function that sums a mixed list of ints
    and floats - returns a float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Sums a mixed list of ints and floats and returns a float"""
    sum_mixed = 0
    for num in mxd_list:
        sum_mixed += num
    return float(sum_mixed)
