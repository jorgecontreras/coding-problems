# first and last position of element in sorted array

def first_and_last(nums, target):
        start = 0
        end = len(nums)
        result = [-1, -1]
        found_at = None

        while start < end: 
            mid = (end+start) // 2
            
            if nums[mid] == target:
                found_at = mid
                break
            elif nums[mid] > target:
                end = mid 
            else:
                start = mid+1

            

        if found_at is not None:
            left = found_at
            right = found_at

            while left > 0 and nums[left-1] == target:
                left -= 1

            while right < len(nums)-1 and nums[right+1] == target:
                right += 1

            return [left, right]

        return result
    

data = [1,1,2,3,4,5,6,6,6,6,7,7,7,7,8,9,10]
target = 9

result = first_and_last(data, target)

print(result)