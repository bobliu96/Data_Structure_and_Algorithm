class Array2D:
    def __init__(self):
        self.length = 0
        self.data = []

    def search(self, row, col):
        return self.data[row][col]

    def traverse(self):
        for i in self.data:
            for j in self.data[i]:
                print(i, j)

    def insert(self, row, item):
        while self.length <= row:
            self.data.append([])
            self.length += 1
        self.data[row].append(item)
        return self.data


newArray = Array2D()
newArray.insert(3,1)
newArray.insert(5,2)
print(newArray.data)
