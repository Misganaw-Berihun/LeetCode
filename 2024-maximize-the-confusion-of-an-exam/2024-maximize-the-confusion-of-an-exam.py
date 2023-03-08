class Solution:
    def check(self, prefix, window, k):
        n = len(prefix)
        for i in range(window, n):
            num_trues = prefix[i] - prefix[i- window]
            num_falses = window - num_trues
            
            if num_trues <= k or num_falses <= k:
                return True
        
        return False
        
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left, right = -1, n + 1
        
        prefix = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + (answerKey[i-1] == "T")
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if self.check(prefix, mid, k):
                left = mid
            else:
                right = mid
        
        return left
        