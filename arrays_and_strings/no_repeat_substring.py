# no repeat substring

def solve(s):
    start = longest = 0
    positions = {}

    for i in range(len(s)):
        if s[i] in positions:
            #calculate length
            longest = max(longest, i - start)
            start = max(start, positions[s[i]] + 1)
        
        positions[s[i]] = i
    return longest

t1 = "aabccbb"
t2 = "abbbb"
t3 = "abccde"
t4 = "gzxcvbxdfdfgdfoiuytewplplpgt"

assert solve(t1) == 3
assert solve(t2) == 2
assert solve(t3) == 3
assert solve(t4) == 12
