class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CircularSinglyLinkedList:
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
            result += ' --> '
        return result
            
    
    def append(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next= new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise Exception("Index Out of Range")
        new_node = Node(value)
        
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail =  new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def traverse(self):
        current = self.head
        print("<=============== Traverse Start =================>")
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break
        print("<=============== Traverse End =================>")
        return True
    
    def search(self, value):
        index = 0
        current = self.head
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            if current.value == self.head:
                break
            index +=1
        return index
    
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index > self.length:
            raise Exception("Index out of Range")
        current = self.head
        for _ in range(index):
            current=  current.next
        return current
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first
        elif index == self.length-1:
            return self.pop()
        
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = None
        
    # Split a Circular Linked List into Two Halves
    def split_list(self):
        if self.length == 0:
            return None, None
 
        mid = (self.length + 1) // 2
        count = 1
 
        first_list = CircularSinglyLinkedList()
        second_list = CircularSinglyLinkedList()
 
        current = self.head
        last_first_list = None
 
        while count <= mid:
            first_list.append(current.value)
            last_first_list = current
            current = current.next
            count += 1
 
        # Set the tail of the first half
        if last_first_list:
            first_list.tail = last_first_list
            first_list.tail.next = first_list.head
 
        # Handle the second half
        while current != self.head:
            second_list.append(current.value)
            current = current.next
 
        # Set the tail of the second half
        if second_list.length > 0:
            second_list.tail = self.tail
            second_list.tail.next = second_list.head
 
        return first_list, second_list
            

cslinkedlist = CircularSinglyLinkedList()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
cslinkedlist.append(50)

print("Result After Append",cslinkedlist)

cslinkedlist.prepend(3)
print("Result After Prepend Method:", cslinkedlist)

cslinkedlist.insert(6, 5)
print("Result After Insert: ", cslinkedlist)

cslinkedlist.traverse()
# print("Result After Travers: ", cslinkedlist)

print("Searched Index is: ",cslinkedlist.search(30))

print("Get Method: ", cslinkedlist.get(3))

cslinkedlist.set(4, 999)
print("Result after update: ", cslinkedlist)

cslinkedlist.pop_first()
print("Result after pop first method :", cslinkedlist)

cslinkedlist.pop()
print("Result after pop method :", cslinkedlist)

cslinkedlist.remove(3)
print("Result after Remove method :", cslinkedlist)


        
    