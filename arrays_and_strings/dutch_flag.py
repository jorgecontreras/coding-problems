# dutch flag problem

class Solution:
    def sort_012(self, nums):
        left, center, right = 0,0, len(nums) - 1

        while center <= right:
            # a zero is found
            if nums[center] == 0:
                nums[center], nums[left] = nums[left], nums[center]
                left += 1
                center += 1

            # a two is found
            elif nums[center] == 2:
                nums[center], nums[right] = nums[right], nums[center]
                right -= 1

            # else, we have a 1
            else:
                center += 1

        return nums



    def test_function(self,test_case):
        sorted_array = self.sort_012(test_case)
        
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail")


# test cases
s = Solution()
s.test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
s.test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
s.test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
s.test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
s.test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
s.test_function([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
s.test_function([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])
s.test_function([])
s.test_function([2, 1, 0])