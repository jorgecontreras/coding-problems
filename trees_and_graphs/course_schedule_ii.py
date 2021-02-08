# COURSE SCHEDULE II

from collections import deque, defaultdict

class Courses:

    def find_order(self, numCourses, prerequisites):
        
        # initialize
        sorted_courses = []
        in_degrees = {c:0 for c in range(numCourses)}
        graph = defaultdict(list)

        # build graph
        for p in prerequisites:
            parent, child = p[1], p[0]
            graph[parent].append(child)
            in_degrees[child] += 1

        # find sources
        sources = deque()
        for c in in_degrees:
            if in_degrees[c] == 0:
                sources.append(c)

        # sort
        while sources:
            course = sources.popleft()
            sorted_courses.append(course)

            for child in graph[course]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        # check for cycles
        if len(sorted_courses) != len(in_degrees):
            return []

        else:
            return sorted_courses


# tests
c = Courses()

numCourses_1 = 2
prerequisites_1 = [[1,0]]
output_1 = [0,1]

numCourses_2 = 4
prerequisites_2 = [[1,0],[2,0],[3,1],[3,2]]
output_2 = [0,2,1,3]
output_2b = [0,1,2,3]

numCourses_3 = 1
prerequisites_3 = []
output_3 = [0]

numCourses_4 = 2
prerequisites_4 = []
output_4 = [0,1]

assert c.find_order(numCourses_1, prerequisites_1) == output_1
assert c.find_order(numCourses_2, prerequisites_2) == output_2 or c.find_order(numCourses_2, prerequisites_2) == output_2b
assert c.find_order(numCourses_3, prerequisites_3) == output_3
assert c.find_order(numCourses_4, prerequisites_4) == output_4

print("all tests passed.")