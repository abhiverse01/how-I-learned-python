# Binary Search Tree (BST) Implementation in Python

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
            else:
                self._insert(node.left, data)
        else:
            if not node.right:
                node.right = BSTNode(data)
            else:
                self._insert(node.right, data)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# Example Usage
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)

print("In-Order Traversal (Sorted Order):")
bst.inorder_traversal(bst.root)  # Output: 20 30 40 50 70

print("\nSearch for 40:", bst.search(40))  # Output: True
print("Search for 100:", bst.search(100))  # Output: False


# Breadth-First Search Algorithm
# Breadth-First Search (BFS) is an algorithm used for traversing tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

from collections import deque

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print("Level-Order Traversal:")
level_order_traversal(bst.root)  # Output: 50 30 70 20 40


"""
Output:

In-Order Traversal (Sorted Order):
20 30 40 50 70 
Search for 40: True
Search for 100: False
Level-Order Traversal:
50 30 70 20 40 

"""