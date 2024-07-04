#!/usr/bin/env python3
"""Type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list and returns the float"""
    return float(sum(input_list))
