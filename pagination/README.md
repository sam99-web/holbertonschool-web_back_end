# Pagination

## Description

This project explores different pagination strategies for large datasets in Python. Using a CSV file of popular baby names (~19,000 rows), we implement three types of pagination: simple offset-based, hypermedia (HATEOAS), and deletion-resilient pagination.

## Learning Objectives

- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- `pycodestyle` style (version 2.5.*)
- All functions and coroutines must be type-annotated
- All modules and functions must have documentation

## Setup

Download the dataset:

```bash
# Place this file at the root of the project
Popular_Baby_Names.csv
```

## Files

| File | Description |
| --- | --- |
| `0-simple_helper_function.py` | Helper function `index_range` that returns start/end indexes for pagination |
| `1-simple_pagination.py` | `Server` class with `get_page` method — simple offset-based pagination |
| `2-hypermedia_pagination.py` | `Server` class with `get_hyper` method — returns page data + navigation metadata |
| `3-hypermedia_del_pagination.py` | `Server` class with `get_hyper_index` method — deletion-resilient pagination |

## Tasks

### 0. Simple helper function

Function `index_range(page, page_size)` returns a tuple `(start_index, end_index)`.
Pages are 1-indexed.

```python
index_range(1, 7)    # → (0, 7)
index_range(3, 15)   # → (30, 45)
```

### 1. Simple pagination

`get_page(page, page_size)` returns the correct page of the dataset.

- Uses `assert` to validate arguments (must be integers > 0)
- Returns an empty list if the page is out of range

```python
server.get_page(1, 3)      # → first 3 rows
server.get_page(3000, 100) # → []
```

### 2. Hypermedia pagination

`get_hyper(page, page_size)` returns a dictionary with:

```python
{
    'page_size'  : 2,       # length of returned data
    'page'       : 1,       # current page number
    'data'       : [...],   # the page data
    'next_page'  : 2,       # None if last page
    'prev_page'  : None,    # None if first page
    'total_pages': 9709     # total number of pages
}
```

### 3. Deletion-resilient hypermedia pagination

`get_hyper_index(index, page_size)` uses an indexed dataset (`Dict[int, List]`) to ensure no rows are skipped even if items are deleted between two queries.

```python
{
    'index'      : 3,    # start index of current page
    'data'       : [...],
    'page_size'  : 2,
    'next_index' : 5     # index to use for the next query
}
```

**How it works:** the method iterates through absolute indexes in a dictionary and simply skips missing keys (deleted rows), so deletions never cause items to be missed on subsequent pages.

## Author

Holberton School — Web Back-End