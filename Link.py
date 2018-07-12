class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.traverse(data)

    def traverse(self, data):
        node = self.head
        while node != None:
            node = node.next
        node = Node(data)

    def print(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next



l = Linked()

l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)

l.insert(16)

l.print()