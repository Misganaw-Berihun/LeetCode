class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        visited = set()
        nums.sort()
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in visited:
                visited.add(nums[i])
                
            if len(visited) == 3:
                return nums[i]
            
        return nums[-1]
        