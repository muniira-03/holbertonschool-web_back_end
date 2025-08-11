#!/usr/bin/env python3
"""Module to measure average runtime per coroutine"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total runtime for wait_n and return average time per call.

    Args:
        n (int): Number of coroutines
        max_delay (int): Maximum delay

    Returns:
        float: Average runtime per coroutine
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n