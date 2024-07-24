#!/usr/bin/python3
'''Module for Least Recently Used (LRU) caching.
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Defines a cache system using the LRU eviction policy,
    inheriting from the BaseCaching class.
    '''

    def __init__(self):
        '''Initializes the cache object.
        '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''Adds an item to the cache using the LRU technique.
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
        '''Retrieves the cache data associated with the key.
        '''
        if key is None or key not in self.cache_data:
            return None

        self.queue.remove(key)
        self.queue.append(key)

        return self.cache_data[key]
