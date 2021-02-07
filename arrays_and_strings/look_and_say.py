# look and say

"""
Question 2: Look and Say
Implement a function that outputs the Look and Say sequence:
1 
11 
21 
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
"""

# start counter at 1
# while digit is same, increase counter by 1
# when digit is different, reset counter to 1
# concatenate counter + digit
# recurse

def look_and_say(start, n):
    #base case
    if n == 0:
        return start

    # decrease loop counter
    n -= 1

    counter = 1
    result = ""
    # count number of repeated characters
    for i in range(len(start) - 1):
        if start[i] == start[i+1]:
            counter += 1
        else:
            result += str(counter) + str(start[i])
            counter = 1
            
    result += str(counter) + start[-1]
    print(result)
    return look_and_say(result, n)
    

def solution(n):
    return look_and_say("1", n)

print(solution(10))