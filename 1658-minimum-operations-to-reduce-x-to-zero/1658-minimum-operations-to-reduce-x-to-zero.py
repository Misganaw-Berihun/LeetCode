class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        d[0] = -1
        target = sum(nums) - x
        cur = 0
        ans = inf
        
        if target == 0:
            return n
            
        for i in range(n):
            cur += nums[i]
            temp = cur - target
       
            if temp in d:
                ans = min(ans, d[temp] + n - i)
            
            if cur not in d:
                d[cur] = i
        
        if ans == inf:
            ans = -1
            
        return ans