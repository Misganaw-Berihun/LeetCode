class Solution:
    def binary_search(self, prefix, target):
        left = 0
        right = len(prefix) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if prefix[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
        
        
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = [0]
        nums.sort()
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        answer = []
        
        for j in range(len(queries)):
            res = self.binary_search(prefix, queries[j])
            answer.append(res)
            
        return answer