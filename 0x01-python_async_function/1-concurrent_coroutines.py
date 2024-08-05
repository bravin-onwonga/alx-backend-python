#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Takes two integers n and max_delay and spawns the async function
    wait_random n times and returns a list of all the delays"""
    my_list = []
    for _ in range(n):
        res = await wait_random(max_delay)
        my_list.append(res)
    return my_list
