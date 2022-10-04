class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1 for i in range(n)]
        stk = []
        for i in range(2 * n - 1):
            idx = i % n
            while stk and nums[stk[-1]] < nums[idx]:
                top = stk.pop()
                ans[top] = nums[idx]
            stk.append(idx)
        return ans