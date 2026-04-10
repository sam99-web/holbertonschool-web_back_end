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
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    sorted_delays = []
    for delay in delays:
        inserted = False
        for i, val in enumerate(sorted_delays):
            if delay < val:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)
    return sorted_delays