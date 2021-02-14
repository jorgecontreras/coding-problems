# WORD SQUARES
#
# Hashmap
#
# Time complexity: O(N * 26^L), where N is the number of words and L is the length of the word
# Space complexity: O(N * L)

from collections import defaultdict

class Solution:
    def squares(self, words):
        hashmap = defaultdict(list)
        length = len(words[0])
        results = []
        
        def buildHashmap():
            for word in words:
                for i in range(1, length):
                    hashmap[word[:i]].append(word)
                    
        def backtrack(i, square):
            if i == length:
                results.append(list(square))
                return
            prefix = "".join(w[i] for w in square)
            for candidate in hashmap[prefix]:
                square.append(candidate)
                backtrack(i + 1, square)
                square.pop()
        
        buildHashmap()
    
        for word in words:
            backtrack(1, [word])
            
        return results

s = Solution()

word_list_1 = ["ball", "area", "lady", "lead", "wall"]
squares = s.squares(word_list_1)

print(squares)