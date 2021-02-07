def isCryptSolution(crypt, solution):
    
    solution_d = {}
    numbers = []
    
    for s in solution:
        solution_d[s[0]] = s[1]
        
    for word in crypt:
        n = ""
        for l in word:
            n += solution_d[l]
        if n[0] == '0' and len(word) > 1:
            return False
        numbers.append(n)
        
    return int(numbers[0]) + int(numbers[1]) == int(numbers[2])
