class Stack:
    def __init__(self):
        self.length = 0
        self.data = []
        self.maxSize = 3

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return self.length >= self.maxSize

    def push(self, item):
        if self.length < self.maxSize:
            self.data.append(item)
            self.length += 1
        else:
            print("stack is full")

    def pop(self):
        item = self.data[-1]
        self.data = self.data[:self.length-1]
        self.length -= 1
        return item

    def peek(self):
        return self.data[-1]

newstack = Stack()
print(newstack.isEmpty())
print(newstack.isFull())
newstack.push(1)
newstack.push(2)
newstack.push(3)
newstack.push(4)
print(newstack.isEmpty())
print(newstack.isFull())
newstack.pop()
newstack.pop()
newstack.pop()
print(newstack.isEmpty())
print(newstack.isFull())

