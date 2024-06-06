#!/usr/bin/env python3
"""
    Module implementing a function that takes 'any' list
    and returns 'any' list or None.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns Any list of None"""
    if lst:
        return lst[0]
    else:
        return None
