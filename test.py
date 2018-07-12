class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_data(data, self.root)

    def insert_data(self, data, node):
        if data < node.data:
            if node.left_node is not None:
                self.insert_data(data, node.left_node)
            else:
                node.left_node = Node(data)
        else:
            if node.right_node is not None:
                self.insert_data(data, node.right_node)
            else:
                node.right_node = Node(data)

    def min(self):
        self.min_data(self.root)

    def min_data(self, root):
        if root.left_node:
            self.min_data(root.left_node)
        else:
            print(root.left_node.data)
