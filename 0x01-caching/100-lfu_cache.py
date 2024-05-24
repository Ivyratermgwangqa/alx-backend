#!/usr/bin/env python3

from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    """LFUCache inherits from BaseCaching and implements LFU caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.frequency = defaultdict(int)
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value for the key key."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
                if len(lfu_keys) == 1:
                    discarded_key = lfu_keys[0]
                else:
                    discarded_key = next(k for k in self.order if k in lfu_keys)
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                self.order.remove(discarded_key)
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key in self.cache_data:
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
