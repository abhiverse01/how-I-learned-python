import asyncio
import time
from functools import wraps


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

