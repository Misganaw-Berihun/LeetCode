class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        indices = defaultdict(int)
        ans = 0
        indices[-1] = -1
        total = -1
        
        for i in range(n):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1
            
            if total in indices:
                ans = max(ans, i - indices[total])
            else:
                indices[total] = i
        
        return ans