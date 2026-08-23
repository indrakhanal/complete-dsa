"""
Write code to partition a linked list around a value x, such that all node less than x come before all nodes greater then or equals to x
"""


from linklist import LinkedList

def partition(l1, x):
    currNode = l1.head
    l1.tail = l1.head
    
    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value <= x:
            currNode.next = l1.head
            l1.head = currNode
        else:
            l1.tail.next = currNode
            l1.tail = currNode
        currNode = nextNode
    if l1.tail.next is not None:
        l1.tail.next = None
        
customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
partition(customLL, 80)
print(customLL)

