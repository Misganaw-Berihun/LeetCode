class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        prev = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for k in range(1, length + 1):
            cur = [[0 for i in range(n + 1)] for j in range(m + 1)] 
            one_cnt = strs[k - 1].count("1")
            zero_cnt = len(strs[k - 1]) - one_cnt
            for j in range(m + 1):
                for i in range(n + 1):
                        include = float('-inf')
                        if i - one_cnt >= 0 and j - zero_cnt >= 0:
                            include = 1 + prev[j - zero_cnt][i - one_cnt]
                        exclude = prev[j][i]
                        cur[j][i] = max(include, exclude)
            prev = cur
        return cur[m][n]
    
        