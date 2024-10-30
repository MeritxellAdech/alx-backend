#!/usr/bin/python3
""" LIFO Cache """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache
    - last in First Out implementation
    - Inherits from BaseCaching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add item to the cache
        Args
            key:str
                The name of the item
            item"str
                The value of the item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        cache_len = len(self.cache_data)
        if cache_len > BaseCaching.MAX_ITEMS:
            recent = list(self.cache_data.keys())
            self.cache_data.pop(recent[-2])
            print(f"DISCARD: {recent[-2]}")

    def get(self, key):
        """Get an item from the cache
        Args
            key:str
                The name of the item
        Return
            The value found or None"""
        return None if key is None else self.cache_data.get(key)
