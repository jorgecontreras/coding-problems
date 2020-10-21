# Hash Map Courses

map = {
    "C112": [],
    "C110": [],
    "C340": [],
    "C102": ["C340"],
    "C103": ["C102", "C340", "C340"],
    "C104": ["C103", "C102", "C340"],
    "C105": ["C110"],
    "C106": ["C112"],
    "C107": ["C104", "C103", "C102", "C340", "C105", "C106"]

}

# C100, C200, C300
# we should order by count asc
# iterate each asc and add them to a list as we go through
# make sure on each pass that the required course is already in the list, otherwise no path will be available

def CoursePath(map):
    ordered = []
    sortz = {k: len(v) for k, v in sorted(map.items(), key=lambda item: len(item[1]))}

    for course, reqs in sortz.items():
        if reqs == 0:
            ordered.append(course)
        else:
            for req in map[course]:
                if req not in ordered:
                    return None
                if course not in ordered:
                    ordered.append(course)
    return ordered

print(CoursePath(map))
