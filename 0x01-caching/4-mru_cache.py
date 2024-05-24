#!/usr/bin/env python3

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """MRUCache inherits from BaseCaching and implements MRU caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value for the key key."""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(-1)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
