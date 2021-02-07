# permutation with changing case

def find_letter_case_string_permutations(st):
    result = [st]

    for i in range(len(st)):
        if not st[i].isalpha(): # skip numbers
            continue

        # change case of ith character of each existing permutation
        for p in range(len(result)):
            chars = list(result[p])
            chars[i] = chars[i].swapcase()
            result.append(''.join(chars))

    return result


t1 = "ab7c"
t2 = "7h4A"

print(find_letter_case_string_permutations(t1))
print(find_letter_case_string_permutations(t2))
