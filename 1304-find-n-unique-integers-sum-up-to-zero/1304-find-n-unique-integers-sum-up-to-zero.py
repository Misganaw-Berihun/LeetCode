class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        num = 0
        for i in range(1, n):
            ans.append(-i)
            num += i
        
        ans.append(num)
        return ans