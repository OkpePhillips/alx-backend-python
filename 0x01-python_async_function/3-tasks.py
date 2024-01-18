#!/usr/bin/env python3
'''
Creating a function that returns a asyncio.Task.
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Wrapping the wait_random coroutine in a Task
    using asyncio.ensure_future
    '''
    task = asyncio.ensure_future(wait_random(max_delay))
    return task
