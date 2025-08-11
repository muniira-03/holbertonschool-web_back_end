#!/usr/bin/env python3
"""Module for running multiple task_wait_random concurrently"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times and return delays in ascending order.

    Args:
        n (int): Number of coroutines
        max_delay (int): Maximum delay

    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []
    for coro in asyncio.as_completed([task_wait_random(max_delay) for _ in range(n)]):
        delay = await coro
        delays.append(delay)
    return delays