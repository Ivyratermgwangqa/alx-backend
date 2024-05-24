#!/usr/bin/env python3
"""
LIFOCache module
This module provides a caching system with LIFO replacement policy.
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache class
    Inherits from BaseCaching and implements a LIFO caching system.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.order.pop(-2)
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
