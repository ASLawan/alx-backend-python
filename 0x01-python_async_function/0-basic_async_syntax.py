#!/usr/bin/env python3
"""
    Module with function that implements an asynchronouse
    coroutine that waits for random delay
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns delay value as a float"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == "__main__":
    random_delay = asyncio.run(wait_random())
    print(random_delay)
