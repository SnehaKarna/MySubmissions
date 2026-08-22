class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:

        graph = {i: [] for i in range(numCourses)}

        # Build directed graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = set()
        path = set()

        def dfs(course):

            # Course already in current path → cycle
            if course in path:
                return False

            # Already checked this course
            if course in visited:
                return True

            path.add(course)
            visited.add(course)

            # Check all courses depending on this course
            for nextCourse in graph[course]:

                if not dfs(nextCourse):
                    return False

            # Done exploring this path
            path.remove(course)

            return True

        # Check every course
        for course in range(numCourses):

            if not dfs(course):
                return False

        return True