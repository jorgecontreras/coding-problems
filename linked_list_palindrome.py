
# Given a singly linked list of integers, determine whether or not it's a palindrome.

# Example

# For l = [0, 1, 0], the output should be
# isListPalindrome(l) = true;

# For l = [1, 2, 2, 3], the output should be
# isListPalindrome(l) = false.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverseList(node):
    prev = None
    while(node):
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt
    return prev
    
def isListPalindrome(l):
    if l is None:
        return True
    
    # find the middle of the list using two pointers
    slow, fast = l, l
    while slow and fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    left = l
    right = reverseList(slow)
    
    #compare both lists
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    
    return True
