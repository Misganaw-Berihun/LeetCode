class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            count = 0
            while i != 0:
                count += i & 1
                i >>= 1
                
            answer.append(count)
        return answer