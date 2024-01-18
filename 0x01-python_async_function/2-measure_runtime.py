#!/usr/bin/env python3
'''
Measuring the time elapsed in an async function call
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    ''' Accessing average time per iteration '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    appr_time = total_time / n

    return appr_time
