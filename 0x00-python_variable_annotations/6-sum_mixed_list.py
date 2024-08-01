#!/usr/bin/env python3
"""Working with mixed type list"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list with ints and floats"""
    return sum(mxd_lst)
