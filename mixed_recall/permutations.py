# PERMUTATIONS

# [1, 3, 6] => [[1,3,6], [3,1,6], [3,6,1], [6,3,1], [6,1,3], [1,6,3]]
# Time: O(n!)
# Space: O(n!)

def permutations(nums):
    # base case
    if len(nums) == 0:
        return [[]]

    first = nums[0]
    output = []
    
    for permutation in permutations(nums[1:]):
        for i in range(len(permutation) + 1):
            new = permutation[:i] + [first] + permutation[i:]
            output.append(new)

    return output
    
t1 = permutations([1,3,6])

print(t1)
