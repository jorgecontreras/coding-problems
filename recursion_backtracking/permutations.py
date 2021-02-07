# permutations

class Solution:

    def recurse(self, available, fixed=[], result=[]):
        
        if len(available) == 0:
            result.append(fixed)

        for i in range(len(available)):
            self.recurse(available[:i] + available[i+1:], fixed + [available[i]], result)
        
        return result

    def permutations(self, arr):
        return self.recurse(arr)





t1 = [1,3,5]
s = Solution()

print(s.permutations(t1))