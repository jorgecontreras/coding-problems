def longest_substring_with_k_distinct(str, k):
  distinct = []
  subs = []
  sub = ""
  longest = 0
  count = 0
  for c in str:
    if c not in distinct:
      distinct.append(c)
    if len(distinct) <= k:
      sub = sub + c
      count += 1
    else:
      subs.append(sub)
      distinct = []
      sub = ""
      if count > longest:
          longest = count
      count = 0
  if longest > 0:
    return longest
  else:
    return -1

print(longest_substring_with_k_distinct('araaci', 1))