#!/usr/bin/env python3
"""Module to collect two random numbers"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Function to collect the ten random values and return it as a list"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
