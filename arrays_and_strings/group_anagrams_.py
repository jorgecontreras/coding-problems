# group anagrams
from collections import defaultdict

def group_anagrams(words):
    
    groups = defaultdict(list)

    for word in words:
        groups[tuple(sorted(word))].append(word)

    return groups.values()


print(group_anagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc", "hud", "dhu", "nit"]))