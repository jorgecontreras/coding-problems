# twosum

def twosum(nums, k):

    seen = {}

    for i, n in enumerate(nums):
        diff = k-n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i

    return [] 


t1 = [2,5,9,3,6,4,5,1]

print(twosum(t1, 44))
        

    