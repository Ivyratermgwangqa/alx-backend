#!/usr/bin/env python3
"""
MRUCache module
This module provides a caching system with MRU replacement policy.
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache class
    Inherits from BaseCaching and implements a MRU caching system.
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
                discard = self.order.pop(-1)
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
