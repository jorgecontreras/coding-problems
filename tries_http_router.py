# HTTPRouter using a Trie

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.not_found_handler = not_found_handler
        self.insert(['/'], root_handler) #this node is required to handle requests to '/' path
        
    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for part in path:
            if part not in current_node.children:
                current_node.insert(part, self.not_found_handler) #initialize the node with not found handler
            current_node = current_node.children[part] # go one level deeper
        current_node.handler = handler # we arrived to leaf node, assign the handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if path == ['']: # splitting the path by '/' will leave empty string for the root
            path = ['/'] # we change it to point to node '/' to ensure the root handler is called

        current_node = self.root

        for part in path:
            if part not in current_node.children:
                return self.not_found_handler
            current_node = current_node.children[part]
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, part, handler):
        # Insert the node as before
        self.children[part] = RouteTrieNode()
        self.handler = handler
                

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, uri, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        parts = self.split_path(uri)
        self.routes.insert(parts, handler)

        
    def lookup(self, uri):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # remove trailing slash to make it work with or without it
        uri = uri.rstrip("/")

        parts = self.split_path(uri)
        
        return self.routes.find(parts)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        parts = path.split('/')
        return parts

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("")) # should print 'root handler'
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
