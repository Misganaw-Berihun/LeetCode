class Solution:        
    def findDigits(self, num, digits):
        while num > 0:
            digits.append(num % 10)
            num //= 10
        
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = []
        self.findDigits(n, digits)
        count = Counter(digits)
        
        for i in range(32):
            p = 1 << i
            digits = []
            self.findDigits(p, digits)
            count2 = Counter(digits)
            
            ok = True
            for key in count:
                if count[key] != count2[key]:
                    ok = False
            
            for key in count2:
                if count[key] != count2[key]:
                    ok = False
            
            if ok:
                return ok
        
        return False