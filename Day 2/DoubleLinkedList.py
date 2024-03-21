class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self,value):
        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end = " ")
            temp = temp.next
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+= 1
        return True

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        return True
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1,index, -1):
                temp = temp.prev
        return temp            
    def insert(self,index,value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        before.next = new_node
        new_node.next = after
        after.prev = new_node
        new_node.prev = before

    def pop(self):
        end = self.tail.prev
        self.tail = end
        end.next = None
        self.length -=1
    
    def pop_first(self):
        term = self.head.next
        self.head = term
        term.prev = None
        
        self.length -=1

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
           return self.pop()
        before = self.get(index - 1)
        after = before.next.next

        before.next = after
        after.prev = before
        self.length -= 1
dll = DoubleLinkedList(1)

dll.prepend(0)
dll.print_list()
print()
dll.append(2)
dll.append(4)
dll.append(5)

dll.insert(3,3)
dll.print_list()

