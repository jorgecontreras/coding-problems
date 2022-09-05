# SUBSETS
def subsets(items):
    if len(items) == 0:
        return [[]]

    first = items[0]
    exclude = subsets(items[1:])

    include = []
    for exc in exclude:
        subset = [ first ] + exc
        include.append(subset)

    return include + exclude

t1 = [1, 5, 3]

print(subsets(t1))