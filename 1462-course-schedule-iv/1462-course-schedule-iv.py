class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        @cache
        def dfs(course, target):
            nonlocal adjacencyList
            if course == target:
                return True
            
            for cor in adjacencyList[course]:
                if dfs(cor, target):
                    return True
            return False
            
        adjacencyList = defaultdict(list)
        for pre, course in prerequisites:
            adjacencyList[pre].append(course)
        
        return [dfs(i, j) for i, j in queries]
        