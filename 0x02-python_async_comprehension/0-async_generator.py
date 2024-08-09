#!/usr/bin/env python3
"""Module on async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generator function that loops ten times and yields a random
    float between 0 and 10"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
