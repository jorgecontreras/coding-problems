# Square root of an integer

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #handle edge cases
    if number == 0 or number == 1:
        return number

    if number < 0:
        return None

    # use binary search!
    # idea: the answer can be somewhere between 0 and the number
    # make try and error to find the most accurate sqrt
    possible = [i for i in range(number)]

    while len(possible) > 1:
        mid = len(possible) // 2
        answer = possible[mid]
        if answer * answer == number:
            return answer
        elif answer * answer > number:
            possible = possible[:mid]
        else:
            possible = possible[mid:]

    return possible[0]
        

# test cases
print ("Pass" if  (None == sqrt(-9)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (1 == sqrt(2)) else "Fail")
print ("Pass" if  (10 == sqrt(100)) else "Fail")
print ("Pass" if  (100 == sqrt(10000)) else "Fail")
print ("Pass" if  (12 == sqrt(145)) else "Fail")