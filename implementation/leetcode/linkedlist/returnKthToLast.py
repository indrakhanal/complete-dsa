from linklist import LinkedList

def nthToLast(l1, n):
    pointer1 = l1.head
    pointer2 = l1.head
    
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
        
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
abc = nthToLast(customLL, 3)
print(abc.value)