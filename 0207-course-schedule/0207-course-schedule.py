from collections import defaultdict

class Solution:

    NOT_VISITED = 0
    VISIT_IN_PROGRESS = 1
    VISIT_COMPLETED = 2

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = defaultdict(list)

        for course, course_preq in prerequisites:
            dependencies[course].append(course_preq)

        visit_status = [self.NOT_VISITED] * numCourses

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
            return False

        for current_course in range(numCourses):
            if cycle_present(current_course):
                return False

        return True