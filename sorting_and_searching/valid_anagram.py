"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

def is_anagram(w1, w2):
    return tuple(sorted(w1)) == tuple(sorted(w2))

assert is_anagram("anagram", "anagram") == True
assert is_anagram("rat", "car") == False

print("all tests passed.")
