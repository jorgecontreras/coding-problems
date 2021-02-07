# look and say

def look_and_say():

    text = "1"
    times = 5

    while times > 0:
        start = 0
        count = 1
        res = ""

        if len(text) == 1:
            res = "11"

        for i in range(1, len(text)):
            if text[i] == text[i-1]:
                count += 1
            else:
                res += str(count) + str(text[i-1]) 
                count = 1

        res += str(count) + str(text[i-1])
        
        print(res)
        text = res
        times -= 1

look_and_say()
        

        

