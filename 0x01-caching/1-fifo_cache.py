#!/usr/bin/python3
""" FIFOCache"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache
    - evicts blocks in order in which they are added
    - inherits from BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache
        Args
            key:str
                The name of the item
            item:str
                The value of the item"""
        if key is None or item is None:
            return
        cache_len = len(self.cache_data)
        if cache_len >= BaseCaching.MAX_ITEMS:
            keys = list(self.cache_data.keys())
            self.cache_data.pop(keys[0])
            print(f"DISCARD: {keys[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache
        Args
            key:str
                The name of the item to be retrieved
        Return
            The retrieved item"""
        if key is None:
            return None
        return self.cache_data.get(key)
