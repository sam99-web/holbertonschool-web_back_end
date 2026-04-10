#!/usr/bin/env python3
"""Module mesurant le temps d'execution de wait_n."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Mesure le temps total d'execution de wait_n et retourne total_time / n.

    Args:
        n: Le nombre de coroutines a executer.
        max_delay: Le delai maximum en secondes.

    Returns:
        Le temps moyen d'execution par coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n