#!/usr/bin/env python3
'''Module for Task 1
'''
import csv
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Calculates the start and end index
    for a given page and page size
    '''
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)


class Server:
    """Server class to paginate a
    database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Retrieves a specific page of data.
        '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert (page > 0 and page_size > 0)
        startIndex, endIndex = index_range(page, page_size)
        paginatedData = self.dataset()
        if startIndex > len(paginatedData):
            return []
        return paginatedData[startIndex:endIndex]
