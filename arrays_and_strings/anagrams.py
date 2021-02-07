def anagrams(word, words):
    #your code here
    anagrams = []
    
    target = 0
    for l in word:
        target += ord(l)
        
    for item in words:
        value = 0
        for l in item:
            value += ord(l)
        if value == target:
            anagrams.append(item)
    return anagrams
