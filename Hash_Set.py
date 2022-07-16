class HashTable:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def __hash(self, key):

        return key % self.size

    def insert(self, key):
        location = self.__hash(key)

        if self.data[location] is None:
            self.data[location] = [key]
        else:
            self.data[location].append(key)

    def get(self, key):
        location = self.__hash(key)

        if self.data[location] is None:
            raise KeyError()
        else:
            return key in self.data[location]

    def remove(self, key):
        location = self.__hash(key)

        if self.data[location] is not None:
            while key in self.data[location]:
                self.data[location].remove(key)


myHash = HashTable(1000)
myHash.insert(20)
myHash.insert(50)
myHash.get(20)
myHash.get(5)