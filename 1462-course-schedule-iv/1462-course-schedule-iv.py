class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        @cache
        def dfs(course, target):
            nonlocal adjacencyList
            if (course, target) in memo:
                return (course, target)
            
            if course == target:
                return True
            
            for cor in adjacencyList[course]:
                if dfs(cor, target):
                    memo[(course, target)] =  True
                    return True
            memo[(course, target)] = False
            return False
        
        memo = {}
        adjacencyList = defaultdict(list)
        for pre, course in prerequisites:
            adjacencyList[pre].append(course)
        
        return [dfs(i, j) for i, j in queries]
        