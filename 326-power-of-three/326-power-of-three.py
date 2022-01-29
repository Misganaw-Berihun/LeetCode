class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 3:
            return n == 3 or n == 1;
        elif n % 3 != 0:
            return False
        
        return self.isPowerOfThree(n/3)
        