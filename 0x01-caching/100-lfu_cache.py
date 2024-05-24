#!/usr/bin/env python3
"""
LFUCache module
This module provides a caching system with LFU replacement policy.
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache class
    Inherits from BaseCaching and implements a LFU caching system.
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()
        self.freq = defaultdict(int)
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.freq[key] += 1
            else:
                self.freq[key] = 1
                self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                candidates = [k for k in self.order if self.freq[k] == min_freq]
                if len(candidates) > 1:
                    discard = candidates[0]
                else:
                    discard = candidates[0]
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.freq[discard]
                self.order.remove(discard)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data[key]
        return None
