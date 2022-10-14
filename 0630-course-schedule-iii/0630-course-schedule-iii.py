class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        key = lambda a: a[1]
        courses.sort(key = key)
        ans, curTime = 0, 0
        heap = []
        
        for duration, lastDay in courses:
            curTime += duration
            heappush(heap, -duration)
            ans += 1
            
            if curTime > lastDay and heap:
                top = -heappop(heap)
                curTime -= top
                ans -= 1
            
        return ans