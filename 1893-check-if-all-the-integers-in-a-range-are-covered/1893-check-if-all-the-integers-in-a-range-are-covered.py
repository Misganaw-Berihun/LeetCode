class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        N = len(ranges)
        ranges.sort()
        for i in range(N):
            while ranges[i][0] <= left and left <= ranges[i][1]:
                left += 1
            
            if left > right:
                return True
        return False
        