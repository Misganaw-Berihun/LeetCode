class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        max_pos = 0
        can_jump = True
        i = 0
        
        while can_jump and i < size:
            max_pos = max(max_pos, i + nums[i])
            if i >= max_pos:
                can_jump = False
            i += 1
        
        return max_pos >= (size - 1)
        