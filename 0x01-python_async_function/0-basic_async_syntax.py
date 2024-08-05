#!/usr/bin/env python3
"""Introduction to the aynchio and random modules"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """A simple function that takes a int (max_delay) waits for
    a random delay between 0 and max_delay(include) and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
