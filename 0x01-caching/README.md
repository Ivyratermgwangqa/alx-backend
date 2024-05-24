# 0x01. Caching

This project is about implementing different caching algorithms in Python. The goal is to understand and apply various cache replacement policies, such as FIFO, LIFO, LRU, MRU, and LFU.

## Learning Objectives

By the end of this project, you should be able to:

- Explain what a caching system is.
- Describe the purpose of a caching system.
- Understand the limits of a caching system.
- Explain the following cache replacement policies:
  - FIFO (First In First Out)
  - LIFO (Last In First Out)
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)
  - LFU (Least Frequently Used)

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` style (version 2.5).
- All files must be executable.
- The length of your files will be tested using `wc`.
- All modules should have a documentation.
- All classes should have a documentation.
- All functions (inside and outside a class) should have a documentation.

## File Descriptions

### `base_caching.py`

This module defines the `BaseCaching` class, which serves as the base for all caching systems. It contains:
- A dictionary `self.cache_data` to store the cache items.
- Constants and methods to manage the cache.

### `0-basic_cache.py`

This module defines the `BasicCache` class, which inherits from `BaseCaching` and implements a basic caching system with no limits.

### `1-fifo_cache.py`

This module defines the `FIFOCache` class, which inherits from `BaseCaching` and implements a caching system using the FIFO (First In First Out) replacement policy.

### `2-lifo_cache.py`

This module defines the `LIFOCache` class, which inherits from `BaseCaching` and implements a caching system using the LIFO (Last In First Out) replacement policy.

### `3-lru_cache.py`

This module defines the `LRUCache` class, which inherits from `BaseCaching` and implements a caching system using the LRU (Least Recently Used) replacement policy.

### `4-mru_cache.py`

This module defines the `MRUCache` class, which inherits from `BaseCaching` and implements a caching system using the MRU (Most Recently Used) replacement policy.

### `100-lfu_cache.py`

This module defines the `LFUCache` class, which inherits from `BaseCaching` and implements a caching system using the LFU (Least Frequently Used) replacement policy.

## How to Use

Each cache class can be tested using its corresponding main file. For example, to test `BasicCache`, run:

```sh
./0-main.py
```

This will execute the test cases defined in `0-main.py` and demonstrate the functionality of the `BasicCache` class.

## Author

This project is part of the ALX Back-end curriculum.
```
