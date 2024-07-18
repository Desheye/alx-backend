#!/usr/bin/env python3
'''Module for Task 2'''
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Get start and end index for a page'''
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)


class Server:
    """Server to paginate baby names database"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Get a page of data'''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        startIndex, endIndex = index_range(page, page_size)
        paginatedData = self.dataset()
        if startIndex > len(paginatedData):
            return []
        return paginatedData[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''Get hypermedia info for a page'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        page_info = {
            'page_size': page,
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_page': total_pages,
        }
        return page_info
