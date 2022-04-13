class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans, in_coming, out_going = [], [0] * numCourses, defaultdict(set)
        queue = deque()        
        
        for course, pre in prerequisites:
            out_going[pre].add(course)
            in_coming[course] += 1
        
        for i in range(numCourses):
            if in_coming[i] == 0:
                queue.append(i)
                
        while queue:
            pre = queue.popleft()
            ans.append(pre)
            
            for course in out_going[pre]:
                in_coming[course] -= 1
                if in_coming[course] == 0:
                    queue.append(course)
                    
        if len(ans) == numCourses:
            return ans
        else:
            return []
            
        