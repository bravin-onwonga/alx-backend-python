#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """Takes two integers n and max_delay and spawns the async function
    wait_random n times and returns a list of all the delays"""
    my_list = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(my_list)
