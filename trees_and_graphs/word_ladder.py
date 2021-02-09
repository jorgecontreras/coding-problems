# Word Ladder
# 
# Breadth First Seach
#
# Time complexity: O(M^2 x N) N number of words. M length of word
# Space complexity: O(M^2 x N) 
#

from collections import deque, defaultdict

class WordLadder:

    # preprocess will get the close words in advance, 
    # to speed up the lookup step
    def preprocess(self):
        
        self.word_list_generic = defaultdict(list)

        for word in self.word_list:
            chars = list(word)
            for i in range(self.wl):
                char = chars[i]
                chars[i] = "*"
                self.word_list_generic["".join(chars)].append(word)
                chars[i] = char

    def find_close_words(self, word):

        close_words = []
        chars = list(word)
        for i in range(self.wl):
            char = chars[i]
            chars[i] = "*"
            generic = "".join(chars)
            chars[i] = char
            if generic in self.word_list_generic:
                close_words += [w for w in self.word_list_generic[generic] if w not in self.visited]
        
        return close_words

    def closest_path_length(self, begin_word, end_word, word_list):

        # word length (all words have same length)
        self.wl = len(word_list[0])

        # keep track of visited words
        self.visited = set()

        # make a set for faster lookup
        self.word_list = set(word_list)

        # if target word is not in word list, stop here
        if end_word not in self.word_list:
            return 0

        # preprocess words
        self.preprocess()
        
        # depth level will help us determine distance
        self.level = 1

        # create a queue and start from begin word
        queue = deque()
        queue.append(begin_word)

        # keep processing elements in the queue
        while queue:
            level_size = len(queue)
            while level_size > 0:
                word = queue.popleft()

                # mark visited
                self.visited.add(word)

                close_words = self.find_close_words(word)

                # if we find the end word we have finished, distance is level + 1
                if end_word in close_words:
                    return self.level + 1
                
                # not found end word, then we add the close words to the queue
                queue += list(close_words)
                level_size -= 1

            # going one level deeper
            self.level += 1

        return 0

wl = WordLadder()

word_list_1 = ["hot","dot","dog","lot","log","cog"]
begin_word_1 = "hit"
end_word_1 = "cog"
output_1 = wl.closest_path_length(begin_word_1, end_word_1, word_list_1)

word_list_2 = ["hot","dot","dog","lot","log"]
begin_word_2 = "hit"
end_word_2 = "cog"
output_2 = wl.closest_path_length(begin_word_2, end_word_2, word_list_2)

assert output_1 == 5
assert output_2 == 0

print("all tests passed.")