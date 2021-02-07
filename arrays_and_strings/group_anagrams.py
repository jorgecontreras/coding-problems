# group anagrams

# Given an array of strings, group anagrams together.

# For example, given the following array:

# ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
# Return:

# [['eat', 'ate', 'tea'],
# ['apt', 'pat'],
# ['now']]

# Intuition: Two strings are anagrams if and only if their sorted strings are equal.

from collections import defaultdict

def group_anagrams(words):
    ans = defaultdict(list)
    for word in words:
        ans[tuple(sorted(word))].append(word)
    
    return ans.values()

print(group_anagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))