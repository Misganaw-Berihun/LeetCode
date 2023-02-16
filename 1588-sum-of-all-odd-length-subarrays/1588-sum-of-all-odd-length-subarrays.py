class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0 for i in range(n + 1)]
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + arr[i - 1]
        
        ans = 0
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -2):
                ans += (prefix[i] - prefix[j])
        
        return ans