# encrypted words

# ex. a, b, c : bac
# 
# ex. abcxcba: xbacbca

# mid = 3
# 
# abc
# mid = 1
# a
# time complexity O(NlogN)
# space complexity: O(1)

def encrypt(text):

    # base case
    if len(text) < 2:
        return text

    start, end = 0, len(text) - 1
    mid = start + (end-start) // 2

    left = encrypt(text[start:mid])
    right = encrypt(text[mid+1:])

    return text[mid] + left + right


t2 = "abcxcba"
expected_2 = "xbacbca"
output_2 = encrypt(t2)

assert expected_2 == output_2