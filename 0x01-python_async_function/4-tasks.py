#!/usr/bin/env python3
"""
    Module that implements coroutines and
    returns a list of delay values
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays"""
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        if not delays or delay >= delays[-1]:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
    return delays
