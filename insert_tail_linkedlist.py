# Insert a Node at the Tail of a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertNodeAtTail(self, head, data):

        if head.next is None:
            head.next = Node(data)
        else:
            self.insertNodeAtTail(head.next, data)

    def print(self):
        ptr = self.head
        while ptr != None:
            print(ptr.data)
            ptr = ptr.next


l = LinkedList()
l.insert(12)
l.insert(123)
l.insert(122)
l.insert(123)

l.insertNodeAtTail(l.head, 0)

l.print()
