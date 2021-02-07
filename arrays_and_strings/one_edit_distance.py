# one edit distance

def one_edit_distance(s, t):
    ns, nt = len(s), len(t)

    # make s be the shorter var
    if ns > nt:
        return one_edit_distance(t, s)

    # if length difference is more than 1, dont bother
    if nt - ns > 1:
        return False

    # check chars one by one
    for i in range(ns):
        # here we've found a difference
        if s[i] != t[i]:
            if ns == nt: #both strigs are same size, so remaining characters must match
                return s[i+1:] == t[i+1:]
            else: # strings are different size, remaining chars from t+1 must match
                return s[i:] == t[i+1:]

    # no differences so far, last check is make sure both strings are not same size
    return ns != nt


a1 = "abxcdf"
b1 = "abxcff"

a2 = "abcde"
b2 = "acb"

a3 = "ac"
b3 = "acx"

one_edit_distance(a1, b1)

assert one_edit_distance(a1, b1) == True
assert one_edit_distance(a2, b2) == False
assert one_edit_distance(a3, b3) == True