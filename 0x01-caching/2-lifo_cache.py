#!/usr/bin/env python3

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFOCache inherits from BaseCaching and implements LIFO caching system"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value for the key key."""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
