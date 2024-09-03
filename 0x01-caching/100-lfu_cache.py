#!/usr/bin/env python3
"""
LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.queue = [[]]

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.queue:
                    for i in range(len(self.queue)):
                        if len(self.queue[i]) > 0 and self.queue[i][0]:
                            removed = self.queue[i].pop(0)
                            break
                    del self.cache_data[removed]
                    print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.queue[0].append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.cache_data:
            for i in range(len(self.queue)):
                if key in self.queue[i]:
                    self.queue[i].remove(key)
                    if i + 1 == len(self.queue):
                        self.queue.append([])
                    self.queue[i + 1].append(key)
                    break
        return self.cache_data.get(key, None)
