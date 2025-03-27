# Dynamic Resizing
# Description: This program demonstrates the dynamic resizing of an array using the concept of pointers in Python.


import sys
lst = []
for i in range(10):
    print(f"Size: {len(lst)}, Capacity: {sys.getsizeof(lst)} bytes")
    lst.append(i)

"""
Output:
Size: 0, Capacity: 56 bytes
Size: 1, Capacity: 88 bytes
Size: 2, Capacity: 88 bytes
Size: 3, Capacity: 88 bytes
Size: 4, Capacity: 88 bytes
Size: 5, Capacity: 120 bytes
Size: 6, Capacity: 120 bytes
Size: 7, Capacity: 120 bytes
Size: 8, Capacity: 120 bytes
Size: 9, Capacity: 184 bytes

"""