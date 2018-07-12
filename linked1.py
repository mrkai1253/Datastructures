# node
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


# linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def traverse(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next


ll = SinglyLinkedList()
n = int(input("Enter the number of nodes >"))
for i in range(n):
    data = input("Enter the data >")
    ll.insert_node(data)

ll.traverse()
