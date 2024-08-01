#!/usr/bin/env python3
"""Module dealing with correct duck-typed annotations"""
from typing import Sequence, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return a value or None whether a list is given or not"""
    if lst:
        return lst[0]
    else:
        return None
