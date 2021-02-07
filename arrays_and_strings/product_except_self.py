# product except self

def product_except_self(nums):
    result = [1]

    # first pass: get the product of the left-side elements
    p = 1
    for i in range(1, len(nums)):
        p *= nums[i-1]
        result.append(p)
    
    # second pass: get the product o the right-side elements and update the result array
    p = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= p
        p *= nums[i]

    return result
    
t1 = [1,2,3,4]
t2 = [2,1,0,8]
t3 = [1,2]

assert product_except_self(t1) == [24,12,8,6]
assert product_except_self(t2) == [0,0,16,0]
assert product_except_self(t3) == [2,1]

print("tests passed.")