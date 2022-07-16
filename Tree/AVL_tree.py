class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root == None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root == node
            return
        elif value <= self.root.value:
            self.root.left = self.insert(value)
        else:
            self.root.right = self.insert(value)

        self.height = 1 + max(self.getHeight(self.root.left), self.getHeight(self.root.right))


