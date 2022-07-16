class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return
        current = self.root
        while current != None:
            if value <= current.value:
                if current.left:
                    current = current.left
                    continue
                current.left = node
                return
            else:
                if current.right:
                    current = current.right
                    continue
                current.right = node
                return

    def search(self, value):
        if self.root == None:
            return False
        current = self.root
        while current != None:
            if value < current.value:
                if current.left:
                    current = current.left
                    continue
                return False
            elif value > current.value:
                if current.right:
                    current = current.right
                    continue
                return False
            else:
                return True

    def remove(self, value):
        if self.root == None:
            return 'Empty Tree'
        current_node = self.root
        parent_node = None
        while current_node != None:
            if current_node.value > value:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                parent_node = current_node
                current_node = current_node.right
            elif current_node.value == value: #match is found
                #left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.value >= current_node.value:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return
                #right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.value >= current_node.value:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                #no left and right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None:
                        current_node = None
                        return
                    if parent_node.value >= current_node.value:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                #both left and right has child
                elif current_node.left != None and current_node.right != None:
                    delete_node = current_node.right
                    delete_node_parent = current_node.right
                    while delete_node.left != None:
                        delete_node_parent = delete_node
                        delete_node = delete_node.left
                    current_node.value = delete_node.value
                    if delete_node == delete_node_parent:
                        current_node.right = delete_node.right
                        return
                    if delete_node.right == None:
                        delete_node_parent.left = None
                        return
                    else:
                        delete_node_parent.left = delete_node.right
                        return
        return 'Value not found'

    def Traverse(self, value):
        if self.root == None:
            return 'Empty Tree'
        elif value == 'preorder':
            self.preorder(self.root)
        elif value == 'inorder':
            self.inorder(self.root)
        elif value == 'postorder':
            self.postorder(self.root)
        else:
            return'Invalid Traverse Method'

    def preorder(self, node):
        if node != None:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def postorder(self, node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)

bst = BST()
bst.insert(80)
bst.insert(20)
bst.insert(30)
bst.insert(60)
bst.insert(40)
bst.insert(50)
bst.Traverse('preorder')
bst.Traverse('inorder')
bst.Traverse('postorder')
print(bst.search(10))
