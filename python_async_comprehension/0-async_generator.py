#!/usr/bin/env python3
"""Module contenant un generateur asynchrone de nombres aleatoires."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Genere 10 nombres aleatoires entre 0 et 10 avec pause d'1 seconde."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
