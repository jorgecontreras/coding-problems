
# Stack class
class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pull(self):
        if len(self.items) > 0:
            self.items.pop()

# simplifyPath function
def simplifyPath(path):
    parts = path.split('/')
    stack = Stack()
    
    for part in parts:
        if part == '.' or part == '':
            continue    
        elif part == '..':
            stack.pull()    
        else:
            stack.push(part)
    
    return "/" + "/".join(stack.items)
