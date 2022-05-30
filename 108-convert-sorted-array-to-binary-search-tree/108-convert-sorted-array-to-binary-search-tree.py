# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
            nonlocal n
            if left > right:
                    return None
            mid = (left + right) // 2
            rt = TreeNode(nums[mid], construct(left, mid - 1), construct(mid + 1, right));
            return rt
        n = len(nums)
        return construct(0, n - 1)