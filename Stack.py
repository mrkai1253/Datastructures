# LIFO
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data =(self.stack[-1])
        del self.stack[-1]
        return data

    def print_data(self):
        for i in range(len(self.stack)):
            print(self.stack[i])


s = Stack()
for i in range(10):
    s.push(i)
s.print_data()
print(s.pop()," popped")
s.print_data()
