from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = defaultdict(list)

        for course, course_preq in prerequisites:
            dependencies[course].append(course_preq)

        visited = set()

        def cycle_present(course):
            if not dependencies[course]:
                return False

            if course in visited:
                return True

            visited.add(course)

            for dependency in dependencies[course]:
                if cycle_present(dependency):
                    return True

            dependencies[course] = []
            return False

        for course in range(numCourses):
            if cycle_present(course):
                return False

        return True