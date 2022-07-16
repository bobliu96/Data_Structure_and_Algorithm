class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        #heap[0] is filled with a random value
        self.heap[0] = 0
        self.front = 1

    def printHeap(self):
        for i in range(1, (self.size // 2)+1):
            print('Parent:'+str(self.heap[i]) +
                  'Left Child:' + str(self.heap[i * 2]) +
                  'Right Child:' + str(self.heap[i * 2 + 1]))

    def parent(self, index):
        return index // 2

    def leftChild(self, index):
        return  2 * index

    def rightChild(self, index):
        return  2 * index + 1

    def isLeaf(self, index):
        return (index > self.size // 2) and index <= self.size

    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def maxHeapify(self, index):
        #if node is a non-leaf node
        if not self.isLeaf(index):
            left_index = self.leftChild(index)
            right_index = self.rightChild(index)

            #if node is smaller than both of its child
            if self.heap[index] < self.heap[left_index] or self.heap[index] < self.heap[right_index]:

                #left child bigger than right child
                if self.heap[left_index] > self.heap[right_index]:
                    #swap node and left child
                    self.swap(index, left_index)
                    #maxheapify left child
                    self.maxHeapify(left_index)

                #right child is bigger or equal to left child
                else:
                    #swap node and right child
                    self.swap(index, right_index)
                    #maxheapify right child
                    self.maxHeapify(right_index)

    def insert(self, value):
        if self.size > self.maxsize:
            return
        self.size += 1
        self.heap[self.size] = value
        current = self.size

        while self.heap[current] >= self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def extract_max(self):
        pop = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.heap[self.size] = 0
        self.size -= 1
        self.maxHeapify(self.front)
        return pop


heap = MaxHeap(7)
heap.insert(30)
heap.insert(20)
heap.insert(10)
heap.insert(40)
heap.insert(50)
heap.insert(70)
heap.insert(60)
heap.printHeap()
