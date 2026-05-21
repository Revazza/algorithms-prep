from typing import List


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        courses = dict()

        for i in range(num_courses):
            courses[i] = []

        for c, p in prerequisites:
            courses[c].append(p)

        # 0:[1,2 3]
        # 1:[2,3]
        # 2:[]
        # 3:[1]

        # 0 -> 1 -> 2 -> v

        visited = set()
        finished = set()
        def can_finish(course) -> bool:
            if course in visited:
                return False
            if course in finished:
                return True

            pres = courses[course]
            if len(pres) == 0:
                return True

            visited.add(course)

            for pre in pres:
                if not can_finish(pre):
                    return False

            visited.remove(course)
            return True

        for c in courses:
            if not can_finish(c):
                return False
            finished.add(c)

        return True
