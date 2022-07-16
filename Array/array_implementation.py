class Array:
    def __init__(self):
        self.length = 0
        self.data = []

    def search(self, index):
        return self.data[index]

    def traverse(self):
        for i in range(len(self.data)):
           print([i,self.data[i]])

    def insert(self, item):
        self.data.append(item)
        self.length += 1
        return self.data

    def delete(self, index):
        item = self.data[index]
        self.shiftItem(index)
        return item

    def update(self,index,item):
        self.data[index] = item
        return self.data

    def shiftItem(self, index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        self.data = self.data[:self.length-1]
        self.length -= 1

newArray = Array()
newArray.insert('1')
newArray.insert('2')
newArray.insert('3')
print(newArray.search(1))
newArray.delete(1)
print(newArray.data)
