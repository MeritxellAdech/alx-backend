#!/usr/bin/env python3
"""
index_range function
"""


def index_range(page, page_size):
    """Establishes the range index
    Args
        page:int
        The page number to retrieve data from
        page_size:int
        The number of rows to retrieve from
    Return
        The range retrieve as tuple
    """
    size = page * page_size
    return (size - page_size, size)
