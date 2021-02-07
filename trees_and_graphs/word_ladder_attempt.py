"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 words.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no possible transformation.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.
"""
from typing import List
from unittest import TestCase
import unittest

class WordLadder:

    def __init__(self):
        self.ans = []
        self.visited = set()

    def is_close(self, w1, w2):
        for i,c in enumerate(w1):
            if w1[i] != w2[i]:
                return w1[i+1:] == w2[i+1:]
        return False

    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        
        #convert word_list to set, for faster lookups
        dictionary = set(word_list)

        current_word = begin_word
        self.visited.add(begin_word)

        #search close word (max 1 char different)
        
        for word in dictionary:
            if word not in self.visited and self.is_close(current_word, word):
                # current word is candidate, we could find more, 
                # so we will need 0/1 knapsack-backtracking to try all possible paths
                # and calculate min cost
                self.ans.append(word)
                if word == end_word:
                    return len(self.ans)
                self.ladder_length(word, end_word, word_list)

        return 0
        

class TestWordLadder(TestCase):
    def setUp(self) -> None:
        self.s = WordLadder()
        
    def test_ladder_length(self) -> None:
        self.assertEqual(5, self.s.ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]), "Should be 5")
        self.assertEqual(0, self.s.ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]), "Should be 0")

if __name__ == '__main__':
    unittest.main()