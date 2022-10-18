class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        nice_subarrays = 0
        prefix[0] = 1
        cur = 0
        
        for idx in range(len(nums)):
            if nums[idx] % 2:
                cur += 1
            
            diff = cur - k
            if diff in prefix:
                nice_subarrays += prefix[diff]
                
            prefix[cur] += 1
        
        return nice_subarrays
#[0,1,1,0,1,1]
#[0,1,2,2,3,3]