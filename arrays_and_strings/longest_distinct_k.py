"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

def solve(s, k):
    d = {}
    start = 0
    longest = 0
    for i in range(len(s)):
        d[s[i]] = d.get(s[i], 0) + 1
        while len(d) > k:
            removed = s[start]
            d[removed] -= 1
            if d[removed] == 0:
                del d[removed]
            start += 1
        longest = max(longest, i-start+1)
            
    
    return longest

t1 = "araaci"
k1 = 2

t2 = "araaci"
k2 = 1

t3 = "cbbebi"
k3 = 3

assert solve(t1, k1) == 4
assert solve(t2, k2) == 2
assert solve(t3, k3) == 5

print("Tests passed.")
