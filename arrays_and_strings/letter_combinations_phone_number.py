from collections import deque

# letter combinations of phone number

keyboard = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],

}

def phone_combinations(numbers):
    combinations = deque()
    for n in numbers:
        if len(combinations) == 0:
            for c in keyboard[n]:
                combinations.append(c)
        else:
            post = []
            while combinations:
                pre = combinations.popleft()
                for c in keyboard[n]:
                    post.append(pre + str(c))
            combinations += post

    return list(combinations)

t1 = "23"

print(phone_combinations(t1))
assert phone_combinations(t1) == ["ad","ae","af","bd","be","bf","cd","ce","cf"]