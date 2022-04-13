class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_coming = [0 for i in range(numCourses)] 
        neighbours = defaultdict(set)
        cnt = 0
        queue = deque()
        
        for course, pre in prerequisites:
            neighbours[pre].add(course)
            in_coming[course] += 1
            
        for i in range(numCourses):
            if in_coming[i] == 0:
                queue.append(i)
            
        while queue:
            course = queue.popleft()
            cnt += 1
            
            for neigh in neighbours[course]:
                in_coming[neigh] -= 1
                if in_coming[neigh] == 0:
                    queue.append(neigh)
                    
        return cnt == numCourses
                
                
            
        
        