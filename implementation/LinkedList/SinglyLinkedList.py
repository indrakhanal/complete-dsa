class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail  = new_node
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
        
    def insert(self,index, value):
        new_node = Node(value)
        if index<0 or index>self.length:
            return False
        elif self.head is None:
            self.head = new_node
            self.tail  = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            
        self.length += 1
        return True
    def traverse(self):
        current  = self.head
        while current:
            print(current.value)
            current = current.next
    
    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        current_ = self.head
        if index < 0 or index>self.length:
            return False
        else:
            for _ in range(index):
                current_ = current_.next
            return current_
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
            
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index > self.length or index < 0:
            return None
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            
        self.length -= 1
        
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head
        
    def find_middle(self):
        if self.length == 0:
            return None
        lengt = int(self.length/2)
        
        current = self.head
        for _ in range(lengt):
            current = current.next
        return current
    
    def remove_duplicates(self):
        if self.head is None:
            return
        node_values =  set()
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node
            
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
        
        
                
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(f"New List after appending: {new_linked_list}")
new_linked_list.prepend(50)
a = new_linked_list.insert(0, 40)

print(new_linked_list, a)
new_linked_list.traverse()
print("Index is: ", new_linked_list.search(10))

print("Get Method Result: ", new_linked_list.get(3).value)

new_linked_list.set(3, 33)
print("Final", new_linked_list)

new_linked_list.reverse()
print("Reverse Link List", new_linked_list)

new_linked_list.pop_first()
print("After POP First Node new List: ", new_linked_list)

new_linked_list.pop()
print("List After POP Operation: ", new_linked_list)

new_linked_list.remove(2)
print("After remove method: ",new_linked_list)

new_linked_list.delete_all()
print("After Deleting All element fro list: ", new_linked_list)


