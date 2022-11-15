class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        i = n - 1
        
        while i == n - 1 or (i >= 0 and carry != 0):           
            carry = ((digits[i] + 1) // 10)
            digits[i] = (digits[i] + 1) % 10
            
            i -= 1
        
        return [1] * carry + digits