# All Tasks Scheduling Orders
#
# Topological sort with backtracking
#
# Time complexity: O(V! + E) 
# Space complexity: O(V! + E)

from collections import deque

class Tasks:

    def topsort(self, tasks, prerequisites):
        # initialize
        in_degrees = {i: 0 for i in range(tasks)}
        graph = {i: [] for i in range(tasks)}
        self.sorted_orders = []
        sorted_order = [] 

        # build graph
        for p in prerequisites:
            parent, child = p[0], p[1]
            graph[parent].append(child)
            in_degrees[child] += 1

        # find sources
        sources = deque([v for v in in_degrees if in_degrees[v] == 0])

        # recurse
        self.recurse(graph, in_degrees, sources, sorted_order)

        return self.sorted_orders

    def recurse(self, graph, in_degrees, sources, sorted_order):
        if sources:
            for vertex in sources:
                
                # append
                sorted_order.append(vertex)

                # copy sources, removing current 
                sources_next = deque(sources)
                sources_next.remove(vertex)

                # decrement children in-degrees
                for child in graph[vertex]:
                    in_degrees[child] -= 1
                    if in_degrees[child] == 0:
                        sources_next.append(child)

                # recurse
                self.recurse(graph, in_degrees, sources_next, sorted_order)

                # backtrack
                sorted_order.remove(vertex)
                for child in graph[vertex]:
                    in_degrees[child] += 1

        # if order is valid, append to result
        if len(sorted_order) == len(in_degrees):
            self.sorted_orders.append(list(sorted_order))

# tests
t = Tasks()

def main():
  print("Task Orders: ")
  print(t.topsort(3, [[0, 1], [1, 2]]))

  print("Task Orders: ")
  print(t.topsort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))

  print("Task Orders: ")
  print(t.topsort(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))


main()