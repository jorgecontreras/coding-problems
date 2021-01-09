def areFollowingPatterns(strings, patterns):
    d = {}
    for i,word in enumerate(strings):
        if word in d and d[word] != patterns[i]:
            return False
        d[word] = patterns[i]
    return len(d) == len(set(d.values()))
