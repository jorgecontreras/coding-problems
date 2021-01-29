# ALIEN DICTIONARY - FIND THE TOPOLOGICAL SORT
#
# time complexity O(V + N)
# V: total number of characters
# N: total number of words
#
# space complexity O(V + N)
# we are storing rules for each character in an adjacency list
# 

"""
Problem Statement #
There is a dictionary containing words from an alien language for which we don’t know the ordering of the alphabets. Write a method to find the correct order of the alphabets in the alien language. It is given that the input is a valid dictionary and there exists an ordering among its alphabets.

Example 1:

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:

1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

From the above two points, we can conclude that the correct character order is: "bac"
Example 2:

Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following ordering among its characters:

1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'

From the above two points, we can conclude that the correct character order is: "cab"
Example 3:

Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
Output: ywxz
Explanation: From the given words we can conclude the following ordering among its characters:

1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'

From the above five points, we can conclude that the correct character order is: "ywxz"
"""

from collections import deque


def find_order(words):
    # initialize
    graph = {}
    in_degrees = {}

    for word in words:
        for c in word:
            graph[c] = []
            in_degrees[c] = 0 

    # build the graph
    for i in range(len(words) - 1):
        # compare with next word
        w1, w2 = words[i], words[i+1] 

        #compare each character until we find a difference
        for j in range(min(len(w1), len(w2))):
            #diff found
            if w1[j] != w2[j]: 
                parent, child = w1[j], w2[j]
                graph[parent].append(child)
                in_degrees[child] += 1
                break

    # find sources
    sources = deque()
    for v in in_degrees:
        if in_degrees[v] == 0:
            sources.append(v)

    # sort
    sorted_order = []
    while sources:
        v = sources.popleft()
        sorted_order.append(v)

        for child in graph[v]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)
    
    # check cycles
    if len(sorted_order) != len(in_degrees):
        return []

    return "".join(sorted_order)

def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()   