from turtle import left


class Node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val
        self.height = 1

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, val):
        pass