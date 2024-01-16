#!/usr/bin/env python3
"""Coroutine that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine will loop 10 times each time asynchronously
       wait 1 second, then yield a random number between 0 and 10"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
