class Solution:
    def countBits(self, n: int) -> List[int]:
        acc = [0] * (n+1)
        offset = 1

        for i in range(1,n+1):
            if i == 2*offset:
                offset *= 2
            
            dif = i - offset
            acc[i] = 1 + acc[dif]


        return acc
                    