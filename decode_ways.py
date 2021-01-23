# Decode ways

# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "111" can have each of its "1"s be mapped into 'A's to make "AAA", or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA". Note that "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a non-empty string num containing only digits, return the number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.
from functools import lru_cache

@lru_cache
def decode_with_memo(index, s):    
    if index == len(s):
        return 1

    # in char is 0, it cant be decoded
    if s[index] == '0':
        return 0

    if index == len(s)-1:
        return 1

    answer = decode_with_memo(index + 1, s)
    if int(s[index:index+2]) <= 26:
        answer += decode_with_memo(index + 2, s)

    return answer

def decode_ways(text):
    return decode_with_memo(0, text)


t1 = "123"

assert decode_ways(t1) == 3