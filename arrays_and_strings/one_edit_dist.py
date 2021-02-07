# one edit distance

def one_edit_dist(str1, str2):

    # force str1 to be shorter
    if len(str1) > len(str2):
        return one_edit_dist(str2, str1)

    # check if difference is more than two
    if len(str2) - len(str1) > 1:
        return False

    # check chars one by one
    for i in range(len(str1)):
        # if difference found, verify remaining chars are equal
        if str1[i] != str2[i]: #diff found
            if len(str1) == len(str2):
                return str1[i+1:] == str2[i+1:]
            else:
                return str1[i:] == str2[i+1:]

    return str1 != str2




t1 = "bcd"
t2 = "bxcd"

print(one_edit_dist(t1, t2))

