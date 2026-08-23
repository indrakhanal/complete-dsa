"""
nterview Questions - 4 : Sum Lists
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
"""

from linklist import LinkedList

def sumList(lla, llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0
    l1 = LinkedList()
    
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        l1.add(int(result % 10))
        carry = result / 10
    return l1

lla  = LinkedList()
lla.add(7)
lla.add(1)
lla.add(6)

llb = LinkedList()
llb.add(5)
llb.add(9)
llb.add(2)

print(lla)
print(llb)
print(sumList(lla, llb))
