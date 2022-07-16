class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("empty list")
        else:
            current = self.head
            for i in range(self.length - 2):
                current = current.next
            current.next = self.tail
            current.next.next = None
            self.length -= 1

newstack = Stack()
print(newstack.isEmpty())
newstack.push(1)
newstack.push(2)
newstack.push(3)
newstack.push(4)
print(newstack.isEmpty())
newstack.pop()
newstack.pop()
newstack.pop()
newstack.pop()
print(newstack.isEmpty())

