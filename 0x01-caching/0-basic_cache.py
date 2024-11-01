#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    - is a basic implementation of a caching system
    - it inherits rom BaseCaching class
    """

    def __init__(self):
        """Initialize BasicCache"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
