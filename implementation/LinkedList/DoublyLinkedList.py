class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        result = ''
        temp_node = self.head
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '  <=>  '
            temp_node = temp_node.next
        return result
        
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
    def reverse_traverse(self):
        tail_node = self.tail
        while tail_node:
            print(tail_node.value)
            tail_node = tail_node.prev
            
    def search(self, value):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            index += 1
            current_node = current_node.next
        return None
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            curret_node = self.head
            for _ in range(index):
                curret_node = curret_node.next
        else:
            curret_node = self.tail
            for _ in range(self.length -1, index, -1):
                curret_node = curret_node.prev
        return curret_node
    
    def set_value(self, index, value):
        update_val = self.get(index)
        if update_val:
            update_val.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return 'Error'
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        temp_node = self.get(index-1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        
    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        popped_node = self.head
        self.head = self.head.next
        self.head.prev = None
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        poppend_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        self.tail = self.tail.prev
        self.tail.next = None
        poppend_node.prev = None
        self.length -=1
        return poppend_node
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return 'Error'
        if index == 1:
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
        
    
    
        
                
            
            
        
        
        
new_Dll = DoublyLinkedList()
new_Dll.append(10)
new_Dll.append(20)
new_Dll.append(30)
new_Dll.append(40)
new_Dll.append(50)

new_Dll.prepend(5)
print("<===========Traversal Result==============>")
print(new_Dll.traverse())
print("<===========Traversal Result End==============>")

print("<===========Reverse Traversal Result==============>")
print(new_Dll.reverse_traverse())
print("<===========Reverse Traversal Result End==============>")

print("Search value is at Index of:",  new_Dll.search(500))



