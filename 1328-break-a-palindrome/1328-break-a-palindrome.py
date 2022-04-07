class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        result = ""
        if n == 1:
            return ""
        
        for i in range(n):
            if n % 2  and i == n // 2:
                result += palindrome[i]
                continue
            if palindrome[i] != 'a' :
                result += 'a'
                return result + palindrome[i + 1:]
            else:
                if i == n - 1:
                    result += 'b'
                else:
                    result += palindrome[i]
        return result
                
                
        
            
        