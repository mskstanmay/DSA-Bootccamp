class Node:
    def __init__(self,value) :
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
            return True
        temp = self.root
        while(True):
            if newnode == temp:
                return False
            if newnode.value < temp.value:
                if temp.left is None:
                    temp.left = newnode
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newnode
                temp = temp.right
    def contains(self,value):
        if self.root is None:
            return False
        temp = self.root
        while(temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

mytree = BinarySearchTree()

print(mytree.contains(2),mytree.contains(4))

mytree.insert(1)
mytree.insert(2)
mytree.insert(3)

print(mytree.contains(2),mytree.contains(4))
print(mytree.root.value,mytree.root.right.value,mytree.root.right.right.value)