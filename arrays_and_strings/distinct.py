def longest_substring_with_k_distinct(str, k):
  distinct = set()
  longest = 0
  count = 0
  for c in str:
    if c not in distinct:
      distinct.add(c)
    if len(distinct) <= k:
      count += 1
    else:
      distinct = set()
      longest = max(count, longest)
      count = 0
  if longest > 0:
    return longest
  else:
    return -1

print(longest_substring_with_k_distinct('araaci', 1))
t1 = "araaci"
t2 = "araaci"
t3 = "cbbebi"

assert longest_substring_with_k_distinct(t1, 2) == 4
assert longest_substring_with_k_distinct(t2, 1) == 2
assert longest_substring_with_k_distinct(t3, 3) == 5