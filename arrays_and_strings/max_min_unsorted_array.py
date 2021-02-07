# Max and Min in a Unsorted Array

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    smallest = None
    largest = None
    for i, n in enumerate(ints):
        # when it's the first pass, both variables are initialized with the number
        if i == 0:
            smallest = n
            largest = n
        # the rest of the numbers are compared to the current value of smallest and largest
        else:
            if n > largest:
                largest = n
            if n < smallest:
                smallest = n
    return smallest, largest


## Test cases
import random

#empty list
l = [i for i in range(0, 0)]  
random.shuffle(l)
print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")

# 0 - 9
l = [i for i in range(0, 10)]  
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# only one value in the list
l = [i for i in range(2, 3)]  
random.shuffle(l)
print ("Pass" if ((2, 2) == get_min_max(l)) else "Fail")

#negative numbers
l = [i for i in range(-100, 0)]  
random.shuffle(l)
print ("Pass" if ((-100, -1) == get_min_max(l)) else "Fail")

#large range
l = [i for i in range(-10000, 10000)]  
random.shuffle(l)
print ("Pass" if ((-10000, 9999) == get_min_max(l)) else "Fail")