class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        key = lambda a : (len(a), a)
        return sorted(nums, key = key)[-k]