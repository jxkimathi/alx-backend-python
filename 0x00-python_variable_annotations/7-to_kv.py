#!/usr/bin/env python3
"""Takes in an int or float with a str and returns tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key value pair to a tuple"""
    return (k, float(v**2))
