def is_palindrome(text):
    p1 = 0
    p2 = len(text) - 1 

    while p1 < p2:
        if not text[p1].isalnum():
            p1 += 1
            continue
        if not text[p2].isalnum():
            p2 -= 1
            continue
        if text[p1].lower() != text[p2].lower():
            return False
        p1 += 1
        p2 -= 1

    return True



t1 = "A man, a plan, a canal: Panama"
t2 = "race a car"
t3 = ""
t4 = "0P"

assert is_palindrome(t1) == True
assert is_palindrome(t2) == False
assert is_palindrome(t3) == True
assert is_palindrome(t4) == False