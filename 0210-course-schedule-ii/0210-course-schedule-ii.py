from collections import defaultdict

class Solution:

    NOT_VISITED = 0
    VISIT_IN_PROGRESS = 1
    VISIT_COMPLETED = 2

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        dependencies = defaultdict(list)

        for current_course, course_preq in prerequisites:
            dependencies[current_course].append(course_preq)

        visit_status = [self.NOT_VISITED] * numCourses

        result = []

        def cycle_present(course) -> bool:

            if visit_status[course] == self.VISIT_IN_PROGRESS:
                return True

            if visit_status[course] == self.VISIT_COMPLETED:
                return False

            visit_status[course] = self.VISIT_IN_PROGRESS

            for dependency in dependencies[course]:
                if cycle_present(dependency):
                    return True

            visit_status[course] = self.VISIT_COMPLETED
            result.append(course)
            return False

        for current_course in range(numCourses):
            if cycle_present(current_course):
                return []

        return result

