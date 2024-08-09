#!/usr/bin/env python3
"""Module to collect two random numbers"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Function to collect the ten random values and return it as a list"""
    result = [i async for i in async_generator()]
    return result
