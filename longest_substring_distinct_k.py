# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

def longest_distinct(str, k):
    l = 0
    longest = 0
    distinct = {}

    for r in range(len(str)):
        distinct[str[r]] = distinct.get(str[r], 0) + 1
        
        while len(distinct) > k:
            distinct[str[l]] -= 1
            if distinct[str[l]] == 0:
                del distinct[str[l]]
            l += 1
        longest = max(longest, r-l+1)
    return longest

t1 = "araaci"
t2 = "araaci"
t3 = "cbbebi"

assert longest_distinct(t1, 2) == 4
assert longest_distinct(t2, 1) == 2
assert longest_distinct(t3, 3) == 5