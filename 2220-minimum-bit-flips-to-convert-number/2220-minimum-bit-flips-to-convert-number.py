class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        ans = 0
        while xor != 0:
            if xor & 1 > 0:
                ans += 1
            xor = xor >> 1

        return ans
        