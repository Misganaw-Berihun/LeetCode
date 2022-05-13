class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)
        s = (s.lstrip('0b')[::-1])
        s = s + (32 - len(s)) * '0'
        return int(s , 2)