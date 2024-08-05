#!/usr/bin/env python3
"""Measure the runtime of an asynch program"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function to measure the time taken for the function
    imported to finish executing"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_taken = time.perf_counter() - start
    return time_taken / n
