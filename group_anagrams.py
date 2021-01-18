# group anagrams

# Given an array of strings, group anagrams together.

# For example, given the following array:

# ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
# Return:

# [['eat', 'ate', 'tea'],
# ['apt', 'pat'],
# ['now']]

def group_anagrams(words):
    values = dict()

    for word in words:
        value = 0
        for c in word:
            value += ord(c)
        if value in values:
            values[value] = values[value] + [word]
        else:
            values[value] = [word]

    result = []

    for v, item in values.items():
        result.append(item)

    return result

print(group_anagrams(['eat', 'ate', 'apt', 'pat', 'tea', 'now']))