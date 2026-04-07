#!/usr/bin/env python3
"""Module that creates a tuple from a string and a number."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number."""
    return (k, float(v ** 2))