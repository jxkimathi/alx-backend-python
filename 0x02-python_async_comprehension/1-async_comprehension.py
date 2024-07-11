#!/usr/bin/env python3
"""Writing a coroutine that returns 10 random numbers"""
import asyncio
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers and runs a coroutine"""
    return [num async for num in async_generator()]
