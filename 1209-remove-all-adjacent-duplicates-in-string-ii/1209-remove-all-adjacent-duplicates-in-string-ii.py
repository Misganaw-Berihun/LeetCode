class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        ans = ""
        for i in range(len(s)):
            if len(stk) == 0 or stk[-1][0] != s[i]:
                stk.append((s[i], 1))
            else:
                p = stk.pop()
                if p[1] != k - 1:
                    stk.append((s[i], p[1] + 1))
        
        while stk:
            p = stk.pop()
            ans = p[0] * p[1] + ans
            
        return ans
                
        