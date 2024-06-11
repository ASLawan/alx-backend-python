#!/usr/bin/env python3
"""
    module implementing a coroutine that computes the total runtime
    for running asyn_comprehension four times in parallel
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures and returns total runtime from running async_comprehension
    fout times in a parallel"""

    start_time = time.time()

    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )

    end_time = time.time()

    total_time = end_time - start_time

    return total_time
