#!/usr/bin/env python3
"""Module for running multiple coroutines concurrently without sort()"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times with max_delay, return delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random

    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []
    for coro in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await coro
        delays.append(delay)
    return delays