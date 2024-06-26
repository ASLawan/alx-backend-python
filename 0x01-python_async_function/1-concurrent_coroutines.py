#!/usr/bin/env python3
"""
    Module that implements coroutines and
    returns a list of delay values
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays"""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        if not delays or delay >= delays[-1]:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
    return delays
