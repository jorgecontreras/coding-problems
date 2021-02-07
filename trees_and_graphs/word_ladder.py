# Word Ladder

from collections import deque

class WordLadder:

    def is_close(self, w1, w2):
        for i in range(self.wl):
            #if a char is different
            if w1[i] != w2[i]:
                # check the rest of the string, should be equal
                return w1[i+1:] == w2[i+1:]

    def find_close_words(self, word):

        close_words = set()
        
        for w in self.word_list:
            if self.is_close(w, word):
                if w not in self.visited:
                    close_words.add(w)
        
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