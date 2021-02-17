# INTEGER TO ROMAN

def integer_to_roman(num):
    output = ""

    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # split the number in different parts
    th = num // 1000
    h = num % 1000 // 100
    t = num % 100 // 10
    u = num % 10

    return thousands[th] + hundreds[h] + tens[t] + units[u]

assert integer_to_roman(8) == "VIII"
assert integer_to_roman(10) == "X"
assert integer_to_roman(1994) == "MCMXCIV"
assert integer_to_roman(58) == "LVIII"

print("all tests passed.")