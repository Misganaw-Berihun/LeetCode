class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        ans = [-1 for i in range(len(nums1))]
        dict = defaultdict(int)
        for i in range(len(nums2)):
            while stk and stk[-1] < nums2[i]:
                top = stk.pop()
                dict[top] = nums2[i]
            stk.append(nums2[i])
        
        for i in range(len(nums1)):
            if nums1[i] in dict:
                ans[i] = dict[nums1[i]]
        
        return ans