class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'A', 'E', 'e', 'o', 'O', 'u', 'U', 'i','I'}
        left = 0
        right = len(s) - 1
        left_cnt = 0
        right_cnt = 0
        
        while left < right:
            if s[left] in vowels:
                left_cnt += 1
            
            if s[right] in vowels:
                right_cnt += 1
            
            left += 1
            right -= 1
        
        return left_cnt == right_cnt