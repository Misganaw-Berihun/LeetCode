class Solution:
    def concatenatedBinary(self, n: int) -> int:
        shift, res = 0, 0
        mod = 1000000007
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                shift += 1
            res = ((res << shift) | i) % mod
        return res