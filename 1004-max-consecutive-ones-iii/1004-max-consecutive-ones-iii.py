class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        queue = deque()
        ans = 0
        idx = 0
        zeros = 0
        
        for i,v in enumerate(nums):
            if v == 0:
                queue.append(i)
                zeros += 1
                
            if zeros > k :
                ans = max(i - idx,ans)
                
                idx = queue.popleft() + 1
                
                zeros -= 1
                
        ans = max(ans , len(nums) - idx)
        
        return ans