#!/usr/bin/env python3
"""Coroutine that loops asynchronously"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform() * 10
