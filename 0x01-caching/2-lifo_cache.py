#!/usr/bin/python3
'''Module for Last-In First-Out (LIFO) caching.
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Defines a caching system that inherits from
    BaseCaching and uses the LIFO policy.
    '''

    def __init__(self):
        '''Initializes the cache object.'''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''Adds an item to the cache using the LIFO method.
        '''
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            tobe_discard = self.queue.pop()
            print('DISCARD: {}'.format(tobe_discard))
            del self.cache_data[tobe_discard]

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Retrieves the cache data associated with the key.
        '''
        if key is None or key not in self.cache_data:
            return

        return self.cache_data[key]
