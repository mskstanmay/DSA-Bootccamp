class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self, value=None):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def getNode(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
 
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            prev_node = self.getNode(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1

    def display(self):
        current = self.head
        while current is not None:
            print(current.value,end = " ")
            current = current.next
        print("None")

# Initialize an empty LinkedList
a = SingleLinkedList()
a.prepend(0)
a.append(2)
a.insert(1,1)
a.display()
