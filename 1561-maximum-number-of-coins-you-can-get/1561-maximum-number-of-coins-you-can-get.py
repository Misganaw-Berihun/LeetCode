class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left, right, ans =0, len(piles) - 2, 0
        while left <= right:
            ans += piles[right]
            left += 1
            right -= 2
        return ans
        