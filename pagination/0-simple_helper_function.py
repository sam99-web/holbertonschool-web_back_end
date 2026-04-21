#!/usr/bin/env python3
"""
Pagination helper module.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns the start and end index for pagination.

    Page numbers are 1-indexed (first page is page 1).

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
