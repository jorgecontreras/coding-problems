def spin_words(sentence):
    # Your code goes here
    words = sentence.split()
    output = []
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
        output.append(word)
        
    return " ".join(output)
