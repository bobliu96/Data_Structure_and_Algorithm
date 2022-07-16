class CircularQueue:
    def __init__(self):
        self.length = 0
        self.data = []
        self.maxSize = 5
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.length == 0

    def enqueue(self, value):
        if self.length < self.maxSize:
            if self.length == 0:
                self.data.append(value)
                self.head = 1
                self.tail = (self.head+1) % self.maxSize
                self.length += 1
            else:
                self.data.append(value)
                self.head = (self.head+1) % self.maxSize
                self.tail = (self.head+1) % self.maxSize
                self.length += 1
        else:
            print('Queue is full')

    def dequeue(self):
        if self.length == 0:
            print('empty queue')
        elif self.length == 1:
            self.data.pop(0)
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.data.pop(0)
            self.head = (self.head+1) % self.maxSize
            self.tail = (self.head + 1) % self.maxSize
            self.length -= 1

#test cases
newQueue = CircularQueue()
print(newQueue.isEmpty())
newQueue.enqueue(1)
print(newQueue.data)
newQueue.enqueue(2)
print(newQueue.data)
newQueue.enqueue(3)
print(newQueue.data)
newQueue.enqueue(4)
print(newQueue.data)
newQueue.enqueue(5)
print(newQueue.data)
print(newQueue.isEmpty())

newQueue.enqueue(6)

newQueue.dequeue()
newQueue.enqueue(6)
print(newQueue.data)
newQueue.dequeue()
newQueue.enqueue(7)
print(newQueue.data)
newQueue.dequeue()
newQueue.enqueue(8)
print(newQueue.data)
newQueue.dequeue()
newQueue.enqueue(9)
print(newQueue.data)
newQueue.dequeue()
newQueue.enqueue(10)
print(newQueue.data)

newQueue.dequeue()
print(newQueue.data)
newQueue.dequeue()
print(newQueue.data)
newQueue.dequeue()
print(newQueue.data)
newQueue.dequeue()
print(newQueue.data)
newQueue.dequeue()
print(newQueue.data)
