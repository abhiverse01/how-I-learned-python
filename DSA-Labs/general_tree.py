# General Tree Implementation in Python

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, parent, child_data):
        new_node = TreeNode(child_data)
        if not self.root:
            self.root = new_node
        else:
            parent.children.append(new_node)

    def traverse(self, node):
        if not node:
            return
        print(node.data, end=" ")
        for child in node.children:
            self.traverse(child)

# Example Usage
tree = Tree()
tree.add_node(None, "A")           # Root
tree.add_node(tree.root, "B")      # Child of A
tree.add_node(tree.root, "C")      # Child of A
tree.add_node(tree.root.children[0], "D")  # Child of B

print("General Tree Traversal (Pre-Order):")
tree.traverse(tree.root)  # Output: A B D C