#!/usr/bin/env python3
'''
Module to return list of delays in an async function
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' Using asyncio.gather to run functions concurrently '''
    delays = await asyncio.gather(*(task_wait_random(
                                    max_delay) for _ in range(n)))
    return sorted(delays)
