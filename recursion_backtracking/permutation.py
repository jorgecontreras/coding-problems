# PERMUTATIONS
def permutations(items):
    if len(items) == 0:
        return [[]]

    first = items[0]
    output = []
    for permutation in permutations(items[1:]):
        for i in range(len(permutation) + 1):
            element = permutation[:i] + [first] + permutation[i:]
            output.append(element)

    return output

print(permutations([1,2,3]))