# Hybrid Data Structures
## Array + Stack Hybrid

"""
efficient random access (from the array) and efficient last-in-first-out (LIFO) operations (from the stack). Let's implement a hybrid data structure in Python, where we can use both array-like indexing and stack-like operations (push, pop).

Key Features:
Random Access (Array-like): Ability to access elements in constant time (O(1)) using indices.
Stack Operations (Stack-like): push and pop operations that efficiently add/remove elements from the end of the structure.
Flexibility: We can provide constant-time access to both the top of the stack and any element of the array, making this structure useful for scenarios where both behaviors are needed.
Use Case Examples:
Browser History: Stack operations allow easy access to the most recent pages visited, and array-like indexing allows you to quickly access any previous page.
Undo-Redo Systems: In text editors, you can use this structure to quickly access both the current state (stack-like) and previous states (array-like access).
Game States: Efficient access to game states (array-like) while supporting state-saving with undo/redo (stack-like operations).

"""

class HybridArrayStack:
    def __init__(self):
        self.data = []

    # Stack-like: Push an element to the end of the array (acts like stack)
    def push(self, value):
        self.data.append(value)

    # Stack-like: Pop the last element (acts like stack)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.data.pop()

    # Array-like: Access element by index
    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

    # Stack-like: Peek at the top element (last element added)
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.data[-1]

    # Array-like: Set element at a specific index
    def set(self, index, value):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        self.data[index] = value

    # Array-like: Check if the array/stack is empty
    def is_empty(self):
        return len(self.data) == 0

    # Array-like: Get the current size of the hybrid structure
    def size(self):
        return len(self.data)

    # Array-like: Print the contents of the structure
    def print_structure(self):
        print("Hybrid Array-Stack:", self.data)

# Example Usage
hybrid = HybridArrayStack()

# Stack-like operations
hybrid.push(10)
hybrid.push(20)
hybrid.push(30)
hybrid.print_structure()  # Output: [10, 20, 30]

print("Popped:", hybrid.pop())  # Output: 30 (stack-like pop)
hybrid.print_structure()  # Output: [10, 20]

# Array-like access
print("Element at index 1:", hybrid.get(1))  # Output: 20
hybrid.set(1, 50)
print("After setting index 1 to 50:", hybrid.get(1))  # Output: 50

# Peek (stack-like)
print("Peek:", hybrid.peek())  # Output: 50

hybrid.print_structure()  # Output: [10, 50]



"""
Explanation of Methods:
push(value): Adds an element to the end of the array (stack-like behavior).
pop(): Removes the last element from the array (stack-like behavior).
get(index): Returns the element at a specified index (array-like behavior).
set(index, value): Updates the value at a given index (array-like behavior).
peek(): Returns the last element without removing it (stack-like behavior).
is_empty(): Checks if the data structure is empty.
size(): Returns the current size of the structure.
print_structure(): Prints the contents of the data structure for debugging.

"""


"""

Performance:
Push/Pop Operations: Both push and pop have a time complexity of O(1), making them very efficient for stack-like operations.
Random Access (get/set): Accessing or updating an element by its index also has a time complexity of O(1), leveraging the array-like indexing benefits.

"""
