#!/usr/bin/env python3
'''LFU Caching Module
'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''Defines a caching system using the
    LFU (Least Frequently Used) eviction policy.
    '''

    def __init__(self):
        '''Initializes the cache.
        '''
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        '''Adds an item to the cache.
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = min(
                    self.frequency,
                    key=lambda k:
                    (self.frequency[k], self.usage_order.index(k))
                )
                print('DISCARD: {}'.format(lfu_key))
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.usage_order.remove(lfu_key)

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        '''Retrieves the cache data associated with the key.
        '''
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
