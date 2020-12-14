def solution(s):
    i = 0
    r = []
    while s[i:i+2]:
        if len(s[i:i+2]) == 1:
            r.append(s[i:i+2] + "_")
            break
        r.append(s[i:i+2])
        i += 2
        
    return r
