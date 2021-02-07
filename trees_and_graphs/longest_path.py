# longest path

def longest_path(text):
    res = 0
    d = {}
    for file in text.splitlines():
        depth = file.count("\t")
        if "." not in file:
            d[depth] = len(file) - depth
        else:
            curr = len(file) + sum([d[v] for v in range(depth)])
            res= max(res,curr)
    return res



t1 = "user\f\tpictures\f\tdocuments\f\t\tnotes.txt"
print(longest_path(t1))