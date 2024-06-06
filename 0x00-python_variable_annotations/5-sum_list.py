#!/usr/bin/env python3
"""
    Module implementing a function that takes a list as input
    and returns the sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list and returns float"""
    float_sum = 0
    for num in input_list:
        float_sum += num

    return float_sum
