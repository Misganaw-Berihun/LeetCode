class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort()
        temp = [points[0]]
        for i in range(1, len(points)):
            if points[i][0] > temp[-1][1]:
                temp.append(points[i])
            else:
                temp[-1][0] = max(points[i][0], temp[-1][0])
                temp[-1][1] = min(points[i][1], temp[-1][1])
        return len(temp)
            
        
        