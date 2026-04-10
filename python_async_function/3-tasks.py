#!/usr/bin/env python3
"""Module creant une asyncio.Task a partir de wait_random."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Cree et retourne une asyncio.Task pour wait_random."""
    return asyncio.get_event_loop().create_task(wait_random(max_delay))
