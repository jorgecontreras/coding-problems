# Compare version
# Time complexity: O(M + N), where M and N are the length of input strings
# Space complexity: O(M + N)

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parts1 = version1.split(".")
        parts2 = version2.split(".")
        length = max(len(parts1), len(parts2))
        
        for i in range(length):
            p1 = int(parts1[i]) if i < len(parts1) else 0
            p2 = int(parts2[i]) if i < len(parts2) else 0
            
            if p1 < p2:
                return -1
            elif p1 > p2:
                return 1
            
        return 0

s = Solution()

assert s.compareVersion("1.01", "1.001" ) == 0
assert s.compareVersion("1.0", "1.0.0" ) == 0
assert s.compareVersion("0.1", "1.1" ) == -1
assert s.compareVersion("1.0.1", "1" ) == 1
assert s.compareVersion("7.5.2.4", "7.5.3" ) == -1

print("all tests passed.")
