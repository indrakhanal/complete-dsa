"""
Merge Two Sorted Linked List
You are given the heads of two sorted linked lists list1 and list2. 

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.   
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):
    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next
        
class Solution(object): 
    def mergeTwoList(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        return dummy.next
    
    def deleteDuplicates(self, head):
        current = head
        
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
    # Remove Linked List Elements
    def removeElements(self, head, val):
        dummy_node = ListNode(-1)
        dummy_node.next = head
        
        prev_node, curr_node = dummy_node, head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node.next = curr_node
            curr_node = curr_node.next
            
        return dummy_node.next
            
    #Reverse Linked List
    def reverseList(self, head):
        prev_node = None
        curr_node = head
 
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node
    

head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
print(head.next.val)
solution = Solution()
result = solution.removeElements(head, 6)

print(print_linked_list(result))
