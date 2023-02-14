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
            
            if count == count2:
                return True
        
        return False