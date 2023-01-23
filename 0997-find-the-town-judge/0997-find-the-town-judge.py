class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = defaultdict(int)
        trust_count = defaultdict(int)
        for src, end in trust:
            trusted_count[end] += 1
            trust_count[src] += 1
        
        for i in range(1, n + 1):
            if trusted_count[i] == n - 1 and trust_count[i] == 0:
                return i
        
        return -1
        
        