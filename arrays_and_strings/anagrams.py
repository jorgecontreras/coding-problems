# Given a string "target" and a list of strings "words",
# find all strings from the list that are an anagram of the target.
# 
# Solution:
# two words are anagrams if they have the exact same characters.
# This can be checked by sorting the characters in each string and make sure both match.
#
# Time complexity: O(NlogN), we need to traverse all elements and perform a sort each time.
#
# Space complexity: O(M x N): to store the output list, 
# where M is the number of words and N the number of characters

def anagrams(target, words):
    #your code here
    anagrams = []
    target = sorted(target)

    for item in words:
        if sorted(item) == target:
            anagrams.append(item)
    return anagrams

#tests
word = 'heat'
words = ['teah', 'eaht', 'diat', 'amex', 'gold', 'time', 'cibt', 'aapl']

assert anagrams(word, words) == ['teah', 'eaht']

print("all tests passed.")