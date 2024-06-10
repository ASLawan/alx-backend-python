#!/usr/bin/env python3
"""
    module with function to create and return
    asynio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
