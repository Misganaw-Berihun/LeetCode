class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stk = []
        n, m = len(s), len(part)
        
        for i in range(n):
            stk.append(s[i])
            
            if len(stk) >= m and ''.join(stk[-m:]) == part:
                j = 0
                while j < m:
                    stk.pop()
                    j += 1
            
        
        return ''.join(stk)