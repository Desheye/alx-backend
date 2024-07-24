#!/usr/bin/env python3
'''Module for basic caching functionality.
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Defines a cache system using a dictionary
    for storing and retrieving items.
    '''

    def put(self, key, item):
        '''Add an item to the cache.
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Retrieve an item from the cache by key.
        '''
        return self.cache_data.get(key, None)

