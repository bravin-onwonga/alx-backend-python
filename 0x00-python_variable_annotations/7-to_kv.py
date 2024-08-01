#!/usr/bin/env python3
"""Working with mixed type arguments"""

from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of str k and sqr of int || float"""
    v_sqr: float = v ** 2
    return (k, v_sqr)
