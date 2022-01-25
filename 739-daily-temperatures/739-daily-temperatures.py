class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                p = stack.pop()
                ans[p[1]] = i - p[1]
            stack.append((t,i))
        
        return ans
        