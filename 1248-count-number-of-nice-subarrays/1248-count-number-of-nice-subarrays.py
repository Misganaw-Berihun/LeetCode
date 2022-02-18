class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        visited = defaultdict(int)
        visited[0] = 1
        ans = 0
                
        for i,val in enumerate(nums):
            nums[i] = 1 if val %2 else 0
            
        for j in range(1,len(nums)):
            nums[j] = nums[j-1] + nums[j]
            
        for v in nums:
            temp = visited.get(v-k)
        
            if temp:
                ans += temp
                
            visited[v] += 1
            
        return ans
             
            
            
            
            
            
        