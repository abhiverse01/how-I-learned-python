import asyncio
import time
from functools import wraps
from days.day_3 import Fileopener
# --------------------------
# Generators
# --------------------------
# A generator that yields squares of numbers up to n
def squares(n):
        for i in range(1, n + 1):
                yield i ** 2

# --------------------------
# Async Functions (Coroutines)
# --------------------------
async def async_countdown(n):
        while n > 0:
                print(f"Async countdown: {n}")
                await asyncio.sleep(1)
                n -= 1
        print("Countdown complete!")


# --------------------------
# Metaclass
# --------------------------
class AutoRepr(type):
        """
        A metaclass that automatically creates a __repr__ method for classes.
        """
        def __new__(cls, name, bases, dct):
                if '__repr__' not in dct:
                        def __repr__(self):
                                attrs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
                                return f"{name}({attrs})"
                        dct['__repr__'] = __repr__
                return super().__new__(cls, name, bases, dct)

class Person(metaclass=AutoRepr):
        def __init__(self, name, age):
                self.name = name
                self.age = age


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


# --------------------------
# Sample Functions using decorators
# --------------------------
@timer
def compute_squares(n):
        # Using the generator to compute squares and summing them up
        total = sum(sq for sq in squares(n))
        print(f"Sum of squares up to {n}: {total}")
        return total

@repeat(3)
def greet(name):
        print(f"Hello, {name}!")

# --------------------------
# Main Execution
# --------------------------
def main():
        # Using compute_squares with a timer decorator
        compute_squares(10)

        # Using greet with repeat decorator
        greet("Python Enthusiast")

        # Using FileOpener context manager to read/write from a temporary file
        temp_filename = "temp.txt"
        with FileOpener(temp_filename, "w") as f:
                f.write("Learning advanced Python concepts!")
        
        # Demonstrate the generator usage:
        print("Squares generated:")
        for sq in squares(5):
                print(sq, end=" ")
        print("\n")

        # Demonstrate the metaclass by creating a Person instance
        p = Person("Alice", 30)
        print("Person instance:", p)

        # Running the async countdown
        print("Starting async countdown...")
        asyncio.run(async_countdown(3))

if __name__ == "__main__":
        main()