#!/usr/bin/env python3
'''Module for Task 0
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Calculates the start and end index
    for a given page and page size
    '''
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)
