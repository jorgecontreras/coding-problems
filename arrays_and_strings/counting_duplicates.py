def duplicate_count(text):
    # Your code goes here
    once = set()
    repeated = set()
    for n in str(text):
        if n.lower() in once:
            repeated.add(n.lower())
        else:
            once.add(n.lower())
    return len(repeated)
