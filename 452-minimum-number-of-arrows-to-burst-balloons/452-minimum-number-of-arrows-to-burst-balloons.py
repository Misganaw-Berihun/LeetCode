class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort()
        start, end = points[0][0], points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                start, end = points[i]
                ans += 1
            else:
                start = max(points[i][0], start)
                end = min(points[i][1], end)
        return ans
            
        
        