#!/usr/bin/env python3
"""
    Module implementing function that returns a sequence and
    length of given sequence.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a tuple containing a sequence and length of sequence"""
    return [(i, len(i)) for i in lst]
