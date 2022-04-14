class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        temp = []
        points.sort()
        if points[0][1] >= points[1][0]:
            temp.append([max(points[0][0], points[1][0]), 
                                        min(points[0][1], points[1][1])])
        else:
            temp.append(points[0])
            temp.append(points[1])
        
        for i in range(2, len(points)):
            if points[i][0] > temp[-1][1]:
                temp.append(points[i])
            else:
                temp[-1][0] = max(points[i][0], temp[-1][0])
                temp[-1][1] = min(points[i][1], temp[-1][1])
                
        return len(temp)
            
        
        