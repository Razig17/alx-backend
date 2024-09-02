#!/usr/bin/env python3
"""
This module contains a helper function that
returns the index range for pagination parameters.
"""

from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and end index for the
    given page number and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index = index_range(page, page_size)
        rows = self.dataset()
        if index[0] < len(rows) and index[1] <= len(rows):
            return rows[index[0]:index[1]]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing the following key-value pairs:
        page: the current page number
        page_size: the current page size
        data: the page of the dataset
        data_length: the length of the dataset
        next_page: the next page number
        """
        rows = self.dataset()
        data = self.get_page(page, page_size)
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(rows) / page_size)
        next_page = page + 1 if page < total_pages else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
