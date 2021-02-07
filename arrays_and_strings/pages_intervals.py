# not working

def solution(args):
    items = []
    span = 0
    for i in range(1, len(args)):
        if abs(args[i] - args[i-1]) >= 2:
            if span == 1:
                items.append(start)
                items.append(end)
            elif span > 1:
                items.append(start + "-" + end)
            else:
                items.append(str(args[i-1]))
            
            span = 0
        else:
            if span == 0:
                start = str(args[i-1])
                end = str(args[i])
            
            span += 1
            if span >= 2:
                end = str(args[i])
        
    if span == 1:
        items.append(start + "," + end)  
    elif span >= 2: 
        items.append(start + "-" + end) 
    return ",".join(items)

t1 = [-74,-71,-68--63,-60,-58,-57,-54,-52,-51]
print(solution(t1))