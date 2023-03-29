class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            count = 0
            for j in range(32):
                if ((1 << j) & i) > 0:
                    count += 1
            answer.append(count)
        return answer