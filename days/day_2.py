import asyncio
import time
from functools import wraps

#!/usr/bin/env python3
"""
File: day_2.py
A collection of examples showcasing advanced Python concepts:
    - Decorators (with and without parameters)
    - Context managers
    - Generators
    - Async functions
    - Metaclasses
"""


# --------------------------
# Decorators
# --------------------------
# A simple decorator that times a function execution
def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
                return result
        return wrapper

# A decorator with parameters: it repeats function execution 'n' times
def repeat(n):
        def decorator(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                        result = None
                        for i in range(n):
                                print(f"Iteration {i + 1}/{n} for function '{func.__name__}'")
                                result = func(*args, **kwargs)
                        return result
                return wrapper
        return decorator

