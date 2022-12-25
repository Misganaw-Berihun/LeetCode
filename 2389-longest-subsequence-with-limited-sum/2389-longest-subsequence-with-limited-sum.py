class Solution:
    def binary_search(self, prefix, target):
        left = 0
        right = len(prefix)
        
        while left + 1 < right:
            mid = left + (right - left)//2
            
            if prefix[mid] <= target:
                left = mid
            else:
                right = mid
        
        return left
        
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        size = len(nums)
        q_size = len(queries)
        prefix = [0 for i in range(size + 1)]
        ans = [0 for i in range(q_size)]
        
        nums.sort()
        for i in range(1, size + 1):
            prefix[i] = (prefix[i-1] + nums[i - 1])
            
        for j in range(q_size):
            ans[j] = self.binary_search(prefix, queries[j])
            
        return ans