#!/usr/bin/env python3
"""Module contenant une coroutine asynchrone d'attente aléatoire."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Attend un delai aleatoire entre 0 et max_delay secondes et le retourne."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
