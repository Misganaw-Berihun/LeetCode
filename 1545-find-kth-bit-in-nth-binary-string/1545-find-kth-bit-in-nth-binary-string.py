class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(N,K):
            if N == 1:
                return "0"

            i = (2 ** N - 1) // 2 

            if K == i:
                return "1"
            elif K < i:
                return rec(N-1,K)
            else:
                l = 2 **N - 1
                temp = rec(N-1,l-K-1)
                if temp == "0":
                    return "1"
                else:
                    return "0"
        
        return rec(n,k-1)