#!/usr/bin/env python3
"""Asynchronous coroutine that takes in int arg"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Random delay wait between 0 and max_delay"""
    number = random.uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
