
"""
Interview Questions - 5 : 
IntersectionGiven two (singly) linked lists, determine if the two lists intersect. 
Return the intersecting node. Note that the intersection is defined based on reference, 
not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
"""


from linklist import LinkedList, Node

def intersection(l1,l2):
    if l1.tail is not l2.tail:
        return False
    
    lenA = len(l1)
    lenB = len(l2)
    
    shorter = l1 if lenA < lenB else l2
    longer = l2 if lenA < lenB else l1
    
    diff = len(longer)- len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head
    
    for i in range(diff):
        longerNode = longerNode.next
        
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode  = longerNode.next
    return longerNode


#helper addition method
def addSameNode(lla, llb, value):
    tempNode = Node(value)
    lla.tail.next = tempNode
    lla.tail = tempNode
    llb.tail.next = tempNode
    llb.tail = tempNode
    
lla = LinkedList()
lla.generate(3, 0, 10)

llb = LinkedList()
llb.generate(4,0,10)

addSameNode(lla, llb, 11)
addSameNode(lla, llb, 14)

print(lla)
print(llb)
print(intersection(lla, llb).value)

