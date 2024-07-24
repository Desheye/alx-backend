#!/usr/bin/env python3
'''Module implementing First-In First-Out (FIFO) caching.
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''Defines a cache system using a dictionary with a FIFO
    eviction policy when the cache limit is reached.
    '''

    def __init__(self):
        '''Initializes the cache.
        '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''Adds an item to the cache.
        '''
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            tobe_discard = self.queue.pop(0)
            print('DISCARD: {}'.format(tobe_discard))
            del self.cache_data[tobe_discard]

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Retrieves an item from the cache by key.
        '''
        return self.cache_data.get(key, None)
