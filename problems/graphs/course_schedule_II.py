from typing import List


class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = dict()
        for i in range(num_courses):
            courses[i] = []

        for c, p in prerequisites:
            courses[c].append(p)

        visited = set()
        finished = []

        def fill_finished(course) -> bool:
            if course in visited:
                return False
            if course in finished:
                return True

            visited.add(course)
            prs = courses[course]

            for pr in prs:
                if not fill_finished(pr):
                    return False

            finished.append(course)
            visited.remove(course)
            return True

        for c in range(num_courses):
            if not fill_finished(c):
                return []

        return finished
