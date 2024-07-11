#!/usr/bin/env python3
"""Writing a coroutine that returns 10 random numbers"""
import asyncio
from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def asynnc_comprehension() -> List[float]:
    """Collects 10 random numbers and runs a coroutine"""
    return [num async for num in async_generator]
