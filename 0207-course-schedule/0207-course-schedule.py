class Solution:
    def canFinish(self,numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(course):
            if visited[course] == -1:  # cycle detected
                return False
            if visited[course] == 1:  # already visited and processed
                return True

            visited[course] = -1  # mark as visited

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visited[course] = 1  # mark as processed
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
