class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        return xor.bit_count()
        