class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
            if fast == slow:
                break
            
        slow = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
            
        return slow
        