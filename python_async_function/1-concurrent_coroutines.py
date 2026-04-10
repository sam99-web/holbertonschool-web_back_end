#!/usr/bin/env python3
"""Module executant plusieurs coroutines en parallele."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawne wait_random n fois et retourne les delais en ordre croissant.

    Args:
        n: Le nombre de fois que wait_random est appele.
        max_delay: Le delai maximum en secondes.

    Returns:
        La liste des delais en ordre croissant.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)
    return delays
