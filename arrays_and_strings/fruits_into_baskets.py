# fruits into baskets

# longest subarray with at most two distinct elements

# open the window
# keep moving forward until dict length goes over 2
    # start closing the window until dict is again 2 or less
    # dont forget to store the size we reached at that point
# continue with remaining elements


def solve(fruits):

    largest = 0
    distinct = {}
    start = 0 

    for i in range(len(fruits)):
        f = fruits[i]
        distinct[f] = distinct.get(f, 0) + 1

        while len(distinct) > 2:
            #largest = max(largest, i-start)
            remove = fruits[start]
            distinct[remove] -= 1
            if distinct[remove] == 0:
                del distinct[remove]
            start += 1
        
        largest = max(largest, i-start+1)

    return largest 

t1 = ['A', 'B', 'C', 'A', 'C']
o1 = 3

t2 = ['B', 'C', 'B', 'B', 'C', 'A']
o2 = 5

print(solve(t1))
print(solve(t2))