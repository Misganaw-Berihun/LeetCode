class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 0
        size = len(points)
        
        for i in range(size):
            x, y = points[i]
            count = defaultdict(int)
            cur_max_points = 0
            
            for j in range(size):
                new_x, new_y = points[j]
                if i != j:
                    slope = inf
                    if new_x != x:
                        slope = (new_y - y) / (new_x - x)
                    
                    count[slope] += 1
                    cur_max_points = max(count[slope], cur_max_points)
                    
            max_points = max(cur_max_points, max_points)
        
        return max_points + 1
        