```python
class Node:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class SyntaxTree:
    def __init__(self):
        self.root = Node('program')

    def add_node(self, node, parent=None):
        if parent is None:
            parent = self.root
        parent.add_child(node)

    def traverse(self, node=None):
        if node is None:
            node = self.root

        print(f'Node: {node.type}, Value: {node.value}')

        for child in node.children:
            self.traverse(child)
```