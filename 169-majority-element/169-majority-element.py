class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for i,v in count.items():
            if v > len(nums) // 2:
                return i
        