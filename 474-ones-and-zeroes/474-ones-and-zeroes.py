class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        cur = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for k in range(length):
            one_cnt = strs[k].count("1")
            zero_cnt = len(strs[k]) - one_cnt
            for j in range(m, zero_cnt - 1, -1):
                for i in range(n, one_cnt - 1, -1):
                        include = float('-inf')
                        if i - one_cnt >= 0 and j - zero_cnt >= 0:
                            include = 1 + cur[j - zero_cnt][i - one_cnt]
                        exclude = cur[j][i]
                        cur[j][i] = max(include, exclude)
        return cur[m][n]
    
        