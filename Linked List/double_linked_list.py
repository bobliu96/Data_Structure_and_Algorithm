class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        string = ''
        node = self.head

        while node is not None:
            if node.next is not None:
                string += str(node.value) + '-->'
            else:
                string += str(node.value)
            node = node.next
        return string

    def insert(self, index, value):
        node = Node(value)
        if index > self.length:
            print('Input index out of range')

        elif index == self.length:
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            self.length += 1

        elif index == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.length += 1

        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.length += 1

    def search(self, value):
        if value == self.head.value:
            return True
        else:
            current = self.head
            for i in range(self.length-1):
                current = current.next
                if value == current.value:
                    return True
            return False

    def remove(self,index):
        if self.length == 0:
            print('empty list')

        elif index > self.length:
            print('Input index out of range')

        elif index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            elif self.length == 2:
                self.head = self.head.next
                self.tail = self.head
                self.head.prev = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1
            return

        current = self.head
        for i in range(index-1):
            current = current.next
        current.next = current.next.next
        current.next.prev = current
        self.length -= 1
        if current.next == None:
            self.tail = current

newLinkedList = DoubleLinkedList()
newLinkedList.insert(0,0)
newLinkedList.insert(1,1)
newLinkedList.insert(2,2)
newLinkedList.insert(3,4)
print(newLinkedList.search(2))
#newLinkedList.remove(3)
print(str(newLinkedList))
