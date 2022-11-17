class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        d = 0
        while d * d <= c:
            l = d
            r = c
            
            d_sq = d * d
            while l <= r:
                m = l + (r - l) // 2
                
                m_sq = m * m
                add = m_sq + d_sq
                if add == c:
                    return True
                
                elif (add > c):
                    r = m - 1
                
                else:
                    l = m + 1
            d += 1
    
        return False       