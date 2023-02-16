class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        n = len(gain)
        ans = 0
        
        for i in range(n):
            height += gain[i]
            ans = max(ans, height)
        
        return ans