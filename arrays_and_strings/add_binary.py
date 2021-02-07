# add binary

def add_binary(a, b):
    # find longest number
    n = max(len(a), len(b))

    #fill with 0s to match lengths
    a, b = a.zfill(n), b.zfill(n)

    carry = 0
    answer = []

    # iterate rom right to left
    for i in range(n-1, -1, -1):
        carry = carry + 1 if a[i] == '1' else carry + 0
        carry = carry + 1 if b[i] == '1' else carry + 0

        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')

        carry //= 2

    if carry == 1:
        answer.append('1')
    
    return ''.join(answer[::-1])



a = "111"
b = "111"

print(add_binary(a, b))