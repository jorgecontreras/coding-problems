# permutations dfs

def permutations(nums):
    return dfs(nums, [], [])

def dfs(available, fixed, result):
    if len(available) == 0:
        result.append(fixed)

    for i in range(len(available)):
        dfs(available[:i] + available[i+1:], fixed + [available[i]], result)

    return result

print(permutations([1,2,3]))