#!/usr/bin/env python3
"""An asynchronous routine"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns n instances of wait_random"""
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    results = await asyncio.gather(*tasks)
    delays.extend(results)

    return sorted(delays)
