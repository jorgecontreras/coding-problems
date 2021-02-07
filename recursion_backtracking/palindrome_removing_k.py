"""
Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrxfetaw' and a k of 2, you could delete f and x to get 'waterretaw'.

test case.
watercwaterx True
wateropretaw True
"""

def recurse(s1, s2, m, n):
    #finished m
    if not m: return n

    #finished n
    if not n: return m

    #both chars match, remove both and 
    #continue recursing with remaining chars
    if s1[m-1] == s2[n-1]:
        return recurse(s1, s2, m-1, n-1)

    #remove one or the other
    cost = 1 + min(recurse(s1, s2, m-1, n), recurse(s1, s2, m, n-1)) 

    return cost



def is_k_palindrome(s, k):
    reversed_string = s[::-1]
    m = n = len(s)

    rem = recurse(s, reversed_string, m, n)
    return rem <= k*2

    
t1 = "waterretaw"
k1 = 2

print(is_k_palindrome(t1, k1))

