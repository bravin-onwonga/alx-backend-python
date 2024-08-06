#!/usr/bin/env python3
"""Measuring the total run time"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Calls the async_comprehension 4 times and
    returns the total time taken"""
    start = time.perf_counter()
    coroutines = (async_comprehension() for _ in range(4))
    await asyncio.gather(*(coroutines))
    return time.perf_counter() - start
