class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        ans = 0
        while xor:
            ans += 1
            xor = xor & (xor - 1)

        return ans
        