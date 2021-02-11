from collections import defaultdict
# WORD SQUARES
#
# Recursion
#
# Time complexity: O(N * 26^L * L), where N is the number of words and L is the length of the word.
# Space complexity: O(N * L + N * L/2)
#
# How it works:
#
# The main idea of the algorithm is to try one word at a time, and continue placing new rows as long as the constraints are met.
# When a word breaks the requirement, the program backtracks and starts with a new word.
# If the square is completed, the result is added to the answer.

# Trie Node
class TrieNode:
    def __init__(self):
        self.is_word = False 
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    # find all the complete words that are found under the node
    def suffixes(self, suffix='', collected=[]):
        for char, node in self.children.items():
            if node.is_word:
                collected.append(suffix + char)
            if node.children:
                node.suffixes(suffix + char, collected)

        return collected

# Trie Data Structure
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert a word in the Trie
    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)

            current_node = current_node.children[char]

        current_node.is_word = True

    # Find the node where the prefix is located.
    def find(self, prefix):

        current_node = self.root
        
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None

        return current_node

class WordSquares:
    def __init__(self):
        self.trie = Trie()

    # build the Trie
    def initialize(self, words):
        for word in words:
            self.trie.insert(word)

    # find the words that start with a given prefix
    def find(self, prefix):
        #first locate the node
        node = self.trie.find(prefix)
        #if there is such node, return all the suffixes (complete words under it)
        if node:
            return node.suffixes('', [])
        else:
            return []

    # keep filling the next rows as long as constraints are met 
    # (that means if words with certain prefixes are found)
    def backtracking(self, step, word_squares, results):
        # completed the square
        if step == self.length:
            results.append(list(word_squares))
            return

        # get the next prefix
        prefix = "".join([word[step] for word in word_squares])

        # iterate over the possible candidates if any
        for candidate in self.find(prefix):
            word_squares.append(prefix+candidate)
            self.backtracking(step+1, word_squares, results)
            #make sure to pop, so we can try other candidates if last one did not work
            word_squares.pop() 

    # find the word squares for a given word list
    def squares(self, words):
        self.words = words
        self.length = len(words[0])

        results = []
        word_squares = []

        # try one word at a time
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)

        return results

# tests
ws = WordSquares()

word_list = ["ball", "area", "lady", "lead", "wall"]
ws.initialize(word_list)
squares = ws.squares(word_list)

#tests
assert squares == [['ball', 'area', 'lead', 'lady'], ['wall', 'area', 'lead', 'lady']]

print("all tests passed.")