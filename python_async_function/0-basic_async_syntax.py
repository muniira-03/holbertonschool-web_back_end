#!/usr/bin/env python3
"""Module that contains an asynchronous coroutine for waiting a random time"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return the delay.

    Args:
        max_delay (int): Maximum number of seconds to wait (default is 10).

    Returns:
        float: The actual delay time waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay