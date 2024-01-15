#!/usr/bin/env python3
"""Create a coroutine|task"""
import asyncio
from typing import Coroutine
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Coroutine:
    """Returns a coroutine"""
    return asyncio.create_task(wait_random(max_delay))
