class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        count[0] = 1
        
        cur = 0
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                cur += 1
            temp = (cur - k)
            ans += count[temp]
            count[cur] += 1
            
        return ans
            