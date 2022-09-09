# SUBSETS
# time: O(2^n)
# space = O(2^n)

# base case
# index
# recursive
# first
def subsets(items):
    # base case
    if len(items) == 0:
        return [[]]

    first = items[0]
    
    exclude = subsets(items[1:])
    include = []
    for exc in exclude:
        include.append([first] + exc)

    return include + exclude


items = [3,5,1]

# [
#   [],
#   [3],
#   [5],
#   [1],
#   [3,5],
#   [3,1],
#   [5,1]
#   [3,5,1] 
# ]

ans = subsets(items)

print(ans)