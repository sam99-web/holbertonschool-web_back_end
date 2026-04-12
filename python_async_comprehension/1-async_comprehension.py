#!/usr/bin/env python3
"""Module contenant une coroutine utilisant une async comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collecte 10 nombres aleatoires via async comprehension."""
    return [i async for i in async_generator()]
