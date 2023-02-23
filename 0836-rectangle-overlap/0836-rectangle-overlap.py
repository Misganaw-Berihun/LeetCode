class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        x3, y3, x4, y4 = rec2[0], rec2[1], rec2[2], rec2[3]
        
        x1 = max(x1, x3)
        x2 = min(x2, x4)
        y1 = max(y1, y3)
        y2 = min(y2, y4)
        
        ans = False
        if x1 < x2 and y1 < y2:
            ans = True
        
        return ans
        