# PARENTHETICAL POSSIBILITIES
"""
Write a function, parenthetical_possibilities, that takes in a string as an argument. 
The function should return an array containing all of the strings that could be generated 
by expanding all parentheses of the string into its possibilities.

For example, the possibilities for 'x(mn)yz' are 'xmyz', 'xnyz'.
"""
# m = largest group
# n = number of groups
# Time O(m^n)
# Space O(m^n)
def parenthetical_possibilities(s):
    # base case
    # if the string is empty, return the only possibility
    if len(s) == 0:
        return ['']

    choices, suffix = options(s)
    output = []
    for choice in choices:
        possibilities = parenthetical_possibilities(suffix)
        output += [choice + p for p in possibilities]

    return output


def options(s):
    """
    helper function that returns all the possibilities of a string, 
    and the suffix which is whatever string found after the closing parenthesis
    """
    if s[0] == "(":
        end = s.index(")")
        options = s[1:end]
        suffix = s[end+1:]
        return (options, suffix)

    return (s[0], s[1:])

t1 = parenthetical_possibilities("(qr)ab(stu)c")
t2 = parenthetical_possibilities("(etc)(blvd)(cat)")

assert t1 == [ 'qabsc', 'qabtc', 'qabuc', 'rabsc', 'rabtc', 'rabuc' ]
assert t2 == [
  'ebc', 'eba', 'ebt', 'elc', 'ela',
  'elt', 'evc', 'eva', 'evt', 'edc',
  'eda', 'edt', 'tbc', 'tba', 'tbt',
  'tlc', 'tla', 'tlt', 'tvc', 'tva',
  'tvt', 'tdc', 'tda', 'tdt', 'cbc',
  'cba', 'cbt', 'clc', 'cla', 'clt',
  'cvc', 'cva', 'cvt', 'cdc', 'cda',
  'cdt'
 ]

t3 = parenthetical_possibilities("")
assert t3 == ['']

print("All tests passed!")