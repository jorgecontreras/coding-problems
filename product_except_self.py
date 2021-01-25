# product except self

def product_except_self(nums):
    p1 = p2 = 1
    result = [1]

    for i in range(1, len(nums)):
        p1 *= nums[i-1]
        result.append(p1)

    for i in range(len(nums) - 1, -1, -1):
        result[i] *= p2
        p2 *= nums[i]

    return result 
    
t1 = [1,2,3,4]

assert product_except_self(t1) == [24,12,8,6]