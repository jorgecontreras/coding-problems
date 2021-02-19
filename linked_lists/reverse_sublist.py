# Reverse Sub list
# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
#
# Time complexity: O(N)
# Space complexity: O(1)
#
# Algorithm:
#
# 1. Skip p nodes and identify last node of the left part (left) and last node of sublist (center)
#
#          center
#  left      |
#   |        |
#   v        v
# [ 1 ] -> [ 2 ] -> [ 3 ] -> [ 4 ] -> [ 5 ]
#
# 2. Reverse from p to q
#
# [ 1 ]    [ 2 ] <- [ 3 ] <- [ 4 ]   [ 5 ]
# 
# 3. connect left
#    __________________________
#   |                          |
#   |                          v
# [ 1 ]    [ 2 ] <- [ 3 ] <- [ 4 ]   [ 5 ]
#
# 4. connect right
#    __________________________
#   |                          |
#   |                          v
# [ 1 ]    [ 2 ] <- [ 3 ] <- [ 4 ]   [ 5 ]
#            |                         ^
#            |_________________________|
# 
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
    if p == q:
      return head

    # 1. skip 'p' nodes
    node, prev = head, None

    i = 1
    while node and i < p:
        prev = node
        node = node.next
        i += 1

    left = prev # last node of left part
    center = node # last node of sublist
 
    # 2. reverse nodes from p to q
    i = 0
    while node and i <= q - p:
        node.next, node, prev = prev, node.next, node
        i += 1

    # 3. connect with left part
    if left:
        left.next = prev

    else:
        head = prev

    # 4. connect with right part
    center.next = node

    return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()