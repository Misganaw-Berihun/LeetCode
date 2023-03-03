class Solution:
    def mySqrt(self, x: int) -> int:
        l = -1
        r = x + 1
        
        while l + 1 < r:
            m = (l + r) // 2
            
            if m * m <= x:
                l = m
            else:
                r = m
        
        return l
        