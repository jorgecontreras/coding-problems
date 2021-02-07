"""
Problem Statement #
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

"aaabccddeefefeaaa" k=2
output: 6

"aabbcbcbbddefefefefefe" k=2
output: 7
"""

# most frequency? not necessarily
# less variability? ex efefef? no
# distance between same letters?

def longest(s, k):
    start, longest, max_repeat = 0, 0, 0
    frequency = {}

    for i in range(len(s)):
        frequency[s[i]] = frequency.get(s[i], 0) + 1
        max_repeat = max(max_repeat, frequency[s[i]])
        
        if i - start + 1 - max_repeat > k:
            frequency[s[start]] -= 1 
            start += 1
        longest = max(longest, i - start + 1)
    return longest

def main():
  print(longest("aabccbb", 2))
  print(longest("abbcb", 1))
  print(longest("abccde", 1))
  print(longest("aabbcbcbbddefefefefefe", 2))
  print(longest("aaabccddeefefeaaa", 2))



main()