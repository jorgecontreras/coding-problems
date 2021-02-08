# Autocomplete with tries

### Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

### Finding Suffixes
Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

![autocomplete](https://github.com/jorgecontreras/coding-problems/blob/master/media/tries.jpg)

### Time complexity

The insert method has a time complexity of **O(M)** where M is the length of the word

The find method has a time complexity of **O(M)**, where M is the number of letters in the prefix

The suffixes method has a time complexity of **O(N*K)** where N is the number of letters in each word below and K is the number of words that match that prefix (number of children and grandchildren from given node)

### Space complexity

insert method uses space **O(M)**, where M is the number of letters in the word

find method uses space **O(1)**, no additional storage required to arrive at prefix node

suffixes method uses space **O(K)**, where K is the number of words found beneath the prefix node.
