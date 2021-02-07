# An imminent hurricane threatens the coastal town of Codeville. 
# If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, 
# determine how many boats will be needed to save everyone.

# For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.

def num_boats(population, k):
    people = sorted(population)

    boats = 0
    weight = 0
    for person in people:
        if person + weight <= k:
            weight += person
        else:
            weight = person
            boats += 1

    if weight > 0:
        boats += 1

    return boats

# test
p = [100, 200, 150, 80]
k = 200

n = num_boats(p, k)

print(n)