# You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.
#
# Example
#
# For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
# addTwoHugeNumbers(a, b) = [9876, 5434, 0].
#
# Explanation: 987654321999 + 18001 = 987654340000.
#
# For a = [123, 4, 5] and b = [100, 100, 100], the output should be
# addTwoHugeNumbers(a, b) = [223, 104, 105].
#
# Explanation: 12300040005 + 10001000100 = 22301040105.
#
#
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    number_1 = ""
    number_2 = ""
    while a:
        value = str(a.value)
        while len(value) < 4:
            value = "0" + value
        number_1 += value
        a = a.next
        
    while b:
        value = str(b.value)
        while len(value) < 4:
            value = "0" + value
        number_2 += value 
        b = b.next
    
    result = str(int(number_1) + int(number_2))
    
    answer = []
    while len(result) > 0:
        chunk = result[-4:]
        answer.insert(0, int(chunk))
        result = result[:-4]

    return answer    
