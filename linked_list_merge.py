## Given two singly linked lists sorted in non-decreasing order,
## your task is to merge them. In other words, return a singly linked list, 
## also sorted in non-decreasing order, that contains the elements from both original lists.


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    l3 = None
    l3_head = None
    
    while l1 and l2:
        if l1.value < l2.value:
            if l3:
                l3.next = ListNode(l1.value)
                l3 = l3.next
            else:
                l3 = ListNode(l1.value)
                l3_head = l3
            l1 = l1.next
        else:
            if l3:
                l3.next = ListNode(l2.value)
                l3 = l3.next
            else:
                l3 = ListNode(l2.value)
                l3_head = l3
            l2 = l2.next
                
    while l1:
        if l3:
            l3.next = ListNode(l1.value)
            l3 = l3.next
        else:
            l3 = ListNode(l1.value)
            l3_head = l3
        l1 = l1.next
            
    while l2:
        if l3:
            l3.next = ListNode(l2.value)
            l3 = l3.next
        else:
            l3 = ListNode(l2.value)
            l3_head = l3
        l2 = l2.next
            
    return l3_head
