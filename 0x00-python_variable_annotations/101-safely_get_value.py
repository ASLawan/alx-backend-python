#!/usr/bin/env python3
"""
    Module implementing a function that takes a dictionary
    and returns value of given key or default value

"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key:
                     Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Raturns value of specified key from dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
