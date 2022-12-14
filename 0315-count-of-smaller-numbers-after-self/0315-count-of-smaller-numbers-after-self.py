class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        tmp = []
        N  = len(nums)
        for i in range(N - 1, -1 , -1):
            idx = bisect_left(tmp, nums[i])
            ans.append(idx)
            tmp.insert(idx, nums[i])
        
        return ans[::-1]
        