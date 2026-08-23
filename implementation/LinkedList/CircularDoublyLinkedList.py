class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node =  self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' <--> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next= new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next= new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            
    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break
            
    def search(self, value):
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return True
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
    
    def get(self, index):
        if index<0 or index >= self.length:
            return None
        current_node = None
        if index < self.length // 2:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for i in range(self.length-1, index, -1):
                current_node = current_node.prev
        return current_node
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        temp = self.get(index-1)
        new_node = Node(value)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node
        self.length += 1
        
    def pop_first(self):
        if self.head is not None:
            return None
        
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head.next
            self.length -= 1
            return popped_node
        
    def pop(self):
        if self.head is None:
            return None
        
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -=1
        return popped_node
    
    def remove(self, index):
        if self.head is None or index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def deleteAll(self):
        self.head = None
        self.tail = None
        self.length = 0
        
        
        
        
            
        
        
        
        
        
                
            
        
        
        
new_cdll = CircularDoublyLinkedList()
new_cdll.append(10)
new_cdll.append(20)
new_cdll.append(30)
new_cdll.append(10)
new_cdll.append(10)
new_cdll.prepend(100)
print("New CDLL is:", new_cdll)
new_cdll.reverse_traverse()
print("search result: ", new_cdll.search(100))
print("get result: ", new_cdll.get(4))