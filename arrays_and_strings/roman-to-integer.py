# roman to integer

def roman_to_integer(s):
    conversion = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0

    for i in range(len(s)):
        value = conversion[s[i]]

        if i+1 < len(s):
            if s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                value = -value
            if s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                value = -value
            if s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                value = -value

        num += value
        
    return num


assert roman_to_integer("III") == 3
assert roman_to_integer("IV") == 4
assert roman_to_integer("IX") == 9
assert roman_to_integer("LVIII") == 58
assert roman_to_integer("MCMXCIV") == 1994
