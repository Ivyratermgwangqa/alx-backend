# 0x00. Pagination

This project demonstrates how to implement pagination in Python for managing and navigating through large datasets. It includes tasks that cover simple pagination, hypermedia pagination, and deletion-resilient pagination.

## Learning Objectives

By the end of this project, you should be able to:

- Paginate a dataset using simple page and page_size parameters.
- Paginate a dataset with hypermedia metadata.
- Implement pagination in a deletion-resilient manner.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All modules should have a documentation string (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`).
- All functions should have a documentation string (e.g., `python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- All functions and coroutines must be type-annotated.

## Setup

You can use the `Popular_Baby_Names.csv` dataset provided in the project.

## Project Structure

- `0-simple_helper_function.py`: Contains the `index_range` function which calculates the start and end indices for pagination.
- `1-simple_pagination.py`: Contains the `Server` class with the `get_page` method for simple pagination.
- `2-hypermedia_pagination.py`: Extends the `Server` class with the `get_hyper` method to include pagination metadata.
- `3-hypermedia_del_pagination.py`: Further extends the `Server` class with the `get_hyper_index` method to handle pagination resilient to deletions in the dataset.
- `README.md`: This documentation file.
- `0-main.py`, `1-main.py`, `2-main.py`, `3-main.py`: Main files to test each task.
- `Popular_Baby_Names.csv`: The dataset file used for pagination tasks.

## Usage

1. **Simple Helper Function**:
    - Run `0-main.py` to test the `index_range` function.

    ```sh
    ./0-main.py
    ```

2. **Simple Pagination**:
    - Run `1-main.py` to test the `Server` class and its `get_page` method.

    ```sh
    ./1-main.py
    ```

3. **Hypermedia Pagination**:
    - Run `2-main.py` to test the `get_hyper` method in the `Server` class.

    ```sh
    ./2-main.py
    ```

4. **Deletion-Resilient Pagination**:
    - Run `3-main.py` to test the `get_hyper_index` method in the `Server` class.

    ```sh
    ./3-main.py
    ```

## Author

This project was completed as part of the ALX Backend curriculum.

```
