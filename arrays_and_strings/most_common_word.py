# MOST COMMON WORD
#
# Time complexity: O(N+M) N: paragraph length, M: banned length
# Space complexity: O(N+M)

def most_common_word(paragraph, banned):
    banned = set(banned)
    freq = {}
    max_f = 0
    max_w = None

    # cleanup
    paragraph = paragraph.replace(",", " ")

    for word in paragraph.split(" "):
        lw = "".join(filter(str.isalpha, word.lower()))

        # still need to remove punctuation
        if lw not in banned and lw != "":
            freq[lw] = freq.get(lw, 0) + 1
            if freq[lw] > max_f:
                max_f = freq[lw]
                max_w = lw
     
    return max_w


p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]

assert most_common_word(p, b) == "ball"

p = "a, a, a, a, b,b,b,c, c"
b = ["a"]

assert most_common_word(p, b) == "b"

p = "Bob. hIt, baLl"
b = ["bob", "hit"]

assert most_common_word(p, b) == "ball"

print("all tests passed.")