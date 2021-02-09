

def compress(text):
    text += " "
    repeat = text[0]
    count = 0
    output = ""
    i = 0

    while i < len(text):
        if text[i] != repeat:
            if count == 1:
                output += str(repeat)
            else:
                output += str(count) + str(repeat)
            
            repeat = text[i]
            count = 0
        else:
            count += 1
            i += 1

    return output

text = "aaaabbbbbaaaadcfbbbbaassssssrrrrrtttvtvt"
print(compress(text))