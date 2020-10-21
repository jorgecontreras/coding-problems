# search in a rotated sorted array

def rotated_array_search(input_list, number, p=0):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # cut in half. it's very similar to binary search.
    mid = len(input_list) // 2

    # --- BASE CASES --- 
    # bingo! the number was found at position mid 
    # (plus the value of p, which was tracking the position in the original input_list)
    if number == input_list[mid]: 
        return p + mid

    # :( the list has only one element left, and it's not what we are looking for, return -1
    if len(input_list) == 1 and input_list[0] != number:
        return -1

    # --- KEEP SEARCHING ---
    # the approach is like binary search, but with a bit more conditions (because of the rotation)
    # the key to this problem is to know if we should keep searching to the left or right.
    # we need to check not only the mid value, but also the edges.
    
    # GO RIGHT: get rid of left half, but keep track of where the mid was (we'll call it p)
    if input_list[mid] > input_list[0] > number:
        input_list = input_list[mid:]
        p += mid 

    elif number > input_list[mid] > input_list[0]:
        input_list = input_list[mid:]
        p += mid 

    # GO LEFT: get rid of right half
    elif  input_list[0] >= number < input_list[mid]:
        input_list = input_list[:mid]

    elif number >= input_list[0] > input_list[mid]:
        input_list = input_list[:mid]

    # call itself recursively, with a reduced input
    return rotated_array_search(input_list, number, p) 

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])