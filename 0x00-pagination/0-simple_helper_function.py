#!/usr/bin/env python3
"""
This module contains a helper function that
returns the index range for pagination parameters.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and end index for the
    given page number and page size.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
