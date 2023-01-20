class Solution:        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        length = len(nums)
        
        def backtrack(cur, prev, path): 
            if cur >= length:
                if len(path) >= 2:
                    ans.add(tuple(path))
                return
            
            if nums[cur] >= prev:
                backtrack(cur + 1, nums[cur], path + [nums[cur]])
                
            backtrack(cur + 1, prev, path)
            
        backtrack(0, -101, [])
        return ans