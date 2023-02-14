class Solution:        
    def reorderedPowerOf2(self, n: int) -> bool:
        c1 = Counter(str(n))
        
        for i in range(32):
            p = 1 << i
            c2 = Counter(str(p))
            
            if c1 == c2:
                return True
        
        return False