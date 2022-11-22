class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_len = len(s)
        ans = [[] for i in range(numRows)]
        
        idx = 0
        step = 1
        
        if numRows == 1:
            return s
        
        for ch in s:
            ans[idx].append(ch)
            if idx == numRows - 1:
                step = -1
            if idx == 0:
                step = 1
            idx += step
        
        res = ''
        for i in range(numRows):
            res += ''.join(ans[i])
        
        return res