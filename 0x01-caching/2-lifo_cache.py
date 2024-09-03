#!/usr/bin/env python3
"""
LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.queue:
                    removed = self.queue.pop(-1)
                    del self.cache_data[removed]
                    print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)
