class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        cur = 0
        remIndexOf = defaultdict(int)
        remIndexOf[0] = 0
        
        for i in range(N):
            cur += nums[i]
            rem = cur % k
            if rem not in remIndexOf:
                remIndexOf[rem] = i + 1
            elif remIndexOf[rem] < i:
                return True
            
        
        return False
        