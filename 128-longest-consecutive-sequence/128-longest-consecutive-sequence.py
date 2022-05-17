class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        occur, cur_streak, longest_streak = set(nums), 0, 0
        for num in nums:
            if num - 1 not in occur:
                cur = num
                cur_streak = 1
                
                while cur + 1 in occur:
                    cur = cur + 1
                    cur_streak += 1
                    
                longest_streak = max(longest_streak, cur_streak)
                
        return longest_streak        