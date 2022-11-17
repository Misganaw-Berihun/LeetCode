class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = ceil(sqrt(c))
         
        while l <= r:
            add = l * l + r * r
            if add == c:
                return True
            elif add > c:
                r -= 1
            else:
                l += 1
        
        return False