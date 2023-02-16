class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        nums.sort()
        
        prefix = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        ans = []
        for i in range(m):
            j = n 
            
            while j > 0 and prefix[j] > queries[i]:
                j -= 1
            
            ans.append(j)
        
        
        return ans
        