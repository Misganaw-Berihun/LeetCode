class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        offset = 10_000
        memo = [0 for i in range(2 * offset + 2)]
        for num in nums:
            memo[num + offset] += 1
        
        cnt = 0
        for i in range(2 * offset + 1, -1, -1):
            if memo[i] > 0:
                cnt += memo[i]
            
            if cnt >= k:
                return (i - offset)
        
            