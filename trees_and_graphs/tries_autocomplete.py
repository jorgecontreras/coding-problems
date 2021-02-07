# Autocomplete with tries

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix='', collected=[]):
        ## recursive function that collects the suffix for 
        ## all complete words below this point
        
        for c, child in self.children.items():
            if child.is_word:
                collected.append(suffix + c)
            if len(child.children) > 0:
                child.suffixes(suffix + c, collected)
        
        return collected

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.insert(c)
            
            current_node = current_node.children[c]

        current_node.is_word = True


    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for c in prefix:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                return None
        return current_node

# test cases
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory",
    "car", "carrier", "carpet", "cabernet", "ceiling", "coworker", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes('', [])))
        else:
            print(prefix + " not found")
    else:
        print('')

# uncomment these two lines to test in CLI
#user_input = input("Search: ")
#f(user_input)


test_cases = ["tri", "sand", "ant", "car", "", "fun"]

for test_case in test_cases:
    print("----------")
    print(test_case + ": ")
    print("----------")
    f(test_case)
    print("\n")
