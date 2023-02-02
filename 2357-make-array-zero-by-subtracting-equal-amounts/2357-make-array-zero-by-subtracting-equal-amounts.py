class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(num_set)
        if 0 in num_set:
            return n - 1
        return n
        