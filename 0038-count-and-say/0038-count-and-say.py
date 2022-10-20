class Solution:
    def count(self, digit_str):
        i = 0
        cnt = []
        while i < len(digit_str):
            j = i + 1
            while j < len(digit_str) and digit_str[i] == digit_str[j]:
                j += 1
            
            cnt.append(str(j - i))
            cnt.append(digit_str[i])
            i = j
        return ''.join(cnt)
    
    def countAndSay(self, n: int) -> str:
        cur = "1"
        
        for i in range(n-1):
            cur = self.count(cur)
        
        return cur