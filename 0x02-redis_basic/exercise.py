#!/usr/bin/env python3
'''
Using redis in python via the redis-py library.
'''
import redis
import uuid
from typing import Union


class Cache:
    '''
    A cache class to create an instance of Redis.
    '''
    def __init__(self, host='localhost', port=6379, db=0):
        '''
        Instantiating a redis object.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        A method to store input data in redis and return key.
        '''
        r_key = str(uuid.uuid4())
        self._redis.set(r_key, data)
        return r_key
