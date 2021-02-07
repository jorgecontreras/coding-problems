# Given an array of sorted numbers and a taget sum, find a pair in the array whose sum is equal to the given target

def pair_target_sum(arr, target_sum):
    start = 0
    end = len(arr)-1 
    while start < end:
        addition = arr[start] + arr[end]
        if addition == target:
            return [start,end]
        elif addition < target:
            start += 1
        else:
            end -= 1
    
    return[-1,-1]

input_data = [1,2,3,4,6]
target = 6
result = pair_target_sum(input_data, target)
print(result)

input_data = [2,5,9,11]
target = 11
result = pair_target_sum(input_data, target)
print(result)