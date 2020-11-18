# Dutch national flag problem

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    left_index = 0
    right_index = len(input_list) - 1
    center_index = 0

    while center_index <= right_index:
        # if we find a 0, push it to the left side
        if input_list[center_index] == 0:
            input_list[center_index] = input_list[left_index]
            input_list[left_index] = 0 
            left_index += 1
            center_index += 1
        # if we find a 2, push it to the right side
        elif input_list[center_index] == 2:
            input_list[center_index] = input_list[right_index]
            input_list[right_index] = 2
            right_index -= 1
        # not 0, and not 2? must be a 1, keep going
        else:
            center_index += 1

    return input_list



def test_function(test_case):
    sorted_array = sort_012(test_case)
    
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# test cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test_function([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2])
test_function([])
test_function([2, 1, 0])