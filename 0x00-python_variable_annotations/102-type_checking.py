#!/usr/bin/env python3
"""Using mypy to validate a piece of code"""

from typing import List, Any, Union, cast, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Increases the size of an array based on a factor provided"""
    factor = cast(int, int(factor))
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
