#!/usr/bin/env python3
"""Module covering working with callables using typing"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float
    using the multiplier passed"""
    def multiply(n: float) -> float:
        """Return the result of the float arg * the multiplier"""
        return multiplier * n
    return multiply
