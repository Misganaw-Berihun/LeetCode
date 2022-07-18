class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        prev = [0 for i in range(N + 1)]
        for i in range(1, M + 1):
            cur = [0 for i in range(N + 1)]
            for j in range(1, N + 1):
                if text1[j-1] == text2[i-1]:
                    cur[j] = prev[j-1] + 1
                else:
                    cur[j] = max(cur[j-1], prev[j])
            prev = cur
        return cur[N]
        