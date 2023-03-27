from sortedcontainers import *
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = SortedList()
        ans = 0
        
        for a, b in zip(nums1, nums2):
            ans += arr.bisect_right(a - b + diff)
            arr.add(a - b)
        return ans