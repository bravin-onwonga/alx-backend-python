#!/usr/bin/env python3
"""Simple module with a function to sum a list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of all the values of the list"""
    return sum(input_list)
