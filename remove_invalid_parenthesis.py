# remove invalid parenthesis

"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

class Solution:

    def remove_invalid(self, s):

        # s: original string
        # i: index
        # left_count: number of opening parenthesis added to the expression we are building
        # right_count: number of closing parenthesis added to the expression we are building
        # left_rem: left parenthesis to be removed
        # right_rem: right parenthesis to be removed
        # exp: the expression that we are building, would result in something valid
        
        def recurse(s, i, left_count, right_count, left_rem, right_rem, exp):
            # reached end of string. 
            if i == len(s):
                # if no more parenthesis to be removed, then it's a valid expression
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(exp)
                    result[ans] = 1
            else:
                # the discard case
                if (s[i] == "(" and left_rem > 0) or (s[i] == ")" and right_rem > 0):
                    recurse(s, i + 1,
                            left_count, 
                            right_count,
                            left_rem - (s[i] == "("),
                            right_rem - (s[i] == ")"), exp)
            
                exp.append(s[i])

                if s[i] != "(" and s[i] != ")":
                    recurse(s, i+1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, exp)

                elif s[i] == "(":
                    recurse(s, i + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, exp)
                    
                elif s[i] == ")" and left_count > right_count:
                        recurse(s, i + 1,
                                left_count,
                                right_count + 1,
                                left_rem,
                                right_rem, exp)
                
                # pop for backtracking
                exp.pop()

        left = 0
        right = 0
        # find count of misplaced left/right parenthesis
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                right = right + 1 if left == 0 else right

                left = left - 1 if left > 0 else left 

        result = {}

        recurse(s, 0, 0, 0, left, right, [])

        return list(result.keys())
    
s = Solution()

t1 = "()())()"
ans = s.remove_invalid(t1)

t2 = "(a)())()"
ans2 = s.remove_invalid(t2)

print(ans)
print(ans2)