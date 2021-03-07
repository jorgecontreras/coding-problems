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
    
    return ans

groups = group_anagrams(["cab","cod","tin","pew","duh","may","ill","buy","int","bar","max","doc", "nit", "same", "mase", "ames"])

for tag, group in groups.items():
    print(str(tag) + ": " + str(group))