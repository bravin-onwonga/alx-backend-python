#!/usr/bin/env python3
"""Similar code to the 1-concurrent_coroutine.wait_n function"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Takes two integers n and max_delay and spawns the async function
    wait_random n times and returns a list of all the delays"""
    coroutines = (task_wait_random(max_delay) for _ in range(n))
    my_list = await asyncio.gather(*(coroutines))
    return sorted(my_list)
