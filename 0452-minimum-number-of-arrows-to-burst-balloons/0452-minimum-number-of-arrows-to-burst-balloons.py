class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        size = len(points)
        points.sort(key = lambda a: a[1])
        arrow_cnt = 1
        cur_end = points[0][1]
        
        for i in range(size):
            if points[i][0] > cur_end:
                arrow_cnt += 1
                cur_end = points[i][1]
        
        return arrow_cnt