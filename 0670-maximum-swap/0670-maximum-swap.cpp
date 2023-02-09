class Solution:
    def getDigits(self, num):
        digits = []
        
        while num > 0:
            digits.append(num % 10)
            num //= 10
        
        return digits[::-1]
        
    def findNum(self, digits):
        num = 0
        
        for d in digits:
            num = num * 10 + d
        
        return num
        
    def swap(self, i, j, digits):
        digits[i], digits[j] = digits[j], digits[i]
        
    def maximumSwap(self, num: int) -> int:
        digits = self.getDigits(num)
        length = len(digits)
        ans = num
    
        for i in range(length):
            for j in range(i + 1):
                self.swap(i, j, digits)
                temp = self.findNum(digits)
                self.swap(i, j, digits)
                ans = max(ans, temp)
                
        return ans