class Node:
    def __init__(self, data=None):
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

    def insert_at_post(self, data, pos):

        head = self.head
        count = 0
        prev = None
        n = Node(data)
        while count != pos:
            count = count + 1
            prev = head
            head = head.next
        print('Count ',count)
        print('last head', head.data)
        print('Prev', prev.data)

        prev.next = n
        n.next = head



l = LinkedList()
l.insert(7)
l.insert(13)
l.insert(16)
l.insert(12)
l.insert(14)
l.insert(14)
l.insert(1)
l.insert(2)
l.insert(3)
l.print()

print('#' * 40)

l.insert_at_post('Asish', 2)

l.print()
