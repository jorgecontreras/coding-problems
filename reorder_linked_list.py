# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
# 3 steps:

# 1. find middle point
# 2. reverse second half
# 3. merge the two lists appending one of each

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        while self.head:
            print(self.head.val)
            self.head = self.head.next 

    def append(self, val):

        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while(current.next):
                current = current.next 
            current.next = node

    def size(self):
        size = 0
        while self.head:
            self.head = self.head.next
            size += 1

        return size

    def reorder(self):
        
        # find middle point of the list using fast and slow pointers
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        prev, node = None, slow
        while node:
            node.next, prev, node = prev, node, node.next
        
        # self.head is the start of the first list
        # prev is the start of the second list
        l1, l2 = self.head, prev

        while l2.next:
            l1.next, l1 = l2, l1.next 
            l2.next, l2 = l1, l2.next



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    


# create sample list
linked_list = LinkedList()

nums = [1,2,3,4,5]
for n in nums:
    linked_list.append(n)

linked_list.reorder()
linked_list.display()

