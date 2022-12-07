# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSum(self, rt, low, high):
        if not rt:
            return 0
        left = self.rangeSum(rt.left, low, high)
        right = self.rangeSum(rt.right, low, high)
        
        add = 0
        if low <= rt.val <= high:
            add = rt.val
        
        return left + right + add
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.rangeSum(root, low, high)
        