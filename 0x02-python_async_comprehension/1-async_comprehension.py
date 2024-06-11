#!/usr/bin/env python3
"""
    Module with async function implementing async list comprehension
    - returns  a list of ten random numbers
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine that collects 10 random numbers using async comprehension
    over async_generator, then retruns the 10 random numbers"""

    return [number async for number in async_generator()]
