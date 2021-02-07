class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        node = ListNode(value)
        
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = node
        self.size += 1


    def traverse(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            
def reverseList(node):
    prev = None
    while node:
        node.next, prev, node = prev, node, node.next

    return prev

class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        first = head
        second = reverseList(slow)
        
        while second:
            if first.value != second.value:
                return False
            first = first.next
            second = second.next
        return True


test_case = [1,2,3,3,2,1]

linked_list = LinkedList()

for n in test_case:
    linked_list.insert(n)

solution = Solution()

answer = solution.is_palindrome(linked_list.head)

print(answer)

