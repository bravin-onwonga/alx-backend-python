#!/usr/bin/env python3
"""Module on duck typing and iterables"""
from typing import Mapping, Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples as items"""
    return [(i, len(i)) for i in lst]
