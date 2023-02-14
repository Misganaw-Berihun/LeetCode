class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_cnt = 0
        b_cnt = 0
        
        for ch in s:
            if ch == 'a':
                a_cnt += 1
        
        b_cnt = (n - a_cnt)
        ans = min(b_cnt, a_cnt)
        a = 0
        
        for i in range(n):
            if s[i] == 'a':
                a += 1
            
            b = (i + 1 - a)
            temp = (a_cnt - a)
            ans = min(b + temp, ans)
        
        return ans
            