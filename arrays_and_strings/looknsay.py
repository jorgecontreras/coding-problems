# look and say

def look_and_say(look):

    repeat = look[0]
    look = look[1:] + " "
    count = 1
    say = ""

    for n in look:
        if n != repeat:
            say += str(count) + str(repeat)
            count = 1
            repeat = n
        else:
            count += 1

    return say 

say = "1"

for i in range(10):
    print(say)
    say = look_and_say(say)