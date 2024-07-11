
"""Writes a coroutine that will run a function 4 times"""
import asyncio
import time
from typing import List
from random import uniform

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of the coroutines"""
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()
    return end_time - start_time
