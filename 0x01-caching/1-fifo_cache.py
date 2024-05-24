#!/usr/bin/env python3
"""
FIFOCache module
This module provides a caching system with FIFO replacement policy.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    Inherits from BaseCaching and implements a FIFO caching system.
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
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.order.pop(0)
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
