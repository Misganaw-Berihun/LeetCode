class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(count.keys())
        if 0 in count:
            return n - 1
        return n
        