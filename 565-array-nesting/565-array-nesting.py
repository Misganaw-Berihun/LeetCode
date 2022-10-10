class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        ans = 0
        def dfs(n):
            if n in visited:
                return 0
            
            visited.add(n)
            return 1 + dfs(nums[n])
    
        for num in nums:
            if num not in visited:
                ans = max(ans, dfs(num))
        
        return ans
        