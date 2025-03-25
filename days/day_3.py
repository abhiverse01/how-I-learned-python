import asyncio
import time
from functools import wraps

# --------------------------
# Context Manager
# --------------------------
class FileOpener:
        """
        A context manager for file handling that ensures file clean-up.
        """
        def __init__(self, filepath, mode):
                self.filepath = filepath
                self.mode = mode
                self.file_obj = None

        def __enter__(self):
                self.file_obj = open(self.filepath, self.mode)
                print(f"Opened file: {self.filepath}")
                return self.file_obj

        def __exit__(self, exc_type, exc_val, exc_tb):
                if self.file_obj:
                        self.file_obj.close()
                        print(f"Closed file: {self.filepath}")
                if exc_type:
                        print(f"An error occurred: {exc_val}")
                return False  # Do not suppress exceptions

