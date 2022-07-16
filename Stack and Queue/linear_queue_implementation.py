class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None

    def peek(self):
        return self.head

newQueue = Queue()
print(newQueue.isEmpty())
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)
print(newQueue.isEmpty())
newQueue.dequeue()
newQueue.dequeue()
newQueue.dequeue()
print(newQueue.isEmpty())
